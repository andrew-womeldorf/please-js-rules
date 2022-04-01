# Javascript Rules for Please.Build

This repo is a plugin that provides OpenAPI rules for the
[Please](https://please.build) build system.

Follow the example set by projects in
[github.com/please-build](https://github.com/please-build), and
[docs](https://please.build/config.html#plugindefinition).

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

## Configuration

This plugin can be configured via the plugins section as follows:

```
[Plugin "please_js"]
SomeConfig = some-value
```
