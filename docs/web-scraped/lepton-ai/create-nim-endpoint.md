# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/endpoints/create-from-nim

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



# Create Endpoints from NVIDIA NIM

Copy page

Learn how to create dedicated endpoints from NVIDIA NIM.

For enhanced performance and seamless compatibility, NVIDIAâoptimized models from the NIM container registry are available on DGX Cloud Lepton.

## Prerequisites

These models require an NVIDIA account with access to the NIM container registry.

### NVIDIA Registry

You must have an NVIDIA account with access to the NIM container registry and configure the [registry auth key](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html#launch-nvidia-nim-for-llms) on DGX Cloud Lepton.

Refer to [this guide](/dgx-cloud/lepton/features/workspace/registry/#nvidia) for details. Once the registry auth key is created, add a private registry via [Settings > Registries > New Registry Auth](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/settings/registries).

![Create registry auth](/dgx-cloud/lepton/_next/static/media/create-registry.3cb1ce7c.png)

Choose **NVIDIA** as the registry type and paste the registry auth key in the **API Key** field.

![Create registry auth](/dgx-cloud/lepton/_next/static/media/auth-key.856d395a.png)

### NGC API Key

Besides the registry auth key, you also need an [NGC API key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-api-keys). Navigate to the [NGC API key creation page](https://org.ngc.nvidia.com/setup/api-keys) and click **Generate Personal Key**.

In the **Service Included** field, select **Public API Endpoints**.

![NGC API key 0.6x](/dgx-cloud/lepton/_next/static/media/ngc-api-key.7bca824d.png)

Store the NGC API key on DGX Cloud Lepton as a [secret](/dgx-cloud/lepton/features/workspace/secret/).

## Create endpoint from NVIDIA NIM

Navigate to the [Create Endpoint](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/deployments/create/nim) page on the dashboard.

For **Endpoint name** , enter `nim-endpoint` or any name you prefer.

For **Resource** , choose an appropriate resource based on the model size.

For **NIM configuration** :

  * Select a model image from the list of builtâin models, or enter a custom model image.
  * Select the NVIDIA registry auth you created (see [registry auth](/dgx-cloud/lepton/features/workspace/registry/#nvidia)).
  * Select the NGC API key you saved as a [secret](/dgx-cloud/lepton/features/workspace/secret/) in your workspace.



For other endpointârelated configurations, refer to [this guide](/dgx-cloud/lepton/features/endpoints/configurations/).

For NIM engineârelated configurations, refer to [this guide](https://docs.nvidia.com/nim/large-language-models/latest/configuration.html#environment-variables). Configure the NIM engine by setting the relevant environment variables.

When finished, click **Create Endpoint** to create the endpoint.

[Create Endpoints from Container Image](/dgx-cloud/lepton/features/endpoints/create-from-container-image/)[Create LLM Endpoints](/dgx-cloud/lepton/features/endpoints/create-llm/)

Prerequisites

Create endpoint from NVIDIA NIM

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
