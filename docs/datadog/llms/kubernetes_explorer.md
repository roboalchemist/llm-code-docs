# Source: https://docs.datadoghq.com/containers/monitoring/kubernetes_explorer.md

---
title: Kubernetes Explorer
description: >-
  Using Datadog's Kubernetes Explorer page to monitor your Kubernetes resources,
  such as pods and deployments.
breadcrumbs: Docs > Containers > Container Monitoring > Kubernetes Explorer
---

# Kubernetes Explorer

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex.8494f89bafae55950571c130fe511ab9.png?auto=format"
   alt="Kubernetes Explorer, showing Kubernetes Pods." /%}

Datadog's [Kubernetes Explorer](https://app.datadoghq.com/orchestration/overview) allows you to monitor the state of pods, deployments, and other Kubernetes resources. You can also view resource specifications for failed pods within a deployment, correlate node activity with related logs, track resource utilization, automatically scale workloads, and remediate errors.

{% alert level="info" %}
Kubernetes Explorer requires Datadog Agent 7.27.0+ and Datadog Cluster Agent 1.11.0+.If you are using Kubernetes 1.25+, then Cluster Agent 7.40.0+ is required.
{% /alert %}

## Configuration{% #configuration %}

### Enable Kubernetes Explorer{% #enable-kubernetes-explorer %}

Kubernetes Explorer is **enabled by default** for most Datadog Agent installations.

{% tab title="Datadog Operator" %}
When you install the Datadog Agent by using the Datadog Operator, Kubernetes Explorer is enabled by default.

To verify that Kubernetes Explorer is enabled, ensure that the `features.orchestratorExplorer.enabled` parameter is set to `true` in your `datadog-agent.yaml`:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    clusterName: <CLUSTER_NAME>
    credentials:
      apiKey: <DATADOG_API_KEY>
      appKey: <DATADOG_APP_KEY>
  features:
    orchestratorExplorer:
      enabled: true
```

{% /tab %}

{% tab title="Helm" %}
When you install the Datadog Agent by using the [official Helm chart](https://github.com/DataDog/helm-charts), Kubernetes Explorer is enabled by default.

To verify that Kubernetes Explorer is enabled, ensure that the `orchestratorExplorer.enabled` parameter is set to `true` in your `datadog-values.yaml` file:

```yaml
datadog:
  clusterName: <CLUSTER_NAME>
  # (...)
  processAgent:
    enabled: true
  orchestratorExplorer:
    enabled: true
```

Then, upgrade your Helm chart.
{% /tab %}

{% tab title="Manual" %}
For manual setup, see [Set up Kubernetes Explorer with a DaemonSet](https://docs.datadoghq.com/infrastructure/faq/set-up-orchestrator-explorer-daemonset).
{% /tab %}

### Collect custom resources{% #collect-custom-resources %}

### Add custom tags to resources{% #add-custom-tags-to-resources %}

To ease filtering, you can add custom tags to your Kubernetes resources through the `DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS` environment variable. **These tags only appear in Kubernetes Explorer.**

{% tab title="Datadog Operator" %}
Set the `DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS` environment variable **twice** in `datadog-agent.yaml`:

- In `agents.containers.processAgent.env`
- In `clusterAgent.env`

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>
      appKey: <DATADOG_APP_KEY>
  features:
    liveContainerCollection:
      enabled: true
    orchestratorExplorer:
      enabled: true
  override:
    agents:
      containers:
        processAgent:
          env:
            - name: "DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS"
              value: "tag1:value1 tag2:value2"
    clusterAgent:
      env:
        - name: "DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS"
          value: "tag1:value1 tag2:value2"
```

Then, apply the new configuration:

```bash
kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
```

{% /tab %}

{% tab title="Helm" %}
Set the `DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS` environment variable **twice** in `datadog-agent.yaml`:

- In `processAgent.env`
- In `clusterAgent.env`

