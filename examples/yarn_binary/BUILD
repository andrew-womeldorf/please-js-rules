package(default_visibility = ["PUBLIC"])

subinclude("//build_defs:js")

yarn_library(
    name = "@redocly--ajv",
    package_name = "ajv",
    scope = "@redocly",
    version = "8.6.4",
    deps = [
        ":fast-deep-equal",
        ":json-schema-traverse",
        ":require-from-string",
        ":uri-js",
    ],
)

yarn_library(
    name = "@redocly--openapi-cli",
    package_name = "openapi-cli",
    scope = "@redocly",
    version = "1.0.0-beta.91",
    deps = [
        ":@redocly--openapi-core",
        ":@types--node",
        ":assert-node-version",
        ":chokidar",
        ":colorette",
        ":glob",
        ":glob-promise",
        ":handlebars",
        ":portfinder",
        ":simple-websocket",
        ":yargs",
    ],
)

yarn_library(
    name = "@redocly--openapi-core",
    package_name = "openapi-core",
    scope = "@redocly",
    version = "1.0.0-beta.91",
    deps = [
        ":@redocly--ajv",
        ":@types--node",
        ":colorette",
        ":js-levenshtein",
        ":js-yaml",
        ":lodash.isequal",
        ":minimatch",
        ":node-fetch",
        ":pluralize",
        ":yaml-ast-parser",
    ],
)

yarn_library(
    name = "@types--glob",
    package_name = "glob",
    scope = "@types",
    version = "7.2.0",
    deps = [
        ":@types--minimatch",
        ":@types--node",
    ],
)

yarn_library(
    name = "@types--minimatch",
    package_name = "minimatch",
    scope = "@types",
    version = "3.0.5",
)

yarn_library(
    name = "@types--node",
    package_name = "node",
    scope = "@types",
    version = "17.0.23",
)

yarn_library(
    name = "ansi-regex",
    package_name = "ansi-regex",
    version = "5.0.1",
)

yarn_library(
    name = "ansi-styles",
    package_name = "ansi-styles",
    version = "4.3.0",
    deps = [
        ":color-convert",
    ],
)

yarn_library(
    name = "anymatch",
    package_name = "anymatch",
    version = "3.1.2",
    deps = [
        ":normalize-path",
        ":picomatch",
    ],
)

yarn_library(
    name = "argparse",
    package_name = "argparse",
    version = "2.0.1",
)

yarn_library(
    name = "assert-node-version",
    package_name = "assert-node-version",
    version = "1.0.3",
    deps = [
        ":expected-node-version",
        ":semver",
    ],
)

yarn_library(
    name = "async",
    package_name = "async",
    version = "2.6.3",
    deps = [
        ":lodash",
    ],
)

yarn_library(
    name = "balanced-match",
    package_name = "balanced-match",
    version = "1.0.2",
)

yarn_library(
    name = "binary-extensions",
    package_name = "binary-extensions",
    version = "2.2.0",
)

yarn_library(
    name = "brace-expansion",
    package_name = "brace-expansion",
    version = "1.1.11",
    deps = [
        ":balanced-match",
        ":concat-map",
    ],
)

yarn_library(
    name = "braces",
    package_name = "braces",
    version = "3.0.2",
    deps = [
        ":fill-range",
    ],
)

yarn_library(
    name = "chokidar",
    package_name = "chokidar",
    version = "3.5.3",
    deps = [
        ":anymatch",
        ":braces",
        ":glob-parent",
        ":is-binary-path",
        ":is-glob",
        ":normalize-path",
        ":readdirp",
        ":fsevents",
    ],
)

yarn_library(
    name = "cliui",
    package_name = "cliui",
    version = "7.0.4",
    deps = [
        ":string-width",
        ":strip-ansi",
        ":wrap-ansi",
    ],
)

yarn_library(
    name = "color-convert",
    package_name = "color-convert",
    version = "2.0.1",
    deps = [
        ":color-name",
    ],
)

