# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/drone-ci.md

# Drone CI

> Step-by-step guide to integrating ggshield secret scanning into Drone CI pipelines using the GitGuardian Docker image.

## Prelude

GitGuardian CI/CD integration with Drone CI is performed through our CLI application: [`ggshield`](../../getting-started.md).  
`ggshield` is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

## Preview

![Drone CI](/img/ggshield/cicd-integrations/drone_ci/drone-ci-ggshield-secret-scan-ci.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings. It should be available for Drone CI runners.
3. In order to add ggshield to your pipelines, configure your `.drone.yml` to add a ggshield scanning step.

```yml
kind: pipeline
type: docker
name: default

steps:
  - name: ggshield
    image: gitguardian/ggshield:latest
    commands:
      - ggshield secret scan ci
```
