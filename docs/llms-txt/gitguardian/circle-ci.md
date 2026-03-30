# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/circle-ci.md

# CircleCI

> Step-by-step guide to integrating ggshield secret scanning into CircleCI using the ggshield-orb.

## Prelude

GitGuardian CI/CD integration with CircleCI is performed through our CLI application: [`ggshield`](../../getting-started.md).  
ggshield is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

CircleCI is supported in `ggshield` through [ggshield-orb](https://github.com/GitGuardian/gg-shield-orb).

## Preview

![CircleCI output](/img/ggshield/cicd-integrations/circle_ci/output.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings.
3. In order to add ggshield to your pipelines configure your `.circleci/config.yml` add the ggshield orb:

```yaml
orbs:
  ggshield: gitguardian/ggshield

workflows:
  main:
    jobs:
      - ggshield/scan:
          name: ggshield-scan # best practice is to name each orb job
          base_revision: << pipeline.git.base_revision >>
          revision: <<pipeline.git.revision>>
```
