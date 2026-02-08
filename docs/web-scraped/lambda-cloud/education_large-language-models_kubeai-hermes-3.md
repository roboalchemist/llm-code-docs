# Using KubeAI to deploy Nous Research's Hermes 3 and other LLMs -

Source: https://docs.lambda.ai/education/large-language-models/kubeai-hermes-3/

---

[kubernetes ](../../../tags/#tag:kubernetes)[llama ](../../../tags/#tag:llama)[llm ](../../../tags/#tag:llm)
# Using KubeAI to deploy Nous Research's Hermes 3 and other LLMs [# ](#using-kubeai-to-deploy-nous-researchs-hermes-3-and-other-llms)

## Introduction [# ](#introduction)

[See our video tutorial on using KubeAI to deploy Nous Research's Hermes 3 and other LLMs. ](https://youtu.be/HEtPO2Wuiac?)

[KubeAI: Private Open AI on Kubernetes ](https://github.com/substratusai/kubeai)is a Kubernetes solution for running inference on open-weight large language models (LLMs), including [Nous Research's Hermes 3 fine-tuned Llama 3.1 8B model ](https://nousresearch.com/hermes3/)and [NVIDIA's Nemotron fine-tuned Llama 3.1 70B model ](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct). 

Using model servers such as [vLLM ](https://blog.vllm.ai/2023/06/20/vllm.html)and [Ollama ](https://ollama.com/), KubeAI enables you to interact with LLMs using both a web UI powered by [Open WebUI ](https://openwebui.com/)and an OpenAI-compatible API. 

In this tutorial, you'll: 

- Stand up a single-node Kubernetes cluster on an 8x H100 [on-demand instance ](https://lambda.ai/service/gpu-cloud)using [K3s ](https://k3s.io/). 
- Install the [NVIDIA GPU Operator ](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)so your Kubernetes cluster can use your instance's GPUs. 
- Deploy KubeAI in your Kubernetes cluster to serve both Nous Research's Hermes 3 model and NVIDIA's Nemotron model. 
- Interact with the models using KubeAI's web UI. 
- Interact with the models using KubeAI's OpenAI-compatible API. 
- Use [NVTOP ](https://github.com/Syllo/nvtop)to observe GPU utilization. 
## Stand up a single-node Kubernetes cluster [# ](#stand-up-a-single-node-kubernetes-cluster)

- 
Use the [console ](https://cloud.lambda.ai/instances)or [Cloud API ](https://docs.lambda.ai/api/cloud#launchInstance)to launch an 8x H100 instance. Then, SSH into your instance by running: 

```
`[](#__codelineno-0-1)ssh ubuntu@<INSTANCE-IP-ADDRESS> -L 8080:localhost:8080
`
```
