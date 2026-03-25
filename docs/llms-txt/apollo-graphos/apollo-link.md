# Source: https://www.apollographql.com/docs/react/api/link/apollo-link.md

# ApolloLink

The base class for all links in Apollo Client. A link represents either a self-contained modification to a GraphQL operation or a side effect (such as logging).

Links enable you to customize Apollo Client's request flow by composing together different pieces of functionality into a chain of links. Each link represents a specific capability, such as adding authentication headers, retrying failed requests, batching operations, or sending requests to a GraphQL server.

Every link must define a request handler via its constructor or by extending this class and implementing the `request` method.

TypeScript

```
 import { ApolloLink } from "@apollo/client";

 const link = new ApolloLink((operation, forward) => {
   console.log("Operation:", operation.operationName);
   return forward(operation);
 });
```

## Constructor signature

```ts
constructor(
  request?: ApolloLink.RequestHandler
): ApolloLink
```

## Static methods

### [`ApolloLink.from`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.from)

Composes multiple links into a single composed link that executes each provided link in serial order.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#from-example)

TypeScript

```
 import { from, HttpLink, ApolloLink } from "@apollo/client";
 import { RetryLink } from "@apollo/client/link/retry";
 import MyAuthLink from "../auth";

 const link = ApolloLink.from([
   new RetryLink(),
   new MyAuthLink(),
   new HttpLink({ uri: "http://localhost:4000/graphql" }),
 ]);
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#from-signature)

TypeScript

```
from(
  links: ApolloLink[]
): ApolloLink
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#from-parameters)

Name / Type

Description

[`links`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#from-parameters-links)\
`ApolloLink[]`

An array of `ApolloLink` instances or request handlers that are executed in serial order.

### [`ApolloLink.split`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.split)

Creates a link that conditionally routes a request to different links.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-example)

TypeScript

```
 import { ApolloLink, HttpLink } from "@apollo/client";

 const link = ApolloLink.split(
   (operation) => operation.getContext().version === 1,
   new HttpLink({ uri: "http://localhost:4000/v1/graphql" }),
   new HttpLink({ uri: "http://localhost:4000/v2/graphql" })
 );
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-signature)

TypeScript

```
split(
  test: (op: ApolloLink.Operation) => boolean,
  left: ApolloLink,
  right?: ApolloLink
): ApolloLink
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters)

Name / Type

Description

[`test`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-test)\
`(op: ApolloLink.Operation) => boolean`

A predicate function that receives the current `operation` and returns a boolean indicating which link to execute. Returning `true` executes the `left` link. Returning `false` executes the `right` link.

[`left`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-left)\
`ApolloLink`

The link that executes when the `test` function returns `true`.

[`right`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-right)\
`ApolloLink`

The link that executes when the `test` function returns `false`. If the `right` link is not provided, the request is forwarded to the next link in the chain.

### [`ApolloLink.execute`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.execute)

Executes a GraphQL request against a link. The `execute` function begins the request by calling the request handler of the link.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-example)

TypeScript

```
 const observable = ApolloLink.execute(link, { query, variables }, { client });

 observable.subscribe({
   next(value) {
     console.log("Received", value);
   },
   error(error) {
     console.error("Oops got error", error);
   },
   complete() {
     console.log("Request complete");
   },
 });
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-signature)

TypeScript

```
execute(
  link: ApolloLink,
  request: ApolloLink.Request,
  context: ApolloLink.ExecuteContext
): Observable<ApolloLink.Result>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters)

Name / Type

Description

[`link`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-link)\
`ApolloLink`

The `ApolloLink` instance to execute the request.

[`request`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-request)\
`ApolloLink.Request`

The GraphQL request details, such as the `query` and `variables`.

Show/hide child attributes

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-request-context)

`DefaultContext`

Context provided to the link chain. Context is not sent to the server and is used to communicate additional metadata from a request to individual links in the link chain.

###### [`extensions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-request-extensions)

`Record<string, any>`

A map of extensions that will be sent with the GraphQL request to the server.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-request-query)

`DocumentNode`

The parsed GraphQL document that will be sent with the GraphQL request to the server.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-request-variables)

`OperationVariables`

The variables provided for the query.

[`context`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-context)\
`ApolloLink.ExecuteContext`

The execution context for the request, such as the `client` making the request.

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#execute-parameters-context-client)

`ApolloClient`

The Apollo Client instance that executed the GraphQL request.

### [`ApolloLink.empty`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.empty)

Creates a link that completes immediately and does not emit a result.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#empty-example)

TypeScript

```
 const link = ApolloLink.empty();
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#empty-signature)

TypeScript

```
empty(): ApolloLink
```

### [`ApolloLink.concat`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.concat)

> ⚠️ Deprecated
>
> Use `ApolloLink.from` instead. `ApolloLink.concat` will be removed in a future major version.

Combines multiple links into a single composed link.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-example)

TypeScript

```
 const link = ApolloLink.concat(firstLink, secondLink, thirdLink);
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-signature)

TypeScript