```yaml
agents:
  containers:
    processAgent:
      env:
        - name: "DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS"
          value: "tag1:value1 tag2:value2"
clusterAgent:
  env:
    - name: "DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS"
      value: "tag1:value1 tag2:value2"
```

Then, upgrade your Helm chart.
{% /tab %}

{% tab title="DaemonSet" %}
Set the environment variable on both the Process Agent and Cluster Agent containers:

```yaml
- name: DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS
  value: "tag1:value1 tag2:value2"
```

{% /tab %}

## Usage{% #usage %}

### Views{% #views %}

Toggle among the **Pods**, **Clusters**, **Namespaces**, and other Kubernetes resources in the **Select Resources** dropdown menu in the top left corner of the page.

Each of these views includes a data table to help you better organize your data by field such as status, name, and Kubernetes labels, and a detailed Cluster Map to give you a bigger picture of your pods and Kubernetes clusters.

**See Query filter details for more details on how to filter these views.**

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_replicasets.ee4e338e435e12d49003c3b5c67a1af7.png?auto=format"
   alt="Orchestrator Explorer opened to show Workloads > Replica Sets, in Summary mode" /%}

#### Group by functionality and facets{% #group-by-functionality-and-facets %}

Group pods by tags, Kubernetes labels, or Kubernetes annotations to get an aggregated view which allows you to find information quicker. You can perform a group by using the "Group by" bar on the top right of the page or by clicking on a particular tag or label and locating the group by function in the context menu as shown below.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_groupby.3af011d423b7c0e41a95822922c60d06.png?auto=format"
   alt="An example of grouping by team" /%}

You can also use facets on the left hand side of the page to group resources or filter for resources you care most about, such as pods with a CrashLoopBackOff pod status.

{% video
   url="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/crashloopbackoff.mp4" /%}

### Cluster map{% #cluster-map %}

A cluster map gives you a bigger picture of your pods and Kubernetes clusters. You can see all of your resources together on one screen with customized groups and filters, and choose which metrics to fill the color of the nodes.

Examine resources from cluster maps by clicking on any circle or group to populate a detailed panel.

{% video
   url="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/cluster-map.mp4" /%}

### Information panel{% #information-panel %}

Click on any row in the table or on any object in a Cluster Map to view information about a specific resource in a side panel.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_panel.a2d42a118725015e6c69a921bf85b0b7.png?auto=format"
   alt="A view of resources in the side panel, opened to processes." /%}

The side panel's **YAML** tab shows the full resource definition. Starting in **Agent version 7.44.0**, it also includes seven days of definition history. You can compare what changed over time and across different versions. The time indicated is approximately when the changes were applied to the resource.

To prevent displaying a large number of irrelevant changes, updates affecting only the following fields are ignored:

- metadata.resourceVersion
- metadata.managedFields
- metadata.generation
- metadata.annotations["kubernetes.io/config.seen"]
- status

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_manifest_history.b0ada55feaa7cb5e7365a3f3bb31125b.png?auto=format"
   alt="A view of resources in the side panel, showing the yaml history feature" /%}

The other tabs show more information for troubleshooting the selected resource:

