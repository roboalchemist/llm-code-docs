# Source: https://docs.datadoghq.com/containers/datadog_operator.md

---
title: Datadog Operator
description: Deploy and manage the Datadog Agent on Kubernetes using the Datadog Operator
breadcrumbs: Docs > Container Monitoring > Datadog Operator
source_url: https://docs.datadoghq.com/datadog_operator/index.html
---

# Datadog Operator

[Datadog Operator](http://github.com/DataDog/datadog-operator) is an open source [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that enables you to deploy and configure the Datadog Agent in a Kubernetes environment.

By using the Operator, you can use a single Custom Resource Definition (CRD) to deploy the node-based Agent, [Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent), and [cluster checks runner](https://docs.datadoghq.com/containers/cluster_agent/clusterchecks). The Operator reports deployment status, health, and errors in the Operator's CRD status. Because the Operator uses higher-level configuration options, it limits the risk of misconfiguration.

Once you have deployed the Agent, the Datadog Operator provides the following:

- Validation for your Agent configurations
- Keeping all Agents up-to-date with your configuration
- Orchestration for creating and updating Agent resources
- Reporting of Agent configuration status in the Operator's CRD status
- Optionally, use of an advanced DaemonSet deployment by using Datadog's [ExtendedDaemonSet](https://github.com/DataDog/extendeddaemonset)

### Why use the Datadog Operator instead of a Helm chart or DaemonSet?{% #why-use-the-datadog-operator-instead-of-a-helm-chart-or-daemonset %}

You can also use a Helm chart or a DaemonSet to install the Datadog Agent on Kubernetes. However, using the Datadog Operator offers the following advantages:

- The Operator has built-in defaults based on Datadog best practices.
- Operator configuration is more flexible for future enhancements.
- As a [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), the Datadog Operator is treated as a first-class resource by the Kubernetes API.
- Unlike the Helm chart, the Operator is included in the Kubernetes reconciliation loop.

Datadog fully supports using a DaemonSet to deploy the Agent, but manual DaemonSet configuration leaves significant room for error. Therefore, using a DaemonSet is not highly recommended.

## Usage{% #usage %}

See the [Getting Started with the Datadog Operator](https://docs.datadoghq.com/getting_started/containers/datadog_operator) guide to learn how to use the Operator to deploy the Datadog Agent.

For all installation and configuration options, see the detailed [installation](https://github.com/DataDog/datadog-operator/blob/main/docs/installation.md) and [configuration](https://github.com/DataDog/datadog-operator/blob/main/docs/configuration.v2alpha1.md) pages in the [`datadog-operator`](http://github.com/DataDog/datadog-operator) repo.

## Further Reading{% #further-reading %}

- [Getting Started with the Datadog Operator](https://docs.datadoghq.com/getting_started/containers/datadog_operator)
- [Datadog Operator: Advanced Installation](https://github.com/DataDog/datadog-operator/blob/main/docs/installation.md)
- [Datadog Operator: Configuration](https://github.com/DataDog/datadog-operator/blob/main/docs/configuration.v2alpha1.md)
- [Instrument your app using the Datadog Operator and Admission Controller](https://www.datadoghq.com/architecture/instrument-your-app-using-the-datadog-operator-and-admission-controller/)
