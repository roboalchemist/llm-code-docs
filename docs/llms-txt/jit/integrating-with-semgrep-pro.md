# Source: https://docs.jit.io/docs/integrating-with-semgrep-pro.md

# Semgrep Pro Tier Integration

Integrating with Semgrep Pro Tier

## Overview

Semgrep Pro Tier integration enables you to use Semgrep's Pro Tier (commercial) Static Code Anaylsis (SAST) within Jit's platform.

## Activating and disabling Semgrep Pro Tier integration

**To activate Semgrep Pro SAST**

1. From Semgrep's platform, select **Settings** > **Tokens** and create a new Agent (CI) token.
2. From the Jit platform, select **Settings** > **Integrations** .
3. Follow the instructions in Semgrep Pro integration card to store the API key as a secret in Jit platform.
4. Activate the SAST plan items from the relevant security plan. Go to [Security Plans](https://docs.jit.io/docs/security-plans-1) and click it. For example, SAST are part of [Jit MVS for AppSec Plan](https://docs.jit.io/docs/jit-mvs-for-appsec-plan).
5. Enable Semgrep Pro Tier SAST by adding the following snippet to the end of your jit-plan.yml file — either in the .jit repository or wherever you manage your Jit configurations.\
   This will also disable other SAST jobs to avoid any conflicts.

```yaml jit-plan.yml
override:
  workflows:
    sast:
      jobs:
        static-code-analysis-semgrep-pro:
          enabled: true
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
        static-code-analysis-bash:
          enabled: false
        static-code-analysis-php:
          enabled: false
 
```

By default, the scan detects only `ERROR` severity. To include other levels (e.g., `MEDIUM`), use `override` at the bottom of `jit-plans.yml` as shown below:

```yaml jit-plan.yml
override:
  workflows:
    sast:
      jobs:
        static-code-analysis-semgrep-pro:
          enabled: true
          steps:
            - name: Run Semgrep Code Pro Tier
              with:
                args:  --pro --json --severity ERROR --severity WARNING
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
        static-code-analysis-bash:
          enabled: false
        static-code-analysis-php:
          enabled: false

```

> 📘 Additional information
>
> * This code overrides the original Jit configuration by disabling Jit's SAST  tools and enabling Semgrep's Pro Tier.
> * You can add or delete this code any time you want to switch between Semgrep's Pro Tier and Jit's SAST.

**To disable Semgrep's Pro Tier SAST**

Delete the above code from your `.jit/jit-plan.yml`. This reverts your plan back to Jit's tools for SAST.