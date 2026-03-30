# Source: https://www.apollographql.com/docs/graphos/schema-design/guides/federated-directives/shareable-directive.md

# Using the @shareable Directive

The `@shareable` directive indicates that a field can be resolved by multiple subgraphs. In Apollo Federation, each field on an entity is typically resolved by exactly one subgraph; `@shareable` changes that so the router can obtain the field from any subgraph that defines it.

If a field is `@shareable` in any subgraph, the field has to be marked `@shareable` or `@external` in every subgraph that defines the field, and both subgraphs have to resolve it identically to make sure data is consistent.

This guide explains when `@shareable` is the right tool, what tradeoffs you're accepting, and how to avoid common mistakes. For composition rules, error codes, and federation versioning, see the [@shareable directive reference](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#shareable).

## When to use @shareable

Use `@shareable` when all of these conditions are met:

* **Multiple subgraphs need to resolve the same field or type.** For example, a Profile subgraph owns user data and a Notifications subgraph needs to resolve `User.email` directly, and both have access to the same user database.

* **The data is identical.** Every subgraph that resolves the field has to return the exact same value for the same entity or input. That usually requires a shared data source.

* **You can maintain data consistency.** You have a process to keep definitions in sync and to prevent values from diverging across subgraphs.

* **You accept the coordination cost.** Every subgraph that defines the shareable element has to define it identically (or use `@external`) and stay in sync when the definition changes.

* **For entity fields and entry points, you accept router-controlled resolution.** The router chooses which subgraph resolves the field; you are not relying on a single "source of truth" subgraph at query time.

### Identifying common use cases

Consider using `@shareable` in these scenarios:

* **Value types (shared structures)**: Non-entity types like `PageInfo` or `Money` that multiple subgraphs define identically. The field resolves with its parent; the router doesn't make a routing decision for the value type itself. Coordination cost is the main concern; all defining subgraphs have to keep the type in sync.

* **Entity fields (shared resolution)**: Entity fields that more than one subgraph can resolve from the same underlying data (for example, the same database). Use when reducing subgraph hops justifies delegating resolution to the router. You give up control over which subgraph resolves the field.

* **Entry points (shared queries or mutations)**: Query or mutation fields that multiple subgraphs define so that any of them can serve the operation. Use only when you understand that the router might choose between subgraphs using tie-breakers (like alphabetical subgraph name). Adding a new subgraph that defines the same entry point can shift traffic unexpectedly.

## Ensuring data consistency

Composition rules make sure your schema is valid, but they don't guarantee that your data is consistent. You're responsible for maintaining data consistency.

* **Same data source:** For entity fields and entry points, subgraphs that resolve shareable fields should read from the same data source where possible. If they compute values independently, drift is likely.

* **No logical differences:** The resolved data has to match across subgraphs. Don't use `@shareable` to expose different behavior or data sources; use `@shareable` only when the result is functionally identical.

* **Coordination on changes:** When you change a shareable type or field, all subgraphs that define that type or field have to be updated (or use `@inaccessible` or `@external` as appropriate) so that the supergraph stays consistent.

Never break the promise of identical data. If you do, your API returns inconsistent results—some requests get one subgraph's answer, others get a different subgraph's answer. You won't get an error; you'll get silent data corruption that's nearly impossible to debug.

When you mark a field `@shareable`, you give up control over which subgraph resolves that field. The router decides, based on the cheapest query plan. You cannot rely on a specific subgraph resolving the field for a given request.

## When to avoid using `@shareable`

Avoid using `@shareable` in these scenarios:

* **Fault tolerance or redundancy:** `@shareable` is a query planning optimization, not a redundancy mechanism. The router builds the query plan before execution and doesn't retry with a different subgraph if one fails. If Profile is down, the router won't get `email` from Notifications—if Profile fails, the request fails. Use infrastructure (health checks, circuit breakers, subgraph retries) for fault tolerance, not schema directives.

* **Single source of truth:** If one subgraph is the canonical owner of the data and you need clients to always get data from that subgraph, don't mark the field `@shareable`. Marking it `@shareable` removes that guarantee.

* **Possible data divergence:** If subgraphs could return different values (different databases, logic, or retention), don't use `@shareable`. Inconsistency is silent and difficult to debug.

