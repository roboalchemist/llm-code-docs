# Source: https://docs.datadoghq.com/security/code_security/secret_scanning.md

---
title: Secret Scanning
description: Use Datadog Secret Scanning to find secrets exposed in source code.
breadcrumbs: Docs > Datadog Security > Code Security > Secret Scanning
---

# Secret Scanning

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

Datadog Secret Scanning scans code to find exposed secrets. Datadog also attempts to validate secrets and surface their status (valid, invalid) to help you prioritize secrets remediation.

## Set up Secret Scanning{% #set-up-secret-scanning %}

Scans can run in your CI/CD pipelines or directly in Datadog with hosted scanning (supported for GitHub, Azure DevOps, and GitLab). To get started, go to the [**Code Security Setup**](https://app.datadoghq.com/security/configuration/code-security/setup) and click **Activate scanning for your repositories** or learn how to set up Secret Scanning using [GitHub actions](https://docs.datadoghq.com/security/code_security/secret_scanning/github_actions) or with [other CI providers](https://docs.datadoghq.com/security/code_security/secret_scanning/generic_ci_providers).

## Secret Scanning rules{% #secret-scanning-rules %}

Datadog Secret Scanning is powered by [Sensitive Data Scanner (SDS)](https://docs.datadoghq.com/security/sensitive_data_scanner/) and includes all of the rules in the [Secrets and credentials category of SDS](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/?category=Secrets+and+credentials#overview).

## Further Reading{% #further-reading %}

- [Detect and block exposed credentials with Datadog Secret Scanning](https://www.datadoghq.com/blog/code-security-secret-scanning)
