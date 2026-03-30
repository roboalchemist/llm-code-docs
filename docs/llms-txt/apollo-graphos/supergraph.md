# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph.md

# Supergraph resources

A **Supergraph** is a Kubernetes resource that allows you to run the GraphOS Router and its supporting resources.

When you create a Supergraph in your cluster, the Apollo GraphOS Operator will automatically provision the following resources for you:

* A [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) for the GraphOS Router
* A [Service](https://kubernetes.io/docs/concepts/services-networking/service/) for traffic ingress
* A [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) for your GraphOS Router configuration
* A [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) for the [graph API key](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys)

## Deploying a Supergraph

To deploy a Supergraph in your Kubernetes cluster, you must define at least three properties:

* The number of **replicas**
* The GraphOS Router **version** you want to use
* The Supergraph schema source

You can also optionally configure the router using the `routerConfig` property. See [Configuring the Router](https://www.apollographql.com/docs/apollo-operator/resources/supergraph.md#configuring-the-router) for details.

Here is an example that deploys two replicas of the GraphOS Router version 2.7.0, using the latest Supergraph schema version of the **my-graph\@my-variant** graph variant.

```yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: my-supergraph
spec:
  # Number of replicas
  replicas: 2
  # Version of the GraphOS Router
  podTemplate:
    routerVersion: 2.7.0
  # Source for the Supergraph Schema
  schema:
    studio:
      graphRef: my-graph@my-variant
```

## Specifying a schema source

The Supergraph resource type supports three schema sources:

* A GraphOS Studio graph variant reference (**graphRef**).
* A [SupergraphSchema](https://www.apollographql.com/docs/apollo-operator/supergraphschema) resource reference.
* An OCI artifact reference.

### Apollo GraphOS Studio

You can specify a graph variant reference (**graphRef**).

By default, the Supergraph will use the latest available launch in Apollo GraphOS Studio. When you make a change, for example by publishing a new version of a subgraph schema, the Apollo GraphOS Operator will trigger an update to your Supergraph.

```yaml
spec:
  schema:
    studio:
      graphRef: my-graph@my-variant
```

If you want finer grain control over your deployment process, you can specify a launch ID.

You can combine this with a git generator and [schema change notifications](https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-changes) to automatically create pull requests in your repository whenever a new version of your Supergraph schema is available.

```yaml
spec:
  schema:
    studio:
      graphRef: my-graph@my-variant
      launchId: "00000000-0000-0000-0000-000000000000"
```

### SupergraphSchema resource

If you are using [Subgraph](https://www.apollographql.com/docs/apollo-operator/subgraph) and [SupergraphSchema](https://www.apollographql.com/docs/apollo-operator/supergraphschema) resources to define your Supergraph schema using Kubernetes-native resources, you can directly reference the SupergraphSchema resource in your cluster instead.

In this case, the Supergraph will use the latest launch ID marked as **Available** in the SupergraphSchema status.

```yaml
spec:
  schema:
    resource:
      name: my-supergraph
      # Optional: if the resource is not in the same namespace as your Supergraph,
      # you can specify the namespace here:
      namespace: apollo-schemas
```

### OCI artifact reference

For increased reliability, you can store your Supergraph schema as an OCI artifact in your own registry.

To store your supergraph schema in an OCI artifact, you store it in a layer using the `application/vnd.apollographql.schema` file type.

```yaml
spec:
  schema:
    oci:
      reference: my-registry/my-graph:my-tag
      # Optional: graph variant reference for automated integration with the GraphOS Platform
      graphRef: my-graph@my-variant
```

## Configuring the Router

Define router configuration directly in the Supergraph CRD using the `spec.routerConfig` property. The operator automatically applies this configuration—no manual patching or ConfigMap mounting required.

The `routerConfig` section uses the same YAML structure as a standalone router configuration file. Here's an example:

```yaml
spec:
  routerConfig:
    supergraph:
      listen: 0.0.0.0:4000
      introspection: true
    cors:
      allow_any_origin: true
    coprocessor:
      url: http://coprocessor.apollo.svc.cluster.local:8081
      timeout: 2s
      router:
        request:
          headers: true
    authentication:
      router:
        jwt:
          jwks:
            - url: http://auth-service:8080/.well-known/jwks.json
```

**Limitation**: Rhai script configuration is not currently supported via `spec.routerConfig`.

## Monitoring Supergraph deployments

The Apollo GraphOS Operator will monitor changes in your Supergraph resource and reflect them in the resource status. These changes can happen either because you have changed the Supergraph spec or there is a new version of your Supergraph schema available.

It will reflect the state of your resource using three **status conditions** types:

* **SchemaLoaded**: If it was able to load your Supergraph schema and what is the latest known schema version.
* **Progressing**: If a deployment of the GraphOS Router is in progress or was successful, and its current state.
* **Ready**: If your GraphOS Router replicas are able to process traffic.

Here is an example of the conditions for a **Supergraph** with a successful deployment:

```yaml
status:
  conditions:
    - type: "SchemaLoaded"
      status: "True"
      reason: "Loaded"
      observedGeneration: 3
      schema:
        studio:
          graphRef: my-graph@my-variant
          launchId: "00000000-0000-0000-0000-000000000000"
          updatedAt: "2025-07-03T12:34:56Z"
    - type: "Progressing"
      status: "True"
      reason: "DeploymentCompleted"
      observedGeneration: 3
      schema:
        studio:
          graphRef: my-graph@my-variant
          launchId: "00000000-0000-0000-0000-000000000000"
          updatedAt: "2025-07-03T12:34:56Z"
    - type: "Ready"
      status: "True"
      reason: "DeploymentCompleted"
      observedGeneration: 3
      schema:
        studio:
          graphRef: my-graph@my-variant
          launchId: "00000000-0000-0000-0000-000000000000"
          updatedAt: "2025-07-03T12:34:56Z"
```

### Monitoring schema loading

Once the Apollo GraphOS Operator detects that a new Supergraph schema is available, it will update the **SchemaLoaded** condition with the following properties:

* `type: SchemaLoaded`
* `status: True`
* `reason: Loaded`

On the other hand, if the Operator fail to load the Supergraph schema, it will have a condition with the following values:

* `type: SchemaLoaded`
* `status: False`
* `reason: MissingData | reason: FetchError | reason: InvalidSpec`

### Monitoring Supergraph deployments

The deployment of those resources can either be progressing, complete or failed. The Operator will automatically populate the **Progressing** condition to reflect that state.

#### Progressing Supergraph deployment

When the Operator starts a deployment, it will update the Progressing condition with the following properties:

* `type: Progressing`
* `status: True`
* `reason: HasChanges | reason: DeploymentInProgress`

The **HasChanges** reason reflects that the Operator recently applied changes to the underlying resources. If one of these resources is the underlying Deployment, this will trigger a new rollout and will cause the Progressing condition to update to DeploymentInProgress

### Complete Supergraph deployment

When the underlying deployment is complete, the Operator will update the Progressing condition with the following properties:

* `type: Progressing`
* `status: True`
* `reason: DeploymentCompleted`

It will also update the Ready condition with the following properties:

* `type: Ready`
* `status: True`
* `reason: DeploymentCompleted`

#### Failed Supergraph deployment

If the deployment fails, the Operator will update the Progressing condition with the following properties:

* `type: Progressing`
* `status: False`
* `reason: DeploymentFailed`
