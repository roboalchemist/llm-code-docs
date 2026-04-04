# Source: https://docs.vespa.ai/en/basics/operations.html.md

# Source: https://docs.vespa.ai/en/operations/enclave/operations.html.md

# Source: https://docs.vespa.ai/en/operations/kubernetes/operations.html.md

# Lifecycle Operations for Vespa on Kubernetes

 

The ConfigServer and Vespa Application Pods have built-in resilience and recovery capabilities; they are automatically recovered during failures and gracefully shut down during maintenance or scaling operations to preserve data integrity.

### Automatic Recovery

Vespa relies on standard Kubernetes controllers to detect and restart crashed Pods. If a container exits unexpectedly (e.g., OOMKilled or application crash), the kubelet will automatically restart it.

However, the ConfigServers track the health history of every Pod. To prevent a "crash loop" from causing cascading failures or constantly churning resources, the system implements a strict throttling mechanism. The ConfigServers allow a maximum of 2 involuntary Pod disruptions per 24-hour period for a given Vespa Application. If this limit is exceeded, the ConfigServer stops automatically failing these Pods and will require human intervention to investigate the root cause.

### Graceful Shutdown

To prevent query failures or data loss during termination, a [PreStop Hook](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) is placed on every ConfigServer and Vespa Application Pod. During a voluntary disruption, this hook ensures that existing traffic is drained and that data is flushed before killing the Pod.

Two types of disruptions exist in Kubernetes:

| Type | Scenario | Behavior |
| --- | --- | --- |
| **Voluntary Disruption** | Scaling down, rolling upgrades, or node maintenance. | The preStop hook detects a voluntary disruption, stops the Vespa Container cluster from accepting new traffic, flushes in-memory data to disk for Content clusters, and ensures a clean exit before the Pod is deleted. |
| **Involuntary Disruption** | Node hardware failure, kernel panic, or eviction. | Kubernetes initiates the termination. The preStop hook attempts to run to flush data and close connections. However, if the Pod is lost abruptly. the hook cannot run, and recovery relies on Vespa's data replication. |

### Availability Management (PodDisruptionBudgets)

Defining a `PodDisruptionBudget` (PBD) is not supported for Vespa on Kubernetes. The ConfigServer will override any PBD with its own orchestration policy, such as 2 involuntary Pod disruptions per 24 hours, and enforce it over the PDB.

 Copyright © 2026 - [Cookie Preferences](#)

