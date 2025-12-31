# Source: https://relay.dev/docs/guides/relay-resolvers/limitations/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Limitations]

[Version: v20.1.0]

On this page

<div>

# Limitations

</div>

Relay Resolvers are do have some limitations. Here we will collect a list of known limitations and provide alternatives where possible.

## No info argument[​](#no-info-argument "Direct link to No info argument") 

In a full GraphQL implementation, resolvers would have access to an `info` argument. This argument is not available in Relay Resolvers today.

## Not all GraphQL constructs are supported[​](#not-all-graphql-constructs-are-supported "Direct link to Not all GraphQL constructs are supported") 

Today Relay Resolvers only support a subset of GraphQL constructs. For example, it\'s not currently possible to define input types, enums or interfaces using Relay Resolvers.

## No support for mutations[​](#no-support-for-mutations "Direct link to No support for mutations") 

Today Relay Resolvers only support the read path. Defining mutation fields is not yet supported. We are working to understand what it means to perform a mutation against a reactive schema, and hope to support them in the future.

## Resolvers are always evaluated lazily[​](#resolvers-are-always-evaluated-lazily "Direct link to Resolvers are always evaluated lazily") 

Today Relay Resolvers are always evaluated lazily on a per-fragment basis. This has the advantage that if a resolver is not read, it will never be evaluated. However, it can lead to issues with waterfalls if your client schema ends up making async requests to fetch data as its read. We are actively exploring other execution strategies for Relay Resolvers, such as evaluating all fields in a query at request time, but expect the way resolvers are defined to remain stable.

## Verbose/awkward docblock syntax[​](#verboseawkward-docblock-syntax "Direct link to Verbose/awkward docblock syntax") 

Today defining a resolver requires defining a function with a docblock which uses special syntax and duplicates information already specified in the function\'s name and types. Further, in order to enforce that these values match up, Relay emits type assertions in its generated types. While these assertions do ensure safety, they are an awkward developer experience.

To address these issues we are exploring a more streamlined approach where names and types can be inferred from your Flow or TypeScript code similar to the approach taken by [Grats](https://grats.capt.dev/). This syntax may become available in future versions of Relay.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/limitations.md)