yarn_library(
    name = "color-name",
    package_name = "color-name",
    version = "1.1.4",
)

yarn_library(
    name = "colorette",
    package_name = "colorette",
    version = "1.4.0",
)

yarn_library(
    name = "concat-map",
    package_name = "concat-map",
    version = "0.0.1",
)

yarn_library(
    name = "debug",
    package_name = "debug",
    version = "4.3.4",
    deps = [
        ":ms",
    ],
)

yarn_library(
    name = "emoji-regex",
    package_name = "emoji-regex",
    version = "8.0.0",
)

yarn_library(
    name = "escalade",
    package_name = "escalade",
    version = "3.1.1",
)

yarn_library(
    name = "expected-node-version",
    package_name = "expected-node-version",
    version = "1.0.2",
)

yarn_library(
    name = "fast-deep-equal",
    package_name = "fast-deep-equal",
    version = "3.1.3",
)

yarn_library(
    name = "fill-range",
    package_name = "fill-range",
    version = "7.0.1",
    deps = [
        ":to-regex-range",
    ],
)

yarn_library(
    name = "fs.realpath",
    package_name = "fs.realpath",
    version = "1.0.0",
)

yarn_library(
    name = "fsevents",
    package_name = "fsevents",
    version = "2.3.2",
)

yarn_library(
    name = "get-caller-file",
    package_name = "get-caller-file",
    version = "2.0.5",
)

yarn_library(
    name = "glob",
    package_name = "glob",
    version = "7.2.0",
    deps = [
        ":fs.realpath",
        ":inflight",
        ":inherits",
        ":minimatch",
        ":once",
        ":path-is-absolute",
    ],
)

yarn_library(
    name = "glob-parent",
    package_name = "glob-parent",
    version = "5.1.2",
    deps = [
        ":is-glob",
    ],
)

yarn_library(
    name = "glob-promise",
    package_name = "glob-promise",
    version = "3.4.0",
    deps = [
        ":@types--glob",
    ],
)

yarn_library(
    name = "handlebars",
    package_name = "handlebars",
    version = "4.7.7",
    deps = [
        ":minimist",
        ":neo-async",
        ":source-map",
        ":wordwrap",
        ":uglify-js",
    ],
)

yarn_library(
    name = "inflight",
    package_name = "inflight",
    version = "1.0.6",
    deps = [
        ":once",
        ":wrappy",
    ],
)

yarn_library(
    name = "inherits",
    package_name = "inherits",
    version = "2.0.4",
)

yarn_library(
    name = "is-binary-path",
    package_name = "is-binary-path",
    version = "2.1.0",
    deps = [
        ":binary-extensions",
    ],
)

yarn_library(
    name = "is-extglob",
    package_name = "is-extglob",
    version = "2.1.1",
)

yarn_library(
    name = "is-fullwidth-code-point",
    package_name = "is-fullwidth-code-point",
    version = "3.0.0",
)

yarn_library(
    name = "is-glob",
    package_name = "is-glob",
    version = "4.0.3",
    deps = [
        ":is-extglob",
    ],
)

yarn_library(
    name = "is-number",
    package_name = "is-number",
    version = "7.0.0",
)

yarn_library(
    name = "js-levenshtein",
    package_name = "js-levenshtein",
    version = "1.1.6",
)

yarn_library(
    name = "js-yaml",
    package_name = "js-yaml",
    version = "4.1.0",
    deps = [
        ":argparse",
    ],
)

yarn_library(
    name = "json-schema-traverse",
    package_name = "json-schema-traverse",
    version = "1.0.0",
)

yarn_library(
    name = "lodash",
    package_name = "lodash",
    version = "4.17.21",
)

yarn_library(
    name = "lodash.isequal",
    package_name = "lodash.isequal",
    version = "4.5.0",
)

yarn_library(
    name = "minimatch",
    package_name = "minimatch",
    version = "3.1.2",
    deps = [
        ":brace-expansion",
    ],
)

