# Source: https://www.apollographql.com/docs/apollo-operator/resources/subgraph.md

# Subgraph resources

When using the Apollo GraphOS Operator, you can define subgraphs as a set of **Subgraph** resources in your Kubernetes cluster, then combine them together using [SupergraphSchema](https://www.apollographql.com/docs/apollo-operator/supergraphschema) resources. The Operator will then automatically track and publish subgraph changes to Apollo GraphOS Studio.

## Defining a Subgraph

You can define a subgraph using the **Subgraph** resource type, deployed closed to your subgraph implementation (for example, the set of Kubernetes Service, Deployment, and other resources that constitute the actual implementation for that subgraph).

```yaml
apiVersion: apollographql.com/v1alpha2
kind: Subgraph
metadata:
  name: my-subgraph
  namespace: my-namespace
  labels:
    subgraph: my-subgraph
spec:
  endpoint: http://my-subgraph.my-namespace.svc.cluster.local
  schema:
    sdl: |
      type Query {
        hello: String
      }
```

The Subgraph resource type allows you to define your schema in three different ways:

* As an in-line SDL (see example above).
* As a GraphQL schema file in an OCI container image.
* As an OCI artifact.

### Using an OCI container image

To ensure that your subgraph schema and implementation stay in sync, we recommend you to store your schema in the same container image as your subgraph implementation.

You can then specify the image and path as the source of your schema:

```yaml
spec:
  # OCI Image schema source
  schema:
    ociImage:
      reference: {YOUR_REGISTRY}/{YOUR_REPOSITORY}/{TAG}
      path: /schema.graphql
```

### Using an Apollo-compatible OCI artifact

The Operator can load Subgraph schemas as OCI artifact using the `application/vnd.apollographql.schema` file type. To create an OCI artifact using the right content type, we recommend using the oras CLI as such:

```bash
oras push $YOUR_REGISTRY/$YOUR_REPOSITORY:$TAG \
     --artifact-type application/vnd.apollographql.schema \
     $FILENAME:application/vnd.apollographql.schema
```

You can then use an OCI reference as the source of your schema:

```yaml
spec:
  # OCI artifact schema source
  schema:
    oci:
      reference: {YOUR_REGISTRY}/{YOUR_REPOSITORY}/{TAG}
```

## Monitoring Subgraph resources

The Apollo GraphOS Operator will monitor changes in your Subgraph resource and reflect them in the resource status. These changes can happen either because you have changed the Supergraph spec or it detected a new version of your subgraph schema.

It will reflect the state of your resource using a **SchemaLoaded** condition.

```yaml
status:
  conditions:
    - type: "SchemaLoaded"
      status: "True"
      reason: "Loaded"
      observedGeneration: 3
      schema:
        ociImage:
          sdlHash: "sha256:{some hash}"
          updatedAt: "2025-07-03T12:34:56Z"
```

If the Operator successfully loaded a subgraph schema, it will have a condition with the following values:

* `type: SchemaLoaded`
* `status: True`
* `reason: Loaded`

On the other hand, if the Operator fail to load the subgraph schema, it will have a condition with the following values:

* `type: SchemaLoaded`
* `status: False`
* `reason: MissingData | reason: FetchError | reason: InvalidSpec`

## Composing Subgraphs into a SupergraphSchema

Now that you have defined your subgraphs as a set of Kubernetes resources, you can create [SupergraphSchema](https://www.apollographql.com/docs/apollo-operator/supergraphschema) resources to compose them into supergraph schemas.
