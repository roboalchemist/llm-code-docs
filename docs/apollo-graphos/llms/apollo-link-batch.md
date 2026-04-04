# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md

# BatchLink

`BatchLink` is a non-terminating link that provides the core batching functionality for grouping multiple GraphQL operations into batches based on configurable timing and key-based grouping strategies. It serves as a base link to `BatchHttpLink`.

**note**

You will not generally use `BatchLink` on your own unless you need to provide batching capabilities to third-party terminating links. Prefer using `BatchHttpLink` to batch GraphQL operations over HTTP.

TypeScript

```
 import { BatchLink } from "@apollo/client/link/batch";

 const link = new BatchLink({
   batchInterval: 20,
   batchMax: 5,
   batchHandler: (operations, forwards) => {
     // Custom logic to process batch of operations
     return handleBatch(operations, forwards);
   },
 });
```

## Constructor signature

```ts
constructor(
  options?: BatchLink.Options
): BatchLink
```

## Types

### [`BatchLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#batchlink.options)

Configuration options for creating a `BatchLink` instance.

Properties

Name / Type

Description

###### [`batchDebounce`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#options-batchdebounce)

`boolean`

"batchInterval" is a throttling behavior by default, if you instead wish to debounce outbound requests, set "batchDebounce" to true. More useful for mutations than queries.

###### [`batchHandler`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#options-batchhandler)

`BatchLink.BatchHandler`

The handler that executes a batch of operations.

Read more...

This function receives an array of operations and their corresponding forward functions, and should return an Observable that emits the results for all operations in the batch.

###### [`batchInterval`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#options-batchinterval)

`number`

The interval at which to batch, in milliseconds.

###### [`batchKey`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#options-batchkey)

`(operation: ApolloLink.Operation) => string`

Creates the key for a batch

###### [`batchMax`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch.md#options-batchmax)

`number`

The maximum number of operations to include in a single batch.
