# Source: https://docs.datadoghq.com/containers/cluster_agent.md

---
title: Cluster Agent for Kubernetes
description: >-
  Centralized approach to collecting cluster-level monitoring data with the
  Datadog Cluster Agent
breadcrumbs: Docs > Containers > Cluster Agent for Kubernetes
---

# Cluster Agent for Kubernetes

## Overview{% #overview %}

The Datadog Cluster Agent provides a streamlined, centralized approach to collecting cluster level monitoring data. By acting as a proxy between the API server and node-based Agents, the Cluster Agent helps to alleviate server load. It also relays cluster level metadata to node-based Agents, allowing them to enrich the metadata of locally collected metrics.

Using the Datadog Cluster Agent allows you to:

- Alleviate the impact of Agents on your infrastructure.
- Isolate node-based Agents to their respective nodes, reducing RBAC rules to solely read metrics and metadata from the kubelet.
- Provide cluster level metadata that can only be found in the API server to the Node Agents, in order for them to enrich the metadata of the locally collected metrics.
- Enable the collection of cluster level data, such as the monitoring of services or SPOF and events.
- Use Horizontal Pod Autoscaling (HPA) with custom Kubernetes metrics and external metrics. See the [Autoscaling on custom and external metrics guide](https://docs.datadoghq.com/containers/guide/cluster_agent_autoscaling_metrics) for more details.

If you installed the Datadog Agent using Helm chart v2.7.0 or Datadog Operator v1.0.0+, the **Datadog Cluster Agent is enabled by default**.

Datadog publishes container images to Google Artifact Registry, Amazon ECR, Azure ACR, and Docker Hub:

| Google Artifact Registry | Amazon ECR             | Azure ACR            | Docker Hub        |
| ------------------------ | ---------------------- | -------------------- | ----------------- |
| gcr.io/datadoghq         | public.ecr.aws/datadog | datadoghq.azurecr.io | docker.io/datadog |

By default, the Cluster Agent image is pulled from Google Artifact Registry (`gcr.io/datadoghq`). If Artifact Registry is not accessible in your deployment region, use another registry.

{% alert level="danger" %}
Docker Hub is subject to image pull rate limits. If you are not a Docker Hub customer, Datadog recommends that you update your Datadog Agent and Cluster Agent configuration to pull from GCR or ECR. For instructions, see [Changing your container registry](https://docs.datadoghq.com/agent/guide/changing_container_registry).
{% /alert %}

### Minimum Agent and Cluster Agent versions{% #minimum-agent-and-cluster-agent-versions %}

For optimal compatibility Datadog recommends to keep your Cluster Agent and Agent on matching versions. For a full support matrix of Kubernetes versions and Datadog versions see the [Kubernetes installation page](https://docs.datadoghq.com/containers/kubernetes/installation#minimum-kubernetes-and-datadog-agent-versions).

- [Setup: Setup the Datadog Cluster Agent in your Kubernetes Cluster.](https://docs.datadoghq.com/agent/cluster_agent/setup)
- [Commands & Options: List of all commands and options available for the Cluster Agent.](https://docs.datadoghq.com/agent/cluster_agent/commands)
- [Cluster Checks: Cluster checks provide the ability to Autodiscover and perform checks on load-balanced cluster services like Kubernetes services.](https://docs.datadoghq.com/agent/cluster_agent/clusterchecks)
- [Endpoint Checks: Endpoint checks extend cluster checks to monitor any endpoint behind cluster services.](https://docs.datadoghq.com/agent/cluster_agent/endpointschecks)
- [Admission Controller: Configure the Admission Controller for simplified application Pod configuration.](https://docs.datadoghq.com/agent/cluster_agent/admission_controller)
- [Cluster Agent Troubleshooting: Find troubleshooting information for the Datadog Cluster Agent.](https://docs.datadoghq.com/agent/cluster_agent/troubleshooting)

## Monitoring the Cluster Agent{% #monitoring-the-cluster-agent %}

The Datadog Agent includes an integration that automatically monitors the Cluster Agent. The integration runs on the regular Datadog Agent pod that is on the same node as the Cluster Agent. It will not run in the Cluster Agent itself. Refer to the [Datadog Cluster Agent integration documentation](https://docs.datadoghq.com/integrations/datadog_cluster_agent/) for details.

## Further Reading{% #further-reading %}

- [Introducing the Datadog Cluster Agent](https://www.datadoghq.com/blog/datadog-cluster-agent/)
- [Autoscale your Kubernetes workloads with any Datadog metric](https://www.datadoghq.com/blog/autoscale-kubernetes-datadog/)
- [Bring high-performance observability to secure Kubernetes environments with Datadog's CSI driver](https://www.datadoghq.com/blog/datadog-csi-driver/)
