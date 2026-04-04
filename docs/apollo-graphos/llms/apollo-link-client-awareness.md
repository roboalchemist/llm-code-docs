# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md

# ClientAwarenessLink

`ClientAwarenessLink` provides support for providing client awareness features.

Client awareness adds identifying information about the client to HTTP requests for use with metrics reporting tools, such as [Apollo GraphOS](https://apollographql.com/docs/graphos/platform). It is included in the functionality of [`HttpLink`](https://apollographql.com/docs/react/api/link/apollo-link-http) by default.

Client awareness distinguishes between user-provided client awareness (provided by the `clientAwareness` option) and enhanced client awareness (provided by the `enhancedClientAwareness` option). User-provided client awareness enables you to set a customized client name and version for identification in metrics reporting tools. Enhanced client awareness enables the identification of the Apollo Client package name and version.

TypeScript

```
 import { ClientAwarenessLink } from "@apollo/client/link/client-awareness";

 const link = new ClientAwarenessLink({
   clientAwareness: {
     name: "My Client",
     version: "1",
   },
   enhancedClientAwareness: {
     transport: "extensions",
   },
 });
```

## Constructor signature

```ts
constructor(
  options?: ClientAwarenessLink.Options
): ClientAwarenessLink
```

## Configuring client awareness

Client awareness can be configured in various ways in Apollo Client.

### Configuring with Apollo Client

You can configure client awareness when initializing your Apollo Client instance using the `clientAwareness` and `enhancedClientAwareness` options. Options configured with the `ClientAwarenessLink` constructor, `HttpLink` constructor, or [request context](https://www.apollographql.com/docs/react/api/link/introduction#managing-context) take precedence.

```ts
import { ApolloClient } from "@apollo/client";

new ApolloClient({
  clientAwareness: {
    name: "My Client",
    version: "my_client_version",
  },
  enhancedClientAwareness: {
    transport: "extensions",
  },
});
```

### Configuring with `HttpLink`

You can configure client awareness when initializing an `HttpLink` using the `clientAwareness` and `enhancedClientAwareness` options. These options take precedence over options provided to the `ApolloClient` constructor but can be overridden by [request context](https://www.apollographql.com/docs/react/api/link/introduction#managing-context).

```ts
import { ApolloClient, HttpLink } from "@apollo/client";

const link = new HttpLink({
  clientAwareness: {
    name: "My Client",
    version: "my_client_version",
  },
  enhancedClientAwareness: {
    transport: "extensions",
  },
});

const client = new ApolloClient({
  link,
  // additional options
});
```

If you use `BaseHttpLink`, add `ClientAwarenessLink` to your link chain manually to enable client awareness. `HttpLink` includes `ClientAwarenessLink` by default.

### Configuring with request context

Configure client awareness on a per-request basis by providing the `clientAwareness` field in the request's `context`. These values take precedence over all other configurations.

The `enhancedClientAwareness` field is not supported in request context. Configure this feature at the client or link level instead.

```ts
const client = new ApolloClient(/* ... */);

function MyComponent() {
  const { data } = useQuery(query, {
    context: {
      clientAwareness: {
        name: "My Client",
        version: "my_client_version",
      },
    },
  });

  // ...
}
```

## Types

### [`ClientAwarenessLink.ContextOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenesslink.contextoptions)

Options passed to `ClientAwarenessLink` through [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Previous non-terminating links in the link chain also can set these values to customize the behavior of `ClientAwarenessLink` for each operation.

**note**

Some of these values can also be provided to the `ClientAwarenessLink` constructor. If a value is provided to both, the value in `context` takes precedence.

Properties

Name / Type

Description

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#contextoptions-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

### [`ClientAwarenessLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenesslink.options)

Properties

Name / Type

Description

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#options-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

###### [`enhancedClientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#options-enhancedclientawareness)

`ClientAwarenessLink.EnhancedClientAwarenessOptions`

Configures the "enhanced client awareness" feature. This feature allows you to identify the version of the Apollo Client library used in your application in Apollo Studio (and other monitoring or analytics tools) by adding information about the Apollo Client library to outgoing requests.

### [`ClientAwarenessLink.ClientAwarenessOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenesslink.clientawarenessoptions)

Properties

Name / Type

Description

###### [`name`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenessoptions-name)

`string`

A custom name (e.g., `iOS`) that identifies this particular client among your set of clients. Apollo Server and Apollo Studio use this property as part of the [client awareness](https://www.apollographql.com/docs/apollo-server/monitoring/metrics.md#identifying-distinct-clients) feature.

This option can either be set as part of the Apollo Client constructor call or when manually constructing a `HttpLink`, `BatchHttpLink` or `ClientAwarenessLink`.

###### [`transport`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenessoptions-transport)

`"headers" | false`

Determines how `name` and `version` are sent in outgoing requests.

If `name` and `version` are not provided, this option will be ignored. (These options can either be set as part of the Apollo Client constructor call or when manually constructing a `HttpLink`, `BatchHttpLink` or `ClientAwarenessLink`.)

* If set to `"headers"`, `name` and `version` will be sent in the request headers as `apollographql-client-name` and `apollographql-client-version`, respectively.

* If set to `false`, `name` and `version` will not be included in outgoing requests.

###### [`version`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenessoptions-version)

`string`

A custom version that identifies the current version of this particular client (e.g., `1.2`). Apollo Server and Apollo Studio use this property as part of the [client awareness](https://www.apollographql.com/docs/apollo-server/monitoring/metrics.md#identifying-distinct-clients) feature.

This is **not** the version of Apollo Client that you are using, but rather any version string that helps you differentiate between versions of your client.

This option can either be set as part of the Apollo Client constructor call or when manually constructing a `HttpLink`, `BatchHttpLink` or `ClientAwarenessLink`.

### [`ClientAwarenessLink.EnhancedClientAwarenessOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#clientawarenesslink.enhancedclientawarenessoptions)

Properties

Name / Type

Description

###### [`transport`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-client-awareness.md#enhancedclientawarenessoptions-transport)

`"headers" | "extensions" | false`

Determines how the the version information of Apollo Client is sent in outgoing requests.

* If set to `"extensions"`, library `name` and `version` will be sent in an object in the request extensions as `clientLibrary`.

* If set to `false`, library name and version will not be included in outgoing requests.
