# Javascript Rules for Please.Build

This repo is a plugin that provides OpenAPI rules for the
[Please](https://please.build) build system.

Follow the example set by projects in
[github.com/please-build](https://github.com/please-build), and
[docs](https://please.build/config.html#plugindefinition).

These rules exist to fill in some gaps that I had with the JS rules in the
Pleasings repo:

- Scoped packages
- Generating the deps to support scoped packages
- Generating targets for scripts in packages

## Basic Usage

Include this plugin in your project:

```python
# BUILD
plugin_repo(
    name = "please-js",
    owner = "andrew-womeldorf",
    revision = "<Some git tag, commit, or other reference>",
)
```

Use it in a `BUILD` file:

```python
# some_dir/BUILD
subinclude("///please-js//build_defs:js")

yarn_library(
    name = "@types--node",
    package_name = "node",
    scope = "@types",
    version = "17.0.23",
)
```

**It's recommended to install packages with `yarn add --flat`, then use the
//build_defs:yarn_to_please script to generate the BUILD file.** Always use the
`--flat` option when adding packages with yarn, so that there's only one
version of a package.

## Configuration

This plugin can be configured via the plugins section as follows:

```
[Plugin "please_js"]
SomeConfig = some-value
```

## Other Javascript Rules

There's several existing JS rules, and I haven't seen a ton of documentation
around why they each exist, so I made my own which are VERY heavily based on
the existing JS rules in the Pleasings repo. See:

- [Pleasings: JS](https://github.com/thought-machine/pleasings/blob/master/js/js.build_defs)
- [Pleasings: Yarn](https://github.com/thought-machine/pleasings/blob/master/js/yarn.build_defs)
- [Tatskaari/please-js](https://github.com/Tatskaari/please-js) (uses ESBuild!)
