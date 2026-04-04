# Source: https://www.apollographql.com/docs/react/networking/basic-http-networking.md

# Basic HTTP networking

Apollo Client has built-in support for communicating with a GraphQL server over HTTP with `HttpLink`.
To set up this communication, provide an `HttpLink` instance as the `link` option to the `ApolloClient` constructor:

```js
import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "https://api.example.com",
  }),
});
```

If you provide this parameter, Apollo Client sends all GraphQL operations (queries and mutations) to the specified URL over HTTP.

## Including credentials in requests

`HttpLink` can include user credentials (basic auth, cookies, etc.) in the HTTP requests it makes to a GraphQL server. By default, credentials are included only if the server is hosted at the same origin as the application using Apollo Client. You can adjust this behavior by providing a value for the `credentials` option to the `HttpLink` constructor:

```js
import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "https://api.example.com",
    // Enable sending cookies over cross-origin requests
    credentials: "include",
  }),
});
```

The following values for `credentials` are supported:

| Option        | Description                                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `same-origin` | Send user credentials (cookies, basic http auth, etc.) if the server's URL is on the same origin as the requesting client. This is the default value. |
| `omit`        | Never send or receive credentials.                                                                                                                    |
| `include`     | Always send user credentials (cookies, basic http auth, etc.), even for cross-origin requests.                                                        |

For more information, see [`Request.credentials`](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials).

## Customizing request headers

You can specify the names and values of custom headers to include in every HTTP request to a GraphQL server. To do so, provide the `headers` option to the `HttpLink` constructor, like so:

```js
import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "https://api.example.com",
    headers: {
      authorization: localStorage.getItem("token"),
      "client-name": "WidgetX Ecom [web]",
      "client-version": "1.0.0",
    },
  }),
});
```

## API

### [`HttpLink.Options`](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#httplink.options)

Options provided to the `HttpLink` constructor.

**note**

Some of these options are also available to override in [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Context options override the options passed to the constructor. Treat these options as default values that are used when the request context does not override the value.

Properties

Name / Type

Description

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

Other

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

###### [`enhancedClientAwareness`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-enhancedclientawareness)

`ClientAwarenessLink.EnhancedClientAwarenessOptions`

Configures the "enhanced client awareness" feature. This feature allows you to identify the version of the Apollo Client library used in your application in Apollo Studio (and other monitoring or analytics tools) by adding information about the Apollo Client library to outgoing requests.

###### [`fetch`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-fetch)

`typeof fetch`

A function to use instead of calling the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) directly when sending HTTP requests to your GraphQL endpoint. The function must conform to the signature of `fetch`.

By default, the Fetch API is used unless it isn't available in your runtime environment.

See [Customizing `fetch`](https://apollographql.com/docs/react/api/link/introduction#customizing-fetch).

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

###### [`includeExtensions`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-includeextensions)

`boolean`

If `true`, includes the `extensions` field in operations sent to your GraphQL endpoint.

###### [`includeUnusedVariables`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-includeunusedvariables)

`boolean`

If `true`, unused variables from the operation will not be stripped from the request and will instead be sent to the GraphQL endpoint.

Read more...

Unused variables are likely to trigger server-side validation errors, per [https://spec.graphql.org/draft/#sec-All-Variables-Used](https://spec.graphql.org/draft/#sec-All-Variables-Used). `includeUnusedVariables` can be useful if your server deviates from the GraphQL specification by not strictly enforcing that rule.

###### [`preserveHeaderCase`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-preserveheadercase)

`boolean`

If `true`, header names won't be automatically normalized to lowercase. This allows for non-http-spec-compliant servers that might expect capitalized header names.

###### [`print`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-print)

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

###### [`useGETForQueries`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#options-usegetforqueries)

`boolean`

If `true`, the link uses an HTTP `GET` request when sending query operations to your GraphQL endpoint. Mutation operations continue to use `POST` requests. If you want all operations to use `GET` requests, set `fetchOptions.method` instead.

### [`HttpLink.ContextOptions`](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#httplink.contextoptions)

Options passed to `HttpLink` through [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Previous non-terminating links in the link chain also can set these values to customize the behavior of `HttpLink` for each operation.

**note**

Some of these values can also be provided to the `HttpLink` constructor. If a value is provided to both, the value in `context` takes precedence.

Properties

Name / Type

Description

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

###### [`http`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-http)

`BaseHttpLink.HttpOptions`

An object that configures advanced functionality, such as support for persisted queries.

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/networking/basic-http-networking.md#contextoptions-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.
