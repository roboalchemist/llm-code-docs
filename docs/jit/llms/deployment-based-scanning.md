# Source: https://docs.jit.io/docs/deployment-based-scanning.md

# Deployment-Based Scanning

## Overview

Jit offers the option to trigger runtime scanning tools when a new code deployment is detected. Scanning runtime environments every time a deployment occurs reduces the chances of security issues finding their way onto runtime environments.

Deployment-based scanning is available for the following security requirements—

* [Ensure Your APIs are Secure](https://docs.jit.io/docs/ensure-your-api-is-secure)
* [Scan Your Web Application for Vulnerabilities](https://docs.jit.io/docs/run-a-web-application-scanner)

## Prerequisites

1. **Deployment via Github actions** Jit deployment scanning currently only supports deployments via **Github actions**. Support for more deployment services is coming soon. In order to use deployment scanning, a deployment job must be included in the Github actions workflow. Jit looks for the `environments:<name>` tag in the workflow YAML to determine if a deployment has occurred and will look for the environment name to know which runtime environment to scan. Learn more about [deployments with Github actions](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions).

```yaml Deployment YAML file (example)
name: 'Deploy to staging'

on:
  push:
    branches:
      - dev
      - main
  pull_request:
    branches:
      - main
jobs:
  deploy-staging:
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
```

2. [Slack integration](https://docs.jit.io/docs/integrating-with-slack) is required to enable deployment scanning.

## Configuring deployment scanning

When activating one of the supported security controls, set the *trigger* in the control configuration to *Scan on deployment*:

Under `Environment name` enter the environment defined in the deployment YAML on Github actions. Jit needs an exact match between the environment name defined on Jit and on Github Actions to trigger a scan.

**Note** - Environment names are global. When you change it in any control configuration, it will change on all controls.

## Slack notifications

Jit requires an active [Slack integration](https://docs.jit.io/docs/integrating-with-slack) to enable deployment scanning. You can configure Slack via the [Integrations page](https://docs.jit.io/docs/integrations-page) or when configuring a security control that supports deployment scanning.

When a deployment scan detects findings, it will report them in two places:

1. The [pipelines](https://docs.jit.io/docs/pipelines-page) page, under a *Deployment* pipeline.
2. A Slack notification, sent to the selected channel under *Deployments* in the Slack integration configuration: