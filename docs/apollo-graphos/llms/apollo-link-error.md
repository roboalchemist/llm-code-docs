# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-error.md

# ErrorLink

Use the `ErrorLink` to perform custom logic when a [GraphQL or network error](https://apollographql.com/docs/react/data/error-handling) occurs.

This link is used after the GraphQL operation completes and execution is moving back up your [link chain](https://apollographql.com/docs/react/api/link/introduction#handling-a-response). The `errorHandler` function should not return a value unless you want to [retry the operation](https://apollographql.com/docs/react/data/error-handling#retrying-operations).

For more information on the types of errors that might be encountered, see the guide on [error handling](https://apollographql.com/docs/react/data/error-handling).

TypeScript

```
 import { ErrorLink } from "@apollo/client/link/error";
 import {
   CombinedGraphQLErrors,
   CombinedProtocolErrors,
 } from "@apollo/client/errors";

 // Log any GraphQL errors, protocol errors, or network error that occurred
 const errorLink = new ErrorLink(({ error, operation }) => {
   if (CombinedGraphQLErrors.is(error)) {
     error.errors.forEach(({ message, locations, path }) =>
       console.log(
         `[GraphQL error]: Message: ${message}, Location: ${locations}, Path: ${path}`
       )
     );
   } else if (CombinedProtocolErrors.is(error)) {
     error.errors.forEach(({ message, extensions }) =>
       console.log(
         `[Protocol error]: Message: ${message}, Extensions: ${JSON.stringify(
           extensions
         )}`
       )
     );
   } else {
     console.error(`[Network error]: ${error}`);
   }
 });
```

## Constructor signature

```ts
constructor(
  errorHandler: ErrorLink.ErrorHandler
): ErrorLink
```

## Types

### [`ErrorLink.ErrorHandler`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorlink.errorhandler)

Callback that is called by `ErrorLink` when an error occurs from a downstream link in link chain.

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandler-signature)

TypeScript

```
ErrorHandler(
  options: ErrorHandlerOptions
): Observable<ApolloLink.Result> | void
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandler-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandler-parameters-options)\
`ErrorHandlerOptions`

The options object provided by `ErrorLink` to the error handler when an error occurs.

### [`ErrorLink.ErrorHandlerOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorlink.errorhandleroptions)

The object provided to the `ErrorHandler` callback function.

Properties

Name / Type

Description

###### [`error`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandleroptions-error)

`ErrorLike`

The error that occurred during the operation execution. This can be a `CombinedGraphQLErrors` instance (for GraphQL errors) or another error type (for network errors).

Use `CombinedGraphQLErrors.is(error)` to check if it's a GraphQL error with an `errors` array.

###### [`forward`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandleroptions-forward)

`ApolloLink.ForwardFunction`

A function that calls the next link in the link chain. Calling `return forward(operation)` in your `ErrorLink` callback [retries the operation](https://www.apollographql.com/data/error-handling#retrying-operations), returning a new observable for the upstream link to subscribe to.

###### [`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandleroptions-operation)

`ApolloLink.Operation`

The details of the GraphQL operation that produced an error.

###### [`result`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-error.md#errorhandleroptions-result)

`ApolloLink.Result`

The raw GraphQL result from the server (if available), which may include partial data alongside errors.
