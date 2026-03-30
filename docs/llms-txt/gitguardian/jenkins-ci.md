# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/jenkins-ci.md

# Jenkins CI

> Step-by-step guide to integrating ggshield secret scanning into Jenkins CI pipelines using the GitGuardian Docker image.

## Prelude

GitGuardian CI/CD integration with Jenkins CI is performed through our CLI application: [`ggshield`](../../getting-started.md).  
`ggshield` is a wrapper around the GitGuardian API for secrets detection, an API key is required for authentication.

## Preview

![Jenkins CI status](/img/ggshield/cicd-integrations/jenkins/status.png)

![Jenkins CI output](/img/ggshield/cicd-integrations/jenkins/jenkins-ci-ggshield-secret-scan-ci.png)

## Installation

> [Service accounts](../../../api-docs/service-accounts.md) are recommended to run this integration.
>
> Please note that service accounts are only available for workspaces under our Business plan, and their administration is restricted to Managers. If your workspace is under the Free plan, you can still use a [personal access token](../../../api-docs/personal-access-tokens.md) to run this integration.

1. Create a service account from the [API section](https://dashboard.gitguardian.com/workspace/api/service-accounts) of your GitGuardian workspace (or a [personal access token](https://dashboard.gitguardian.com/api/personal-access-tokens) if you are on the Free plan).
2. Add this API key to the `GITGUARDIAN_API_KEY` environment variable in your project settings.

![Bitbucket pipelines env](/img/ggshield/cicd-integrations/jenkins/env_variable_setting.png)

3. In order to add ggshield to your pipelines configure your `Jenkinsfile` to add a ggshield stage:

```groovy
pipeline {
    agent none
    stages {
        stage('GitGuardian Scan') {
            agent {
                docker { image 'gitguardian/ggshield:latest' }
            }
            environment {
                GITGUARDIAN_API_KEY = credentials('gitguardian-api-key')
            }
            steps {
                sh 'ggshield secret scan ci'
            }
        }
    }
}
```
