# Source: https://docs.jit.io/docs/checkmarx-integration.md

# Checkmarx Integration

## Overview

Checkmarx integration enables you to use Checkmarx (commercial) Static Code Anaylsis (SAST) within Jit's platform.

## Activating and disabling Checkmarx  integration

**To activate Checkmarx SAST**

1. From Checkmarx's platform, select **Settings** >  **Identify and Access Management** > **API Keys** and create a new API key.
2. From the Jit platform, select **Settings** > **Integrations** .
3. Follow the instructions in Checkmarx integration card to store the API key as a secret in Jit platform.
4. Activate the SAST plan items from the relevant security plan. Go to [Security Plans](https://docs.jit.io/docs/security-plans-1) and click it. For example, SAST are part of [Jit MVS for AppSec Plan](https://docs.jit.io/docs/jit-mvs-for-appsec-plan).
5. Activate Checkmarx SAST by adding the following snippet at the bottom of the `jit-plan.yml` file in your `.jit` repository, or in the repository where you manage Jit's configurations:

```yaml jit-plan.yml
override:
  workflows:
    sast:
      jobs:
        static-code-analysis-checkmarx:
          enabled: true
 
```

6. Disable other SAST jobs to prevent conflicts. Your `jit-plan.yml` overrides should look as follows:

```yaml jit-plan.yml
override:
  workflows:
    sast:
      jobs:
        static-code-analysis-csharp:
          enabled: false
        static-code-analysis-go:
          enabled: false
        static-code-analysis-java:
          enabled: false
        static-code-analysis-js:
          enabled: false
        static-code-analysis-kotlin:
          enabled: false
        static-code-analysis-python:
          enabled: false
        static-code-analysis-python-semgrep:
          enabled: false
        static-code-analysis-rust:
          enabled: false
        static-code-analysis-scala:
          enabled: false
        static-code-analysis-swift:
          enabled: false
        static-code-analysis-ruby:
          enabled: false
        static-code-analysis-c-cpp:
          enabled: false
```

<br />

**Severity Threshold**

You can control which findings are reported based on their severity level by using the `SEVERITY_THRESHOLD` environment variable. For example:

* Setting the threshold to `CRITICAL` will only show findings with CRITICAL severity
* Setting the threshold to `HIGH` will only show findings with HIGH severity
* Setting the threshold to `MEDIUM` will show findings with both HIGH and MEDIUM severity
* Setting the threshold to `LOW` will show ALL findings (LOW, MEDIUM, and HIGH)

Example configuration with severity threshold:

```yaml
override:
  workflows:
    sast:
      jobs:        
        static-code-analysis-checkmarx:
          enabled: true
          steps:
          - name: Run Checkmarx SAST
            with:
                env:
                    SEVERITY_THRESHOLD: MEDIUM # this will represent both HIGH & MEDIUM severity.
```

<br />

**Regional Server Configuration**

Checkmarx provides several regional servers that you can use. By default, the `EU Environment` is used, but you can specify a different server using the `CX_BASE_URI` environment variable.

Available servers:

* US Environment: `https://ast.checkmarx.net`
* US2 Environment: `https://us.ast.checkmarx.net`
* EU Environment: `https://eu.ast.checkmarx.net` (default)
* EU2 Environment: `https://eu-2.ast.checkmarx.net`
* DEU Environment: `https://deu.ast.checkmarx.net`
* Australia & New Zealand: `https://anz.ast.checkmarx.net`
* India: `https://ind.ast.checkmarx.net`
* Singapore: `https://sng.ast.checkmarx.net`
* UAE: `https://mea.ast.checkmarx.net`
* Israel: `https://gov-il.ast.checkmarx.net`

Example configuration with custom server:

```yaml
override:
  workflows:
    sast:
      jobs:        
        static-code-analysis-checkmarx:
          enabled: true
          steps:
          - name: Run Checkmarx SAST
            uses: ${{ context.config.custom_registry || registry.jit.io }}/control-checkmarx-alpine:latest
            with:
                env:
                    CX_BASE_URI: https://us.ast.checkmarx.net
```

Note: Setting the base URI is optional and is primarily an administrative variable for configuring the scan.

<br />

**Project Naming**

When running Checkmarx, a default project named "jit" will be automatically generated for ALL scans. This is part of the standard Checkmarx configuration and cannot be changed. This will be the single project generated for all your scans.

<br />

**Complete Configuration Example**

```yaml
override:
  workflows:
    sast:
      jobs:        
        static-code-analysis-checkmarx:
          enabled: true
          steps:
          - name: Run Checkmarx SAST
            with:
                env:
                    SEVERITY_THRESHOLD: MEDIUM
                    CX_BASE_URI: https://us.ast.checkmarx.net
        # Disable other SAST scans to avoid duplication
        static-code-analysis-c-cpp:
          enabled: false
        static-code-analysis-csharp:
          enabled: false
        static-code-analysis-go:
          enabled: false
        static-code-analysis-java:
          enabled: false
        static-code-analysis-js:
          enabled: false
        static-code-analysis-kotlin:
          enabled: false
        static-code-analysis-python:
          enabled: false
        static-code-analysis-python-semgrep:
          enabled: false
        static-code-analysis-ruby:
          enabled: false
        static-code-analysis-rust:
          enabled: false
        static-code-analysis-scala:
          enabled: false
        static-code-analysis-swift:
          enabled: false
```

<br />

> 📘 Additional information
>
> * This code overrides the original Jit configuration by disabling Jit's SAST  tools and enabling Checkmarx's.
> * You can add or delete this code any time you want to switch between Checkmarx and Jit's SAST.

**To disable Checkmarx's SAST**

Delete the above code from your `.jit/jit-plan.yml`. This reverts your plan back to Jit's tools for SAST.