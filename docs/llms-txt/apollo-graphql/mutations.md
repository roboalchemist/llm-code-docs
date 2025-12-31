# Apollo Client Mutations: Comprehensive Guide

Source: https://www.apollographql.com/docs/react/data/mutations

## Overview

Mutations enable you to modify backend data using GraphQL. Apollo Client's `useMutation` hook provides the primary API for executing mutations in React applications, allowing developers to send updates to GraphQL servers and manage the resulting state changes.

## Core Concepts

### The useMutation Hook

The `useMutation` hook accepts a GraphQL mutation document and returns a tuple containing:

1. **Mutate function**: Called to execute the mutation (not automatic like `useQuery`)
2. **Status object**: Contains `data`, `loading`, `error`, and other fields tracking execution state

```javascript
const [mutate, { data, loading, error }] = useMutation(MUTATION_DOCUMENT);
```

### Key Differences from useQuery

Unlike `useQuery`, mutations do not execute automatically on component render. Instead, you explicitly call the mutate function in response to user actions, typically form submissions.

## Executing Mutations

### Basic Example

```javascript
const ADD_TODO = gql`
  mutation AddTodo($type: String!) {
    addTodo(type: $type) {
      id
      type
    }
  }
`;

function AddTodo() {
  const [addTodo, { loading, error }] = useMutation(ADD_TODO);

  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      addTodo({ variables: { type: "groceries" } });
    }}>
      <input />
      <button type="submit">Add Todo</button>
    </form>
  );
}
```

### Providing Options

Options can be supplied to `useMutation` directly or to the mutate function call. When provided to both, the mutate function's values take precedence, with variables being shallowly merged.

```javascript
const [addTodo] = useMutation(ADD_TODO, {
  variables: { type: "default" }
});

// Call with additional/override variables
addTodo({ variables: { type: "custom" } });
```

## Tracking Mutation Status

The returned status object includes fields for monitoring execution:

- **`loading`**: Boolean indicating if mutation is in flight
- **`error`**: Contains either `graphQLErrors` array or `networkError`
- **`called`**: Boolean indicating if mutate function was invoked
- **`data`**: Mutation result data

```javascript
if (loading) return "Submitting...";
if (error) return `Error: ${error.message}`;
```

### Reset Function

The `reset()` function restores the mutation's result to its initial state, useful for dismissing error messages or clearing completed state:

```javascript
const [login, { error, reset }] = useMutation(LOGIN_MUTATION);

{error && (
  <ErrorWindow
    message={error.message}
    onDismiss={() => reset()}
  />
)}
```

## Updating Local Data

### Strategy Overview

After mutation execution, update cached data using these approaches:

1. **Refetch queries**: Request updated data from the server
2. **Direct cache update**: Modify cache manually without additional requests
3. **Combined approach**: Update cache then optionally refetch for validation

### Refetching Queries

Specify queries to refetch after mutation completes:

```javascript
const [addTodo] = useMutation(ADD_TODO, {
  refetchQueries: [
    GET_TODOS,          // DocumentNode object
    "GetComments",      // Query name string
    { query: GET_TODOS, variables: { id: 1 } }
  ]
});
```

Special refetch values:
- `"active"`: Refetch all active queries
- `"all"`: Refetch all active and inactive queries

### Direct Cache Updates

The `update` function allows manual cache modifications after mutations complete. This approach provides "immediate" UI updates without network requests:

```javascript
const [addTodo] = useMutation(ADD_TODO, {
  update(cache, { data: { addTodo } }) {
    cache.modify({
      fields: {
        todos(existingTodos = []) {
          const newTodoRef = cache.writeFragment({
            data: addTodo,
            fragment: gql`
              fragment NewTodo on Todo {
                id
                type
              }
            `
          });
          return [...existingTodos, newTodoRef];
        }
      }
    });
  }
});
```

**Important**: The `update` function executes twice if an optimistic response is provided—once with optimistic data, once with actual server response.

