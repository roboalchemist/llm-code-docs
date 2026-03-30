# Source: https://developers.buffer.com/guides/api-standards.md

# API Standards

The Buffer API follows a set of design principles rooted in GraphQL best practices. These standards ensure the schema remains stable, predictable, and easy to consume as it evolves over time.

## Always Add, Never Modify or Remove

The API follows an additive evolution model. Existing fields and types will not be modified or removed, ensuring that your queries and mutations continue to work as the schema evolves. New fields and types are added alongside existing ones, so you do not need to worry about breaking changes from schema updates.

Fields may be deprecated using the `@deprecated` annotation, which indicates that a field should no longer be used. Deprecated fields include a `reason` string that describes the replacement and when the field will be removed.

```jsx
type ExampleType {
  oldField: String @deprecated(reason: "Use `newField`. This will be removed on the 12/10/2021")
  newField: String
}
```

When a field is deprecated, you will have advance notice before it is removed. Monitor the `@deprecated` annotations in the schema to stay informed of upcoming changes and migrate to the recommended replacements before the removal date.

## Using Input Objects for Operation Arguments

Operations use input objects rather than inline arguments. This keeps the argument surface flexible as the API evolves. For example, instead of passing individual scalars:

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

Operations return typed response objects rather than scalar values. This allows responses to evolve over time — for example, adding new fields — without breaking the contract. It also enables the use of union types for error handling.

```jsx
type Mutation {
  createPost(...): Post
}
```

Instead, the API uses typed responses that can include additional data and error states:

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

The schema uses nullability to communicate exactly what you can expect from each field. A non-null field (marked with `!`) guarantees a value will always be present. A nullable field may return `null`, and your client should handle that case.

Here is an example:

```jsx
type Post {
  type: PostStatus!
  sentAt: DateTime
}
```

For this type, there are two states:

- **Non-null** — a value will always be provided. You do not need to handle a null state. For example, a post always has a `PostStatus`:

```jsx
type: PostStatus!
```

- **Nullable** — a null value may be returned, and your client should handle it. For example, a post only has a `sentAt` for when a post has been published:

```jsx
sentAt: DateTime
```

### Nullability in Arrays

Nullability applies to both the array itself and the type contained within it.

**In short**: if an array will never contain null entries, the entry type is marked as non-null. If the array itself can never be null, it is also marked as non-null.

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

Mutation responses return meaningful data related to the action performed, rather than generic status flags. For example, instead of:

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

This provides you with immediately useful data and avoids redundant checks. For example, if you are using Apollo Client, the local cache will automatically update when it receives a response that matches the `id` and `__typename` of an already-cached object.

## Maintaining Input Type Ordering

New fields are always appended to the end of input types. This is important because some code-generated clients send arguments positionally. If a new field were inserted in the middle, existing positional arguments would shift and map to the wrong fields.

Here is an example. Given this input type:

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
  - Fields are nullable — omitting a filter field means no filtering is applied for that criterion.
  - Filtering logic uses an **AND** operation between all defined items.

**first**

The maximum number of items to return (synonymous with "limit").

**after**

The cursor to start fetching from. Cursors are opaque strings — do not parse or construct them yourself.

### Response Fields

**totalCount**

