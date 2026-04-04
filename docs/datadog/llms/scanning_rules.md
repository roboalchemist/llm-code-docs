# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules.md

---
title: Scanning Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Sensitive Data Scanner > Scanning Rules
---

# Scanning Rules

## Telemetry Data{% #telemetry-data %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.eu, app.ddog-gov.com



{% alert level="info" %}
Human Name Scanner detects personal names in logs using machine learning. The feature is in Preview for the  site. Fill out the [form](https://www.datadoghq.com/product-preview/human-name-pii-detection-in-logs-using-machine-learning/) to request access.
{% /alert %}


{% /callout %}

Sensitive Data Scanner for Telemetry Data uses scanning rules to determine what sensitive information to match within the data. This data can be from your application logs, APM spans, RUM events, and events from Event Management. You can use Datadog's [Scanning Rule Library](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) to create rules or you can create [custom rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules/).

Datadog's Scanning Rule Library containes predefined scanning rules that detect common patterns, such as email addresses, credit card numbers, API keys, authorization tokens, network and device information, and more. See [Library Rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) for more information.

You can also create custom scanning rules using regular expression (regex) patterns to define the sensitive information for which you want to match. See [Custom Rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules/) for more information.

## Cloud Storage{% #cloud-storage %}

Sensitive Data Scanner for Cloud Storage also uses scanning rules to determine what sensitive information to match within the data. All rules from the Datadog Scanning Library are applied and cannot be edited. See [Library Rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) for more information.

## Further reading{% #further-reading %}

- [Visually identify and prioritize security risks using Cloudcraft](https://www.datadoghq.com/blog/cloudcraft-security/)
