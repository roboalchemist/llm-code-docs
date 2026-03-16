# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md

# SchemaLink

`SchemaLink` is a terminating link that executes GraphQL operations against a local GraphQL schema instead of making network requests. This is commonly used for server-side rendering (SSR) and mocking data.

**note**

While `SchemaLink` can provide GraphQL results on the client, the GraphQL execution layer is [quite large](https://bundlephobia.com/result?p=graphql) for practical client-side use. For client-side state management, consider Apollo Client's [local state management](https://apollographql.com/docs/react/local-state/local-state-management/) functionality instead, which integrates with the Apollo Client cache.

TypeScript

```
 import { SchemaLink } from "@apollo/client/link/schema";
 import schema from "./path/to/your/schema";

 const link = new SchemaLink({ schema });
```

## Constructor signature

```ts
constructor(
  options: SchemaLink.Options
): SchemaLink
```

## Usage examples

### Server Side Rendering

When performing SSR *on the same server*, you can use this library to avoid making network calls.

```js
import { ApolloClient, InMemoryCache } from "@apollo/client";
import { SchemaLink } from "@apollo/client/link/schema";

import schema from "./path/to/your/schema";

const graphqlClient = new ApolloClient({
  cache: new InMemoryCache(),
  ssrMode: true,
  link: new SchemaLink({ schema }),
});
```

### Mocking

For more detailed information about mocking, refer to the [graphql-tools documentation](https://www.graphql-tools.com/docs/graphql-tools/mocking).

```js
import { ApolloClient, InMemoryCache } from '@apollo/client';
import { SchemaLink } from '@apollo/client/link/schema';
import { makeExecutableSchema, addMockFunctionsToSchema } from 'graphql-tools';

const typeDefs = `
  Query {
  ...
  }
`;

const mocks = {
  Query: () => ...,
  Mutation: () => ...
};

const schema = makeExecutableSchema({ typeDefs });
const schemaWithMocks = addMockFunctionsToSchema({
  schema,
  mocks
});

const apolloCache = new InMemoryCache(window.__APOLLO_STATE__);

const graphqlClient = new ApolloClient({
  cache: apolloCache,
  link: new SchemaLink({ schema: schemaWithMocks })
});
```

## Types

### [`SchemaLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#schemalink.options)

Options for configuring the `SchemaLink`.

Properties

Name / Type

Description

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#options-context)

`SchemaLink.ResolverContext | SchemaLink.ResolverContextFunction`

Context object or function that returns the context object to provide to resolvers. The context is passed as the third parameter to all GraphQL resolvers.

* If a static object is provided, the same context will be used for all operations

* If a function is provided, the function is called for each operation to generate operation-specific context

###### [`rootValue`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#options-rootvalue)

`any`

The root value passed to root-level resolvers. It's typically not used in most schemas but can be useful for certain advanced patterns.

###### [`schema`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#options-schema)

`GraphQLSchema`

An executable GraphQL schema to use for operation execution.

Read more...

This should be a complete, executable GraphQL schema created using tools like `makeExecutableSchema` from `@graphql-tools/schema` or `buildSchema` from `graphql`.

TypeScript

```
 import { makeExecutableSchema } from "@graphql-tools/schema";

 const schema = makeExecutableSchema({
   typeDefs,
   resolvers,
 });

 const link = new SchemaLink({ schema });
```

###### [`validate`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#options-validate)

`boolean`

Whether to validate incoming queries against the schema before execution.

When enabled, queries will be validated against the schema before execution, and validation errors will be returned in the result's `errors` array, just like a remote GraphQL server would.

This is useful for testing and development to catch query errors early, but may add overhead in production environments.

### `SchemaLink.ResolverContext`

The resolver context object passed to GraphQL resolvers.

This context object is passed as the third parameter to GraphQL resolvers and typically contains data-fetching connectors, authentication information, and other request-specific data.

#### Signature

```ts
type ResolverContext = Record<string, any>;
```

### [`SchemaLink.ResolverContextFunction`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#schemalink.resolvercontextfunction)

A function that returns the resolver context for a given operation.

This function is called for each operation and allows you to create operation-specific context. This is useful when you need to include information from the operation (like headers, variables, etc.) in the resolver context.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-example)

TypeScript

```
 const link = new SchemaLink({
   schema,
   context: (operation) => {
     return {
       userId: operation.getContext().userId,
       dataSources: {
         userAPI: new UserAPI(),
       },
     };
   },
 });
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-signature)

TypeScript

```
ResolverContextFunction(
  operation: ApolloLink.Operation
): SchemaLink.ResolverContext | PromiseLike<SchemaLink.ResolverContext>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters)

Name / Type

Description

[`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation)\
`ApolloLink.Operation`

The Apollo Link operation

Show/hide child attributes

###### [`client`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-client)

`ApolloClient`

The Apollo Client instance executing the request.

###### [`extensions`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-extensions)

`Record<string, any>`

A map that stores extensions data to be sent to the server.

###### [`getContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-getcontext)

`() => Readonly<ApolloLink.OperationContext>`

A function that gets the current context of the request. This can be used by links to determine which actions to perform. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context)

###### [`operationName`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-operationname)

`string | undefined`

The string name of the GraphQL operation. If it is anonymous, `operationName` will be `undefined`.

###### [`operationType`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-operationtype)

`OperationTypeNode`

The type of the GraphQL operation, such as query or mutation.

###### [`query`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-query)

`DocumentNode`

A `DocumentNode` that describes the operation taking place.

###### [`setContext`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-setcontext)

`{ (context: Partial<ApolloLink.OperationContext>): void; (updateContext: (previousContext: Readonly<ApolloLink.OperationContext>) => Partial<ApolloLink.OperationContext>): void; }`

A function that takes either a new context object, or a function which takes in the previous context and returns a new one. See [managing context](https://apollographql.com/docs/react/api/link/introduction#managing-context).

###### [`variables`](https://www.apollographql.com/docs/react/api/link/apollo-link-schema.md#resolvercontextfunction-parameters-operation-variables)

`OperationVariables`

A map of GraphQL variables being sent with the operation.
