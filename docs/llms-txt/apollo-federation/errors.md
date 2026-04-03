# Apollo Federation Error Codes

When GraphOS attempts to compose your subgraph schemas into a supergraph schema, it confirms that:

* The subgraphs have valid GraphQL and Federation syntax
* The resulting supergraph schema is valid
* The graph router or gateway has all of the information it needs to execute operations against the resulting schema

If composition fails, a new supergraph schema cannot be generated. This document lists subgraph validation and composition error codes, along with their root causes.

Composition may flag potential improvements or *hints* on schemas which are technically valid. These hints aren't  errors, and are instead logged as part of the composition build step.
To learn more, see the [composition hints doc](https://www.apollographql.com/docs/federation/hints/).

## Errors

The following errors might be raised during composition:

Error Code /  Minimum Federation Version&#x20;
Description

###### `ABSOLUTE_CONNECT_URL_WITH_SOURCE`

Since v2.10.0\*\*

The `@connect` directive is using a `source`, but the URL is absolute. This is not allowed because the `@source` URL is joined with the `@connect` URL, so the `@connect` URL should only be a path.

###### `CIRCULAR_REFERENCE`

Since v2.10.0\*\*

A [circular reference](https://www.apollographql.com/docs/graphos/schema-design/connectors/troubleshooting#circular-references) was detected in a `@connect`'s `selection` argument.

###### `CONNECTORS_FIELD_WITH_ARGUMENTS`

Since v2.10.0\*\*

A field resolved by a connector has arguments defined.

###### `CONNECTORS_UNRESOLVED_FIELD`

Since v2.10.0\*\*

The schema includes fields that aren't resolved by a connector.

###### `CONNECTORS_UNSUPPORTED_ABSTRACT_TYPE`

Since v2.10.0\*\*

[Abstract types](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations#abstract-schema-types-are-unsupported) are not allowed when using connectors.

###### `CONNECTORS_UNSUPPORTED_FEDERATION_DIRECTIVE`

Since v2.10.0\*\*

[Certain directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations) are not allowed when using connectors.

###### `DEFAULT_VALUE_USES_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` but is used in the default value of an element visible in the API schema.

###### `DIRECTIVE_COMPOSITION_ERROR`

Since v2.1.0

Error when composing custom directives.

###### `DIRECTIVE_DEFINITION_INVALID`

Since v2.0.0

A built-in or Federation directive has an invalid definition in the schema.

Replaces [`TAG_DEFINITION_INVALID`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#tag-definition-invalid).

###### `DISALLOWED_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` that is not allowed to be `@inaccessible`.

###### `DOWNSTREAM_SERVICE_ERROR`

Since v0.x

Indicates an error in a subgraph service query during query execution in a federated service.

###### `DUPLICATE_SOURCE_NAME`

Since v2.10.0\*\*

Indicates two connector sources with the same name were created.

###### `EMPTY_MERGED_ENUM_TYPE`

Since v2.0.0

An enum type has no value common to all the subgraphs that define the type. Merging that type would result in an invalid empty enum type.

###### `EMPTY_MERGED_INPUT_TYPE`

Since v2.0.0

An input object type has no field common to all the subgraphs that define the type. Merging that type would result in an invalid empty input object type.

###### `EMPTY_SOURCE_NAME`

Since v2.10.0\*\*

No `name` was provided when creating a connector source with `@source`.

###### `ENTITY_NOT_ON_ROOT_QUERY`

Since v2.10.0\*\*

The `@connect` directive's `entity` argument should only be used on the root `Query` field.

###### `ENTITY_RESOLVER_ARGUMENT_MISMATCH`

Since v2.10.0\*\*

The arguments for an entity reference resolver do not match the entity type.

###### `ENTITY_TYPE_INVALID`

Since v2.10.0\*\*

The `@connect` directive's `entity` argument should only be used with non-list, nullable, object types.

###### `ENUM_VALUE_MISMATCH`

Since v2.0.0

An enum type that is used as both an input and output type has a value that is not defined in all the subgraphs that define the enum type.

###### `EXTENSION_WITH_NO_BASE`

Since v0.x

A subgraph is attempting to `extend` a type that is not originally defined in any known subgraph.

###### `EXTERNAL_ARGUMENT_DEFAULT_MISMATCH`

Since v2.0.0

An `@external` field declares an argument with a default that is incompatible with the corresponding argument in the declaration(s) of that field in other subgraphs.

###### `EXTERNAL_ARGUMENT_MISSING`

Since v2.0.0

An `@external` field is missing some arguments present in the declaration(s) of that field in other subgraphs.

###### `EXTERNAL_ARGUMENT_TYPE_MISMATCH`

Since v2.0.0

An `@external` field declares an argument with a type that is incompatible with the corresponding argument in the declaration(s) of that field in other subgraphs.

###### `EXTERNAL_COLLISION_WITH_ANOTHER_DIRECTIVE`

Since v2.1.0

The `@external` directive collides with other directives in some situations.

###### `EXTERNAL_MISSING_ON_BASE`

Since v0.x

A field is marked as `@external` in a subgraph but with no non-external declaration in any other subgraph.

###### `EXTERNAL_ON_INTERFACE`

Since v2.0.0

The field of an interface type is marked with `@external`: as external is about marking field not resolved by the subgraph and as interface field are not resolved (only implementations of those fields are), an "external" interface field is nonsensical

###### `EXTERNAL_TYPE_MISMATCH`

Since v0.x

An `@external` field has a type that is incompatible with the declaration(s) of that field in other subgraphs.

###### `EXTERNAL_UNUSED`

Since v0.x

An `@external` field is not being used by any instance of `@key`, `@requires`, `@provides` or to satisfy an interface implementation.

###### `FIELD_ARGUMENT_DEFAULT_MISMATCH`

Since v2.0.0

An argument (of a field/directive) has a default value that is incompatible with that of other declarations of that same argument in other subgraphs.

###### `FIELD_ARGUMENT_TYPE_MISMATCH`

Since v2.0.0

An argument (of a field/directive) has a type that is incompatible with that of other declarations of that same argument in other subgraphs.

Replaces [`VALUE_TYPE_INPUT_VALUE_MISMATCH`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#value-type-input-value-mismatch).

###### `FIELD_TYPE_MISMATCH`

Since v2.0.0

A field has a type that is incompatible with other declarations of that field in other subgraphs.

Replaces [`VALUE_TYPE_FIELD_TYPE_MISMATCH`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#value-type-field-type-mismatch).

###### `GRAPHQL_ERROR`

Since v2.10.0\*\*

A problem with GraphQL syntax or semantics was found. These will usually be caught before this validation process.

###### `GROUP_SELECTION_IS_NOT_OBJECT`

Since v2.10.0\*\*

A group selection mapping (`a { b }`) was used, but the field is not an object.

###### `GROUP_SELECTION_REQUIRED_FOR_OBJECT`

Since v2.10.0\*\*

Fields that return an object type must use a group selection mapping `{}`.

###### `HTTP_HEADER_NAME_COLLISION`

Since v2.10.0\*\*

The `name` mapping must be unique for all headers.

###### `IMPLEMENTED_BY_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` but implements an element visible in the API schema.

###### `INPUT_FIELD_DEFAULT_MISMATCH`

Since v2.0.0

An input field has a default value that is incompatible with other declarations of that field in other subgraphs.

###### `INVALID_BODY`

Since v2.10.0\*\*

The `http.body` provided in `@connect` was not valid.

###### `INVALID_HEADER`

Since v2.10.0\*\*

A provided header in `@source` or `@connect` was not valid.

###### `INVALID_SELECTION`

Since v2.10.0\*\*

The provided selection mapping in a `@connect`s `selection` was not valid.

###### `INVALID_SOURCE_NAME`

Since v2.10.0\*\*

The `name` provided for a `@source` was invalid. Source names must start with a letter, include only letters, numbers, underscores (`_`) and hyphens (`-`), and be less than 64 characters.

###### `INVALID_URL`

Since v2.10.0\*\*

A URL provided to `@source` or `@connect` was not valid.

###### `INVALID_URL_SCHEME`

Since v2.10.0\*\*

A URL scheme provided to `@source` or `@connect` was not `http` or `https`.

###### `INTERFACE_FIELD_NO_IMPLEM`

Since v2.0.0

After subgraph merging, an implementation is missing a field of one of the interfaces it implements (which can happen for valid subgraphs).

###### `INTERFACE_KEY_MISSING_IMPLEMENTATION_TYPE`

Since v2.3.0

A subgraph has a `@key` on an interface type, but that subgraph does not define an implementation (in the supergraph) of that interface.

###### `INTERFACE_KEY_NOT_ON_IMPLEMENTATION`

Since v2.3.0

A `@key` is defined on an interface type, but is not defined (or is not resolvable) on at least one of the interface implementations.

###### `INTERFACE_OBJECT_USAGE_ERROR`

Since v2.3.0

Error in the usage of the `@interfaceObject` directive.

###### `INVALID_FEDERATION_SUPERGRAPH`

Since v2.1.0

Indicates that a schema provided for an Apollo Federation supergraph is not a valid supergraph schema.

###### `INVALID_FIELD_SHARING`

Since v2.0.0

A field that is non-shareable in at least one subgraph is resolved by multiple subgraphs.

###### `INVALID_GRAPHQL`

Since v2.0.0

A schema is invalid GraphQL: it violates one of the rules of the specification.

###### `INVALID_LINK_DIRECTIVE_USAGE`

Since v2.0.0

An application of the `@link` directive is invalid/does not respect the specification.

###### `INVALID_LINK_IDENTIFIER`

Since v2.1.0

A URL/version for a `@link` feature is invalid/does not respect the specification.

###### `INVALID_SHAREABLE_USAGE`

Since v2.1.2

The `@shareable` Federation directive is used in an invalid way.

###### `INVALID_SUBGRAPH_NAME`

Since v2.0.0

A subgraph name is invalid. (Subgraph names cannot be a single underscore (`_`)).

###### `KEY_DIRECTIVE_IN_FIELDS_ARG`

Since v2.1.0

The `fields` argument of a `@key` directive includes some directive applications. This is not supported.

###### `KEY_FIELDS_HAS_ARGS`

Since v2.0.0

The `fields` argument of a `@key` directive includes a field defined with arguments (which is not currently supported).

###### `KEY_FIELDS_SELECT_INVALID_TYPE`

Since v0.x

The `fields` argument of `@key` directive includes a field whose type is a list, interface, or union type. Fields of these types cannot be part of a `@key`.

###### `KEY_INVALID_FIELDS_TYPE`

Since v2.0.0

The value passed to the `fields` argument of a `@key` directive is not a string.

###### `KEY_INVALID_FIELDS`

Since v2.0.0

The `fields` argument of a `@key` directive is invalid (it has invalid syntax, includes unknown fields, ...).

###### `KEY_UNSUPPORTED_ON_INTERFACE`

Since v2.0.0

A `@key` directive is used on an interface, which is only supported when `@link`ing to Federation v2.3 or later.

###### `LINK_IMPORT_NAME_MISMATCH`

Since v2.0.0

The import name for a merged directive (as declared by the relevant `@link(import:)` argument) is inconsistent between subgraphs.

###### `MERGED_DIRECTIVE_APPLICATION_ON_EXTERNAL`

Since v2.0.0

In a subgraph, a field is both marked `@external` and has a merged directive applied to it.

###### `MISSING_ENTITY_CONNECTOR`

Since v2.10.0\*\*

A `@key` was defined without a corresponding entity connector.

###### `MISSING_HTTP_METHOD`

Since v2.10.0\*\*

The `@connect` directive is missing an HTTP method.

###### `MULTIPLE_HTTP_METHODS`

Since v2.10.0\*\*

The `@connect` directive has multiple HTTP methods when only one is allowed.

###### `MUTATION_FIELD_MISSING_CONNECT`

Since v2.10.0\*\*

A mutation field is missing the `@connect` directive.

###### `NO_QUERIES`

Since v2.0.0

None of the composed subgraphs expose any query.

###### `NO_SOURCE_IMPORT`

Since v2.10.0\*\*

The subgraph doesn't import the `@source` directive. This isn't necessarily a problem, but is likely a mistake.

###### `NO_SOURCES_DEFINED`

Since v2.10.0\*\*

This is a specialization of [`SOURCE_NAME_MISMATCH`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#source_name_mismatch) error that indicates no sources were defined.

###### `NULLABILITY_MISMATCH`

Since v2.10.0\*\*

A variable is nullable in a location which requires non-null at runtime.

###### `ONLY_INACCESSIBLE_CHILDREN`

Since v2.0.0

A type visible in the API schema has only `@inaccessible` children.

###### `OVERRIDE_COLLISION_WITH_ANOTHER_DIRECTIVE`

Since v2.0.0

The `@override` directive cannot be used on external fields, nor to override fields with either `@external`, `@provides`, or `@requires`.

###### `OVERRIDE_FROM_SELF_ERROR`

Since v2.0.0

Field with `@override` directive has "from" location that references its own subgraph.

###### `OVERRIDE_LABEL_INVALID`

Since v2.7.0

The `@override` directive `label` argument must match the pattern `/^[a-zA-Z][a-zA-Z0-9_-:./]*$/ or /^percent((d{1,2}(.d{1,8})?|100))$/`.

###### `OVERRIDE_ON_INTERFACE`

Since v2.3.0

The `@override` directive cannot be used on the fields of an interface type.

###### `OVERRIDE_SOURCE_HAS_OVERRIDE`

Since v2.0.0

Field which is overridden to another subgraph is also marked `@override`.

###### `PROVIDES_DIRECTIVE_IN_FIELDS_ARG`

Since v2.1.0

The `fields` argument of a `@provides` directive includes some directive applications. This is not supported.

###### `PROVIDES_FIELDS_HAS_ARGS`

Since v2.0.0

The `fields` argument of a `@provides` directive includes a field defined with arguments (which is not currently supported).

###### `PROVIDES_FIELDS_MISSING_EXTERNAL`

Since v0.x

The `fields` argument of a `@provides` directive includes a field that is not marked as `@external`.

###### `PROVIDES_INVALID_FIELDS_TYPE`

Since v2.0.0

The value passed to the `fields` argument of a `@provides` directive is not a string.

###### `PROVIDES_INVALID_FIELDS`

Since v2.0.0

The `fields` argument of a `@provides` directive is invalid (it has invalid syntax, includes unknown fields, ...).

###### `PROVIDES_ON_NON_OBJECT_FIELD`

Since v2.0.0

A `@provides` directive is used to mark a field whose base type is not an object type.

###### `PROVIDES_UNSUPPORTED_ON_INTERFACE`

Since v2.0.0

A `@provides` directive is used on an interface, which is not (yet) supported.

###### `QUERY_FIELD_MISSING_CONNECT`

Since v2.10.0\*\*

A query field is missing the `@connect` directive.

###### `QUERY_ROOT_TYPE_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` but is the query root type, which must be visible in the API schema.

###### `REFERENCED_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` but is referenced by an element visible in the API schema.

###### `RELATIVE_CONNECT_URL_WITHOUT_SOURCE`

Since v2.10.0\*\*

The `@connect` directive is using a relative URL (path only) but does not define a `source`. This is a a specialization of [`INVALID_URL`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#invalid-url).

###### `REQUIRED_ARGUMENT_MISSING_IN_SOME_SUBGRAPH`

Since v2.0.0

An argument of a field or directive definition is mandatory in some subgraphs, but the argument is not defined in all the subgraphs that define the field or directive definition.

###### `REQUIRED_INACCESSIBLE`

Since v2.0.0

An element is marked as `@inaccessible` but is required by an element visible in the API schema.

###### `REQUIRED_INPUT_FIELD_MISSING_IN_SOME_SUBGRAPH`

Since v2.0.0

A field of an input object type is mandatory in some subgraphs, but the field is not defined in all the subgraphs that define the input object type.

###### `REQUIRES_DIRECTIVE_IN_FIELDS_ARG`

Since v2.1.0

The `fields` argument of a `@requires` directive includes some directive applications. This is not supported.

###### `REQUIRES_FIELDS_MISSING_EXTERNAL`

Since v0.x

The `fields` argument of a `@requires` directive includes a field that is not marked as `@external`.

###### `REQUIRES_INVALID_FIELDS_TYPE`

Since v2.0.0

The value passed to the `fields` argument of a `@requires` directive is not a string.

###### `REQUIRES_INVALID_FIELDS`

Since v2.0.0

The `fields` argument of a `@requires` directive is invalid (it has invalid syntax, includes unknown fields, ...).

###### `REQUIRES_UNSUPPORTED_ON_INTERFACE`

Since v2.0.0

A `@requires` directive is used on an interface, which is not (yet) supported.

###### `ROOT_MUTATION_USED`

Since v0.x

A subgraph's schema defines a type with the name `mutation`, while also specifying a different type name as the root query object. This is not allowed.

###### `ROOT_QUERY_USED`

Since v0.x

A subgraph's schema defines a type with the name `query`, while also specifying a different type name as the root query object. This is not allowed.

###### `ROOT_SUBSCRIPTION_USED`

Since v0.x

A subgraph's schema defines a type with the name `subscription`, while also specifying a different type name as the root query object. This is not allowed.

###### `SATISFIABILITY_ERROR`

Since v2.0.0

Subgraphs can be merged, but the resulting supergraph API would have queries that cannot be satisfied by those subgraphs.

###### `SELECTED_FIELD_NOT_FOUND`

Since v2.10.0\*\*

A field included in a `@connect` directive's `selection` argument is not defined on the corresponding type.

###### `SHAREABLE_HAS_MISMATCHED_RUNTIME_TYPES`

Since v2.0.0

A shareable field return type has mismatched possible runtime types in the subgraphs in which the field is declared. As shared fields must resolve the same way in all subgraphs, this is almost surely a mistake.

###### `SOURCE_NAME_MISMATCH`

Since v2.10.0\*\*

The `source` argument used in a `@connect` directive doesn't match any named connecter sources created with `@source`.

###### `SUBSCRIPTION_IN_CONNECTORS`

Since v2.10.0\*\*

Connectors currently [don't support subscription operations](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations#subscriptions-are-unsupported).

###### `TYPE_DEFINITION_INVALID`

Since v2.0.0

A built-in or Federation type has an invalid definition in the schema.

###### `TYPE_KIND_MISMATCH`

Since v2.0.0

A type has the same name in different subgraphs, but a different kind. For instance, one definition is an object type but another is an interface.

Replaces `VALUE_TYPE_KIND_MISMATCH`, `EXTENSION_OF_WRONG_KIND`, `ENUM_MISMATCH_TYPE`.

###### `TYPE_WITH_ONLY_UNUSED_EXTERNAL`

Since v2.0.0

A Federation 1 schema has a composite type comprised only of unused external fields. Note that this error can only be raised for Federation 1 schema as Federation 2 schema do not allow unused external fields (and errors with code [`EXTERNAL_UNUSED`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#external_unused) will be raised in that case). But when Federation 1 schema are automatically migrated to Federation 2 ones, unused external fields are automatically removed, and in rare case this can leave a type empty. If that happens, an error with this code will be raised.

###### `UNDEFINED_ARGUMENT`

Since v2.10.0\*\*

Part of the `@connect` refers to an `$args` which is not defined.

###### `UNDEFINED_FIELD`

Since v2.10.0\*\*

Part of the `@connect` refers to an `$this` which is not defined.

###### `UNKNOWN_CONNECTORS_VERSION`

Since v2.10.0\*\*

The version set in the connectors `@link` URL is not recognized.

###### `UNKNOWN_FEDERATION_LINK_VERSION`

Since v2.0.0

The version of Federation in a `@link` directive on the schema is unknown.

###### `UNKNOWN_LINK_VERSION`

Since v2.1.0

The version of `@link` set on the schema is unknown.

###### `UNSUPPORTED_FEATURE`

Since v2.1.0

Indicates an error due to feature currently unsupported by Federation.

###### `UNSUPPORTED_LINKED_FEATURE`

Since v2.0.0

Indicates that a feature used in a `@link` is either unsupported or is used with unsupported options.

###### `UNSUPPORTED_VARIABLE_TYPE`

Since v2.10.0\*\*

A type used in a connector's variable is [not yet supported](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations) (i.e., unions).

\*\* Error codes introduced in v2.10.0 related to Apollo Connectors are subject to change.

## Removed codes

The following error codes have been removed and are no longer generated by the most recent version of the `@apollo/gateway` library:

Removed code
Comment

###### `DUPLICATE_ENUM_DEFINITION`

As duplicate enum definitions is invalid GraphQL, this will now be an error with code [`INVALID_GRAPHQL`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#invalid_graphql).

###### `DUPLICATE_ENUM_VALUE`

As duplicate enum values are invalid in GraphQL, this will now be an error with code [`INVALID_GRAPHQL`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#invalid_graphql).

###### `DUPLICATE_SCALAR_DEFINITION`

As duplicate scalar definitions are invalid in GraphQL, this will now be an error with code [`INVALID_GRAPHQL`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/errors.md#invalid_graphql).

###### `ENUM_MISMATCH`

Subgraph definitions for an enum are now merged by composition.

###### `EXTERNAL_USED_ON_BASE`

As there is no type ownership anymore, there is also no particular limitation as to where a field can be external.

###### `INTERFACE_FIELD_IMPLEM_TYPE_MISMATCH`

This error was thrown by a validation introduced to avoid running into a known runtime bug. Since Federation v2.3, the underlying runtime bug has been addressed and the validation/limitation was no longer necessary and has been removed.

###### `KEY_FIELDS_MISSING_EXTERNAL`

Using `@external` for key fields is now discouraged, unless the field is truly meant to be external.

###### `KEY_FIELDS_MISSING_ON_BASE`

Keys can now use any field from any other subgraph.

###### `KEY_MISSING_ON_BASE`

Each subgraph is now free to declare a key only if it needs it.

###### `KEY_NOT_SPECIFIED`

Each subgraph can declare a key independently of any other subgraph.

###### `MULTIPLE_KEYS_ON_EXTENSION`

Every subgraph can have multiple keys, as necessary.

###### `NON_REPEATABLE_DIRECTIVE_ARGUMENTS_MISMATCH`

Since Federation v2.1.0, the case this error used to cover is now a warning (with code `INCONSISTENT_NON_REPEATABLE_DIRECTIVE_ARGUMENTS`) instead of an error.

###### `PROVIDES_FIELDS_SELECT_INVALID_TYPE`

`@provides` can now be used on fields of interface, union, and list types.

###### `PROVIDES_NOT_ON_ENTITY`

`@provides` can now be used on any type.

###### `REQUIRES_FIELDS_HAS_ARGS`

Since Federation v2.1.1, using fields with arguments in a `@requires` is fully supported.

###### `REQUIRES_FIELDS_MISSING_ON_BASE`

Fields in `@requires` can now be from any subgraph.

###### `REQUIRES_USED_ON_BASE`

As there is no type ownership anymore, there is also no particular limitation as to which subgraph can use a `@requires`.

###### `RESERVED_FIELD_USED`

This error was previously not correctly enforced: the service and entities, if present, were overridden; this is still the case.

###### `VALUE_TYPE_NO_ENTITY`

There is no strong difference between entity and value types in the model (they are just usage patterns), and a type can have keys in one subgraph but not another.

###### `VALUE_TYPE_UNION_TYPES_MISMATCH`

Subgraph definitions for a union are now merged by composition.
