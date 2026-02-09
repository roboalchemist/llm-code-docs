# Source: https://docs.datadoghq.com/containers/autoscaling.md

---
title: Kubernetes Autoscaling
description: >-
  Automatically scale Kubernetes workloads using Datadog metrics and intelligent
  scaling recommendations
breadcrumbs: Docs > Containers > Kubernetes Autoscaling
---

# Kubernetes Autoscaling

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="info" %}
This feature is not available for the Datadog for Government (US1-FED) site.
{% /alert %}


{% /callout %}

Datadog Kubernetes Autoscaling continuously monitors your Kubernetes resources to provide immediate scaling recommendations and multidimensional autoscaling of your Kubernetes workloads. You can deploy autoscaling through the Datadog web interface, or with a `DatadogPodAutoscaler` custom resource.

## How it works{% #how-it-works %}

Datadog uses real-time and historical utilization metrics and event signals from your existing Datadog Agents to make recommendations. You can then examine these recommendations and choose to deploy them.

By default, Datadog Kubernetes Autoscaling uses estimated CPU and memory cost values to show savings opportunities and impact estimates. You can also use Kubernetes Autoscaling alongside Cloud Cost Management to get reporting based on your exact instance type costs.

Automated workload scaling is powered by a `DatadogPodAutoscaler` custom resource that defines scaling behavior on a per-workload level. The Datadog Cluster Agent acts as the controller for this custom resource.

Each cluster can have a maximum of 1000 workloads optimized with Datadog Kubernetes Autoscaler.

### Compatibility{% #compatibility %}

- **Distributions**: This feature is compatible with all of Datadog's [supported Kubernetes distributions](https://docs.datadoghq.com/containers/kubernetes/distributions).
- **Workload autoscaling**: This feature is an alternative to Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA). Datadog recommends that you remove any HPAs or VPAs from a workload when enabling Datadog Kubernetes Autoscaling to optimize it. These workloads are identified in the application on your behalf. **Note:** You can experiment with Datadog Kubernetes Autoscaling while keeping your HPA and/or VPA by creating a `DatadogPodAutoscaler` with `mode: Preview` in the `applyPolicy` section.

### Requirements{% #requirements %}

