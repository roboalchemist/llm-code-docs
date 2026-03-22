# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md

# BaseHttpLink

`BaseHttpLink` is a terminating link that sends a GraphQL operation to a remote endpoint over HTTP. It serves as a base link to `HttpLink`.

`BaseHttpLink` supports both POST and GET requests, and you can configure HTTP options on a per-operation basis. You can use these options for authentication, persisted queries, dynamic URIs, and other granular updates.

**note**

Prefer using `HttpLink` over `BaseHttpLink`. Use `BaseHttpLink` when you need to disable client awareness features and would like to tree-shake the implementation of `ClientAwarenessLink` out of your app bundle.

TypeScript

```
 import { BaseHttpLink } from "@apollo/client/link/http";

 const link = new BaseHttpLink({
   uri: "http://localhost:4000/graphql",
   headers: {
     authorization: `Bearer ${token}`,
   },
 });
```

## Constructor signature

```ts
constructor(
  options: BaseHttpLink.Options = {}
): BaseHttpLink
```

## Usage

See the [`HttpLink` documentation](https://www.apollographql.com/docs/react/api/link/apollo-link-http) for more information on
how to use `BaseHttpLink`.

## Types

### [`BaseHttpLink.ContextOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#basehttplink.contextoptions)

Options passed to `BaseHttpLink` through [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Previous non-terminating links in the link chain also can set these values to customize the behavior of `BaseHttpLink` for each operation.

**note**

Some of these values can also be provided to the `HttpLink` constructor. If a value is provided to both, the value in `context` takes precedence.

Properties

Name / Type

Description

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#contextoptions-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#contextoptions-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#contextoptions-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

###### [`http`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#contextoptions-http)

`BaseHttpLink.HttpOptions`

An object that configures advanced functionality, such as support for persisted queries.

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#contextoptions-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.

### [`BaseHttpLink.HttpOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#basehttplink.httpoptions)

Options passed to `BaseHttpLink` through the `http` property of a request context.

Properties

Name / Type

Description

###### [`accept`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#httpoptions-accept)

`string[]`

A list of additional `accept` headers to include in the request, as defined in [https://datatracker.ietf.org/doc/html/rfc7231#section-5.3.2](https://datatracker.ietf.org/doc/html/rfc7231#section-5.3.2)

JSON

```
 ["application/custom+json;q=1.0"]
```

###### [`includeExtensions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#httpoptions-includeextensions)

`boolean`

If `true`, includes the `extensions` field in operations sent to your GraphQL endpoint.

###### [`includeQuery`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#httpoptions-includequery)

`boolean`

If `false`, the GraphQL query string is not included in the request. Set this option if you're sending a request that uses a [persisted query](https://www.apollographql.com/docs/react/api/link/persisted-queries.md).

###### [`preserveHeaderCase`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#httpoptions-preserveheadercase)

`boolean`

If `true`, header names won't be automatically normalized to lowercase. This allows for non-http-spec-compliant servers that might expect capitalized header names.

### [`BaseHttpLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#basehttplink.options)

Options provided to the `BaseHttpLink` constructor.

**note**

Some of these options are also available to override in [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Context options override the options passed to the constructor. Treat these options as default values that are used when the request context does not override the value.

Properties

Name / Type

Description

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`fetch`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-fetch)

`typeof fetch`

A function to use instead of calling the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) directly when sending HTTP requests to your GraphQL endpoint. The function must conform to the signature of `fetch`.

By default, the Fetch API is used unless it isn't available in your runtime environment.

See [Customizing `fetch`](https://apollographql.com/docs/react/api/link/introduction#customizing-fetch).

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

###### [`includeExtensions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-includeextensions)

`boolean`

If `true`, includes the `extensions` field in operations sent to your GraphQL endpoint.

###### [`includeUnusedVariables`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-includeunusedvariables)

`boolean`

If `true`, unused variables from the operation will not be stripped from the request and will instead be sent to the GraphQL endpoint.

Read more...

Unused variables are likely to trigger server-side validation errors, per [https://spec.graphql.org/draft/#sec-All-Variables-Used](https://spec.graphql.org/draft/#sec-All-Variables-Used). `includeUnusedVariables` can be useful if your server deviates from the GraphQL specification by not strictly enforcing that rule.

###### [`preserveHeaderCase`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-preserveheadercase)

`boolean`

If `true`, header names won't be automatically normalized to lowercase. This allows for non-http-spec-compliant servers that might expect capitalized header names.

###### [`print`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-print)

`BaseHttpLink.Printer`

A function to use when transforming a GraphQL document into a string. It accepts an `ASTNode` (typically a `DocumentNode`) and the original `print` function as arguments, and is expected to return a string. This option enables you to, for example, use `stripIgnoredCharacters` to remove whitespace from queries.

By default the [GraphQL `print` function](https://graphql.org/graphql-js/language/#print) is used.

TypeScript

```
 import { stripIgnoredCharacters } from "graphql";

 const httpLink = new HttpLink({
   uri: "/graphql",
   print: (ast, originalPrint) => stripIgnoredCharacters(originalPrint(ast)),
 });
```

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.

###### [`useGETForQueries`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-base-http.md#options-usegetforqueries)

`boolean`

If `true`, the link uses an HTTP `GET` request when sending query operations to your GraphQL endpoint. Mutation operations continue to use `POST` requests. If you want all operations to use `GET` requests, set `fetchOptions.method` instead.
