# Source: https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md

# class InMemoryCache

Methods of the `InMemoryCache` class (the cache used by almost every instance of [`ApolloClient`](https://www.apollographql.com/docs/react/api/core/ApolloClient/)) are documented here.

> Before reading about individual methods, see [Caching in Apollo Client](https://www.apollographql.com/docs/react/caching/overview/).

## `readQuery`

Executes a GraphQL query directly against the cache and returns its result (or `null` if the query cannot be fulfilled):

```js
// Query a cached Todo object with id 5
const { todo } = cache.readQuery({
  query: gql`
    query ReadTodo {
      todo(id: 5) {
        id
        text
        completed
      }
    }
  `,
});
```

For usage instructions, see [Interacting with cached data: `readQuery`](https://www.apollographql.com/docs/react/caching/cache-interaction/#readquery).

Accepts the following parameters:

Name /Type
Description

###### `options`

`Object`

**Required.** Provides configuration options for the query, including the actual query to execute.

Supported fields are listed below.

###### `optimistic`

`Boolean`

If `true`, `readQuery` returns optimistic results.

The default value is `false`.

### Options

Name /Type
Description

###### `query`

`DocumentNode`

**Required.** The GraphQL query to execute, created by wrapping a query string in the `gql` template literal.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `query`.

###### `id`

`String`

The root `id` to use for the query.

The default value is `ROOT_QUERY`, which is the ID of the root query object.

By specifying the ID of another cached object, you can query arbitrary cached data without conforming to the structure of your schema's supported queries. This enables `readQuery` to behave similarly to [`readFragment`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#readfragment).

### Signature

```ts title=src/cache/core/cache.ts
readQuery<TData = unknown, TVariables = OperationVariables>(
  options: Cache.ReadQueryOptions<TData, TVariables>,
  optimistic: boolean = false,
): Unmasked<TData> | null
```

## `writeQuery`

Writes data to the cache in the shape of a provided GraphQL query. Returns a `Reference` to the written object or `undefined` if the write failed.

```js
// Create or modify a cached Todo object with id 5
cache.writeQuery({
  query: gql`
    query ReadTodo($id: ID!) {
      todo(id: $id) {
        id
        text
        completed
      }
    }
  `,
  data: {
    todo: {
      __typename: "Todo",
      id: 5,
      text: "Buy grapes 🍇",
      completed: false,
    },
  },
  variables: {
    id: 5,
  },
});
```

For usage instructions, see [Interacting with cached data: `writeQuery`](https://www.apollographql.com/docs/react/caching/cache-interaction/#writequery).

Takes an `options` object as a parameter. Supported fields of this object are described below.

### Options

Name /Type
Description

###### `query`

`DocumentNode`

**Required.** The GraphQL query that defines the shape of the data to write. Created by wrapping a query string in the `gql` template literal.

###### `data`

`Object`

**Required.** The data to write to the cache. This object's fields must conform to the shape defined by `query`.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `query`.

###### `id`

`String`

The `id` of the root object to use with `query`.

The default value is `ROOT_QUERY`, which is the ID of the root query object.

By specifying the ID of another cached object, you can modify arbitrary cached data without conforming to the structure of your schema's supported queries. This enables `writeQuery` to behave similarly to [`writeFragment`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#writefragment).

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's modified by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

###### `overwrite`

`Boolean`

If `true`, ignore existing cache data when calling `merge` functions, allowing incoming data to replace existing data, without warnings about data loss.

The default value is `false`.

### Signature

```ts title=src/cache/core/cache.ts
writeQuery<TData = unknown, TVariables = OperationVariables>(
  options: Cache.WriteQueryOptions<TData, TVariables>,
): Reference | undefined
```

## `updateQuery`

Fetches data from the cache in the shape of a provided GraphQL query, then *updates* that cached data according to a provided update function.

Returns the updated result or `null` if the update failed.

```js
// Fetches a Todo object with id 5 and flips its `completed` boolean
cache.updateQuery(
  // options object
  {
    query: gql`
      query ReadTodo($id: ID!) {
        todo(id: $id) {
          id
          text
          completed
        }
      }
    `,
    variables: {
      id: 5,
    },
  },
  // update function
  (data) => ({
    todo: {
      ...data.todo,
      completed: !data.todo.completed,
    },
  })
);
```

Takes an `options` object and an update function as parameters (both described below).

### Options

Name /Type
Description

###### `query`

`DocumentNode`

**Required.** The GraphQL query that defines the shape of the data to fetch. Created by wrapping a query string in the `gql` template literal.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `query`.

###### `id`

`String`

The `id` of the root object to use with `query`.

The default value is `ROOT_QUERY`, which is the ID of the root query object.

By specifying the ID of another cached object, you can modify arbitrary cached data without conforming to the structure of your schema's supported queries. This enables `updateQuery` to behave similarly to [`updateFragment`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#updatefragment).

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's modified by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

###### `overwrite`

`Boolean`

If `true`, ignore existing cache data when calling `merge` functions, allowing incoming data to replace existing data, without warnings about data loss.

The default value is `false`.

### `updateQuery` update function

The update function of `updateQuery` takes a query's current cached value and returns the value that should replace it (or `undefined` if no change should be made).

The returned value is automatically passed to [`writeQuery`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#writequery), which modifies the cached data.

Please note the `update` function has to calculate the new value in an immutable way. You can read more about immutable updates in the [React documentation](https://beta.reactjs.org/learn/updating-objects-in-state).

### Signature

```ts title=src/cache/core/cache.ts
public updateQuery<TData = unknown, TVariables = OperationVariables>(
  options: Cache.UpdateQueryOptions<TData, TVariables>,
  update: (data: TData | null) => TData | null | void,
): TData | null
```

## `readFragment`

Reads data from the cache in the shape of a provided GraphQL fragment:

```js
const todo = cache.readFragment({
  id: "5", // The value of the to-do item's unique identifier
  fragment: gql`
    fragment MyTodo on Todo {
      id
      text
      completed
    }
  `,
});
```

Returns the requested data or `null` if data is not available in the cache.

For usage instructions, see [Interacting with cached data: `readFragment`](https://www.apollographql.com/docs/react/caching/cache-interaction/#readfragment).

Accepts the following parameters:

Name /Type
Description

###### `options`

`Object`

**Required.** Provides configuration options, including the actual fragment to use.

Supported fields are listed below.

###### `optimistic`

`Boolean`

If `true`, `readFragment` returns optimistic results.

The default value is `false`.

### Options

Name /Type
Description

###### `id`

`String`

**Required.** The ID of the cached object that this call is reading a fragment of.

If the cache does not contain an object with the specified ID, `readFragment` returns `null`.

###### `fragment`

`DocumentNode`

**Required.** A GraphQL document created with the `gql` template literal tag that includes the fragment to read.

If the document includes more than one fragment, you must also provide [`fragmentName`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#fragmentname) to indicate which to use.

###### `fragmentName`

`String`

The name of the fragment defined in the `fragment` document to use in the call.

You don't need to provide this value if the `fragment` document includes only one fragment.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `fragment`.

### Signature

```ts title=src/cache/core/cache.ts
readFragment<TData = unknown, TVariables = OperationVariables>(
  options: Cache.ReadFragmentOptions<TData, TVariables>,
  optimistic: boolean = false,
): Unmasked<TData> | null
```

## `writeFragment`

Writes data to the cache in the shape of the provided GraphQL fragment. Returns a `Reference` to the written object or `undefined` if the write failed.

```js
client.writeFragment({
  id: "Todo:5",
  fragment: gql`
    fragment MyTodo on Todo {
      completed
    }
  `,
  data: {
    completed: true,
  },
});
```

For usage instructions, see [Interacting with cached data: `writeFragment`](https://www.apollographql.com/docs/react/caching/cache-interaction/#writefragment).

Takes an `options` object as a parameter. Supported fields of this object are described below.

### Options

Name /Type
Description

###### `id`

`String`

**Required.** The ID of the cached object that this call is writing a fragment to.

If the cache does not contain an object with the specified ID, `writeFragment` returns `null`.

###### `fragment`

`DocumentNode`

**Required.** A GraphQL document created with the `gql` template literal tag that includes the fragment to write.

If the document includes more than one fragment, you must also provide [`fragmentName`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#fragmentname) to indicate which to use.

###### `data`

`Object`

**Required.** The data to write to the cache. This object's fields must conform to the shape defined by `fragment`.

###### `fragmentName`

`String`

The name of the fragment defined in the `fragment` document to use in the call.

You don't need to provide this value if the `fragment` document includes only one fragment.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `fragment`.

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's modified by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

###### `overwrite`

`Boolean`

If `true`, ignore existing cache data when calling `merge` functions, allowing incoming data to replace existing data, without warnings about data loss.

The default value is `false`.

### Signature

```ts title=src/cache/core/cache.ts
writeFragment<TData = unknown, TVariables = OperationVariables>(
  options: Cache.WriteFragmentOptions<TData, TVariables>,
): Reference | undefined
```

## [`watchFragment`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment)Requires ≥ 3.10.0

Watches the cache store of the fragment according to the options specified and returns an `Observable`. We can subscribe to this `Observable` and receive updated results through an observer when the cache store changes.

You must pass in a GraphQL document with a single fragment or a document with multiple fragments that represent what you are reading. If you pass in a document with multiple fragments then you must also specify a `fragmentName`.

### [Signature](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment-signature)

TypeScript

```
watchFragment<TData, TVariables>(
  options: ApolloClient.WatchFragmentOptions<TData, TVariables> & {
        from: Array<ApolloCache.FromOptionValue<TData>>;
    }
): ApolloClient.ObservableFragment<Array<TData>>
```

### [Parameters](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment-parameters-options)\
`ApolloClient.WatchFragmentOptions<TData, TVariables> & { from: Array<ApolloCache.FromOptionValue<TData>>; }`

An object of type `WatchFragmentOptions` that allows the cache to identify the fragment and optionally specify whether to react to optimistic updates.

### [Result](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment-result)

```
ApolloClient.ObservableFragment<Array<TData>>
```

Show/hide child attributes

(Warning: some properties might be missing from the table due to complex inheritance!)

###### [`getCurrentResult`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#watchfragment-result-getcurrentresult)

`() => ApolloClient.WatchFragmentResult<Array<TData>>`

Return the current result for the fragment.

## `updateFragment`

Fetches data from the cache in the shape of a provided GraphQL fragment, then *updates* that cached data according to a provided update function.

Returns the updated result or `null` if the update failed.

```js
// Fetches a Todo object with id 5 and sets its `completed` boolean to true
const todo = cache.updateFragment(
  // options object
  {
    id: "5", // The value of the to-do item's unique identifier
    fragment: gql`
      fragment MyTodo on Todo {
        completed
      }
    `,
  },
  // update function
  (data) => ({ ...data, completed: true })
);
```

Takes an `options` object and an update function as parameters (both described below).

### Options

Name /Type
Description

###### `id`

`String`

**Required.** The ID of the cached object that this call is reading a fragment of.

If the cache does not contain an object with the specified ID, `updateFragment` returns `null`.

###### `fragment`

`DocumentNode`

**Required.** A GraphQL document created with the `gql` template literal tag that includes the fragment to read.

If the document includes more than one fragment, you must also provide [`fragmentName`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#fragmentname) to indicate which to use.

###### `fragmentName`

`String`

The name of the fragment defined in the `fragment` document to use in the call.

You don't need to provide this value if the `fragment` document includes only one fragment.

###### `variables`

`Object`

A map of any GraphQL variable names and values required by `fragment`.

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's modified by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

###### `overwrite`

`Boolean`

If `true`, ignore existing cache data when calling `merge` functions, allowing incoming data to replace existing data, without warnings about data loss.

The default value is `false`.

### `updateFragment` update function

The update function of `updateFragment` takes a fragment's current cached value and returns the value that should replace it (or `undefined` if no change should be made).

The returned value is automatically passed to [`writeFragment`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#writefragment), which modifies the cached data.

Please note the `update` function has to calculate the new value in an immutable way. You can read more about immutable updates in the [React documentation](https://beta.reactjs.org/learn/updating-objects-in-state).

### Signature

```ts title=src/cache/core/cache.ts
public updateFragment<TData = unknown, TVariables = OperationVariables>(
  options: Cache.UpdateFragmentOptions<TData, TVariables>,
  update: (data: TData | null) => TData | null | void,
): TData | null
```

## [`batch`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch)

Executes multiple cache operations as a single batch, ensuring that watchers are only notified once after all operations complete. This is useful for improving performance when making multiple cache updates, as it prevents unnecessary re-renders or query refetches between individual operations.

The `batch` method supports both optimistic and non-optimistic updates, and provides fine-grained control over which cache layer receives the updates and when watchers are notified.

For usage instructions, see [Interacting with cached data: `cache.batch`](https://www.apollographql.com/docs/react/caching/cache-interaction.md#using-cachebatch).

### [Example](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-example)

JavaScript

```
 cache.batch({
   update(cache) {
     cache.writeQuery({
       query: GET_TODOS,
       data: { todos: updatedTodos },
     });
     cache.evict({ id: "Todo:123" });
   },
 });
```

### [Signature](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-signature)

TypeScript

```
batch<TUpdateResult>(
  options: Cache.BatchOptions<InMemoryCache, TUpdateResult>
): TUpdateResult
```

### [Parameters](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-parameters-options)\
`Cache.BatchOptions<InMemoryCache, TUpdateResult>`

Show/hide child attributes

###### [`onWatchUpdated`*(optional)*](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-parameters-options-onwatchupdated)

`(this: TCache, watch: Cache.WatchOptions, diff: Cache.DiffResult<any>, lastDiff?: Cache.DiffResult<any> | undefined) => any`

Optional callback invoked for each watcher affected by the batch operation.

Receives the watch options, the new diff result, and optionally the previous diff result.

Return `false` to prevent broadcasting to that specific watcher.

###### [`optimistic`*(optional)*](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-parameters-options-optimistic)

`string | boolean`

Controls how optimistic data is handled:

* `string`: Creates a new optimistic layer with this ID. Use `removeOptimistic` later to remove it.

* `true`: Updates the current top layer of the cache (including any optimistic data).

* `false`: Updates only the root (non-optimistic) cache data.

###### [`removeOptimistic`*(optional)*](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#batch-parameters-options-removeoptimistic)

`string`

If provided, removes the optimistic layer with this ID after the batch completes.

This is useful for atomically applying server data while removing a pending optimistic update, triggering at most one broadcast for both operations.

Note: this option is needed because calling `cache.removeOptimistic` during the transaction function may not be safe, since any modifications to cache layers may be discarded after the transaction finishes.

## `identify`

Returns the canonical ID for a specified cached object.

You can provide either an object or an object *reference* to this function:

* If you provide an object, `identify` returns the object's string-based ID (e.g., `Car:1`).
* If you provide a reference, `identify` return the reference's `__ref` ID string.

For usage instructions, see [Interacting with cached data: Identify cached entities](https://www.apollographql.com/docs/react/caching/cache-interaction/#obtaining-an-objects-cache-id).

Accepts the following parameters:

Name /Type
Description

###### `object`

`StoreObject` or `Reference`

**Required.** The cached object (or object reference) to obtain the canonical ID for.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
identify(object: StoreObject | Reference): string | undefined
```

## `modify`

Modifies one or more field values of a cached object. Must provide a **modifier function** for each field to modify. A modifier function takes a cached field's current value and returns the value that should replace it.

Returns `true` if the cache was modified successfully and `false` otherwise.

For usage instructions, see [Using `cache.modify`](https://www.apollographql.com/docs/react/caching/cache-interaction/#using-cachemodify).

Takes an `options` object as a parameter. Supported fields of this object are described below.

### Options

Name /Type
Description

###### `fields`

`Object`

**Required.** A map that specifies the modifier function to call for each modified field of the cached object.

See [Modifier function API](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#modifier-function-api) below.

###### `id`

`string`

The ID of the cached object to modify.

The default value is `ROOT_QUERY` (the ID of the root query singleton object).

###### `optimistic`

`Boolean`

If `true`, also modifies the optimistically cached values for included fields.

The default value is `false`.

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's modified by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

#### Modifier function API

A modifier function takes a cached field's current value and returns the value that should replace it, or the [`DELETE` sentinel object](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#delete) to delete the field entirely.

The first parameter passed to a modifier function is the current cached value of the field being modified.

The second parameter is a helper object that contains the following utilities:

Name /Type
Description

###### `fieldName`

`String`

The name of the field being modified.

###### `storeFieldName`

`String`

The full key for the field used internally, including serialized key arguments.

###### `readField`

`Function`

A helper function for reading other fields on the object passed to the modifier function as the first parameter.

###### `canRead`

`Function`

A helper function that returns `true` for non-normalized `StoreObject`s and non-dangling `Reference`s. This indicates that `readField(name, objOrRef)` has a chance of working.

Useful for filtering dangling references out of lists.

###### `isReference`

`Function`

A helper function that returns `true` if a particular object is a reference to a cached entity.

###### `DELETE`

`Object`

A sentinel object that you can return from a modifier function to indicate that the field should be deleted entirely.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
modify(options: Cache.ModifyOptions): boolean
```

## `gc`

Performs garbage collection of unreachable normalized objects in the cache:

```js
cache.gc();
```

Returns an array containing the IDs of all objects removed from the cache.

For usage instructions, see [`cache.gc`](https://www.apollographql.com/docs/react/caching/garbage-collection/#cachegc).

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
gc();
```

## `evict`

Either removes a normalized object from the cache or removes a specific field from a normalized object in the cache:

```js
cache.evict({ id: "my-object-id", fieldName: "myFieldName" });
```

Returns `true` if data was removed from the cache, `false` otherwise.

For usage instructions, see [`cache.evict`](https://www.apollographql.com/docs/react/caching/garbage-collection/#cacheevict).

Takes an `options` object as a parameter. Supported fields of this object are described below.

### Options

Name /Type
Description

###### `id`

`String`

The ID of the cached object to remove (or remove a field from).

The default value is `ROOT_QUERY`, which is the ID of the root query object.

###### `fieldName`

`String`

The name of the field to remove from the cached object.

Omit this option if you are removing the entire object.

###### `args`

`Record<string, any>`

If provided with `fieldName`, only instances of the field with the specified arguments are removed from the cache.

Otherwise, all instances of the field are removed for the cached object.

###### `broadcast`

`Boolean`

If `true`, automatically refresh all active queries that depend on at least one field that's removed by this call. If `false`, silences the broadcast of cache updates and prevents automatic query refresh.

The default value is `true`.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
evict(options: Cache.EvictOptions): boolean
```

## `extract`

Returns a serialized representation of the cache's current contents as a `NormalizedCacheObject`.

Accepts the following parameters:

Name /Type
Description

###### `optimistic`

`Boolean`

If `true`, optimistic data is included in the serialization.

The default value is `false`.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
extract(optimistic: boolean = false): NormalizedCacheObject
```

## `restore`

Restores the cache's state from a serialized `NormalizedCacheObject` (such as one returned by [`extract`](https://www.apollographql.com/docs/react/api/cache/InMemoryCache.md#extract)). This removes all existing data from the cache.

Returns the `InMemoryCache` instance it's called on.

Accepts the following parameters:

Name /Type
Description

###### `data`

`NormalizedCacheObject`

**Required.** The serialization to restore the cache from.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
restore(data: NormalizedCacheObject): this
```

## `makeVar`

Creates a reactive variable with an optional initial value:

```js
const cartItems = makeVar([]);
```

Returns the reactive variable function you use to read or modify the variable's value.

For usage instructions, see [Reactive variables](https://www.apollographql.com/docs/react/local-state/reactive-variables/).

Accepts the following parameters:

Name /Type
Description

###### `value`

Any

The reactive variable's initial value.

### Signature

```ts title=src/cache/inmemory/inMemoryCache.ts
makeVar<T>(value: T): ReactiveVar<T>
```
