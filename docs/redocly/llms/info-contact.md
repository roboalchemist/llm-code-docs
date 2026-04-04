# Source: https://redocly.com/docs/cli/rules/oas/info-contact.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/info-contact.md

# info-contact

Requires the `Contact` info object defined in your API.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |



```mermaid
flowchart TD

Root ==> Info --> Contact

style Contact fill:#codaf9,stroke:#0044d4,stroke-width:5px
```

## API design principles

When it comes to APIs, we generally want more consumers.
If they need help to purchase, integrate, or troubleshoot, your contact info should be front and center.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off`. |


An example configuration:


```yaml
rules:
  info-contact: warn
```

## Examples

Given this configuration:


```yaml
rules:
  info-contact: error
```

Example of **incorrect** contact:


```yaml
info:
  version: 1.0.0
  title: Incorrect example missing contact
  termsOfService: 'https://example.com/terms/'
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
```

Example of **correct** contact:


```yaml
info:
  contact:
    name: Redocly API Support
    url: https://www.redocly.com/support
    email: team@redocly.com
```

## Related rules

- [info-license](/docs/cli/v1/rules/oas/info-license)
- [info-license-url](/docs/cli/v1/rules/oas/info-license-url)
- [spec](/docs/cli/v1/rules/oas/struct)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/info-contact.ts)
- [Contact object docs](https://redocly.com/docs/openapi-visual-reference/contact/)