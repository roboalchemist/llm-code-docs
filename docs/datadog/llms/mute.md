# Source: https://docs.datadoghq.com/security/automation_pipelines/mute.md

---
title: Mute Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Findings Automation Pipelines > Mute Rules
---

# Mute Rules

Configure mute rules to streamline security alerts by automatically filtering out non-urgent findings. This approach helps reduce noise from known false positives and accepted risks, allowing you to focus on addressing the most critical threats.

## Create a mute rule{% #create-a-mute-rule %}

1. On the [Automation Pipelines](https://app.datadoghq.com/security/configuration/findings-automation?opened-sections=mute) page, click **Add a New Rule** and select **Mute**.
1. Enter a descriptive name for the rule, for example, **Compensating control in place for account payment-prod**.
1. Use the following boxes to configure the rule criteria:
   - **Any of these types**: The types of findings that the rule should check for. Available types include:
     - **Runtime Code Vulnerability**
     - **Static Code Vulnerability**
     - **Library Vulnerability**
     - **Secret**
     - **Infrastructure as Code**
     - **Container Image Vulnerability**
     - **Host Vulnerability**
     - **Misconfiguration**
     - **Attack Path**
     - **Identity Risk**
     - **API Security**
   - **Any of these tags or attributes**: The resource tags or attributes that must match for the rule to apply.
1. To add severity criteria to the rule, click **Add Severity**.
1. Specify the mute reason and duration:
   - **Reason for muting**: The reason for muting the finding. Available reasons include:
     - **False Positive**
     - **Risk Accepted**
     - **Pending fix**
     - **No Fix**
     - **Duplicate**
     - **Other**
   - **Rule expiration**: The date on which the rule expires.
   - **Further description for muting reason**: Optional box for additional details.
1. Click **Save**. The rule applies to new findings immediately and starts checking existing findings within the next hour.

## Rule matching order{% #rule-matching-order %}

When Datadog identifies a finding, it evaluates the finding against your sequence of mute rules. Starting with the first rule, if there's a match, Datadog mutes the finding for the specified duration and stops evaluating further. If no match occurs, Datadog moves to the next rule. This process continues until a match is found or all rules are checked without a match.

## Further reading{% #further-reading %}

- [Automation Pipelines](https://docs.datadoghq.com/security/automation_pipelines)
- [Prevent cloud misconfigurations from reaching production with Datadog IaC Security](https://www.datadoghq.com/blog/datadog-iac-security/)
