# Source: https://www.apollographql.com/docs/kotlin/essentials/mutations.md

# Source: https://www.apollographql.com/docs/ios/fetching/mutations.md

# Source: https://www.apollographql.com/docs/react/data/mutations.md

# Mutations in Apollo Client

Now that we've [learned how to query data](https://www.apollographql.com/docs/react/data/queries/) from our backend with Apollo Client, the natural next step is to learn how to *modify* back-end data with **mutations**.

This article demonstrates how to send updates to your GraphQL server with the `useMutation` hook. You'll also learn how to update the Apollo Client cache after executing a mutation, and how to track loading and error states.

> To follow along with the examples below, open up our [starter project](https://codesandbox.io/s/mutations-example-app-start-gm7i5) and [sample GraphQL server](https://codesandbox.io/s/mutations-example-app-server-sxewr) on CodeSandbox. You can view the completed version of the app [here](https://codesandbox.io/s/mutations-example-app-final-tjoje).

## Prerequisites

If your application is built using TypeScript, we recommend reading the [TypeScript guide](https://www.apollographql.com/docs/react/development-testing/static-typing) to learn how to use TypeScript with Apollo Client.

This article assumes you're familiar with building basic GraphQL mutations. If you need a refresher, we recommend that you
[read this guide](https://graphql.org/learn/mutations/).

This article also assumes that you've already set up Apollo Client and have wrapped your React app in an `ApolloProvider` component. For help with those steps, [get started](https://www.apollographql.com/docs/react/get-started/).

## Executing a mutation

The `useMutation` [React hook](https://react.dev/reference/react) is the primary API for executing mutations in an Apollo application.

To execute a mutation, you first call `useMutation` within a React component and pass it the mutation you want to execute, like so:

```jsx title=my-component.jsx
import { gql } from "@apollo/client";
import { useMutation } from "@apollo/client/react";

// Define mutation
const INCREMENT_COUNTER = gql`
  # Increments a back-end counter and gets its resulting value
  mutation IncrementCounter {
    incrementCounter {
      currentValue
    }
  }
`;

function MyComponent() {
  const [mutate, { data, loading, error }] = useMutation(INCREMENT_COUNTER);
}
```

As shown above, you use the `gql` function to parse the mutation string into a GraphQL document that you then pass to `useMutation`.

When your component renders, `useMutation` returns a tuple that includes:

* A **mutate function** that you can call at any time to execute the mutation
  * Unlike `useQuery`, `useMutation` *doesn't* execute its operation automatically on render. Instead, call the `mutate` function to execute the mutation.
* An object with fields that represent the current status of the mutation's execution (`data`, `loading`, etc.)
  * This object is similar to the object returned by the `useQuery` hook. For details, see [Result](https://www.apollographql.com/docs/react/data/mutations.md#result).

### Example

Let's say we're creating a to-do list application and we want the user to be able to add items to their list. First, we'll create a corresponding GraphQL mutation named `ADD_TODO`. Remember to wrap GraphQL strings in the `gql` function to parse them into query documents:

```jsx title=add-todo.jsx
import { gql } from "@apollo/client";
import { useMutation } from "@apollo/client/react";

const ADD_TODO = gql`
  mutation AddTodo($type: String!) {
    addTodo(type: $type) {
      id
      type
    }
  }
`;
```

Next, we'll create a component named `AddTodo` that represents the submission form for the to-do list. Inside it, we'll pass our
`ADD_TODO` mutation to the `useMutation` hook:

```jsx title=add-todo.jsx
function AddTodo() {
  const [value, setValue] = useState("");
  const [addTodo, { data, loading, error }] = useMutation(ADD_TODO);

  if (loading) return "Submitting...";
  if (error) return `Submission error! ${error.message}`;

  return (
    <div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addTodo({ variables: { type: value } });
          setValue("");
        }}
      >
        <input
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
          }}
        />
        <button type="submit">Add Todo</button>
      </form>
    </div>
  );
}
```

In this example, our form's `onSubmit` handler calls the **mutate function** (named `addTodo`) that's returned by the `useMutation` hook. This tells Apollo Client to execute the mutation by sending it to our GraphQL server.

`useMutation` behaves differently than [`useQuery`](https://www.apollographql.com/docs/react/data/queries/), which executes its operation as soon as its component renders. This is because mutations are more commonly executed in response to a user action (such as submitting a form in this case).

### Providing options

The `useMutation` hook accepts an `options` object as its second parameter. Here's an example that provides some default values for GraphQL `variables`:

```js
const [addTodo, { data, loading, error }] = useMutation(ADD_TODO, {
  variables: {
    type: "placeholder",
    someOtherVariable: 1234,
  },
});
```

You can *also* provide options directly to your mutate function, as demonstrated in this snippet from [the example above](https://www.apollographql.com/docs/react/data/mutations.md#example):

```js
addTodo({
  variables: {
    type: value,
  },
});
```

Here, we use the `variables` option to provide the values of any GraphQL variables that our mutation requires (specifically, the `type` of the created to-do item).

Learn more about the available options in [Options](https://www.apollographql.com/docs/react/data/mutations.md#options).

#### Option precedence

If you provide the same option to both `useMutation` *and* your mutate function, the mutate function's value takes precedence. In the specific case of the `variables` option, the two objects are merged *shallowly*, which means any variables provided only to `useMutation` are preserved in the resulting object. This helps you set default values for variables.

In [the example snippets above](https://www.apollographql.com/docs/react/data/mutations.md#providing-options), `value` would override `"placeholder"` as the value of the `type` variable. The value of `someOtherVariable` (`1234`) would be preserved.

When using TypeScript, you might see an error related to a missing variable when a required variable is not provided to either the hook or the `mutate` function. Providing required variables to the hook makes them optional in the `mutate` function. If a required variable is not provided to the hook, it is required in the `mutate` function.

##### Merging `context` from the hook and `mutate` function

Due to option precedence, `context` provided to the `mutate` function overrides `context` provided to the `useMutation` hook. In some cases, you might want to merge the `context` value provided to the hook with a value available at the time you execute the `mutate` function.

You accomplish this by using a callback function for the `context` option provided to the `mutate` function. The callback function is called with the `context` value provided to the hook, allowing you to merge them together.

```ts
addTodo({
  context: (hookContext) => ({
    ...hookContext,
    myCustomValue: true,
  }),
});
```

Your callback function is not required to merge the context values together. The `context` value sent to the link chain is the value returned from the function which makes it possible to change the `context` value in any way you wish, such as omitting a property from the hook context.

### Tracking mutation status

In addition to a mutate function, the `useMutation` hook returns an object that represents the current state of the mutation's execution. The fields of this object include booleans that indicate whether the mutate function has been `called` and whether the mutation's result is currently `loading`.

[The example above](https://www.apollographql.com/docs/react/data/mutations.md#example) destructures the `loading` and `error` fields from this object to render the `AddTodo` component differently depending on the mutation's current status:

```jsx
if (loading) return "Submitting...";
if (error) return `Submission error! ${error.message}`;
```

The `useMutation` hook supports `onCompleted` and `onError` options if you need to perform side effects when the mutation completes. See the [API reference](https://www.apollographql.com/docs/react/api/react/useMutation) for more details.

Learn more about result object in [Result](https://www.apollographql.com/docs/react/data/mutations.md#result).

### Resetting mutation status

The mutation result object returned by `useMutation` includes a [`reset` function](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-reset):

```js
const [login, { reset }] = useMutation(LOGIN_MUTATION);
```

Call `reset` to reset the mutation's result to its initial state (i.e., *before* the mutate function was called). You can use this to enable users to dismiss mutation result data or errors in the UI.

Calling `reset` does *not* remove any cached data returned by the mutation's execution. It only affects the state associated with the `useMutation` hook, causing the corresponding component to rerender.

```js
function LoginPage() {
  const [login, { error, reset }] = useMutation(LOGIN_MUTATION);

  return (
    <>
      <form>
        <input class="login" />
        <input class="password" />
        <button onclick={login}>Login</button>
      </form>
      {error && (
        <LoginFailedMessageWindow
          message={error.message}
          onDismiss={() => reset()}
        />
      )}
    </>
  );
}
```

## Updating local data

When you execute a mutation, you modify back-end data. Usually, you then want to update your *locally cached* data to reflect the back-end modification. For example, if you execute a mutation to add an item to your to-do list, you also want that item to appear in your cached copy of the list.

### Supported methods

The most straightforward way to update your local data is to [refetch any queries](https://www.apollographql.com/docs/react/data/mutations.md#refetching-queries) that might be affected by the mutation. However, this method requires additional network requests.

If your mutation returns all of the objects and fields that it modified, you can [update your cache directly](https://www.apollographql.com/docs/react/data/mutations.md#updating-the-cache-directly) *without* making any followup network requests.

We recommend reading the guide on [Caching in Apollo Client](https://www.apollographql.com/docs/react/caching/overview) to understand how data is stored in the cache and how to perform updates to that data.

## Refetching queries

You can refetch queries after a mutation by providing a `refetchQueries` option to `useMutation`:

```js
// Refetches two queries after mutation completes
const [addTodo, { data, loading, error }] = useMutation(ADD_TODO, {
  refetchQueries: [
    GET_POST, // DocumentNode object parsed with gql
    "GetComments", // Query name
  ],
});
```

You can provide one of the following values to `refetchQueries`:

* A `refetchQueries` array to refetch specific queries
* The shorthand `"active"` string to refetch all active queries
* The shorthand `"all"` string to refetch all active and inactive queries

It is most common to provide a `refetchQueries` array when performing mutations. Learn more about active and inactive queries in the [Refetching](https://www.apollographql.com/docs/react/data/refetching) guide.

When providing `refetchQueries` as an array, each element in the `refetchQueries` array is one of the following:

* A `DocumentNode` object parsed with the `gql` function
* The name of a query as a string (e.g., `GetComments`)
  * To refer to queries by name, make sure each of your app's queries have a *unique* name.

Each query in the `refetchQueries` array must be an *active* query. If an inactive or unknown query is provided, a warning will be logged to the console.

Each included query is executed with its most recently provided set of variables.

You can provide the `refetchQueries` option either to `useMutation` or to the mutate function. For details, see [Option precedence](https://www.apollographql.com/docs/react/data/mutations.md#option-precedence).

## Updating the cache directly

### Include modified objects in mutation responses

As a best practice, a mutation response should include any object(s) the mutation modified. This enables Apollo Client to normalize those objects and cache them according to their `__typename` and [`keyFields`](https://www.apollographql.com/docs/react/caching/cache-configuration/#customizing-cache-ids).

[In the example above](https://www.apollographql.com/docs/react/data/mutations.md#example), our `ADD_TODO` mutation might return a `Todo` object with the following structure:

```json
{
  "__typename": "Todo",
  "id": "5",
  "type": "groceries"
}
```

Apollo Client automatically adds the `__typename` field to every object in your queries and mutations by default.

Upon receiving this response object, Apollo Client caches it with key `Todo:5`. If a cached object *already* exists with this key, Apollo Client overwrites any existing fields that are also included in the mutation response (other existing fields are preserved).

Returning modified objects like this is a helpful first step to keeping your cache in sync with your backend. However, it isn't always sufficient. For example, a newly cached object isn't automatically added to any *list fields* that should now include that object. To accomplish this, you can define an [`update` function](https://www.apollographql.com/docs/react/data/mutations.md#the-update-function).

### The `update` function

When a [mutation's response](https://www.apollographql.com/docs/react/data/mutations.md#include-modified-objects-in-mutation-responses) is insufficient to update *all* modified fields in your cache (such as certain list fields), you can define an `update` function to apply manual changes to your cached data after a mutation.

You provide an `update` function to `useMutation`, like so:

```jsx
const GET_TODOS = gql`
  query GetTodos {
    todos {
      id
    }
  }
`;

function AddTodo() {
  let input;
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
              `,
            });
            return [...existingTodos, newTodoRef];
          },
        },
      });
    },
  });

  return (
    <div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addTodo({ variables: { type: input.value } });
          input.value = "";
        }}
      >
        <input
          ref={(node) => {
            input = node;
          }}
        />
        <button type="submit">Add Todo</button>
      </form>
    </div>
  );
}
```

As shown, the `update` function is passed a `cache` object that represents the Apollo Client cache. This object provides access to cache API methods like `readQuery`/`writeQuery`, `readFragment`/`writeFragment`, `modify`, and `evict`. These methods enable you to execute GraphQL operations on the cache as though you're interacting with a GraphQL server.

> Learn more about supported cache functions in [Interacting with cached data](https://www.apollographql.com/docs/react/caching/cache-interaction/).

The `update` function is *also* passed an object with a `data` property that contains the result of the mutation. You can use this value to update the cache with `cache.writeQuery`, `cache.writeFragment`, or `cache.modify`.

If your mutation specifies an [optimistic response](https://www.apollographql.com/docs/react/performance/optimistic-ui/), your `update` function is called **twice**: once with the optimistic result, and again with the actual result of the mutation when it returns.

When the `ADD_TODO` mutation executes in the above example, the newly added and returned `addTodo` object is automatically saved into the cache *before* the `update` function runs. However, the cached list of `ROOT_QUERY.todos` (which is watched by the `GET_TODOS` query) is *not* automatically updated. This means that the `GET_TODOS` query isn't notified of the new `Todo` object, which in turn means that the query doesn't update to show the new item.

To address this, we use `cache.modify` to surgically insert or delete items from the cache, by running "modifier" functions. In the example above, we know the results of the `GET_TODOS` query are stored in the `ROOT_QUERY.todos` array in the cache, so we use a `todos` modifier function to update the cached array to include a reference to the newly added `Todo`. With the help of `cache.writeFragment`, we get an internal reference to the added `Todo`, then append that reference to the `ROOT_QUERY.todos` array.

Any changes you make to cached data inside of an `update` function are automatically broadcast to queries that are listening for changes to that data. Consequently, your application's UI will update to reflect these updated cached values.

### Refetching after `update`

An `update` function attempts to replicate a mutation's back-end modifications in your client's local cache. These cache modifications are broadcast to all affected active queries, which updates your UI automatically. If the `update` function does this correctly, your users see the latest data immediately, without needing to await another network round trip.

However, an `update` function might get this replication *wrong* by setting a cached value incorrectly. You can "double check" your `update` function's modifications by refetching affected active queries. To do so, you first provide an `onQueryUpdated` callback function to your mutate function:

```js
addTodo({
  variables: { type: input.value },
  update(cache, result) {
    // Update the cache as an approximation of server-side mutation effects
  },
  onQueryUpdated(observableQuery) {
    // Define any custom logic for determining whether to refetch
    if (shouldRefetchQuery(observableQuery)) {
      return observableQuery.refetch();
    }
  },
});
```

After your `update` function completes, Apollo Client calls `onQueryUpdated` *once for each active query with cached fields that were updated*. Within `onQueryUpdated`, you can use any custom logic to determine whether you want to refetch the associated query.

To refetch a query from `onQueryUpdated`, call `return observableQuery.refetch()`, as shown above. Otherwise, no return value is required. If a refetched query's response differs from your `update` function's modifications, your cache and UI are both automatically updated again. Otherwise, your users see no change.

Occasionally, it might be difficult to make your `update` function update all relevant queries. Not every mutation returns enough information for the `update` function to do its job effectively. To make absolutely sure a certain query is included, you can combine `onQueryUpdated` with `refetchQueries: [...]`:

```js
addTodo({
  variables: { type: input.value },
  update(cache, result) {
    // Update the cache as an approximation of server-side mutation effects.
  },
  // Force ReallyImportantQuery to be passed to onQueryUpdated.
  refetchQueries: ["ReallyImportantQuery"],
  onQueryUpdated(observableQuery) {
    // If ReallyImportantQuery is active, it will be passed to onQueryUpdated.
    // If no query with that name is active, a warning will be logged.
  },
});
```

If `ReallyImportantQuery` was already going to be passed to `onQueryUpdated` thanks to your `update` function, then it will only be passed once. Using `refetchQueries: ["ReallyImportantQuery"]` just guarantees the query will be included.

If you find you've included more queries than you expected, you can skip or ignore a query by returning `false` from `onQueryUpdated`, after examining the `ObservableQuery` to determine that it doesn't need refetching. Returning a `Promise` from `onQueryUpdated` causes the final `Promise<FetchResult<TData>>` for the mutation to await any promises returned from `onQueryUpdated`, eliminating the need for the legacy `awaitRefetchQueries: true` option.

To use the `onQueryUpdated` API without performing a mutation, try the [`client.refetchQueries`](https://www.apollographql.com/docs/react/data/refetching/#clientrefetchqueries) method. In the standalone `client.refetchQueries` API, the `refetchQueries: [...]` mutation option is called `include: [...]`, and the `update` function is called `updateCache` for clarity. Otherwise, the same internal system powers both `client.refetchQueries` and refetching queries after a mutation.

## `useMutation` API

Supported options and result fields for the `useMutation` hook are listed below.

Most calls to `useMutation` can omit the majority of these options, but it's
useful to know they exist. To learn about the `useMutation` hook API in more
detail with usage examples, see the [API reference](https://www.apollographql.com/docs/react/api/react/hooks/).

### Options

The `useMutation` hook accepts the following options:

Operation options

###### [`awaitRefetchQueries`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-awaitrefetchqueries)

`boolean`

If `true`, makes sure all queries included in `refetchQueries` are completed before the mutation is considered complete.

The default value is `false` (queries are refetched asynchronously).

###### [`errorPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-errorpolicy)

`ErrorPolicy`

Specifies how the mutation handles a response that returns both GraphQL errors and partial results.

For details, see [GraphQL error policies](https://www.apollographql.com/docs/react/data/error-handling.md#graphql-error-policies).

The default value is `none`, meaning that the mutation result includes error details but *not* partial results.

###### [`onCompleted`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-oncompleted)

`(data: MaybeMasked<TData>, clientOptions?: Options<TData, TVariables, TCache>) => void`

A callback function that's called when your mutation successfully completes with zero errors (or if `errorPolicy` is `ignore` and partial data is returned).

This function is passed the mutation's result `data` and any options passed to the mutation.

###### [`onError`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-onerror)

`(error: ErrorLike, clientOptions?: Options<TData, TVariables, TCache>) => void`

A callback function that's called when the mutation encounters one or more errors (unless `errorPolicy` is `ignore`).

This function is passed an [`ApolloError`](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/errors/index.ts#L36-L39) object that contains either a `networkError` object or a `graphQLErrors` array, depending on the error(s) that occurred, as well as any options passed the mutation.

###### [`onQueryUpdated`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-onqueryupdated)

`OnQueryUpdated<any>`

Optional callback for intercepting queries whose cache data has been updated by the mutation, as well as any queries specified in the `refetchQueries: [...]` list passed to `client.mutate`.

Returning a `Promise` from `onQueryUpdated` will cause the final mutation `Promise` to await the returned `Promise`. Returning `false` causes the query to be ignored.

###### [`refetchQueries`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-refetchqueries)

`((result: NormalizedExecutionResult<Unmasked<TData>>) => InternalRefetchQueriesInclude) | InternalRefetchQueriesInclude`

An array (or a function that *returns* an array) that specifies which queries you want to refetch after the mutation occurs.

Each array value can be either:

* An object containing the `query` to execute, along with any `variables`

* A string indicating the operation name of the query to refetch

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-variables)

`Partial<TVariables> & TConfiguredVariables`

An object containing all of the GraphQL variables your mutation requires to execute.

Each key in the object corresponds to a variable name, and that key's value corresponds to the variable value.

Networking options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the mutation.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-context)

`DefaultContext`

If you're using [Apollo Link](https://www.apollographql.com/docs/react/api/link/introduction.md), this object is the initial value of the `context` object that's passed along your link chain.

###### [`notifyOnNetworkStatusChange`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-notifyonnetworkstatuschange)

`boolean`

If `true`, the in-progress mutation's associated component re-renders whenever the network status changes or a network error occurs.

The default value is `true`.

Caching options

###### [`fetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-fetchpolicy)

`MutationFetchPolicy`

Provide `no-cache` if the mutation's result should *not* be written to the Apollo Client cache.

The default value is `network-only` (which means the result *is* written to the cache).

Unlike queries, mutations *do not* support [fetch policies](https://www.apollographql.com/docs/react/data/queries.md#setting-a-fetch-policy) besides `network-only` and `no-cache`.

###### [`optimisticResponse`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-optimisticresponse)

`Unmasked<NoInfer<TData>> | ((vars: TVariables, { IGNORE }: { IGNORE: IgnoreModifier; }) => Unmasked<NoInfer<TData>> | IgnoreModifier)`

By providing either an object or a callback function that, when invoked after a mutation, allows you to return optimistic data and optionally skip updates via the `IGNORE` sentinel object, Apollo Client caches this temporary (and potentially incorrect) response until the mutation completes, enabling more responsive UI updates.

For more information, see [Optimistic mutation results](https://www.apollographql.com/docs/react/performance/optimistic-ui.md).

###### [`update`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-update)

`MutationUpdaterFunction<TData, TVariables, TCache>`

A function used to update the Apollo Client cache after the mutation completes.

For more information, see [Updating the cache after a mutation](https://www.apollographql.com/docs/react/data/mutations.md#updating-the-cache-after-a-mutation).

Other

###### [`keepRootFields`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-keeprootfields)

`boolean`

To avoid retaining sensitive information from mutation root field arguments, Apollo Client v3.4+ automatically clears any `ROOT_MUTATION` fields from the cache after each mutation finishes. If you need this information to remain in the cache, you can prevent the removal by passing `keepRootFields: true` to the mutation. `ROOT_MUTATION` result data are also passed to the mutation `update` function, so we recommend obtaining the results that way, rather than using this option, if possible.

###### [`updateQueries`*(optional)*](https://www.apollographql.com/docs/react/data/mutations.md#mutationhookoptions-interface-updatequeries)

`MutationQueryReducersMap<TData>`

A `MutationQueryReducersMap`, which is map from query names to mutation query reducers. Briefly, this map defines how to incorporate the results of the mutation into the results of queries that are currently being watched by your application.

### Result

The `useMutation` result is a tuple with a mutate function in the first position and an object representing the mutation result in the second position.

You call the mutate function to trigger the mutation from your UI.

###### [`called`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-called)

`boolean`

If `true`, the mutation's mutate function has been called.

###### [`client`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-client)

`ApolloClient`

The instance of Apollo Client that executed the mutation.

Can be useful for manually executing followup operations or writing data to the cache.

###### [`data`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-data)

`MaybeMasked<TData> | null | undefined`

The data returned from your mutation. Can be `undefined` if the `errorPolicy` is `all` or `ignore` and the server returns a GraphQL response with `errors` but not `data` or a network error is returned.

###### [`error`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-error)

`ErrorLike | undefined`

If the mutation produces one or more errors, this object contains either an array of `graphQLErrors` or a single `networkError`. Otherwise, this value is `undefined`.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`loading`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-loading)

`boolean`

If `true`, the mutation is currently in flight.

###### [`reset`](https://www.apollographql.com/docs/react/data/mutations.md#mutationresult-interface-reset)

`() => void`

A function that you can call to reset the mutation's result to its initial, uncalled state.

## Next steps

The `useQuery` and `useMutation` hooks together represent Apollo Client's core
API for performing GraphQL operations. Now that you're familiar with both,
you can begin to take advantage of Apollo Client's full feature set, including:

* [Optimistic UI](https://www.apollographql.com/docs/react/performance/optimistic-ui/): Learn how to improve perceived performance by returning an optimistic response before your mutation result comes back from the server.
* [Local state](https://www.apollographql.com/docs/react/local-state/local-state-management/): Use Apollo Client to manage the entirety of your application's local state by executing client-side mutations.
* [Caching in Apollo](https://www.apollographql.com/docs/react/caching/cache-configuration/): Dive deep into the Apollo Client cache and how it's normalized. Understanding the cache is helpful when writing `update` functions for your mutations!
