# Source: https://docs.datadoghq.com/security/code_security/static_analysis/generic_ci_providers.md

# Source: https://docs.datadoghq.com/security/code_security/secret_scanning/generic_ci_providers.md

---
title: Secret Scanning with Generic CI Providers
description: >-
  Use Datadog Static Secret Scanning to scan pre-prod code for quality issues
  and security vulnerabilities.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Secret Scanning > Secret Scanning
  with Generic CI Providers
---

# Secret Scanning with Generic CI Providers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="warning" %}
Secret Scanning is not available for the  site.
{% /alert %}


{% /callout %}

If you don't use [GitHub Actions](https://docs.datadoghq.com/security/code_security/secret_scanning/github_actions/) to set up Secret Scanning, you can run the [Datadog CI](https://github.com/DataDog/datadog-ci?tab=readme-ov-file#sarif) CLI directly in your CI pipeline platform and upload Static Analysis Results Interchange Format (SARIF) reports to Datadog.

Prerequisites:

- unzip
- Node.js 14 or later

Configure the following environment variables:

| Name         | Description                                                                                                                                                                                                                               | Required | Default         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- |
| `DD_API_KEY` | Your Datadog API key. This key is created by your [Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) and should be stored as a secret.                                                          | Yes      |
| `DD_APP_KEY` | Your Datadog application key. This key is created by your [Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/#application-keys), should include the `code_analysis_read` scope, and be stored as a secret. | Yes      |
| `DD_SITE`    | The [Datadog site](https://docs.datadoghq.com/getting_started/site/) to send information to. Your Datadog site is .                                                                                                                       | No       | `datadoghq.com` |

Select an analyzer for your architecture and OS from the following options:

| Architecture | OS        | Name                                                    | Link                                                                                                                                          |
| ------------ | --------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `aarch64`    | `Darwin`  | `datadog-static-analyzer-aarch64-apple-darwin.zip`      | [Download](https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-aarch64-apple-darwin.zip)      |
| `aarch64`    | `Linux`   | `datadog-static-analyzer-aarch64-unknown-linux-gnu.zip` | [Download](https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-aarch64-unknown-linux-gnu.zip) |
| `x86_64`     | `Darwin`  | `datadog-static-analyzer-x86_64-apple-darwin.zip`       | [Download](https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-x86_64-apple-darwin.zip)       |
| `x86_64`     | `Linux`   | `datadog-static-analyzer-x86_64-unknown-linux-gnu.zip`  | [Download](https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-x86_64-unknown-linux-gnu.zip)  |
| `x86_64`     | `Windows` | `datadog-static-analyzer-x86_64-pc-windows-msvc.zip`    | [Download](https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-x86_64-pc-windows-msvc.zip)    |

Add the following to your CI pipeline:

```bash
# Set the Datadog site to send information to
export DD_SITE="datadoghq.com"
export DD_API_KEY=<YOUR-API-KEY>
export DD_APP_KEY=<YOUR-APP-KEY>

# Install dependencies
npm install -g @datadog/datadog-ci

# Download the latest Datadog static analyzer:
# https://github.com/DataDog/datadog-static-analyzer/releases
DATADOG_STATIC_ANALYZER_URL=https://github.com/DataDog/datadog-static-analyzer/releases/latest/download/datadog-static-analyzer-x86_64-unknown-linux-gnu.zip
curl -L $DATADOG_STATIC_ANALYZER_URL > /tmp/ddog-static-analyzer.zip
unzip /tmp/ddog-static-analyzer.zip -d /tmp
mv /tmp/datadog-static-analyzer /usr/local/datadog-static-analyzer

# Run Static Code Analysis
/usr/local/datadog-static-analyzer -i . -o /tmp/report.sarif -f sarif --enable-secrets true --enable-static-analysis false

# Upload results
datadog-ci sarif upload /tmp/report.sarif
```

{% alert level="info" %}
This example uses the x86_64 Linux version of Datadog's static analyzer for Secret Scanning. If you're using a different OS or architecture, you should select it from the table above and update the `DATADOG_STATIC_ANALYZER_URL` value. You can view all releases on the [GitHub Releases](https://github.com/DataDog/datadog-static-analyzer/releases) page.
{% /alert %}

**Note:** When a diff-aware scan cannot be completed, the entire directory is scanned.
