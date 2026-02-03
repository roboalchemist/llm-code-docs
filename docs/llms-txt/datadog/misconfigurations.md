# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations.md

---
title: Cloud Security Misconfigurations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations
---

# Cloud Security Misconfigurations

Cloud Security Misconfigurations makes it easier to assess and visualize the current and historic security posture of your cloud resources, automate audit evidence collection, and remediate misconfigurations that leave your organization vulnerable to attacks. By continuously surfacing security weaknesses resulting from misconfigurations, teams can mitigate risks while ensuring compliance with industry standards.

## Detect misconfigurations across your cloud resources{% #detect-misconfigurations-across-your-cloud-resources %}

Strengthen your security posture and achieve continuous compliance by detecting, prioritizing, and remediating misconfigurations across all your cloud resources using Datadog's out-of-the-box compliance rules.

View a high-level overview of your security posture on the [Overview page](https://app.datadoghq.com/security/csm). Examine the details of misconfigurations and analyze historical configurations with the [Misconfigurations Findings page](https://app.datadoghq.com/security/compliance).

Cloud Security Misconfigurations evaluates resources in increments between 15 minutes and 4 hours (depending on type). Datadog generates new misconfigurations as soon as a scan is completed, and stores a complete history of all misconfigurations for the past 15 months so they are available in case of an investigation or audit.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/misconfigurations_explorer_4.d0c35cb66f332ac47104dc77f0b7690a.png?auto=format"
   alt="Cloud Security Misconfigurations Findings page" /%}

## Maintain compliance with industry frameworks and benchmarks{% #maintain-compliance-with-industry-frameworks-and-benchmarks %}

Cloud Security Misconfigurations comes with more than 1,000 out-of-the-box compliance rules that are maintained by a team of security experts. The rules map to controls and requirements within compliance standards and industry benchmarks, such as PCI and SOC2 compliance frameworks.

[View compliance reports](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks) to see how well you're doing against each control in a compliance framework. The reports include details such as resources with the most failed misconfigurations, a comprehensive breakdown of the number of resources with pass/fail misconfigurations, and the top three high-severity rule failures.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/frameworks_and_benchmarks/compliance_reports_5.0125def367d619fec9b6a08843d238d2.png?auto=format"
   alt="Cloud Security Misconfigurations compliance frameworks" /%}

## Manage out-of-the-box and custom detection rules{% #manage-out-of-the-box-and-custom-detection-rules %}

[Out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/#cat-posture-management-cloud) surface the most important risks so that you can immediately take steps to remediate. Datadog continuously develops new default rules, which are automatically imported into your account. [Customize the rules](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks#view-your-compliance-posture) by defining how each rule scans your environment, [create custom rules](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/custom_rules), and set up real-time notifications for failed misconfigurations.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/detection_rules.caf6a903db53e008764ed6b03cae37ce.png?auto=format"
   alt="Cloud Security Misconfigurations detection rules" /%}

## Set up real-time notifications{% #set-up-real-time-notifications %}

[Send real-time notifications](https://docs.datadoghq.com/security/notifications/) when a new misconfiguration is detected in your environment, so that your teams can take action to mitigate the risk. Notifications can be sent to [Slack, email, PagerDuty, webhooks, and more](https://docs.datadoghq.com/security/notifications/#notification-channels).

Use template variables and Markdown to [customize notification messages](https://docs.datadoghq.com/security/notifications/#detection-rule-notifications). Edit, disable, and delete existing notification rules, or create new rules and define custom logic for when a notification is triggered based on severity and rule type.

## Review and remediate misconfigurations{% #review-and-remediate-misconfigurations %}

Investigate details using the [Misconfigurations Findings page](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/findings), where you can view detailed information about a resource, such as configuration, compliance rules applied to the resource, and tags that provide additional context about who owns the resource and its location within your environment. If a misconfiguration does not match your business use case or is an accepted risk, you can [mute the misconfiguration](https://docs.datadoghq.com/security/cloud_security_management/mute_issues) up to an indefinite period of time.

To remediate a misconfiguration, you can:

- [Create a Jira issue](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/jira?tab=csmmisconfigurations) and assign it to a team
- Use [Workflow Automation](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/workflows/) to create automated remediation workflows (with or without human involvement)
- For supported Terraform resources:
  - Locate the file and line the misconfiguration is in and identify the code owners
  - Generate a pull request in GitHub with code changes that fix the underlying misconfiguration

## Get started{% #get-started %}

{% callout %}
##### Try Detect, Prioritize, and Remediate Cloud Security Risks with Datadog Cloud Security in the Learning Center

The Datadog Learning Center is full of hands-on courses to help you learn about this topic. Enroll at no cost to learn how to secure your cloud environments with Cloud Security misconfigurations.

[ENROLL NOW](https://learn.datadoghq.com/courses/csm-misconfigurations)
{% /callout %}

- [Complete setup and configuration](https://docs.datadoghq.com/security/cloud_security_management/setup)
- [Getting Started with Cloud Security](https://docs.datadoghq.com/getting_started/cloud_security_management)
- [Datadog role permissions for Cloud Security Misconfigurations](https://docs.datadoghq.com/account_management/rbac/permissions/#cloud-security-platform)
- [Out-of-the-box cloud detection rules for Cloud Security Misconfigurations](https://docs.datadoghq.com/security/default_rules/#cat-posture-management-cloud)
- [Out-of-the-box infrastructure detection rules for Cloud Security Misconfigurations](https://docs.datadoghq.com/security/default_rules/#cat-posture-management-infra)
- [Learn more about misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/findings)
- [Monitor the security and compliance posture of your Azure environment](https://www.datadoghq.com/blog/cspm-for-azure-with-datadog/)
- [Improve the compliance and security posture of your Google Cloud environment](https://www.datadoghq.com/blog/cspm-for-gcp-with-datadog/)