The total number of results matching the query filters, consistent with [GraphQL pagination best practices](https://graphql.org/learn/pagination/) and [GitHub's implementation](https://docs.github.com/en/graphql/reference/objects#branchprotectionruleconflictconnection).

**pageInfo**

- `startCursor`: The first cursor in the list. Use it to fetch the previous page.
- `endCursor`: The last cursor in the list. Use it to fetch the next page.
- `hasPreviousPage`: `true` if a previous page is available. Currently always `false` as only forward pagination is supported.
- `hasNextPage`: `true` if a next page is available.

## Error Handling

The API uses two categories of errors:

- **Non-recoverable errors** appear in the standard GraphQL `errors` array. These represent issues that are not caused by user input — such as authentication failures, missing resources, or server errors. Non-recoverable errors include an error `code` in the `extensions` object (e.g. `NOT_FOUND`, `FORBIDDEN`, `UNAUTHORIZED`, `UNEXPECTED`).

- **Recoverable errors** (user errors) are returned as typed data in the response payload. These represent situations the user can act on — such as input validation failures or account limits being reached.

### Mutations

#### Modelling Errors

Every mutation returns a payload union, allowing it to return both its success state and any user-facing errors. The payload follows the naming convention `{MutationName}Payload`.

```graphql
union PostCreatePayload = PostCreateSuccess | ...
```

You can query for the specific error types you need to handle. New error types may be added to a payload over time.

```graphql
union PostCreatePayload = PostCreateSuccess | QueueLimitReached | PostValidationFailed
```

Every typed error implements the `MutationError` interface:

```graphql
interface MutationError {
    message: String!
}
```

Each error type includes the `message` field from the interface, and may also include additional fields specific to that error. For example, a `QueueLimitError` includes the account's queue limit, and a `PostAlreadyExistsError` returns the existing post:

```graphql
type QueueLimitError implements MutationError {
    message: String!
    limit: Int!
}

type PostAlreadyExistsError implements MutationError {
    message: String!
    post: Post!
}
```

Error types can contain more complex data. For example, a `ValidationError` includes a list of field-level errors:

```graphql
type FieldError {
    validationError: String!
    field: String!
}

type ValidationError implements MutationError {
    message: String!
    errors: [FieldError!]!
}
```

The `message` field contains a human-readable string suitable for display. In most cases you will use the error type itself to determine what to show, but the `message` provides a sensible default (see **Future Proofing Error Responses** below).

#### Consuming Errors

To consume typed errors, use the `... on` pattern to match specific error types in the response. This lets you handle each error differently — for example, showing a specific recovery path to the user.

You only need to match the specific error types you care about. For everything else, use `... on MutationError` as a catch-all to display the generic error message:

```graphql
mutation CreatePost {
  createPost {
    ... on PostCreateSuccess {
      // handle fields
    }
    ... on QueueLimitError {
      message
      limit
    }
    ... on MutationError {
      message
    }
  }
}
```

If you do not need to handle specific error types, you can rely entirely on the `MutationError` interface:

```graphql
mutation CreatePost {
  createPost {
    ... on PostCreateSuccess {
      // handle fields
    }
    ... on MutationError {
      message
    }
  }
}
```

#### Future Proofing Error Responses

Some mutations may not have specific typed errors defined initially. To ensure your client handles any errors that may be added in the future, every mutation payload includes a `VoidMutationError` type:

```graphql
type VoidMutationError implements MutationError {
  message: String!
}

union PostCreatePayload = PostCreateSuccess | VoidMutationError
```

The API will never explicitly return a `VoidMutationError`, but its presence in the union means that if you include `... on MutationError` in your query, your client will automatically receive the `message` for any new error types added later — without requiring any code changes.

```graphql
... on MutationError {
  message
}
```

For this reason, **always include `... on MutationError`** in your mutation queries.

#### Non-Recoverable Errors

Non-recoverable errors are returned in the standard GraphQL `errors` array. These include an error `code` in the `extensions` object to provide additional context. Common error codes include:

- `NOT_FOUND` — the requested resource does not exist
- `FORBIDDEN` — you do not have permission for this action
- `UNAUTHORIZED` — authentication is required or invalid
- `UNEXPECTED` — an unexpected server error occurred

If you need to display error details to users, use typed errors (as described above) instead of relying on the `errors` array.

### Queries

In most cases, queries return either the requested data or a non-recoverable error in the `errors` array:

```graphql
type Query {
  channels(input: ChannelsInput!): [Channel!]!
}
```

A successful result returns the list of `Channel` types. If an error occurs, it will appear in the `errors` array.

In rare cases, a query may need to return a user-recoverable error. When this applies, the query uses a union payload, the same pattern as mutations. For example, if fetching a post requires the user to reconnect their channel, the response includes a typed error:

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
