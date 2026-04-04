# Source: https://www.apollographql.com/docs/graphos/connectors/responses.md

# Mapping HTTP Responses

With Apollo Connectors, you map HTTP response data from REST APIs to your GraphQL schema.
This mapping capability is what makes Connectors powerful, allowing your REST data to be accessed through GraphQL's flexible query language without writing custom transformation code.

In this guide, you'll learn more about:

* Why Connectors require mapping
* Rules for mapping HTTP responses

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.
If you learn best with videos and exercises, this [interactive course](https://www.apollographql.com/tutorials/connectors-mapping-and-transforms) teaches the syntax and methods of the Connectors mapping language.

## Mapping overview

Mapping HTTP responses to your GraphQL schema transforms the data returned by your REST APIs into a format that fits your GraphQL API structure. This ensures GraphQL requests can provide consistent, predictable responses to clients, even when working with data from different API sources.

You map your GraphQL schema to an HTTP response using the Apollo Connectors mapping language in the `@connect` directive's `selection` field.
This process is sometimes referred to as *selection mapping*.

The mapping language you use for selection mapping is the same mapping language you use in URLs, headers, and request bodies when making HTTP requests.

### Unique features of selection mapping

In the context of selection mapping, the mapping language has an important, unique feature. When used in `selection`, it's assumed that all fields come from the HTTP response body unless otherwise specified. For example, given the following JSON response:

```JSON title=JSON Response
{
 "id": 1,
 "name": "Lunar Rover Wheels"
}
```

You can use the following selection to map the `id` and `name` fields:

```graphql title=Example Connector with selection
type Query {
  products: Products
    @connect(
      source: "ecomm"
      http: { GET: "/products" }
      selection: "id name"
    )
}

type Product {
  id: ID!
  name: String
}
```

#### Multiline syntax

Long `selection` strings can be broken up into multiple lines with GraphQL multiline string syntax (`"""`):

```graphql title=Example: Multiline selection
type Query {
  products: Products
    @connect(
      source: "ecomm"
      http: { GET: "/products" }
      selection: """
      id
      name
      description
      """
    )
}

type Product {
  id: ID!
  name: String
  description: String
}
```

This is particularly valuable when you have a longer nested selection to map. The following example shows how each line in the `selection` translates a JSON response to fields in the GraphQL schema below.

```JSON title=JSON Response
{
  "id": 1,
  "name": "Lunar Rover Wheels",
  "variants": [
    {
      "name": "Standard Wheel",
      "price": {
        "original": 4999,
        "discounts": [],
        "final": 4999
      },
      "specifications": {
        "Material": {
          "value": "Titanium alloy"
        },
        "Diameter": {
          "value": "50 cm"
        }
      },
      "inventory": {
        "quantity": 100,
        "sellUnavailable": false
      },
      "shipping": {
        "ship1": {
          "weight": 5,
          "method": "GROUND",
          "estimate": {
            "price": 499,
            "arrival": 1675804800000
          }
        },
        "ship2": {
          "weight": 5,
          "method": "AIR",
          "estimate": {
            "price": 999,
            "arrival": 1675790400000
          }
        }
      },
      "upc": "0001234567890",
      "sku": "RW-001",
      "taxable": true,
      "variantId": "variant1"
    }
  ]
}
```

```graphql title=Multiline nested selection
type Query {
  product(id: ID!): Product
    @connect(
      http: { GET: "https://ecommerce.demo-api.apollo.dev/products/{$args.id}" }
      selection: """
      id                   # 1
      variants {           # 2
        name               # 3
        price {            # 4             
          original         # 5           
          final            # 6
        }        
      }
      """
    )
}

type Product {
  id: ID!                 # 1
  variants: [Variant]     # 2
}

type Variant {
  name: String           # 3
  price: Price           # 4
}

type Price {
  original: Int          # 5
  final: Int             # 6
}
```

#### `$status` variable

In `selection`, you also get access to the [`$status` variable](https://www.apollographql.com/docs/graphos/connectors/mapping/variables#status), which isn't available anywhere else. `$status` represents the HTTP status code of a response.

## Selection mapping rules

The `selection` field is responsible for more than just mapping response fields to the schema; it powers the core of each Connector, so it has some special rules.

### Selections can't be empty

The `selection` field isn't allowed to be empty.
You must map at least one field in every Connector.
If you have an endpoint that doesn't return any response data, you can map a scalar value using a [literal value](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#literal-values):

```connectors
success: $(true)
```

### All schema fields must be mapped

The only way to populate a field from a Connector is via `selection`, so every field defined in the schema must be mapped at least once in a Connector. The exception is fields that are resolved from another subgraph, such as those marked `@external`.

### Leaf selections must be scalars

Different Connectors can resolve different fields of the same object, so you must specify every field that a given Connector resolves. That means you can never map an entire object and expect the fields to be implicitly mapped. You must map all fields explicitly.

```graphql
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: "id name description"
    )
}

type Product {
  id: ID!
  name: String!
  description: String
  reviews: [Review]
    @connect(
      source: "ecomm"
      http: {GET: "/products/{$this.id}/reviews"}
      # selection: "$.reviews"  ❌ This won't work
      selection: """          # ✅ This works
      $.reviews {
        id
        rating
        comment
      }
      """
    )
}

type Review {
  id: ID!
  rating: Float!
  comment: String
}
```

Even though the `reviews` field contains all the information needed from the first Connector, you can't map just `$.reviews`. You must specify each field—`id`, `rating`, and `comment`—individually. This enables the query planner to know that the `rating` field must be fetched from elsewhere.

## Mapping non-JSON content types

While Connectors work best with JSON responses, they also support non-JSON content types, including test-based responses and empty responses. This is particularly useful when services return non-`200` status codes.

| Response Content Type                                                  | `$` Behavior in Selection Mapping                                                                                       | Mapping Example                               |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Blank (`content-length: 0`)                                            | `$` is `null`; mapping can use [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals) | `myField: $("This can be any literal value")` |
| Text (`text/plain`)                                                    | `$` is the literal text of the response, as a string                                                                    | `myField: $`                                  |
| Other (for example `text/html`)                                        | `$` is `null`; mapping can use [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals) | `myField: $("This can be any literal value")` |
| JSON-like (for example `application/json`, `application/vnd.api+json`) | Response is treated as JSON, `$` is the parsed JSON                                                                     | `myField: fieldFromResponse`                  |
| No `content-type` header                                               | Response is assumed to be JSON, `$` is the parsed JSON                                                                  | `myField: fieldFromResponse`                  |

If the `content-type` header indicates a JSON response and the response is invalid JSON (for example, invalid syntax or the presence of null bytes), response mapping is skipped and the router emits a top-level error.

## Additional resources

* Read the other pages in this section to see examples for [mapping fields](https://www.apollographql.com/docs/graphos/connectors/responses/fields) and [handling non-200 responses.](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling)
* Refer to the [Mapping Language section](https://www.apollographql.com/docs/graphos/connectors/mapping) to learn about working with [arrays](https://www.apollographql.com/docs/graphos/connectors/responses/arrays), [enums](https://www.apollographql.com/docs/graphos/connectors/responses/enums), and [literal values](https://www.apollographql.com/docs/graphos/connectors/responses/literals).
