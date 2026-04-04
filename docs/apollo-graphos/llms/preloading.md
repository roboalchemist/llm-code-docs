# Source: https://www.apollographql.com/docs/react/api/react/preloading.md

# createQueryPreloader

## [`createQueryPreloader`](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader)

A higher order function that returns a `preloadQuery` function which can be used to begin loading a query with the given `client`. This is useful when you want to start loading a query as early as possible outside of a React component.

> Refer to the [Suspense - Initiating queries outside React](https://www.apollographql.com/docs/react/data/suspense.md#initiating-queries-outside-react) section for a more in-depth overview.

### [Example](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader-example)

JavaScript

```
 const preloadQuery = createQueryPreloader(client);
```

### [Signature](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader-signature)

TypeScript

```
createQueryPreloader(
  client: ApolloClient
): PreloadQueryFunction
```

[(src/react/query-preloader/createQueryPreloader.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/query-preloader/createQueryPreloader.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader-parameters)

Name / Type

Description

[`client`](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader-parameters-client)\
`ApolloClient`

The `ApolloClient` instance that will be used to load queries from the returned `preloadQuery` function.

### [Result](https://www.apollographql.com/docs/react/api/react/preloading.md#createquerypreloader-result)

The \`preloadQuery\` function.

```
PreloadQueryFunction
```
