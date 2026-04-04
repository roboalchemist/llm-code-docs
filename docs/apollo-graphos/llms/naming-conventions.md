# Source: https://www.apollographql.com/docs/graphos/schema-design/guides/naming-conventions.md

# Schema Naming Conventions

If you're an enterprise customer looking for more material on this topic, try the [Enterprise best practices: Schema design](https://www.apollographql.com/tutorials/schema-design-best-practices) course on Odyssey.

Not an enterprise customer? [Learn about GraphOS for Enterprise.](https://www.apollographql.com/pricing?referrer=docs-content)

## Enforcing conventions

Use GraphOS [schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting) to catch naming violations. GraphOS schema linting can be done within [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) which can allow you to enforce this in your CI/CD pipelines, or it can be run using [Rover](https://www.apollographql.com/docs/graphos/platform/schema-management/linting#one-off-linting) for one-off requests locally.

## High-level guidance

* Regardless of your chosen conventions, be consistent across the entire schema.
* Be specific with names—don't "land grab" names with broad applicability.
* Avoid acronyms, initialisms, and abbreviations.

### Casing

Use `camelCase` for field names, argument names, and directive names:

```graphql
type Query {
  myCamelCaseFieldNames(myArgumentName: String): String
}

directive @myDirective on FIELD
```

Use `PascalCase` for type names:

```graphql
type MyType { ... }

enum MyEnum { ... }

interface MyInterface { ... }

union MyUnion = ...

scalar MyScalar
```

Use `SCREAMING_SNAKE_CASE` for enum values:

```graphql
enum MyEnum {
  VALUE_ONE
  VALUE_TWO
}
```

### Field names

Avoid verb prefixes like `get` or `list` on query (read) fields:

```graphql
type Query {
  # ❌ incorrect
  getProducts: [Product]

  # ✅ correct
  products: [Product]
}
```

This creates consistency between root fields and nested fields:

```graphql
# ❌ incorrect
query Products {
  getProducts {
    id
    getReviews {
      content
    }
  }
}

# ✅ correct
query Products {
  products {
    id
    reviews {
      content
    }
  }
}
```

Start mutation fields with a verb:

```graphql
type Mutation {
  # ❌ incorrect
  customerAdd(input: AddCustomerInput): AddCustomerPayload!

  # ✅ correct
  addCustomer(input: AddCustomerInput): AddCustomerPayload!
}
```

### Type names

Use the suffix `Input` when naming input types:

```graphql
input AddCustomerInput {
  name: String!
}
```

Use a consistent suffix like `Response` or `Payload` when naming output types returned from mutations:

```graphql
type Mutation {
  addCustomer(input: AddCustomerInput!): AddCustomerResponse!
}

type AddCustomerResponse {
  success: Boolean!
}
```

## Additional considerations

### Namespacing

When resolving naming conflicts between different domains, we recommend using one of the following:

#### `PascalCase` prefix

```graphql
type StoreCustomer { ... }
type SiteCustomer { ... }
```

#### `Single_Underscore` prefix

```graphql
type Store_Customer { ... }
type Site_Customer { ... }
```
