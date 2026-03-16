# Source: https://www.apollographql.com/docs/graphos/connectors/responses/fields.md

# Mapping Response Fields

When mapping REST API responses to GraphQL fields, you'll often need to transform data structures to match your schema.
This guide shows common patterns for mapping fields from JSON responses to your GraphQL schema, including renaming, wrapping, and unwrapping fields.

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

## Basic selection mapping

Given the following JSON response:

```json title=JSON Response
{
  "id": 1,
  "name": "Lunar Rover Wheels",
  "description": "Innovatively designed wheels for lunar rovers, built to endure harsh moon terrain and provide optimal agility. Each wheel is constructed using advanced materials to withstand temperature fluctuations and dust."
}
```

You can create a basic, flat GraphQL type with fields that map to REST endpoint fields of the same names:

```graphql title=Example: basic selection
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      # The REST endpoint returns "id", "name", and "description"
      # in its response, and they're mapped directly to fields of
      # the same name in the GraphQL schema.
      selection: "id name description"
    )
}

type Product {
  id: ID!
  name: String!
  description: String!
}
```

## Renaming fields

Given the following JSON response:

```json title=JSON Response
{
  "product_id": "1",
  "title": "Lunar Rover Wheels"
}
```

You can map a JSON response field to a schema field of a different name using the same syntax as GraphQL aliases.
The desired name (the one present in the schema `type`) comes first followed by a colon (`:`) and the name of the field in the response: `desiredName: original_name`

```graphql title=Example: renaming fields
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: """
      id: product_id
      name: title
      """
    )
}

type User {
  id: ID!
  name: String!
}
```

## Unwrapping fields

Suppose the JSON response includes nesting that you don't need in your schema:

```json title=JSON Response
{
  "result": {
    "id": "1",
    "name": {
      "value": "Lunar Rover Wheels"
    },
    "specifications": {
      "material": "Titanium alloy",
      "diameter": "50 cm"
    }
  }
}
```

You can "unwrap" fields using the `.` prefix:

```graphql title=Example: unwrapping
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: """
      $.result {
        id
        name: name.value
        $.specifications {
          material
          diameter
        }
      }
      """
    )
}

type Product {
  id: ID!
  name: String!
  material: String
  diameter: String
}
```

### Using `$` when unwrapping