### Combining Update with Refetch Validation

Use `onQueryUpdated` to refetch affected queries after cache updates, ensuring accuracy:

```javascript
addTodo({
  variables: { type: value },
  update(cache, result) {
    // Manual cache modifications
  },
  onQueryUpdated(observableQuery) {
    return shouldRefetch(observableQuery)
      ? observableQuery.refetch()
      : undefined;
  }
});
```

## Best Practices for Mutation Responses

Mutations should return "all objects and fields that it modified." This enables Apollo Client to normalize and cache results appropriately.

Example response structure:

```json
{
  "__typename": "Todo",
  "id": "5",
  "type": "groceries"
}
```

Apollo Client automatically adds `__typename` and caches the object using its `__typename` and `keyFields` configuration.

## useMutation API Reference

### Key Options

| Option | Type | Purpose |
|--------|------|---------|
| `variables` | Object | GraphQL variables required by mutation |
| `refetchQueries` | Array/Function | Queries to refetch after mutation |
| `update` | Function | Manual cache update handler |
| `optimisticResponse` | Object/Function | Immediate UI response before server reply |
| `onCompleted` | Function | Callback on successful completion |
| `onError` | Function | Callback on error |
| `errorPolicy` | String | How to handle responses with errors |
| `context` | Object | Apollo Link context values |
| `fetchPolicy` | String | Cache behavior (`network-only` or `no-cache`) |
| `awaitRefetchQueries` | Boolean | Wait for refetch completion |
| `keepRootFields` | Boolean | Preserve ROOT_MUTATION cache fields |

### Result Properties

| Property | Type | Purpose |
|----------|------|---------|
| `called` | Boolean | Mutate function was invoked |
| `loading` | Boolean | Mutation in flight |
| `error` | ErrorLike | Error object if mutation failed |
| `data` | Object | Mutation result data |
| `client` | ApolloClient | Apollo Client instance used |
| `reset` | Function | Reset to initial state |

## Error Handling

Configure error policies to control partial data handling:

- **`none`** (default): Include errors and reject partial results
- **`ignore`**: Return partial results, suppress errors
- **`all`**: Return both errors and partial results

```javascript
const [mutate] = useMutation(MUTATION, {
  errorPolicy: "all",
  onError(error) {
    console.log(error.graphQLErrors);
    console.log(error.networkError);
  }
});
```

## Performance: Optimistic UI

Provide immediate UI feedback before server response:

```javascript
const [addTodo] = useMutation(ADD_TODO, {
  optimisticResponse: {
    addTodo: {
      __typename: "Todo",
      id: -1,
      type: inputValue
    }
  }
});
```

The optimistic response is cached immediately and replaced with actual server data when received.

## Common Patterns

### Form Submission

```javascript
<form onSubmit={e => {
  e.preventDefault();
  mutate({ variables: { /* form data */ } });
  resetForm();
}}>
```

### Post-Mutation Navigation

```javascript
const [login] = useMutation(LOGIN, {
  onCompleted({ login }) {
    navigate("/dashboard");
  }
});
```

### Dependent Mutations

Chain mutations using `onCompleted`:

```javascript
const [createUser] = useMutation(CREATE_USER, {
  onCompleted(userData) {
    createProfile({ variables: { userId: userData.id } });
  }
});
```

## Integration with Caching

Understanding Apollo Client's cache normalization is essential for effective mutation handling. Objects are cached by `__typename` and configured `keyFields`, enabling automatic cache updates when mutations return modified objects.

For complex cache scenarios, the `cache.modify()` API provides granular control over normalized cache entries, field-by-field modifications, and reference management.

---

**Related Topics**: [Optimistic mutation results](https://www.apollographql.com/docs/react/performance/optimistic-ui/), [Caching in Apollo Client](https://www.apollographql.com/docs/react/caching/overview), [Error handling](https://www.apollographql.com/docs/react/data/error-handling/)
