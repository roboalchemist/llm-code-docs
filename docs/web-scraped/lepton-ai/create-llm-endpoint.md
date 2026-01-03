# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/endpoints/create-llm

Toggle Menu

Menu

[](/dgx-cloud/lepton/)

Get Started

  * [Introduction](/dgx-cloud/lepton/get-started/)
  * [Endpoint](/dgx-cloud/lepton/get-started/endpoint/)
  * [Dev Pod](/dgx-cloud/lepton/get-started/dev-pod/)
  * [Batch Job](/dgx-cloud/lepton/get-started/batch-job/)
  * [Node Group](/dgx-cloud/lepton/get-started/node-group/)
  * [Workspace](/dgx-cloud/lepton/get-started/workspace/)



Compute

  * Bring Your Own Compute



Features

  * Endpoints
  * Dev Pods
  * Batch Jobs
  * Nodes
  * Clusters
  * Utilities
  * Workspace



Examples

  * Batch Job
  * Connections
  * Dev Pod
  * Endpoint
  * Fine Tuning
  * Raycluster



Reference

  * CLI
  * [Python SDK Reference](/dgx-cloud/lepton/reference/api/)
  * Workload Identity
  * Limits
  * [Support](/dgx-cloud/lepton/reference/support/)



# Create LLM Endpoints

Copy page

Learn how to deploy LLM endpoints on DGX Cloud Lepton.

In this guide, we'll show you how to create a dedicated endpoint from LLMs with inference engine vLLM and SGLang to serve models from Hugging Face.

## Create LLM Endpoints with vLLM

[vLLM](https://docs.vllm.ai/en/latest/) is a fast and easy-to-use library for LLM inference and serving. To create a dedicated endpoint with vLLM, follow these steps:

  1. Go to the [Endpoints](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/list?creation=true) page and click **Create Endpoint**.
  2. Select **Create LLM Endpoint**.
  3. Select **vLLM** as the inference engine.
  4. For **Endpoint name** , enter `vllm-endpoint` or any name you prefer.
  5. For **Model** , click **Load from Hugging Face** and search by keyword. For example, `meta-llama/Llama-3.1-8B-Instruct`. If the model is gated, provide a Hugging Face token. Create a token in your [Hugging Face account](https://huggingface.co/settings/tokens) and save it as a secret in your workspace.
  6. For **Resource** , choose an appropriate resource based on the model size.
  7. For **Image configuration** , leave defaults as is. To add arguments, expand the command-line arguments section and add your own. vLLM arguments are listed [here](https://docs.vllm.ai/en/latest/serving/engine_args.html).
  8. Leave other configurations at their defaults, or refer to [endpoint configurations](/dgx-cloud/lepton/features/endpoints/configurations/) for details.



We recommend setting up an access token for your endpoint instead of making it public.

Once created, the endpoint appears on the [Endpoints](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/list) page. View logs for each replica by clicking the Logs button in the Replica section.

Test the endpoint in the playground by clicking the endpoint you created.

To access the endpoint via API, click the API tab on the endpoint detail page to find the API key and endpoint URL.

## Create LLM Endpoints with SGLang

[SGLang](https://docs.sglang.ai/) is a fast serving framework for large language models and vision language models. It enables faster, more controllable interactions by co-designing the backend runtime and frontend language. To create a dedicated endpoint with SGLang, follow these steps:

  1. Go to the [Endpoints](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/list?creation=true) page and click **Create Endpoint**.
  2. Select **Create LLM Endpoint**.
  3. Select **SGLang** as the inference engine.
  4. For **Endpoint name** , enter `sglang-endpoint` or any name you prefer.
  5. For **Model** , click **Load from Hugging Face** and search by keyword. For example, `meta-llama/Llama-3.1-8B-Instruct`. If the model is gated, provide a Hugging Face token. Create a token in your [Hugging Face account](https://huggingface.co/settings/tokens) and save it as a secret in your workspace.
  6. For **Resource** , choose an appropriate resource based on the model size.
  7. For **Image configuration** , leave defaults as is. To add arguments, expand the command-line arguments section and add your own. SGLang arguments are listed [here](https://docs.sglang.ai/backend/server_arguments.html).
  8. Leave other configurations at their defaults, or refer to [endpoint configurations](/dgx-cloud/lepton/features/endpoints/configurations/) for details.



We recommend setting up an access token for your endpoint instead of making it public.

Once created, the endpoint appears on the [Endpoints](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/list) page. View logs for each replica by clicking the Logs button in the Replica section.

Test the endpoint in the playground by clicking the endpoint you created.

To access the endpoint via API, click the API tab on the endpoint detail page to find the API key and endpoint URL.

[Create Endpoints from NVIDIA NIM](/dgx-cloud/lepton/features/endpoints/create-from-nim/)[Dev Pod Configurations](/dgx-cloud/lepton/features/dev-pods/configurations/)

Create LLM Endpoints with vLLM

Create LLM Endpoints with SGLang

[](/dgx-cloud/lepton/)

### Corporate Info

  * [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)
  * [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/)
  * [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
  * [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/)



### NVIDIA Developer

  * [Developer Home](https://developer.nvidia.com/)
  * [Blog](https://blogs.nvidia.com/)



### Resources

  * [Contact Us](https://www.nvidia.com/en-us/contact/)
  * [Developer Program](https://developer.nvidia.com/developer-program)



Copyright @ 2025, NVIDIA Corporation.
