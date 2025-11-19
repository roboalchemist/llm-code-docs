# Source: https://docs.hypermode.com/dgraph/graphql/query/order-page.md

# Order and Pagination

> Every type with fields whose types can be ordered gets ordering built into the query and any list fields of that type.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Every type with fields whose types can be ordered (`Int`, `Float`, `String`,
`DateTime`) gets ordering built into the query and any list fields of that type.
Every query and list field gets pagination with `first` and `offset` and
ordering with `order` parameter.

The `order` parameter isn't required for pagination.

For example, find the most recent 5 posts.

```graphql
queryPost(order: { desc: datePublished }, first: 5) { ... }
```

Skip the first five recent posts and then get the next 10.

```graphql
queryPost(order: { desc: datePublished }, offset: 5, first: 10) { ... }
```

It is also possible to give multiple orders. For example, sort by date and
within each date order the posts by number of likes.

```graphql
queryPost(order: { desc: datePublished, then: { desc: numLikes } }, first: 5) { ... }
```
