# Source: https://docs.datadoghq.com/containers/kubernetes/installation.md

---
title: Install the Datadog Agent on Kubernetes
description: >-
  Install and configure the Datadog Agent on Kubernetes using the Datadog
  Operator, Helm, or kubectl
breadcrumbs: >-
  Docs > Container Monitoring > Kubernetes > Install the Datadog Agent on
  Kubernetes
source_url: https://docs.datadoghq.com/kubernetes/installation/index.html
---

# Install the Datadog Agent on Kubernetes

## Overview{% #overview %}

This page provides instructions on installing the Datadog Agent in a Kubernetes environment.

For dedicated documentation and examples for major Kubernetes distributions including AWS Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), Google Kubernetes Engine (GKE), Red Hat OpenShift, Rancher, and Oracle Container Engine for Kubernetes (OKE), see [Kubernetes distributions](https://docs.datadoghq.com/agent/kubernetes/distributions).

For dedicated documentation and examples for monitoring the Kubernetes control plane, see [Kubernetes control plane monitoring](https://docs.datadoghq.com/agent/kubernetes/control_plane).

### Minimum Kubernetes and Datadog Agent versions{% #minimum-kubernetes-and-datadog-agent-versions %}

Some features related to later Kubernetes versions require a minimum Datadog Agent version.

| Kubernetes version | Agent version | Cluster Agent version | Reason                                                                         |
| ------------------ | ------------- | --------------------- | ------------------------------------------------------------------------------ |
| 1.16.0+            | 7.19.0+       | 1.9.0+                | Kubelet metrics deprecation                                                    |
| 1.21.0+            | 7.36.0+       | 1.20.0+               | Kubernetes resource deprecation                                                |
| 1.22.0+            | 7.37.0+       | 7.37.0+               | Supports dynamic service account token                                         |
| 1.25.0+            | 7.40.0+       | 7.40.0+               | Supports `v1` API group                                                        |
| 1.33.0+            | 7.67.0+       | 7.67.0+               | Fixes incompatibilities with Kubernetes `AllocatedResources` in `/pods` output |

For optimal compatibility Datadog recommends to keep your Cluster Agent and Agent on matching versions.

## Installation{% #installation %}

Use the [Installing on Kubernetes](https://app.datadoghq.com/account/settings/agent/latest?platform=kubernetes) page in Datadog to guide you through the installation process.

1. **Select installation method**

Choose one of the following installation methods:

   - [Datadog Operator](https://docs.datadoghq.com/containers/datadog_operator) (recommended): a Kubernetes [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that you can use to deploy the Datadog Agent on Kubernetes and OpenShift. It reports deployment status, health, and errors in its Custom Resource status, and it limits the risk of misconfiguration thanks to higher-level configuration options.
   - [Helm](https://helm.sh)
   - Manual installation. See [Manually install and configure the Datadog Agent with a DaemonSet](https://docs.datadoghq.com/containers/guide/kubernetes_daemonset/)

{% tab title="Datadog Operator" %}

{% alert level="info" %}
Requires [Helm](https://helm.sh) and the [kubectl CLI](https://kubernetes.io/docs/tasks/tools/#kubectl).
{% /alert %}

**Install the Datadog Operator**

To install the Datadog Operator in your current namespace, run:

```shell
helm repo add datadog https://helm.datadoghq.com
helm install datadog-operator datadog/datadog-operator
kubectl create secret generic datadog-secret --from-literal api-key=<DATADOG_API_KEY>
```

- Replace `<DATADOG_API_KEY>` with your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).

**Configure `datadog-agent.yaml`**

Create a file, `datadog-agent.yaml`, that contains:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    clusterName: <CLUSTER_NAME>
    site: <DATADOG_SITE>
    credentials:
      apiSecret:
        secretName: datadog-secret
        keyName: api-key
```

- Replace `<CLUSTER_NAME>` with a name for your cluster.
- Replace `<DATADOG_SITE>` with your [Datadog site](https://docs.datadoghq.com/getting_started/site). Your site is . (Ensure the correct SITE is selected on the right).

**Deploy Agent with the above configuration file**

Run:

```shell
kubectl apply -f datadog-agent.yaml
```

{% /tab %}

{% tab title="Helm" %}

{% alert level="info" %}
Requires [Helm](https://helm.sh).
{% /alert %}

**Add the Datadog Helm repository**

Run:

```shell
helm repo add datadog https://helm.datadoghq.com
helm repo update
kubectl create secret generic datadog-secret --from-literal api-key=<DATADOG_API_KEY>
```

- Replace `<DATADOG_API_KEY>` with your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).

**Configure `datadog-values.yaml`**

Create a file, `datadog-values.yaml`, that contains:

```yaml
datadog:
 apiKeyExistingSecret: datadog-secret
 clusterName: <CLUSTER_NAME>
 site: <DATADOG_SITE>
```

- Replace `<CLUSTER_NAME>` with a name for your cluster.
- Replace `<DATADOG_SITE>` with your [Datadog site](https://docs.datadoghq.com/getting_started/site). Your site is . (Ensure the correct SITE is selected on the right).

**Deploy Agent with the above configuration file**

Run:

```shell
helm install datadog-agent -f datadog-values.yaml datadog/datadog
```

{% alert level="info" %}
For Windows, append `--set targetSystem=windows` to the `helm install` command.
{% /alert %}

{% /tab %}

**Confirm Agent installation**

Verify that Agent pods (tagged with `app.kubernetes.io/component:agent`) appear on the [Containers](https://app.datadoghq.com/containers) page in Datadog. Agent pods are detected within a few minutes of deployment.

{% alert level="info" %}
`<CLUSTER_NAME>` allows you to scope hosts and Cluster Checks. This unique name must be dot-separated tokens and abide by the following restrictions:

- Must only contain lowercase letters, numbers, and hyphens
- Must start with a letter
- Must end with a number or a letter
- Must be less than or equal to 80 characters

{% /alert %}

### Unprivileged installation{% #unprivileged-installation %}

To run an unprivileged installation, add the following `securityContext` to your configuration relative to your desired `<USER_ID>` and `<GROUP ID>`:

- Replace `<USER_ID>` with the UID to run the Datadog Agent. Datadog recommends setting this value to `100` for the preexisting `dd-agent` user [for Datadog Agent v7.48+](https://docs.datadoghq.com/data_security/kubernetes/#running-container-as-root-user).
- Replace `<GROUP_ID>` with the group ID that owns the Docker or containerd socket.

This sets the `securityContext` at the pod level for the Agent.

{% tab title="Datadog Operator" %}
To run an unprivileged installation, add the following to `datadog-agent.yaml`:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    clusterName: <CLUSTER_NAME>
    site: <DATADOG_SITE>
    credentials:
      apiSecret:
        secretName: datadog-secret
        keyName: api-key

  override:
    nodeAgent:
      securityContext:
        runAsUser:  <USER_ID>
        supplementalGroups:
          - <GROUP_ID>
```

Then, deploy the Agent:

```shell
kubectl apply -f datadog-agent.yaml
```

{% /tab %}

{% tab title="Helm" %}
To run an unprivileged installation, add the following to your `datadog-values.yaml` file:

```yaml
datadog:
  apiKeyExistingSecret: datadog-secret
  clusterName: <CLUSTER_NAME>
  site: <DATADOG_SITE>
  securityContext:
    runAsUser: <USER_ID>
    supplementalGroups:
      - <GROUP_ID>
```

Then, deploy the Agent:

```shell
helm install datadog-agent -f datadog-values.yaml datadog/datadog
```

{% /tab %}

### Container registries{% #container-registries %}

Datadog publishes container images to Google Artifact Registry, Amazon ECR, Azure ACR, and Docker Hub:

| Google Artifact Registry | Amazon ECR             | Azure ACR            | Docker Hub        |
| ------------------------ | ---------------------- | -------------------- | ----------------- |
| gcr.io/datadoghq         | public.ecr.aws/datadog | datadoghq.azurecr.io | docker.io/datadog |

By default, the Agent image is pulled from Google Artifact Registry (`gcr.io/datadoghq`). If Artifact Registry is not accessible in your deployment region, use another registry.

If you are deploying the Agent in an AWS environment, Datadog recommend that you use Amazon ECR.

{% alert level="danger" %}
Docker Hub is subject to image pull rate limits. If you are not a Docker Hub customer, Datadog recommends that you update your Datadog Agent and Cluster Agent configuration to pull from Google Artifact Registry or Amazon ECR. For instructions, see [Changing your container registry](https://docs.datadoghq.com/agent/guide/changing_container_registry).
{% /alert %}

{% tab title="Datadog Operator" %}
To use a different container registry, modify `global.registry` in `datadog-agent.yaml`.

For example, to use Amazon ECR:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    clusterName: <CLUSTER_NAME>
    registry: public.ecr.aws/datadog
    site: <DATADOG_SITE>
    credentials:
      apiSecret:
        secretName: datadog-secret
        keyName: api-key
```

{% /tab %}

{% tab title="Helm" %}
To use a different container registry, modify `registry` in `datadog-values.yaml`.

For example, to use Amazon ECR:

```yaml
registry: public.ecr.aws/datadog
datadog:
  apiKeyExistingSecret: datadog-secret
  site: <DATADOG_SITE>
```

{% /tab %}

For more information, see [Changing your container registry](https://docs.datadoghq.com/containers/guide/changing_container_registry/).

### Uninstall{% #uninstall %}

{% tab title="Datadog Operator" %}

```shell
kubectl delete datadogagent datadog
helm delete datadog-operator
```

This command deletes all Kubernetes resources created by installing Datadog Operator and deploying the Datadog Agent.
{% /tab %}

{% tab title="Helm" %}

```shell
helm uninstall datadog-agent
```

{% /tab %}

## Next steps{% #next-steps %}

### Monitor your infrastructure in Datadog{% #monitor-your-infrastructure-in-datadog %}

Use the [Containers](https://app.datadoghq.com/containers) page for visibility into your container infrastructure, with resource metrics and faceted search. For information on how to use the Containers page, see [Containers View](https://docs.datadoghq.com/infrastructure/containers).

Use the [Container Images](https://app.datadoghq.com/containers/images) page for insights into every image used in your environment. This page also displays vulnerabilities found in your container images from [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management). For information on how to use the Container Images page, see the [Containers Images View](https://docs.datadoghq.com/infrastructure/containers/container_images).

The [Kubernetes](https://app.datadoghq.com/kubernetes) section features an overview of all your Kubernetes resources. [Orchestrator Explorer](https://app.datadoghq.com/orchestration/overview) allows you to monitor the state of pods, deployments, and other Kubernetes concepts in a specific namespace or availability zone, view resource specifications for failed pods within a deployment, correlate node activity with related logs, and more. The [Resource Utilization](https://app.datadoghq.com/orchestration/resource/pod) page provides insights into how your Kubernetes workloads are using your computing resources across your infrastructure. For information on how to use these pages, see [Orchestrator Explorer](https://docs.datadoghq.com/infrastructure/containers/orchestrator_explorer) and [Kubernetes Resource Utilization](https://docs.datadoghq.com/infrastructure/containers/kubernetes_resource_utilization).

### Enable features{% #enable-features %}

- [APM for Kubernetes: Set up and configure trace collection for your Kubernetes application.](https://docs.datadoghq.com/containers/kubernetes/apm)
- [Log collection in Kubernetes: Set up log collection in a Kubernetes environment.](https://docs.datadoghq.com/agent/kubernetes/log)
- [Prometheus & OpenMetrics: Collect your exposed Prometheus and OpenMetrics metrics from your application running inside Kubernetes.](https://docs.datadoghq.com/agent/kubernetes/prometheus)
- [Control plane monitoring: Monitor the Kubernetes API server, controller manager, scheduler, and etcd.](https://docs.datadoghq.com/agent/kubernetes/control_plane)
- [Further Configuration: Collect events, override proxy settings, send custom metrics with DogStatsD, configure container allowlists and blocklists, and reference the full list of available environment variables.](https://docs.datadoghq.com/agent/kubernetes/configuration)

## Further Reading{% #further-reading %}

- [Further Configure the Datadog Agent on Kubernetes](https://docs.datadoghq.com/agent/kubernetes/configuration)
- [Datadog Helm chart - All configuration options](https://github.com/DataDog/helm-charts/blob/main/charts/datadog/README.md#all-configuration-options)
- [Upgrading Datadog Helm](https://github.com/DataDog/helm-charts/blob/main/charts/datadog/README.md#upgrading)
