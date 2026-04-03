# Source: https://developers.buffer.com/guides/api-standards.md

# API Standards

We've designed the Buffer API around a set of principles that keep things stable and predictable as we evolve the schema.

## Always Add, Never Modify or Remove

We only add to the schema. We won't modify or remove existing fields and types. Your queries and mutations will keep working as we ship updates. New fields and types are added alongside existing ones, so you don't need to worry about breaking changes.

When we plan to retire a field, we mark it with the `@deprecated` annotation. Deprecated fields include a `reason` that describes the replacement and when the field will be removed.

```jsx
type ExampleType {
  oldField: String @deprecated(reason: "Use `newField`. This will be removed on the 12/10/2021")
  newField: String
}
```

You'll always have advance notice before a field is removed. Keep an eye on the `@deprecated` annotations in the schema, our [Changelog](../changelog.html), and migrate to the recommended replacements before the removal date.

## Using Input Objects for Operation Arguments

We use input objects rather than inline arguments. This keeps things flexible as the API evolves. For example, instead of passing individual scalars:

```jsx
type Mutation {
  createPost(text: String): ...
}
```

The API uses a dedicated input type:

```jsx
input PostInput {
  orgId: String
  text: String
}

type Mutation {
  createPost(input: PostInput!): ...
}
```

This means new fields can be added to the input type without affecting existing operations.

## Returning Typed Responses

Our operations return typed response objects rather than scalar values. This lets responses evolve over time. For example, adding new fields, without breaking the contract. It also enables union types for error handling.

```jsx
type Mutation {
  createPost(...): Post
}
```

Instead, we use typed responses that can include additional data and error states:

```jsx
type PostActionSuccess {
  post: Post!
}

type LimitReachedError {
  message: String!
}

union PostActionPayload = PostActionSuccess | LimitReachedError

type Mutation {
  createPost(...): PostActionPayload
}
```

## Being Specific with Nullability

We use nullability to communicate exactly what you can expect from each field. A non-null field (marked with `!`) guarantees a value will always be present. A nullable field may return `null`, and your client should handle that case.

Here's an example:

```jsx
type Post {
  type: PostStatus!
  sentAt: DateTime
}
```

For this type, there are two states:

- **Non-null** - a value will always be provided. You don't need to handle a null state. For example, a post always has a `PostStatus`:

```jsx
type: PostStatus!
```

- **Nullable** - a null value may be returned, and your client should handle it. For example, a post only has a `sentAt` for when a post has been published:

```jsx
sentAt: DateTime
```

### Nullability in Arrays

Nullability applies to both the array itself and the type contained within it.

**In short**: if an array will never contain null entries, the entry type is marked as non-null. If the array itself can never be null, it's also marked as non-null.

```jsx
posts: [Post]
```

Both the array and its entries can be null. You could receive `null`, or an array containing null values such as `[ATTACHMENT, null, ATTACHMENT]`.

```jsx
posts: [Post]!
```

The array will never be null (it will always be returned, even if empty), but individual entries may be null. For example, `[null, TAG, null]` or `[]`, but never `null`.

```jsx
posts: [Post!]
```

The array may be null, but when present, its entries will never be null. For example, `[]`, `null`, or `[MEDIA, MEDIA]`.

When both the array and entries are non-null:

```jsx
posts: [Post!]!
```

You are guaranteed a non-null array with non-null entries.

### Boolean Values

Boolean fields are always non-null. You will always receive either `true` or `false`, so there is no need to handle a null state for boolean values.

## Returning Contextual Responses to Clients

Our mutation responses return meaningful data related to the action performed, rather than generic status flags. For example, instead of:

```kotlin
type PostActionSuccess  {
    success: Boolean!
}
```

The response returns the resource that was affected:

```kotlin
type PostActionSuccess {
    post: Post!
}
```

This gives you immediately useful data and avoids redundant checks. If you're using Apollo Client, the local cache will automatically update when it receives a response matching the `id` and `__typename` of an already-cached object.

## Maintaining Input Type Ordering

We always append new fields to the end of input types. This matters because some code-generated clients send arguments positionally. If a new field were inserted in the middle, existing positional arguments would shift and map to the wrong fields.

Here's an example. Given this input type:

```kotlin
input IdeaCreationInput {
  organizationId: String!
  content: IdeaContentInput!
  source: String
}
```

A code-generated client (e.g. Apollo on Android) produces:

```kotlin
public data class IdeaCreationInput(
  public val organizationId: String,
  public val content: IdeaContentInput,
  public val cta: Optional<String?> = Optional.Absent,
)
```

And the client sends arguments positionally:

```kotlin
IdeaCreateMutation(
    IdeaCreationInput(
        idea.organizationId!!,
        idea.toInput(),
        Optional.presentIfNotNull(source)
    )
)
```

If a new field `groupId` were added in the middle:

```kotlin
input IdeaCreationInput {
  organizationId: String!
  content: IdeaContentInput!
  groupId: ID
  source: String
}
```

The generated class would shift:

```kotlin
public data class IdeaCreationInput(
  public val organizationId: String,
  public val content: IdeaContentInput,
  public val groupId: Optional<String?> = Optional.Absent,
  public val cta: Optional<String?> = Optional.Absent,
)
```

Clients that have not updated would now send the `source` value as `groupId`, causing incorrect behavior.

```kotlin
IdeaCreateMutation(
    IdeaCreationInput(
        idea.organizationId!!,
        idea.toInput(),
        Optional.presentIfNotNull(source)
    )
)
```

