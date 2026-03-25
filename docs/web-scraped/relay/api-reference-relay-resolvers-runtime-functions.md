# Source: https://relay.dev/docs/api-reference/relay-resolvers/runtime-functions/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Relay Resolvers]
-   [Runtime Functions]

[Version: v20.1.0]

On this page

<div>

# Runtime Functions

</div>

This page documents the runtime functions associated with Relay Resolvers. For an overview of Relay Resolvers and how to think about them, see the [Relay Resolvers](/docs/guides/relay-resolvers/introduction/) guide.

## RelayModernStore[​](#relaymodernstore "Direct link to RelayModernStore") 

RelayModernStore exposes `batchLiveStateUpdates()`. See [Live Fields](/docs/guides/relay-resolvers/live-fields/#batching) for more details of how to use this method.

## `readFragment()`[​](#readfragment "Direct link to readfragment") 

Derived resolver fields model data that is derived from other data in the graph. To read the data that a derived field depends on, they must use the `readFragment()` function which is exported from `relay-runtime`. This function accepts a GraphQL fragment and a fragment key, and returns the data for the fragment.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

`readFragment()` may only be used in Relay Resolvers. It will throw an error if used in any other context.

``` 
import  from "relay-runtime";

/**
 * @RelayResolver User.fullName: String
 * @rootFragment UserFullNameFragment
 */
export function fullName(key: UserFullNameFragment$key): string 
  `, key);
  return `$ $`;
}
```

Note that Relay will ensure your field resolver is recomputed any time data in that fragment changes.

See the [Derived Fields](/docs/guides/relay-resolvers/derived-fields/) guide for more information.

## `suspenseSentinel()`[​](#suspensesentinel "Direct link to suspensesentinel") 

Live resolvers model client state that can change over time. If at some point during that field\'s lifecycle, the data being read is in a pending state, for example if the data is being fetched from an API, the resolver may return the `suspenseSentinel()` to indicate that the data is not yet available.

Relay expects that when the data is available, the `LiveStateValue` will notify Relay by calling the subscribe callback.

``` 
import  from 'relay-runtime';

/**
 * @RelayResolver Query.myIp: String
 * @live
 */
export function myIp(): LiveState<string> 
      return state.ip;
    },
    subscribe: (callback) => ,
  };
}
```

See the [Live Fields](/docs/guides/relay-resolvers/live-fields/) guide for more information.

## `useClientQuery()`[​](#useclientquery "Direct link to useclientquery") 

If a query contains only client fields, it may not currently be used with hooks like `usePreloadedQuery` and `useLazyLoadQuery` since both of those hooks assume they will need to issue a network request. If you attempt to use these APIs in Flow you will get a type error.

Instead, for client-only queries, you can use the `useClientQuery` hook:

``` 
import  from 'react-relay';

export function MyComponent() 
  `);
  return <div></div>;
}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/relay-resolvers/runtime-functions.md)