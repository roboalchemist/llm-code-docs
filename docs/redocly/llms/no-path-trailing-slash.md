# Source: https://redocly.com/docs/cli/rules/oas/no-path-trailing-slash.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/no-path-trailing-slash.md

# no-path-trailing-slash

Ensures that paths in your API do not end with a trailing slash (`/`).

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

Some web tooling (like mock servers, real servers, code generators, application frameworks, etc.) treats `example.com/foo` and `example.com/foo/` as the same thing, but other tooling does not.

[Technically speaking](https://www.rfc-editor.org/rfc/rfc8820#name-uri-paths), they are different because the trailing slash indicates there is another resource identified by an empty string.

Enable this rule to avoid confusion in your documentation.
When it comes to developer experience, consistency rules.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  no-path-trailing-slash: error
```

## Examples

Given this configuration:


```yaml
rules:
  no-path-trailing-slash: error
```

Example of **incorrect** path:


```yaml
paths:
  /customers/:
    $ref: ./paths/customers.yaml
```

Example of **correct** path:


```yaml
paths:
  /customers:
    $ref: ./paths/customers.yaml
```

## Related rules

- [no-server-trailing-slash](/docs/cli/v1/rules/oas/no-server-trailing-slash)
- [path-not-include-query](/docs/cli/v1/rules/oas/path-not-include-query)
- [path-declaration-must-exist](/docs/cli/v1/rules/oas/path-declaration-must-exist)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/no-path-trailing-slash.ts)
- [Paths object docs](https://redocly.com/docs/openapi-visual-reference/paths/)