- [**Logs**](https://docs.datadoghq.com/logs): View logs from your container or resource. Click on any log to view related logs in the Log Explorer.
- [**APM**](https://docs.datadoghq.com/tracing): View traces from your container or resource, including the date, service, duration, method, and status code of a trace.
- [**Metrics**](https://docs.datadoghq.com/metrics): View live metrics for your container or resource. You can view any graph full screen, share a snapshot of it, or export it from this tab.
- **Processes**: View all processes running in the container of this resource.
- **Network**: View a container or resource's network performance, including source, destination, sent and received volume, and throughput fields. Use the **Destination** field to search by tags like `DNS` or `ip_type`, or use the **Group by** filter in this view to group network data by tags, like `pod_name` or `service`.
- [**Events**](https://docs.datadoghq.com/events): View all Kubernetes events for your resource.
- **Monitors**: View monitors tagged, scoped, or grouped for this resource.

For a detailed dashboard of this resource, click the View Dashboard in the top right corner of this panel.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/view-pod-dashboard.ed674c5790c041b9935a6998fcbc9fe2.png?auto=format"
   alt="A link to a pod dashboard from Live Containers overview" /%}

### Resource utilization{% #resource-utilization %}

*For the Resource Utilization page, see [Resource Utilization](https://docs.datadoghq.com/infrastructure/containers/kubernetes_resource_utilization)*.

Within the Kubernetes Explorer tab, you can explore a selection of resource utilization metrics.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_resource_utilization.08e4a20c12a7b4395a257bd419e9f6dd.png?auto=format"
   alt="Container Resource Utilization" /%}

All of these columns support sorting, which helps you to pinpoint individual workloads based on their resource utilization.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ex_resource_utilization_sorted_column.6653c50c2e2e08d43f9f7724ddf3656e.png?auto=format"
   alt="Container Resource Utilization Sorted Columns" /%}

## Query filter details{% #query-filter-details %}

You can narrow down the displayed resources by supplying a query within the "Filter by" search bar on the top left of the page.

### Syntax{% #syntax %}

A query filter is composed of terms and operators. Example:

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_syntax.d68923dd544effda5645ee9f5cca141a.png?auto=format"
   alt="Orchestrator Explorer query filter syntax." /%}

#### Terms{% #terms %}

There are multiple types of terms available:

| Type                                                                                                                                                                                                                                              | Examples                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Tags**: Attached to resources by [the agent collecting them](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/?tab=containerizedenvironments). There are also additional tags that Datadog generates for Kubernetes resources. | `datacenter:staging`, `tag#datacenter:staging`*(the `tag#` is optional)*                                                                                           |
| **Labels**: Extracted from [a resource's metadata](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). They are typically used to organize your cluster and target specific resources with selectors.                     | `label#chart_version:2.1.0`                                                                                                                                        |
| **Annotations**: Extracted from [a resource's metadata](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/). They are generally used to support tooling that aid in cluster management.                               | `annotation#checksum/configmap:a1bc23d4`                                                                                                                           |
| **Metrics**: Added to workload resources (pods, deployments, etc.). You can find resources based on their utilization. To see what metrics are supported, see Resource Utilization Filters.                                                       | `metric#cpu_usage_pct_limits_avg15:>80%`                                                                                                                           |
| **String matching**: Supported by some specific resource attributes, see below.*Note: string matching does not use the key-value format, and you cannot specify the attribute to match on.*                                                       | `"10.132.6.23"` (IP),`"9cb4b43f-8dc1-4a0e"` (UID),`web-api-3` (Name)                                                                                               |
| **Fields**: Extracted from [a resource's metadata](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/) or from custom resources' indexed fields.                                                                  | `field#metadata.creationTimestamp:>=4wk`, `field#metadata.deletionTimestamp:<=1hr`, `field#status.currentReplicas:3`, `field#status.conditions.Active.status:True` |

***Note**: You might find the same key-value pairs as both a tag and label (or annotation) - this is dependent on how your cluster is configured.*

The following resource attributes are supported in arbitrary **String Matching**:

- `metadata.name`
- `metadata.uid`
- IP Addresses found in:
  - Pods
  - Nodes (internal and external)
  - Services (cluster, external, and load balancer IPs)

You do not need to specify a key to search for a resource by name, or IP. Quotes are not required unless your string search includes certain special characters.

#### Comparators{% #comparators %}

All terms support the `:` equality operator. Metric value terms support numeric comparisons as well:

- `:>` Greater than (for example, `metric#cpu_usage_avg15:>0.9`)
- `:>=` Greater than or equal
- `:<` Less than
- `:<=` Less than or equal

#### Operators{% #operators %}

To combine multiple terms into a complex query, you can use any of the following case sensitive boolean operators:

| Operator    | Description                                                                                            | Example                             |
| ----------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| `AND`       | **Intersection**: Both terms are in the selected events (if nothing is added, AND is taken by default) | `a AND b`                           |
| `OR`        | **Union**: Either term is contained in the selected events                                             | `a OR b`                            |
| `NOT` / `-` | **Exclusion**: The following term is NOT in the event (apply to each individual raw text search)       | `a AND NOT b` or`a AND -b`          |
| `( )`       | **Grouping:** Specify how to group terms logically.                                                    | `a AND (b OR c)` or`(a AND b) or c` |

##### `OR` value shorthand{% #or-value-shorthand %}

Multiple terms sharing the same key can be combined into a single term if they all use the `OR` operator. For example, this query:

```
app_name:web-server OR app_name:database OR app_name:event-consumer
```

Can be reduced to:

```
app_name:(web-server OR database OR event-consumer)
```

### Wildcards{% #wildcards %}

You can use `*` wildcards as part of a term to filter by partial matches, both for values and keys. Some examples:

- `kube_job:stats-*`: Find all resources with a `kube_deployment` tag value starting with `stats-`.
- `pod_name:*canary`: Find all resources with a `pod_name` value ending in `canary`.
- `label#release:*`: Find all resources with a `release` label, regardless of its value.
- `-label#*.datadoghq.com/*`: Find resources that do not have any Datadog scoped labels.
- `kube_*:*stats*canary`: Find resources that have related resource tags (`kube_*`), with `stats` in the middle of the value, also ending with `canary`.

### Extracted tags{% #extracted-tags %}

In addition to the tags you have [configured](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/?tab=containerizedenvironments) within your Datadog agent, Datadog injects generated tags based on resource attributes that can help your searching and grouping needs. These tags are added to resources conditionally, when they are relevant.

#### All resources{% #all-resources %}

All resources have the `kube_cluster_name` tag and all namespaced resources have the `kube_namespace` tag added to them.

Additionally, resources contain a `kube_<api_kind>:<metadata.name>` tag. For example, a deployment named `web-server-2` would have the `kube_deployment:web-server-2` tag automatically added to it.

**Note**: There are some exceptions to this pattern:

- Pods use `pod_name` instead.
- *VPAs: `verticalpodautoscaler`*.
- *HPAs: `horizontalpodautoscaler`*.
- *Persistent Volume Claims: `persistentvolumeclaim`*.

Based on the labels attached to the resource, the following tags will also be extracted:

| Tag                   | Source Label                   |
| --------------------- | ------------------------------ |
| `kube_app_name`       | `app.kubernetes.io/name`       |
| `kube_app_instance`   | `app.kubernetes.io/instance`   |
| `kube_app_version`    | `app.kubernetes.io/version`    |
| `kube_app_component`  | `app.kubernetes.io/component`  |
| `kube_app_part_of`    | `app.kubernetes.io/part-of`    |
| `kube_app_managed_by` | `app.kubernetes.io/managed-by` |
| `env`                 | `tags.datadoghq.com/env`       |
| `version`             | `tags.datadoghq.com/version`   |
| `service`             | `tags.datadoghq.com/service`   |

#### Relationships{% #relationships %}

Related Resources will be tagged with each other. Some examples:

- A pod that is part of the "XYZ" deployment will have a `kube_deployment:xyz` tag.
- An ingress that points at service "A" will have a `kube_service:a` tag.

Resources that are spawned from "parent" resources will have the `kube_ownerref_kind` and `kube_ownerref_name` tags (such as pods and jobs).

**Tip:** Utilize the filter query autocomplete feature to discover what related resource tags are available. Type `kube_` and see what results are suggested.

#### Pods{% #pods %}

Pods are given the following tags:

- `pod_name`
- `pod_phase` (extracted from the manifest)
- `pod_status` (calculated similarly to `kubectl`)

#### Workloads{% #workloads %}

Workload resources (pods, deployments, stateful sets, etc.) will have the following tags, indicating their support within the Resources Utilization page:

- `resource_utilization` (`supported` or `unsupported`)
- `missing_cpu_requests`
- `missing_cpu_limits`
- `missing_memory_requests`
- `missing_memory_limits`

#### Conditions{% #conditions %}

Some conditions, for some resources, are extracted as tags. For example, you can find the `kube_condition_available` tag on deployments. The tag format is always `kube_condition_<name>` with a `true` or `false` value.

**Tip**: Use the autocomplete feature to discover what conditions are available on a given resource type by entering `kube_condition` and reviewing the results.

#### Resource specific tags{% #resource-specific-tags %}

Some resources have specific tags that are extracted based on your cluster's environment. The following tags are available in addition to the shared tags above.

| Resource                                              | Extracted Tags                                                                                                                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster**                                           | `api_server_version``kubelet_version`                                                                                                                      |
| **Custom Resource Definitions** &**Custom Resources** | `kube_crd_kind``kube_crd_group``kube_crd_version``kube_crd_scope``kube_crd_resource`                                                                       |
| **Namespace**                                         | `phase`                                                                                                                                                    |
| **Node**                                              | `kube_node_unschedulable``kube_node_kubelet_version``kube_node_kernel_version``kube_node_runtime_version``eks_fargate_node``node_schedulable``node_status` |
| **Persistent Volume**                                 | `kube_reclaim_policy``kube_storage_class_name``pv_type``pv_phase`                                                                                          |
| **Persistent Volume Claim**                           | `pvc_phase``kube_storage_class_name`                                                                                                                       |
| **Pod**                                               | `pod_name` (instead of `kube_pod`)`pod_phase` (extracted from the Manifest)`pod_status` (calculated similarly to `kubectl`)                                |
| **Service**                                           | `kube_service_type``kube_service_port`                                                                                                                     |

### Resource Utilization Filters{% #resource-utilization-filters %}

The following workload resources are enriched with resource utilization metrics:

- Clusters
- Daemonsets
- Deployments
- Nodes
- Pods
- Replica Sets
- Stateful Sets

These metrics are calculated at the time of collection, based on the average values over the last 15 minutes. You can filter by metric values like so: `metric#<metric_name><comparator><numeric_value>`.

- `metric_name` is an available metric (see below)
- `comparator` is a supported comparator
- and `numeric_value` is a floating point value.

For these workload resources, the following metric names are available:

| CPU                            | Memory                         |
| ------------------------------ | ------------------------------ |
| `cpu_limits_avg15`             | `mem_limits_avg15`             |
| `cpu_requests_avg15`           | `mem_requests_avg15`           |
| `cpu_usage_avg15`              | `mem_usage_avg15`              |
| `cpu_usage_pct_limits_avg15`   | `mem_usage_pct_limits_avg15`   |
| `cpu_usage_pct_requests_avg15` | `mem_usage_pct_requests_avg15` |
| `cpu_waste_avg15`              | `mem_waste_avg15`              |

In addition, clusters, and nodes have the following metrics available to them:

- `cpu_usage_pct_alloc_avg15`
- `cpu_requests_pct_alloc_avg15`
- `mem_usage_pct_alloc_avg15`
- `mem_requests_pct_alloc_avg15`

#### Metric units{% #metric-units %}

CPU metrics are stored as a number of cores.

Memory metrics are stored as bytes.

Percents (`*_pct_*`) are stored as floats, where `0.0` is 0%, and `1.0` is 100%. The value is the ratio of the two indicated metrics - for example `cpu_usage_pct_limits_avg15` is the value of `usage / limits`. Metric values can be above 100%, such as Percentage CPU Usage of Requests.

## Notes and known issues{% #notes-and-known-issues %}

- Data is updated automatically in constant intervals.
- In clusters with 1000+ Deployments or ReplicaSets you may notice elevated CPU usage from the Cluster Agent. There is an option to disable container scrubbing in the Helm chart. See [the Helm Chart repo](https://github.com/DataDog/helm-charts/tree/master/charts/datadog) for more details.

## Further reading{% #further-reading %}

- [Monitor your Kubernetes operators to keep applications running smoothly](https://www.datadoghq.com/blog/kubernetes-operator-performance)
