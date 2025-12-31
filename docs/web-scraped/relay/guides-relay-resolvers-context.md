# Source: https://relay.dev/docs/guides/relay-resolvers/context/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Context]

[Version: v20.1.0]

On this page

<div>

# Context

</div>

In order to pass a service, or other values to be shared with all resolvers, the `RelayModernStore` provides a means of passing context. This gets passed to the third argument of all resolvers (live and non-live). This context argument analogous to the [context argument](https://graphql.org/learn/execution/#root-fields--resolvers) used on the server which usually holds things like the database connection.

## Setup[​](#setup "Direct link to Setup") 

In order to pass context to live resolvers, pass a `resolverContext` argument to the initialization of `RelayModernStore` before creating the environment:

``` 
const store = new RelayModernStore(source, ,
});
```

## Usage in Resolvers[​](#usage-in-resolvers "Direct link to Usage in Resolvers") 

-   JavaScript
-   Flow

The last argument in a resolver will contain the context type which contains the value passed into the store on initialization. If the resolver is on a model type or reads a `@rootFragment`, the context value will be the third argument. If the resolver is *not* on a model type and does *not* read a `@rootFragment` the context value will be passed as the thrid argument. Relay\'s generated artifacts will include generated type assertions to check that your resolver is typed correctly.

``` 
import type  from 'relay-runtime';

/**
 * @RelayResolver Query.counter: Int
 * @live
 */
export function counter(
  _args,
  context
) ,
  };
}
```

Context is not currently supported in Flow

## Type Checking[​](#type-checking "Direct link to Type Checking") 

In order to ensure that the resolver is implemented with the correct types, pass a `resolverContextType` in the project config. This parameter expects a type name and a `path` to import from:

``` 

}
```

To import from a package, use the following syntax for a `package` import:

``` 

}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/context.md)