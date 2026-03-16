# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraphset.md

# SupergraphSet resources

**SupergraphSet** is a Kubernetes resource that allows you to automatically create and manage multiple [Supergraph](https://www.apollographql.com/docs/apollo-operator/resources/supergraph) resources based on graph variants in Apollo Studio. Instead of manually creating individual Supergraph resources for each variant, you can define a template and let the Operator handle the creation and lifecycle management.

**Warning**: SupergraphSet support is currently experimental.

## Defining a SupergraphSet

You can define a SupergraphSet using the **SupergraphSet** resource type. The SupergraphSet will automatically create Supergraph resources for all matching graph variants in Apollo Studio.

```yaml
apiVersion: apollographql.com/v1alpha3
kind: SupergraphSet
metadata:
  name: my-supergraph-set
spec:
  # Schema source for the SupergraphSet
  schema:
    studio:
      graphId: my-graph
      includeVariants:
        - named: production
        - named: staging
      excludeVariants:
        - named: development
  # Template for the underlying Supergraph resources
  supergraphTemplate:
    replicas: 2
    podTemplate:
      routerVersion: "2.4.0"
    routerConfig:
      homepage:
        enabled: true
      sandbox:
        enabled: true
      supergraph:
        introspection: true
```

## Specifying a schema source

The SupergraphSet resource type currently supports Apollo Studio as the schema source. You specify a **graphId** and optionally filter which variants to include or exclude.

### Apollo Studio

You can specify a graph ID reference and filter variants using include/exclude patterns.

```yaml
spec:
  schema:
    studio:
      graphId: my-graph
      includeVariants:
        - named: production
        - named: staging
      excludeVariants:
        - named: development
```

The `includeVariants` and `excludeVariants` fields support two types of patterns:

* **Named patterns**: Exact name matching
* **Matching patterns**: Regex-based matching

For example, to include all variants that start with "prod-" and exclude any that contain "test":

```yaml
spec:
  schema:
    studio:
      graphId: my-graph
      includeVariants:
        - matching: "^prod-"
      excludeVariants:
        - matching: "test"
```

If no `includeVariants` are specified, all variants for the graph will be included (subject to any `excludeVariants`).

## Supergraph template

The `supergraphTemplate` field defines how each Supergraph resource should be configured. This template is applied to all Supergraphs created by the SupergraphSet.

```yaml
spec:
  supergraphTemplate:
    replicas: 2
    podTemplate:
      routerVersion: "2.4.0"
    routerConfig:
      homepage:
        enabled: true
      sandbox:
        enabled: true
      supergraph:
        introspection: true
```

The template supports all the same configuration options as individual [Supergraph](https://www.apollographql.com/docs/apollo-operator/supergraph) resources except for schema sources.

## Suspending SupergraphSet operations

You can temporarily suspend the SupergraphSet to prevent it from creating or deleting Supergraph resources. This is useful when you want to make manual changes or temporarily stop automatic management.

```yaml
spec:
  suspend: true
```

When suspended, the SupergraphSet will:

* Stop creating new Supergraph resources for new variants
* Stop deleting Supergraph resources for removed variants

To re-enable automatic management, remove the `suspend: true` property or set it to `false`.

## Monitoring SupergraphSet resources

The Apollo GraphOS Operator will monitor changes in your SupergraphSet resource and reflect them in the resource status. These changes can happen either because you have changed the SupergraphSet spec or there are changes to the matching graph variants in Apollo Studio.

It will reflect the state of your resource using the **graphRefs** field in the status:

```yaml
status:
  studio:
    graphRefs:
      - my-graph@production
      - my-graph@staging
```

The status shows all graph references that match the SupergraphSet's schema configuration and are currently being managed.

### Monitoring Supergraph creation and deletion

The SupergraphSet controller will automatically:

* Create new Supergraph resources for graph variants that match the schema configuration
* Delete Supergraph resources for graph variants that no longer match
* Update the status with the current list of matching graph references

Each Supergraph created by the SupergraphSet will have:

* A name generated from the SupergraphSet name and a hash of the graph reference
* Owner references pointing back to the SupergraphSet
* The same labels and annotations as the SupergraphSet
* Configuration based on the `supergraphTemplate`

You can monitor the individual Supergraph resources to see their deployment status, just like any other Supergraph resource.
