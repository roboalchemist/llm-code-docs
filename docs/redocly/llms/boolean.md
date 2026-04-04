# Source: https://redocly.com/learn/openapi/openapi-visual-reference/boolean.md

# `boolean`

> The boolean type matches only two special values: `true` and `false`. Note that values that evaluate to `true` or `false`, such as 1 and 0, are not accepted by the schema.


## Visuals

The following schema describes a boolean.


```yaml
type: boolean
description: True if it is active
example: true
```

The following image shows the boolean schema.

![schema boolean](/assets/schema-boolean.c436d3e8de26a35662f038335e6b4438ad46bdde4319d14d65fff3dd1e292486.6f948c6e.png)

## Types

- SchemaProperties



```ts
const SchemaProperties: NodeType = {
  properties: {},
  additionalProperties: 'Schema',
};
```