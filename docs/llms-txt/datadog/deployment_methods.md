# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/deployment_methods.md

---
title: Deploying Agentless Scanning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Cloud
  Security Agentless Scanning > Deploying Agentless Scanning
---

# Deploying Agentless Scanning

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

There are two recommended ways to deploy Agentless scanners in your environment, either using cross-account scanning, or same account scanning.

{% tab title="Cross-account scanning" %}
With cross-account scanning, Agentless scanners are deployed across multiple regions in a single cloud account. The deployed Agentless scanners are granted visibility across multiple accounts without needing to perform cross-region scans, which are expensive in practice.

For larger accounts with 250 or more hosts, this is the most cost-effective option as it avoids cross-region scans, and reduces friction for managing your Agentless scanners. You can either create a dedicated account for your Agentless scanners or choose an existing one. The account where the Agentless scanners are located can also be scanned.

For AWS Organizations, you can use a [CloudFormation StackSet](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/enable#aws-cloudformation-stackset-setup) to deploy the delegate role across all member accounts, automating the onboarding process for cross-account scanning.

The following diagram illustrates how Agentless scanning works when deployed in a central cloud account:

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/setup/cloud_storage/central-scanner.2908be09bc9c7ae5a164fce78c10ee1b.png?auto=format"
   alt="Diagram of Agentless scanning showing the Agentless scanner is deployed in a central Cloud account" /%}

{% /tab %}

{% tab title="Same account scanning" %}
With same account scanning, a single Agentless scanner is deployed per account. Although this can incur more costs, as it requires each Agentless scanner to perform cross-region scans per account, Datadog recommends this option if you do not want to grant cross-account permissions.

The following diagram illustrates how Agentless scanning works when deployed within each Cloud account:

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/setup/cloud_storage/scanner-in-each-account.148704d6f7f552bc91f086b2352a0c2a.png?auto=format"
   alt="Diagram of Agentless scanning showing the Agentless scanner is deployed in each Cloud account" /%}

{% /tab %}

## Recommended configuration{% #recommended-configuration %}

Agentless Scanning incurs [additional cloud service provider costs](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning#cloud-service-provider-cost) for running scanners in your cloud environments. To manage costs while ensuring reliable scans every 12 hours, Datadog recommends setting up Agentless Scanning with Terraform as the default template. Terraform allows deploying one scanner per region which prevents cross-region networking. To improve the scanner's efficacy, ensure your setup follows those guidelines:

- Deploy scanners within a single AWS account
- Deploy a scanner in each region that has more than 250 hosts
- Deploy a scanner in any region containing a data store if using [Cloud Storage Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning#cloud-storage-scanning)

Datadog automatically schedules scans to the right region to minimize the cross region costs.

**Note**: The actual scanned data remains in your infrastructure, and only the collected list of packages, as well as information related to collected hosts (hostnames/EC2 Instances), are reported back to Datadog.

## Further reading{% #further-reading %}

- [Cloud Security Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning)
