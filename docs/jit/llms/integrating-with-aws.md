# Source: https://docs.jit.io/docs/integrating-with-aws.md

# AWS Integration

Integrating with AWS

## Overview

Implementing Jit's AWS integration will enable two core benefits:

* Enable contextual prioritization for security issues, which assigns a risk score to every issue based on their runtime and business context
* Detect security risks in your AWS environment
  * [Scan for Infrastructure Runtime Misconfigurations](https://docs.jit.io/docs/scan-runtime-infra#aws-checklist)
  * [Import AWS Security Hub Findings](https://docs.jit.io/docs/import-aws-security-hub-findings)
  * [Require MFA for AWS](https://docs.jit.io/docs/require-mfa-for-cloud-providers)

Though it does not require the integration steps below, Jit recommends that you also activate the [Scan IaC for Misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations) security requirement for complete infrastructure protection.

## Steps for integrating with AWS

### Integrating with AWS accounts

**To integrate Jit with an AWS account—**

1. Sign in to your AWS account.

2. From the [Integrations Page](https://docs.jit.io/docs/integrations-page), locate the AWS tile and select **Connect**.

3. Select the AWS account tile and select **Next**.

4. Select the region(s) containing the resources you wish to monitor from the dropdown and select **Click here to integrate**. The AWS Management Console opens.

5. You are prompted to create a stack from Jit's template using CloudFormation. [Permissions information](https://docs.jit.io/docs/integrating-with-aws#permissions). Configure parameters as indicated below:
   * AccountName— (optional) Provide a name for identifying this account from within the Jit platform. If none is provided, the name of the account displayed in the Jit platform will be the account ID.
   * ExternalID— Do not change this value.
   * ResourceNamePrefix— If desired, you can alter the name of the prefix that is automatically given to resources created by this template.\
     Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom names.

6. Select **Create stack**. The stack creation process may take a few moments.

7. Confirm successful integration by navigating back to the integrations page and selecting the **Configure** button on the AWS tile. Successful integration is indicated by a list item for the account. In the event of integration failure, see [Troubleshooting AWS Integration](https://docs.jit.io/docs/troubleshooting-aws-integration).

### Integrating with AWS organizations

**To integrate Jit with an AWS organization—**

1. Sign in to the root account of your AWS organization.

2. From the [Integrations Page](https://docs.jit.io/docs/integrations-page), locate the AWS tile and select **Connect**.

3. Select the AWS organization tile and select **Next**.

4. Select the region(s) containing the resources you wish to monitor from the dropdown and open the **Click here to enable stack sets** link in a new window or tab. The AWS Management Console opens. Select **Enabled trusted access** and navigate back to the Jit platform tab.

5. Select **Click here to integrate**.

6. You are prompted to create a stack from Jit's template using CloudFormation. [Permissions information](https://docs.jit.io/docs/integrating-with-aws#permissions). Configure parameters as indicated below:
   * OrganizationRootId— Enter the root ID of your organization here. You can find this information by navigating to [AWS Organizations > AWS Accounts > Root](console.aws.amazon.com/organizations/v2/home/root) in the AWS Management Console. Note that the root ID always begins with "**r-**."\
     ![](https://files.readme.io/f08c762-root_id.png)
   * ExternalID— Do not change this value.
   * ResourceNamePrefix— If desired, you can alter the name of the prefix that is automatically given to resources created by this template.\
     Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom names.

7. Select **Create stack**. The stack creation process may take a few moments.

8. Confirm successful integration by navigating back to the integrations page and selecting the **Configure** button on the AWS tile. Successful integration is indicated by a list item for your management account.  In the event of integration failure, see [Troubleshooting AWS Integration](https://docs.jit.io/docs/troubleshooting-aws-integration).

> 📘 New accounts in monitored organizations
>
> New accounts created within an organization that is integrated with Jit are automatically monitored.

### Automate using terraform

To automate the process using terraform - you can follow [this repo](https://github.com/jitsecurity/jit-customer-scripts/tree/main/src/integrations/aws_integration_automation).

## Permissions

As a necessary part of the integration process, Jit creates a new CloudFormation stack in your AWS account/organization from the following template: <https://jit-aws-prod.s3.amazonaws.com/jit_aws_integration_stack_template_v2.json>.

This template implements the following AWS managed policies to enable read-only permissions required by Jit to run security scans via Prowler.

**AWS managed policies**—

* `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess`
* `arn:aws:iam::aws:policy/SecurityAudit`

For additional information on AWS managed policies, see [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html).

Read-only permission is granted to the following AWS actions—

| Reference                                                                                                                 | Actions                                                                                                                                                                                                                                                     | Resources                         |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [s3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html)                               | GetAccountPublicAccessBlock, GetLifecycleConfiguration, GetBucketPolicy                                                                                                                                                                                     | \*                                |
| [ds](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdirectoryservice.html)                    | List\*                                                                                                                                                                                                                                                      | \*                                |
| [ec2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html)                             | GetEbsEncryptionByDefault                                                                                                                                                                                                                                   | \*                                |
| [ecr](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticcontainerregistry.html)        | Describe\*                                                                                                                                                                                                                                                  | \*                                |
| [elasticfilesystem](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticfilesystem.html) | DescribeBackupPolicy                                                                                                                                                                                                                                        | \*                                |
| [glue](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsglue.html)                              | GetConnections, GetSecurityConfiguration, SearchTables                                                                                                                                                                                                      | \*                                |
| [lambda](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html)                          | GetFunction\*                                                                                                                                                                                                                                               | \*                                |
| [shield](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html)                          | DescribeProtection, GetSubscriptionState                                                                                                                                                                                                                    | \*                                |
| [ssm](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html)                     | GetDocument                                                                                                                                                                                                                                                 | \*                                |
| [support](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupport.html)                        | Describe\*                                                                                                                                                                                                                                                  | \*                                |
| [tag](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonresourcegrouptaggingapi.html)         | GetTagKeys                                                                                                                                                                                                                                                  | \*                                |
| [iam](https://docs.aws.amazon.com/service-authorization/latest/reference/list_identityandaccessmanagement.html)           | ListRoles, ListUsers, GetAccountSummary, ListVirtualMfaDevices ListMfaDevices, GenerateCredentialReport, GetPolicy, GetAccountAuthorizationDetails, GetCredentialReport, GenerateServiceLastAccessedDetails, GetServiceLastAccessedDetails, GetLoginProfile | \*                                |
| [organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html)            | DescribeOrganization, ListPolicies\*, DescribePolicy                                                                                                                                                                                                        | \*                                |
| [cloudtrail](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudtrail.html)                  | DescribeTrails, GetTrail, GetTrailStatus                                                                                                                                                                                                                    | \*                                |
| [access-analyzer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamaccessanalyzer.html)      | Get\_, List\_, ValidatePolicy                                                                                                                                                                                                                               | \*                                |
| [account](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsaccountmanagement.html)              | Get\*                                                                                                                                                                                                                                                       | \*                                |
| [appstream](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappstream2.0.html)              | Describe\_, List\_                                                                                                                                                                                                                                          | \*                                |
| [codeartifact](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodeartifact.html)              | List\*                                                                                                                                                                                                                                                      | \*                                |
| [codebuild](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscodebuild.html)                    | BatchGet\*                                                                                                                                                                                                                                                  | \*                                |
| [macie](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmacie.html)                         | GetMacieSession                                                                                                                                                                                                                                             | \*                                |
| [apigateway](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigatewaymanagement.html)     | GET                                                                                                                                                                                                                                                         | arn:aws:apigateway:*::/restapis/* |

## Disabling AWS accounts/organizations

**To disable monitoring of an AWS account—**

1. From the [Integrations Page](https://docs.jit.io/docs/integrations-page), locate the AWS tile and select **Configure** to open the *Resource management* dialog.
2. Uncheck the account you wish to disable.
3. Select **Update**.

**To disable monitoring of an AWS organization—**

1. From the [Integrations Page](https://docs.jit.io/docs/integrations-page), locate the AWS tile and select **Configure** to open the *Resource management* dialog.
2. Uncheck the management account of the organization you wish to disable.
3. Select **Update**.

## Removing AWS integration

**To remove an AWS account from Jit—**

From the AWS console, navigate to the **Stacks** tab in **CloudFormation** and delete *JitControlsStack*.

**To remove an AWS organization from Jit—**

1. From the AWS console, navigate to the **StackSets** tab in **CloudFormation** and select **JitOrganizationsStacksSet**.
2. Using the **Actions** menu, select **delete stacks from stack set**. This process may take a few minutes.
3. Navigate to the **Stacks** tab, and delete *JitOrganizationsStacksSet*.

## Adding regions

Jit supports adding regions in addition to those specified in your initial integration.

To add regions, navigate to your .jit repo and add the region(s) to your `.jit/jit-integration.yml` file as shown in the examples below.

```yaml AWS account
aws:
- account_id: '123456789012'
  account_name: my account
  regions:
  - us-east-1
  - us-west-2
  - # add regions to this list
  type: account
```
```yaml AWS organization
aws:
- account_id: '123456789012'
  account_name: My organization
  regions:
  - us-east-1
  - # add regions to this list 
  type: org
```