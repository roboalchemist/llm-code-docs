# Deploying Llama 3.2 3B in a Kubernetes (K8s) cluster -

Source: https://docs.lambda.ai/education/large-language-models/k8s-ollama-llama-3-2/

---

[api](../../../tags/#tag:api)[kubernetes](../../../tags/#tag:kubernetes)[llama](../../../tags/#tag:llama)[llm](../../../tags/#tag:llm)

# Deploying Llama 3.2 3B in a Kubernetes (K8s) cluster [#](#deploying-llama-32-3b-in-a-kubernetes-k8s-cluster)

## Introduction [#](#introduction)

In this tutorial, you'll:

- Stand up a single-node Kubernetes cluster on an [on-demand instance](https://lambda.ai/service/gpu-cloud)using [K3s](https://k3s.io/).
- Install the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)so your cluster can use your instance's GPUs.
- Deploy [Ollama](https://ollama.com/)in your cluster to serve the [Llama 3.2 3B model](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/).
- Install the Ollama client.
- Interact with the Llama 3.2 3B model.
Note

You don't need a Kubernetes cluster to run Ollama and serve the Llama 3.2 3B model. Part of this tutorial is to demonstrate that it's possible to stand up a Kubernetes cluster on on-demand instances.
