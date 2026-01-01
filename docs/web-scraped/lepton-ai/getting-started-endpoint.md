# Source: https://docs.nvidia.com/dgx-cloud/lepton/get-started/endpoint

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



# Endpoint

Copy page

Learn how to create and use endpoints on DGX Cloud Lepton for AI model deployment.

An **Endpoint** is a running instance of an AI model that exposes an HTTP server.

DGX Cloud Lepton lets you deploy AI models as endpoints, making them accessible via high-performance, scalable REST APIs.

## Create an Endpoint

Navigate to the [create LLM endpoint page](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/create/vllm).

Select vLLM as the LLM engine, and load a model from Hugging Face in the **Model** section. In this case, we will use the `nvidia/Nemotron-Research-Reasoning-Qwen-1.5B` model.

Then, in the **Resource** section, select the node group and your desired resource shape. In this case, use `H100-80GB-HBM3` x 1 from node group `h100`.

![create endpoint 0.8x](/dgx-cloud/lepton/_next/static/media/create.8b91d829.png)

Click **Create** to deploy an endpoint that:

  * Uses one H100 GPU from node group `h100`
  * Deploys the `nvidia/Nemotron-Research-Reasoning-Qwen-1.5B` model with vLLM



You need to have a [node group](/dgx-cloud/lepton/get-started/node-group/) with available nodes in your workspace first.

## Use the Endpoint

By default, the endpoint is public and can be accessed by anyone with the URL. Refer to the [endpoint configurations](/dgx-cloud/lepton/features/endpoints/configurations/) for managing endpoint access control.

### Playground

After the endpoint is created, the endpoint details page shows a chat playground where you can interact with the deployed model.

![endpoint playground 0.8x](/dgx-cloud/lepton/_next/static/media/endpoint-playground.330bf8c8.png)

### API Request

You can also use the endpoint URL to make API requests. Go to the **API** tab on the endpoint details page for details.

For example, you can use the following command to list the available models in the endpoint.


## Next Steps

For more information about endpoints, refer to the following:

  * [Endpoint configurations](/dgx-cloud/lepton/features/endpoints/configurations/)
  * [Create endpoints from NVIDIA NIM](/dgx-cloud/lepton/features/endpoints/create-from-nim/)
  * [Create LLM endpoints](/dgx-cloud/lepton/features/endpoints/create-llm/)
  * [Create endpoints from container image](/dgx-cloud/lepton/features/endpoints/create-from-container-image/)



[Introduction](/dgx-cloud/lepton/get-started/)[Dev Pod](/dgx-cloud/lepton/get-started/dev-pod/)

Create an Endpoint

Use the Endpoint

Next Steps

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
