# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/gitlab-pipelines.md

# GitLab pipelines

> Step-by-step guide to integrating ggshield secret scanning into GitLab CI/CD pipelines using the GitGuardian Docker image.

## Prelude

GitGuardian CI/CD integration with GitLab CI/CD is performed through our CLI application: [`ggshield`](../../getting-started.md).  
ggshield is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

**Note:** If you want to ensure full coverage of your GitLab projects as well as full git history scans and reporting, you may be interested in using GitGuardian's [GitLab integration](../../../internal-monitoring/integrate-sources/vcs-integrations/gitlab.md).

## Preview

![GitLab pipelines status](/img/ggshield/cicd-integrations/gitlab_pipelines/status.png)

![GitLab pipelines output](/img/ggshield/cicd-integrations/gitlab_pipelines/gl-pipelines-ggshield-secret-scan-ci.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

![GitLab CI/CD env](/img/ggshield/cicd-integrations/gitlab_pipelines/env_variable_setting.png)

3. Add a new step using ggshield to your GitLab project's pipeline.

```yaml
stages:
  - scanning

gitguardian scan:
  image: gitguardian/ggshield:latest
  stage: scanning
  script: ggshield secret scan ci
```

## Additional notes

> For ggshield to scan every commit in a merge request pipeline the CI
> must clone the full repository instead of just fetching the branch.
> The following snippet ensures this behavior.

```yml
variables:
GIT_STRATEGY: clone
GIT_DEPTH: 0
```
