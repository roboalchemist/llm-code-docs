# Source: https://www.apollographql.com/docs/graphos/connectors/requests/body.md

# Setting HTTP Request Bodies

Apollo Connectors support [`POST`, `PUT`, `PATCH`, and `DELETE` requests](https://www.apollographql.com/docs/graphos/connectors/requests#basic-example-connectors), including request bodies.
The `http.body` field defines a JSON body to send with requests using the [mapping language](https://www.apollographql.com/docs/graphos/connectors/reference/mapping).

## Example request bodies

### Basic `http.body` example

This example uses the `id` and `quantity` fields from the `input` argument to create a JSON body like this:

```graphql
type Mutation {
  addProduct(input: AddProductInput!): Product
    @connect(
      source: "ecomm"
      http: {
        POST: "/products/add"
        body: """
        $args.input {
          id
          quantity
        }
        """
      }
      selection: "id"
    )
}
```

```json
{
  "id": 1,
  "quantity": 2
}
```

The values in the JSON body depend on the `input` argument's values.

### Example `http.body` with methods

This example updates a product country code using the [`slice` method](https://www.apollographql.com/docs/graphos/connectors/mapping/methods#string-methods) in the `body`.

```graphql
type Mutation {
  updateProduct(id: ID!, countryName: String!): Product
    @connect(
      source: "ecomm"
      http: {
        PUT: "/products/{$args.id}"
        body: "countryCode: $args.countryName->slice(0, 2)"
      }
      selection: "id"
    )
}
```

Given a `countryName` of `"FRANCE"` the request body would look like this:

```json
{
  "countryCode": "FR"
}
```

### Example `http.body` with literal value

This example shows how to include [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals#using-literal-values) in your request body using the `$()` syntax.

```graphql
type Mutation {
  deleteProduct(id: ID!): DeleteResult
    @connect(
      source: "ecomm"
      http: {
        DELETE: "/products/{$args.id}"
        body: """
        $({
          reason: "User requested deletion",
          permanentDelete: true,
        })
        """
      }
      selection: "success"
    )
}
```

```json
{
  "reason": "User requested deletion",
  "permanentDelete": true,
}
```

## Form URL encoding

By adding a `Content-Type` header of exactly `application/x-www-form-urlencoded`, GraphOS Router encodes the request body as a form URL encoded string.

```graphql title=Form URL encoding
type Mutation {
  createPost(input: CreatePostInput!): Post
    @connect(
      http: {
        POST: "https://api.example.com/posts"
        headers: [{ name: "Content-Type", value: "application/x-www-form-urlencoded" }],      
        body: """
        $args.input {
          title
          content
        }
        """
      }
    )
  }
```

The router first maps the request body to a JSON object:

```json
{
  "title": "Hello, world!",
  "content": "This is a post."
}
```

Then, it encodes the object as a `x-www-form-urlencoded` string:

```plaintext
title=Hello%2C+world%21&content=This+is+a+post.
```

### URL encoding details

Connectors follow these rules for URL encoding:

* List values are indexed starting from 0 using the `list[0]=value` syntax.
* Nested objects use the `parent[child]=value` syntax.
* Spaces are encoded as `+`.

```graphql title=Example: form URL encoding
type Mutation {
  example(input: ExampleInput!): Example
  @connect(
    http: { POST: "/example", headers: [{ name: "content-type", value: "application/x-www-form-urlencoded" }] }
    body: """
      $args.input {
        name
        tags
        addresses {
          street
          city
          state
          zip
        }
      }
    """
  )
}

input ExampleInput {
  name: String!
  tags: [String!]
  addresses: [AddressInput!]
}

input AddressInput {
  street: String!
  city: String!
  state: String!
  zip: String!
}
```

```plaintext title=Result (new lines added for readability)
name=Example
&tags[0]=tag1
&tags[1]=tag2
&addresses[0][street]=123+Main+St
&addresses[0][city]=Anytown
&addresses[0][state]=CA
&addresses[0][zip]=12345
&addresses[1][street]=456+Elm+St
&addresses[1][city]=Othertown
&addresses[1][state]=NY
&addresses[1][zip]=54321
```
