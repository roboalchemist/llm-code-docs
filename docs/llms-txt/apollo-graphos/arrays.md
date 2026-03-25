# Source: https://www.apollographql.com/docs/graphos/connectors/mapping/arrays.md

# Mapping Arrays

In Apollo Connectors selection mapping, array handling happens automatically, so you must ensure that your schema uses list types appropriately.

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

## Example array handling

For example, given the following JSON response:

```json title=JSON Response
{
  "results": [
    {
      "id": "1",
      "variants": [
        { "id": "1", "color": "Silver" },
        { "id": "2", "color": "Platinum" }
      ],
      "reviews": ["Best purchase ever!", "Good value"]
    }
  ]
}
```

You can use the following selection mapping:

```graphql title=Example: wrapping fields
type Query {
  products: [Product]  # List 1
    @connect(
      http: { GET: "https://ecommerce.demo-api.apollo.dev/products" }
      selection: """
      $.results {                    # Populates list 1
        id
        variants {                   # Populates list 2
          id
          type: color
        }
        reviews                      # Populates list 3
      }
      """
    )
}

type User {
  id: ID!
  variants: [Variant] # List 2
  reviews: [String] # List 3
}

type Variant {
  id: ID!
  color: String
}
```

## List management

Various methods, including `->first`, `->last`, `->slice`, and `->size`, let you transform lists.

For example, to transform a list into its first value, use `->first` like so:

```connectors title=Selection mapping snippet
color->first
```

```json title=Response data
{
  "color": ["red", "green", "blue"]
}
```

```json title=Result
{
  "color": "red"
}
```

To wrap a single item in a list, you can use a [literal list](https://www.apollographql.com/docs/graphos/connectors/responses/literals) and select the property:

```connectors title=Selection mapping snippet
$([$.color])
```

```json title=Response data
{
  "color": "red"
}
```

```json title=Result
{
  "color": ["red"]
}
```

## Convert a map into a list of key-value pairs

Converting a map into a list of key-value pairs is particularly useful when you need to work with data in a more structured or iterable format. For example, in a frontend application, you might want to render a list of items, such as color names and their corresponding hex codes.

The example below uses the `->entries` method to convert a map of color names and hex codes into a list of objects. You can use the following selection mapping snippet:

```connectors title=Selection mapping snippet
colors: colors->entries
```

To transform response data like this:

```json title=Response data
{
  "colors": {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff"
  }
}
```

```json title=Result
{
  "colors": [
    { "key": "red", "value": "#ff0000" },
    { "key": "green", "value": "#00ff00" },
    { "key": "blue", "value": "#0000ff" }
  ]
}
```

To use different names for keys and values, select the fields with aliases:

```connectors title=Selection mapping snippet
colors: colors->entries {
  name: key
  hex: value
}
```

```json title=Response data
{
  "colors": {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff"
  }
}
```

```json title=Result
{
  "colors": [
    { "name": "red", "hex": "#ff0000" },
    { "name": "green", "hex": "#00ff00" },
    { "name": "blue", "hex": "#0000ff" }
  ]
}
```

## Additional resources

* Refer to the [mapping language reference](https://www.apollographql.com/docs/graphos/connectors/reference/mapping) for a complete overview of mapping syntax and usage.
* The [methods reference](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/methods) lists all available object and array methods.