A leading `$.` is required when unwrapping a single property.
Without `$.`, it is interpreted as mapping the field to [create an object](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#creating-objects).
With `$.`, it is interpreted as mapping the value.

For example, given the following JSON:

```json
{ "name": "Lunar Rover Wheels" }
```

The following selections have the corresponding results:

| Selection            | Result                                     |
| -------------------- | ------------------------------------------ |
| `name`               | `{ "name": "Lunar Rover Wheels" }`         |
| `$.name`             | `"Lunar Rover Wheels"`                     |
| `product_name: name` | `{ "product_name": "Lunar Rover Wheels" }` |

When selecting a path of properties, such as `name.value`, the `$.` is allowed but not required:

```json
{ "name": { "value": "Lunar Rover Wheels" } }
```

| Selection          | Result                                          |
| ------------------ | ----------------------------------------------- |
| `$.name.value`     | `"Lunar Rover Wheels"`                          |
| `name.value`       | `"Lunar Rover Wheels"`                          |
| `$.name { value }` | `{ "value": "Lunar Rover Wheels" }`             |
| `name { value }`   | `{ "name": { "value": "Lunar Rover Wheels" } }` |

The simple form also applies when using [value transformations](https://www.apollographql.com/docs/graphos/connectors/responses/fields.md#transforming-values). These are equivalent:

| Selection                                                                               | Result                 |
| --------------------------------------------------------------------------------------- | ---------------------- |
| `name->match(["Lunar Rover Wheels", "Wheels"], ["Zero-Gravity Moon Boots", "Boots"])`   | `{ "name": "Wheels" }` |
| `$.name->match(["Lunar Rover Wheels", "Wheels"], ["Zero-Gravity Moon Boots", "Boots"])` | `{ "name": "Wheels" }` |

## Wrapping fields

You can create nested fields from a flat structure using a variation on the alias syntax. This is especially useful for converting a simple foreign key into an entity reference.
If the foreign keys are in a list, you can use the `$` symbol to refer to items in the list.

For example, given the following JSON response:

```json title=JSON Response
{
  "id": "1",
  "brand_id": "2",
  "variant_ids": ["3", "4"]
}
```

You can create the desired structure using curly braces (`{}`) and `$`:

```graphql title=Example: wrapping fields
type Query {
  user(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: """
      id
      brand: { id: brand_id }
      variants: $.variant_ids { id: $ }
      """
    )
}

type Product {
  id: ID!
  brand: Brand
  variant: [Variant]
}

type Brand {
  id: ID!
}

type Variant {
  id: ID!
}
```

## Accessing fields that start with a numerical value

Field names that start with a numerical value must be put in quotes (`" "`).

For example, given the following JSON response that includes a `specifications.3DModel` field:

```json title=JSON Response
{
  "id": 1,
  "name": "Lunar Rover Wheels",
  "specifications": {
    "material": "Titanium alloy",
    "diameter": "50 cm",
    "3DModel": "https://example.com/lunar-rover-wheel-3d"
  }
}
```

You can map the field like so:

```graphql title=Example: field name with numeric starting character
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: """
      id
      modelUrl: specifications."3DModel"
      """
    )
}

type Product {
  id: ID!
  modelUrl: String
}
```

This example also [unwraps](https://www.apollographql.com/docs/graphos/connectors/responses/fields.md#unwrapping-fields) and [renames](https://www.apollographql.com/docs/graphos/connectors/responses/fields.md#renaming-fields) the `specifications.3DModel` field to top-level `modelUrl` field.

## Example: Complex nested selection

A complex, nested GraphQL type, `Product`, maps its fields from a REST endpoint returning multiple nested objects.

```json
{
  "id": 1,
  "name": "Lunar Rover Wheels",
  "createdAt": 1675200000000,
  "updatedAt": 1675200000000,
  "description": "Innovatively designed wheels for lunar rovers, built to endure harsh moon terrain and provide optimal agility. Each wheel is constructed using advanced materials to withstand temperature fluctuations and dust.",
  "slug": "lunar-rover-wheels",
  "tags": [
    { "tagId": "1", "name": "Instruments" },
    { "tagId": "2", "name": "Space" }
  ],
  "category": "Engineering Components",
  "availability": "AVAILABLE",
  "variants": [
    {
      "name": "Standard Wheel",
      "price": {
        "original": 4999,
        "discounts": [],
        "final": 4999
      },
      "specifications": {
        "Material": { "value": "Titanium alloy" },
        "Diameter": { "value": "50 cm" }
      },
      "inventory": { "quantity": 100, "sellUnavailable": false },
      "variantId": "variant1"
    }
  ]
}
```

```graphql
type Query {
  product(id: ID!): Product
    @connect(
      http: { path: "https://ecommerce.demo-api.apollo.dev/products/{$args.id}" }
      selection: """
      id
      name
      description
      availability
      createdAt
      updatedAt
      tags: $.tags {
        id: tagId
        name
      }
      variants: $.variants {
        name
        taxable
        price {
          original
          final
        }
        specifications: $.specifications {
          material: Material.value
          diameter: Diameter.value
        }
        inventory {
          quantity
          sellUnavailable
        }
      }
      """
    )
}

type Product {
  id: ID!
  name: String!
  createdAt: Float
  updatedAt: Float
  description: String!
  availability: String!
  tags: [Tag]
  variants: [Variant]
}

type Tag {
  id: ID!
  name: String!
}

type Variant {
  name: String!
  price: Price
  specifications: Specifications
  inventory: Inventory
}

type Price {
  original: Int
  final: Int
}

type Specifications {
  material: String
  diameter: String
}

type Inventory {
  quantity: Int
  sellUnavailable: Boolean
}
```

## Additional resources

* Refer to the [mapping language reference](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping) for a complete overview of mapping syntax and usage.
* Read the other pages in the mapping section to see examples for working with [arrays](https://www.apollographql.com/docs/graphos/connectors/mapping/arrays), [enums](https://www.apollographql.com/docs/graphos/connectors/mapping/enums), and [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals).
