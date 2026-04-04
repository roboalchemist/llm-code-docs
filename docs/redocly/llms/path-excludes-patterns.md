# Source: https://redocly.com/docs/cli/v1/rules/oas/path-excludes-patterns.md

# path-excludes-patterns

Disallow patterns from paths.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

The [`no-http-verbs-in-paths` rule](/docs/cli/v1/rules/oas/no-http-verbs-in-paths) is pre-built for a very specific set of patterns.
This rule is the general Swiss army knife version.
If you absolutely know something should not be in the path (for example `foo`), then add the pattern to prevent it.

Some common things to check using this rule: other common CRUD verbs, bad words, and internal code or terminology.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |
| patterns | [string] | List of patterns to match. For example, `^\/[a-z]`. |


An example configuration:


```yaml
rules:
  path-excludes-patterns:
    severity: error
    patterns:
      - ^\/[0-9]
```

## Examples

Given this configuration:


```yaml
rules:
  path-excludes-patterns:
    severity: error
    patterns:
      - ^\/[0-9]
```

Example of an **incorrect** path:


```yaml
paths:
  /1customers/{id}:
    post:
      parameters:
        - name: id
          in: path
          required: true
```

Example of a **correct** path:


```yaml
paths:
  /customers/{id}:
    post:
      parameters:
        - name: id
          in: path
          required: true
```

## Related rules

- [no-http-verbs-in-paths.md](/docs/cli/v1/rules/oas/no-http-verbs-in-paths)
- [paths-kebab-case](/docs/cli/v1/rules/oas/paths-kebab-case)
- [operation-description](/docs/cli/v1/rules/oas/operation-description)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/parameter-description.ts)
- [Paths docs](https://redocly.com/docs/openapi-visual-reference/paths/)