# Source: https://docs.hypermode.com/dgraph/dql/facets.md

# Source: https://docs.hypermode.com/dgraph/concepts/facets.md

# Source: https://docs.hypermode.com/dgraph/dql/facets.md

# Source: https://docs.hypermode.com/dgraph/concepts/facets.md

# Source: https://docs.hypermode.com/dgraph/dql/facets.md

# Source: https://docs.hypermode.com/dgraph/concepts/facets.md

# Facets

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

Dgraph allows a set of properties to be associated with any `Relationship`. E.g.
if there is a "worksFor" relationships between Node "Bob" and Node "Google",
this relationship may have facet values of "since": 2002-05-05 and "position":
"Engineer".

Facets can always be replaced by adding a new Node representing the relationship
and storing the facet data as attributes of the new Node.

The term "facet" is also common in database and search engine technology, and
indicates a dimension or classification of data. One way to use facets it to
indicate a relationship type.
