# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/setup/cloud_storage.md

---
title: Cloud Storage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Sensitive Data Scanner > Setup > Cloud Storage
---

# Cloud Storage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Cloud Storage scanning is not available in the selected site ().
{% /alert %}


{% /callout %}

## Overview{% #overview %}

{% callout %}
##### Join the Preview Program!

Scanning support for Amazon S3 buckets and RDS instances is in Preview. To enroll, click Request Access.

[Request Access](https://www.datadoghq.com/product-preview/data-security/)
{% /callout %}

Deploy Datadog Agentless scanners in your environment to scan for sensitive information in your cloud storage resources. Agentless scanners are EC2 instances that you control and run within your environment. The scanners use [Remote Configuration](https://docs.datadoghq.com/remote_configuration) to retrieve a list of S3 buckets as well as their dependencies. They scan many types of text files, such as CSVs and JSONs in your S3 buckets.

When an Agentless scanner finds a match with any of the [SDS library rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/), the scanning instance sends the rule type and location of the match to Datadog. **Note**: Cloud storage resources and their files are only read in your environment - no sensitive data that was scanned is sent back to Datadog.

In the Sensitive Data Scanner [Findings page](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/data-security), you can see what cloud storage resources have been scanned and any matches found, including the rules that matched them.

This document walks you through:

- Enabling Remote Configuration to use Sensitive Data Scanner for Cloud Storage
- Security considerations to take into account when using Sensitive Data Scanner for Cloud Storage
- Deploying scanners to your environment using CloudFormation or Terraform

## Enable Remote Configuration{% #enable-remote-configuration %}

Remote Configuration allows Datadog to send configuration data (such as which cloud storage resources to scan) to your deployed scanners. To use Sensitive Data Scanner in your AWS environments, you need to ensure that:

- Remote Configuration is enabled for your Datadog organization.
- You are using Remote-Configuration-enabled Datadog API keys for AWS accounts with scanners deployed to them.

Remote Configuration is enabled by default on most organizations. To verify this, navigate to the [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config) settings page. If it is not enabled:

1. Ensure your RBAC permissions include [`org_management`](https://github.com/DataDog/terraform-module-datadog-agentless-scanner).
1. From the Remote Configuration [setup page](https://app.datadoghq.com/organization-settings/remote-config/setup), click **Enable for your Organization** > **Next Step**.
1. Search for and select the API keys that you want to use with Remote Configuration and click **Enable Keys**.
1. Click **Next Step** > **Done**. You do not need to configure Datadog components like the Agent or tracers.

**Notes**:

- Only AWS accounts that have scanners deployed to them need Remote-Configuration-enabled Datadog API keys.
- Only admins with `org_management` permissions can enable Remote Configuration for your organization. After Remote Configuration has been enabled, only users with `api_keys_write` permission can enable Remote Configuration for individual API keys.

## Security considerations{% #security-considerations %}

Because the scanner instances are potentially granted access to sensitive data, Datadog recommends restricting access to these instances solely to administrative users.

To further mitigate this risk, Datadog implements the following security measures:

- The Datadog scanner operates within your infrastructure, ensuring that all data, including sensitive data results, remain isolated and secure.
- All data transmission between the scanner and Datadog is encrypted using industry standard protocols (such as HTTPS) to ensure data confidentiality and integrity.
- Datadog carefully reviews and limits the permissions needed by the scanner to ensure that it can conduct scans without unnecessary access. This means the scanner operates under the principle of least privilege and is granted only the minimum permissions necessary to perform effectively.
- Unattended security updates are enabled on Datadog's scanner instances. This feature automates the process of installing critical security patches and updates without requiring manual intervention.
- The Datadog scanner instances are automatically rotated every 24 hours. This rotation ensures that the scanner instances are continually updated with the latest Ubuntu images.
- Access to the scanner instances is tightly controlled through the use of security groups. No inbound access to the scanner is allowed, further reducing the risk of compromising the instance.

To scan Amazon S3 buckets, these permissions are required:

- `s3:GetObject`
- `s3:ListBucket`
- `kms:Decrypt`
- `kms:GenerateDataKey`

## Deploy scanners{% #deploy-scanners %}

Agentless scanners are EC2 instances that run in your environment. They scan your S3 buckets for sensitive information.

There are two methods for deploying scanners to your environment:

- Automatically deploy using CloudFormation
- Manually deploy using Terraform

### Automatically deploy scanners using CloudFormation{% #automatically-deploy-scanners-using-cloudformation %}

When you deploy Agentless scanners using CloudFormation, a single scanner is created per account and scans across all of the account's regions. You set the region that the scanner is deployed on.

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/setup/cloud_storage/scanner-in-each-account.148704d6f7f552bc91f086b2352a0c2a.png?auto=format"
   alt="Diagram showing a scanner in each account scanning across regions within that account" /%}

You can add a scanner to a new AWS account or an existing AWS account.

{% tab title="New AWS account" %}

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration/data-security) settings page.
1. On the **Storage** tab, in the **Cloud Settings** section, click **Add AWS accounts by following these steps**.
1. Leave **Automatically using CloudFormation** enabled.
1. Select the AWS region in the dropdown menu.
1. Select an API key that is already configured for Remote Configuration. If the API key you select does not have Remote Configuration enabled, Remote Configuration is automatically enabled for that key upon selection. **Note**: Only users with `api_keys_write` permissions can enable Remote Configuration for individual API keys.
1. If you want to send AWS logs to Datadog, leave **Yes** selected.
1. Select **Yes** if you want to use Datadog Cloud Security.
1. **Enable Sensitive Data Scanner** is automatically selected by default. This tells CloudFormation to add the AWS Managed SecurityAudit policy to your Datadog AWS Integration role and enable Agentless Scanning to start scanning your cloud data stores.
1. Click **Launch CloudFormation Template**.

{% /tab %}

{% tab title="Existing AWS account" %}

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration/data-security) settings page.
1. On the **Storage** tab, in the **AWS** section:
   - If you have Agentless scanning already enabled in an account:
     1. Click the pencil icon for the account.
     1. Toggle **Enable Sensitive Data Scanning** on to add the scanner to the account.
     1. Click **Save**.
   - If you don't have Agentless scanning enabled in an account:
     1. Click on the plus icon for the account you want to enable sensitive data scanning for.
     1. Select that you want to add the scanner using CloudFormation.
     1. Select the AWS region in the dropdown menu.
     1. Select an API key that is already configured for Remote Configuration. If the API key you select does not have Remote Configuration enabled, Remote Configuration is automatically enabled for that key upon selection.
     1. Toggle **Enable Sensitive Data Scanning** on to add the scanner to the account.
     1. Click **Launch CloudFormation Template**.

{% /tab %}

### Manually deploy scanners using Terraform{% #manually-deploy-scanners-using-terraform %}

You can deploy Agentless scanners using the [Terraform Module Datadog Agentless Scanner](https://github.com/DataDog/terraform-module-datadog-agentless-scanner). Datadog recommends that you choose one of these two setup options if you manually deploy scanners:

- Create an AWS account dedicated to Agentless scanners. Deploy a scanner for every region that has cloud resources you want to scan.

  {% image
     source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/setup/cloud_storage/central-scanner.2908be09bc9c7ae5a164fce78c10ee1b.png?auto=format"
     alt="Diagram showing a central scanner for a region and the scanner scanning across different accounts" /%}

- Deploy a scanner for every region that has cloud resources that you want to scan.

  {% image
     source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/setup/cloud_storage/scanner-in-each-region.50a82772b9c07a1ec1ee280c4fe8d471.png?auto=format"
     alt="Diagram showing a scanner in each region that scans accounts within that region" /%}

## Scanning groups{% #scanning-groups %}

In the [Cloud Storage](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration/data-security) settings page, the **Scanning Groups** section is read-only. All [library rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) are applied within the scanning group.

## Cloud service provider cost{% #cloud-service-provider-cost %}

When using Agentless Scanning, there are additional costs for running scanners in your cloud environments.

To establish estimates on scanner costs, reach out to your [Datadog Customer Success Manager](mailto:success@datadoghq.com).

## Disable Agentless scanning{% #disable-agentless-scanning %}

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration/data-security) settings page.
1. Click the pencil icon next to the account for which you want to disable Agentless scanning.
1. Toggle **Enable Sensitive Data Scanning** to off.

## Uninstall Agentless scanning{% #uninstall-agentless-scanning %}

To uninstall Agentless Scanning, log in to your AWS console and delete the CloudFormation stack created for Agentless Scanning.

## Further reading{% #further-reading %}

- [Cloud Security Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning)
- [Learn more about out-of-the-box library rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules)
- [Learn more about creating custom rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules)
