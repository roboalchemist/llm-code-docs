# Source: https://relay.dev/docs/guides/relay-resolvers/introduction/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Introduction to Relay Resolvers]

[Version: v20.1.0]

On this page

<div>

# Introduction to Relay Resolvers

</div>

Relay Resolvers are a Relay feature which allow you to augment Relay's GraphQL graph with values that are known only on the client. This allows you to schematize client state in the same way that you model server state, and to use Relay's familiar data-fetching APIs to access that state. Client state can include both data from client-side data stores as well as derived data that is computed from other values in the graph.

By modeling derived and client state in the graph, Relay can present a unified data access API for product developers. All globally relevant data that a product engineer wants to access can be discovered and efficiently obtained from the same structured GraphQL schema. Additionally resolvers provide a number of runtime benefits:

-   Global memoization with garbage collection
-   Efficient reactive recomputation of resolvers
-   Efficient UI updates when data changes

You can think of resolvers as additional schema types and fields which are defined in your client code and are stitched into your server's schema. Just like you define resolver methods/functions which model your fields on the server, Relay Resolves are defined using resolver functions.

## Use Cases for Relay Resolvers[​](#use-cases-for-relay-resolvers "Direct link to Use Cases for Relay Resolvers") 

Relay Resolvers are useful for modeling a number of different kinds of data. Here are some examples of types of data that can be schematized using Relay Resolvers and made available to product code:

-   **User-Created Data** - You can model complex form state, or other data that should outlive a specific component tree
-   **Client-Side Database** - Persistent data stores like IndexDB, localStorage, or SQLite
-   **Third-Party APIs** - Data that is fetched from a third-party API directly by the client, for example search results from an third-party search provider
-   **Encrypted Data** - End-to-end encrypted data that is opaque on the server and thus cannot be modeled in the server schema
-   **Legacy Data Stores** - During the adoption of Relay and GraphQL, data from pre-existing data layers, like Redux, can be exposed in the graph to ensure migrated and un-migrated portions of your app always remain in sync

## Defining a Resolver[​](#defining-a-resolver "Direct link to Defining a Resolver") 

Resolvers are defined using exported functions that are annotated with a special [`@RelayResolver` docblock](/docs/api-reference/relay-resolvers/docblock-format/). These docblocks are visible to the Relay compiler, and allow the compiler to build up your client schema and automatically import your function in Relay's generated artifacts. Resolver functions may be defined in any file in your Relay project, though you may wish to define some convention for where they live within your codebase.

The simplest resolver augments an existing type and does not have any inputs:

``` 
/**
 * @RelayResolver Query.greeting: String
 */
export function greeting(): string 
```

Consuming resolvers is identical to consuming a server field. Product code doesn\'t need to know which kind of field it is reading.

``` 
import  from 'react-relay';
import  from 'react-relay';

function Greeting() `, );
  return <p></p>;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If your query contains only client-defined fields, you will need to use a a different query API to fetch data. Note how this example uses `useClientQuery` instead of `useLazyLoadQuery` or `usePreloadedQuery`. If your query also contains server data, you can use the standard `useLazyLoadQuery` or `usePreloadedQuery` APIs.

We intend to remove this requirement in future versions of Relay.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/introduction.md)