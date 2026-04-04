# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraphschema.md

# SupergraphSchema resources

Once you have created [Subgraph](https://www.apollographql.com/docs/apollo-operator/resources/subgraph) resources to define your subgraph schemas, you can compose them together using **SupergraphSchema** resources. The Apollo GraphOS Operator will then automatically send subgraph changes to the [GraphOS Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api) and monitor supergraph builds.

**SupergraphSchema** resources work by matching label selectors against known resources.

```yaml
apiVersion: apollographql.com/v1alpha2
kind: SupergraphSchema
metadata:
  name: my-supergraph
spec:
  # Selectors for matching Subgraph resources
  selectors:
    - matchLabels:
        domain: my-supergraph
    - matchLabels:
        subgraph: my-subgraph
  # Graph variant used in Apollo GraphOS Studio
  graphRef: my-supergraph@my-variant
```

## Using Subgraph selectors

The **SupergraphSchema** resource type supports selecting Subgraphs using a list of [label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). Each item in that list will be used to match subgraphs independently, acting as a logical **OR** between list items. Within an item, the Operator will combine every label (using matchLabels) and expression (using matchExpressions) using a local **AND**.

For example, if you have a set of subgraphs with the following labels:

| **Name\Label** | **domain** | **team**   | **service** | **version** |
| -------------- | ---------- | ---------- | ----------- | ----------- |
| **Orders**     | retail     | andromeda  | orders      | 3           |
| **Products**   | retail     | betelgeuse | products    |             |
| **Reviews**    | retail     | betelgeuse | reviews     |             |
| **Revenue**    | finance    | cassiopeia | revenue     |             |

The following selectors configuration will match the **Orders** and **Products** subgraphs:

```yaml
spec:
  selectors:
    - matchLabels:
        team: betelgeuse
        service: products
    - matchLabels:
        domain: retail
      matchExpression:
        - { key: version, operator: Exists }
```

The following selectors configuration will match the **Orders**, **Products**, and **Reviews** subgraphs:

```yaml
spec:
  selectors:
    - matchLabels:
        domain: retail
```

### Removing subgraphs

By default, when you remove a **Subgraph** resource matched by a **SupergraphSchema**'s selectors, it will automatically remove the subgraph from your graph variant.

This does not apply when using the partial option on the SupergraphSchema.

### Debouncing frequent changes

By default, the Apollo GraphOS Operator will debounce changes with a wait period of five seconds to avoid sending many composition requests if you are performing multiple changes at once.

You can customize the debounce period in the Operator configuration.

### Triggering and disabling compositions

When the Operator detects any change to the set of **Subgraph** resources that match the **SupergraphSchema**'s selectors, it will automatically trigger a new composition in GraphOS Studio and wait on its results.

If you do not want to trigger a composition at this time, for example because you are awaiting changes across multiple subgraphs, or you want to make sure the Operator detects your subgraphs correctly, you can temporarily pause compositions by setting `compositionEnabled: false` on the SupergraphSchema specification:

```yaml
spec:
  compositionEnabled: false
```

When you want to re-enable compositions, you can remove the `compositionEnabled: false` property.

### Partial SupergraphSchema

You may be adopting the Apollo GraphOS Operator for existing workloads, or might have subgraphs in other Kubernetes clusters or defined outside of Kubernetes.

For these cases, you can mark your SupergraphSchema resource with `partial: true`. The Apollo GraphOS Operator will not remove or modify subgraphs it does not recognize.

```yaml
spec:
  partial: true
```

By default, `partial` is `false`.

Please note that when you are using a partial SupergraphSchema, you cannot use it as a schema source for [Supergraph](https://www.apollographql.com/docs/apollo-operator/supergraph) resources.

## Deletion policy

When you delete a **SupergraphSchema** resource, you can control what happens to the corresponding graph variant in Apollo GraphOS Studio using the `deletionPolicy` field.

The deletion policy has two options:

* **`KeepVariant`** (default): The graph variant in Apollo GraphOS Studio will be preserved when the SupergraphSchema resource is deleted.
* **`DeleteVariant`**: The graph variant in Apollo GraphOS Studio will be deleted when the SupergraphSchema resource is deleted.

```yaml
spec:
  deletionPolicy: DeleteVariant
```

If you don't specify a deletion policy, the default behavior is to keep the variant (`KeepVariant`).

## Monitoring SupergraphSchema resources

The Apollo GraphOS Operator will monitor changes in your SupergraphSchema resource and reflect them in the resource status. These changes can happen either because you have changed the SupergraphSchema spec, or there is an update to the set of matching Subgraphs.

It will reflect the state of your resource using three **status conditions** types:

* **SubgraphsDetected**: Tracking which subgraphs were detected for the SupergraphSchema selectors, and their latest schema hashes.
* **CompositionPending**: Tracking the state of the latest composition request.
* **Available**: Latest graph artifact available.

### Monitoring Subgraph detection

The Operator will store a **SubgraphsDetected** condition containing a list of names, namespaces, and hashes for each subgraph it has detected matching the following properties:

* `type: SubgraphsDetected`
* `status: True`
* `reason: SubgraphsDetected`

Here is what a sample **SubgraphsDetected** condition may look like for a schema with 3 subgraphs:

```yaml
status:
  conditions:
    - lastTransitionTime: "2025-04-15T09:30:00Z"
      message: Found 3 matching subgraph(s)
      observedGeneration: 27
      reason: SubgraphsDetected
      type: SubgraphsDetected
      subgraphs:
        - name: comments
          namespace: default
          schema:
            sdlHash: sha256:95ca4b9acfba39511cfdcbbc3144875d5130220ca82a09db863ab27316814807
        - name: media
          namespace: default
          schema:
            sdlHash: sha256:d5a041961a1f004a2e834e79a8fd0bbff691cce2c50cabb82c1d7623ae02efcb
        - name: ratings
          namespace: default
          schema:
            sdlHash: sha256:94d1dcb533792c0ae22401c4416767761d4d4c921b4fa5cce120a5ec7e5e2ac8
      status: "True"
```

### Monitoring build results

Once the Operator triggers a new composition, it will automatically monitor its state and will report back using the **CompositionPending** and **Available** conditions, which contain both the set of subgraphs and information about the composition request (its graphRef and launchId).

#### Composition pending

When a composition is pending, the Operator will set the **CompositionPending** condition with the following properties:

* `type: CompositionPending`
* `status: True`
* `reason: CompositionRequested`

#### Composition failed

When a composition fails, the Operator will set the **CompositionPending** condition with the following properties:

* `type: CompositionPending`
* `status: False`
* `reason: InvalidGraphRef | reason: MalformedSchema | reason: Superseded | reason: Unknown`

#### Composition completed

When a composition succeeds, the Operator will set the **CompositionPending** with the following properties:

* `type: CompositionPending`
* `status: True`
* `reason: CompositionCompleted`

Furthermore, it will update the **Available** condition with the latest metadata to retrieve the matching supergraph schema, and with the following properties:

* `type: Available`
* `status: True`
* `reason: CompositionCompleted`
