# Source: https://docs.datadoghq.com/containers/guide/cluster_agent_disable_admission_controller.md

---
title: Disable the Datadog Admission Controller with the Cluster Agent
description: >-
  Safely disable and remove the Datadog Admission Controller from your
  Kubernetes cluster using the Cluster Agent
breadcrumbs: >-
  Docs > Containers > Containers Guides > Disable the Datadog Admission
  Controller with the Cluster Agent
---

# Disable the Datadog Admission Controller with the Cluster Agent

## Overview{% #overview %}

The Datadog Cluster Agent manages the Datadog Admission Controller by creating, updating, and deleting Admission Controllers as needed. To disable the Admission Controller or remove the Cluster Agent, you must first disable the Admission Controller features in the Cluster Agent configuration and redeploy the Cluster Agent. Once the Admission Controllers are removed, the Cluster Agent can be safely removed if necessary.

## Prerequisites{% #prerequisites %}

Datadog Cluster Agent v7.63+

## Steps{% #steps %}

{% tab title="Datadog Operator" %}
To disable the Admission Controllers with your Cluster Agent managed by the Datadog Operator:

1. Set `features.admissionController.enabled` to `false` in your `DatadogAgent` configuration.
1. Set `features.admissionController.validation.enabled` to `false` in your `DatadogAgent` configuration.
1. Set `features.admissionController.mutation.enabled` to `false` in your `DatadogAgent` configuration.

```yaml
  apiVersion: datadoghq.com/v2alpha1
  kind: DatadogAgent
  metadata:
    name: datadog
  spec:
    features:
      admissionController:
        enabled: false
        validation:
          enabled: false
        mutation:
          enabled: false
```

After redeploying the Cluster Agent with the updated configuration, the Admission Controllers are removed.
{% /tab %}

{% tab title="Helm" %}
To disable the Admission Controllers with your Cluster Agent managed by the Datadog Helm Chart:

1. Set `clusterAgent.admissionController.enabled` to `false`.
1. Set `clusterAgent.admissionController.validation.enabled` to `false`.
1. Set `clusterAgent.admissionController.mutation.enabled` to `false`.

```yaml
clusterAgent:
  enabled: true
  admissionController:
    enabled: false
    validation:
      enabled: false
    mutation:
      enabled: false
```

{% /tab %}

You can confirm the Admission Controllers are removed by checking `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` resources in your cluster.

```shell
kubectl get validatingwebhookconfigurations.admissionregistration.k8s.io
```

```shell
kubectl get mutatingwebhookconfigurations.admissionregistration.k8s.io
```

## Further Reading{% #further-reading %}

- [Introducing the Datadog Cluster Agent](https://www.datadoghq.com/blog/datadog-cluster-agent/)
- [Datadog Admission Controller](https://docs.datadoghq.com/containers/cluster_agent/admission_controller/)
- [Troubleshooting the Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/troubleshooting/)
