# Source: https://redocly.com/docs/cli/rules/oas/info-license.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/info-license.md

# info-license

Requires the license info in your API descriptions.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |



```mermaid
flowchart TD

Root ==> Info --> License

style License fill:#codaf9,stroke:#0044d4,stroke-width:5px
```

## API design principles

The principle of providing your users with accurate and relevant information does not apply to API design only, but to any product-related communication in general.

Before they can work with your API, your users must understand the terms and conditions of your API usage.

By being upfront with the API license, you can reduce friction and encourage API adoption.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `warn` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  info-license: error
```

## Examples

Given the following configuration:


```yaml
rules:
  info-license: error
```

Example of an **incorrect** license:


```yaml
info:
  version: v1.1
```

Example of a **correct** license:


```yaml
info:
  license:
    name: Apache 2.0
```

## Related rules

- [info-contact](/docs/cli/v1/rules/oas/info-contact)
- [info-license-url](/docs/cli/v1/rules/oas/info-license-url)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/info-license.ts)
- [License object docs](https://redocly.com/docs/openapi-visual-reference/license/)