```
concat(
  links: ApolloLink[]
): ApolloLink
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-parameters)

Name / Type

Description

[`links`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-parameters-links)\
`ApolloLink[]`

The links to concatenate into a single link. Each link will execute in serial order.

## Instance methods

### [`concat`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat)

Combines the link with other links into a single composed link.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-example)

TypeScript

```
 import { ApolloLink, HttpLink } from "@apollo/client";

 const previousLink = new ApolloLink((operation, forward) => {
   // Handle the request

   return forward(operation);
 });

 const link = previousLink.concat(
   link1,
   link2,
   new HttpLink({ uri: "http://localhost:4000/graphql" })
 );
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-signature)

TypeScript

```
concat(
  links: ApolloLink[]
): ApolloLink
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-parameters)

Name / Type

Description

[`links`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#concat-parameters-links)\
`ApolloLink[]`

### [`split`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split)

Concatenates a link that conditionally routes a request to different links.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-example)

TypeScript

```
 import { ApolloLink, HttpLink } from "@apollo/client";

 const previousLink = new ApolloLink((operation, forward) => {
   // Handle the request

   return forward(operation);
 });

 const link = previousLink.split(
   (operation) => operation.getContext().version === 1,
   new HttpLink({ uri: "http://localhost:4000/v1/graphql" }),
   new HttpLink({ uri: "http://localhost:4000/v2/graphql" })
 );
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-signature)

TypeScript

```
split(
  test: (op: ApolloLink.Operation) => boolean,
  left: ApolloLink,
  right?: ApolloLink
): ApolloLink
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters)

Name / Type

Description

[`test`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-test)\
`(op: ApolloLink.Operation) => boolean`

A predicate function that receives the current `operation` and returns a boolean indicating which link to execute. Returning `true` executes the `left` link. Returning `false` executes the `right` link.

[`left`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-left)\
`ApolloLink`

The link that executes when the `test` function returns `true`.

[`right`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#split-parameters-right)\
`ApolloLink`

The link that executes when the `test` function returns `false`. If the `right` link is not provided, the request is forwarded to the next link in the chain.

## Types

### [`ApolloLink.ExecuteContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.executecontext)

Context provided for link execution, such as the client executing the request. It is separate from the request operation context.

Properties

Name / Type

Description

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#executecontext-client)

`ApolloClient`

The Apollo Client instance that executed the GraphQL request.

### [`ApolloLink.ForwardFunction`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.forwardfunction)

A function that when called will execute the next link in the link chain.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-example)

TypeScript

```
 const link = new ApolloLink((operation, forward) => {
   // process the request

   // Call `forward` to execute the next link in the chain
   return forward(operation);
 });
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-signature)

TypeScript

```
ForwardFunction(
  operation: ApolloLink.Operation
): Observable<ApolloLink.Result>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters)

Name / Type

Description

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation)\
`ApolloLink.Operation`

The current `ApolloLink.Operation` object for the request.

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#forwardfunction-parameters-operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.

### [`ApolloLink.Request`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.request)

The input object provided to `ApolloLink.execute` to send a GraphQL request through the link chain.

Properties

Name / Type

Description

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#request-context)

`DefaultContext`

Context provided to the link chain. Context is not sent to the server and is used to communicate additional metadata from a request to individual links in the link chain.

###### [`extensions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#request-extensions)

`Record<string, any>`

A map of extensions that will be sent with the GraphQL request to the server.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#request-query)

`DocumentNode`

The parsed GraphQL document that will be sent with the GraphQL request to the server.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#request-variables)

`OperationVariables`

The variables provided for the query.

### [`ApolloLink.RequestHandler`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.requesthandler)

A request handler is responsible for performing some logic and executing the request, either by [forwarding](https://apollographql.com/docs/react/api/link/introduction#the-request-handler) the operation to the next link in the chain, or sending the operation to the destination that executes it, such as a GraphQL server.

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-signature)

TypeScript

```
RequestHandler(
  operation: ApolloLink.Operation,
  forward: ApolloLink.ForwardFunction
): Observable<ApolloLink.Result>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters)

Name / Type

Description

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation)\
`ApolloLink.Operation`

The `Operation` object that provides information about the currently executed GraphQL request.

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.

[`forward`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#requesthandler-parameters-forward)\
`ApolloLink.ForwardFunction`

A function that is called to execute the next link in the chain.

### [`ApolloLink.Operation`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.operation)

The currently executed operation object provided to an `ApolloLink.RequestHandler` for each link in the link chain.

Properties

Name / Type

Description

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.

### [`ApolloLink.OperationContext`](https://www.apollographql.com/docs/react/api/link/apollo-link.md#apollolink.operationcontext)

The `context` object that can be read and modified by links using the `operation.getContext()` and `operation.setContext()` methods.

Properties

(Warning: some properties might be missing from the table due to complex inheritance!)

Name / Type

Description

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operationcontext-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

###### [`queryDeduplication`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link.md#operationcontext-querydeduplication)

`boolean`

Indicates whether `queryDeduplication` was enabled for the request.
