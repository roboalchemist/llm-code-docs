# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/hints.md

# Composition Hints

When you successfully compose your subgraph schemas into a supergraph schema, the composition process can flag potential improvements or hints. Hints are violations of the [GraphOS schema linter's](https://www.apollographql.com/docs/graphos/platform/schema-management/linting) [composition rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules#composition-rules). You can review them on the [Checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) page in GraphOS Studio or via the [Rover CLI](https://www.apollographql.com/docs/rover/).

Composition hints only appear in GraphOS Studio and via the `rover subgraph check` command for graphs on [federation version `2.4`](https://www.apollographql.com/docs/federation/federation-versions/#v24) or later. You can update a graph's version from its **Settings** page in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).

The [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs#subgraph-check) command outputs rule violations with the [severity levels](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/#setting-severity-levels) you've configured for your graph variant. The [`rover supergraph compose`](https://www.apollographql.com/docs/rover/commands/supergraphs#supergraph-compose) command outputs rule violations for all local subgraph schemas.

See below for a list of composition rules categorized by rule type. The heading for each rule is the code that GraphOS returns for the rule violation. Refer to the [rules reference page](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules) for a comprehensive list of linter rules.

### Inconsistent elements

These rules identity inconsistencies in fields, types, arguments, etc across subgraphs. Such inconsistencies can disrupt or even break [composition](https://www.apollographql.com/docs/federation/federated-types/composition).

#### Compatibility

In some cases, inconsistency rules also indicate the compatibility of checked types. Two types are compatible if one is a non-nullable version, a list version, a subtype, or a combination of any of these of the other.

For example, the `price` fields in the example subgraphs below are inconsistent and incompatible because they use completely different types (`Float` vs `String`):

```graphql title=Subgraph A
type Product {
  id: ID!
  name: String
  price: Float #highlight-line
}
```

```graphql title=Subgraph B
type Product {
  id: ID!
  name: String
  price: String #highlight-line
}
```

These `price` fields in the example subgraphs below are inconsistent but compatible since both use `Float`s, but one is nullable and the other is the non-nullable list of `Float`s.

```graphql title=Subgraph A
type Product {
  id: ID!
  name: String
  price: Float #highlight-line
}
```

```graphql title=Subgraph B
type Product {
  id: ID!
  name: String
  price: [Float]! #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
  price(currency: Currency): Float #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
  price(currency: Currency, taxIncluded: Boolean): Float #highlight-line
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
  price(currency: Currency, taxIncluded: Boolean): Float #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
  price(currency: Currency, taxIncluded: Boolean): Float #highlight-line
}
```

Because subgraph A's `price` field expects a non-nullable `Currency` argument type and subgraph B allows a nullable `Currency` argument type, the following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
  price(currency: Currency!): Float #highlight-line
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
  price(currency: Currency): Float #highlight-line
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
  price(currency: Currency!): Float #highlight-line
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
  price(currency: Currency!): Float #highlight-line
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
  price: Money #highlight-line
}

type Money {
  amount: Float!
  currency: Currency!
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
  price: Money! #highlight-line
}

type Money {
  amount: Float!
  currency: Currency!
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
  price: Money! #highlight-line
}

type Money {
  amount: Float!
  currency: Currency!
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
  price: Money! #highlight-line
}

type Money {
  amount: Float!
  currency: Currency!
}

enum Currency {
  USD
  EUR
  GBP
  JPY
  AUD
  CAD
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
  weight(kg: Float = 1.0): Float #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
  weight(kg: Float): Float #highlight-line
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
  weight(kg: Float = 1.0): Float #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
  weight(kg: Float = 1.0): Float #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
"""
A type representing a product.
"""
type Product {
  id: ID!
  name: String
}
```

```graphql title=❌ Subgraph B
"""
An object representing a product.
"""
type Product {
  id: ID!
  name: String
}
```

Use instead:

```graphql title=✅ Subgraph A
"""
A type representing a product.
"""
type Product {
  id: ID!
  name: String
}
```

```graphql title=✅ Subgraph B
"""
A type representing a product.
"""
type Product {
  id: ID!
  name: String
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product
  @key(fields: "id") { #highlight-line
  id: ID!
  name: String
}
```

```graphql title=❌ Subgraph B
type Product { #highlight-line
  id: ID!
  stock: Int
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product
  @key(fields: "id") { #highlight-line
  id: ID!
  name: String
}
```

```graphql title=✅ Subgraph B
type Product
  @key(fields: "id") { #highlight-line
  id: ID!
  stock: Int
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
  BACK_ORDER #highlight-line
}

input ProductInput {
  name: String!
  status: ProductStatus!
}
```

```graphql title=❌ Subgraph B
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
}

input ProductInput {
  name: String!
  status: ProductStatus!
}
```

Use instead:

```graphql title=✅ Subgraph A
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
  BACK_ORDER
}

input ProductInput {
  name: String!
  status: ProductStatus!
}
```

```graphql title=✅ Subgraph B
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
  BACK_ORDER
}

input ProductInput {
  name: String!
  status: ProductStatus!
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
enum OrderStatus {
  CREATED
  PROCESSING #highlight-line
  COMPLETED
}

type Order {
  name: String!
  status: OrderStatus!
}
```

```graphql title=❌ Subgraph B
enum OrderStatus {
  CREATED
  COMPLETED
}

type Order {
  name: String!
  status: OrderStatus!
}
```

Use instead:

```graphql title=✅ Subgraph A
enum OrderStatus {
  CREATED
  PROCESSING
  COMPLETED
}

type Order {
  name: String!
  status: OrderStatus!
}
```

```graphql title=✅ Subgraph B
enum OrderStatus {
  CREATED
  PROCESSING
  COMPLETED
}

type Order {
  name: String!
  status: OrderStatus!
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @log(message: String!) on QUERY #highlight-line
```

```graphql title=❌ Subgraph B
directive @log(message: String!) on FIELD #highlight-line
```

Use instead:

```graphql title=✅ Subgraph A
directive @log(message: String!) on QUERY | FIELD
```

```graphql title=✅ Subgraph B
directive @log(message: String!) on QUERY | FIELD
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @modify(field: String!) on FIELD
```

```graphql title=❌ Subgraph B
# 🦗🦗🦗
```

Use instead:

```graphql title=✅ Subgraph A
directive @modify(field: String!) on FIELD
```

```graphql title=✅ Subgraph B
directive @modify(field: String!) on FIELD
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @validateLength(max: Int!) repeatable on FIELD
```

```graphql title=❌ Subgraph B
directive @validateLength(max: Int!) on FIELD
```

Use instead:

```graphql title=✅ Subgraph A
directive @validateLength(max: Int!) repeatable on FIELD
```

```graphql title=✅ Subgraph B
directive @validateLength(max: Int!) repeatable on FIELD
```

The following example violates the rule:

```graphql title=❌ Subgraph A
input ProductInput {
  name: String
  price: Float #highlight-line
}

input OrderInput {
  product: ProductInput
}
```

```graphql title=❌ Subgraph B
input ProductInput {
  name: String
}

input OrderInput {
  product: ProductInput
}
```

Use instead:

```graphql title=✅ Subgraph A
input ProductInput {
  name: String
  price: Float
}

input OrderInput {
  product: ProductInput
}
```

```graphql title=✅ Subgraph B
input ProductInput {
  name: String
  price: Float
}

input OrderInput {
  product: ProductInput
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
interface Product {
  id: ID!
  name: String
  cost: Float #highlight-line
}

type DigitalProduct implements Product {
  id: ID!
  name: String
  cost: Float
  size: Int
}
```

```graphql title=❌ Subgraph B
interface Product {
  id: ID!
  name: String
  # cost is not defined in the interface
}

type PhysicalProduct implements Product {
  id: ID!
  name: String
  cost: Float
  weight: Float
}
```

Use instead:

```graphql title=✅ Subgraph A
interface Product {
  id: ID!
  name: String
  cost: Float #highlight-line
}

type DigitalProduct implements Product {
  id: ID!
  name: String
  cost: Float
  size: Int
}
```

```graphql title=✅ Subgraph B
interface Product {
  id: ID!
  name: String
  cost: Float #highlight-line
}

type PhysicalProduct implements Product {
  id: ID!
  name: String
  cost: Float
  weight: Float
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
}

type Query {
  allProducts: [Product] @customDirective(orderBy: "name") #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
}

type Query {
  allProducts: [Product] @customDirective(orderBy: "price") #highlight-line
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
}

type Query {
  allProducts: [Product] @customDirective(orderBy: "name") #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
}

type Query {
  allProducts: [Product] @customDirective(orderBy: "name") #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID! @shareable
  name: String @shareable
  price: Float #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID! @shareable
  name: String @shareable
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product @shareable {
  id: ID!
  name: String
  price: Float #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product @shareable {
  id: ID!
  name: String
  price: Float #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
  details: Details @shareable #highlight-line
}

type Details {
  size: String #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
  details: Details @shareable #highlight-line
}

type Details {
  weight: Float #highlight-line
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
  details: Details @shareable #highlight-line
}

type Details {
  size: String #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
  details: Details @shareable #highlight-line
}

type Details {
  size: String #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @customDirective(message: String!) on OBJECT | FIELD_DEFINITION #highlight-line
```

```graphql title=❌ Subgraph B
directive @customDirective(message: String!) on FIELD_DEFINITION #highlight-line
```

Use instead:

```graphql title=✅ Subgraph A
directive @customDirective(message: String!) on OBJECT | FIELD_DEFINITION
```

```graphql title=✅ Subgraph B
directive @customDirective(message: String!) on OBJECT | FIELD_DEFINITION
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @customDirective on OBJECT
```

```graphql title=❌ Subgraph B
directive @customDirective repeatable on OBJECT
```

Use instead:

```graphql title=✅ Subgraph A
directive @customDirective repeatable on OBJECT
```

```graphql title=✅ Subgraph B
directive @customDirective repeatable on OBJECT
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
}

type Service {
  id: ID!
  description: String
}

union SearchResult = Product | Service #highlight-line
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
}

union SearchResult = Product #highlight-line
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
}

type Service {
  id: ID!
  description: String
}

union SearchResult = Product | Service #highlight-line
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
}

type Service {
  id: ID!
  description: String
}

union SearchResult = Product | Service #highlight-line
```

### Overridden and unused elements

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Subgraph B")
}
```

```graphql title=❌ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean!
}
```

```graphql title=✅ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Subgraph B")
}
```

```graphql title=❌ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
  inStock: Boolean!
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  name: String!
  inStock: Boolean!
}
```

```graphql title=✅ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Subgraph B", label: "percent(50)")
}
```

```graphql title=❌ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
  inStock: Boolean!
}
```

After completing the migration, use instead:

```graphql title=✅ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  name: String!
  inStock: Boolean!
}
```

```graphql title=✅ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  name: String!
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
}

type Product {
  id: ID!
  name: String
}
```

```graphql title=❌ Subgraph B
type Order {
  id: ID!
  product: Product
  status: String
}
```

Use instead:

```graphql title=✅ Subgraph A
enum ProductStatus {
  AVAILABLE
  SOLD_OUT
}

type Product {
  id: ID!
  name: String
  status: ProductStatus
}
```

```graphql title=✅ Subgraph B
type Order {
  id: ID!
  product: Product
  status: ProductStatus
}
```

### Directives

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product {
  id: ID!
  name: String
}

type Query {
  products: [Product] @customDirective(orderBy: ["name"]) #highlight-line
}
```

```graphql title=❌ Subgraph B
type Product {
  id: ID!
  name: String
}

type Query {
  products: [Product] @customDirective(orderBy: ["price"]) #highlight-line
}
```

Use instead:

```graphql title=✅ Subgraph A
type Product {
  id: ID!
  name: String
}

type Query {
  products: [Product] @customDirective(orderBy: ["name", "price"]) #highlight-line
}
```

```graphql title=✅ Subgraph B
type Product {
  id: ID!
  name: String
}

type Query {
  products: [Product] @customDirective(orderBy: ["name", "price"]) #highlight-line
}
```

The following example violates the rule:

```graphql title=❌ Subgraph A
directive @log(message: String!) on QUERY #highlight-line
```

```graphql title=❌ Subgraph B
directive @log(message: String!) on FIELD #highlight-line
```

Use instead:

```graphql title=✅ Subgraph A
directive @log(message: String!) on QUERY | FIELD
```

```graphql title=✅ Subgraph B
directive @log(message: String!) on QUERY | FIELD
```

The following example violates the rule:

```graphql title=❌ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Subgraph B")
}
```

```graphql title=❌ Subgraph B
# Subgraph B doesn't exist
```

Use instead:

```graphql title=✅ Subgraph A
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Subgraph B")
}
```

```graphql title=✅ Subgraph B
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean!
}
```
