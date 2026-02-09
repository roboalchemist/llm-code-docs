# Serving the Llama 3.1 8B and 70B models using Lambda Cloud on-demand instances -

Source: https://docs.lambda.ai/education/large-language-models/serving-llama-3-1-docker/

---

[docker](../../../tags/#tag:docker)[llama](../../../tags/#tag:llama)[llm](../../../tags/#tag:llm)

# Serving the Llama 3.1 8B and 70B models using Lambda Cloud on-demand instances [#](#serving-the-llama-31-8b-and-70b-models-using-lambda-cloud-on-demand-instances)

This tutorial shows you how to use a [Lambda Cloud](https://lambda.ai/service/gpu-cloud)1x or 8x A100 or H100 on-demand instance to serve the Llama 3.1 8B and 70B models. You'll serve the model using [vLLM running inside of a Docker container](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html).

## Start the vLLM API server [#](#start-the-vllm-api-server)

If you haven't already, use the [console](https://cloud.lambda.ai/instances)or [Cloud API](https://docs.lambda.ai/api/cloud)to launch an instance. Then, SSH into your instance.

Run:

```bash
`[](#__codelineno-0-1)export HF_TOKEN=HF-TOKEN HF_HOME="/home/ubuntu/.cache/huggingface" MODEL_REPO=meta-llama/MODEL
`

```
