# sgqlc module

This package offers an easy-to-use GraphQL client. The source code is
extensively documented, so to get started, have a look at the following
modules:

- 

Use `sgqlc.endpoint` to access GraphQL endpoints, notably
`sgqlc.endpoint.http` provides `HTTPEndpoint` that makes
use of `urllib.request.urlopen()`.

- 

To declare GraphQL schema types as Python classes, use `sgqlc.types`.

- 

These type classes can then be used by `sgqlc.operation` to generate
and interpret GraphQL queries.

- 

`sgqlc.codegen` offers code generation to help using `sgqlc.types`
from schema introspection results (`schema.json`) and
`sgqlc.operation` using GraphQL Domain Specific Language (DSL)
executable documents.

- 

`sgqlc.types.datetime` provides bindings for `datetime` [https://docs.python.org/3/library/datetime.html#module-datetime] and
ISO 8601, while `sgqlc.types.relay` exposes `Node`, `PageInfo` and
`Connection` types, useful for pagination.

license:

ISC