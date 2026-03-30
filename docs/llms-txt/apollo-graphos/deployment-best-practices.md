# Source: https://www.apollographql.com/docs/graphos/platform/production-readiness/deployment-best-practices.md

# Deployment Best Practices

This article covers deployment best practices, including:

* Updating and removing subgraphs
* Advanced deployment workflows, including blue-green and canary deployments

Before diving into those topics, it's important to understand the `rover subgraph publish` lifecycle that happens whenever you publish a subgraph's schema changes to GraphOS.

## The `rover subgraph publish` lifecycle

Whenever you run the command [`rover subgraph publish`](https://www.apollographql.com/docs/rover/commands/subgraphs#publishing-a-subgraph-schema-to-graphos) for a particular subgraph, it updates the subgraph's schema and the router's configuration.

Because your graph is dynamically changing and multiple subgraphs might be updated simultaneously, it's possible for changes to cause composition errors, even if [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs#validating-subgraph-schema-changes) was successful. For this reason, updating a subgraph re-triggers composition in GraphOS, ensuring that all subgraphs still compose to form a complete supergraph before updating the supergraph configuration. The workflow behind the scenes can be summed up as follows:

1. The subgraph schema is uploaded to GraphOS and indexed.
2. The subgraph is updated in the registry to use its new schema.
3. All subgraphs are composed in GraphOS to produce a new supergraph schema.
4. If composition fails, the command exits and emits errors.
5. If composition succeeds, [Apollo Uplink](https://www.apollographql.com/docs/graphos/routing/uplink) begins serving the updated supergraph schema.

The router sits on the other side of the equation. The router regularly polls Apollo Uplink for changes to its configuration. The lifecycle of dynamic configuration updates is as follows:

1. The router polls Uplink for updates to its configuration.
2. On update, the router downloads the updated configuration, including the new supergraph schema.
3. The router uses the new supergraph schema to update its query planning logic. The router also prewarms the query plan cache with known queries in a separate thread.
4. The router continues resolving in-flight requests with the previous configuration and uses the updated configuration for all new requests once prewarming has completed.

Alternatively, instead of getting its configuration from Apollo Uplink, the router can specify a local file to a supergraph schema upon its deployment. This static configuration is useful when you want the router to use a schema different than the latest validated schema from Uplink or when you don't have connectivity to Apollo Uplink. For an example of this workflow, see an [example of configuring the router for blue-green deployment](https://www.apollographql.com/docs/graphos/platform/production-readiness/deployment-best-practices.md#example-blue-green-deployment).

## Updating subgraphs safely

When rolling out changes to a subgraph, use the following workflow:

1. Confirm the backward compatibility of each schema change by running [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs/#validating-subgraph-schema-changes) in your CI pipeline.

* Refer to the [backward incompatible section](https://www.apollographql.com/docs/graphos/platform/production-readiness/change-management#backward-incompatible-subgraph-schema-changes) on schema change management for more details.

2. Merge backward compatible changes that successfully pass schema checks.
3. Deploy changes to the subgraph in your infrastructure.
4. Wait until all replicas finish deploying.
5. Only publish schema changes to GraphOS after all replicas of that subgraph are deployed. You publish a subgraph's schema by running [`rover subgraph publish`](https://www.apollographql.com/docs/rover/commands/subgraphs/#publishing-a-subgraph-schema-to-graphos):

   ```bash
   rover subgraph publish my-supergraph@my-variant \
     --schema ./accounts/schema.graphql \
     --name accounts \
     --routing-url https://my-running-subgraph.com/api
   ```

Waiting to publish the updated schema until after these steps ensures that:

* Resolvers are in place for all operations that are executable against your graph.
* Operations can't attempt to access fields that don't yet exist.

### Changes affecting query planner performance

Certain changes to your subgraph schemas pass `rover subgraph check`, meaning the updated subgraph schema can successfully be composed into the supergraph. Despite this, some of these changes may harm the [query planner's](https://www.apollographql.com/docs/graphos/routing/about-router#subgraph-query-planner) performance.

Examples of changes that can impact query planning include:

* Modifying `@key`, `@requires`, `@provides`, or `@shareable` directive usage
* Adding or removing a type implementation from an interface
* Using `interfaceObject` and adding new fields to an interface

Approach subgraph field and type migrations as you would database migrations.
The example scenarios below provide guidance on handling these types of changes.

#### Example change to `@requires`

Consider the following example of a `Products` subgraph and a `Reviews` subgraph:

```graphql title=Products subgraph
type Product @key(fields: "upc") {
  upc: ID!
  nameLowerCase: String!
}
```

```graphql title=Reviews subgraph
type Product @key(fields: "upc") {
  upc: ID!
  nameLowercase: String! @external
  reviews: [Review]! @requires(fields: "nameLowercase")
}
```

Suppose you want to deprecate the `nameLowercase` field and replace it with the `name` field, like so:

```graphql title=Products subgraph
type Product @key(fields: "upc") {
  upc: ID!
  nameLowerCase: String! @deprecated
  name: String!
}
```

```graphql title=Reviews subgraph
type Product @key(fields: "upc") {
  upc: ID!
  nameLowercase: String! @external
  name: String! @external
  reviews: [Review]! @requires(fields: "name")
}
```

To perform this migration in place:

1. Modify the `Products` subgraph to add the new field using `rover subgraph publish` to push the new subgraph schema.
2. Deploy a new version of the `Reviews` subgraph with a resolver that accepts either `nameLowercase` or `name` in the source object.
3. Modify the Reviews subgraph's schema in the registry so that it `@requires(fields: "name")`.
4. Deploy a new version of the `Reviews` subgraph with a resolver that only accepts the `name` in its source object.

Alternatively, you can perform this operation with an atomic migration at the subgraph level by modifying the subgraph's URL:

1. Modify the `Products` subgraph to add the `name` field (as usual, first deploy all replicas, then use `rover subgraph publish` to push the new subgraph schema).
2. Deploy a new set of `Reviews` replicas to a new URL that reads from `name`.
3. Register the `Reviews` subgraph with the new URL and the schema changes above.

With this atomic strategy, the query planner resolves all outstanding requests to the old subgraph URL that relied on `nameLowercase` with the old query-planning configuration, which `@requires` the `nameLowercase` field. All new requests are made to the new subgraph URL using the new query-planning configuration, which `@requires` the `name` field.

#### Example interface type implementation removal

Suppose you define a `Channel` interface in one subgraph and other types that implement `Channel` in two other subgraphs:

```graphql title=Channel subgraph
interface Channel @key(fields: "id") {
  id: ID!
}
```

```graphql title=Web subgraph
type WebChannel implements Channel @key(fields: "id") {
  id: ID!
  webHook: String!
}
```

```graphql title=Email subgraph
type EmailChannel implements Channel @key(fields: "id") {
  id: ID!
  emailAddress: String!
}
```

To safely remove the `EmailChannel` type from your supergraph schema:

1. Perform a `rover subgraph publish` of the `email` subgraph that removes the `EmailChannel` type from its schema.
2. Deploy a new version of the subgraph that removes the `EmailChannel` type.

The first step causes the query planner to stop sending fragments `...on EmailChannel`, which would fail validation if sent to a subgraph that isn't aware of the type.

If you want to keep the `EmailChannel` type but remove it from the `Channel` interface, the process is similar. Instead of removing the `EmailChannel` type altogether, only remove the `implements Channel` addendum to the type definition. This is because the query planner expands queries to interfaces or unions into fragments on their implementing types.

For example, a query like this:

```graphql
query FindChannel($id: ID!) {
  channel(id: $id) {
    id
  }
}
```

generates two queries, one to each subgraph, like so:

```graphql title=Query to email subgraph
query {
  _entities(...) {
    ...on EmailChannel {
      id
    }
  }
}
```

```graphql title=Query to web subgraph
query {
  _entities(...) {
    ...on WebChannel {
      id
    }
  }
}
```

Currently, the router expands all interfaces into implementing types.

## Removing a subgraph

To "de-register" a subgraph with Apollo, call `rover subgraph delete`:

This action cannot be reversed!

```bash
rover subgraph delete my-supergraph@my-variant --name accounts
```

The next time it starts up or polls, your router obtains an updated configuration that reflects the removed subgraph.

## Advanced deployment workflows

With managed federation, you can control which version of your schema your router fleet uses. In most cases, rolling over all of your router instances to a new schema version is safe, assuming you've used [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/) to confirm that your changes are backward compatible. Your deployment model, however, may require an advanced workflow to deploy a specific schema version.

Two types of advanced deployment workflows:

* **Blue-green deployment workflow**. For deployments that require progressive rollout, such as blue-green deployments, you can configure your environments to refer to a single [graph variant](https://www.apollographql.com/docs/graphos/get-started/concepts/graphs-and-variants#variants) by pinning each environment's supergraph schema to your routers at deployment time. Using a single variant between different production environments enables GraphOS Studio to get usage reports, analyze the combined production traffic of all environments, and provide a consistent changelog of your schema over time.

* **Graph variant workflow**. Changes at the router level might involve various different updates, such as [migrating entities](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/migrate-fields) from one subgraph to another. If your infrastructure requires a more advanced deployment process to handle the different router updates, you can use [graph variants](https://www.apollographql.com/docs/graphos/get-started/concepts/graphs-and-variants#variants) to manage router fleets running with different configurations.

  A common use for graph variants is [contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview), for example, to create separate contract variants for the public and private APIs of a supergraph schema.

### Example blue-green deployment

A blue-green deployment strategy uses two environments: One environment (blue) serves the schema variant for live traffic, and the other environment (green) uses a variant for a new release under development. When the new release is ready, traffic moves from the blue to the green environment. This cycle repeats with each new release.

#### Choosing a deployment approach

| Approach              | Best for                                                          | Downtime | Rollback speed | Complexity |
| --------------------- | ----------------------------------------------------------------- | -------- | -------------- | ---------- |
| Graph artifacts (OCI) | High-traffic production environments requiring immutable versions | Zero     | Instant        | High       |
| Platform API          | Integrated CI/CD pipelines with launch tracking                   | Zero     | Instant        | High       |
| Rolling               | Low-traffic or simpler setups                                     | Minimal  | Delayed        | Low        |

#### Blue-green with graph artifacts

[Graph artifacts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/graph-artifacts) are versioned, immutable packages of your supergraph schema. Each time you publish a schema, GraphOS automatically generates a graph artifact. GraphOS stores each artifact in the GraphOS registry and identifies it by a unique SHA-256 digest.

To implement blue-green deployment with graph artifacts:

1. Launch the blue router fleet with the initial graph artifact reference:

   ```bash
   APOLLO_KEY="your-api-key" \
   APOLLO_GRAPH_ARTIFACT_REFERENCE="artifact.api.apollographql.com/my-graph-a50b9d546b298e5a@sha256:14409db3d8a8d74ff9e9a0b5712c0aa8d574bcacc3656e1bc0c55ecf97cd9264" \
   router
   ```

2. Publish a new subgraph to GraphOS. GraphOS composes a new supergraph, but your router fleet will not automatically deploy. [Query for the new graph artifact URI](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/graph-artifacts#find-oci-artifact-references) using the Platform API.

   ```graphql title=GraphArtifactTagLocation
   query GraphArtifactTagLocation($graphId: ID!, $variantName: String!) {
     graphArtifactTagLocation(graphID: $graphId, variantName: $variantName) {
       repository
       tag
     }
   }
   ```

3. Launch the green router fleet with the updated graph artifact reference:

   ```bash
   APOLLO_KEY="your-api-key" \
   APOLLO_GRAPH_ARTIFACT_REFERENCE="artifact.api.apollographql.com/my-graph-a50b9d546b298e5a@sha256:08a2d3c63bf9fc88276d97a9e8df5f841fd772724ad10f119f7e516f228b74c6" \
   router
   ```

4. Shift traffic and monitor. Use your existing infrastructure to monitor and adjust the weighted routing of your load balancers. If errors occur, shift traffic back to the blue fleet.

#### Rolling deployment with graph artifacts

Instead of maintaining two fleets, redeploy each router in the fleet with a new [`APOLLO_GRAPH_ARTIFACT_REFERENCE`](https://www.apollographql.com/docs/graphos/routing/configuration/envvars#apollo_graph_artifact_reference) value.

#### Blue-green deployment with the Platform API

Implement blue-green deployment with the [Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api):

1. Publish all the release's subgraphs at once using the Platform API [`publishSubgraphs` mutation](https://studio.apollographql.com/graph/apollo-platform/variant/main/schema/reference/objects/GraphMutation#publishSubgraphs).

   ```graphql
   ## Publish multiple subgraphs together in a batch
   ## and retrieve the associated launch, along with any downstream launches synchronously.
   mutation PublishSubgraphsMutation(
     $graphId: ID!
     $graphVariant: String!
     $revision: String!
     $subgraphInputs: [PublishSubgraphsSubgraphInput!]!
   ) {
     graph(id: $graphId) {
       publishSubgraphs( #highlight-line
         graphVariant: $graphVariant
         revision: $revision
         subgraphInputs: $subgraphInputs
         downstreamLaunchInitiation: "SYNC"
       ) {
         launch {
           id
           downstreamLaunches {
             id
             graphVariant
             status
           }
         }
       }
     }
   }
   ```

This initiates a launch, as well as any downstream launches necessary for contracts. It returns the launch IDs, with downstream launch IDs configured to return synchronously (`downstreamLaunchInitiation: "SYNC"`) with the mutation.

For contracts, you can also request that any downstream launches return the variant associated with each launch, for example, `downstreamLaunches { graphVariant }`.  When querying for a specific launch, be sure to pass the variant associated with the launch in the following steps.

2. Poll for the completed launch and any downstream launches.

   ```graphql
   ## Poll for the status of any individual launch by ID
   query PollLaunchStatusQuery($graphId: ID!, $graphVariant: String!, $launchId: ID!) {
     graph(id: $graphId) {
       variant(name: $graphVariant) {
         launch(id: $launchId) {
           status
         }
       }
     }
   }

   ```

   When polling for a contract, the `$graphVariant` argument of this query must refer to the contract variant rather than the base variant. You can get it from the query in step 1, from `Launch.graphVariant / downstreamLaunches { graphVariant }`.

3. After the launch and downstream launches have completed, retrieve the supergraph schema of the launch.

   ```graphql
   ## Fetch the supergraph SDL by launch ID.
   query FetchSupergraphSDLQuery($graphId: ID!, $graphVariant: String!, $launchId: ID!) {
     graph(id: $graphId) {
       variant(name: $graphVariant) {
         launch(id: $launchId) {
           build {
             result {
               ... on BuildSuccess {
                 coreSchema {
                   coreDocument
                 }
               }
             }
           }
         }
       }
     }
   }

   ```

   When retrieving for a contract, the `$graphVariant` argument of this query must refer to a contract variant. You can get it from the query in step 1, from `Launch.graphVariant / downstreamLaunches { graphVariant }`.

4. Deploy your routers with the [`-s` or `--supergraph` option](https://www.apollographql.com/docs/graphos/reference/router/configuration#-s----supergraph) to specify the supergraph schema.

   * Specifying the `-s` or `--supergraph` option disables polling for the schema from Uplink.

   * For an example using the option in a `docker run` command, see [Specifying the supergraph](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/docker#specifying-the-supergraph).

5. If you need to roll back to a previous blue-green deployment, ensure the previous deployment is available and shift traffic back to the previous deployment.

   * A router image must use an embedded supergraph schema via the `--supergraph` flag.

   * A deployment should include both router and subgraphs to ensure resolvers and schemas are compatible.

   * If a previous deployment can't be redeployed, repeat steps 3 and 4 with the `launchID` you want to roll back to. Ensure the deployed subgraphs are compatible with the supergraph schema, then redeploy the router with a newly fetched supergraph schema for your target `launchID`. Before considering only rolling back the supergraph schema, see its [caveats](https://www.apollographql.com/docs/graphos/platform/production-readiness/rolling-back-schema-changes#roll-back-supergraph-schema-only).

### Example canary deployment

A canary deployment applies graph updates in an environment separate from a live production environment and validates its updates starting with a small subset of production traffic. As updates are validated in the canary deployment, more production traffic is routed to it gradually until it handles all traffic.

To configure your canary deployment, you can fetch the supergraph schema for a launchID for the canary deployment, then have that canary deployment report metrics to a `prod` variant. Similar to the [blue-green deployment example](https://www.apollographql.com/docs/graphos/platform/production-readiness/deployment-best-practices.md#example-blue-green-deployment), your canary deployment is pinned to the same graph variant as your other, live deployment, so metrics from both deployments are reported to the same graph variant. As your canary deployment is scaled up, it will eventually become the stable deployment serving all production traffic, so we want that deployment reporting to the live `prod` variant.

To configure a canary deployment for the `prod` graph variant:

1. Publish all the canary deployment's subgraphs at once using the Platform API [`publishSubgraphs` mutation](https://studio.apollographql.com/graph/apollo-platform/variant/main/schema/reference/objects/GraphMutation#publishSubgraphs).

   ```graphql
   ## Publish multiple subgraphs together in a batch
   ## and retrieve the associated launch, along with any downstream launches synchronously.
   mutation PublishSubgraphsMutation(
     $graphId: ID!
     $graphVariant: String!
     $revision: String!
     $subgraphInputs: [PublishSubgraphsSubgraphInput!]!
   ) {
     graph(id: $graphId) {
       publishSubgraphs( #highlight-line
         graphVariant: "prod" ## name of production variant
         revision: $revision
         subgraphInputs: $subgraphInputs
         downstreamLaunchInitiation: "SYNC"
       ) {
         launch {
           id
           downstreamLaunches {
             id
             graphVariant
             status
           }
         }
       }
     }
   }
   ```

This initiates a [launch](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/launch/), as well as any downstream launches necessary for [contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/create/#automatic-updates). It returns the launch IDs, with downstream launch IDs configured to return synchronously (`downstreamLaunchInitiation: "SYNC"`) with the mutation.

For contracts, you can also request that any downstream launches return the variant associated with each launch, for example, `downstreamLaunches { graphVariant }`.  When querying for a specific launch, be sure to pass the variant associated with the launch in the following steps.

2. Poll for the completed launch and any downstream launches.

   ```graphql
   ## Poll for the status of any individual launch by ID
   query PollLaunchStatusQuery($graphId: ID!, $graphVariant: String!, $launchId: ID!) {
     graph(id: $graphId) {
       variant(name: $graphVariant) {
         launch(id: $launchId) {
           status
         }
       }
     }
   }

   ```

   When polling for a contract, the `$graphVariant` argument of this query must refer to the contract variant rather than the base variant. You can get it from the query in step 1, from `Launch.graphVariant / downstreamLaunches { graphVariant }`.

3. After the launch and downstream launches have completed, retrieve the supergraph schema of the launch.

   ```graphql
   ## Fetch the supergraph SDL by launch ID.
   query FetchSupergraphSDLQuery($graphId: ID!, $graphVariant: String!, $launchId: ID!) {
     graph(id: $graphId) {
       variant(name: $graphVariant) {
         launch(id: $launchId) {
           build {
             result {
               ... on BuildSuccess {
                 coreSchema {
                   coreDocument
                 }
               }
             }
           }
         }
       }
     }
   }

   ```

   When retrieving for a contract, the `$graphVariant` argument of this query must refer to a contract variant. You can get it from the query in step 1, from `Launch.graphVariant / downstreamLaunches { graphVariant }`.

4. Deploy your routers with the [`-s` or `--supergraph` option](https://www.apollographql.com/docs/graphos/reference/router/configuration#-s----supergraph) to specify the supergraph schema.

   * Specifying the `-s` or `--supergraph` option disables polling for the schema from Uplink.

   * For an example using the option in a `docker run` command, see [Specifying the supergraph](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/docker#specifying-the-supergraph).

5. If you need to roll back, ensure the previous deployment is available and shift traffic back to the live deployment.

   * A router image must use an embedded supergraph schema via the `--supergraph` flag.

   * A deployment should include both router and subgraphs to ensure resolvers and schemas are compatible.

   * If a previous deployment can't be redeployed, repeat steps 3 and 4 with the `launchID` you want to roll back to. Ensure the deployed subgraphs are compatible with the supergraph schema, then redeploy the router with a newly fetched supergraph schema for your target `launchID`. Before considering only rolling back the supergraph schema, see its [caveats](https://www.apollographql.com/docs/graphos/platform/production-readiness/rolling-back-schema-changes#roll-back-supergraph-schema-only).

With your canary deployment [reporting metrics to GraphOS](https://www.apollographql.com/docs/graphos/platform/insights/collection), you can use [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content) to verify a canary's performance before rolling out changes to the rest of the graph.