yarn_library(
    name = "minimist",
    package_name = "minimist",
    version = "1.2.6",
)

yarn_library(
    name = "mkdirp",
    package_name = "mkdirp",
    version = "0.5.6",
    deps = [
        ":minimist",
    ],
)

yarn_library(
    name = "ms",
    package_name = "ms",
    version = "2.1.2",
)

yarn_library(
    name = "neo-async",
    package_name = "neo-async",
    version = "2.6.2",
)

yarn_library(
    name = "node-fetch",
    package_name = "node-fetch",
    version = "2.6.7",
    deps = [
        ":whatwg-url",
    ],
)

yarn_library(
    name = "normalize-path",
    package_name = "normalize-path",
    version = "3.0.0",
)

yarn_library(
    name = "once",
    package_name = "once",
    version = "1.4.0",
    deps = [
        ":wrappy",
    ],
)

yarn_library(
    name = "path-is-absolute",
    package_name = "path-is-absolute",
    version = "1.0.1",
)

yarn_library(
    name = "picomatch",
    package_name = "picomatch",
    version = "2.3.1",
)

yarn_library(
    name = "pluralize",
    package_name = "pluralize",
    version = "8.0.0",
)

yarn_library(
    name = "portfinder",
    package_name = "portfinder",
    version = "1.0.28",
    deps = [
        ":async",
        ":debug",
        ":mkdirp",
    ],
)

yarn_library(
    name = "punycode",
    package_name = "punycode",
    version = "2.1.1",
)

yarn_library(
    name = "queue-microtask",
    package_name = "queue-microtask",
    version = "1.2.3",
)

yarn_library(
    name = "randombytes",
    package_name = "randombytes",
    version = "2.1.0",
    deps = [
        ":safe-buffer",
    ],
)

yarn_library(
    name = "readable-stream",
    package_name = "readable-stream",
    version = "3.6.0",
    deps = [
        ":inherits",
        ":string_decoder",
        ":util-deprecate",
    ],
)

yarn_library(
    name = "readdirp",
    package_name = "readdirp",
    version = "3.6.0",
    deps = [
        ":picomatch",
    ],
)

yarn_library(
    name = "require-directory",
    package_name = "require-directory",
    version = "2.1.1",
)

yarn_library(
    name = "require-from-string",
    package_name = "require-from-string",
    version = "2.0.2",
)

yarn_library(
    name = "safe-buffer",
    package_name = "safe-buffer",
    version = "5.2.1",
)

yarn_library(
    name = "semver",
    package_name = "semver",
    version = "5.7.1",
)

yarn_library(
    name = "simple-websocket",
    package_name = "simple-websocket",
    version = "9.1.0",
    deps = [
        ":debug",
        ":queue-microtask",
        ":randombytes",
        ":readable-stream",
        ":ws",
    ],
)

yarn_library(
    name = "source-map",
    package_name = "source-map",
    version = "0.6.1",
)

yarn_library(
    name = "string-width",
    package_name = "string-width",
    version = "4.2.3",
    deps = [
        ":emoji-regex",
        ":is-fullwidth-code-point",
        ":strip-ansi",
    ],
)

yarn_library(
    name = "string_decoder",
    package_name = "string_decoder",
    version = "1.3.0",
    deps = [
        ":safe-buffer",
    ],
)

yarn_library(
    name = "strip-ansi",
    package_name = "strip-ansi",
    version = "6.0.1",
    deps = [
        ":ansi-regex",
    ],
)

yarn_library(
    name = "to-regex-range",
    package_name = "to-regex-range",
    version = "5.0.1",
    deps = [
        ":is-number",
    ],
)

yarn_library(
    name = "tr46",
    package_name = "tr46",
    version = "0.0.3",
)

yarn_library(
    name = "uglify-js",
    package_name = "uglify-js",
    version = "3.15.3",
)

yarn_library(
    name = "uri-js",
    package_name = "uri-js",
    version = "4.4.1",
    deps = [
        ":punycode",
    ],
)

