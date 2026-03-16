# Source: https://www.apollographql.com/docs/kotlin/essentials/queries.md

# Source: https://www.apollographql.com/docs/ios/fetching/queries.md

# Source: https://www.apollographql.com/docs/react/data/queries.md

# Queries

This article shows how to fetch GraphQL data in React with the `useQuery` hook and attach the result to your UI. You'll also learn how Apollo Client simplifies data management code by tracking error and loading states for you.

This article shows how to use Apollo Client in a React application that
doesn't make use of React's "Suspense" features. For modern React applications
built around Suspense, suspense-enabled data fetching hooks are described in
Apollo Client's [Suspense docs](https://www.apollographql.com/docs/react/data/suspense/).

## Prerequisites

If your application is built using TypeScript, we recommend reading the [TypeScript guide](https://www.apollographql.com/docs/react/development-testing/static-typing) to learn how to use TypeScript with Apollo Client.

This article assumes you're familiar with building basic GraphQL queries. If you need a refresher, we recommend [this guide](http://graphql.org/learn/queries/). You can also build example queries against Apollo's [full-stack tutorial server](https://apollo-fullstack-tutorial.herokuapp.com/graphql).

This article also assumes that you've already set up Apollo Client and have wrapped your React app in an `ApolloProvider` component. For more information, see the [getting started guide](https://www.apollographql.com/docs/react/get-started/).

> To follow along with the examples below, open up our [starter project](https://codesandbox.io/s/queries-example-app-start-nvp9z) and [sample GraphQL server](https://codesandbox.io/s/queries-example-app-server-71z1g) on CodeSandbox. You can view the completed version of the app [here](https://codesandbox.io/s/queries-example-app-final-nrlnl).

## Executing a query

The `useQuery` [React hook](https://react.dev/reference/react) is the primary API for executing queries in a non-suspenseful Apollo application (for information about using Apollo Client with suspenseful React, see [Suspense](https://www.apollographql.com/docs/react/data/suspense)). To run a query within a React component, call `useQuery` and pass it a GraphQL document. When your component renders, `useQuery` returns an object from Apollo Client that contains `loading`, `error`, `dataState` and `data` properties you can use to render your UI.

Let's look at an example. First, we'll create a GraphQL query named `GET_DOGS`. Remember to wrap query strings in the `gql` function to parse them into query documents:

```js title=index.js
import { gql } from "@apollo/client";
import { useQuery } from "@apollo/client/react";

const GET_DOGS = gql`
  query GetDogs {
    dogs {
      id
      breed
    }
  }
`;
```

Next, we'll create a component named `Dogs`. Inside it, we'll pass our `GET_DOGS` query to the `useQuery` hook:

```jsx title=index.js
function Dogs({ onDogSelected }) {
  const { loading, error, data } = useQuery(GET_DOGS);

  if (loading) return "Loading...";
  if (error) return `Error! ${error.message}`;

  return (
    <select name="dog" onChange={onDogSelected}>
      {data.dogs.map((dog) => (
        <option key={dog.id} value={dog.breed}>
          {dog.breed}
        </option>
      ))}
    </select>
  );
}
```

As our query executes and the values of `loading`, `error`, and `data` change, the `Dogs` component can intelligently render different UI elements according to the query's state:

* As long as `loading` is `true` (indicating the query is still in flight), the component presents a `Loading...` notice.
* When loading is `false` and there is no `error`, the query has completed. The component renders a dropdown menu that's populated with the list of dog breeds returned by the server.

When the user selects a dog breed from the populated dropdown, the selection is sent to the parent component via the provided `onDogSelected` function.

If you are using TypeScript, `data` is typed as `unknown` when the query type is unknown. Accessing fields on `data` results in a TypeScript error. See the [TypeScript with Apollo Client](https://www.apollographql.com/docs/react/development-testing/static-typing) guide to learn how to add types for your queries.

In the next step, we'll associate the dropdown with a more sophisticated query that uses GraphQL variables.

## Caching query results

Whenever Apollo Client fetches query results from your server, it automatically **caches** those results locally. This makes later executions of that same query extremely fast.

To see this caching in action, let's build a new component called `DogPhoto`. `DogPhoto` accepts a prop called `breed` that reflects the current value of the dropdown menu in our `Dogs` component:

```jsx title=index.js
const GET_DOG_PHOTO = gql`
  query Dog($breed: String!) {
    dog(breed: $breed) {
      id
      displayImage
    }
  }
`;

function DogPhoto({ breed }) {
  const { loading, error, data } = useQuery(GET_DOG_PHOTO, {
    variables: { breed },
  });

  if (loading) return null;
  if (error) return `Error! ${error}`;

  return (
    <img src={data.dog.displayImage} style={{ height: 100, width: 100 }} />
  );
}
```

Notice that we're providing a configuration option (`variables`) to the `useQuery` hook this time. The `variables` option is an object that contains all of the variables we want to pass to our GraphQL query. In this case, we want to pass the currently selected `breed` from the dropdown.

Select `bulldog` from the dropdown to see its photo appear. Then switch to another breed, and then switch *back* to `bulldog`. You'll notice that the bulldog photo loads instantly the second time around. This is the cache at work!

Next, let's learn some techniques for ensuring that our cached data is fresh.

## Updating cached query results

Sometimes, you want to make sure that your query's cached data is up to date with your *server's* data. Apollo Client supports two strategies for this: **polling** and **refetching**.

### Polling

Polling provides near-real-time synchronization with your server by executing your query periodically at a specified interval. To enable polling for a query, pass a `pollInterval` configuration option to the `useQuery` hook with an interval in milliseconds:

```jsx title=index.js
function DogPhoto({ breed }) {
  const { loading, error, data } = useQuery(GET_DOG_PHOTO, {
    variables: { breed },
    pollInterval: 500,
  });

  if (loading) return null;
  if (error) return `Error! ${error}`;

  return (
    <img src={data.dog.displayImage} style={{ height: 100, width: 100 }} />
  );
}
```

By setting `pollInterval` to 500, we fetch the current breed's image from the server every 0.5 seconds. Note that if you set `pollInterval` to `0`, the query does **not** poll.

> You can also start and stop polling dynamically with the [`startPolling` and `stopPolling` functions](https://www.apollographql.com/docs/react/data/queries.md#startpolling) that are returned by the `useQuery` hook. When using these functions, set the `pollInterval` configuration option as a parameter of the `startPolling` function.

### Refetching

Refetching enables you to refresh query results in response to a particular user
action, as opposed to using a fixed interval.

Let's add a button to our `DogPhoto` component that calls our query's
`refetch` function whenever it's clicked.

You can optionally provide a new `variables` object to the `refetch` function.
If you don't provide a `variables` object, the query uses the same `variables`
object that it used in its previous execution.

```jsx title=index.js
function DogPhoto({ breed }) {
  const { loading, error, data, refetch } = useQuery(GET_DOG_PHOTO, {
    variables: { breed },
  });

  if (loading) return null;
  if (error) return `Error! ${error}`;

  return (
    <div>
      <img src={data.dog.displayImage} style={{ height: 100, width: 100 }} />
      <button onClick={() => refetch()}>Refetch new breed!</button>
    </div>
  );
}
```

Click the button and notice that the UI updates with a new dog photo. Refetching is an excellent way to guarantee fresh data, but it introduces some complexity with loading state. In the next section, we'll cover strategies for handling complex loading and error state.

#### Providing new variables to `refetch`

You call `refetch` with a new set of variables like so:

```jsx
<button
  onClick={() =>
    refetch({
      breed: "dalmatian", // Always refetches a dalmatian instead of original breed
    })
  }
>
  Refetch!
</button>;
```

If you provide new values for *some* of your original query's variables but not *all* of them, `refetch` uses each omitted variable's original value.

## Inspecting loading states

We've already seen that the `useQuery` hook exposes our query's current loading state. This is helpful when a query first loads, but what happens to our loading state when we're refetching or polling?

Let's return to our refetching example from the previous section. If you click the refetch button, you'll see that the component re-renders while we're refetching the photo.

The `useQuery` hook's result object provides fine-grained information about the status of the query via the `networkStatus` property. This allows us to indicate to the user that we're refetching the photo:

```jsx title=index.js
import { NetworkStatus } from "@apollo/client";

function DogPhoto({ breed }) {
  const { loading, error, data, refetch, networkStatus } = useQuery(
    GET_DOG_PHOTO,
    {
      variables: { breed },
    }
  );

  if (networkStatus === NetworkStatus.refetch) return "Refetching!";
  if (loading) return null;
  if (error) return `Error! ${error}`;

  return (
    <div>
      <img src={data.dog.displayImage} style={{ height: 100, width: 100 }} />
      <button onClick={() => refetch()}>Refetch!</button>
    </div>
  );
}
```

The value of `loading` also updates accordingly. Even if you don't use the more fine-grained information provided by the `networkStatus` property, the `loading` property indicates that the refetch is in progress.

The `networkStatus` property is a `NetworkStatus` enum that represents different loading states. Refetch is represented by `NetworkStatus.refetch`. There are additional values for e.g. polling and pagination. For a full list of all the possible loading states, check out [this table](https://www.apollographql.com/docs/react/api/core/ObservableQuery#networkstatus).

If you want to disable automatic re-rendering when the network status changes, set `notifyOnNetworkStatusChange` to `false` either in individual queries or globally via `defaultOptions`:

```js
const client = new ApolloClient({
  // ... other options
  defaultOptions: {
    watchQuery: {
      notifyOnNetworkStatusChange: false,
    },
  },
});
```

> To view a complete version of the app we just built, check out the CodeSandbox [here](https://codesandbox.io/s/queries-example-app-final-nrlnl).

## Inspecting error states

You can customize your query error handling by providing the `errorPolicy`
configuration option to the `useQuery` hook. The default value is `none`, which tells Apollo Client to treat all GraphQL errors as runtime errors. In this case, Apollo Client discards any query response data returned by the server and sets the `error` property in the `useQuery` result object.

If you set `errorPolicy` to `all`, `useQuery` does *not* discard query response data, allowing you to render partial results.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling/).

## Fetching in response to user interaction

When React renders a component that calls `useQuery`, Apollo Client automatically executes the corresponding query. But what if you want to execute a query in response to a user interaction, such as a user clicking a button?

The [`useLazyQuery`](https://www.apollographql.com/docs/react/api/react/useLazyQuery) hook is for manually executing queries. Unlike `useQuery`, when you use `useLazyQuery`, it doesn't immediately execute its associated query. Instead, it returns an execution function that you call whenever you need to execute the query.

Here's an example:

```jsx title=index.js
import React from "react";
import { useLazyQuery } from "@apollo/client/react";

function GetDogsOnClick() {
  const [getDogs, { loading, error, data }] = useLazyQuery(GET_DOGS);

  if (loading) return <p>Loading ...</p>;
  if (error) return `Error! ${error.message}`;

  return (
    <div>
      {data?.dogs.map((dog) => (
        <Dog key={dog.id} dog={dog} />
      ))}
      <button onClick={() => getDogs()}>Load dogs</button>
    </div>
  );
}
```

The first item in `useLazyQuery`'s return tuple is the execution function, and the second item is an object that contains information about the executed query, such as the `loading`, `error`, `data`, and `dataState` properties.

### Re-rendering with new options

Unlike `useQuery`, options provided to `useLazyQuery` that change on re-renders do not automatically execute the query. Instead, `useLazyQuery` waits to execute the query with the updated options until you call the execution function again.

The following is an example that changes the fetch policy depending on whether the user is online or offline:

```tsx
function GetDogs({ isOnline }) {
  const [getDogs, { loading, data }] = useLazyQuery(GET_DOGS, {
    fetchPolicy: isOnline ? "network-only" : "cache-only",
  });

  if (loading) return <p>Loading ...</p>;

  return (
    <div>
      {data && <Dogs data={data.dogs} />}
      <button onClick={() => getDogs()}>Get dogs</button>
    </div>
  );
}
```

The changed options are immediately applied to the underlying `ObservableQuery` (accessible by the `observable` property) even though the query isn't executed. Inspecting the options on the `observable` returns the updated options. This means the updated options are used for other APIs (such as `refetch`), even before you call the execution function again.

### Working with variables

You provide `variables` to the execution function when executing the query.

The following example gets a specific dog's photo when you click the **Get photo** button:

```jsx
function DogPhoto() {
  const [getDogPhoto, { loading, error, data }] = useLazyQuery(GET_DOG_PHOTO);

  if (loading) return <p>Loading ...</p>;
  if (error) return `Error! ${error.message}`;

  return (
    <div>
      {data?.dog && <img src={data.dog.displayImage} />}
      <button onClick={() => getDogPhoto({ variables: { name: "Lucky" } })}>
        Get photo
      </button>
    </div>
  );
}
```

When using TypeScript, the `variables` option is required if the query provided to `useLazyQuery` contains required variables. If the options argument isn't provided to the execution function, or the `variables` option is missing required variables, TypeScript raises an error.

#### Changing variables

You change variables by calling the execution function with updated variables.

The following example gets the selected dog's photo when you click the **Get photo** button.

```jsx
function DogPhoto() {
  const [selectedDog, setSelectedDog] = useState(null);
  const [getDogPhoto, { loading, error, data }] = useLazyQuery(GET_DOG_PHOTO);

  if (loading) return <p>Loading ...</p>;
  if (error) return `Error! ${error.message}`;

  return (
    <div>
      <DogSelect
        onChange={(dogName) => setSelectedDog(dogName)}
        value={selectedDog}
      />
      {data?.dog && <img src={data.dog.displayImage} />}
      {selectedDog && (
        <button
          onClick={() => getDogPhoto({ variables: { name: selectedDog } })}
        >
          Get photo
        </button>
      )}
    </div>
  );
}
```

If you need to reference the currently executed query's variables, use the `variables` property returned by `useLazyQuery`. The `variables` property contains the value of the variables from the last execution of the query.

The `variables` property is empty until you call the execution function for the first time. Use the `called` property returned by `useLazyQuery` to determine if you've called the execution function at least once.

```jsx
function DogPhoto() {
  const [getDogPhoto, { called, variables }] = useLazyQuery(GET_DOG_PHOTO);

  return (
    <div>
      {/* ... */}
      <button onClick={() => getDogPhoto({ variables: { name: selectedDog } })}>
        Get photo
      </button>

      {called && <span>Last fetched: {variables.name}</span>}
    </div>
  );
}
```

### Using the promise returned from the execution function

The execution function returns a promise that resolves with the query result:

```jsx
function GetDogs() {
  const [getDogs, { data, loading, error }] = useLazyQuery(GET_DOGS);

  const handleClick = async () => {
    const { data } = await getDogs();

    // Do something with `data`
  };

  return (
    <div>
      {/* ... */}
      <button onClick={handleClick}>Get dogs</button>
    </div>
  );
}
```

The result returned from the promise is useful when you need to execute side-effects using the data returned by the query.

Use the `data`, `error`, and other properties returned by `useLazyQuery` to sync the query state with your component. Avoid using your own state setters from React's `useState` hook with data resolved from the promise. This ensures your component stays up-to-date with cache changes as they occur throughout your application.

In cases where you don't need to keep your component in sync with query state, use `client.query()` directly because it won't unnecessarily render your component for data that you don't use.

Using `useLazyQuery` in these situations is an antipattern.

```ts
import { useApolloClient } from "@apollo/client/react";

function GetDogs() {
  const client = useApolloClient();

  const handleClick = async () => {
    const { data } = await client.query({ query: GET_DOGS });

    // Do something with `data`
  };

  return <button onClick={handleClick}>Get dogs</button>;
}
```

#### Handling errors

The promise resolves or rejects depending on the configured [`errorPolicy`](https://www.apollographql.com/docs/react/data/error-handling#setting-an-error-policy). For a more comprehensive guide on working with errors, read the [Error handling documentation](https://www.apollographql.com/docs/react/data/error-handling).

##### `errorPolicy: "none"`

The promise rejects with the error that caused the query to fail.

```ts
const handleClick = async () => {
  try {
    const { data } = await getDogs();
  } catch (error) {
    if (CombinedGraphQLErrors.is(error)) {
      // handle GraphQL errors
    }

    // Handle other error types
    console.log(error.message);
  }
};
```

Errors always cause the promise to reject. The `error` property is never set when the promise resolves.

##### `errorPolicy: "all"`

The promise resolves with an object that includes the error and any partial data returned by the query. Read the partial data on the `data` property and the error that caused the query to fail on the `error` property.

```ts
const handleClick = async () => {
  const { data, error } = await getDogs();

  if (CombinedGraphQLErrors.is(error)) {
    // handle GraphQL errors returned by the query
  }
};
```

The `data` property might be `undefined` instead of containing partial data. This typically occurs when a [network error](https://www.apollographql.com/docs/react/data/error-handling#network-errors) causes the query to fail, because the error isn't associated with GraphQL execution.

##### `errorPolicy: "ignore"`

The promise resolves with an object that includes any partial data returned by the query. Errors are discarded.

```ts
const handleClick = async () => {
  const { data } = await getDogs();

  if (data !== undefined) {
    // Do something with the returned data
  }
};
```

`data` might be `undefined` if a [network error](https://www.apollographql.com/docs/react/data/error-handling#network-errors) occurs. Check if `data` is `undefined` before you use it, in case an error occurs during query execution.

#### Retaining query results

Apollo Client aborts in-flight queries executed by `useLazyQuery` when the component unmounts or when you start another query by calling the execution function. This causes the promise to reject. In some cases, you might find this behavior undesirable and prefer to let the query run to completion.

Apollo Client ensures the rejected promise doesn't throw an unhandled rejection error when you don't add a rejection handler to the promise. However, this means that aborted errors are silent and might go unnoticed. If you want to be notified when the request is aborted, provide a rejection handler for the promise.

The promise returned by the execution function includes a `.retain()` method. When you call it, it ensures the query continues running even if the component unmounts or you start a new query before the previous one finishes.

```jsx
function GetDogs() {
  const [getDogs] = useLazyQuery(GET_DOGS);

  const handleClick = async () => {
    const promise = getDogs();

    // Retain the query even if component unmounts
    promise.retain();

    const { data } = await promise;

    // Do something with data
  };

  return <button onClick={handleClick}>Get dogs</button>;
}
```

The `retain()` method returns the original promise, so you can shorten the previous example to a single line:

```ts
const { data } = await getDogs().retain();
```

For a complete list of supported options and result properties, see the [`useLazyQuery` API reference](https://www.apollographql.com/docs/react/api/react/useLazyQuery).

## Setting a fetch policy

By default, the `useQuery` hook checks the Apollo Client cache to see if all the data you requested is already available. If all of the data *is* available in the cache, `useQuery` returns that data and *doesn't* query your GraphQL server. This `cache-first` policy is Apollo Client's default **fetch policy**.

You specify a fetch policy using the `fetchPolicy` option. For example, we can instruct `useQuery` to bypass the cache and fetch from the network by setting the `fetchPolicy` option to `network-only`:

```js
const { loading, error, data } = useQuery(GET_DOGS, {
  fetchPolicy: "network-only", // Doesn't check cache before making a network request
});
```

### `nextFetchPolicy`

You can *also* specify a query's `nextFetchPolicy`. When provided, `fetchPolicy` is used for the query's *first* execution, and `nextFetchPolicy` is used to determine how the query responds to future cache updates:

```js
const { loading, error, data } = useQuery(GET_DOGS, {
  fetchPolicy: "network-only", // Used for first execution
  nextFetchPolicy: "cache-first", // Used for subsequent executions
});
```

For example, this is helpful if you want a query to always make an initial network request, but you're comfortable reading from the cache after that.

#### `nextFetchPolicy` functions

If you want to apply a single `nextFetchPolicy` by default, because you find yourself manually providing `nextFetchPolicy` for most of your queries, you can configure `defaultOptions.watchQuery.nextFetchPolicy` when creating your `ApolloClient` instance:

```js
new ApolloClient({
  link,
  client,
  defaultOptions: {
    watchQuery: {
      nextFetchPolicy: "cache-only",
    },
  },
});
```

This configuration applies to all `client.watchQuery` calls and `useQuery` calls that do not otherwise configure `nextFetchPolicy`.

If you want more control over how `nextFetchPolicy` behaves, you can provide a function instead of a `WatchQueryFetchPolicy` string:

```js
new ApolloClient({
  link,
  client,
  defaultOptions: {
    watchQuery: {
      nextFetchPolicy(currentFetchPolicy) {
        if (
          currentFetchPolicy === "network-only" ||
          currentFetchPolicy === "cache-and-network"
        ) {
          // Demote the network policies (except "no-cache") to "cache-first"
          // after the first request.
          return "cache-first";
        }
        // Leave all other fetch policies unchanged.
        return currentFetchPolicy;
      },
    },
  },
});
```

This `nextFetchPolicy` function will be called after each request, and uses the `currentFetchPolicy` parameter to decide how to modify the fetch policy.

In addition to being called after each request, your `nextFetchPolicy` function will also be called when variables change, which by default resets the `fetchPolicy` to its initial value, which is often important to trigger a fresh network request for queries that started out with `cache-and-network` or `network-only` fetch policies.

To intercept and handle the `variables-changed` case yourself, you can use the `NextFetchPolicyContext` object passed as the second argument to your `nextFetchPolicy` function:

```js
new ApolloClient({
  link,
  client,
  defaultOptions: {
    watchQuery: {
      nextFetchPolicy(
        currentFetchPolicy,
        {
          // Either "after-fetch" or "variables-changed", indicating why the
          // nextFetchPolicy function was invoked.
          reason,
          // The rest of the options (currentFetchPolicy === options.fetchPolicy).
          options,
          // The original value of options.fetchPolicy, before nextFetchPolicy was
          // applied for the first time.
          initialFetchPolicy,
          // The ObservableQuery associated with this client.watchQuery call.
          observable,
        }
      ) {
        // When variables change, the default behavior is to reset
        // options.fetchPolicy to context.initialFetchPolicy. If you omit this logic,
        // your nextFetchPolicy function can override this default behavior to
        // prevent options.fetchPolicy from changing in this case.
        if (reason === "variables-changed") {
          return initialFetchPolicy;
        }

        if (
          currentFetchPolicy === "network-only" ||
          currentFetchPolicy === "cache-and-network"
        ) {
          // Demote the network policies (except "no-cache") to "cache-first"
          // after the first request.
          return "cache-first";
        }

        // Leave all other fetch policies unchanged.
        return currentFetchPolicy;
      },
    },
  },
});
```

In order to debug these `nextFetchPolicy` transitions, it can be useful to add `console.log` or `debugger` statements to the function body, to see when and why the function is called.

### Supported fetch policies

Name
Description

###### `cache-first`

(default)

Apollo Client first executes the query against the cache. If *all* requested data is present in the cache, that data is returned. Otherwise, Apollo Client executes the query against your GraphQL server and returns that data after caching it.

Prioritizes minimizing the number of network requests sent by your application.

This is the default fetch policy.

###### `cache-only`

Apollo Client executes the query *only* against the cache. It never queries your server in this case.

When the cache does not contain data for all requested fields, a `cache-only` query returns `data: undefined` with `dataState: "empty"` and a `networkStatus` of `NetworkStatus.ready`.

###### `cache-and-network`

Apollo Client executes the full query against both the cache *and* your GraphQL server. The query automatically updates if the result of the server-side query modifies cached fields.

Provides a fast response while also helping to keep cached data consistent with server data.

###### `network-only`

Apollo Client executes the full query against your GraphQL server, *without* first checking the cache. The query's result *is* stored in the cache. After the first result is received, external cache updates will be reflected by this query.

Prioritizes consistency with server data, but can't provide a near-instantaneous response when cached data is available.

###### `no-cache`

Similar to `network-only`, except the query's result *is not* stored in the cache and external cache updates are completely ignored.

###### `standby`

Uses the same logic as `cache-first`, except this query does *not* automatically update when underlying field values change. You can still *manually* update this query with `refetch` and `updateQueries`.

`standby` queries return `networkStatus: NetworkStatus.ready` even before subscription, providing immediate feedback to your UI.

## Skipping queries with `skipToken`

`skipToken` provides a type-safe mechanism to skip query execution. When you pass `skipToken` to `useQuery` instead of the options object, the hook will not execute the query and keeps the last `data` available. It is typically used conditionally to start query execution when the input data is available.

```js title=Recommended usage of skipToken with useQuery
import { skipToken, useQuery } from "@apollo/client/react";

const { data } = useQuery(query, id ? { variables: { id } } : skipToken);
```

Imagine this common scenario: You want to skip your query if a certain required variable is not set. You might be tempted to write something like this:

```ts
const { data } = useQuery(query, {
  variables: { id },
  skip: !id,
});
```

But in that case, TypeScript will complain:

```text
Type 'number | undefined' is not assignable to type 'number'.
      Type 'undefined' is not assignable to type 'number'.ts(2769)
```

To get around that, you have to tell TypeScript to ignore the fact that `id` could be `undefined`:

```ts
const { data } = useQuery(query, {
  variables: { id: id! },
  skip: !id,
});
```

Alternatively, you could also use some obscure default value:

```ts
const { data } = useQuery(query, {
  variables: { id: id || 0 },
  skip: !id,
});
```

Both of these solutions hide a potential bug. If your `skip` logic becomes more complex, you might accidentally introduce a bug that causes your query to execute, even when `id` is still `undefined`. In that case, TypeScript cannot warn you about it.

Instead we recommend using `skipToken`. It provides type safety without the need for an obscure default value:

```ts
const { data } = useQuery(query, id ? { variables: { id } } : skipToken);
```

Here it becomes apparent for TypeScript that there is a direct connection between skipping and the `variables` option - and it will work without unsafe workarounds.

## `useQuery` API

Supported options and result fields for the `useQuery` hook are listed below.

Most calls to `useQuery` can omit the majority of these options, but it's useful to know they exist. To learn about the `useQuery` hook API in more detail with usage examples, see the [API reference](https://www.apollographql.com/docs/react/api/react/hooks/#usequery).

### Options

The `useQuery` hook accepts the following options:

Operation options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the query.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

###### [`errorPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-errorpolicy)

`ErrorPolicy`

Specifies how the query handles a response that returns both GraphQL errors and partial results.

For details, see [GraphQL error policies](https://www.apollographql.com/docs/react/data/error-handling.md#graphql-error-policies).

The default value is `none`, meaning that the query result includes error details but not partial results.

###### [`skip`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-skip)

`boolean`

If true, the query is not executed.

The default value is `false`.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-variables)

`TVariables`

An object containing all of the GraphQL variables your query requires to execute.

Each key in the object corresponds to a variable name, and that key's value corresponds to the variable value.

Networking options

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-context)

`DefaultContext`

If you're using [Apollo Link](https://www.apollographql.com/docs/react/api/link/introduction.md), this object is the initial value of the `context` object that's passed along your link chain.

###### [`notifyOnNetworkStatusChange`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-notifyonnetworkstatuschange)

`boolean`

If `true`, the in-progress query's associated component re-renders whenever the network status changes or a network error occurs.

The default value is `true`.

###### [`pollInterval`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-pollinterval)

`number`

Specifies the interval (in milliseconds) at which the query polls for updated results.

The default value is `0` (no polling).

###### [`skipPollAttempt`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-skippollattempt)

`() => boolean`

A callback function that's called whenever a refetch attempt occurs while polling. If the function returns `true`, the refetch is skipped and not reattempted until the next poll interval.

###### [`ssr`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-ssr)

`boolean`

Pass `false` to skip executing the query during [server-side rendering](https://www.apollographql.com/docs/react/performance/server-side-rendering.md).

Caching options

###### [`fetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-fetchpolicy)

`WatchQueryFetchPolicy`

Specifies how the query interacts with the Apollo Client cache during execution (for example, whether it checks the cache for results before sending a request to the server).

For details, see [Setting a fetch policy](https://www.apollographql.com/docs/react/data/queries.md#setting-a-fetch-policy).

The default value is `cache-first`.

###### [`initialFetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-initialfetchpolicy)

`WatchQueryFetchPolicy`

Defaults to the initial value of options.fetchPolicy, but can be explicitly configured to specify the WatchQueryFetchPolicy to revert back to whenever variables change (unless nextFetchPolicy intervenes).

###### [`nextFetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-nextfetchpolicy)

`WatchQueryFetchPolicy | ((this: ApolloClient.WatchQueryOptions<TData, TVariables>, currentFetchPolicy: WatchQueryFetchPolicy, context: InternalTypes.NextFetchPolicyContext<TData, TVariables>) => WatchQueryFetchPolicy)`

Specifies the `FetchPolicy` to be used after this query has completed.

###### [`refetchWritePolicy`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-refetchwritepolicy)

`RefetchWritePolicy`

Specifies whether a `NetworkStatus.refetch` operation should merge incoming field data with existing data, or overwrite the existing data. Overwriting is probably preferable, but merging is currently the default behavior, for backwards compatibility with Apollo Client 3.x.

###### [`returnPartialData`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryhookoptions-interface-returnpartialdata)

`boolean`

If `true`, the query can return partial results from the cache if the cache doesn't contain results for all queried fields.

The default value is `false`.

### Result

After being called, the `useQuery` hook returns a result object with the following properties. This object contains your query result, plus some helpful functions for refetching, dynamic polling, and pagination.

Operation data

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-data)

`DataValue.Complete<TData> | DataValue.Streaming<TData> | DataValue.Partial<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`dataState`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-datastate)

`"complete" | "streaming" | "partial" | "empty"`

Describes the completeness of `data`.

* `empty`: No data could be fulfilled from the cache or the result is incomplete. `data` is `undefined`.

* `partial`: Some data could be fulfilled from the cache but `data` is incomplete. This is only possible when `returnPartialData` is `true`.

* `streaming`: `data` is incomplete as a result of a deferred query and the result is still streaming in.

* `complete`: `data` is a fully satisfied query result fulfilled either from the cache or network.

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-error)

`ErrorLike`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`previousData`*(optional)*](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-previousdata)

`MaybeMasked<TData>`

An object containing the result from the most recent *previous* execution of this query.

This value is `undefined` if this is the query's first execution.

###### [`variables`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-variables)

`TReturnVariables`

An object containing the variables that were provided for the query.

Network info

###### [`client`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-client)

`ApolloClient`

The instance of Apollo Client that executed the query. Can be useful for manually executing followup queries or writing data to the cache.

###### [`loading`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-loading)

`boolean`

If `true`, the query is still in flight.

###### [`networkStatus`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-networkstatus)

`NetworkStatus`

A number indicating the current network state of the query's associated request. [See possible values.](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/core/networkStatus.ts#L4)

Used in conjunction with the [`notifyOnNetworkStatusChange`](https://www.apollographql.com/docs.md#notifyonnetworkstatuschange) option.

Helper functions

###### [`fetchMore`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-fetchmore)

`<TFetchData = TData, TFetchVars extends OperationVariables = TVariables>(fetchMoreOptions: ObservableQuery.FetchMoreOptions<TData, TVariables, TFetchData, TFetchVars>) => Promise<ApolloClient.QueryResult<MaybeMasked<TFetchData>>>`

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

###### [`refetch`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-refetch)

`(variables?: Partial<TVariables>) => Promise<ApolloClient.QueryResult<MaybeMasked<TData>>>`

A function that enables you to re-execute the query, optionally passing in new `variables`.

To guarantee that the refetch performs a network request, its `fetchPolicy` is set to `network-only` (unless the original query's `fetchPolicy` is `no-cache` or `cache-and-network`, which also guarantee a network request).

See also [Refetching](https://www.apollographql.com/docs/react/data/queries.md#refetching).

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

###### [`startPolling`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-startpolling)

`(pollInterval: number) => void`

A function that instructs the query to begin re-executing at a specified interval (in milliseconds).

###### [`stopPolling`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-stoppolling)

`() => void`

A function that instructs the query to stop polling after a previous call to `startPolling`.

###### [`subscribeToMore`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-subscribetomore)

`SubscribeToMoreFunction<TData, TVariables>`

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.

###### [`updateQuery`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-updatequery)

`(mapFn: UpdateQueryMapFn<TData, TVariables>) => void`

A function that enables you to update the query's cached result without executing a followup GraphQL operation.

See [using updateQuery and updateFragment](https://www.apollographql.com/docs/react/caching/cache-interaction.md#using-updatequery-and-updatefragment) for additional information.

Other

###### [`observable`](https://www.apollographql.com/docs/react/data/queries.md#queryresult-interface-observable)

`ObservableQuery<TData, TVariables>`

A reference to the internal `ObservableQuery` used by the hook.

## Next steps

Now that you understand how to fetch data with the `useQuery` hook, [learn how to *update* your data with the `useMutation` hook!](https://www.apollographql.com/docs/react/data/mutations/)

After that, learn about some other handy Apollo Client features:

* [Local state management](https://www.apollographql.com/docs/react/local-state/local-state-management/): Learn how to query local data.
* [Pagination](https://www.apollographql.com/docs/react/pagination/overview): Learn how to fetch data incrementally from list fields.
