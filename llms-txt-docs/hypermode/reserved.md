# Source: https://docs.hypermode.com/dgraph/graphql/schema/reserved.md

# Reserved Names

> This document provides the full list of names that are reserved and can’t be used to define any other identifiers.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

The following names are reserved and can't be used to define any other
identifiers:

* `Int`
* `Float`
* `Boolean`
* `String`
* `DateTime`
* `ID`
* `uid`
* `Subscription`
* `as` (case-insensitive)
* `Query`
* `Mutation`
* `Point`
* `PointList`
* `Polygon`
* `MultiPolygon`
* `Aggregate` (as a suffix of any identifier name)

For each type, Dgraph generates a number of GraphQL types needed to operate the
GraphQL API, these generated type names also can't be present in the input
schema. For example, for a type `Author`, Dgraph generates:

* `AuthorFilter`
* `AuthorOrderable`
* `AuthorOrder`
* `AuthorRef`
* `AddAuthorInput`
* `UpdateAuthorInput`
* `AuthorPatch`
* `AddAuthorPayload`
* `DeleteAuthorPayload`
* `UpdateAuthorPayload`
* `AuthorAggregateResult`

**Mutations**

* `addAuthor`
* `updateAuthor`
* `deleteAuthor`

**Queries**

* `getAuthor`
* `queryAuthor`
* `aggregateAuthor`

Thus if `Author` is present in the input schema, all of those become reserved
type names.
