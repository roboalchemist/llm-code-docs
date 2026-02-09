# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-api.md

# AWS Integration: API

Before you can onboard an AWS account to Snyk via the API, you need access to the AWS account and associated credentials with permissions to create a read-only Identity and Access Management (IAM) role. See the prerequisites on the [AWS integration](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration) page.

The steps follow to onboard an AWS account via the API:

1. [Download an infrastructure as code (IaC) template](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-api/step-1-download-iam-role-iac-template-api): to give Snyk permissions to scan your account.
2. [Create an AWS IAM role](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-api/step-2-create-the-snyk-iam-role-api): using the template you downloaded.
3. [Create and scan a Cloud Environment.](https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/aws-integration/aws-integration-api/step-3-create-and-scan-a-cloud-environment-api)

When you have completed the steps, you will be able to do the following:

* View the cloud configuration issues Snyk finds. See [Manage cloud issues](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-issues).
* Prioritize your vulnerabilities with cloud context.
