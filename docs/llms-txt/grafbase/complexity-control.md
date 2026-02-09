# Source: https://grafbase.com/docs/gateway/configuration/complexity-control.md

# Source: https://grafbase.com/docs/gateway/security/complexity-control.md

# Complexity Control

GraphQL queries offer lots of flexiblity to build the queries you need. But
this flexibility can be abused, causing excess load on downstream servers.

[Operation limits][op-limits] allow users to set a high water mark on many of
the properties of a GraphQL query. But they are quite a blunt tool - not all
subgraphs have the same performance characteristics and even within a subgraph
not all fields neccesarily cause the same load.

That's where complexity control comes in: it allows you to set an overall
complexity limit in the Grafbase Gateway, but leaves the definition of how
complex each field is up to the developers of the subgraphs.

Read more on [configuring the complexity control][config].

## Configuring Complexity

It's up to each individual subgraph to define the compleixty of it's fields.
This can be acheived with two directives: `@cost` & `@listSize`

### Field Cost

The `@cost` directive is defined as such:

```graphql
directive @cost(
  weight: Int!
) on ARGUMENT_DEFINITION | ENUM | FIELD_DEFINITION | INPUT_FIELD_DEFINITION | OBJECT | SCALAR
```

This directive can be provided on a field, argument, or type. When provided on
a field or argument it sets the cost of that field or argument appearing in a
query. When provided on a type it sets the cost of a field of that type
appearing in a query. If an individual field has a cost then that will be
override any cost set on the type of that field.

If no cost directive can be found for a particular field or it's type, then a
default cost will be applied. If the field is of a scalar type, then its cost
is assumed to be zero. If the field is of an object type, then its default
cost is 1.

### List Size

The `@listSize` directive is defined as such:

```graphql
directive @listSize(
  assumedSize: Int
  slicingArguments: [String!]
  sizedFields: [String!]
  requireOneSlicingArgument: Boolean = true
) on FIELD_DEFINITION
```

This directive controls the size that we assume each list field has. In brief
it's arguments are:

- `assumedSize` if provided sets the size that we assume this list is.
- `slicingArguments` says that the given arguments to this field define the
  length of the list.
- `sizedFields` can be used on connection fields that are following the [GraphQL
  cursor specification][cursor-spec] to indicate which subfields of the current
  field are controlled by the slicing arguments on this field.
- `requireOneSlicingArgument` can be set when slicing arguments is also set.
  If set an error will be raised if we receive a query for this field that
  doesn't have exactly one slicing argument provided. This argument defaults
  to true, but if slicingArguments is not provided it is not used.

For more details you can read the detailed specification of `@listSize` in the
[Cost Directive Specification][cost-spec].

## Complexity Calculation

The complexity score of an operation is calculated by walking the query, and
summing up the cost of each individual field. Fields are assigned a cost
according to the cost of the field or the type of the field, plus the cost of
all their children. If the field in question is a list then its cost is
multiplied by the expected size of the list.

For example this query would be calculated as:

```graphql
query {
  # (self + children) * listSize = (1 + 1) * 4 = 8
  products(limit: 4) {
    id # scalar: 0
    title # scalar: 0
    price # scalar: 0
    author {
      # object: 1
      id # scalar: 0
      name # scalar: 0
    }
  }
}
```

[op-limits]: /docs/gateway/security/operation-limits
[cost-spec]: https://ibm.github.io/graphql-specs/cost-spec.html#sec-The-List-Size-Directive
[cursor-spec]: https://relay.dev/graphql/connections.htm
[config]: /docs/gateway/configuration/complexity-control