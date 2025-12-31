# Source: https://relay.dev/docs/guided-tour/updating-data/typesafe-updaters-faq/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Updating Data]
-   [Typesafe updaters FAQ]

[Version: v20.1.0]

On this page

<div>

# Typesafe Updaters FAQ

</div>

# General

## What is typesafe updaters?[​](#what-is-typesafe-updaters "Direct link to What is typesafe updaters?") 

Typesafe updaters is the name given to a project to provide a typesafe and ergonomic alternative to the existing APIs for imperatively updating data in the Relay store.

For example, [`readUpdatableFragment`](/docs/api-reference/store/#readupdatablefragmentfragment-updatablefragmenttfragmenttype-tdatafragmentreference-hasupdatablespreadtfragmenttype-updatabledatatdata) and [`readUpdatableQuery`](/docs/api-reference/store/#readupdatablequeryquery-updatablequerytvariables-tdatavariables-tvariables-updatabledatatdata) are two typesafe updaters that the store exposes.

## Why?[​](#why "Direct link to Why?") 

Relay provides typesafe and ergonomic APIs for fetching and managing data that originates on the server. In addition, Relay provides the ability to define local-only fields in **client schema extensions**. However, the APIs for mutating the data in these fields has hitherto been verbose and not ergonomic, meaning that we could not recommend Relay as a solution for managing local state.

## What was wrong with the existing APIs?[​](#what-was-wrong-with-the-existing-apis "Direct link to What was wrong with the existing APIs?") 

The pre-existing APIs are verbose and not typesafe. They make it easy to make a variety of mistakes and require that the developer understand a new set of APIs only when writing updaters.

Typesafe updaters is a set of APIs that are typesafe and more ergonomic. They leverage well-known Relay idioms (queries, fragments, type refinement) and use getters and setters instead of requiring that the developer learn about a set of methods that are unused elsewhere.

## How does a developer use typesafe updaters?[​](#how-does-a-developer-use-typesafe-updaters "Direct link to How does a developer use typesafe updaters?") 

With typesafe updaters, a developers writes an updatable query or a fragment that specifies the data to imperatively update. Then, the developer reads out that data from the store, returning a so-called **updatable proxy**. Then, the developer mutates that updatable proxy. Mutating that updatable proxy using setters (e.g. `updatableData.name = "Godzilla"`) results in calls to the old API, but with added type safety.

## What is an updatable query or fragment?[​](#what-is-an-updatable-query-or-fragment "Direct link to What is an updatable query or fragment?") 

An updatable query or fragment is a query or fragment that has the `@updatable` directive.

# Updatable queries and fragments are not fetched

## Are fields selected in updatable queries and fragments fetched from the server?[​](#are-fields-selected-in-updatable-queries-and-fragments-fetched-from-the-server "Direct link to Are fields selected in updatable queries and fragments fetched from the server?") 

No! The server doesn\'t know about updatable queries and fragments. Their fields are never fetched.

Even if you spread an updatable fragment in a regular query or fragment, the fields selected by that updatable fragment are not fetched as part of that request.

## What if I want to fetch a field and also mutate it?[​](#what-if-i-want-to-fetch-a-field-and-also-mutate-it "Direct link to What if I want to fetch a field and also mutate it?") 

You should select that field in both a regular query/fragment **and** in an updatable query/fragment.

## What are some consequences of this?[​](#what-are-some-consequences-of-this "Direct link to What are some consequences of this?") 

-   When you read out updatable data, it can be missing if it isn\'t present in the store.
-   You cannot spread regular fragments in updatable queries/fragments.
-   The generated artifact for updatable queries/fragments does not contain a query ID and does not contain a normalization AST (which is used for writing network data to the store.)
-   Directives like `@defer`, etc. do not make sense in this context, and are disallowed.

# Misc

## Where do I get a `store`?[​](#where-do-i-get-a-store "Direct link to where-do-i-get-a-store") 

The classes `RelayRecordSourceSelectorProxy`, `RecordSourceProxy` and `RelayRecordSourceProxy` contain the methods `readUpdatableQuery` and `readUpdatableFragment`. One can acquire an instance of these classes:

-   In updaters of mutations and subscriptions
-   In optimistic updaters of mutations
-   When using `RelayModernEnvironment`\'s `commitUpdate`, `applyUpdate`, etc. methods.
-   When using the standalone `commitLocalUpdate` method.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/typesafe-updaters-faq.md)