# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/travis-ci.md

# Travis CI

> Step-by-step guide to integrating ggshield secret scanning into Travis CI pipelines.

## Prelude

GitGuardian CI/CD integration with Travis CI is performed through our CLI application: [`ggshield`](../../getting-started.md).  
`ggshield` is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings.
3. In order to add ggshield to your pipelines, configure your `.travis.yml` to add a ggshield scanning job.

```yml
jobs:
  include:
    - name: GitGuardian Scan
      language: python
      python: 3.8
      install:
        - pip install ggshield
      script:
        - ggshield secret scan ci
```

For further explanations about how to define encrypted variables in Travis CI, please read [their documentation](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml).

<!-- Add image with ggshield integrated into the travis CI  -->
