# Source: https://docs.datadoghq.com/containers/monitoring/kubernetes_resource_utilization.md

---
title: Kubernetes Resource Utilization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Containers > Container Monitoring > Kubernetes Resource Utilization
---

# Kubernetes Resource Utilization

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/kubernetes_resource_utilization.758f880f3f5e365fa2c62650f03e87f9.png?auto=format"
   alt="Kubernetes resource utilization view" /%}

Datadog's [Kubernetes resource utilization](https://app.datadoghq.com/orchestration/resource/pod?groups=tag%23kube_deployment%2Ctag%23kube_namespace%2Ctag%23kube_cluster_name) view gives you insights into how your Kubernetes workloads are using your computing resources across your infrastructure. This helps you to understand resource usage and make better decisions about sizing and capacity planning, as well as reducing the amount of CPU or memory waste.

With a constantly-updated status of how well your resource requests and limits match your pods' current usage, you can improve bin packing within your Kubernetes clusters.

## Prerequisites{% #prerequisites %}

- Datadog Agent v7.45.0+
- Enable [Kubernetes Explorer](https://docs.datadoghq.com/containers/monitoring/kubernetes_explorer)

## Usage{% #usage %}

In Datadog, go to the [**Kubernetes Overview** page](https://app.datadoghq.com/kubernetes) and select the [**Resource Utilization** tab](https://app.datadoghq.com/orchestration/resource/pod?groups=tag%23kube_deployment%2Ctag%23kube_namespace%2Ctag%23kube_cluster_name).

The page opens on **Pods**, with a default grouping by `kube_cluster_name`, `kube_namespace`, and `kube_deployment`.

Optimizing the sizing for CPU and memory is typically done separately. Data in the table is split between a **CPU** and a **Memory** toggle.

#### Default columns{% #default-columns %}

{% tab title="CPU" %}

- **Pod group**: Represents deployments by default, but depends on what you specify in the **Group by** field in the upper right. This column includes the sum of usage, requests, and limits for the pods in each group.
- **CPU idle**: Amount of unused CPU, calculated as the sum of differences between usage and requests.
- **CPU usage/requests**: Sum of usage divided by sum of requests, as a percentage.
- **CPU usage/limits**: Sum of usage divided by sum of limits, as a percentage.
- **CPU graph**: A line graph displaying the evolution of usage, requests, and limits over time. Click on each row to see a longer timeframe.

{% /tab %}

{% tab title="Memory" %}

- **Pod group**: Represents deployments by default, but depends on what you specify in the **Group by** field in the upper right. This column includes the sum of usage, requests, and limits for the pods in each group.
- **Memory unused**: Amount of unused memory, calculated as the sum of differences between usage and requests.
- **Memory usage/requests**: Sum of usage divided by sum of requests, as a percentage.
- **Memory usage/limits**: Sum of usage divided by sum of limits, as a percentage.
- **Memory graph**: A line graph displaying the evolution of usage, requests, and limits over time. Click on each row to see a longer timeframe.

{% /tab %}

Use the **Customize** button on the upper right to select other columns to view. Color coding reflects the degree of pod over/under provisioning.

#### Detailed view{% #detailed-view %}

Clicking on a row opens a side panel with the combination of CPU and memory data for each group, with detailed graphs for each pod or container, and a top list of pods.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/kubernetes_resource_utilization_panel.92a9552f96ace68179de71a0ad664a64.png?auto=format"
   alt="Kubernetes resource utilization side panel" /%}

The individual pod or container graphs help you identify outliers that may impact the group in the case of load imbalance. By default, graphs are grouped by `pod_name` to show individual pods. You can change this to group by `kube_container_name` to identify which container(s) contribute the most to over/under provisioning in the case of multi-container pods.

### Optimize idle resources{% #optimize-idle-resources %}

Idle CPU and memory are necessary to ensure that your application has room to grow without pods being immediately throttled or killed.

Too much idle CPU and memory can result in unnecessarily higher costs, but the alternative creates the risk of performance and reliability degradation if resource usage increases.

To help find this balance, adjust the graphs to look at a longer timespan, and avoid making resource sizing decisions based on the most recent usage only. These metrics are standard Kubernetes metrics, so you can query them like all Datadog metricsâfor example, for the last 15 months, at full resolution if needed.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/kubernetes_resource_utilization_metrics.bb00ff9748b2fbd8cba46baedc036e69.png?auto=format"
   alt="Kubernetes resource utilization metrics" /%}

### Known limitations{% #known-limitations %}

Metrics are not displayed for groups containing at least one pod with containers that do not set requests or limits, as Datadog cannot infer the usage percentage without them. These groups without metrics appear last, regardless of the sorting order.

The summation of resource requests and limits for a group is independent of the state of resources belonging to that group. These values may differ from the ones displayed on companion metric graphs.

## Further Reading{% #further-reading %}

- [Practical tips for rightsizing your Kubernetes workloads](https://www.datadoghq.com/blog/rightsize-kubernetes-workloads/)
