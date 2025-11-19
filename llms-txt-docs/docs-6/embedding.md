# Source: https://docs.hypermode.com/dgraph/graphql/schema/directives/embedding.md

# @embedding

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

A Float array can be used as a vector using `@embedding` directive. It denotes a
vector of floating point numbers, i.e an ordered array of float32.

The embeddings can be defined on one or more predicates of a type and they're
generated using suitable machine learning models.

This directive is used in conjunction with `@search` directive to declare the
Hierarchical Navigable Small World (HNSW) index. For more information see:
[@search](/dgraph/graphql/schema/directives/search#vector-embedding) directive
for vector embeddings.
