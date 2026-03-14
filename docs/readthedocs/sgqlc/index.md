# Simple GraphQL Client

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

## Table of Contents

- sgqlc module

- sgqlc-codegen Tool

  - Generate SGQLC Code

    - Downloading schema.json

    - Generating Schema Types

    - Generating Operations

  - sgqlc-codegen Command Line Options

    - Positional Arguments

    - Sub-commands

      - schema

        - Positional Arguments

        - Named Arguments

      - operation

        - Positional Arguments

        - Named Arguments

- sgqlc.types module

  - GraphQL Types in Python

    - Code Generator

    - Examples

      - Common Usage

      - Using `Field` instances

      - Adding types to specific `Schema`

      - Inheritance and Interfaces

      - Cross References (Loops)

      - Special Attribute Names

      - Non GraphQL Attributes

      - Utilities

  - `Arg`

    - `Arg.__init__()`

  - `ArgDict`

    - `ArgDict.__init__()`

    - `ArgDict.__repr__()`

    - `ArgDict.__str__()`

  - `BaseItem`

    - `BaseItem.__init__()`

    - `BaseItem.__repr__()`

    - `BaseItem.__str__()`

    - `BaseItem._to_graphql_name()`

    - `BaseItem._to_python_name()`

  - `BaseMeta`

    - `BaseMeta.__ensure__()`

    - `BaseMeta.__init__()`

    - `BaseMeta.__repr__()`

    - `BaseMeta.__str__()`

  - `BaseType`

    - `BaseType.__weakref__`

  - `Boolean`

    - `Boolean.converter`

  - `ContainerType`

    - `ContainerType.__contains__()`

    - `ContainerType.__getitem__()`

    - `ContainerType.__init__()`

    - `ContainerType.__iter__()`

    - `ContainerType.__len__()`

    - `ContainerType.__repr__()`

    - `ContainerType.__setattr__()`

    - `ContainerType.__setitem__()`

    - `ContainerType.__str__()`

  - `ContainerTypeMeta`

    - `ContainerTypeMeta.__dir__()`

    - `ContainerTypeMeta.__init__()`

  - `Enum`

    - `Enum.__new__()`

  - `Field`

    - `Field.__bytes__()`

    - `Field.__init__()`

  - `Float`

    - `Float.converter`

  - `ID`

    - `ID.converter`

  - `Input`

    - `Input.__init__()`

    - `Input.__new__()`

  - `Int`

    - `Int.converter`

  - `Interface`

    - `Interface.__new__()`

  - `Scalar`

    - `Scalar.__new__()`

  - `Schema`

    - `Schema.__bytes__()`

    - `Schema.__contains__()`

    - `Schema.__getattr__()`

    - `Schema.__getitem__()`

    - `Schema.__iadd__()`

    - `Schema.__init__()`

    - `Schema.__isub__()`

    - `Schema.__iter__()`

    - `Schema.__repr__()`

    - `Schema.__str__()`

  - `String`

    - `String.converter`

  - `Type`

  - `Union`

    - `Union.__new__()`

  - `Variable`

    - `Variable.__init__()`

    - `Variable.__repr__()`

    - `Variable.__str__()`

    - `Variable._to_graphql_name()`

  - `list_of()`

  - `non_null()`

  - Sub Modules

- sgqlc.types.datetime module

  - GraphQL Types for `datetime`

    - Examples

  - `Date`

  - `DateTime`

  - `Time`

- sgqlc.types.relay module

  - GraphQL Types for Relay

    - Examples

  - `Connection`

  - `Node`

  - `PageInfo`

  - `connection_args()`

- sgqlc.types.uuid module

  - GraphQL Types for `uuid`

    - Examples

  - `UUID`

- sgqlc.operation module

  - Generate Operations (Query and Mutations) using Python

    - Performance

    - Code Generator

    - Examples

      - Selecting to Generate Queries

      - Interpret Query Results

      - Error Reporting

      - Mutations

      - Inline Fragments & Interfaces

      - Named Fragments

      - Utilities

  - `Operation`

    - `Operation.__init__()`

    - `Operation.__repr__()`

    - `Operation.__str__()`

    - `Operation.__weakref__`

  - `Selection`

    - `Selection.__dir__()`

    - `Selection.__fields__()`

    - `Selection.__get_all_fields_selection_list()`

    - `Selection.__init__()`

    - `Selection.__repr__()`

    - `Selection.__select_all__()`

    - `Selection.__str__()`

  - `SelectionList`

    - `SelectionList.__as__()`

    - `SelectionList.__fields__()`

    - `SelectionList.__init__()`

    - `SelectionList.__repr__()`

    - `SelectionList.__str__()`

  - `Selector`

    - `Selector.__args__`

    - `Selector.__as__()`

    - `Selector.__call__()`

    - `Selector.__dir__()`

    - `Selector.__fields__`

    - `Selector.__fragment__()`

    - `Selector.__init__()`

    - `Selector.__repr__()`

    - `Selector.__selection__()`

    - `Selector.__str__()`

- sgqlc.endpoint module

  - Access GraphQL endpoints using Python

  - Sub Modules

- sgqlc.endpoint.base module

  - Base Endpoint

  - `BaseEndpoint`

    - `BaseEndpoint.__call__()`

    - `BaseEndpoint.__weakref__`

    - `BaseEndpoint._fixup_graphql_error()`

    - `BaseEndpoint._log_graphql_error()`

    - `BaseEndpoint._log_json_error()`

    - `BaseEndpoint.snippet()`

- sgqlc.endpoint.http module

  - Synchronous HTTP Endpoint

  - `HTTPEndpoint`

    - `HTTPEndpoint.__call__()`

    - `HTTPEndpoint.__init__()`

    - `HTTPEndpoint.__str__()`

    - `HTTPEndpoint._log_http_error()`

- sgqlc.endpoint.requests module

  - Synchronous HTTP Endpoint using python-requests

  - `RequestsEndpoint`

    - `RequestsEndpoint.__call__()`

    - `RequestsEndpoint.__init__()`

    - `RequestsEndpoint.__str__()`

    - `RequestsEndpoint._log_http_error()`

- sgqlc.endpoint.websocket module

- sgqlc.introspection module

  - Introspection

    - Downloading schema.json

  - `variables()`

  - sgqlc.introspection Command Line Options

    - Positional Arguments

    - Named Arguments