#!/usr/bin/env python3

# Based from https://github.com/thought-machine/pleasings/blob/da6986c1ad4fe1a742812cf867775d9f55694f28/js/yarn_deps.py

"""Module to take yarn's output and rewrite it into BUILD rules."""

import json
import sys


NO_DEPS_NO_SCOPE_TEMPLATE = """
yarn_library(
    name = "%s",
    package_name = "%s",
    version = "%s",
)
"""

NO_DEPS_SCOPE_TEMPLATE = """
yarn_library(
    name = "%s",
    package_name = "%s",
    scope = "%s",
    version = "%s",
)
"""

DEPS_NO_SCOPE_TEMPLATE = """
yarn_library(
    name = "%s",
    package_name = "%s",
    version = "%s",
    deps = [
%s    ],
)
"""

DEPS_SCOPE_TEMPLATE = """
yarn_library(
    name = "%s",
    package_name = "%s",
    scope = "%s",
    version = "%s",
    deps = [
%s    ],
)
"""


def parse_name(item):
    if item['name'][0] == '@':
        fqn, _, version = item['name'][1:].partition('@')
        fqn = "@" + fqn
    else:
        fqn, _, version = item['name'].partition('@')

    scope, found, name = fqn.partition('/')
    fqn = fqn.replace("/", "--")

    if found:
        return (fqn, scope, name, version)

    return (fqn, name, scope, version)


def read_deps(items):
    for item in items:
        fqn, scope, name, version = parse_name(item)
        deps = [parse_name(child)[0] for child in item.get('children', [])]
        yield fqn, (scope, name, version, deps)


def fix_deps(fqn, data, seen=frozenset()):
    seen = seen | {fqn}
    scope, name, version, deps = data[fqn]
    deps = [fix_deps(dep, data, seen) for dep in deps if dep not in seen]
    data[fqn] = (scope, name, version, deps)
    return fqn


def main():
    data = json.load(sys.stdin)
    items = dict(read_deps(data['data']['trees']))

    # This is a little ugly; we need to restrict circular dependencies, which means we have to do
    # it top-down, but the only thing giving us reliable information about where the top of the
    # tree is is the color property.
    for item in data['data']['trees']:
        if item.get('color') == 'bold':
            fix_deps(parse_name(item)[0], items)

    for fqn, (scope, name, version, deps) in sorted(items.items()):
        if deps:
            if scope:
                sys.stdout.write(DEPS_SCOPE_TEMPLATE % (fqn, name, scope, version, ''.join("        \":%s\",\n" % dep for dep in deps)))
            else:
                sys.stdout.write(DEPS_NO_SCOPE_TEMPLATE % (fqn, name, version, ''.join("        \":%s\",\n" % dep for dep in deps)))
        else:
            if scope:
                sys.stdout.write(NO_DEPS_SCOPE_TEMPLATE % (fqn, name, scope, version))
            else:
                sys.stdout.write(NO_DEPS_NO_SCOPE_TEMPLATE % (fqn, name, version))


if __name__ == '__main__':
    main()
