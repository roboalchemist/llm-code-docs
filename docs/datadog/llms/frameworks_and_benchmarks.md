# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks.md

---
title: Manage Your Security Compliance Posture
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations >
  Manage Your Security Compliance Posture
---

# Manage Your Security Compliance Posture

Cloud Security Misconfigurations comes with more than 1,300 out-of-the-box compliance rules that evaluate the configuration of your cloud resources and identify potential misconfigurations. Each [compliance rule](https://docs.datadoghq.com/security_monitoring/default_rules/) maps to one or more controls within a [compliance standard or industry benchmark](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/supported_frameworks/). You can also [create custom frameworks](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/custom_frameworks) to define and measure compliance against your own cloud security baseline.

## View your compliance posture{% #view-your-compliance-posture %}

View a high-level overview of your compliance posture for each framework on the Cloud Security Misconfigurations [Compliance](https://app.datadoghq.com/security/compliance) page. Click a framework to see a detailed report that gives you insight into how your configuration scores against the framework's requirements and rules.

- **Star**: Pin a framework to the top of your table.
- **Score**: The [posture score](https://docs.datadoghq.com/glossary/#security-posture-score) for the rules in the given framework.
- **Change**: The difference in posture score over the chosen time range (defaults to 1 month). Hover to see details.
- **Failing Rules**: All the rules failing in the framework. Hover for more details.
- **Resources Passing**: Of all the resources evaluated by rules in the framework, the percentage of which pass all the rules in the framework.
- **Framework Overview**: A detailed report that gives you insight into how you score against a framework's requirements and rules.
- **Explore Resources**: A filtered view of the **Misconfigurations** page that shows resources with misconfigurations for the selected framework.
- **Configure Rules**: Customize how your environment is scanned and set notification targets by modifying the compliance rules for each framework.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/frameworks_and_benchmarks/compliance_reports_5.0125def367d619fec9b6a08843d238d2.png?auto=format"
   alt="The compliance reports section of the Cloud Security Misconfigurations Compliance page provides a high-level overview of your compliance posture" /%}

## Explore compliance framework reports{% #explore-compliance-framework-reports %}

Compliance framework reports show which rules are failing in your environment, along with details about the misconfigured resources.

The summary at the top of the report shows the [posture score](https://docs.datadoghq.com/glossary/#security-posture-score), the top five most severe rule failures, and a detailed breakdown of the rules based on severity. You can also explore your past posture with the time selector, download a PDF or CSV copy of the report, and filter the page by account, team, service, and environment tags.

Below the summary is a complete listing of all rules associated with the framework, organized by default by requirements and controls, along with the number of resources checked by the rule, the percentage of failures, and the change in resources passing the rule over the chosen time period.

Search for a rule name to filter the list, or group by requirement, control, severity, resource type, or resource category to organize the list. You can also click a table column header to sort by that column within the group.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/frameworks_and_benchmarks/cis_aws_compliance_report_5.68fd40886a9b1a2c7417101aac06144f.png?auto=format"
   alt="The CIS AWS compliance framework report provides details on critical rule failures" /%}

Select a rule to view details about the misconfigured resources, the rule description, its framework or industry benchmark mapping, and suggested remediation steps. Then, you can click a specific resource to get more details.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/frameworks_and_benchmarks/failed-finding3.ad6dab076050a91ec7ed96caf4c9c39c.png?auto=format"
   alt="The compliance rule side panel includes information about the rule and resources with failed misconfigurations" /%}

## Show or hide compliance frameworks{% #show-or-hide-compliance-frameworks %}

You can hide frameworks from the list on the [Compliance](https://app.datadoghq.com/security/compliance) page, so you can focus on the ones that are most relevant to your organization.

To hide a framework, either on the Compliance page or on a page for a specific framework, click the **Options** button , then click **Hide framework**.

Then, on the Compliance page, you can use the **Show hidden frameworks** toggle to show hidden frameworks at the bottom of the list, or hide them completely. When the toggle is on, you can click **Show** next to any hidden framework to add it back to the list.

## Further reading{% #further-reading %}

- [Getting started with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cspm/setup)
- [Explore default Cloud Security Misconfigurations cloud configuration compliance rules](https://docs.datadoghq.com/security/default_rules)
- [Search and explore misconfigurations](https://docs.datadoghq.com/security/cspm/findings)
