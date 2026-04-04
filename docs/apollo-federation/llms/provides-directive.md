# Using the @provides Directive

The `@provides` directive optimizes query performance by reducing the number of subgraph calls needed to resolve queries.

This directive creates a relationship between two subgraphs:

* The source of truth subgraph owns the field and can always resolve it.
* The providing subgraph uses `@provides` to return the same data more efficiently at specific query paths.

Both subgraphs must resolve the field identically to ensure data consistency. It must not change the logic or behavior of your queries.

## When to use @provides

Use `@provides` when all of the following conditions are met:

* The query works without `@provides`. The directive only improves performance; it never changes the logical behavior of your GraphQL operations.

* The data is identical. Both subgraphs must resolve the field identically to ensure data consistency.

* You can maintain data consistency between the source of truth and the providing subgraph.

* You have a specific performance goal to reduce the number of subgraph calls.

* The optimization is specific to a query path. The optimization must be scoped to a specific query path instead of any entry point that can reach the provided fields.

* You can ensure privacy and security compliance. Storing and accessing the provided data in the providing subgraph's storage system must comply with your organization's privacy and security requirements.

### Identifying common use cases

You can use `@provides` for the following scenarios:

* **Search optimization**: A search subgraph (for example, backed by Elasticsearch) returns fields owned by another subgraph to avoid additional round trips. For example, a search index might store product names and prices alongside search metadata, allowing it to return product information without calling the Products subgraph.

* **Read-only computed fields**: Fields that derive their value from other fields and have no side effects, where the providing subgraph can compute them identically. For example, a search subgraph might compute a relevance score or ranking that matches what the source subgraph calculates.

* **Optimized data stores**: Specialized stores (Elasticsearch, Redis, and others) that contain a subset of data from the source of truth reduce subgraph calls for specific query paths. The specialized store returns frequently accessed fields directly, avoiding a round trip to the source.

* **Performance-critical queries**: Frequently executed queries benefit from reducing the number of subgraph calls. If a query path is called thousands of times per second, eliminating even one subgraph call significantly reduces latency and load.

## Ensuring data consistency

Composition rules ensure your schema is valid, but they don't guarantee that your data is consistent. You're responsible for maintaining data consistency.

* **Data retention**: The providing subgraph and the source of truth subgraph might have different data retention policies. This is acceptable as long as the providing subgraph has all the data needed for the queries that use `@provides`. Document the query's scope clearly.

* **Eventual consistency**: Account for eventual consistency—the time delay between when data is updated in the source of truth and when it synchronizes to the providing subgraph. Use `@provides` only when eventual consistency is acceptable for your use case.

## When to avoid using `@provides`

Avoid using `@provides` in these scenarios:

* **Fixing slow subgraph performance**: `@provides` is a query planning optimization, not a fix for slow queries or database bottlenecks. Bypassing a slow subgraph with `@provides` hides the problem and adds complexity without addressing the root cause. Optimize at the subgraph level instead by using database tuning, caching, or query optimization.

* **Introducing logical differences**: The provided data must match the source data exactly. Do not use `@provides` to introduce logical differences or alternate data sources.

* **Possible data divergence**: If there's any possibility of data divergence, don't use `@provides`. This includes scenarios where data retention policies differ significantly and cannot be mitigated through query scope, eventual consistency delays are unacceptable for your use case, or different subgraphs might resolve the field differently.

* **Hiding data inconsistencies**: Never use `@provides` to hide conflicting data between subgraphs. Fix the data at the source.

* **Sensitive data without compliance**: Don't use `@provides` for sensitive data (PII, financial information, and other sensitive fields) unless the providing subgraph's storage system is approved and compliant with all relevant regulations.

## Implementing `@provides` in your schema

Implement `@provides` in your schema:

1. Test your query to confirm it works without `@provides`.
2. Verify that data is identical across subgraphs to ensure consistency.
3. Mark the field as `@shareable` in the source-of-truth subgraph.

```graphql title=Products subgraph (source of truth)
type Product @key(fields: "id") {
  id: ID!
  price: Float! @shareable  # Step 3: mark the field as @shareable
}
```

4. Mark the field as `@external` in the providing subgraph.
5. Add `@provides` to the query path that returns the provided field.

```graphql title=Search subgraph (providing subgraph)
type Product @key(fields: "id") {
  id: ID!
  price: Float! @external # Step 4: mark the field as @external
}

type SearchResult {
  products: [Product!]! @provides(fields: "price") # Step 5: add @provides to the query path that returns the provided field
}
```

6. Monitor performance to verify that the optimization works.

### Composition rules

