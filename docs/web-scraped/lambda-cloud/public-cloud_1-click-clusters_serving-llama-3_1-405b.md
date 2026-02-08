# How to serve the Llama 3.1 405B model using a Lambda 1-Click Cluster -

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/serving-llama-3_1-405b/

---

[1-click clusters ](../../../tags/#tag:1-click-clusters)[distributed training ](../../../tags/#tag:distributed-training)
# How to serve the Llama 3.1 405B model using a Lambda 1-Click Cluster [# ](#how-to-serve-the-llama-31-405b-model-using-a-lambda-1-click-cluster)

In this tutorial, you'll learn how to use a 1-Click Cluster (1CC) to serve the [Meta Llama 3.1 405B model ](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B)using [vLLM ](https://docs.vllm.ai/en/latest/index.html)with pipeline parallelism. 

Note 

You need a [Hugging Face ](https://huggingface.co/)account to download the Llama 3.1 405B model. You also need a [User Access Token ](https://huggingface.co/docs/hub/en/security-tokens)with the **Read **role. 

Before you can download the Llama 3.1 405B model, you need to review and accept the model's license agreement. Once you accept the agreement, a request to access the repository will be submitted. 

You can see the status of the request in your [Hugging Face account settings ](https://huggingface.co/settings/gated-repos).
