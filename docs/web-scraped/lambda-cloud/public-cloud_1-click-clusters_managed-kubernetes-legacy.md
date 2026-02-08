# Using Lambda's Managed Kubernetes -

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/managed-kubernetes-legacy/

---

[1-click clusters ](../../../tags/#tag:1-click-clusters)[kubernetes ](../../../tags/#tag:kubernetes)
# Using Lambda's Managed Kubernetes [# ](#using-lambdas-managed-kubernetes)

## Introduction [# ](#introduction)

This guide walks you through getting started with [Lambda's Managed Kubernetes ](https://lambda.ai/kubernetes)(MK8s) on a [1-Click Cluster ](https://lambda.ai/service/gpu-cloud/1-click-clusters)(1CC). 

MK8s provides a Kubernetes environment with GPU support, InfiniBand (RDMA), and shared persistent storage across all nodes in a 1CC. Clusters are preconfigured so you can deploy workloads without additional setup. 

You'll learn how to: 

- Access MK8s using the Rancher Dashboard and `kubectl`. 
- Organize workloads using projects and namespaces. 
- Deploy and manage applications. 
- Expose services using Ingresses. 
- Use shared and node-local persistent storage. 
- Monitor GPU usage with the NVIDIA DCGM Grafana dashboard. 
The guide includes two examples. 

In the first, you'll deploy a vLLM server to serve the [NousResearch Hermes 3 ](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B)model: 

- Create a namespace for the examples. 
- Add a PersistentVolumeClaim (PVC) to cache model downloads. 
- Deploy the vLLM server. 
- Expose it with a Service. 
- Configure an Ingress to make it accessible externally. 
In the second, you'll evaluate the multiplication-solving accuracy of the [DeepSeek R1 Distill Llama 70B ](https://lambda.ai/inference-models/deepseek-llama3.3-70b)model using vLLM: 

- Run a batch job that performs the evaluation. 
- Monitor GPU utilization during the run. 
## Prerequisites [# ](#prerequisites)

You need the Kubernetes command-line tool, `kubectl`, to interact with the cluster. Refer to the Kubernetes documentation for [installation instructions ](https://kubernetes.io/docs/tasks/tools/#kubectl). 

## Accessing MK8s [# ](#accessing-mk8s)

After your 1CC with MK8s is provisioned, you'll receive credentials to access MK8s. These include the Rancher Dashboard URL, username, and password. 

To access MK8s using either the Rancher Dashboard or `kubectl`, you must first configure a firewall rule: 

- 
In the Cloud dashboard, go to the [Firewall ](https://cloud.lambda.ai/firewall)page. 

- 
Click **Edit **to modify the inbound firewall rules. 

- 
Click **Add rule **, then set up the following rule: 

  - **Type **: Custom TCP 
  - **Protocol **: TCP 
  - **Port range **: `443`
  - **Source **: `0.0.0.0/0`
  - **Description **: `Managed Kubernetes dashboard`
- 
Click **Update and save **. 

### Rancher Dashboard [# ](#rancher-dashboard)

To access the MK8s Rancher Dashboard: 

- 
In your browser, go to the URL provided along with your MK8s credentials. You'll see a login screen. 

- 
Enter your username and password, then click **Log in with Local User **. 

- 
In the left sidebar, click the **Local Cluster **button: 

[![Screenshot of Local Cluster button](../../../assets/images/managed-kubernetes/local-cluster-button.png)](../../../assets/images/managed-kubernetes/local-cluster-button.png)

### kubectl [# ](#kubectl)

To access MK8s using `kubectl`: 

- 
Open the Rancher Dashboard as described above. 

- 
In the top-right corner, click the **Download KubeConfig **button: 

[![Screenshot of Download KubeConfig button](../../../assets/images/managed-kubernetes/download-kubeconfig-button.png)](../../../assets/images/managed-kubernetes/download-kubeconfig-button.png)

- 
Save the file to `~/.kube/config`. Alternatively, set the `KUBECONFIG`environment variable to the path of the file. 

- 
(Optional) Restrict access to the file: 

```
`[](#__codelineno-0-1)chmod 600 ~/.kube/config
`
```