Apollo Federation enforces these composition rules. If a subgraph provides an entity field using `@provides`:

* The subgraph must define that field and mark it `@external`.
* The entity field must be marked as either `@shareable` or `@external` in every subgraph that defines it.
* The entity field must be marked as `@shareable` in at least one other subgraph so that at least one subgraph can always resolve the field.

Composition fails if you violate these rules.

## Verifying your optimization

When the router encounters a query with a field that uses `@provides`, it determines if it can satisfy the entire query from the providing subgraph. If it can, it makes a single subgraph call and skips the source of truth—that's the optimization. If it can't, it falls back to calling both subgraphs and there is no optimization.

To verify that the optimization is working, compare the before and after for the operation's [query plan](https://www.apollographql.com/docs/graphos/platform/explorer/additional-features#query-plans-for-supergraphs) and [metrics](https://www.apollographql.com/docs/graphos/platform/insights/operation-metrics#operation-metrics) in GraphOS Studio.

### Example: No optimization

In this example, the providing subgraph (the Search subgraph) only provides the `price` field.

```graphql title=Products subgraph (source of truth)
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Float! @shareable
  description: String!
}
```

```graphql title=Search subgraph (providing subgraph)
type Product @key(fields: "id") {
  id: ID!
  price: Float! @external
}

type SearchResult {
  products: [Product!]! @provides(fields: "price")  # Only provides price
}

type Query {
  searchProducts(query: String!): SearchResult
}
```

However, the query requests multiple fields for a product: `id`, `name`, `price`, and `description`. The router must call the Products subgraph for the rest—no optimization.

```graphql title=Query
query {
  searchProducts(query: "laptop") { # Router calls Search subgraph
    products {
      id
      price      # @provides only covers this field
      name
      description # Router still needs to call Products subgraph for id, name, description fields
    }
  }
}
```

The query plan contains 2 subgraph calls:

* Call 1: Search subgraph (list of products and their price)
* Call 2: Products subgraph (id, name, description)

This results in a failed optimization with no benefits.

### Example: Successful optimization

In this example, the providing subgraph (the Search subgraph) provides the `name` and `price` fields.

```graphql title=Products subgraph (source of truth)
type Product @key(fields: "id") {
  id: ID!
  name: String! @shareable
  price: Float! @shareable
}
```

```graphql title=Search subgraph (providing subgraph)
type Product @key(fields: "id") {
  id: ID!
  name: String! @external
  price: Float! @external
}

type SearchResult {
  products: [Product!]! @provides(fields: "name price")  # Provides all needed fields
}

type Query {
  searchProducts(query: String!): SearchResult
}
```

```graphql title=Query
query {
  searchProducts(query: "laptop") { # Router calls Search subgraph
    products {
      id         # All fields are provided, no need to call the Products subgraph
      name
      price
    }
  }
}
```

The query plan contains a single subgraph call to the Search subgraph to return the `id`, `name`, and `price` fields. This is a successful optimization.

## Examples for using @provides

### Data retention with documented scope

In this example, the Products subgraph (source of truth) has all historical data, but the Search subgraph (providing subgraph) only has data from the last 30 days.

```graphql title=Products subgraph (source of truth - all historical data)
type Product @key(fields: "id") {
  id: ID!
  name: String! @shareable
  price: Float! @shareable
}
```

```graphql title=Search subgraph (providing subgraph - 30 days retention)
type Product @key(fields: "id", resolvable: false) {
  id: ID!
  name: String! @external
  price: Float! @external
}

type Query {
  """Searches for products added in the last 30 days"""
  searchRecentProducts(query: String!): [Product!]! @provides(fields: "name price")
}
```

The query is documented to only search products from the last 30 days, and the backing data source (for example, Elasticsearch) retains 30+ days of data. The query path itself limits the scope, making `@provides` valid even though overall retention differs.

### Privacy-compliant field selection

In this example, the Users subgraph (source of truth) provides all user data, but the Search subgraph (providing subgraph) provides only non-sensitive fields.

```graphql title=Users subgraph (source of truth)
type User @key(fields: "id") {
  id: ID!
  username: String! @shareable
  displayName: String! @shareable
  email: String!
  phoneNumber: String!
  ssn: String!
}
```

```graphql title=Search subgraph (providing only non-sensitive fields)
type User @key(fields: "id") {
  id: ID!
  username: String! @external
  displayName: String! @external
  # email, phoneNumber, ssn are NOT provided
}

type SearchResult {
  users: [User!]! @provides(fields: "username displayName")
}

type Query {
  searchUsers(query: String!): SearchResult
}
```

