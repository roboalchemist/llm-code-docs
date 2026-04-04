# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui/step-1-download-iam-role-iac-template-web-ui.md

# Step 1: Download IAM role IaC template (Web UI)

Before you can create a Cloud Environment, you must download an Infrastructure as Code (IaC) template declaring a read-only **Identity and Access Management** (IAM) role that Snyk can assume to scan the configuration of resources in your Amazon Web Services (AWS) account.

Use this IaC template to provision the role in [Step 2: Create the Snyk IAM role](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui/step-2-create-the-snyk-iam-role).

You can choose the template format, either [Terraform HCL](https://www.terraform.io/language/syntax/configuration) or [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). The IAM permissions are identical in both, so pick the format you are most comfortable working with.

The steps follow to **download the IaC template**.

1. In the [Snyk Web UI](https://app.snyk.io), navigate to **Integrations** > **Cloud platforms**.
2. Select **AWS**.
3. In the **Add AWS Environment** modal, select the **Terraform** button to download a `snyk-permissions-aws.tf` file or **CloudFormation** to download a `snyk-permissions-aws.yml` file:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fb3e8755cc0e73906541265f5b87d00c143add0d%2Fsnyk-cloud-onboard-aws-ui-download-buttons.png?alt=media" alt=""><figcaption><p>The Add AWS Environment modal</p></figcaption></figure>

You can now proceed to [Step 2: Create the Snyk IAM role (Web UI)](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-web-ui/step-2-create-the-snyk-iam-role).
