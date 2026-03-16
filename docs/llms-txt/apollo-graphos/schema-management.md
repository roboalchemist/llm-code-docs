# Source: https://www.apollographql.com/docs/graphos/platform/schema-management.md

# GraphOS Schema Management

GraphOS includes tools to help you develop, publish, and manage changes to your schemas. These fall into two main categories:

* **Schema delivery** tools let you publish schema updates as part of your DevOps workflows.
* **Schema governance** tools let you manage, validate, and enforce standards in your schemas.

## Schema delivery

Schema delivery is the process of making your supergraph schema available to clients. You can publish schema changes [using the Rover CLI](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish#publish-subgraph-schemas) or [GraphOS Platform API](https://www.apollographql.com/docs/graphos/reference/platform-api). Using the Rover CLI, you can publish changes as part of your continuous delivery pipeline.

To integrate other aspects of your supergraph configuration, such as your router configuration or federation version, GraphOS uses the concept of [launches](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/launch). Schema publications trigger launches that you can monitor from the **Launches** page in GraphOS Studio.

### Contracts

GraphOS [contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview) let you deliver different subsets of your supergraph to different consumers. Contracts rely on [`@tags`](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/create/#1-add-tags-to-subgraph-schemas) in subgraph schemas to denote which types and fields are accessible to different consumers.

## Schema governance

GraphOS helps you evolve your schemas safely and collaboratively with built-in schema governance tools:

* [Schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks) catch breaking changes before they’re published and help confirm whether potentially dangerous changes are actually safe.
* [Schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting) enforces consistency and best practices across your schemas. Automated linting reduces maintenance work and boosts developer productivity. You can run linting as [part of schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/#linting-via-schema-checks) in GraphOS Studio or [on demand with the Rover CLI](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/#one-off-linting).
* [Schema proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals) provide built-in change management for subgraph schemas. Team members can suggest changes, review them, and approve them before they go live. Proposals improve governance and also encourage collaboration across teams and organizations.
