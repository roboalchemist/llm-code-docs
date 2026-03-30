# Source: https://redocly.com/docs/cli/configuration/reference/apis.md

# Source: https://redocly.com/docs/cli/v1/configuration/reference/apis.md

# Source: https://redocly.com/docs/cli/configuration/apis.md

# Source: https://redocly.com/docs/cli/v1/configuration/apis.md

# Source: https://redocly.com/docs/realm/config/apis.md

# `apis`

## Introduction

If your project contains multiple APIs, you can use the `apis` configuration section to set up rules and settings for individual APIs.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| `{name}@{version}` | [API object](#api-object) | **REQUIRED**.
Each API needs a name and optionally a version.
Supports alphanumeric characters and underscores. |


### API object

| Option | Type | Description |
|  --- | --- | --- |
| root | string | **REQUIRED**.
Path to the root API description file. |
| rules | [Rules object](/docs/realm/config/rules) | Additional rule configuration for this API. |
| decorators | [Decorators object](/docs/realm/config/openapi/decorators) | Additional decorator configuration for this API. |
| preprocessors | [Decorators object](/docs/realm/config/openapi/decorators) | Preprocessors run before linting, and follow the same structure as decorators.
We recommend the use of decorators over preprocessors in most cases. |
| extends | [string] | Extend an existing configuration sets. Read more about [Extends](/docs/realm/config/openapi/extends). |
| output | string | Output file path.
When running `bundle` without specifying an API, the bundled API description is saved to this location.
Example: `docs/api.yaml`. |


## Examples

The following example shows a simple `redocly.yaml` configuration file with settings for multiple APIs.


```yaml
apis:
  orders@v3:
    root: orders/openapi.yaml
    extends:
      - minimal
    rules:
      tags-alphabetical: error
      operation-operationId-unique: error
      spec-strict-refs: error
  newsletter:
    root: newsletter/openapi.yaml
    extends:
      - recommended-strict
    rules:
      info-contact: off
      operation-summary: off
```

The following example shows `redocly.yaml` configuration file with settings for multiple APIs outputs.


```yaml
apis:
  main@v1:
    root: openapi-v1.yaml
    output: v1/bundled.yaml
  main@v2:
    root: openapi-v2.yaml
    output: v2/bundled.yaml
```

When running `redocly bundle` with this config, the bundled API descriptions are saved to the corresponding location.

## Resources

- **[Extends configuration](/docs/realm/config/openapi/extends)** - Set the base ruleset to use for consistent API validation and linting across your documentation
- **[Rules configuration](/docs/realm/config/rules)** - Define the linting rules that are used for API validation and quality enforcement
- **[Decorators](/docs/realm/config/openapi/decorators)** - Apply transformations to your OpenAPI documents for enhanced functionality and custom modifications
- **[Per-API configuration examples](https://redocly.com/docs/cli/configuration/apis)** - Detailed information and examples for configuring individual APIs with specific settings
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options for comprehensive documentation and platform customization