# Source: https://docs.hypermode.com/dgraph/concepts/dql.md

# DQL

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

DQL is the "Dgraph Query Language" and is based on GraphQL. It is neither a
superset nor subset of GraphQL, but is generally more powerful than GraphQL. DQL
coexists nicely with GraphQL so many users perform most access using GraphQL and
only "drop down" into DQL when there is a particular query mechanism needed that
isn't supported in the GraphQL spec. E.g. @recurse query operations are only in
DQL. Other customers simply use DQL. DQL supports both queries and mutations, as
well as hybrid "upsert" operations.
