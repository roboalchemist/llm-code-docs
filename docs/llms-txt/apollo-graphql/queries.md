# Apollo Client Queries Documentation

Source: https://www.apollographql.com/docs/react/data/queries

## Overview

Apollo Client provides powerful hooks for executing GraphQL queries in React applications. The primary hook, `useQuery`, handles data fetching, caching, and state management automatically.

## Core Hooks

### useQuery

The fundamental hook for executing queries automatically when a component renders.

**Basic Usage:**
```javascript
const { loading, error, data } = useQuery(GET_DOGS);

if (loading) return "Loading...";
if (error) return `Error! ${error.message}`;

return <Dogs data={data.dogs} />;
```

**Key Features:**
- Automatic query execution on component mount
- Built-in loading and error state tracking
- Integrated caching mechanism
- Network status monitoring

### useLazyQuery

For manually triggering queries in response to user interactions rather than automatic execution.

**Usage Pattern:**
```javascript
const [getDogs, { loading, error, data }] = useLazyQuery(GET_DOGS);

return (
  <>
    {data?.dogs.map(dog => <Dog key={dog.id} dog={dog} />)}
    <button onClick={() => getDogs()}>Load dogs</button>
  </>
);
```

**Advantages:**
- Deferred query execution
- Execution function returns a promise
- Useful for search, filters, and on-demand loading

## Query Options

### Fetch Policies

Control how Apollo Client interacts with the cache:

| Policy | Behavior |
|--------|----------|
| `cache-first` | Check cache first; fetch from network only if data missing (default) |
| `cache-only` | Query cache exclusively; never contact server |
| `network-only` | Always fetch from network; store results in cache |
| `cache-and-network` | Query both cache and network simultaneously |
| `no-cache` | Fetch from network without caching results |
| `standby` | Use cache-first logic but don't auto-update on changes |

### nextFetchPolicy

Specify different fetch behavior after the initial query execution:

```javascript
const { data } = useQuery(GET_DOGS, {
  fetchPolicy: "network-only",
  nextFetchPolicy: "cache-first"
});
```

This pattern ensures fresh data on first load, then relies on cache for performance.

### Common Options

| Option | Purpose |
|--------|---------|
| `variables` | Object containing GraphQL variables |
| `pollInterval` | Milliseconds between automatic refetches (0 = disabled) |
| `skip` | Boolean to skip query execution |
| `errorPolicy` | How to handle responses with both errors and partial data |
| `notifyOnNetworkStatusChange` | Trigger re-renders on network status changes |
| `context` | Pass data through Apollo Link chain |

## Data Fetching Strategies

### Polling

Automatically refresh data at regular intervals:

```javascript
const { data } = useQuery(GET_DOG_PHOTO, {
  variables: { breed },
  pollInterval: 500 // Refetch every 500ms
});
```

Control polling dynamically with `startPolling()` and `stopPolling()` functions returned by the hook.

### Refetching

Manually trigger fresh data retrieval:

```javascript
const { data, refetch } = useQuery(GET_DOG_PHOTO, {
  variables: { breed }
});

<button onClick={() => refetch()}>Refresh</button>
```

Pass new variables to refetch:
```javascript
refetch({ breed: "dalmatian" })
```

### Pagination

Implement incremental data loading with `fetchMore`:

```javascript
const { fetchMore } = useQuery(GET_DOGS_PAGINATED);

const loadMore = () => {
  fetchMore({
    variables: { offset: currentOffset + pageSize },
    updateQuery: (prev, { fetchMoreResult }) => {
      return {
        dogs: [...prev.dogs, ...fetchMoreResult.dogs]
      };
    }
  });
};
```

## State Management

### Loading States

The hook provides fine-grained network status tracking:

```javascript
import { NetworkStatus } from "@apollo/client";

const { loading, networkStatus } = useQuery(QUERY);

if (networkStatus === NetworkStatus.refetch) {
  return "Refetching...";
}
```

The `loading` property indicates any in-flight operation, while `networkStatus` offers granular operation type information.

### Error Handling

Configure error behavior with `errorPolicy`:

- `none` (default): Discard partial data on error
- `all`: Return partial data alongside errors
- `ignore`: Return data, suppress errors

```javascript
const { data, error } = useQuery(QUERY, {
  errorPolicy: "all"
});
```

### Data Completeness

The `dataState` property indicates result status:

- `empty`: No data available
- `partial`: Incomplete data from cache
- `streaming`: Deferred query still receiving data
- `complete`: Fully satisfied result

## Advanced Features

### skipToken

Type-safe query skipping mechanism:

```javascript
import { skipToken, useQuery } from "@apollo/client";

const { data } = useQuery(query, userId ? { variables: { userId } } : skipToken);
```

This avoids TypeScript type errors when conditionally skipping queries.

### useLazyQuery Promise Handling

Access results through returned promise:

```javascript
const [getDogs] = useLazyQuery(GET_DOGS);

const handleClick = async () => {
  const { data } = await getDogs();
  // Process data
};
```

Handle errors based on `errorPolicy`:

```javascript
try {
  const { data } = await getDogs();
} catch (error) {
  // Handle GraphQL or network errors
}
```

### Query Result Retention

Keep queries running after component unmount:

```javascript
const promise = getDogs();
promise.retain();
const { data } = await promise;
```

## Performance Optimization

### Caching Benefits

Apollo Client automatically caches results, providing instant responses for repeated queries without network requests.

### Variable Changes

When query variables change, `fetchPolicy` resets to its initial value by default, triggering fresh network requests for `network-only` policies.

### Return Partial Data

Enable partial results from cache:

```javascript
const { data } = useQuery(QUERY, {
  returnPartialData: true
});
```

Useful for rendering incomplete data while waiting for full results.

## Result Object Properties

### Data Properties

- `data`: Query result (may be partial based on `dataState`)
- `previousData`: Result from previous execution
- `variables`: Variables used in query
- `dataState`: Completeness indicator

### Network Properties

- `loading`: Boolean indicating in-flight status
- `networkStatus`: Granular operation state
- `client`: ApolloClient instance reference

### Helper Functions

- `refetch()`: Re-execute with optional new variables
- `fetchMore()`: Pagination support
- `startPolling(interval)`: Begin periodic updates
- `stopPolling()`: End polling
- `subscribeToMore()`: Subscribe to real-time updates
- `updateQuery()`: Manually update cached result

## Best Practices

1. **Use appropriate fetch policies** based on data freshness requirements
2. **Configure `nextFetchPolicy`** for optimal cache usage after initial load
3. **Handle loading states explicitly** to provide user feedback
4. **Leverage `skipToken`** for type-safe conditional queries
5. **Use `refetch` and polling** judiciously to avoid excessive server load
6. **Implement error boundaries** around query execution for resilience
7. **Monitor `networkStatus`** for granular state updates beyond simple `loading`

## Related Documentation

- [Mutations](https://www.apollographql.com/docs/react/data/mutations/)
- [Subscriptions](https://www.apollographql.com/docs/react/data/subscriptions/)
- [Caching](https://www.apollographql.com/docs/react/caching/overview/)
- [Error Handling](https://www.apollographql.com/docs/react/data/error-handling/)
- [Suspense Support](https://www.apollographql.com/docs/react/data/suspense/)
