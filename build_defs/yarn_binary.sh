#!/usr/bin/env bash
#
# Creates the yarn_binary rule for a runnable script in a yarn_library.
#
# This script assumes that your //third_party/js/BUILD file already contains a
# yarn_library for the package that contains the runnable script, and that all
# of the yarn_libraries that it depends on are already listed. In other words,
# this script assumes that you've already run the //build_defs:yarn_to_please
# script for a package :)
#
# The runnable script needs to be listed in the package's `package.json` under
# `.bin`. This key can be a string or an object. If it's an object, then
# `scriptName` must be equal to the key in the object containing the script you
# want to make a binary from. If it's a string, put anything here.
#
# For example, the relevant portion of the package.json in redoc-cli is
# https://github.com/Redocly/redoc/blob/v2.0.0-rc.66/cli/package.json#L6. In
# this case, you don't need to provide the `scriptName` argument to this script,
# because it's implicit.
#
# Here is the relevant portion of the package.json in @redocly/openapi-cli:
# https://github.com/Redocly/openapi-cli/blob/v1.0.0-beta.91/packages/cli/package.json#L6-L8.
# In this case, you need to set `scriptName` to `openapi`.
#
# Usage
#   plz run //build_defs:yarn_binary //target/of/yarn_library targetName [scriptName]
#
# Prints yarn_binary() to stdout. Redirect as neccessary.
#
# See //examples/yarn_binary


set -e

USAGE="<script> //target/of/yarn_library targetName [scriptName]"

if (( $# < 2 )); then
    >&2 echo "Not enough arguments: $USAGE"
    exit
fi

TARGET=$1
TARGETNAME=$2
SCRIPTNAME="${3:-$2}"

# Create a list of dependencies for the yarn_library.
# - Query deps for a rule. This includes nested deps.
# - Only keep the relative target name.
# - Discard the first result (self).
# - Remove duplicates
deps=$(plz query deps $TARGET \
    | cut -d ':' -f 2 \
    | tail -n +2 \
    | sort -u)

echo "yarn_binary("
echo "    name = \"$TARGETNAME\","
echo "    bin_name = \"$SCRIPTNAME\","
echo "    package = \":$(echo $TARGET | cut -d ':' -f 2)\","
echo "    deps = ["

for dep in $deps; do
    echo "        \":${dep}\","
done

echo "    ],"
echo ")"
