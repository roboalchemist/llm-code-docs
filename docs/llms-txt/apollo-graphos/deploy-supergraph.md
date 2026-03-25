# Source: https://www.apollographql.com/docs/apollo-operator/get-started/deploy-supergraph.md

# Deploy a Supergraph

In this guide, you will:

* Create a graph in GraphOS Studio
* Define a `SupergraphSchema` to compose your Subgraphs
* Deploy a `Supergraph` as a running GraphQL API

You will need:

* Apollo GraphOS Operator installed in your cluster (see [Install Operator](https://www.apollographql.com/docs/apollo-operator/get-started/install-operator))
* Subgraphs deployed and schemas loaded (see [Add Subgraphs](https://www.apollographql.com/docs/apollo-operator/get-started/add-subgraphs))

## 1. Create a graph in GraphOS Studio

The Apollo GraphOS Operator can publish and deploy graphs and graph variants from GraphOS Studio, but it cannot create new graphs. You can also use existing graphs with the Operator, however we strongly recommend to use a new graph for this tutorial.

Let's create a new graph in Studio to use as our base for supergraph publishes and deploys.

1. Navigate to [https://studio.apollographql.com/](https://studio.apollographql.com/) and log in.
2. Click on the **Add graph** button.
3. Click on **Connect an existing graph**.
4. Name your graph, then click on **Next**.
5. Take note of the graph ID, you should find it on a line starting with ` rover subgraph publish <graph ID>@current`.

## 2. Create a SupergraphSchema

The SupergraphSchema resource defines how your Subgraphs are composed into a supergraph. It specifies which Subgraphs to include and how they should be composed.

Open a new file named `supergraphschema.yaml` in your favorite IDE. Make sure to replace `<graph ID>` with the value obtained in step 1.

```yaml title=supergraphschema.yaml
apiVersion: apollographql.com/v1alpha2
kind: SupergraphSchema
metadata:
  name: retail
spec:
  selectors:
    - matchLabels:
        domain: retail
  graphRef: <graph ID>@current
```

In this schema, we are taking all the Subgraph resources that match the `retail` domain label and composing them together. The `graphRef` points to the graph we created in GraphOS Studio.

Now let's apply our resource and monitor its status:

```sh
kubectl apply -f supergraphschema.yaml
kubectl get supergraphschema retail -o yaml
```

After some time, you should see an **Available** condition showing the latest available schema. You can also navigate to `https://studio.apollographql.com/graph/<graph ID>/variant/current` to see your Operator-managed variant in Studio.

## 3. Deploy the supergraph

Now that you have a supergraph schema, you can deploy it into your cluster.

Open a `supergraph.yaml` file in your favorite IDE:

```yaml title=supergraph.yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: retail
spec:
  replicas: 2
  schema:
    resource:
      name: retail
  routerConfig:
    homepage:
      enabled: false
    sandbox:
      enabled: true
    supergraph:
      introspection: true
  podTemplate:
    routerVersion: 2.4.0
```

Apply the resource and wait for a **Ready** condition:

```sh
kubectl apply -f supergraph.yaml
kubectl get supergraph retail -o yaml
```

## 4. Test your supergraph

Finally, forward the port to your supergraph.

```text
kubectl port-forward deployment/retail 4000:4000
```

Then navigate to \[http\://localhost:4000/]. You should now see the Apollo Sandbox for your Operator-managed Supergraph!

## Configuration options

### Direct graph reference

You can also deploy a supergraph that references a GraphOS graph directly:

```yaml title=supergraph.yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: retail
spec:
  replicas: 2
  schema:
    graphRef: your-graph-name@current
  routerConfig:
    sandbox:
      enabled: true
  podTemplate:
    routerVersion: 2.4.0
```

### Multiple subgraph selectors

You can use multiple selectors to include subgraphs from different groups:

```yaml title=supergraphschema.yaml
spec:
  selectors:
    - matchLabels:
        domain: retail
    - matchLabels:
        environment: production
```

## Safe deployments

By default, the `Supergraph` uses a standard [Kubernetes Deployment with the RollingUpdate](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-update-deployment) strategy, which gradually replaces pods (typically 25% at a time). For production workloads, use *safe deployments* to enable:

* **Canary deployments**: Gradually shift traffic to new versions
* **Automated analysis**: Run tests and checks before promoting new versions
* **Automatic rollback**: Revert to previous versions if issues are detected

For more details, see the [Safe Deployments](https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts) guide.

## Next steps

You're all done! You have successfully composed and deployed a supergraph using the Apollo GraphOS Operator.

Looking to go further? Here are some next steps:

* [Explore different ways of defining your subgraphs](https://www.apollographql.com/docs/apollo-operator/resources/subgraph)
* [Customize your supergraph deployment](https://www.apollographql.com/docs/apollo-operator/resources/supergraph)
* [Configure safe deployments](https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts) for production workloads