* **Entry points without understanding traffic impact:** Don't mark query or mutation fields `@shareable` unless you understand that a new subgraph defining the same entry point can change which subgraph receives traffic (for example, via alphabetical tie-breaking). Ensure all subgraphs that could receive that traffic are scaled and behaviorally correct. That pattern has legitimate uses, but the failure modes are subtle; consider consulting [Apollo Solutions](https://www.apollographql.com/services/) to validate your architecture.

* **Speculative optimization:** Don't add `@shareable` without a clear benefit. Adding `@shareable` increases coordination and query planning complexity. Identify which query patterns improve and verify with metrics.

## Implementing `@shareable` in your schema

Implement `@shareable` in your schema:

1. Confirm that multiple subgraphs need to resolve the same field or type and that data can be identical across them.
2. In each subgraph that defines the field or type, add `@shareable` (or `@external` where the subgraph references the field or type but does not resolve it).

Example: a Profile subgraph owns user data.

```graphql title=Profile subgraph
type User @key(fields: "id") {
  id: ID!
  email: String
  displayName: String
}

type Query {
  me: User
}
```

The Notifications subgraph also needs to send emails. It could fetch `email` by calling the Profile subgraph, but Notifications already has access to the same user database and can resolve `email` directly:

```graphql title=Notifications subgraph
type User @key(fields: "id") {
  id: ID!
  email: String @shareable
}
```

Without `@shareable`, composition fails: Federation sees two subgraphs resolving the same field and rejects the schema. With `@shareable`, you tell the router that both subgraphs can resolve the field and the router chooses based on the query plan.

Profile also has to mark the field:

```graphql title=Profile subgraph (updated)
type User @key(fields: "id") {
  id: ID!
  email: String @shareable  # Must match Notifications
  displayName: String
}
```

3. Ensure both subgraphs resolve the field identically (for example, same database or same contract).
4. Document ownership and coordination requirements so that future changes keep definitions and data in sync.

### Building the example: Adding a products query

The next example extends the schema: the Profile subgraph now serves a product catalog with a paginated query.

```graphql title=Profile subgraph
type User @key(fields: "id") {
  id: ID!
  email: String @shareable
  displayName: String
}

type Query {
  me: User
  products(first: Int, after: String): ProductConnection!
}

type ProductConnection {
  edges: [ProductEdge!]!
  pageInfo: PageInfo!
}

type ProductEdge {
  cursor: String!
  node: Product!
}

type Product @key(fields: "id") {
  id: ID!
  name: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

The Notifications subgraph also defines paginated queries for notification history:

```graphql title=Notifications subgraph
type User @key(fields: "id") {
  id: ID!
  email: String @shareable
}

type Query {
  notifications(first: Int, after: String): NotificationConnection!
}

type NotificationConnection {
  edges: [NotificationEdge!]!
  pageInfo: PageInfo!
}

type NotificationEdge {
  cursor: String!
  node: Notification!
}

