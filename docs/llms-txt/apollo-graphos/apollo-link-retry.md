# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md

# RetryLink

`RetryLink` is a non-terminating link that attempts to retry operations that fail due to network errors. It enables resilient GraphQL operations by automatically retrying failed requests with configurable delay and retry strategies.

`RetryLink` is particularly useful for handling unreliable network conditions where you would rather wait longer than explicitly fail an operation. It provides exponential backoff and jitters delays between attempts by default.

**note**

This link does not handle retries for GraphQL errors in the response. Use `ErrorLink` to retry an operation after a GraphQL error. For more information, see the [Error handling documentation](https://apollographql.com/docs/react/data/error-handling#on-graphql-errors).

TypeScript

```
 import { RetryLink } from "@apollo/client/link/retry";

 const link = new RetryLink();
```

## Constructor signature

```ts
constructor(
  options?: RetryLink.Options
): RetryLink
```

## Avoiding thundering herd

Starting with `initialDelay`, the delay of each subsequent retry is increased exponentially, meaning it's multiplied by 2 each time. For example, if `initialDelay` is 100, additional retries will occur after delays of 200, 400, 800, etc.

With the `jitter` option enabled, delays are randomized anywhere between 0ms (instant), and 2x the configured delay. This way you get the same result on average, but with random delays.

These two features are combined to help alleviate [the thundering herd problem](https://en.wikipedia.org/wiki/Thundering_herd_problem), by distributing load during major outages. Without these strategies, when your server comes back up it will be hit by all of your clients at once, possibly causing it to go down again.

## Custom strategies

Instead of the options object, you may pass a function for `delay` and/or `attempts`, which implement custom strategies for each. In both cases the function is given the same arguments (`attempt`, `operation`, `error`).

The `attempts` function should return a `boolean` (or a `Promise` which resolves to a `boolean`) indicating whether the response should be retried. If yes, the `delay` function is then called, and should return the number of milliseconds to delay by.

```ts
import { RetryLink } from "@apollo/client/link/retry";

const link = new RetryLink({
  attempts: (attempt, operation, error) => {
    return !!error && operation.operationName != "specialCase";
  },
  delay: (attempt, operation, error) => {
    return attempt * 1000 * Math.random();
  },
});
```

## Types

### [`RetryLink.AttemptsFunction`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#retrylink.attemptsfunction)

A function used to determine whether to retry the current operation.

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-signature)

TypeScript

```
AttemptsFunction(
  attempt: number,
  operation: ApolloLink.Operation,
  error: ErrorLike
): boolean | Promise<boolean>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters)

Name / Type

Description

[`attempt`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-attempt)\
`number`

The current attempt number

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation)\
`ApolloLink.Operation`

The current `ApolloLink.Operation` for the request

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.

[`error`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-error)\
`ErrorLike`

The error that triggered the retry attempt

Show/hide child attributes

###### [`message`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-error-message)

`string`

###### [`name`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-error-name)

`string`

###### [`stack`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsfunction-parameters-error-stack)

`string`

### [`RetryLink.AttemptsOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#retrylink.attemptsoptions)

Configuration options for the standard retry attempt strategy.

Properties

Name / Type

Description

###### [`max`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsoptions-max)

`number`

The max number of times to try a single operation before giving up.

Note that this INCLUDES the initial request as part of the count. E.g. `max` of 1 indicates no retrying should occur.

Pass `Infinity` for infinite retries.

###### [`retryIf`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#attemptsoptions-retryif)

`(error: ErrorLike, operation: ApolloLink.Operation) => boolean | Promise<boolean>`

Predicate function that determines whether a particular error should trigger a retry.

For example, you may want to not retry 4xx class HTTP errors.

### [`RetryLink.DelayFunction`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#retrylink.delayfunction)

A function used to determine the delay for a retry attempt.

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-signature)

TypeScript

```
DelayFunction(
  attempt: number,
  operation: ApolloLink.Operation,
  error: ErrorLike
): number
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters)

Name / Type

Description

[`attempt`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-attempt)\
`number`

The current attempt number

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation)\
`ApolloLink.Operation`

The current `ApolloLink.Operation` for the request

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.

[`error`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-error)\
`ErrorLike`

The error that triggered the retry attempt

Show/hide child attributes

###### [`message`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-error-message)

`string`

###### [`name`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-error-name)

`string`

###### [`stack`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayfunction-parameters-error-stack)

`string`

### [`RetryLink.DelayOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#retrylink.delayoptions)

Configuration options for the standard retry delay strategy.

Properties

Name / Type

Description

###### [`initial`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayoptions-initial)

`number`

The number of milliseconds to wait before attempting the first retry.

Delays will increase exponentially for each attempt. E.g. if this is set to 100, subsequent retries will be delayed by 200, 400, 800, etc, until they reach the maximum delay.

Note that if jittering is enabled, this is the average delay.

###### [`jitter`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayoptions-jitter)

`boolean`

Whether delays between attempts should be randomized.

This helps avoid [thundering herd](https://en.wikipedia.org/wiki/Thundering_herd_problem) type situations by better distributing load during major outages. Without these strategies, when your server comes back up it will be hit by all of your clients at once, possibly causing it to go down again.

###### [`max`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#delayoptions-max)

`number`

The maximum number of milliseconds that the link should wait for any retry.

### [`RetryLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#retrylink.options)

Options provided to the `RetryLink` constructor.

Properties

Name / Type

Description

###### [`attempts`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#options-attempts)

`RetryLink.AttemptsOptions | RetryLink.AttemptsFunction`

Configuration for the retry strategy to use, or a custom retry strategy.

###### [`delay`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-retry.md#options-delay)

`RetryLink.DelayOptions | RetryLink.DelayFunction`

Configuration for the delay strategy to use, or a custom delay strategy.
