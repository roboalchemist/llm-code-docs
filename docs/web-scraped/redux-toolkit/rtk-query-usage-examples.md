# Source: https://redux-toolkit.js.org/rtk-query/usage/examples

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Examples]

On this page

 

<div>

# RTK Query Examples

</div>

## Examples Overview[​](#examples-overview "Direct link to Examples Overview") 

We have a variety of examples that demonstrate various aspects of using RTK Query.

These examples are not meant to be what you base your application on, but exist to show *very specific* behaviors that you may not actually want or need in your application. For most users, the basic examples in the [Queries](/rtk-query/usage/queries) and [Mutations](/rtk-query/usage/mutations) sections will cover the majority of your needs.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Please note that when playing with the examples in CodeSandbox that you can experience quirky behavior, especially if you fork them and start editing files. Hot reloading, CSB service workers and [`msw`](https://mswjs.io/) sometimes have trouble getting on the right page \-- when that happens, just refresh in the CSB browser pane.

## Kitchen Sink[​](#kitchen-sink "Direct link to Kitchen Sink") 

## React Optimistic Updates[​](#react-optimistic-updates "Direct link to React Optimistic Updates") 

In the example below you\'ll notice a few things. There are two `Posts` list on the sidebar. The top one will only update *after* a successful mutation and resync with the server. The *subscribed* one will update immediately due to the optimistic update. In the event of an error, you\'ll see this get rolled back.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

The example has some intentionally wonky behavior\... when editing the name of a post, there is a decent chance you\'ll get a random error.

## React with GraphQL[​](#react-with-graphql "Direct link to React with GraphQL") 

## Authentication[​](#authentication "Direct link to Authentication") 

There are several ways to handle authentication with RTK Query. This is a very basic example of taking a JWT from a login mutation, then setting that in our store. We then use `prepareHeaders` to inject the authentication headers into every subsequent request.

### Dispatching an action to set the user state[​](#dispatching-an-action-to-set-the-user-state "Direct link to Dispatching an action to set the user state") 

This example dispatches a `setCredentials` action to store the user and token information.

### Using `extraReducers`[​](#using-extrareducers "Direct link to using-extrareducers") 

This example uses a matcher from the endpoint and `extraReducers` in the `authSlice`.

## React Class Components[​](#react-class-components "Direct link to React Class Components") 

Check out the `PostDetail` component for an example of Class Component usage.

## Svelte[​](#svelte "Direct link to Svelte") 

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0id2lkdGg6NDRweDtoZWlnaHQ6NDRweCIgdmlld2JveD0iMCAwIDEwMCAxMDAiPjxwb2x5bGluZSBmaWxsPSJub25lIiBwb2ludHM9IjAsIDAsIDEwMCwgMCwgMTAwLCAxMDAiIHN0cm9rZS13aWR0aD0iMTUiIHN0eWxlPSJzdHJva2U6Z3JheSI+PC9wb2x5bGluZT48cG9seWxpbmUgZmlsbD0ibm9uZSIgcG9pbnRzPSIwLCAwLCAwLCAxMDAsIDEwMCwgMTAwIiBzdHJva2Utd2lkdGg9IjE1IiBzdHlsZT0ic3Ryb2tlOmdyYXkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIGZpbGw9Im5vbmUiIHBvaW50cz0iMCwgMCwgMTAwLCAwLCAxMDAsIDEwMCIgc3Ryb2tlLXdpZHRoPSIxNSIgc3R5bGU9ImFuaW1hdGlvbjpzc3ItbG9hZGluZy1zcGFjaW5nIDEuMnMgZWFzZS1pbiwgc3NyLWxvYWRpbmctY29sb3IgNC44cyBsaW5lYXI7YW5pbWF0aW9uLWl0ZXJhdGlvbi1jb3VudDppbmZpbml0ZTthbmltYXRpb24tZGlyZWN0aW9uOm5vcm1hbDthbmltYXRpb24tZmlsbC1tb2RlOmZvcndhcmRzO3RyYW5zZm9ybS1vcmlnaW46Y2VudGVyIGNlbnRlciI+PC9wb2x5bGluZT48cG9seWxpbmUgZmlsbD0ibm9uZSIgcG9pbnRzPSIwLCAwLCAwLCAxMDAsIDEwMCwgMTAwIiBzdHJva2Utd2lkdGg9IjE1IiBzdHlsZT0iYW5pbWF0aW9uOnNzci1sb2FkaW5nLXNwYWNpbmcgMS4ycyBlYXNlLWluLCBzc3ItbG9hZGluZy1jb2xvciA0LjhzIGxpbmVhcjthbmltYXRpb24taXRlcmF0aW9uLWNvdW50OmluZmluaXRlO2FuaW1hdGlvbi1kaXJlY3Rpb246bm9ybWFsO2FuaW1hdGlvbi1maWxsLW1vZGU6Zm9yd2FyZHM7dHJhbnNmb3JtLW9yaWdpbjpjZW50ZXIgY2VudGVyIj48L3BvbHlsaW5lPjwvc3ZnPg==)

 

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/examples.mdx)

[Last updated on **Apr 8, 2022**]