# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/enable.md

---
title: Enabling Agentless Scanning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Cloud
  Security Agentless Scanning > Enabling Agentless Scanning
---

# Enabling Agentless Scanning

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Agentless Scanning provides visibility into vulnerabilities that exist within your cloud infrastructure, without requiring you to install the Datadog Agent. To learn more about Agentless Scanning's capabilities and how it works, see the [Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning) docs.

## Prerequisites{% #prerequisites %}

Before setting up Agentless Scanning, ensure the following prerequisites are met:

- **Remote Configuration**: [Remote Configuration](https://docs.datadoghq.com/remote_configuration) is required to enable Datadog to send information to Agentless scanners, such as which cloud resources to scan.

- **API and Application Keys**:

  - An API key with Remote Configuration enabled is required for scanners to report scan results to Datadog.
  - An Application key with either **Integrations Manage** or **Org Management** permissions is required to enable scanning features through the Datadog API.

- **Cloud permissions**: The Agentless Scanning instance requires specific permissions to scan hosts, host images, container registries, and functions. These permissions are automatically applied as part of the installation process and are strictly limited to the minimum permissions required to perform the necessary scans, following the principle of least privilege.

  {% collapsible-section %}
  AWS scanning permissions: 
Scanning permissions:

  - `ebs:GetSnapshotBlock`
  - `ebs:ListChangedBlocks`
  - `ebs:ListSnapshotBlocks`
  - `ec2:CopySnapshot`
  - `ec2:CreateSnapshot`
  - `ec2:CreateTags`
  - `ec2:DeleteSnapshot`
  - `ec2:DeregisterImage`
  - `ec2:DescribeSnapshotAttribute`
  - `ec2:DescribeSnapshots`
  - `ec2:DescribeVolumes`
  - `ecr:BatchGetImage`
  - `ecr:GetAuthorizationToken`
  - `ecr:GetDownloadUrlForLayer`
  - `kms:CreateGrant`
  - `kms:Decrypt`
  - `kms:DescribeKey`
  - `lambda:GetFunction`
  - `lambda:GetLayerVersion`

Only when Sensitive Data Scanning (DSPM) is enabled:

  - `kms:GenerateDataKey`
  - `s3:GetObject`
  - `s3:ListBucket`

    {% /collapsible-section %}



  {% collapsible-section %}
  Azure scanning permissions: 
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/instanceView/read`
  - `Microsoft.Compute/virtualMachineScaleSets/read`
  - `Microsoft.Compute/virtualMachineScaleSets/instanceView/read`
  - `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read`
  - `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/instanceView/read`
  - `Microsoft.Compute/disks/read`
  - `Microsoft.Compute/disks/beginGetAccess/action`
  - `Microsoft.Compute/disks/endGetAccess/action`

    {% /collapsible-section %}

  {% collapsible-section %}
  GCP scanning permissions: 
  - `compute.disks.create`
  - `compute.disks.createSnapshot`
  - `compute.disks.delete`
  - `compute.disks.get`
  - `compute.disks.setLabels`
  - `compute.disks.use`
  - `compute.globalOperations.get`
  - `compute.images.get`
  - `compute.instances.attachDisk`
  - `compute.instances.detachDisk`
  - `compute.snapshots.create`
  - `compute.snapshots.get`
  - `compute.snapshots.list`
  - `compute.snapshots.delete`
  - `compute.snapshots.setLabels`

    {% /collapsible-section %}

## Setup{% #setup %}

{% alert level="danger" %}
Running Agentless scanners incurs additional costs. To optimize these costs while still ensuring reliable 12-hour scans, Datadog recommends setting up Agentless Scanning with Terraform as the default template.
{% /alert %}

To enable Agentless Scanning, use one of the following workflows:

### Quick start{% #quick-start %}

Designed for new users, the quick start workflow offers an efficient setup process for Cloud Security, enabling immediate monitoring of AWS resources. It uses AWS CloudFormation to automate the configuration.

{% collapsible-section #quick-start-setup %}
#### Quick start setup guide

Designed for new users, the quick start workflow offers an efficient setup process for Cloud Security, enabling immediate monitoring of AWS resources. It uses AWS CloudFormation to automate the configuration, and includes the Cloud Security features: Misconfigurations, Identity Risks (CIEM), and Vulnerability Management.

{% alert level="info" %}
This article provides instructions for the new user quick start workflow that uses AWS CloudFormation to set up Agentless Scanning. For existing users who want to add a new AWS account or enable Agentless Scanning on an existing integrated AWS account, see the instructions for Terraform or AWS CloudFormation.
{% /alert %}

{% alert level="danger" %}
Running Agentless scanners incurs additional costs. To optimize these costs while still ensuring reliable 12-hour scans, Datadog recommends setting up Agentless Scanning with Terraform as the default template.
{% /alert %}

{% alert level="danger" %}
Sensitive Data Scanner for cloud storage is in Limited Availability. [Request Access](https://www.datadoghq.com/private-beta/data-security) to enroll.
{% /alert %}

##### Installation{% #installation %}

1. On the [Intro to Cloud Security](https://app.datadoghq.com/security/csm/) page, click **Get Started with Cloud Security**.
1. Click **Quick Start**. The **Features** page is displayed, showing the features included with Agentless Scanning Quick Start.
1. Click **Start Using Cloud Security** to continue.
1. Select the AWS region where you want to create the CloudFormation stack.
1. Select an API key that is already configured for Remote Configuration. If the API key you select does not have Remote Configuration enabled, Remote Configuration is automatically enabled for that key upon selection.
1. Choose whether to enable **Sensitive Data Scanner** for cloud storage. This automatically catalogs and classifies sensitive data in Amazon S3 resources.
1. Click **Launch CloudFormation Template**. A new window opens, displaying the AWS CloudFormation screen. Use the provided CloudFormation template to create a stack. The template includes the IAM permissions required to deploy and manage Agentless scanners.

##### Update the CloudFormation stack{% #update-the-cloudformation-stack %}

Datadog recommends updating the CloudFormation stack regularly, so you can get access to new features and bug fixes as they get released. To do so, follow these steps:

1. Log in to your AWS console and go to the CloudFormation Stacks page.
1. Select the **DatadogIntegration-DatadogAgentlessScanning-â¦** CloudFormation sub-stack, click **Update**, then click **Update nested stack**.
1. Click **Replace existing template**.
1. In the following S3 URL: `https://datadog-cloudformation-template-quickstart.s3.amazonaws.com/aws/<VERSION>/datadog_agentless_scanning.yaml`, replace `<VERSION>` with the version found in [aws_quickstart/version.txt](https://github.com/DataDog/cloudformation-template/blob/master/aws_quickstart/version.txt). Paste that URL into the **Amazon S3 URL** field.
1. Click **Next** to advance through the next several pages without modifying them, then submit the form.

{% /collapsible-section %}

### Terraform{% #terraform %}

The [Terraform Datadog Agentless Scanner module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner) provides a simple and reusable configuration for installing the Datadog Agentless scanner for AWS, Azure, and GCP.

{% collapsible-section #terraform-setup %}
#### Terraform setup guide

If you've already [set up Cloud Security](https://app.datadoghq.com/security/configuration/csm/setup) and want to add a new cloud account or enable [Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning) on an existing integrated cloud account, you can use either Terraform, AWS CloudFormation, or Azure Resource Manager. This article provides detailed instructions for the Terraform approach.

{% alert level="info" %}
If you're setting up Cloud Security for the first time, you can follow the quick start workflow, which uses AWS CloudFormation to enable Agentless Scanning.
{% /alert %}

{% tab title="New AWS account" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations > AWS**.
1. At the bottom of the AWS section, click **Add AWS accounts by following these steps**. The **Add New AWS Account(s)** dialog is displayed.
1. Under **Choose a method for adding your AWS account**, select **Manually**.
1. Follow the instructions for installing the [Datadog Agentless Scanner module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/blob/main/README.md).
1. Select the **I confirm that the Datadog IAM Role has been added to the AWS Account** checkbox.
1. Enter the **AWS Account ID** and **AWS Role Name**.
1. Click **Save**.

{% /tab %}

{% tab title="Existing AWS account" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations > AWS**.
1. Click the **Edit scanning** button () for the AWS account where you want to deploy the Agentless scanner.
1. **Enable Resource Scanning** should already be toggled on. If it isn't, toggle **Enable Resource Scanning** to the on position.
1. In the **How would you like to set up Agentless Scanning?** section, select **Terraform**.
1. Follow the instructions for installing the [Datadog Agentless Scanner module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/blob/main/README.md).
1. Select the **I confirm the Terraform module is installed** check box.
1. Click **Done**.

{% /tab %}

{% tab title="Existing Azure account" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations > Azure**.
1. Expand the Tenant containing the subscription where you want to deploy the Agentless scanner.
1. Click the **Enable** button for the Azure account where you want to deploy the Agentless scanner.
1. Toggle **Vulnerability Scanning** to the on position.
1. In the **How would you like to set up Agentless Scanning?** section, select **Terraform**.
1. Follow the instructions for installing the [Datadog Agentless Scanner module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/tree/main/azure#readme).
1. Click **Done**.

{% /tab %}

{% tab title="Existing GCP project" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations > GCP**.
1. Expand the account containing the project where you want to deploy the Agentless scanner.
1. Click the **Enable** button for the GCP project where you want to deploy the Agentless scanner.
1. Toggle **Vulnerability Scanning** to the on position.
1. Follow the instructions for installing the [Datadog Agentless Scanner module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/tree/main/gcp#readme).
1. Click **Done**.

{% /tab %}

##### Update the Terraform modules version{% #update-the-terraform-modules-version %}

Update the `source` reference for the Agentless Scanner modules to the latest release. You can find the latest version on [GitHub Releases](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/releases).

For usage examples, refer to our [Github repository](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/tree/main/examples).
{% /collapsible-section %}

### AWS Cloudformation{% #aws-cloudformation %}

Use the AWS CloudFormation template to create a CloudFormation stack. The template includes the IAM permissions required to deploy and manage Agentless scanners.

{% collapsible-section #aws-cloudformation-setup %}
#### AWS CloudFormation setup guide

If you've already [set up Cloud Security](https://app.datadoghq.com/security/configuration/csm/setup) and want to add a new cloud account or enable [Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning) on an existing integrated AWS account, you can use either Terraform or AWS CloudFormation. This article provides detailed instructions for the AWS CloudFormation approach.

{% alert level="info" %}
If you're setting up Cloud Security for the first time, you can follow the quick start workflow, which also uses AWS CloudFormation to enable Agentless Scanning.
{% /alert %}

{% alert level="danger" %}
Running Agentless scanners incurs additional costs. To optimize these costs while still ensuring reliable 12-hour scans, Datadog recommends setting up Agentless Scanning with Terraform as the default template.
{% /alert %}

{% alert level="danger" %}
Sensitive Data Scanner for cloud storage is in Limited Availability. [Request Access](https://www.datadoghq.com/private-beta/data-security) to enroll.
{% /alert %}

##### Set up AWS CloudFormation{% #set-up-aws-cloudformation %}

{% tab title="New AWS account" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **AWS**.
1. At the bottom of the AWS section, click **Add AWS accounts by following these steps**. The **Add New AWS Account(s)** dialog is displayed.
1. Select the AWS region where you want to create the CloudFormation stack.
1. Select an API key that is already configured for Remote Configuration. If the API key you select does not have Remote Configuration enabled, Remote Configuration is automatically enabled for that key upon selection.
1. Choose whether to enable **Sensitive Data Scanner** for cloud storage. This automatically catalogs and classifies sensitive data in Amazon S3 resources.
1. Click **Launch CloudFormation Template**. A new window opens, displaying the AWS CloudFormation screen. Use the provided CloudFormation template to create a stack. The template includes the IAM permissions required to deploy and manage Agentless scanners.

{% /tab %}

{% tab title="Existing AWS account" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **AWS**.
1. Click the **Edit** button () for the AWS account where you want to deploy the Agentless scanner.
1. Verify that **Enable Resource Scanning** is toggled on. If it isn't, switch the **Enable Resource Scanning** toggle to the on position and complete Steps 3-7 in [New AWS Account](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/enable?tab=newawsaccount#set-up-aws-cloudformation).
1. In the **Agentless Scanning** section, toggle **Enable Vulnerability Management (Host, Container and Lambda)** to the on position.
1. Choose whether to **Enable Sensitive Data Scanner for Cloud Storage**. This automatically catalogs and classifies sensitive data in Amazon S3 resources.
1. Click **Done**.

{% /tab %}

##### Update the CloudFormation stack{% #update-the-cloudformation-stack-1 %}

Datadog recommends updating the CloudFormation stack regularly, so you can get access to new features and bug fixes as they get released. To do so, follow these steps:

1. Log in to your AWS console and go to the CloudFormation Stacks page.
1. Select the **DatadogIntegration-DatadogAgentlessScanning-â¦** CloudFormation sub-stack, click **Update**, then click **Update nested stack**.
1. Click **Replace existing template**.
1. In the following S3 URL: `https://datadog-cloudformation-template-quickstart.s3.amazonaws.com/aws/<VERSION>/datadog_agentless_scanning.yaml`, replace `<VERSION>` with the version found in [aws_quickstart/version.txt](https://github.com/DataDog/cloudformation-template/blob/master/aws_quickstart/version.txt). Paste that URL into the **Amazon S3 URL** field.
1. Click **Next** to advance through the next several pages without modifying them, then submit the form.

{% /collapsible-section %}

### AWS CloudFormation StackSet (Multi-Account){% #aws-cloudformation-stackset-multi-account %}

For AWS Organizations with multiple accounts, use a CloudFormation StackSet to deploy the Agentless Scanning delegate role across all member accounts. This approach automates the onboarding process and ensures new accounts added to your Organization are automatically configured.

{% collapsible-section #aws-cloudformation-stackset-setup %}
#### AWS CloudFormation StackSet setup guide

This setup deploys the delegate role required for [cross-account scanning](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/deployment_methods) across your AWS Organization or specific Organizational Units (OUs).

##### Prerequisites{% #prerequisites-1 %}

1. Access to the AWS management account.
1. [Trusted Access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) must be enabled for CloudFormation StackSets.
1. Agentless Scanning must already be configured in your central scanning account. See AWS CloudFormation or Terraform setup.

##### Deploy the StackSet{% #deploy-the-stackset %}

1. Log in to your AWS management account and navigate to **CloudFormation > StackSets**.

1. Click **Create StackSet**.

1. Select **Service-managed permissions**.

1. Under **Specify template**, select **Amazon S3 URL** and enter the following URL:

```text
   https://datadog-cloudformation-template-quickstart.s3.amazonaws.com/aws/v4.3.1/datadog_agentless_delegate_role_stackset.yaml
```

Enter a **StackSet name** (for example, `DatadogAgentlessScanningStackSet`).

Configure the required parameters:

- **ScannerInstanceRoleARN**: The ARN of the IAM role attached to your Agentless scanner instances.

The `ScannerInstanceRoleARN` establishes a trust relationship between the delegate role (created in target accounts) and your scanner instances (already running in the central account). This enables cross-account scanning where:

1. The scanner runs in Account A.
1. The delegate role exists in Accounts B, C, D (deployed through the StackSet).
1. The scanner assumes the delegate roles to scan resources in those accounts.

Set **Deployment targets** to deploy across your Organization or specific OUs.

Enable **Automatic deployment** to automatically configure new accounts added to your Organization.

Select a **single region** for deployment (the IAM role is global and only needs to be deployed once per account).

Review and submit the StackSet.

After the StackSet deploys successfully, the member accounts are configured to allow cross-account scanning from your central scanner account.
{% /collapsible-section %}

### Azure Resource Manager{% #azure-resource-manager %}

Use the Azure Resource Manager template to deploy the Agentless Scanner. The template includes the role definitions required to deploy and manage Agentless scanners.

{% collapsible-section #azure-resource-manager-setup %}
#### Azure Resource Manager setup guide

If you've already [set up Cloud Security](https://app.datadoghq.com/security/configuration/csm/setup) and want to add a new Azure account or enable [Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning) on an existing integrated Azure account, you can use either Terraform or Azure Resource Manager. This article provides detailed instructions for the Azure Resource Manager approach.

{% alert level="danger" %}
Running Agentless scanners incurs additional costs. To optimize these costs while still ensuring reliable 12-hour scans, Datadog recommends setting up Agentless Scanning with Terraform as the default template.
{% /alert %}

{% tab title="New Azure account" %}
###### Set up the Datadog Azure integration{% #set-up-the-datadog-azure-integration %}

Follow the instructions for setting up the [Datadog Azure integration](https://docs.datadoghq.com/integrations/guide/azure-manual-setup/?tab=azurecli).

### Enable Agentless Scanning for your Azure subscriptions{% #enable-agentless-scanning-for-your-azure-subscriptions %}

Complete the following steps to enable Agentless Scanning for your Azure subscriptions:

#### Cloud Security Setup page{% #cloud-security-setup-page %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **Azure**.
1. Locate the tenant ID of your subscription.
1. **(Optional)** To enable detection of misconfigurations, toggle **Resource Scanning** to the on position.
1. Expand the list of Azure subscriptions and locate the subscription where you want to deploy the Agentless scanner.
1. Click the **Enable** button under **Vulnerability Scanning**.
1. The **Vulnerability Scanning** dialog is displayed. Toggle **Vulnerability Scanning** to the on position.
1. Under **How would you like to set up Agentless Scanning?**, select **Azure Resource Manager**.
1. Click **Launch Azure Resource Manager** to be redirected to the Azure portal.

#### Azure portal{% #azure-portal %}

1. Log in to the Azure portal. The template creation form is displayed.
1. Select the subscription and the resource group in which the Agentless scanners are to be deployed. Datadog recommends that you deploy the Datadog Agentless Scanner in a dedicated resource group.
1. In **Subscriptions to scan**, select all the subscriptions you want to scan.
1. Enter your **Datadog API Key**, select your **Datadog Site**, and fill out the remainder of the form.
1. Click on **Review + create**.

{% /tab %}

{% tab title="Existing Azure account" %}
### Enable Agentless Scanning for your Azure subscriptions{% #enable-agentless-scanning-for-your-azure-subscriptions %}

Complete the following steps to enable Agentless Scanning for your Azure subscriptions:

#### Cloud Security Setup page{% #cloud-security-setup-page %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **Azure**.
1. Locate the tenant ID of your subscription.
1. **(Optional)** To enable detection of misconfigurations, toggle **Resource Scanning** to the on position.
1. Expand the list of Azure subscriptions and locate the subscription where you want to deploy the Agentless scanner.
1. Click the **Enable** button under **Vulnerability Scanning**.
1. The **Vulnerability Scanning** dialog is displayed. Toggle **Vulnerability Scanning** to the on position.
1. Under **How would you like to set up Agentless Scanning?**, select **Azure Resource Manager**.
1. Click **Launch Azure Resource Manager** to be redirected to the Azure portal.

#### Azure portal{% #azure-portal %}

1. Log in to the Azure portal. The template creation form is displayed.
1. Select the subscription and the resource group in which the Agentless scanners are to be deployed. Datadog recommends that you deploy the Datadog Agentless Scanner in a dedicated resource group.
1. In **Subscriptions to scan**, select all the subscriptions you want to scan.
1. Enter your **Datadog API Key**, select your **Datadog Site**, and fill out the remainder of the form.
1. Click on **Review + create**.

{% /tab %}

{% /collapsible-section %}

## Configuration{% #configuration %}

### Verify your setup{% #verify-your-setup %}

After completing the setup, you can verify that Agentless Scanning is working correctly by checking for scan results in Datadog. Results typically appear after the first scan cycle completes.

View scan results in the following locations:

- **For host and container vulnerabilities**: [CSM Vulnerabilities Explorer](https://app.datadoghq.com/security/csm/vm). To view only vulnerabilities detected by Agentless Scanning, use the filter `origin:"Agentless scanner"` in the search bar.
- **For Lambda vulnerabilities**: [Code Security (SCA) Explorer](https://app.datadoghq.com/security/code-security/sca)
- **For sensitive data findings**: [Sensitive Data Scanner](https://app.datadoghq.com/sensitive-data-scanner/storage)

### Exclude resources from scans{% #exclude-resources-from-scans %}

To exclude hosts, containers, and functions from scans, apply the tag `DatadogAgentlessScanner:false` to each resource. For detailed instructions, refer to the [Resource Filters documentation](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters/).

## Disable Agentless scanning{% #disable-agentless-scanning %}

{% tab title="AWS" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **AWS**.
1. If required, use filters to find the account you want to stop agentless scanning for. Click the account to open the side panel that contains its settings.
1. On the **Features** tab, click **Configure Agentless Scanning** or **Manage** to open the Agentless Scanning Setup modal.
1. Under **How would you like to set up Agentless scanning?**, click **Terraform**.
1. Under **Enable Features**, beside **Enable Agentless Vulnerability management**, switch the toggle to the off position.
1. Click **Done**.

{% /tab %}

{% tab title="Azure" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **Azure**.
1. Locate your subscription's tenant, expand the list of subscriptions, and identify the subscription for which you want to disable Agentless Scanning.
1. Beside the **Enabled** label, click the **Edit** button () to open the Vulnerability Scanning modal.
1. Beside **Vulnerability Scanning**, switch the toggle to the off position.
1. Click **Done**.

{% /tab %}

{% tab title="GCP" %}

1. On the [Cloud Security Setup](https://app.datadoghq.com/security/configuration/csm/setup) page, click **Cloud Integrations** > **GCP**.
1. Expand the account containing the project where you want to disable Agentless scanning.
1. Beside the **Enabled** label, click the **Edit** button () to open the Vulnerability Scanning modal.
1. Beside **Vulnerability Scanning**, switch the toggle to the off position.
1. Click **Done**.

{% /tab %}

## Uninstall Agentless scanning{% #uninstall-agentless-scanning %}

{% tab title="Terraform" %}
To uninstall Agentless Scanning, remove the scanner module from your Terraform code. For more information, see the [Terraform module](https://github.com/DataDog/terraform-module-datadog-agentless-scanner/blob/main/README.md#uninstall) documentation.
{% /tab %}

{% tab title="AWS CloudFormation" %}
To uninstall Agentless Scanning, log in to your AWS console and delete the CloudFormation stack created for Agentless Scanning.
{% /tab %}

{% tab title="Azure Resource Manager" %}
To uninstall Agentless Scanning, log in to your Azure account. If you created a dedicated resource group for the Agentless scanner, delete this resource group along with the following Azure role definitions:

- Datadog Agentless Scanner Role
- Datadog Agentless Scanner Delegate Role

If you did not use a dedicated resource group, you must manually delete the scanner resources, which can be identified by the tags `Datadog:true` and `DatadogAgentlessScanner:true`.
{% /tab %}

## Further reading{% #further-reading %}

- [Setting up Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup)
- [Cloud Security Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/agentless_scanning)
