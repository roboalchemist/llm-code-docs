# Source: https://redocly.com/docs/cli/rules/respect/respect-supported-versions.md

# Source: https://redocly.com/docs/cli/v1/rules/respect/respect-supported-versions.md

# respect-supported-versions

The `version` property must be one of the supported values.

| Arazzo | Compatibility |
|  --- | --- |
| 1.x | â |


## API design principles

This rule is used with Respect.
The `version` property must be one of the Respect-supported values which may be different from the latest `Arazzo` version.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off`. |


An example configuration:


```yaml
rules:
  respect-supported-versions: error
```

## Examples

Given the following configuration:


```yaml
rules:
  respect-supported-versions: error
```

Example of a **correct** entry:


```yaml
arazzo: 1.0.1
```

## Related rules

- [no-criteria-xpath](/docs/cli/v1/rules/respect/no-criteria-xpath)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/respect/respect-supported-versions.ts)