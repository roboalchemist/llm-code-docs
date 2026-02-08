# Deploying a Llama 3 inference endpoint -

Source: https://docs.lambda.ai/education/large-language-models/deploying-a-llama-3-inference-endpoint/

---

# Deploying a Llama 3 inference endpoint [# ](#deploying-a-llama-3-inference-endpoint)

Meta's Llama 3 large language models (LLMs) feature generative text models recognized for their state-of-the-art performance in common industry benchmarks. 

This guide covers the deployment of a Meta [Llama 3 ](https://llama.meta.com/llama3/)inference endpoint using Lambda [On-Demand Cloud ](https://lambda.ai/service/gpu-cloud). This tutorial uses the Llama 3 models hosted by [Hugging Face ](https://huggingface.co/meta-llama/Meta-Llama-3-8B). 

The model is available in 8B and 70B sizes: 
Model Size Characteristics 8B (8 billion parameters) More efficient and accessible, suitable for tasks where resources are constrained. The 8B model requires a 1x A100 or H100 GPU node. 70B (70 billion parameters) Superior performance and capabilities ideal for complex or high-stakes applications. The 70B model requires an 8x A100 or H100 GPU node. 
### Prerequisites [# ](#prerequisites)

This tutorial assumes the following prerequisites: 

- Lambda On-Demand Cloud instances appropriate for the Llama 3 model size you want to run. 
  - Model 8B ( [meta-llama/Meta-Llama-3-8B) ](https://huggingface.co/meta-llama/Meta-Llama-3-8B)requires 1x A100 or H100 GPU node. 
  - Model 70B ( [meta-llama/Meta-Llama-3-70B) ](https://huggingface.co/meta-llama/Meta-Llama-3-70B)requires 8x A100 or H100 GPU nodes. 
- A Hugging Face [user account ](https://huggingface.co/join). 
- An approved [Hugging Face user access token ](https://huggingface.co/docs/hub/en/security-tokens)that includes repository read permissions for the meta-llama-3 model repository you wish to use. 
JSON outputs in this tutorial are formatted using [jq ](https://jqlang.github.io/jq/). 

### Set up the inference point [# ](#set-up-the-inference-point)

Once you have the appropriate Lambda On-Demand Cloud instances and Hugging Face permissions, begin by setting up an inference point. 

- [Launch your Lambda On-Demand Cloud instance ](https://cloud.lambda.ai/sign-up). 
- [Add or generate an SSH key ](../../../public-cloud/console/#add-generate-and-delete-ssh-keys)to access the instance. 
- SSH into your instance. 
- 
Create a dedicated python environment. 
Llama3 8b Llama3 70b
