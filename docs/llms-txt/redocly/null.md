# Source: https://redocly.com/learn/openapi/openapi-visual-reference/null.md

# `null`

> When a schema specifies a type of `null`, it has only one acceptable value: `null`.


OpenAPI 2.0 has no built-in support for `null` types.
Redocly published a [specification extension `x-nullable`](https://redocly.com/docs-legacy/api-reference-docs/specification-extensions/x-nullable/) which can be used to specify that a field value can be `null`.

In OpenAPI 3.0, a built-in `nullable` field was added.

In OpenAPI 3.1, the `type` accepts an array of types, and `null` can be added to the list of types.

## Visuals

The following shows three examples for implementing null in OAS 2.0, 3.0, and 3.1.


```yaml
type: object
properties:
  screen:
    type: string
    x-nullable: true
```


```yaml
type: object
properties:
  screen:
    type: string
    nullable: true
```


```yaml
type: object
properties:
  screen:
    type:
      - string
      - 'null'
```

The following image shows the schema with a string type of property that is also nullable.

![schema null](/assets/schema-null.1947c0a2f93745bb11d8170aa8f87045fa17ef06301513cba00d9c23bd7a4c89.6f948c6e.png)

## Types

- SchemaProperties



```ts
const SchemaProperties: NodeType = {
  properties: {},
  additionalProperties: 'Schema',
};
```