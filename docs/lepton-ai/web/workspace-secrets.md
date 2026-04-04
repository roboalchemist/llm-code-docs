# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/workspace/secret

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



# Secrets

Copy page

Securely store and manage sensitive information like API keys and credentials in DGX Cloud Lepton, and use them in your deployments and jobs.

Secrets are a secure and reusable way to add credentials and other sensitive information to your workspace. You can use secrets to store sensitive data, such as passwords, API keys, and tokens, and then reference them in your deployments, jobs, and pods.

Secrets are similar to environment variables, but the actual value is no longer editable or revealable once created.

## Managing Secrets

Navigate to the **Secrets** tab on the left-hand side of the workspace settings page. You will see a list of all the secrets you have created. You can add, edit, or delete secrets from this page.

![secrets list](/dgx-cloud/lepton/_next/static/media/secrets.4c557d1c.png)

We provide quick ways to add SSH public keys, GitHub, Hugging Face, OpenAI, Datadog tokens, NGC API keys, and custom secrets as secrets to your workspace. All secrets are stored and associated with the workspace in which they are created.

### Visibility

For every secret, you can set the visibility to **Public** or **Private**.

  * **Public** : The secret is visible to all users in the workspace.
  * **Private** : The secret is only visible to you, the user who created it.



By default, all secrets are created as private.

## Using Secrets

On the dashboard, you can add secrets as environment variables to your deployments, jobs, and pods. Configure them under advanced settings when creating or editing a deployment, job, or pod.

To access the secret value in the deployment, you can use the `os` module:


[Roles and Permissions](/dgx-cloud/lepton/features/workspace/roles-and-permissions/)[Templates](/dgx-cloud/lepton/features/workspace/templates/)

Managing Secrets

Using Secrets

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
