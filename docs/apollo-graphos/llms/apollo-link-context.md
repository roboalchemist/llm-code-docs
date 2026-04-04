# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-context.md

# SetContextLink

`SetContextLink` is a non-terminating link that allows you to modify the context of GraphQL operations before they're passed to the next link in the chain. This is commonly used for authentication, adding headers, and other request-time configuration.

TypeScript

```
 import { SetContextLink } from "@apollo/client/link/context";

 const link = new SetContextLink((prevContext, operation) => {
   return {
     credentials: "include",
     // ...
   };
 });
```

## Constructor signature

```ts
constructor(
  setter: SetContextLink.ContextSetter
): SetContextLink
```

## Usage examples

### Authentication

The most common use case is adding authentication headers to requests:

```ts
const authLink = new SetContextLink((prevContext, operation) => {
  const token = getAuthToken();

  return {
    headers: {
      ...prevContext.headers,
      authorization: token ? `Bearer ${token}` : "",
    },
  };
});
```

### Asynchronous token lookup

You can also perform asynchronous operations to fetch tokens or other data:

```ts
const asyncAuthLink = new SetContextLink(async (prevContext, operation) => {
  const token = await fetchAuthToken();

  return {
    headers: {
      ...prevContext.headers,
      authorization: `Bearer ${token}`,
    },
  };
});
```

## Caching lookups

Typically async actions can be expensive and may not need to be called for every request, especially when a lot of request are happening at once. You can setup your own caching and invalidation outside of the link, to make it faster but still flexible.

Take for example a user auth token being found, cached, then removed on a 401 response:

```js
import { ServerError } from "@apollo/client";
import { SetContextLink } from "@apollo/client/link/context";
import { ErrorLink } from "@apollo/client/link/error";

// cached storage for the user token
let token;
const withToken = new SetContextLink(async (prevContext, operation) => {
  // if you have a cached value, return it immediately
  if (token) {
    return {
      headers: {
        ...prevContext.headers,
        authorization: `Bearer ${token}`,
      },
    };
  }

  const userToken = await AsyncTokenLookup();
  token = userToken;
  return {
    headers: {
      ...prevContext.headers,
      authorization: `Bearer ${token}`,
    },
  };
});

const resetToken = new ErrorLink(({ error }) => {
  if (ServerError.is(error) && error.statusCode === 401) {
    // remove cached token on 401 from the server
    token = null;
  }
});

const authFlowLink = withToken.concat(resetToken);
```

## Types

### [`SetContextLink.ContextSetter`](https://www.apollographql.com/docs/react/api/link/apollo-link-context.md#setcontextlink.contextsetter)

A function that returns an updated context object for an Apollo Link operation.

The context setter function is called for each operation and allows you to modify the operation's context before it's passed to the next link in the chain. The returned context object is shallowly merged with the previous context object.

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-context.md#contextsetter-signature)

TypeScript

```
ContextSetter(
  prevContext: Readonly<ApolloLink.OperationContext>,
  operation: SetContextLink.SetContextOperation
): Promise<Partial<ApolloLink.OperationContext>> | Partial<ApolloLink.OperationContext>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-context.md#contextsetter-parameters)

Name / Type

Description

[`prevContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-context.md#contextsetter-parameters-prevcontext)\
`Readonly<ApolloLink.OperationContext>`

The previous context of the operation (e.g. the value of `operation.getContext()`)

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-context.md#contextsetter-parameters-operation)\
`SetContextLink.SetContextOperation`

The GraphQL operation being executed, without the `getContext` and `setContext` methods

### `SetContextLink.SetContextOperation`

An `ApolloLink.Operation` object without the `getContext` and `setContext` methods. This prevents context setters from directly manipulating the context during the setter function execution.

#### Signature

```ts
type SetContextOperation = Omit<
  ApolloLink.Operation,
  "getContext" | "setContext"
>;
```