type Notification @key(fields: "id") {
  id: ID!
  message: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

Composition fails because both subgraphs define `PageInfo` but do not mark `PageInfo` as shareable.

### Type 1: Value types (coordination cost)

`PageInfo` has no `@key` and no identity; it is a **value type** (a shared data structure). Both subgraphs mark `PageInfo` `@shareable`:

```graphql title=Profile subgraph
type PageInfo @shareable {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

```graphql title=Notifications subgraph
type PageInfo @shareable {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

The router does not choose which subgraph resolves `PageInfo`. The type is resolved by the same subgraph that resolves its parent: `pageInfo` for `products` comes from Profile; `pageInfo` for `notifications` comes from Notifications, so there is no extra routing decision.

Both subgraphs have to keep the `PageInfo` definition in sync. If Profile adds a field like `totalCount`, Notifications has to add the same field (or mark it `@inaccessible` until they do). With many subgraphs and teams, keeping definitions in sync adds real coordination cost. Value type `@shareable` avoids routing decisions but still requires coordination across subgraphs.

### Type 2: Entity fields (routing tradeoff)

In the `User.email` example:

```graphql title=Profile subgraph
type User @key(fields: "id") {
  id: ID!
  email: String @shareable
  displayName: String
}
```

```graphql title=Notifications subgraph
type User @key(fields: "id") {
  id: ID!
  email: String @shareable
}
```

`User` is an entity (it has a `@key`). When both subgraphs can resolve `email`, the router chooses which subgraph resolves `User.email` for each operation, based on the query plan (for example, fewer subgraph calls).

`email` has to return the same value whether the router calls Profile or Notifications. That usually means both subgraphs read from the same database. You no longer control which subgraph resolves the field; the router does. Entity fields add a data consistency requirement: all subgraphs that resolve the field must return identical values, on top of the coordination cost of keeping definitions in sync.

### Type 3: Entry points (traffic unpredictability)

Add a third subgraph: the Analytics team wants product data for reporting.

```graphql title=Analytics subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String! @shareable
}

type Query {
  products(first: Int, after: String): ProductConnection! @shareable
}

type ProductConnection {
  edges: [ProductEdge!]!
  pageInfo: PageInfo!
}

# ... rest of pagination types, all @shareable
```

Profile also has to mark its `products` query as shareable:

```graphql title=Profile subgraph (updated)
type Query {
  me: User
  products(first: Int, after: String): ProductConnection! @shareable
}
```

The schema composes, but shareable entry points introduce risk. Query fields are where requests enter the graph. The router has no prior subgraph call to optimize from, so starting at Profile and starting at Analytics cost the same. When costs are equal, the router uses tie-breakers; one is **alphabetical order by subgraph name**. "Analytics" comes before "Profile," so all `products` queries go to Analytics.

As a result, the Analytics subgraph—built for a few hundred internal requests per day—can receive all production traffic for `products`. There is no composition warning. The subgraph might be unable to handle the load, or Analytics might return different data (for example, filter out discontinued products or use different sorting). Your API behavior can change only because a new subgraph has been deployed.

Shareable entry points tie routing to **subgraph naming and deployment order**. Each new subgraph that defines the same entry point can change which subgraph gets the traffic. That is expected: you told the router that any of those subgraphs can run the query, so the router picks one by its rules.

### Composition rules

Apollo Federation enforces these composition rules when a subgraph defines a shareable field or type:

* If a field is marked `@shareable` in one subgraph, every other subgraph that defines that field has to mark it `@shareable` or `@external`.
* Fields in `@key` are automatically shareable; do not add `@shareable` explicitly on key fields.
* `@shareable` is not allowed on interface fields (Federation 2.2+).

Composition fails if you violate these rules. For full syntax and error codes, see the [directive reference](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#shareable).

## Understanding routing implications

The router calls subgraphs at **entity boundaries**—the `@key` fields that identify entities. For non-shareable fields, exactly one subgraph can resolve each field. When you mark an entity field `@shareable`, the router can choose among multiple subgraphs for that field. You gain flexibility in query planning but lose control over which subgraph runs for a given request.

Value types (no `@key`) do not add routing decisions; a value type is resolved by the same subgraph that resolves its parent. Query, mutation, and subscription fields are where requests enter the graph. There is no prior subgraph call, so the cost of each entry point is the same and the router picks one using tie-breakers (for example, alphabetical subgraph name).

To verify which subgraph resolves shareable fields for an operation, check the operation's [query plan](https://www.apollographql.com/docs/graphos/platform/explorer/additional-features#query-plans-for-supergraphs) and [metrics](https://www.apollographql.com/docs/graphos/platform/insights/operation-metrics#operation-metrics) in GraphOS Studio. The [Query Plan Analyzer](https://github.com/apollographql/qp-analyzer) can help detect query plan changes during schema checks and report routing shifts before they reach production.

## The decision framework

Before adding `@shareable`, work through these questions in order.

### Question 0: What am I applying this to?

| Category         | Routing Impact                     | Primary Concerns                                  |
| ---------------- | ---------------------------------- | ------------------------------------------------- |
| **Value Type**   | None (resolves with parent)        | Coordination across teams                         |
| **Entity Field** | New routing decision per operation | Coordination + routing control + data consistency |
| **Entry Point**  | Arbitrary routing selection        | All of the above + traffic unpredictability       |

Each category adds more concerns than the previous.

### Question 1: What are the coordination costs?

That applies to **all three categories**. Every subgraph that defines a shareable element has to define that element identically (or use `@external`), mark it `@shareable`, and stay in sync when the definition changes.

Ask yourself:

* How many subgraphs define or reference the element?
* How frequently might that definition change?
* How autonomous are the teams that own these subgraphs?
* What is the deployment coordination cost for changes?

### Question 2: Am I okay with shared ownership (value types) or forfeited routing control (entities and entry points)?

* **Value types:** No single team can evolve the type independently; changes require coordination.
* **Entity fields:** The router decides which subgraph resolves the field.
* **Entry points:** The router's choice can appear arbitrary, and adding a new subgraph can shift traffic unexpectedly.

### Question 3: Is the data truly identical? (Entity fields and entry points only)

For entity fields and entry points, ask: for any given input, does every subgraph return the exact same value? Not "similar" and not "should be the same"—**identical**. That usually requires a shared data source. If subgraphs compute values independently, the values will eventually differ.

### Question 4: Is there a real benefit?

`@shareable` increases the router's query planning complexity. Before adding `@shareable`, articulate which query patterns improve and measure the impact. Adding `@shareable` speculatively adds complexity without proven benefit.

## Directive interactions

* **@key:** Fields in `@key` are automatically shareable. Do not add `@shareable` explicitly on key fields.

* **@external:** If a field is `@shareable` in one subgraph, other subgraphs that reference it have to mark it `@shareable` or `@external`.

* **@inaccessible:** Combine with `@shareable` for incremental rollouts—hide new fields until all subgraphs define them.

* **@override:** Can combine with `@shareable`. The `from` subgraph stops resolving; others with `@shareable` continue.

* **@provides:** Use [`@provides`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#provides) when a subgraph can resolve a field *only in specific contexts*—for example, when returning it as part of a relationship. This differs from `@shareable`, where the subgraph can always resolve the field. If you are considering `@shareable` to optimize a specific query path, `@provides` might be the more precise tool.

* **Interface fields:** `@shareable` is not allowed on interface fields (Federation 2.2+).

For detailed interaction rules, see the [federation directives reference](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#shareable).

## Evaluating @shareable: A checklist

Use these questions when reviewing schemas. Not all questions apply to all types.

**Category assessment**

* What type of schema element is that? (Value type / Entity field / Entry point.)
* If entry point: Have you consulted with Apollo Solutions about the implications?

**Coordination assessment**

* How many subgraphs define or reference the element?
* How frequently does that definition change?
* How autonomous are the teams that own these subgraphs?
* Who "owns" that definition when changes are needed?

**Data consistency (entity fields and entry points only)**

* Do all subgraphs that define that field read from the same data source?
* If not the same source, what guarantees identical values?
* How would you detect if values diverged?

**Routing implications**

* Which query patterns benefit from that field or type being shareable?
* Is there a "preferred" subgraph that should resolve that field? (If yes, reconsider `@shareable`.)

**Traffic distribution (entry points only)**

* What happens if a new subgraph defines that same entry point?
* Are all subgraphs scaled to handle the full traffic load?
* How might you detect unexpected traffic shifts?

**Risk assessment (all categories)**

* What breaks if that goes wrong?
* How would you detect the failure in production?
* What is the rollback plan?

## Summary

When you use `@shareable`, you are telling the router that a field returns the same result from every subgraph that defines it. If that is not true, the API can return inconsistent results with no error.

* **Value types:** No routing impact, but coordination costs scale with subgraph count and change frequency. All teams have to stay in sync.
* **Entity fields:** Coordination costs plus routing delegation. You forfeit control over which subgraph resolves the field. Use when data sources are genuinely identical and there's measurable benefit.
* **Entry points:** Same as entity fields, plus traffic can move to a different subgraph when you add or change subgraphs. Understand the implications before using.

Before using `@shareable`:

1. Identify the category.
2. Accept the coordination costs.
3. Accept shared ownership or forfeited routing control.
4. Verify data consistency (entity fields and entry points only).
5. Confirm there is a real benefit.

If you can't confidently address all applicable concerns, don't use the `@shareable` directive.

## Further reading

* [@shareable directive reference](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives#shareable)—Complete syntax, composition rules, and error codes
* [Value types in Federation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types)—How to share non-entity types across subgraphs
* [Query planning best practices](https://www.apollographql.com/docs/graphos/routing/query-planning/query-planning-best-practices)—How the router builds query plans
* [Composition error reference](https://www.apollographql.com/docs/graphos/reference/federation/composition-errors)—Troubleshooting composition failures
* [Apollo Solutions](https://www.apollographql.com/services/)—Architecture consultation for complex federation patterns
