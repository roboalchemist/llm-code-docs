# Source: https://www.apollographql.com/docs/graphos/platform/platform-limits.md

# Platform Limits

The GraphOS Platform API provides various GraphOS actions you can perform from your own custom application. These actions, such as running schema checks or publishing schema updates, are subject to rate limiting.

## Graph schema reads by hash

Accessing a graph schema by its hash using the `Graph.doc` and `Graph.docs` fields is subject to a rate limit of 120 requests per minute, per graph.

## Subgraph publishing

The `Mutation.graph.publishSubgraph` and `Mutation.graph.publishSubgraphs` mutations, along with the `rover subgraph publish` command, are subject to a rate limit of 400 requests per minute, per graph.

## Graph insights data

The `Query.graph.topOperationsReport` query is subject to a rate limit of five requests per minute, per graph.

## Proposals

Proposals have the following limits:

* **Creating proposals**: The `Mutation.graph.createProposal` mutation is subject to a rate limit of 500 requests per minute, per graph.
* **Reading proposals**: The `Query.graph.proposals` and `Query.graph.variant.proposal` queries are subject to a rate limit of 1000 requests per minute, per graph.
* **Updating approvers**: The `Mutation.graph.variant.proposal.updateRequestedReviewers` mutation is subject to a rate limit of 500 requests per minute, per graph.
* **Publishing to proposals**: The `Mutation.graph.variant.proposal.publishSubgraph` and `Mutation.graph.variant.proposal.publishSubgraphs` mutations are subject to a rate limit of 500 requests per minute, per variant.

## Operation collections

Operation collections have the following limits:

* **Reading operation collections**: The `Query.operationCollection` and `Query.operationCollectionEntries` queries are subject to a rate limit of 100 requests per minute.
* **Creating operation collections**: The `Mutation.operationCollection` mutation is subject to a rate limit of 200 requests per minute.
