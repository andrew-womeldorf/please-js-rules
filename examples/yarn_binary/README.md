# NPM Binary

Scenario: I want to use the [Redocly OpenAPI
CLI](https://github.com/Redocly/openapi-cli/tree/v1.0.0-beta.91/packages/cli) tool to
lint my OpenAPI Spec.

This is an NPM Package which defines a script at `.bin` in the
[package.json](https://github.com/Redocly/openapi-cli/blob/v1.0.0-beta.91/packages/cli/package.json#L6-L8).

## Steps

#### Create a package.json

*Use the `--flat` flag to resolve only one version of a dependency in the project.*

```bash
echo "{}" > package.json
yarn add --flat @redocly/openapi-cli
```

#### Create the libraries

```bash
yarn list --json | plz run //build_defs:yarn_to_please > BUILD
```

#### Create the binary

```bash
echo "" >> BUILD
plz run //build_defs:yarn_binary //examples/yarn_binary:@redocly--openapi-cli openapi-cli openapi >> BUILD
```

#### Try it!

```bash
plz run //examples/yarn_binary:openapi-cli -- --help
```
