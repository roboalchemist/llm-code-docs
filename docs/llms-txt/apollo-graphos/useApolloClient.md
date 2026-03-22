# Source: https://www.apollographql.com/docs/react/api/react/useApolloClient.md

# useApolloClient

## [`useApolloClient`](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient)

### [Example](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient-example)

JavaScript

```
 import { useApolloClient } from "@apollo/client/react";

 function SomeComponent() {
   const client = useApolloClient();
   // `client` is now set to the `ApolloClient` instance being used by the
   // application (that was configured using something like `ApolloProvider`)
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient-signature)

TypeScript

```
useApolloClient(
  override?: ApolloClient
): ApolloClient
```

[(src/react/hooks/useApolloClient.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/hooks/useApolloClient.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient-parameters)

Name / Type

Description

[`override`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient-parameters-override)\
`ApolloClient`

### [Result](https://www.apollographql.com/docs/react/api/react/useApolloClient.md#useapolloclient-result)

The \`ApolloClient\` instance being used by the application.

```
ApolloClient
```
