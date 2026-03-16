# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph/autoscalers.md

# Autoscaling your Supergraphs

**Supergraph** resources implement the [scale subresource](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#scale-subresource), allowing you to bring your preferred autoscalers.

## Examples

### HorizontalPodAutoscaler (v1)

```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: my-hpa
spec:
  scaleTargetRef:
    apiVersion: apollographql.com/v1alpha3
    kind: Supergraph
    name: my-supergraph
  minReplicas: 2
  maxReplicas: 8
  targetCPUUtilizationPercentage: 70
```

### HorizontalPodAutoscaler (v2)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-hpa
spec:
  scaleTargetRef:
    apiVersion: apollographql.com/v1alpha3
    kind: Supergraph
    name: my-supergraph
  minReplicas: 2
  maxReplicas: 8
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### KEDA

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: my-keda
spec:
  scaleTargetRef:
    apiVersion: apollographql.com/v1alpha3
    kind: Supergraph
    name: my-supergraph
  minReplicaCount: 2
  maxReplicaCount: 8
  triggers:
    - type: cpu
      metricType: Utilization
      metadata:
        value: "70"
```
