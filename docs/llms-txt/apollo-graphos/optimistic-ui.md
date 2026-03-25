# Source: https://www.apollographql.com/docs/react/performance/optimistic-ui.md

# Optimistic mutation results

It's often possible to predict the most likely result of a mutation *before* your GraphQL server returns it. Apollo Client can use this "most likely result" to update your UI **optimistically**, making your app feel more responsive to the user.

For example, let's say we have a blog application that supports the following mutation:

```graphql
type Mutation {
  updateComment(commentId: ID!, content: String!): Comment!

  # ...other mutations...
}
```

If a user edits an existing comment on a post, the app executes the `updateComment` mutation, which returns a `Comment` object with updated `content`.

Our app knows what the updated `Comment` object will probably look like, which means it can optimistically update its UI to display the update *before* the GraphQL server responds with it. If our app is wrong (e.g., the GraphQL server returns an *unchanged* `Comment` due to an error), the UI will automatically update to reflect the *actual* response.

## The `optimisticResponse` option

To enable this optimistic UI behavior, we provide an `optimisticResponse` option to the [mutate function](https://www.apollographql.com/docs/react/data/mutations/#executing-a-mutation) that we use to execute our mutation.

Let's look at some code:

```jsx title=CommentPageWithData.jsx
// Mutation definition
const UPDATE_COMMENT = gql`
  mutation UpdateComment($commentId: ID!, $commentContent: String!) {
    updateComment(commentId: $commentId, content: $commentContent) {
      id
      __typename
      content
    }
  }
`;

// Component definition
function CommentPageWithData() {
  const [mutate] = useMutation(UPDATE_COMMENT);
  return (
    <Comment
      updateComment={({ commentId, commentContent }) =>
        mutate({
          variables: { commentId, commentContent },
          optimisticResponse: {
            updateComment: {
              id: commentId,
              __typename: "Comment",
              content: commentContent,
            },
          },
        })
      }
    />
  );
}
```

As this example shows, the value of `optimisticResponse` is an object that matches the shape of the mutation response we expect from the server. Importantly, this includes the `Comment`'s `id` and `__typename` fields. The Apollo Client cache uses these values to generate the comment's [unique cache identifier](https://www.apollographql.com/docs/react/caching/cache-configuration/#customizing-cache-ids) (e.g., `Comment:5`).

## Optimistic mutation lifecycle

1. When the code above calls `mutate`, the Apollo Client cache stores a `Comment` object with the field values specified in `optimisticResponse`. *However*, it does not overwrite the *existing* cached `Comment` with the same cache identifier. Instead, it stores a separate, *optimistic* version of the object. This ensures that our cached data remains accurate if our `optimisticResponse` is wrong.

2. Apollo Client notifies all active queries that include the modified comment. Those queries automatically update, and their associated components re-render to reflect the optimistic data. Because this doesn't require any network requests, it's nearly instantaneous to the user.

3. Eventually, our server responds with the mutation's *actual* resulting `Comment` object.

4. The Apollo Client cache removes the optimistic version of the `Comment` object. It also overwrites the *canonical* cached version with values returned from the server.

5. Apollo Client notifies all affected queries again. The associated components re-render, but if the server's response matches our `optimisticResponse`, this is invisible to the user.

6. If the mutation returns a GraphQL error, Apollo Client discards the optimistic version of the object and rolls back to the previous state.

## Bailing out of an optimistic update

In some cases you may want to skip an optimistic update. For example, you may want to perform an optimistic update *only* when certain variables are passed to the mutation. To skip an update, pass a function to the `optimisticResponse` option and return the `IGNORE` sentinel object available on the second argument to bail out of the optimistic update.

Consider this example:

```tsx
const UPDATE_COMMENT = gql`
  mutation UpdateComment($commentId: ID!, $commentContent: String!) {
    updateComment(commentId: $commentId, content: $commentContent) {
      id
      __typename
      content
    }
  }
`;

function CommentPageWithData() {
  const [mutate] = useMutation(UPDATE_COMMENT);

  return (
    <Comment
      updateComment={({ commentId, commentContent }) =>
        mutate({
          variables: { commentId, commentContent },
          optimisticResponse: (vars, { IGNORE }) => {
            if (commentContent === "foo") {
              // conditionally bail out of optimistic updates
              return IGNORE;
            }
            return {
              updateComment: {
                id: commentId,
                __typename: "Comment",
                content: commentContent,
              },
            };
          },
        })
      }
    />
  );
}
```

## Example: Adding a new object to a list

The previous example shows how to provide an optimistic result for an object that's *already* in the Apollo Client cache. But what about a mutation that creates a *new* object? This works similarly.

The biggest difference here is that the client doesn't yet have the new object's `id` (or other identifying field). This means you have to provide a temporary value for the `id` so the Apollo Client cache can store the optimistic result as an object of the correct type.

For example, here's an `optimisticResponse` for an `addTodo` mutation that creates a new item in a user's to-do list:

```js
optimisticResponse: {
  addTodo: {
    id: 'temp-id',
    __typename: "Todo",
    description: input.value // Obtained from user input
  }
}
```

When you execute the mutate function in this case, the Apollo Client cache stores a new `Todo` object with cache identifier `Todo:temp-id`. When the server responds with the new `Todo`'s *actual* `id`, the optimistic object is removed as usual, and the canonical object is cached.

### View on CodeSandbox

You can view a full to-do list example on CodeSandbox:

> You can also run the example client and server locally by cloning the [`docs-examples` repo](https://github.com/apollographql/docs-examples/tree/main/full-stack/todo-list).

When viewing the example, try adding an item to the to-do list. Notice that the item appears in the list instantly, even though the server doesn't *respond* instantly.

Then, try editing an existing item in the to-do list. Notice that the item *doesn't* update instantly. That's because the client doesn't provide an `optimisticResponse` for the `updateTodo` mutation. This helps illustrate the improved responsiveness that an `optimisticResponse` provides.
