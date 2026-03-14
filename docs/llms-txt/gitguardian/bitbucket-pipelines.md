# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/bitbucket-pipelines.md

# Bitbucket pipelines

> Step-by-step guide to integrating ggshield secret scanning into Bitbucket Pipelines using the GitGuardian Docker image.

## Prelude

GitGuardian CI/CD integration with Bitbucket pipeline is performed through our CLI application: [`ggshield`](../../getting-started.md).  
`ggshield` is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

> â  Bitbucket pipelines do not support commit ranges therefore only your latest commit in a pushed group or in a new branch will be scanned.

## Preview

![Bitbucket pipeline output](/img/ggshield/cicd-integrations/bitbucket_pipelines/bitbucket-pipelines-ggshield-secret-scan-ci.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

![Bitbucket pipelines env](/img/ggshield/cicd-integrations/bitbucket_pipelines/env_variable_setting.png)

3. Add a new step using ggshield to your Bitbucket repository's pipeline.

```yaml
stages:
  - scanning

gitguardian scan:
  image: gitguardian/ggshield:latest
  stage: scanning
  script: ggshield secret scan ci
```

> You may be interested in using GitGuardian's [Bitbucket integration](../../../internal-monitoring/integrate-sources/vcs-integrations/bitbucket.md) to ensure full coverage of your Bitbucket repositories as well as full git history scans and reporting.
