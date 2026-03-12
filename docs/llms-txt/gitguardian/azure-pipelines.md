# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/azure-pipelines.md

# Azure pipelines

> Step-by-step guide to integrating ggshield secret scanning into Azure Pipelines using the GitGuardian Docker image.

## Prelude

GitGuardian CI/CD integration with Azure Pipelines is performed through our CLI application: [`ggshield`](../../getting-started.md).  
`ggshield` is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

> â  Azure Pipelines does not support commit ranges outside of GitHub Pull Requests, therefore on push events in a regular branch only your latest commit will be scanned.
> This limitation doesn't apply to GitHub Pull Requests where all the commits in the pull request will be scanned.

## Preview

![Azure Pipelines output](/img/ggshield/cicd-integrations/azure_pipelines/azure-pipelines-secret-scan-ci.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `gitguardianApiKey` secret variable in your pipeline settings.

   - [How to define secret variables in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#secret-variables)

3. Add a new job using ggshield to your Azure pipeline

```yaml
jobs:
  - job: GitGuardianShield
    pool:
      vmImage: 'ubuntu-latest'
    container: gitguardian/ggshield:latest
    steps:
      - script: ggshield secret scan ci
        env:
          GITGUARDIAN_API_KEY: $(gitguardianApiKey)
```