yarn_library(
    name = "util-deprecate",
    package_name = "util-deprecate",
    version = "1.0.2",
)

yarn_library(
    name = "webidl-conversions",
    package_name = "webidl-conversions",
    version = "3.0.1",
)

yarn_library(
    name = "whatwg-url",
    package_name = "whatwg-url",
    version = "5.0.0",
    deps = [
        ":tr46",
        ":webidl-conversions",
    ],
)

yarn_library(
    name = "wordwrap",
    package_name = "wordwrap",
    version = "1.0.0",
)

yarn_library(
    name = "wrap-ansi",
    package_name = "wrap-ansi",
    version = "7.0.0",
    deps = [
        ":ansi-styles",
        ":string-width",
        ":strip-ansi",
    ],
)

yarn_library(
    name = "wrappy",
    package_name = "wrappy",
    version = "1.0.2",
)

yarn_library(
    name = "ws",
    package_name = "ws",
    version = "7.5.7",
)

yarn_library(
    name = "y18n",
    package_name = "y18n",
    version = "5.0.8",
)

yarn_library(
    name = "yaml-ast-parser",
    package_name = "yaml-ast-parser",
    version = "0.0.43",
)

yarn_library(
    name = "yargs",
    package_name = "yargs",
    version = "17.0.1",
    deps = [
        ":cliui",
        ":escalade",
        ":get-caller-file",
        ":require-directory",
        ":string-width",
        ":y18n",
        ":yargs-parser",
    ],
)

yarn_library(
    name = "yargs-parser",
    package_name = "yargs-parser",
    version = "20.2.9",
)

yarn_binary(
    name = "openapi-cli",
    bin_name = "openapi",
    package = ":@redocly--openapi-cli",
    deps = [
        ":ansi-regex",
        ":ansi-styles",
        ":anymatch",
        ":argparse",
        ":assert-node-version",
        ":async",
        ":balanced-match",
        ":binary-extensions",
        ":brace-expansion",
        ":braces",
        ":chokidar",
        ":cliui",
        ":color-convert",
        ":colorette",
        ":color-name",
        ":concat-map",
        ":debug",
        ":emoji-regex",
        ":escalade",
        ":expected-node-version",
        ":fast-deep-equal",
        ":fill-range",
        ":fsevents",
        ":fs.realpath",
        ":get-caller-file",
        ":glob",
        ":glob-parent",
        ":glob-promise",
        ":handlebars",
        ":inflight",
        ":inherits",
        ":is-binary-path",
        ":is-extglob",
        ":is-fullwidth-code-point",
        ":is-glob",
        ":is-number",
        ":js-levenshtein",
        ":json-schema-traverse",
        ":js-yaml",
        ":lodash",
        ":lodash.isequal",
        ":minimatch",
        ":minimist",
        ":mkdirp",
        ":ms",
        ":neo-async",
        ":node-fetch",
        ":normalize-path",
        ":once",
        ":path-is-absolute",
        ":picomatch",
        ":pluralize",
        ":portfinder",
        ":punycode",
        ":queue-microtask",
        ":randombytes",
        ":readable-stream",
        ":readdirp",
        ":@redocly--ajv",
        ":@redocly--openapi-core",
        ":require-directory",
        ":require-from-string",
        ":safe-buffer",
        ":semver",
        ":simple-websocket",
        ":source-map",
        ":string_decoder",
        ":string-width",
        ":strip-ansi",
        ":to-regex-range",
        ":tr46",
        ":@types--glob",
        ":@types--minimatch",
        ":@types--node",
        ":uglify-js",
        ":uri-js",
        ":util-deprecate",
        ":webidl-conversions",
        ":whatwg-url",
        ":wordwrap",
        ":wrap-ansi",
        ":wrappy",
        ":ws",
        ":y18n",
        ":yaml-ast-parser",
        ":yargs",
        ":yargs-parser",
    ],
)
