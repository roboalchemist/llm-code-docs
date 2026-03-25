# Source: https://www.apollographql.com/docs/kotlin/caching/query-watchers.md

# Watching cached data

Because your [normalized cache](https://www.apollographql.com/docs/kotlin/caching/normalized-cache/) can deduplicate your GraphQL data (using proper [cache IDs](https://www.apollographql.com/docs/kotlin/caching/declarative-ids/)), you can use the cache as the source of truth for populating your UI.

When executing an operation, you can use the `ApolloCall.watch` method to automatically be notified whenever its associated cached data changes:

```kotlin
apolloClient.query(TodoDetailsQuery())
  .watch()
  .collect { response ->
    // This code now executes on response *and*
    // every time cached data changes
  }
```

Let's look at some examples.

## Watching a query

Let's say we're building a collaborative todo list app that executes these two queries:

```graphql
# AllTodos.graphql

# Gets all todo items
query AllTodos {
  items {
    id
    completed
    title
  }
}
```

```graphql
# TodoDetails.graphql

# Gets one todo item's details
query TodoDetails($id: String!) {
  item(id: $id) {
    id
    completed
    title
    content
  }
}
```

The app's main view executes the `AllTodos` query to display a list of todo `Item`s, which includes each item's `title` and `completed` status. Here's an example response:

```json
{
  "data": {
    "items": [
      {
        "id": "0",
        "title": "Write code for Apollo Kotlin",
        "completed": true,
      },
      {
        "id": "1",
        "title": "Write documentation for Apollo Kotlin",
        "completed": false,
      }
    ]
  }
}
```

When someone selects a particular item in the UI, the app executes `TodoDetails` to display that item's full details. And because this is a *collaborative* todo list, those details might have *changed* on the backend since executing `AllTodos` (i.e., another user made changes).

In this case, the `TodoDetails` query might return something like this:

```json
{
  "data": {
    "item": {
      "id": "1",
      "title": "Write documentation for Apollo Kotlin",
      "completed": true,
      "content": "Don't forget docs about the normalized cache!"
    }
  }
}
```

With a [normalized cache](https://www.apollographql.com/docs/kotlin/caching/normalized-cache) and [properly configured cache IDs](https://www.apollographql.com/docs/kotlin/caching/declarative-ids/), this updated `Item` is automatically merged with the *existing* cached `Item` that was returned from `AllTodos`. *However*, our UI doesn't automatically update to reflect the new cached data.

To handle this, we can call `watch()` when we execute any query:

```kotlin
apolloClient.query(TodoDetailsQuery())
  .watch()
  .collect { response ->
    // This code now executes on response *and*
    // every time cached data changes
  }
```

Now if another operation updates this query's cached fields, our UI renders with the same logic it used when the query first returned.

## Updating the cache after a mutation

You sometimes need to update your cached data to reflect changes made by a mutation.

For example, in our todo list app, the user might check off a completed item. This might execute the following mutation to modify an `Item`'s `completed` field:

```graphql
mutation SetTodoCompleted($id: String!, $completed: Boolean!) {
  setTodoCompleted(id: $id, completed: $completed) { # Returns the modified Item
    id
  }
}
```

As written, this mutation updates the `completed` field on the server, but *not* in the cache. This is because the mutation response doesn't include the `Item`'s `completed` field.

To update the cache automatically with the new value, you need to request all modified fields in the response:

```graphql
mutation SetTodoCompleted($id: String!, $completed: Boolean!) {
  setTodoCompleted(id: $id, completed: $completed) {
    id
    # Ask for `completed` to update the cache
    completed
  }
}
```

Because the `setTodoCompleted` field above returns an `Item` type with both an `id` *and* the `completed` field, Apollo Kotlin can update the cached `Item` entry with the new data. Additionally, any watchers listening to this `Item`'s `completed` field are automatically notified.

### Optimistic updates

It's often possible to predict the most likely result of a mutation *before* your GraphQL server returns it. Apollo Kotlin can use this "most likely result" to update your UI **optimistically**, making your app feel more responsive to the user.

You provide optimistic data with the `optimisticUpdates` method, like so:

```kotlin
apolloClient.mutation(SetTodocompletedMutation(id = "1", completed = true))
  .optimisticUpdates(
    SetTodocompletedMutation.Data(
      id = "1",
      completed = true,
    )
  )
  .execute()
```

This optimistic data is written to the cache immediately, and any watchers of the corresponding data are notified. Then, when the operation returns, the cache is updated *again* with any changes, and watchers are notified again. If the optimistic data is correct, the second cache update is invisible to the user, because no data changes.
