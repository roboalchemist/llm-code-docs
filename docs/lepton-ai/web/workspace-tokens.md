# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/workspace/token

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



# Token

Copy page

Learn about Lepton's authentication tokens, including User and Workspace tokens, and how to use them securely with the API, CLI, and SDKs.

Tokens could be used to authenticate and authorize requests to DGX Cloud Lepton. They are essential for logging in via the CLI, API, or SDKs.

Keep your tokens secure and do not share them with others.

## Creating Tokens

You can create a new token on the [**Settings - Tokens**](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/settings/api-tokens) tab on the left-hand side of the workspace settings page. When creating a new token, following fields can be configured based on your needs:

  * Token Name: The name of the token.
  * Expiration: The expiration time of the token. Default to 1 day.



![Create token 0.6x](/dgx-cloud/lepton/_next/static/media/create.74d59d5e.png)

## Viewing Tokens

You can view your tokens on the **Token** tab on the left-hand side of the workspace settings page.

![Tokens](/dgx-cloud/lepton/_next/static/media/tokens.46c118c1.png)

You can only see the tokens created by you in the list.

## Using Tokens

Token can be used to authenticate requests to the Lepton API. Simply include the token in the `Authorization` header of your request:


Workspace ID could be found on the [**Settings - General**](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/settings/workspace).

[Templates](/dgx-cloud/lepton/features/workspace/templates/)[Distributed Training with MPI](/dgx-cloud/lepton/examples/batch-job/distributed-training-with-mpi/)

Creating Tokens

Viewing Tokens

Using Tokens

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
