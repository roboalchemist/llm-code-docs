# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/custom_frameworks.md

---
title: Create Custom Compliance Frameworks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations >
  Manage Your Security Compliance Posture > Create Custom Compliance Frameworks
---

# Create Custom Compliance Frameworks

With custom frameworks, you can define and measure compliance against your own cloud security baseline. Custom frameworks are listed on the Cloud Security [Compliance](https://app.datadoghq.com/security/compliance/home) page, have their own real-time report and [security posture score](https://docs.datadoghq.com/glossary/#security-posture-score), and are queryable within explorers and dashboards.

1. On the [Cloud Security Compliance page](https://app.datadoghq.com/security/compliance/home), click **Create Framework**.
1. Enter the following details:
   - **Framework name**: The name of your framework. Can include characters, numbers, and spaces. Must be at least five characters long.
   - **Handle**: The tag name for the custom framework. Can include lowercase letters, numbers, dashes, underscores, and periods. This value is used to query the framework in the explorer or in dashboards.
   - **Version**: The version of the framework. Can include lowercase letters, numbers, dashes, underscores, and periods.
   - **Image URL**: A publicly accessible URL for an image that is used to identify the framework.
1. Click **Next Step: Create Your Framework**.

Next, add requirements to the framework:

{% alert level="danger" %}
You must add at least one requirement, control, and rule before saving the custom framework.
{% /alert %}

1. Click **Add Requirement**.
1. Enter the following details:
   - **Requirement**: A requirement acts as a control family, enabling you to add controls and associate rules with each control. Can include lowercase letters, numbers, dashes, underscores, and periods.
   - **Control**: A control represents the criteria that the requirement must meet and includes the rules associated with these criteria. Multiple rules can be included in a control. Can include lowercase letters, numbers, dashes, underscores, and periods.
1. Click **Add Rules**.
1. Select the cloud or infrastructure configuration rules you want to assign to the control, then click **Add to Control**.
1. To add additional items:
   - For additional rules, click **Add Rules**.
   - For another control, click **Add Control**.
   - For another requirement, click **Add Requirement**.
1. Click **Save**. Changes can take up to four hours to be reflected in the app.

{% alert level="info" %}
To remove a rule from a control, hover over the rule and click **Remove Rule**.
{% /alert %}

## Further reading{% #further-reading %}

- [Getting started with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cspm/setup)
- [Explore default Cloud Security Misconfigurations cloud configuration compliance rules](https://docs.datadoghq.com/security/default_rules)
- [Search and explore misconfigurations](https://docs.datadoghq.com/security/cspm/findings)
- [Securing Datadog's cloud infrastructure: Our playbook and methodology](https://www.datadoghq.com/blog/cloud-security-playbook/)