To avoid this, always use **named arguments** rather than positional arguments when constructing input types in your client code.

## Pagination

Paginated responses use cursor-based pagination with the following structure:

- `edges`: a list of connections to the response items
- `pageInfo`: pagination metadata (see `PaginationPageInfo` below)
- `totalCount`: optional, but when present, always non-null. The total count of all results matching the query filters.

### Request Fields

**input**

The input filter. The top level includes static, required fields (typically the organization ID), plus an optional `filter` object for narrowing results.

- `organizationId`: The organization ID for the request.
- `filter`: Filtering criteria applied to results and counts.
  - Filter values are typically lists of string IDs.
  - Fields are nullable - omitting a filter field means no filtering is applied for that criterion.
  - Filtering logic uses an **AND** operation between all defined items.

**first**

The maximum number of items to return (synonymous with "limit").

**after**

The cursor to start fetching from. Cursors are opaque strings. Do not parse or construct them yourself.

### Response Fields

**totalCount**

The total number of results matching the query filters, consistent with [GraphQL pagination best practices](https://graphql.org/learn/pagination/) and [GitHub's implementation](https://docs.github.com/en/graphql/reference/objects#branchprotectionruleconflictconnection).

**pageInfo**

- `startCursor`: The first cursor in the list. Use it to fetch the previous page.
- `endCursor`: The last cursor in the list. Use it to fetch the next page.
- `hasPreviousPage`: `true` if a previous page is available. Currently always `false` as only forward pagination is supported.
- `hasNextPage`: `true` if a next page is available.

## Error Handling

We use two categories of errors:

- **Non-recoverable errors** appear in the standard GraphQL `errors` array. These represent issues outside your control - authentication failures, missing resources, or server errors. They include an error `code` in the `extensions` object (e.g. `NOT_FOUND`, `FORBIDDEN`, `UNAUTHORIZED`, `UNEXPECTED`).

- **Recoverable errors** (user errors) are returned as typed data in the response payload. These are situations you can act on, like input validation failures or account limits being reached.

### Mutations

#### Modelling Errors

Every mutation returns a payload union that includes both the success state and any user-facing errors. The payload follows the naming convention `{MutationName}Payload`.

```graphql
union PostActionPayload = PostActionSuccess | ...
```

You can query for the specific error types you need to handle. New error types may be added to a payload over time.

```graphql
union PostActionPayload = PostActionSuccess | LimitReachedError | InvalidInputError
```

Every typed error implements the `MutationError` interface:

```graphql
interface MutationError {
    message: String!
}
```

Each error type includes the `message` field from the interface:

```graphql
type LimitReachedError implements MutationError {
    message: String!
}

type InvalidInputError implements MutationError {
    message: String!
}
```

The `message` field contains a human-readable string suitable for display. In most cases you'll use the error type itself to determine what to show, but the `message` provides a sensible default (see **Future Proofing Error Responses** below).

#### Consuming Errors

To consume typed errors, use the `... on` pattern to match specific error types in the response. This lets you handle each error differently - for example, showing a specific recovery path to the user.

You only need to match the error types you care about. For everything else, use `... on MutationError` as a catch-all:

```graphql
mutation CreatePost {
  createPost {
    ... on PostActionSuccess {
      // handle fields
    }
    ... on LimitReachedError {
      message
    }
    ... on MutationError {
      message
    }
  }
}
```

If you don't need to handle specific error types, you can rely entirely on the `MutationError` interface:

```graphql
mutation CreatePost {
  createPost {
    ... on PostActionSuccess {
      // handle fields
    }
    ... on MutationError {
      message
    }
  }
}
```

#### Future Proofing Error Responses

Some mutations may not have specific typed errors defined yet. To make sure your client handles any errors we add in the future, every mutation payload includes a `VoidMutationError` type:

```graphql
type VoidMutationError implements MutationError {
  message: String!
}

union PostActionPayload = PostActionSuccess | VoidMutationError
```

We'll never explicitly return a `VoidMutationError`, but its presence in the union means that if you include `... on MutationError` in your query, your client will automatically receive the `message` for any new error types we add later - no code changes needed.

```graphql
... on MutationError {
  message
}
```

For this reason, **always include `... on MutationError`** in your mutation queries.

#### Non-Recoverable Errors

Non-recoverable errors are returned in the standard GraphQL `errors` array. These include an error `code` in the `extensions` object for additional context. Common error codes include:

- `NOT_FOUND` - the requested resource doesn't exist
- `FORBIDDEN` - you don't have permission for this action
- `UNAUTHORIZED` - authentication is required or invalid
- `UNEXPECTED` - an unexpected server error occurred

If you need to show error details to users, use typed errors (as described above) instead of the `errors` array.

### Queries

In most cases, queries return either the requested data or a non-recoverable error in the `errors` array:

```graphql
type Query {
  channels(input: ChannelsInput!): [Channel!]!
}
```

A successful result returns the list of `Channel` types. If an error occurs, it appears in the `errors` array.

In rare cases, a query may need to return a recoverable error. When this applies, we use a union payload, the same pattern as mutations. For example, if fetching a post requires reconnecting a channel, the response includes a typed error:

```graphql
type PostSuccess {
  post: Post!
}

type ChannelReconnectRequired implements MutationError {
  message: String!
  channelId: String!
}

union PostPayload = PostSuccess | ChannelReconnectRequired

type Query {
  post(input: PostInput!): PostPayload
}
```

This pattern is uncommon for queries but provides a way to surface recoverable errors when needed.
