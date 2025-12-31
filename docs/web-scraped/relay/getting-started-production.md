# Source: https://relay.dev/docs/getting-started/production/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Production Setup]

[Version: v20.1.0]

On this page

<div>

# Production Setup

</div>

Getting the most out of Relay in production requires a few extra steps. This page covers a list of best practices for taking Relay to production.

## Persisted Queries (Trusted Documents)[​](#persisted-queries-trusted-documents "Direct link to Persisted Queries (Trusted Documents)") 

One of GraphQL\'s key innovations is that it enables clients to define arbitrary queries. While this unlocks a lot of flexibility, it also opens the doors to abuse. Scrapers can use GraphQL to scrape data from your site, and malicious users can use GraphQL to send large requests to your server that cause a denial of service. To prevent this, we recommend using [Persisted Queries](/docs/guides/persisted-queries/) also know as [Trusted Documents](https://benjie.dev/graphql/trusted-documents).

With Persisted Queries, the set of queries that the client can send is locked in at build time. This means that scrapers and malicious attackers are limited to sending only the queries used by the client, just like REST. It also has the added benefit that the client code only needs to include an single id for each query rather than the whole query text.

## Relay Lint Rules[​](#relay-lint-rules "Direct link to Relay Lint Rules") 

A key principal of Relay is data colocation where each component defines its own data dependencies. It\'s critical to [How Relay Enables Optimal Data Fetching](https://relay.dev/blog/2023/10/24/how-relay-enables-optimal-data-fetching/). However, this is often unintuitive for developers who are used to fetching data in a single query. Relay\'s ESLint rules can help enforce this pattern by ensuring no component fetches fields which it does not itself use.

We recommend using the [`eslint-plugin-relay`](https://github.com/relayjs/eslint-plugin-relay), especially the `relay/unused-fields` rule.

Learn how to install them: [Relay ESLint Plugin](/docs/getting-started/lint-rules/).

## Running the Relay Compiler in CI[​](#running-the-relay-compiler-in-ci "Direct link to Running the Relay Compiler in CI") 

We recommend committing Relay\'s generated artifacts to source control along with your application code. This ensures generated types are present without needing an additional build, and allows for inspection of generated artifacts in code review. To ensure the generated artifacts are always in sync with the source code, we recommend running the Relay compiler in CI and ensuring it does not change any generated files. A example bash script which checks for changes can be found [here](https://github.com/facebook/relay/blob/0414c9ad0744483e349e07defcb6d70a52cf8b3c/scripts/check-git-status.sh).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/getting-started/production.md)