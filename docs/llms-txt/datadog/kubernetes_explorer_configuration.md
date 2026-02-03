# Source: https://docs.datadoghq.com/containers/monitoring/kubernetes_explorer_configuration.md

---
title: Configure Kubernetes Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Containers > Container Monitoring > Configure Kubernetes Explorer
---

# Configure Kubernetes Explorer

This page lists configuration options for the [Containers](https://app.datadoghq.com/containers) page in Datadog. To learn more about the Containers page and its capabilities, see [Containers View](https://docs.datadoghq.com/infrastructure/containers) documentation.

## Configure Kubernetes Explorer{% #configure-kubernetes-explorer %}

### Resource collection compatibility matrix{% #resource-collection-compatibility-matrix %}

The following table presents the list of collected resources and the minimal Agent, Cluster Agent, and Helm chart versions for each.

| Resource                  | Minimal Agent version | Minimal Cluster Agent version* | Minimal Helm chart version | Minimal Kubernetes version |
| ------------------------- | --------------------- | ------------------------------ | -------------------------- | -------------------------- |
| ClusterRoleBindings       | 7.33.0                | 1.19.0                         | 2.30.9                     | 1.14.0                     |
| ClusterRoles              | 7.33.0                | 1.19.0                         | 2.30.9                     | 1.14.0                     |
| Clusters                  | 7.33.0                | 1.18.0                         | 2.10.0                     | 1.17.0                     |
| CronJobs                  | 7.33.0                | 7.40.0                         | 2.15.5                     | 1.16.0                     |
| CustomResourceDefinitions | 7.51.0                | 7.51.0                         | 3.39.2                     | v1.16.0                    |
| CustomResources           | 7.51.0                | 7.51.0                         | 3.39.2                     | v1.16.0                    |
| DaemonSets                | 7.33.0                | 1.18.0                         | 2.16.3                     | 1.16.0                     |
| Deployments               | 7.33.0                | 1.18.0                         | 2.10.0                     | 1.16.0                     |
| HorizontalPodAutoscalers  | 7.33.0                | 7.51.0                         | 2.10.0                     | 1.1.1                      |
| Ingresses                 | 7.33.0                | 1.22.0                         | 2.30.7                     | 1.21.0                     |
| Jobs                      | 7.33.0                | 1.18.0                         | 2.15.5                     | 1.16.0                     |
| Namespaces                | 7.33.0                | 7.41.0                         | 2.30.9                     | 1.17.0                     |
| Network Policies          | 7.33.0                | 7.56.0                         | 3.57.2                     | 1.14.0                     |
| Nodes                     | 7.33.0                | 1.18.0                         | 2.10.0                     | 1.17.0                     |
| PersistentVolumeClaims    | 7.33.0                | 1.18.0                         | 2.30.4                     | 1.17.0                     |
| PersistentVolumes         | 7.33.0                | 1.18.0                         | 2.30.4                     | 1.17.0                     |
| Pods                      | 7.33.0                | 1.18.0                         | 3.9.0                      | 1.17.0                     |
| ReplicaSets               | 7.33.0                | 1.18.0                         | 2.10.0                     | 1.16.0                     |
| RoleBindings              | 7.33.0                | 1.19.0                         | 2.30.9                     | 1.14.0                     |
| Roles                     | 7.33.0                | 1.19.0                         | 2.30.9                     | 1.14.0                     |
| ServiceAccounts           | 7.33.0                | 1.19.0                         | 2.30.9                     | 1.17.0                     |
| Services                  | 7.33.0                | 1.18.0                         | 2.10.0                     | 1.17.0                     |
| Statefulsets              | 7.33.0                | 1.15.0                         | 2.20.1                     | 1.16.0                     |
| VerticalPodAutoscalers    | 7.33.0                | 7.46.0                         | 3.6.8                      | 1.16.0                     |

**Note**: After version 1.22, Cluster Agent version numbering follows Agent release numbering, starting with version 7.39.0.

### Add custom tags to resources{% #add-custom-tags-to-resources %}

You can add custom tags to Kubernetes resources to ease filtering inside the Kubernetes resources view.

Additional tags are added through the `DD_ORCHESTRATOR_EXPLORER_EXTRA_TAGS` environment variable.

**Note**: These tags only show up in the Kubernetes resources view.

{% tab title="Datadog Operator" %}
Add the environment variable on both the Process Agent and the Cluster Agent by setting `agents.containers.processAgent.env` and `clusterAgent.env` in `datadog-agent.yaml`.

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
If you are using the [official Helm chart](https://github.com/DataDog/helm-charts), add the environment variable on both the Process Agent and the Cluster Agent by setting `agents.containers.processAgent.env` and `clusterAgent.env` in [values.yaml](https://github.com/DataDog/helm-charts/blob/master/charts/datadog/values.yaml).

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

### Collect custom resources{% #collect-custom-resources %}

The [Kubernetes Explorer](https://app.datadoghq.com/orchestration/explorer/pod) automatically collects Custom Resource Definitions (CRDs) by default.

#### Automatic custom resource collection compatibility matrix{% #automatic-custom-resource-collection-compatibility-matrix %}

When the following CRDs are present in your cluster, the Agent automatically collects their Custom Resources (CRs). If a CRD you use is **not** listed hereâor your Agent version is olderâfollow the **manual configuration** steps below.

| CRD group          | CRD kind             | CRD versions | Minimal Agent version |
| ------------------ | -------------------- | ------------ | --------------------- |
| datadoghq.com      | datadogslo           | v1alpha1     | 7.71.0                |
| datadoghq.com      | datadogdashboard     | v1alpha1     | 7.71.0                |
| datadoghq.com      | datadogagentprofile  | v1alpha1     | 7.71.0                |
| datadoghq.com      | datadogmonitor       | v1alpha1     | 7.71.0                |
| datadoghq.com      | datadogmetric        | v1alpha1     | 7.71.0                |
| datadoghq.com      | datadogpodautoscaler | v1alpha2     | 7.71.0                |
| datadoghq.com      | datadogagent         | v2alpha1     | 7.71.0                |
| argoproj.io        | rollout              | v1alpha1     | 7.71.0                |
| karpenter.sh       | \*                   | v1           | 7.71.0                |
| karpenter.k8s.aws  | \*                   | v1           | 7.71.0                |
| azure.karpenter.sh | \*                   | v1beta1      | 7.71.0                |

#### Manual Configuration{% #manual-configuration %}

For the other CRDs, follow these steps to collect the custom resources that these CRDs define:

1. In Datadog, open [Kubernetes Explorer](https://app.datadoghq.com/orchestration/explorer/pod). On the left panel, under **Select Resources**, select [**Kubernetes > Custom Resources > Resource Definitions**](https://app.datadoghq.com/orchestration/explorer/crd).

1. Locate the CRD that defines the custom resource you want to visualize in the explorer. Under the **Versions** column, click the `version` tag you want to configure indexing for.

   {% video
      url="https://datadog-docs.imgix.net/images/infrastructure/containers_view/CRD_indexing_access_1.mp4" /%}

A modal appears:

   {% image
      source="https://datadog-docs.imgix.net/images/infrastructure/containers_view/indexing_modal_1.19cb54ee10eb2c84cbb66cab546ead83.png?auto=format"
      alt="The Collecting and Indexing modal. Contains two sections: Set up Datadog Agent, with copyable snippets for updating an Agent configuration, and Select indexed fields for filtering/sorting, with checkboxes for fields to index and a preview." /%}



1. Follow the instructions in the modal's **Set up Datadog Agent** section to update the Agent configuration for clusters that are not collecting custom resources. The modal lists all such clusters, either because the Agent is not configured to collect custom resources, or because none are available in that cluster. If the Agent is configured and no custom resources exist, no action is required.

   {% tab title="Helm Chart" %}

   1. Add the following configuration to `datadog-values.yaml`:

      ```yaml
      datadog:
        #(...)
        orchestratorExplorer:
          customResources:
            - <CUSTOM_RESOURCE_NAME>
      ```

   1. Upgrade your Helm chart:

      ```
      helm upgrade -f datadog-values.yaml <RELEASE_NAME> datadog/datadog
      ```

   {% /tab %}

   {% tab title="Datadog Operator" %}

   1. Install the Datadog Operator with an option that grants the Datadog Agent permission to collect custom resources:

      ```
      helm install datadog-operator datadog/datadog-operator --set clusterRole.allowReadAllResources=true
      ```

   1. Add the following configuration to your `DatadogAgent` manifest, `datadog-agent.yaml`:

      ```yaml
      apiVersion: datadoghq.com/v2alpha1
      kind: DatadogAgent
      metadata:
        name: datadog
      spec:
        #(...)
        features:
          orchestratorExplorer:
            customResources:
              - <CUSTOM_RESOURCE_NAME>
      ```

   1. Apply your new configuration:

      ```
      kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
      ```

   {% /tab %}

Each `<CUSTOM_RESOURCE_NAME>` must use the format `group/version/kind`.

1. In the modal, under **Select indexed fields for filtering/sorting**, select the fields you want to index from the custom resource for filtering and sorting. For some CRDs, Datadog provides a default configuration. You can select additional fields if needed.
Important alert (level: info): After the Datadog Agent is set up, it collects available custom resources automatically. Indexing fields is optional.
   {% video
      url="https://datadog-docs.imgix.net/images/infrastructure/containers_view/CRD_indexing_modal_1.mp4" /%}

For arrays of objects, see the Indexing complex types section.

1. Select **Update Fields** to save.

After the fields are indexed, you can add them as columns in the explorer and sort them, or include them in Saved Views. You can also filter on indexed fields using the prefix `field#`.

### Indexing complex types{% #indexing-complex-types %}

{% image
   source="https://datadog-docs.imgix.net/images/containers/explorer/crd_groupby_1.efbee06cfe2a40fbbe2e9ab77de6adba.png?auto=format"
   alt="Indexing Configuration: A targets object[] array, with 'Group by' drop down options: no field, containerResource.container, containerResource.name, containerResource.value.type, etc." /%}

For arrays of objects, two group-by strategies are available:

- `No field`: Object's nested fields are indexed solely on nested field name.
- **Field** (for example: `type`, `status`, etc.): Object's nested fields are indexed based on each unique field value.

##### Example: Filtering on DatadogPodAutoscaler custom resources{% #example-filtering-on-datadogpodautoscaler-custom-resources %}

Consider these two custom resources:

**Custom Resource 1 (CR1)**:

```yaml
status:
    conditions:
        - type: HorizontalAbleToScale
          status: 'True'
        - type: VerticalAbleToApply
          status: 'False'
```

**Custom Resource 2 (CR2)**:

```yaml
status:
    conditions:
        - type: VerticalAbleToApply
          status: 'True'
        - type: HorizontalAbleToScale
          status: 'False'
```

You have the filtering possibilities on `status.conditions` based on the two indexing strategies:

{% tab title="Grouping by no field" %}
**Indexed fields for CR1:**

```yaml
status:
    conditions:
        type: [HorizontalAbleToScale, VerticalAbleToApply]
        status: ['True', 'False']
```

**Indexed fields for CR2:**

```yaml
status:
    conditions:
        type: [VerticalAbleToApply, HorizontalAbleToScale]
        status: ['True', 'False']
```

**Example queries:**

**Query 1:**

```text
field#status.conditions.status:"False"
```

**Result:** Returns CR1 and CR2. Both CRs have at least one object with `status:"False"`

**Query 2:**

```text
field#status.conditions.status:"False" AND field#status.conditions.type:VerticalAbleToApply
```

**Result:** Returns CR1 and CR2. At least one `status.condition` object in each custom resource matches one of the filtersâeven if it's not the same object that matches both filters.
{% /tab %}

{% tab title="Grouping by type" %}
**Indexed fields for CR1:**

```yaml
status:
    conditions:
        - HorizontalAbleToScale:
              status: 'True'
        - VerticalAbleToApply:
              status: 'False'
```

**Indexed fields for CR2:**

```yaml
status:
    conditions:
        - VerticalAbleToApply:
              status: 'True'
        - HorizontalAbleToScale:
              status: 'False'
```

**Example query:**

```text
field#status.conditions.HorizontalAbleToScale.status:"False"
```

**Result:** Returns CR2. Only a `status.condition` object whose `type:"HorizontalAbleToScale"` and `status:"False"` is returned.
{% /tab %}

{% alert level="info" %}
You can select up to 50 fields per resource. You can use the preview to validate your indexing choices.
{% /alert %}

### Collect custom resource metrics using Kubernetes State Core check{% #collect-custom-resource-metrics-using-kubernetes-state-core-check %}

{% alert level="info" %}
This functionality requires Cluster Agent 7.63.0+.
{% /alert %}

You can use the `kubernetes_state_core` check to collect custom resource metrics when running the Datadog Cluster Agent.

1. Write definitions for your custom resources and the fields to turn into metrics according to the following format:

   ```yaml
   #=(...)
   collectCrMetrics:
     - groupVersionKind:
         group: "crd.k8s.amazonaws.com"
         kind: "ENIConfig"
         version: "v1alpha1"
       commonLabels:
         crd_type: "eniconfig"
       labelsFromPath:
         crd_name: [metadata, name]
       metricNamePrefix: "userPrefix"
       metrics:
         - name: "eniconfig"
           help: "ENI Config"
           each:
             type: gauge
             gauge:
               path: [metadata, generation]
     - groupVersionKind:
         group: "vpcresources.k8s.aws"
         kind: "CNINode"
         version: "v1alpha1"
         resource: "cninode-pluralized"
       commonLabels:
         crd_type: "cninode"
       labelsFromPath:
         crd_name: [metadata, name]
       metrics:
         - name: "cninode"
           help: "CNI Node"
           each:
             type: gauge
             gauge:
               path: [metadata, generation]
   ```

By default, RBAC and API resource names are derived from the kind in groupVersionKind by converting it to lowercase, and adding an "s" suffix (for example, Kind: ENIConfig â eniconfigs). If the Custom Resource Definition (CRD) uses a different plural form, you can override this behavior by specifying the resource field. In the example above, CNINode overrides the default by setting resource: "cninode-pluralized".

Metric names are produced using the following rules:

   - No prefix: `kubernetes_state_customresource.<metrics.name>`
   - Prefix: `kubernetes_state_customresource.<metricNamePrefix>_<metric.name>`

For more details, see [Custom Resource State Metrics](https://github.com/kubernetes/kube-state-metrics/blob/main/docs/metrics/extend/customresourcestate-metrics.md).

1. Update your Helm or Datadog Operator configuration:

   {% tab title="Helm Chart" %}

   1. Add the following configuration to `datadog-values.yaml`:

      ```yaml
      datadog:
        #(...)
        kubeStateMetricsCore:
          collectCrMetrics:
            - <CUSTOM_RESOURCE_METRIC>
      ```

Replace `<CUSTOM_RESOURCE_METRIC>` with the definitions you wrote in the first step.

   1. Upgrade your Helm chart:

      ```
      helm upgrade -f datadog-values.yaml <RELEASE_NAME> datadog/datadog
      ```

   {% /tab %}

   {% tab title="Datadog Operator" %}
   Important alert (level: info): This functionality requires Agent Operator v1.20+.
   1. Install the Datadog Operator with an option that grants the Datadog Agent permission to collect custom resources:

      ```
      helm install datadog-operator datadog/datadog-operator --set clusterRole.allowReadAllResources=true
      ```

   1. Add the following configuration to your `DatadogAgent` manifest, `datadog-agent.yaml`:

      ```yaml
      apiVersion: datadoghq.com/v2alpha1
      kind: DatadogAgent
      metadata:
        name: datadog
      spec:
        #(...)
        features:
          kubeStateMetricsCore:
            collectCrMetrics:
              - <CUSTOM_RESOURCE_METRIC>
      ```

Replace `<CUSTOM_RESOURCE_METRIC>` with the definitions you wrote in the first step.

   1. Apply your new configuration:

      ```
      kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
      ```

      {% /tab %}

## Further reading{% #further-reading %}

- [See all of your hosts/containers with the Infrastructure Map](https://docs.datadoghq.com/infrastructure/hostmap/)
- [Understand what is going on at any level of your system](https://docs.datadoghq.com/infrastructure/process/)
