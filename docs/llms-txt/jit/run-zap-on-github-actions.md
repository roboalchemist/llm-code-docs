# Source: https://docs.jit.io/docs/run-zap-on-github-actions.md

# Run ZAP-Based Security Controls on a GitHub-Hosted Runner

## Overview

This page explains how to run ZAP-based security controls on a GitHub-hosted runner rather than Jit's job execution system. You may want to do this if the access to your WebApp is protected (no public IP / WAF).

ZAP-based security controls include the following:

* [Ensure Your APIs are Secure (DAST)](https://docs.jit.io/docs/ensure-your-api-is-secure)
* [Scan Your Web Application for Vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner)

## Using the GitHub-hosted runner

> 📘
>
> Jit's configuration files, such as `jit-plan.yml`,`jit-security.yml`, and `jit-config.yml`, are located in the `.jit` directory of the repository you selected for GitHub integration.

Before doing the following steps, open the jit platform and activate the relevant ZAP plan item in the Jit Max Security Plan for Cloud Applications plan.

![](https://files.readme.io/b5f447d0772f6031ff274461d0cf396b27993bc2e0216ca3f6aa9f46851004c7-image.png)

Once activated, you will be prompted to configure the application to be scanned:

Click on "Add application" and fill up the application details.

![](https://files.readme.io/35b3e55f9df60c9dee8d491ea7781425e24431779a4040c58dd5ca9d1aecc4aa-image.png)

Once the application configuration is completed follow the following steps to allow ZAP to run on your self-hosted runner's setup.

**Step 1** Add the following code snippet/s to your `jit-plan.yml` file, depending on whether you want to run [Ensure Your APIs are Secure (DAST)](https://docs.jit.io/docs/ensure-your-api-is-secure), [Scan Your Web Application for Vulnerabilities (DAST)](https://docs.jit.io/docs/run-a-web-application-scanner), or both via the GitHub-hosted runner.

```yaml For API scanning (jit-plan.yml)
override:
  workflows:
    api-security:
      jobs:
        api-security-detection:
          runner:
            setup:
              checkout: false
            type: ci

```

```yaml For web app scanning (jit-plan.yml)
override:
  workflows:
    web-app-scanner:
      jobs:
        web-security-detection:
          runner:
            setup:
              checkout: false
            type: ci
```

```yaml For both security controls (jit-plan.yml)
override:
  workflows:
    api-security:
      jobs:
        api-security-detection:
          runner:
            setup:
              checkout: false
            type: ci
    web-app-scanner:
      jobs:
        web-security-detection:
          runner:
            setup:
              checkout: false
            type: ci
```

Commit the file and in the next ZAP run will be on your self-hosted runners.

> 👍 That's it!
>
> ZAP-based security controls are now configured to run on the GitHub-hosted runner whenever they are triggered.