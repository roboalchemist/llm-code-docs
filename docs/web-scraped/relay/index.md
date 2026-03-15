# Source: https://relay.dev/docs/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Home]

[Version: v20.1.0]

On this page

<div>

# Relay Docs

</div>

Relay is a powerful [GraphQL](https://graphql.org/) client for [React](https://react.dev/). It embodies years of learning to give you **outstanding performance by default** while keeping your code **scalable and maintainable**.

Relay brings the composability of React components to data fetching. Each component declares its own data needs, and Relay combines them into efficient pre-loadable queries. Every aspect of its design is to make the natural way of writing components also the most performant.

## Features[​](#features "Direct link to Features") 

-   **Declarative**: Just declare what data each component needs and Relay will handle generating [optimal queries](https://relay.dev/blog/2023/10/24/how-relay-enables-optimal-data-fetching/) for each surface.
-   **Composable**: Components act like building bricks that can click into place anywhere in your app without needing manually update queries.
-   **Pre-fetchable**: Relay\'s generated queries allow you to start fetching data for your surface before your code even downloads or runs.
-   **Built-in UI patterns**: Relay implements loading states, pagination, refetching, optimistic updates, rollbacks, and other common UI behaviors that are tricky to get right.
-   **Consistent state**: Relay maintains a normalized data store, so components that observe the same data stay in sync even if they reach it by different queries.
-   **Type safe**: Relay generates TypeScript types for each GraphQL snippet so that errors are caught statically, not at runtime.
-   **Streaming/deferred data**: Declaratively defer parts of your query and Relay will progressively re-render your UI as the data streams in.
-   **Developer experience**: Relay\'s [editor support](/docs/editor-support/) provides autocompletion and go-to-definition for your GraphQL schema.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/home.md)