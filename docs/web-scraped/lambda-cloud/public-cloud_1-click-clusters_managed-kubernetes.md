# Using Lambda's Managed Kubernetes -

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/managed-kubernetes/

---

[1-click clusters](../../../tags/#tag:1-click-clusters)[kubernetes](../../../tags/#tag:kubernetes)

# Using Lambda's Managed Kubernetes

## Introduction

This guide walks you through getting started with [Lambda's Managed Kubernetes](https://lambda.ai/kubernetes)(MK8s) on a [1-Click Cluster](https://lambda.ai/service/gpu-cloud/1-click-clusters)(1CC).

MK8s provides a Kubernetes environment with GPU and InfiniBand (RDMA) support, and shared persistent storage across all nodes in a 1CC. Clusters are preconfigured so you can deploy workloads without additional setup.

In this guide, you'll learn how to:

- Access MK8s using `kubectl`.
- Grant access to additional users.
- Organize workloads using namespaces.
- Deploy and manage applications.
- Expose services using Ingresses.
- Use shared and node-local persistent storage.
- Monitor GPU usage with the NVIDIA DCGM Grafana dashboard.
This guide includes two examples:

In the first, you'll deploy a vLLM server to serve the [Nous Research Hermes 4](https://huggingface.co/NousResearch/Hermes-4-14B)model. You'll:

- Create a namespace for the examples.
- Add a PersistentVolumeClaim (PVC) to cache model downloads.
- Deploy the vLLM server.
- Expose it with a Service.
- Configure an Ingress to make it accessible externally.
In the second example, you'll evaluate the multiplication-solving accuracy of the [DeepSeek R1 Distill Qwen 7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)model using vLLM. You'll:

- Run a batch job that performs the evaluation.
- Monitor GPU utilization during the run.

## Prerequisites

You need the Kubernetes command-line tool, `kubectl`, to interact with MK8s. Refer to the Kubernetes documentation for [installation instructions](https://kubernetes.io/docs/tasks/tools/#kubectl).

You also need the `kubelogin`plugin for `kubectl`to authenticate to MK8s. Refer to the [kubelogin README for installation instructions](https://github.com/int128/kubelogin?tab=readme-ov-file#setup).

## Accessing MK8s

To access MK8s, you need to:

- Configure firewall rules to allow connections to MK8s.
- Configure `kubectl`to use the provided `kubeconfig`file.
- Authenticate to MK8s using your [Lambda Cloud account](https://cloud.lambda.ai).

### Configure firewall rules

To access MK8s, you must first create firewall rules for the MK8s API server and Ingress Controller:

-
Navigate to the **Global rules **tab on the [Firewall settings page](https://cloud.lambda.ai/firewall)in the Lambda Cloud console.

-
In the **Rules **section, click **Edit rules **to begin creating a rule.

-
Click **Add rule **, then set up the following rule:

- **Type **: Custom TCP
- **Protocol **: TCP
- **Port range **: `6443`
- **Source **: `0.0.0.0/0`
- **Description **: `MK8s API server`
-
Click **Add rule **again, then set up the following rule:

- **Type **: Custom TCP
- **Protocol **: TCP
- **Port range **: `443`
- **Source **: `0.0.0.0/0`
- **Description **: `MK8s Ingress Controller`
-
Click **Update firewall rules **.

### Configure `kubectl`

You're provided with a `kubeconfig`file when MK8s is provisioned. You need to set up `kubectl`to use this `kubeconfig`file:

-
Save the file to `~/.kube/config`. Alternatively, set the `KUBECONFIG`environment variable to the path of the file.

-
(Optional) Restrict access to the file:

```
`[](#__codelineno-0-1)chmod 600 ~/.kube/config
`
```
