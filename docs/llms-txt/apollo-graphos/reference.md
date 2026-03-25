# Source: https://www.apollographql.com/docs/graphos/routing/customization/rhai/reference.md

# Source: https://www.apollographql.com/docs/graphos/routing/customization/coprocessor/reference.md

# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/checks/reference.md

# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/reference.md

# Contract Reference

## Rules for `@tag`s and contracts

### Valid `@tag` locations

In both Federation 1 and Federation 2, you can apply tags to the following schema elements to filter your contract schema:

* Object, interface, and union type definitions
* Fields of object types
  * Federation 1 doesn't support tagging fields of interface types.
  * In Federation 1, you can still make an interface field inaccessible by tagging the interface definition or by ensuring that object fields that implement the interface field are removed.

In Federation 2 only, you can also apply tags to the following:

* Fields of interface types
* Enum types and their values
* Input types and their fields
* Definitions of custom scalar types
* Arguments of fields, but not directive arguments

### Valid `@tag` names

* `@tag` names can include alphanumeric characters (`a-z`, `A-Z`, `0-9`), along with hyphens (`-`) and forward slashes (`/`).
* Each tag name cannot exceed 128 characters.

```graphql
type User {
  id: ID!
  name: String! @tag(name: "a/b/c/1-2-3")
}
```

### Dependent `@tag`s

* Whenever you tag the definition of an object or interface type, GraphOS automatically considers that tag to be applied to all fields of that type:

  ```graphql
  type InternalUser @tag(name: "internal") {
    id: ID! # Also considered to have @tag(name: "internal")
  }
  ```

* Whenever you tag the definition of an object, interface, or union type, you should always apply that same tag to every field that returns that type:

  ```graphql
  type BillingAccount @tag(name: "internal") {
    id: ID!
    acctNumber: String!
  }

  type Query {
    billingAccounts: [BillingAccount!]! @tag(name: "internal")
  }
  ```

  If you don't do this, a contract might exclude a type while including fields that return that type. This produces an invalid contract schema.

* If a contract excludes an object that implements an interface or is included in a union:

  * The contract is not required to exclude schema fields that return that interface or union as long as at least one other associated object type remains:

    ```graphql
    # Two object types implement this interface.
    interface Identity {
      id: ID!
      name: String!
    }

    # If this implementing type is excluded...
    type InternalUser implements Identity @tag(name: "internal") {
      id: ID!
      name: String!
    }

    # ...but this implementing type remains...
    type ExternalUser implements Identity {
      id: ID!
      name: String!
    }

    type Query {
      # ...then this field doesn't need to be excluded.
      currentIdentity: Identity
    }
    ```

  * However, if a subgraph resolves one of these fields by returning an object of an excluded type, a runtime error occurs in the router and the operation fails.

### Special cases for filtering

* If a contract defines a list of included `@tags`, any object or interface type without an included tag is still included in the contract schema if at least one of its fields is included:

  ```graphql
  # This type definition is included because one if its fields is included.
  type User {
    id: ID! @tag(name: "includeMe")
  }
  ```

* If a contract excludes every field of an object or interface type, the entire type definition is excluded from the contract schema:

  ```graphql
  # This object type is excluded because all its fields are excluded.
  type User {
    id: ID! @tag(name: "excludeMe")
  }
  ```

  This can produce an invalid contract schema if any fields that return the excluded type are included.

* If a contract excludes every object type that's part of a union type, the entire union type definition is excluded from the contract schema:

  ```graphql
  # This union type is excluded because all its possible types are excluded.
  union Media = Book | Movie

  type Book @tag(name: "excludeMe") {
    title: String!
  }

  type Movie @tag(name: "excludeMe") {
    title: String!
  }
  ```

  This can produce an invalid contract schema if any fields that return the excluded union type are included.

* A contract cannot exclude any of the following, even if tagged:

  * Built-in scalars (`Int`, `Float`, etc.)
  * Built-in directives (`@skip`, `@include`, etc.)
  * Custom directives that are applied to type system locations ([see the list](https://spec.graphql.org/October2021/#TypeSystemDirectiveLocation))

* A contract can exclude object fields that are used in a computed field's [`@requires` directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#referencing-an-entity-without-contributing-fields) without causing runtime errors.

## Errors

GraphOS may encounter the following errors when creating or updating a contract schema.
Errors descriptions include the step in the creation process where the error occurred:

Error
Description

##### `ADD_DIRECTIVE_DEFINITIONS_IF_NOT_PRESENT`

An error occurred adding directive definitions for `@tag`, `@inaccessible`, and core directive usages.

##### `DIRECTIVE_DEFINITION_LOCATION_AUGMENTING`

An error occurred augmenting the directive definition for `@tag` to support `OBJECT`, `FIELD_DEFINITION`, `INTERFACE`, and `UNION`.

##### `EMPTY_OBJECT_AND_INTERFACE_MASKING`

All of an object or interface type's fields were excluded, and an error occurred while excluding the entire type.

##### `EMPTY_UNION_MASKING`

All of a union type's included types were excluded, and an error occurred while excluding the entire union.

##### `INPUT_VALIDATION`

The contract is attempting to include and exclude the same tag.

##### `PARSING`

After including and excluding fields, the resulting contract schema failed to parse.

##### `PARSING_TAG_DIRECTIVES`

GraphOS encountered an error while trying to obtain all uses of `@tag` from the source variant schema.

##### `PARTIAL_INTERFACE_MASKING`

An interface field's return type was excluded, and an error occurred while excluding that interface field.

##### `SCHEMA_RETRIEVAL`

GraphOS encountered an error while retrieving the source variant's schema. It might not yet have a valid composed schema.

##### `TAG_INHERITING`

GraphOS encountered an error while attempting to add parent tags to fields.

##### `TAG_MATCHING`

GraphOS encountered an error determining which types and fields should be inaccessible based on their tags.

##### `TO_API_SCHEMA`

GraphOS encountered an error while attempting to generate an API schema from the contract variant's supergraph schema.

##### `TO_FILTER_SCHEMA`

GraphOS failed to generate and return a contract supergraph schema for an unknown reason.

##### `UNKNOWN`

An unknown error occurred.

##### `UNREACHABLE_TYPE_MASKING`

GraphOS encountered an error while attempting to exclude unreachable types in the resulting contract schema.

##### `VERSION_CHECK`

Contracts do not support the Federation version used.
