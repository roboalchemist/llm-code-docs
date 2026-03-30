# Source: https://www.apollographql.com/docs/react.md

# Introduction to Apollo Client

**Apollo Client** is a comprehensive GraphQL state management library for JavaScript. It enables you to manage both local and remote data with GraphQL. Use it to fetch, cache, and modify application data, all while automatically updating your UI.

Apollo Client helps you structure code in an economical, predictable, and declarative way that's consistent with modern development practices. The core `@apollo/client` library provides built-in integration with React, and the larger Apollo community maintains [integrations for other popular view layers](https://www.apollographql.com/docs/react.md#community-integrations).

Get started!

## Core features

Some of Apollo Client's core capabilities include:

* **Declarative data fetching:** Write a query and receive data without manually tracking loading states.
* **Normalized request and response caching:** Boost performance by responding almost immediately to queries with cached data.
* **Excellent developer experience:** Enjoy helpful tooling for TypeScript, Chrome / Firefox devtools, and VS Code.
* **Designed for modern React:** Take advantage of the latest React features, such as hooks and Suspense.
* **Incrementally adoptable:** Drop Apollo Client into any JavaScript or TypeScript app and incorporate it feature by feature.
* **Universally compatible:** Use any build setup and any GraphQL API.
* **Community driven:** Share knowledge with thousands of developers in the GraphQL community.

## AI-powered assistance

Need help while coding? [Skills](https://agentskills.io/what-are-skills) are a lightweight format for extending AI agents with specialized knowledge. The Apollo Client skill teaches your AI assistant expert patterns for Apollo Client 4.x.

Install it with:

```bash
npx skills add apollographql/skills --skill apollo-client
```

Once installed, your AI assistant gains expert knowledge about setup, configuration, troubleshooting, hooks, caching strategies, and React integration patterns.

## GraphOS supported features

Apollo Client works seamlessly with these GraphOS router supported features:

* Receiving data for specific fields incrementally with the [`@defer` directive](https://www.apollographql.com/docs/graphos/operations/defer)
* Real-time updates via [GraphQL subscriptions](https://www.apollographql.com/docs/graphos/operations/subscriptions)
* Safelisting with [persisted queries](https://www.apollographql.com/docs/graphos/operations/persisted-queries)

Apollo Client also supports `@defer` and GraphQL subscription implementations outside of GraphOS. See the [Defer](https://www.apollographql.com/docs/react/data/defer) guide and [Subscriptions](https://www.apollographql.com/docs/react/data/subscriptions) guide for more information.

## Recommended docs

After you [get started](https://www.apollographql.com/docs/react/get-started/), check out the full Apollo Client documentation in the navigation.

We recommend the following articles in particular:

* [**Queries**](https://www.apollographql.com/docs/react/data/queries/). Learn how to fetch and render data using GraphQL queries.
* [**Fragments**](https://www.apollographql.com/docs/react/data/fragments/). Learn how to use fragments and data masking to build robust, data-driven components.
* [**Mutations**](https://www.apollographql.com/docs/react/data/mutations/). Learn how to modify data using GraphQL mutations.
* [**Caching overview**](https://www.apollographql.com/docs/react/caching/overview/). Apollo Client's normalized cache enables you to skip network requests entirely when data is already available locally.
* [**Managing local state**](https://www.apollographql.com/docs/react/local-state/local-state-management/). Apollo Client provides APIs for managing both remote and local data, enabling you to consolidate all of your application's state.
* [**Basic HTTP networking**](https://www.apollographql.com/docs/react/networking/basic-http-networking/). Learn how to send custom headers and other authentication metadata in your queries.
* [**Testing React components**](https://www.apollographql.com/docs/react/development-testing/testing/). Test your GraphQL operations without requiring a connection to a server.

## Community integrations

This documentation set focuses on React, but Apollo Client supports many other libraries and languages:

* JavaScript
  * [Angular](https://www.apollographql.com/docs/react/integrations/integrations/#angular)
  * [Vue](https://www.apollographql.com/docs/react/integrations/integrations/#vue)
  * [Svelte](https://www.apollographql.com/docs/react/integrations/integrations/#svelte)
  * [Solid.js](https://www.apollographql.com/docs/react/integrations/integrations/#solidjs)
  * [Ember](https://www.apollographql.com/docs/react/integrations/integrations/#ember)
  * [Meteor](https://www.meteor.com/) (thanks to [DDP-Apollo](https://github.com/Swydo/ddp-apollo))
* Web Components
  * [Apollo Elements](https://www.apollographql.com/docs/react/integrations/integrations/#web-components)
* Native mobile
  * [Native iOS with Swift](https://www.apollographql.com/docs/ios)
  * [Native Android with Java and Kotlin](https://www.apollographql.com/docs/kotlin)
