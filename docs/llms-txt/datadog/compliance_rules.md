# Source: https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/compliance_rules.md

---
title: Manage Cloud Security Misconfigurations Compliance Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Misconfigurations >
  Manage Cloud Security Misconfigurations Compliance Rules
---

# Manage Cloud Security Misconfigurations Compliance Rules

Cloud Security Misconfigurations [out-of-the-box compliance rules](https://docs.datadoghq.com/security/default_rules/#cat-csm-misconfigurations-cloud) evaluate the configuration of your cloud resources and identify potential misconfigurations so you can immediately take steps to remediate.

The compliance rules follow the same [conditional logic](https://docs.datadoghq.com/security/detection_rules/) as all Datadog Security compliance rules. For Cloud Security Misconfigurations, each rule maps to controls within one or more [compliance frameworks or industry benchmarks](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks).

Cloud Security Misconfigurations uses the following rule types to validate the configuration of your cloud infrastructure:

- [**Cloud configuration**](https://docs.datadoghq.com/security/default_rules/#cat-csm-misconfigurations-cloud): These compliance rules analyze the configuration of resources within your cloud environment. For example, the [CloudFront distribution should be encrypted](https://docs.datadoghq.com/security/default_rules/aws-cloudfront-distribution-cloudfront-distribution-should-be-encrypted/) rule assesses whether an Amazon CloudFront distribution enforces HTTPS to secure communications.

- [**Infrastructure configuration**](https://docs.datadoghq.com/security/default_rules/#cat-posture-management-infra) checks evaluate:

  - **Containers and Kubernetes clusters**, using rules from CIS compliance benchmarks for Docker and Kubernetes.

  - **Linux workloads**, using CIS host benchmarks for Linux distributions including Ubuntu, Red Hat, Amazon Linux, and AlmaLinux.

Cloud Security Misconfigurations supports a subset of the Linux distributions that the Agent supports. For more information, see [Supported Platforms](https://docs.datadoghq.com/agent/supported_platforms/?tab=linux).
Important alert (level: info): In Cloud Security, rules with the **infrastructure** label are applicable to Agent installations.

## Explore default compliance rules{% #explore-default-compliance-rules %}

To filter the default compliance rules by cloud provider:

1. Navigate to the [**Misconfiguration Rules**](https://app.datadoghq.com/security/configuration/compliance/rules) page.
1. Choose one of the following values from the **Tag** facet.
   - **AWS**: cloud_provider:aws
   - **Azure**: cloud_provider:azure
   - **Google Cloud**: cloud_provider:gcp
   - **Docker**: framework:cis-docker
   - **Kubernetes**: framework:cis-kubernetes

## Customize how your environment is scanned by each rule{% #customize-how-your-environment-is-scanned-by-each-rule %}

Customization of a cloud configuration query directly is not supported at this time, but you can customize how your environment is scanned by each rule.

On the [Rules](https://app.datadoghq.com/security/configuration/compliance/rules) page, select a rule to open its details page. Under **Exclude benign activity with suppression queries**, set the filtering logic for how the rule scans your environment.

For example, you can exclude resources tagged with `env:staging` using the **This rule will not generate a misconfiguration if there is a match with any of the following suppression queries** function. You can also limit the scope for a certain rule to resources tagged with `compliance:pci` using the **Only generate a misconfiguration if there is a match with any of the following queries** function.

After you customize a rule, click **Update Rule** at the bottom of the page to apply your changes.

{% image
   source="https://datadog-docs.imgix.net/images/security/cspm/frameworks_and_benchmarks/never-trigger-misconfiguration.6bda475d69ff78f93dae460ff8a10b23.png?auto=format"
   alt="Customize how your environment is scanned by selecting tags to include or exclude from a rule's scope" /%}

## Create custom rules{% #create-custom-rules %}

You can create custom rules to extend the rules being applied to your environment to evaluate your security posture. You can also clone the default detection rules and edit the copies (Google Cloud only). See [Custom Rules](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/custom_rules/) for more information.

## Rule deprecation{% #rule-deprecation %}

Regular audits of all compliance rules are performed to maintain high fidelity signal quality. Deprecated rules are replaced with an improved rule.

The rule deprecation process is as follows:

1. There is a warning with the deprecation date on the rule. In the UI, the warning is shown in the:
   - Signal side panel's **Rule Details > Playbook** section
   - Misconfigurations side panel
   - [Rule editor](https://docs.datadoghq.com/security/detection_rules/#clone-a-rule) for that specific rule
1. Once the rule is deprecated, there is a 15 month period before the rule is deleted. This is due to the signal retention period of 15 months. During this time, you can re-enable the rule by [cloning the rule](https://docs.datadoghq.com/security/detection_rules/#clone-a-rule) in the UI.
1. Once the rule is deleted, you can no longer clone and re-enable it.

## Further Reading{% #further-reading %}

- [Getting Started with Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations)
- [Custom Rules](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/custom_rules/)
- [Misconfigurations Reports](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/)
