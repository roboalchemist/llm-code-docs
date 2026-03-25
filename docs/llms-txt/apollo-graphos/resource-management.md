# Source: https://www.apollographql.com/docs/graphos/routing/self-hosted/resource-management.md

# Managing GraphOS Router Resources in Kubernetes

Self-hosting the GraphOS Router requires a current GraphOS [Enterprise or Free plan](https://www.apollographql.com/pricing).

Determining the correct resource requests and limits for your application pods in a Kubernetes system is not an exact science. Your specific needs depend on many factors, including:

* The cardinality of unique operation shapes
* The latency of underlying subgraphs and data sources
* The size of responses
* The complexity of query plans

Our general recommendation for Kubernetes is to start with these requests and limits:

```yaml
resources:
  requests:
    memory: '1G'
    cpu: '1000m'
  limits:
    memory: '2G'
    # no CPU limit to avoid throttling
```

The [router resource estimator](https://www.apollographql.com/docs/graphos/routing/self-hosted/resource-estimator) is a helpful tool for getting a starting baseline for what resources you may need in production based on your expected traffic.

When using [Horizontal pod autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/), we recommend targeting 90% utilization:

```yaml
metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 90
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 90
```

The GraphOS Router starts up quickly, but when connected to GraphOS the router has to fetch the supergraph schema from Apollo Uplink before it can start serving traffic. We recommend measuring your router's startup time and lowering the `averageUtilization` if your startup time is longer due to Uplink latency or the size of your supergraph schema.
