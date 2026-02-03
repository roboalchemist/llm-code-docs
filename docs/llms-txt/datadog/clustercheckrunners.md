# Source: https://docs.datadoghq.com/containers/guide/clustercheckrunners.md

---
title: Cluster Check Runners
description: >-
  Configure dedicated cluster check runners for scaling cluster and endpoint
  checks in Kubernetes environments
breadcrumbs: Docs > Containers > Containers Guides > Cluster Check Runners
---

# Cluster Check Runners

The Cluster Agent can dispatch out two types of checks: [endpoint checks](https://docs.datadoghq.com/agent/cluster_agent/endpointschecks/) and [cluster checks](https://docs.datadoghq.com/agent/cluster_agent/clusterchecks/). The checks are slightly different.

Endpoint checks are dispatched specifically to the regular Datadog Agent on the same node as the application pod endpoints. Executing endpoint checks on the same node as the application endpoint allows proper tagging of the metrics.

Cluster checks monitor internal Kubernetes services, as well as external services like managed databases and network devices, and can be dispatched much more freely. Using Cluster Check Runners is optional. When you use Cluster Check Runners, a small, dedicated set of Agents runs the cluster checks, leaving the endpoint checks to the normal Agent. This strategy can be beneficial to control the dispatching of cluster checks, especially when the scale of your cluster checks increases.

## Set up{% #set-up %}

First, [deploy the Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/setup/).

Then, deploy the cluster check runner using either [Datadog Operator](https://github.com/DataDog/datadog-operator) or [Helm](https://github.com/DataDog/helm-charts/blob/master/charts/datadog/values.yaml):

{% tab title="Datadog Operator" %}
Using the Operator, you can launch and manage all of these resources with a single manifest. For example:

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
    clusterAgentToken: <DATADOG_CLUSTER_AGENT_TOKEN>
  features:
    clusterChecks:
      enabled: true
      useClusterChecksRunners: true
  override:
    clusterAgent:
      replicas: 2
```

Deploy these resources into your cluster:

```
kubectl apply -f datadog-agent-with-dca-clusterchecksrunner.yaml
```

If you see the following output, it confirms the configuration was applied successfully:

```
datadogagent.datadoghq.com/datadog created
```

See the [Datadog Operator repo](https://github.com/DataDog/datadog-operator) for more information about the Datadog Operator.
{% /tab %}

{% tab title="Helm" %}
You can update the relevant sections of the chart to enable cluster checks, the Cluster Agent, and the cluster check runner at the same time. For example:

```yaml
datadog:
  clusterChecks:
    enabled: true
  #(...)

clusterAgent:
  enabled: true
  #(...)

clusterChecksRunner:
  enabled: true
  replicas: 2
```

{% /tab %}

**Note**: Both the Datadog Operator and the Helm chart use `podAntiAffinity` to avoid having multiple cluster check runners on the same node. This is important because the Cluster Agent identifies the cluster check runners by their node names. Using `podAntiAffinity` avoids having name collisions.
