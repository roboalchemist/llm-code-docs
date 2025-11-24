# Source: https://docs.hypermode.com/dgraph/graphql/schema/directives/auth.md

# @auth

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

`@auth` allows you to define how to apply authorization rules on the
queries/mutation for a type.

Refer to [graphql endpoint security](/dgraph/graphql/security/overview),
[Role-Based Access Control (RBAC) rules](/dgraph/graphql/security/rbac-rules)
and [Graph traversal rules](/dgraph/graphql/security/graphtraversal-rules) for
details.

`@auth` directive isn't supported on `union` and `@remote` types.