- [Remote Configuration](https://docs.datadoghq.com/agent/remote_config) must be enabled both at the organization level and on the Agents in your target cluster. See [Enabling Remote Configuration](https://docs.datadoghq.com/agent/remote_config/?tab=configurationyamlfile#enabling-remote-configuration) for setup instructions.

- [Helm](https://helm.sh/), for updating your Datadog Agent.

- (For Datadog Operator users) [`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/), for updating the Datadog Agent.

- When you are using live autoscaling, Datadog recommends using the latest Datadog Agent version. This helps ensure access to the latest improvements and optimizations. Scaling recommendations require the [Kubernetes State Core](https://docs.datadoghq.com/integrations/kubernetes_state_core/) integration to be enabled.

| Feature                                                                                                            | Minimum Agent Version |
| ------------------------------------------------------------------------------------------------------------------ | --------------------- |
| In-app workload scaling recommendations                                                                            | 7.50+                 |
| Live workload scaling                                                                                              | 7.66.1+               |
| Argo Rollout recommendations and autoscaling                                                                       | 7.71+                 |
| Cluster autoscaling ([preview sign-up](https://www.datadoghq.com/product-preview/kubernetes-cluster-autoscaling/)) | 7.72+                 |

- The following user permissions:

  - Org Management (required for Remote Configuration)
  - API Keys Write (required for Remote Configuration)
  - Workload Scaling Write
  - Autoscaling Manage

- (Recommended) Linux kernel v5.19+ and cgroup v2

## Setup{% #setup %}

{% tab title="Datadog Operator" %}

1. Ensure you are using Datadog Operator v1.16.0+. To upgrade your Datadog Operator:

```shell
helm upgrade datadog-operator datadog/datadog-operator
```
Add the following to your `datadog-agent.yaml` configuration file:
```yaml
spec:
  features:
    autoscaling:
      workload:
        enabled: true
    eventCollection:
      unbundleEvents: true
  override:
    clusterAgent:
      env:
        - name: DD_AUTOSCALING_FAILOVER_ENABLED
          value: "true"
    nodeAgent:
      env:
        - name: DD_AUTOSCALING_FAILOVER_ENABLED
          value: "true"
```
[Admission Controller](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/) is enabled by default with the Datadog Operator. If you disabled it, re-enable it by adding the following highlighted lines to `datadog-agent.yaml`:
```yaml
...
spec:
  features:
    admissionController:
      enabled: true
...
```
Apply the updated `datadog-agent.yaml` configuration:
```shell
kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
```

{% /tab %}

{% tab title="Helm" %}

1. Ensure you are using Agent and Cluster Agent v7.66.1+. Add the following to your `datadog-values.yaml` configuration file:

```yaml
datadog:
  autoscaling:
    workload:
      enabled: true
  kubernetesEvents:
    unbundleEvents: true
```
[Admission Controller](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/) is enabled by default in the Datadog Helm chart. If you disabled it, re-enable it by adding the following highlighted lines to `datadog-values.yaml`:
```yaml
...
clusterAgent:
  admissionController:
    enabled: true
...
```
Update your Helm version:
```shell
helm repo update
```
Redeploy the Datadog Agent with your updated `datadog-values.yaml`:
```shell
helm upgrade -f datadog-values.yaml <RELEASE_NAME> datadog/datadog
```

{% /tab %}

### Idle cost and savings estimates{% #idle-cost-and-savings-estimates %}

{% tab title="With Cloud Cost Management" %}
If [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management) is enabled within an org, Datadog Kubernetes Autoscaling shows idle cost and savings estimates based on your exact bill cost of underlying monitored instances.

See Cloud Cost setup instructions for [AWS](https://docs.datadoghq.com/cloud_cost_management/aws), [Azure](https://docs.datadoghq.com/cloud_cost_management/azure), or [Google Cloud](https://docs.datadoghq.com/cloud_cost_management/google_cloud).

Cloud Cost Management data enhances Kubernetes Autoscaling, but it is not required. All of Datadog's workload recommendations and autoscaling decisions are valid and functional without Cloud Cost Management.
{% /tab %}

{% tab title="Default" %}
If Cloud Cost Management is **not** enabled, Datadog Kubernetes Autoscaling shows idle cost and savings estimates using the following formulas and fixed values:

**Cluster idle**:

```
  (cpu_capacity - max(cpu_usage, cpu_requests)) * core_rate_per_hour
+ (mem_capacity - max(mem_usage, mem_requests)) * memory_rate_per_hour
```

**Workload idle**:

```
  (max(cpu_usage, cpu_requests) - cpu_usage) * core_rate_per_hour
+ (max(mem_usage, mem_requests) - mem_usage) * memory_rate_per_hour
```

**Fixed values**:

- core_rate_per_hour = $0.0295 per CPU core hour
- memory rate_per_hour = $0.0053 per memory GB hour

*Fixed cost values are subject to refinement over time.*
{% /tab %}

## Usage{% #usage %}

### Identify resources to rightsize{% #identify-resources-to-rightsize %}

The [Autoscaling Summary page](https://app.datadoghq.com/orchestration/scaling/summary) provides a starting point for platform teams to understand the total Kubernetes Resource savings opportunities across an organization, and filter down to key clusters and namespaces. The [Cluster Scaling view](https://app.datadoghq.com/orchestration/scaling/cluster) provides per-cluster information about total idle CPU, total idle memory, and costs. Click on a cluster for detailed information and a table of the cluster's workloads. If you are an individual application or service owner, you can also filter by your team or service name directly from the [Workload Scaling list view](https://app.datadoghq.com/orchestration/scaling/workload).

Click **Optimize** on any workload to see its scaling recommendation.

### Enable Autoscaling for a workload{% #enable-autoscaling-for-a-workload %}

After you identify a workload to optimize, Datadog recommends inspecting its **Scaling Recommendation**. You can also click **Configure Recommendation** to add constraints or adjust target utilization levels.

When you are ready to proceed with enabling Autoscaling for a workload, you have two options for deployment:

- Click **Enable Autoscaling**. (Requires Workload Scaling Write permission.)

Datadog automatically installs and configures autoscaling for this workload on your behalf.

- Deploy a `DatadogPodAutoscaler` custom resource.

Use your existing deploy process to target and configure Autoscaling for your workload.

  {% collapsible-section #id-for-anchoring %}
  Example DatadogPodAutoscaler CRD: 
  ```yaml
  apiVersion: datadoghq.com/v1alpha2
  kind: DatadogPodAutoscaler
  metadata:
    name: <name, usually same as Deployment object name>
  spec:
    targetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: <your Deployment name>
    constraints:
      # Adjust constraints as safeguards
      maxReplicas: 50
      minReplicas: 1
    owner: Local
    applyPolicy:
      mode: Apply
    objectives:
      - type: PodResource
        podResource:
          name: cpu
          value:
            type: Utilization
            utilization: 75
  ```

    {% /collapsible-section %}

### Deploy recommendations manually{% #deploy-recommendations-manually %}

As an alternative to Autoscaling, you can also deploy Datadog's scaling recommendations manually. When you configure resources for your Kubernetes deployments, use the values suggested in the scaling recommendations. You can also click **Export Recommendation** to see a generated `kubectl patch` command.

## Further reading{% #further-reading %}

- [Optimize Kubernetes workloads with Custom Query Scaling](https://www.datadoghq.com/blog/kubernetes-custom-query-autoscaling)
- [Centralize and govern your OpenTelemetry pipeline with the DDOT gateway](https://www.datadoghq.com/blog/ddot-gateway)
- [Rightsize workloads and reduce costs with Datadog Kubernetes Autoscaling](https://www.datadoghq.com/blog/datadog-kubernetes-autoscaling/)
- [Kubernetes Resource Utilization](https://docs.datadoghq.com/infrastructure/containers/kubernetes_resource_utilization)
- [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions)
- [Remote Configuration](https://docs.datadoghq.com/agent/remote_config/)
