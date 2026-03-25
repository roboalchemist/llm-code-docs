# Source: https://relay.dev/docs/api-reference/relay-runtime/relay-environment/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Relay Runtime]
-   [Relay Environment]

[Version: v20.1.0]

On this page

<div>

# Relay Environment

</div>

The core of Relay\'s runtime is the `Environment`. The environment knows how to make requests to your GraphQL server and contains the `Store`, Relay\'s normalized data cache. Generally your application will construct a single environment which is configured to fetch data from your server, and then expose that environment to all of your components via `RelayEnvironmentProvider`.

## Creating an Environment[​](#creating-an-environment "Direct link to Creating an Environment") 

To create your environment you must provide two key pieces, a [`Network`](/docs/guides/network-layer/) and a [`Store`](/docs/api-reference/store/).

The `Network` is responsible for making requests to your GraphQL server. The `Store` holds the normalized data cache.

A minimal implementation of an environment might look like this:

RelayEnvironment.js

``` 
import  from "relay-runtime";

const HTTP_ENDPOINT = "https://graphql.org/graphql/";

const fetchGraphQL: FetchFunction = async (request, variables) => ,
    body: JSON.stringify(),
  });
  if (!resp.ok) 
  return await resp.json();
};

export const environment = new Environment()),
  network: Network.create(fetchGraphQL),
});
```

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration") 

The Relay environment accepts a number of additional configuration options when it is created. These options are all optional, but can be used to customize the behavior of the environment.

Notable options include:

-   `log` - A function that will be called with telemetry events. See the types for [`LogEvent`](https://github.com/facebook/relay/blob/0414c9ad0744483e349e07defcb6d70a52cf8b3c/packages/relay-runtime/store/RelayStoreTypes.js#L799) for a full list of events and their fields.
-   [`missingFieldHandlers`](/docs/guided-tour/reusing-cached-data/filling-in-missing-data/) - A list of handlers that will be called when a field is missing from the store. This can be used to enable fulfilling queries to fields like `Query.node` from cache.
-   `getDataID` - A function that will be called to generate a unique ID for a given object. This can be used to customize the way that Relay generates IDs for objects if your server does not implement the [Global Object Identification spec](https://graphql.org/learn/global-object-identification/).
-   [`relayFieldLogger`](/docs/api-reference/field-logger/) - A function that will be called when Relay encounters a field-level error.

For a full list of options, inspect the [provided TypeScript types](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/relay-runtime/lib/store/RelayModernEnvironment.d.ts#L26-L43).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/relay-runtime/relay-environment.md)