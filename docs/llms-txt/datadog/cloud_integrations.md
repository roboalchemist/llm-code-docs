# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/cloud_integrations.md

---
title: Deploying Cloud Security via Cloud Integrations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security >
  Deploying Cloud Security via Cloud Integrations
---

# Deploying Cloud Security via Cloud Integrations

Use the following instructions to enable Misconfigurations and Identity Risks (CIEM) on AWS, Azure, and GCP.

## Enable resource scanning{% #enable-resource-scanning %}

To enable resource scanning for your cloud accounts, you must first set up the integration and then enable Cloud Security for each AWS account, Azure account, and Google Cloud account.

{% alert level="info" %}
Collecting events using Cloud Security Management will affect your billing. For more information, see [Datadog Pricing](https://www.datadoghq.com/pricing/?product=cloud-security-management#products).
{% /alert %}

{% tab title="AWS" %}
### Set up the Datadog AWS integration{% #set-up-the-datadog-aws-integration %}

If you haven't already, set up the [Amazon Web Services integration](https://docs.datadoghq.com/integrations/amazon_web_services/). You must also [enable resource collection](https://docs.datadoghq.com/integrations/amazon_web_services/?tab=roledelegation#cloud-security-management) by attaching the AWS-managed SecurityAudit Policy to the Datadog IAM role in your AWS account.

### Enable Cloud Security for your AWS accounts{% #enable-cloud-security-for-your-aws-accounts %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations**.
1. Expand the **AWS** section and click the account you want to enable Cloud Security for. A side panel with configuration options for that account opens.
1. Under **Features**, beside each feature you want to enable, turn on the **Enable** toggle.
1. To create a filter that excludes certain resources from being evaluated by Cloud Security, under **Evaluation Filters**, click **Limit to Specific Resources**. Then, click **Add Resource Tags**, add `key:value` tags as required, and click **Save**. For more information, see [Use Filters to Exclude Resources from Evaluation](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters).

{% /tab %}

{% tab title="Azure" %}
### Set up the Datadog Azure integration{% #set-up-the-datadog-azure-integration %}

If you haven't already, set up the [Microsoft Azure integration](https://docs.datadoghq.com/integrations/azure).

**Note**: To access the full set of Azure compliance rulesâincluding [Identity Risks](https://docs.datadoghq.com/security/cloud_security_management/identity_risks)âyou must enable the following permissions for the [Microsoft Graph API](https://docs.datadoghq.com/integrations/guide/azure-graph-api-permissions/).

- `AuditLog.Read.All`
- `AdministrativeUnit.Read.All`
- `Application.Read.All`
- `Directory.Read.All`
- `Domain.Read.All`
- `Group.Read.All`
- `Policy.Read.All`
- `PrivilegedAssignmentSchedule.Read.AzureADGroup`
- `PrivilegedEligibilitySchedule.Read.AzureADGroup`
- `RoleManagement.Read.All`
- `User.Read.All`

### Enable Cloud Security for your Azure subscriptions{% #enable-cloud-security-for-your-azure-subscriptions %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations**.
1. Expand the **Azure** section.
1. To enable resource scanning for a subscription, switch the **Resource Scanning** toggle to the on position.
1. To create a filter that excludes certain resources from being evaluated by Cloud Security, click the **Plus** (+) icon under **Resource Evaluation Filters (Optional)**. For more information, see [Use Filters to Exclude Resources from Evaluation](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters).
1. Click **Done**.

{% /tab %}

{% tab title="Google Cloud" %}
### Set up the Datadog Google Cloud Platform integration{% #set-up-the-datadog-google-cloud-platform-integration %}

The Datadog Google Cloud Platform integration uses service accounts to create an API connection between Google Cloud and Datadog. To enable metric collection, create a service account, and then provide Datadog with the service account credentials to begin making API calls on your behalf. For step-by-step instructions, see [Create your Google Cloud service account](https://docs.datadoghq.com/integrations/google_cloud_platform/#1-create-your-google-cloud-service-account).

**Note**: [Google Cloud billing](https://support.google.com/cloud/answer/6293499?hl=en), the [Cloud Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com), the [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com), and the [Cloud Asset API](https://console.cloud.google.com/apis/api/cloudasset.googleapis.com/overview) must all be enabled for the projects you wish to monitor.

#### Datadog{% #datadog %}

1. In Datadog, navigate to the [**Google Cloud Platform Integration**](https://app.datadoghq.com/integrations/google-cloud-platform) page.
1. On the **Configuration** tab, locate the service account and select **Upload Private Key File** to integrate the project with Datadog.
1. Upload the JSON file, then click **Update Configuration**.
1. To monitor multiple projects, use one of the following methods:
   - Repeat the process above to use multiple service accounts.
   - Use the same service account by updating the `project_id` in the downloaded JSON file. Then, upload the file to Datadog as described in steps 1-3.

### Enable Cloud Security for your Google Cloud projects{% #enable-cloud-security-for-your-google-cloud-projects %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations**.
1. Expand the **GCP** section.
1. To enable resource scanning for a project, switch the **Resource Scanning** toggle to the on position.
1. To create a filter that excludes certain resources from being evaluated by Cloud Security, click the **Plus** (+) icon under **Resource Evaluation Filters (Optional)**. For more information, see [Use Filters to Exclude Resources from Evaluation](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters).
1. Click **Done**.

{% /tab %}

## Disable resource scanning{% #disable-resource-scanning %}

{% alert level="info" %}
You can access historical findings from the past 15 months even if resource scanning is disabled.
{% /alert %}

{% tab title="AWS" %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **AWS**.
1. If required, use filters to find the account you want to stop resource scanning for. Click the account to open the side panel that contains its settings.
1. On the **Features** tab, beside **Posture Management**, switch the **Enable** toggle to the off position.

{% /tab %}

{% tab title="Azure" %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **Azure**.
1. To stop resource scanning for an account, switch the **Resource Scanning** toggle to the off position.
1. Click **Done**.

{% /tab %}

{% tab title="Google Cloud" %}

1. On the [**Cloud Security Setup**](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **GCP**.
1. To stop resource scanning for an account, switch the **Resource Scanning** toggle to the off position.
1. Click **Done**.

{% /tab %}
