# Source: https://redocly.com/docs/cli/rules/arazzo/sourcedescriptions-name-unique.md

# Source: https://redocly.com/docs/cli/v1/rules/arazzo/sourcedescriptions-name-unique.md

# sourceDescriptions-name-unique

The `name` property of the Source Description object must be unique across all source descriptions.

| Arazzo | Compatibility |
|  --- | --- |
| 1.x | â |


## Design principles

To avoid confusion or unexpected outputs, each Source Description object must have a unique `name` property.
Especially in a longer list of sources, this could be difficult to identify and could have unwanted side effects.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off`. |


An example configuration:


```yaml
rules:
  sourceDescriptions-name-unique: error
```

## Examples

Given the following configuration:


```yaml
rules:
  sourceDescriptions-name-unique: error
```

Example of a **correct** `sourceDescriptions` list:


```yaml
sourceDescriptions:
  - name: museum-api
    type: openapi
    url: ../openapi.yaml
  - name: pets-api
    type: openapi
    url: ../petstore.yaml
```

## Related rules

- [sourceDescription-type](/docs/cli/v1/rules/arazzo/sourcedescriptions-type)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/arazzo/sourceDescriptions-name-unique.ts)