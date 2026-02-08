# Serving Llama 3.1 405B on a Lambda 1-Click Cluster -

Source: https://docs.lambda.ai/education/large-language-models/serving-llama-3-1-405b/

---

# Serving Llama 3.1 405B on a Lambda 1-Click Cluster [# ](#serving-llama-31-405b-on-a-lambda-1-click-cluster)

In this tutorial, you'll learn how to use a 1-Click Cluster (1CC) to serve the [Meta Llama 3.1 405B model ](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B)using [vLLM ](https://docs.vllm.ai/en/latest/index.html)with pipeline parallelism. 

## Prerequisites [# ](#prerequisites)

For this tutorial, you need: 

- A [Lambda Cloud account ](https://cloud.lambda.ai/sign-up). 
- A [1-Click Cluster ](https://lambda.ai/service/gpu-cloud/1-click-clusters). 
- A [Hugging Face ](https://huggingface.co/)account to download the Llama 3.1 405B model. 
- A [User Access Token ](https://huggingface.co/docs/hub/en/security-tokens)with the **Read **role. 
- Before you can download the Llama 3.1 405B model, you need to review and accept the model's license agreement. Once you accept the agreement, a request to access the repository will be submitted for approval; approval tends to be fast. You can see the status of the request in your [Hugging Face account settings ](https://huggingface.co/settings/gated-repos). 
### Download the Llama 3.1 405B model and set up a head node [# ](#download-the-llama-31-405b-model-and-set-up-a-head-node)

First, follow the [instructions for accessing your 1CC ](../../../public-cloud/1-click-clusters/#accessing-your-1-click-cluster), which includes steps to set up SSH. 

Then SSH into one of your 1CC GPU nodes. You can find the node names on the [1-Click Clusters ](https://cloud.lambda.ai/one-click-clusters/running)page in the Lambda Cloud console. You’ll use this GPU node as a head node for cluster management. 

On the head node, set environment variables needed for this tutorial by running: 

```
`[](#__codelineno-0-1)export HEAD_IP=HEAD-IP
[](#__codelineno-0-2)export SHARED_DIR=/home/ubuntu/FILE-SYSTEM-NAME
[](#__codelineno-0-3)export HF_TOKEN=HF-TOKEN
[](#__codelineno-0-4)export HF_HOME="${SHARED_DIR}/.cache/huggingface"
[](#__codelineno-0-5)export MODEL_REPO=meta-llama/Meta-Llama-3.1-405B-Instruct
`
```
