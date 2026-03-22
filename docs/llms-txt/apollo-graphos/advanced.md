# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts/advanced.md

# Advanced Safe Deployments

This guide covers advanced topics for safe deployments, including custom analysis options, networking integration, and migration strategies.

## Configure custom analysis

Argo Rollouts supports running automated analysis during your deployments. This enables you to run tests, check metrics, and validate the new version before promoting it.

### Configure analysis

You can configure analysis templates that run during specific steps of your rollout. Analysis runs during pauses to validate the new version before promoting it:

```yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: my-supergraph
spec:
  deploymentStrategy:
    rollout:
      steps:
        - setWeight: 20  # Shift 20% of traffic to new version
        - pause:
            duration: 5m  # Wait 5 minutes for analysis
        - analysis:  # Run analysis at this step
            templates:
              - templateName: success-rate  # Reference to AnalysisTemplate
        - setWeight: 50  # Shift 50% of traffic if analysis passes
        - pause:
            duration: 5m  # Wait 5 minutes for analysis
        - analysis:  # Run analysis again at higher traffic
            templates:
              - templateName: success-rate
        - setWeight: 100  # Promote to 100% if analysis passes
      analysis:  # Global analysis configuration - runs when the rollout reaches certain lifecycle events — typically at the start, completion, or during stable promotion
        templates:
          - templateName: success-rate  # AnalysisTemplate name
            args:  # Arguments passed to the template
              - name: service-name
                value: my-supergraph  # Supergraph name for metrics query
```

### Define analysis templates

Analysis templates must be defined as separate Kubernetes resources. Here's an example that checks for success rate using Prometheus metrics:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate  # Template name referenced in Supergraph
spec:
  metrics:
    - name: success-rate
      interval: 30s  # Check metrics every 30 seconds
      count: 5  # Run 5 checks (total 2.5 minutes)
      successCondition: result[0] >= 0.95  # Success if 95%+ requests succeed
      failureCondition: result[0] < 0.90  # Fail if less than 90% succeed
      provider:
        prometheus:
          address: http://prometheus:9090  # Prometheus server address
          query: |
            # Calculate success rate: non-5xx requests / total requests
            sum(rate(http_requests_total{service="{{args.service-name}}",status!~"5.."}[5m]))
            /
            sum(rate(http_requests_total{service="{{args.service-name}}"}[5m]))
```

For more information on analysis templates, see the [Argo Rollouts analysis documentation](https://argoproj.github.io/argo-rollouts/features/analysis/).

## Configure networking integration

When using safe deployments with Argo Rollouts, the operator automatically creates the necessary `Services` and manages traffic distribution. Both stable and canary `Services` are configured based on your `Supergraph`'s `networking` configuration.

### Service configuration

The operator automatically creates two Services for canary deployments:

* **Stable Service**: Points to the stable version of your Supergraph
* **Canary Service**: Points to the canary version during rollouts

Both services use the networking settings from your Supergraph's `spec.networking` configuration (ports, service type, etc.).

### Traffic splitting

Argo Rollouts uses these Services to split traffic between the stable and canary versions. The operator handles Service creation automatically, but you might need to configure your ingress or service mesh to route traffic appropriately.

For ingress-based traffic splitting, configure your ingress to route traffic to both Services based on your rollout strategy. If you're using a service mesh (Istio, Linkerd, etc.), Argo Rollouts can integrate with your mesh for traffic splitting.

Refer to the [Argo Rollouts traffic management documentation](https://argoproj.github.io/argo-rollouts/features/traffic-management/) for detailed configuration options.

## Migrate from Deployment to Rollout

If you have an existing `Supergraph` using a standard Kubernetes `Deployment`, you can migrate to a `Rollout` strategy with zero downtime.

### Perform a zero-downtime migration

To migrate from a Deployment to a Rollout without downtime, set `migrate: true` in your rollout configuration. The first time a Rollout is applied it will not run a Canary deployment.

```yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: my-supergraph
spec:
  replicas: 3  # Number of replicas
  podTemplate:
    routerVersion: 2.7.0  # GraphOS Router version
  deploymentStrategy:
    rollout:
      migrate: true  # Enable zero-downtime migration
      steps:
        - setWeight: 20  # Shift 20% of traffic to Rollout
        - pause:
            duration: 5m  # Wait before next step
        - setWeight: 50  # Shift 50% of traffic to Rollout
        - pause:
            duration: 5m  # Wait before next step
        - setWeight: 80  # Shift 80% of traffic to Rollout
        - pause:
            duration: 5m  # Wait before final step
        - setWeight: 100  # Shift all traffic to Rollout
  schema:
    studio:
      graphRef: my-graph@my-variant  # GraphOS graph variant reference
```

When `migrate: true` is set:

1. The operator creates a Rollout with a `workloadRef` pointing to your existing Deployment.
2. Once the Rollout is `Healthy`, the `Deployment` is scaled down to `0` replicas.
3. The operator automatically cleans up the `Deployment` after rollout completes.

This ensures zero downtime during the migration.

### Perform a standard migration

If you don't set `migrate: true`, the operator performs the following actions:

1. Create a new Rollout.
2. Delete the existing Deployment without waiting for Rollout to be `Healthy`.

This approach might cause a brief service interruption during the transition.

## Troubleshoot issues

### Handle a `Rollout` stuck in `Progressing`

If your `Rollout` is stuck in `Progressing` phase, check for pause conditions or manual approval requirements. The operator automatically creates the necessary `Services` for traffic splitting, but issues can arise from rollout configuration or Argo Rollouts setup.

For general Argo Rollouts troubleshooting, see the [Argo Rollouts troubleshooting documentation](https://argoproj.github.io/argo-rollouts/).

### Traffic not shifting

If traffic isn't shifting as expected, verify that Services are created correctly:

```sh
kubectl get svc
```

The operator automatically creates stable and canary Services based on your Supergraph's `networking` configuration. If Services aren't created, check that your Supergraph spec is valid and the operator is running correctly.

For ingress or service mesh configuration issues, refer to the [Argo Rollouts traffic management documentation](https://argoproj.github.io/argo-rollouts/features/traffic-management/).

## Explore next steps

* Learn more about [Argo Rollouts](https://argoproj.github.io/argo-rollouts/)
* Explore [Argo Rollouts traffic management](https://argoproj.github.io/argo-rollouts/features/traffic-management/) for advanced networking
