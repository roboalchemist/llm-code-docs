# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules.md

# Schema Linter Rules

This reference lists the rules that you can enforce with [GraphOS schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting), along with the code that GraphOS returns for each rule violation.

## Naming rules

These rules enforce naming conventions. Rules are categorized by the part(s) of your schema that they correspond to.

### Fields

The following example violates the rule:

```graphql title=❌ schema.graphql
type User {
  # highlight-start
  FirstName: String! # PascalCase
  # highlight-end
}
```

Use instead:

```graphql title=✅ schema.graphql
type User {
  # highlight-start
  firstName: String # camelCase
  # highlight-end
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type Query {
  getUsers: [User!]! # highlight-line
}
```

Use instead:

```graphql title=✅ schema.graphql
type Query {
  users: [User!]! # highlight-line
}
```

### Types

These rules apply to all types that appear in a GraphQL schema, including:

* Objects
* Interfaces
* Inputs
* Enums
* Unions

The following example violates the rule:

```graphql title=❌ schema.graphql
# highlight-start
type streamingService { # camelCase
  # highlight-end
  id: ID!
}
```

Use instead:

```graphql title=✅ schema.graphql
# highlight-start
type StreamingService { # PascalCase
  # highlight-end
  id: ID!
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type TypeBook { # highlight-line
  title: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
type Book { # highlight-line
  title: String!
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type BookType { # highlight-line
  title: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
type Book { # highlight-line
  title: String!
}
```

### Objects

The following example violates the rule:

```graphql title=❌ schema.graphql
type ObjectBook { # highlight-line
  title: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
type Book { # highlight-line
  title: String!
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type BookObject { # highlight-line
  title: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
type Book { # highlight-line
  title: String!
}
```

### Interfaces

The following example violates the rule:

```graphql title=❌ schema.graphql
interface InterfaceBook { # highlight-line
  title: String
  author: String
}
```

Use instead:

```graphql title=✅ schema.graphql
interface Book { # highlight-line
  title: String
  author: String
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
interface BookInterface { # highlight-line
  title: String
  author: String
}
```

Use instead:

```graphql title=✅ schema.graphql
interface Book { # highlight-line
  title: String
  author: String
}
```

### Inputs and arguments

The following example violates the rule:

```graphql title=❌ schema.graphql
type Mutation {
  #highlight-start
  createBlogPost(BlogPostContent: BlogPostContent!): Post # PascalCase
  #highlight-end
}
```

Use instead:

```graphql title=✅ schema.graphql
type Mutation {
  #highlight-start
  createBlogPost(blogPostContent: BlogPostContent!): Post # camelCase
  #highlight-end
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
input BlogPostDetails { #highlight-line
  title: String!
  content: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
input BlogPostDetailsInput { #highlight-line
  title: String!
  content: String!
}
```

### Enums

The following example violates the rule:

```graphql title=❌ schema.graphql
enum Amenity {
  # highlight-start
  public_park # snake_case
  # highlight-end
}
```

Use instead:

```graphql title=✅ schema.graphql
enum Amenity {
  # highlight-start
  PUBLIC_PARK # SCREAMING_SNAKE_CASE 😱
  # highlight-end
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
enum EnumResidence { # highlight-line
  HOUSE
  APARTMENT
  CONDO
}
```

Use instead:

```graphql title=✅ schema.graphql
enum Residence { # highlight-line
  HOUSE
  APARTMENT
  CONDO
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
enum ResidenceEnum { # highlight-line
  HOUSE
  APARTMENT
  CONDO
}
```

Use instead:

```graphql title=✅ schema.graphql
enum Residence { # highlight-line
  HOUSE
  APARTMENT
  CONDO
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
enum Role { # highlight-line
  EDITOR
  VIEWER
}

type Query {
  users(role: Role): [User!]! # highlight-line
}
```

Use instead:

```graphql title=✅ schema.graphql
enum RoleInput { # highlight-line
  EDITOR
  VIEWER
}

type Query {
  users(role: RoleInput): [User!]! # highlight-line
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
enum RoleInput { # highlight-line
  EDITOR
  VIEWER
}

type Query {
  userRole(userId: ID!): RoleInput # highlight-line
}
```

Use instead:

```graphql title=✅ schema.graphql
enum Role { # highlight-line
  EDITOR
  VIEWER
}

type Query {
  userRole(userId: ID!): Role # highlight-line
}
```

### Directives

The following example violates the rule:

```graphql title=❌ schema.graphql
directive @SpecialField on FIELD_DEFINITION # PascalCase
```

Use instead:

```graphql title=✅ schema.graphql
directive @specialField on FIELD_DEFINITION # camelCase
```

## Composition rules

Composition rules are only available for graphs on [federation version `2.4`](https://www.apollographql.com/docs/federation/federation-versions/#v24) or later. You can update a graph's version from its **Settings** page in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).

Composition rules flag potential improvements to subgraph schemas used to [compose](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition) a supergraph schema.

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

## Other rules

These rules define conventions for the entire schema and directive usage outside of composition.

### Schema

These rules apply to the entire schema.

The following example violates the rule:

```graphql title=❌ schema.graphql
type User {
  username: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
"Represents a user"
type User {
 "A username must be [8-64] characters."
 username: String!
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type SomeUnusedType { # Also fails the TYPE_SUFFIX rule!
  name: String!
}

type AnActuallyUsedType {
  name: String!
}

type Query {
  hello: String!
  title: AnActuallyUsedType
}
```

Use instead:

```graphql title=✅ schema.graphql
type Book {
  title: String!
}

type Query {
  books: [Book!]!
}
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type Query {
  users: [User!]!
}

#highlight-start
query GetUsers {
  # Don't define operations in a schema document
  users {
    id
  }
}
#highlight-end
```

### Directives

This example shows correct `@contact` directive usage:

```graphql title=✅ schema.graphql
"Annotate a schema with contact information for the subgraph owner"
directive @contact(
  "Contact title of the subgraph owner"
  name: String!
  "URL where the subgraph's owner can be reached"
  url: String
  "Other relevant notes can be included here; supports markdown links"
  description: String
) on SCHEMA

extend schema
  @contact(
    name: "Products Team"
    url: "https://myteam.slack.com/archives/teams-chat-room-url"
    description: "Send urgent issues to [#oncall](https://yourteam.slack.com/archives/oncall)."
  )
```

The following example violates the rule:

```graphql title=❌ schema.graphql
type Product {
  title: String @deprecated #highlight-line
  name: String!
}
```

Use instead:

```graphql title=✅ schema.graphql
type Product {
  title: String @deprecated(reason: "Use Product.name instead") #highlight-line
  name: String!
}
```

## Custom rules

The schema linter is [configurable](https://www.apollographql.com/docs/graphos/platform/schema-management/linting#linter-configuration) with the predefined rules documented above.
Custom rule creation isn't currently supported but is under consideration.
