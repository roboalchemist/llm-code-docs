# Source: https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/

Title: Resource Strategy Fit Plugin User Guide | Volcano

URL Source: https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/

Published Time: 2026-02-03T00:00:00+00:00

Markdown Content:
Introduction[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#introduction)
-----------------------------------------------------------------------------------------------------------

The **Resource Strategy Fit Plugin** is a Volcano scheduler plugin that provides intelligent resource allocation strategies for pod scheduling. It supports both global configuration and pod-level annotations to optimize resource utilization across different workloads.

Key Features[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#key-features)
-----------------------------------------------------------------------------------------------------------

*   **Multiple Scoring Strategies**: Supports `LeastAllocated` and `MostAllocated` strategies
*   **Resource-Specific Configuration**: Configure different strategies for different resource types (CPU, Memory, GPU, etc.)
*   **Pod-Level Override**: Allow individual pods to override global configuration via annotations
*   **Weighted Scoring**: Fine-tune resource importance with configurable weights
*   **Wildcard Support**: Use wildcard patterns for resource matching

Installation[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#installation)
-----------------------------------------------------------------------------------------------------------

### 1. Install Volcano[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#1-install-volcano)

Refer to [Install Guide](https://github.com/volcano-sh/volcano/blob/master/installer/README.md) to install Volcano.

### 2. Configure the Plugin[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#2-configure-the-plugin)

Update the Volcano scheduler configuration:

```
kubectl edit cm -n volcano-system volcano-scheduler-configmap
```

Add the `resource-strategy-fit` plugin to your configuration:

```
kind: ConfigMap
apiVersion: v1
metadata:
  name: volcano-scheduler-configmap
  namespace: volcano-system
data:
  volcano-scheduler.conf: |
    actions: "reclaim, allocate, backfill, preempt"
    tiers:
    - plugins:
      - name: priority
      - name: gang
      - name: conformance
    - plugins:
      - name: drf
      - name: predicates
      - name: resource-strategy-fit
        arguments:
          resourceStrategyFitWeight: 10
          resources:
            cpu:
              type: "LeastAllocated"
              weight: 1
            memory:
              type: "LeastAllocated"
              weight: 1
            nvidia.com/gpu:
              type: "MostAllocated"
              weight: 2
```

Global Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#global-configuration)
---------------------------------------------------------------------------------------------------------------------------

### Basic Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#basic-configuration)

The plugin supports two main scoring strategies:

| Strategy | Description | Use Case |
| --- | --- | --- |
| `LeastAllocated` | Prefers nodes with more available resources | General workloads, load balancing |
| `MostAllocated` | Prefers nodes with higher resource utilization | GPU workloads, resource consolidation |

### Configuration Parameters[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#configuration-parameters)

```
arguments:
  resourceStrategyFitWeight: 10          # Plugin weight (default: 10)
  resources:                              # Resource-specific configuration
    cpu:                                 # Resource name
      type: "LeastAllocated"             # Scoring strategy
      weight: 1                          # Resource weight
    memory:
      type: "LeastAllocated"
      weight: 1
    nvidia.com/gpu:
      type: "MostAllocated"
      weight: 2
```

### Advanced Configuration Examples[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#advanced-configuration-examples)

#### 1. GPU-Optimized Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#1-gpu-optimized-configuration)

```
arguments:
  resourceStrategyFitWeight: 20
  resources:
    cpu:
      type: "LeastAllocated"
      weight: 1
    memory:
      type: "LeastAllocated"
      weight: 1
    nvidia.com/gpu:
      type: "MostAllocated"
      weight: 5
    nvidia.com/gpu/*:                     # Wildcard for all GPU types
      type: "MostAllocated"
      weight: 3
```

#### 2. Mixed Strategy Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#2-mixed-strategy-configuration)

```
arguments:
  resourceStrategyFitWeight: 15
  resources:
    cpu:
      type: "LeastAllocated"
      weight: 3
    memory:
      type: "MostAllocated"
      weight: 1
    example.com/custom-resource:
      type: "LeastAllocated"
      weight: 2
```

Pod-Level Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#pod-level-configuration)
---------------------------------------------------------------------------------------------------------------------------------

### Pod Annotations[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#pod-annotations)

Individual pods can override the global configuration using annotations:

| Annotation Key | Description | Example |
| --- | --- | --- |
| `volcano.sh/resource-strategy-scoring-type` | Override scoring strategy | `"LeastAllocated"` or `"MostAllocated"` |
| `volcano.sh/resource-strategy-weight` | Override resource weights | `{"cpu": 2, "memory": 1, "nvidia.com/gpu": 3}` |

### Pod-Level Examples[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#pod-level-examples)

#### 1. Override Strategy for Specific Pod[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#1-override-strategy-for-specific-pod)

```
apiVersion: v1
kind: Pod
metadata:
  name: gpu-workload
  annotations:
    volcano.sh/resource-strategy-scoring-type: "MostAllocated"
    volcano.sh/resource-strategy-weight: '{"nvidia.com/gpu": 5, "cpu": 1}'
spec:
  containers:
  - name: gpu-container
    image: nvidia/cuda:11.0-runtime
    resources:
      requests:
        nvidia.com/gpu: 1
        cpu: "2"
        memory: "4Gi"
      limits:
        nvidia.com/gpu: 1
        cpu: "2"
        memory: "4Gi"
  schedulerName: volcano
```

#### 2. Custom Resource Weights[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#2-custom-resource-weights)

```
apiVersion: v1
kind: Pod
metadata:
  name: custom-resource-pod
  annotations:
    volcano.sh/resource-strategy-scoring-type: "LeastAllocated"
    volcano.sh/resource-strategy-weight: '{"cpu": 3, "memory": 2, "example.com/custom": 5}'
spec:
  containers:
  - name: app
    image: my-app:latest
    resources:
      requests:
        cpu: "1"
        memory: "2Gi"
        example.com/custom: "1"
  schedulerName: volcano
```

Volcano Job Integration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#volcano-job-integration)
---------------------------------------------------------------------------------------------------------------------------------

### Basic Volcano Job[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#basic-volcano-job)

```
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: resource-strategy-job
spec:
  minAvailable: 2
  schedulerName: volcano
  plugins:
    env: []
    svc: []
  tasks:
  - replicas: 2
    name: worker
    template:
      metadata:
        annotations:
          volcano.sh/resource-strategy-scoring-type: "LeastAllocated"
          volcano.sh/resource-strategy-weight: '{"cpu": 2, "memory": 1}'
      spec:
        containers:
        - name: worker
          image: my-worker:latest
          resources:
            requests:
              cpu: "2"
              memory: "4Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
        restartPolicy: Never
```

### Multi-Task Job with Different Strategies[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#multi-task-job-with-different-strategies)

```
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: mixed-strategy-job
spec:
  minAvailable: 3
  schedulerName: volcano
  plugins:
    env: []
    svc: []
  tasks:
  - replicas: 1
    name: gpu-task
    template:
      metadata:
        annotations:
          volcano.sh/resource-strategy-scoring-type: "MostAllocated"
          volcano.sh/resource-strategy-weight: '{"nvidia.com/gpu": 5, "cpu": 1}'
      spec:
        containers:
        - name: gpu-worker
          image: gpu-app:latest
          resources:
            requests:
              nvidia.com/gpu: 1
              cpu: "1"
              memory: "2Gi"
  - replicas: 2
    name: cpu-task
    template:
      metadata:
        annotations:
          volcano.sh/resource-strategy-scoring-type: "LeastAllocated"
          volcano.sh/resource-strategy-weight: '{"cpu": 3, "memory": 2}'
      spec:
        containers:
        - name: cpu-worker
          image: cpu-app:latest
          resources:
            requests:
              cpu: "2"
              memory: "4Gi"
```

Use Cases[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#use-cases)
-----------------------------------------------------------------------------------------------------

### 1. GPU Workload Optimization[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#1-gpu-workload-optimization)

For GPU-intensive workloads, use `MostAllocated` strategy to consolidate GPU usage:

```
# Global configuration
arguments:
  resourceStrategyFitWeight: 20
  resources:
    nvidia.com/gpu:
      type: "MostAllocated"
      weight: 5
    cpu:
      type: "LeastAllocated"
      weight: 1
```

### 2. Load Balancing[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#2-load-balancing)

For general workloads, use `LeastAllocated` strategy to distribute load evenly:

```
# Global configuration
arguments:
  resourceStrategyFitWeight: 10
  resources:
    cpu:
      type: "LeastAllocated"
      weight: 2
    memory:
      type: "LeastAllocated"
      weight: 1
```

### 3. Mixed Workloads[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#3-mixed-workloads)

Combine different strategies for different resource types:

```
# Global configuration
arguments:
  resourceStrategyFitWeight: 15
  resources:
    cpu:
      type: "LeastAllocated"
      weight: 3
    memory:
      type: "LeastAllocated"
      weight: 2
    nvidia.com/gpu:
      type: "MostAllocated"
      weight: 5
```

Troubleshooting[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#troubleshooting)
-----------------------------------------------------------------------------------------------------------------

### Verify Plugin Configuration[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#verify-plugin-configuration)

Check the scheduler logs to ensure the plugin is loaded correctly:

```
kubectl logs -n volcano-system deployment/volcano-scheduler | grep "resource-strategy-fit"
```

Expected output:

```
Initialize resource-strategy-fit plugin with configuration: {resourceStrategyFitWeight: 10, resources: {...}}
```

### Common Issues[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#common-issues)

1.   **Plugin not loaded**: Ensure the plugin is included in the scheduler configuration
2.   **Invalid annotations**: Check JSON format for pod-level weight annotations
3.   **Resource not found**: Verify resource names match exactly (case-sensitive)
4.   **Scoring not working**: Check plugin weight and resource weights are properly configured

### Debug Information[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#debug-information)

Enable debug logging to see scoring decisions:

```
# Add to scheduler configuration
arguments:
  resourceStrategyFitWeight: 10
  # ... other configuration
  logLevel: 4  # Enable debug logging
```

Best Practices[](https://volcano.sh/en/docs/user-guide/how_to_use_resource_strategy_fit_plugin/#best-practices)
---------------------------------------------------------------------------------------------------------------

1.   **Start with global configuration** for consistent behavior across all workloads
2.   **Use pod-level annotations sparingly** for specific workload requirements
3.   **Test different strategies** to find optimal configuration for your use case
4.   **Monitor resource utilization** after applying the plugin
5.   **Use appropriate weights** to balance different resource types
6.   **Consider workload characteristics** when choosing between `LeastAllocated` and `MostAllocated`