Only non-sensitive fields are provided. Sensitive fields (`email`, `phoneNumber`, `ssn`) remain in the Users subgraph even though Elasticsearch might have access to them, ensuring compliance with privacy and security requirements.

### Using @provides with interface implementations

In this example, `Product` is an interface type with two implementing types: `PhysicalProduct` and `DigitalProduct`. Both the Products subgraph (source of truth) and the Search subgraph (providing subgraph) can provide data for each implementing type.

```graphql title=Products subgraph (source of truth)
interface Product @key(fields: "id") {
  id: ID!
  title: String!
}

type PhysicalProduct implements Product @key(fields: "id") {
  id: ID!
  title: String! @shareable
  width: Float! @shareable
  height: Float! @shareable
  depth: Float! @shareable
}

type DigitalProduct implements Product @key(fields: "id") {
  id: ID!
  title: String! @shareable
  downloadSize: Int! @shareable
  fileFormat: String! @shareable
  licenseType: String! @shareable
}
```

```graphql title=Search subgraph (providing subgraph)

type Query {
  searchProducts: Product @provides(fields: """ 
    ... on PhysicalProduct {
      title
      width
      height
      depth
    }
    ... on DigitalProduct {
      title
      downloadSize
      fileFormat
      licenseType
    }
  """)
}

interface Product @key(fields: "id", resolvable: false) {
  id: ID!
  title: String!
}

type PhysicalProduct implements Product @key(fields: "id", resolvable: false) {
  id: ID!
  title: String! @external
  width: Float! @external
  height: Float! @external
  depth: Float! @external
}

type DigitalProduct implements Product @key(fields: "id", resolvable: false) {
  id: ID!
  title: String! @external
  downloadSize: Int! @external
  fileFormat: String! @external
  licenseType: String! @external
}
```

The `searchProducts` query provides fields for both `PhysicalProduct` and `DigitalProduct` using inline fragments to specify which fields to provide for each implementing type.

### Using @provides with interface objects

```graphql title=Products subgraph (source of truth)
interface Product @key(fields: "id") {
  id: ID!
  title: String!
}

type PhysicalProduct implements Product @key(fields: "id") {
  id: ID!
  title: String! @shareable
  width: Float! @shareable
  height: Float! @shareable
  depth: Float! @shareable
}

type DigitalProduct implements Product @key(fields: "id") {
  id: ID!
  title: String! @shareable
  downloadSize: Int! @shareable
  fileFormat: String! @shareable
  licenseType: String! @shareable
}
```

```graphql title=Search subgraph (providing subgraph)
type Query {
  searchProducts: Product @provides(fields: "title")
}

type Product @key(fields: "id", resolvable: false) @interfaceObject {
  id: ID!
  title: String! @external
}
```

The `searchProducts` query provides the `title` field for the `Product` interface object using `@interfaceObject`.

When using `@provides` on an `@interfaceObject` type, every implementation of that interface must mark the provided field as `@shareable` because `@shareable` and `@external` cannot be used on interfaces. In this example, both `PhysicalProduct` and `DigitalProduct` mark `title` as `@shareable`.

### Using @provides with unions

In this example, `Product` is a union type with two member types: `PhysicalProduct` and `DigitalProduct`. Both the Products subgraph (source of truth) and the Search subgraph (providing subgraph) provide data for each member type.

```graphql title=Products subgraph (source of truth)
type PhysicalProduct @key(fields: "id") {
  id: ID!
  title: String! @shareable
  width: Float! @shareable
  height: Float! @shareable
  depth: Float! @shareable
}

type DigitalProduct @key(fields: "id") {
  id: ID!
  title: String! @shareable
  downloadSize: Int! @shareable
  fileFormat: String! @shareable
  licenseType: String! @shareable
}

union Product = PhysicalProduct | DigitalProduct
```

```graphql title=Search subgraph (providing subgraph)
type Query {
  searchProducts: Product @provides(fields: """
    ... on PhysicalProduct {
      title
      width
      height
      depth
    }
    ... on DigitalProduct {
      title
      downloadSize
      fileFormat
      licenseType
    }
  """)
}

type PhysicalProduct @key(fields: "id", resolvable: false) {
  id: ID!
  title: String! @external
  width: Float! @external
  height: Float! @external
  depth: Float! @external
}

type DigitalProduct @key(fields: "id", resolvable: false) {
  id: ID!
  title: String! @external
  downloadSize: Int! @external
  fileFormat: String! @external
  licenseType: String! @external
}

union Product = PhysicalProduct | DigitalProduct
```

The `searchProducts` query provides fields for union members using inline fragments to specify which fields to provide for each union member type.
