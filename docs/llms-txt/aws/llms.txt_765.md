# Source: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/llms.txt

# AWS Serverless Application Repository Developer Guide

> This developer guide helps you work with AWS Serverless Application Repository, which makes it easy for developers and enterprises to quickly find and deploy serverless applications in the AWS Cloud.

- [What Is the AWS Serverless Application Repository?](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html)
- [Quick Start: Publishing Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-quick-start.html)
- [Quotas](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/quotas.html)
- [Troubleshooting](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/troubleshooting.html)
- [Operations](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/operations.html)
- [Document History](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/glossary.html)

## [Publishing Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-publishing-applications.html)

### [Using AWS SAM with the AWS Serverless Application Repository](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/using-aws-sam.html)

The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS.

- [List of Supported AWS Resources](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/list-supported-resources.html): This is the complete list of AWS resources that are supported by the AWS Serverless Application Repository.

### [How to Publish Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-publish.html)

Procedures for publishing your serverless applications to the AWS Serverless Application Repository.

- [Publishing New Application Versions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-publish-new-version.html): This section shows you how to publish a new version of an existing application to the AWS Serverless Application Repository by using the AWS SAM CLI or the AWS Management Console.
- [Verified Author Badge](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-verified-author.html): Verified authors in the AWS Serverless Application Repository are those for which AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester, and has confirmed that the requester's identity is as claimed.
- [Sharing Lambda Layers](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/sharing-lambda-layers.html): If you've implemented functionality in a Lambda layer, you might want to share your layer without hosting a global instance of it.


## [Deploying Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-consuming-applications.html)

- [Application Deployment Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/application-deployment-permissions.html): To deploy an application in the AWS Serverless Application Repository, you must have permission to do so.
- [Application Capabilities](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/acknowledging-application-capabilities.html): Before you can deploy an application, the AWS Serverless Application Repository checks the applicationâs template for IAM roles, AWS resource policies, and nested applications that the template specifies that it should create.

### [How to Deploy Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-consume.html)

Procedures for deploying serverless applications through the AWS Serverless Application Repository.

- [Updating Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-consume-new-version.html): Procedure for updating serverless applications through the AWS Serverless Application Repository.


## [Security](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security.html)

- [Data Protection](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in the AWS Serverless Application Repository.

### [Identity and Access Management](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security-iam.html)

How to authenticate requests and manage access for your AWS Serverless Application Repository resources.

- [How the AWS Serverless Application Repository Works with IAM](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to the AWS Serverless Application Repository, you should understand what IAM features are available to use with the AWS Serverless Application Repository.
- [Identity-Based Policy Examples](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS Serverless Application Repository resources.
- [Application Policy Examples](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security_iam_resource-based-policy-examples.html): Permissions policies attached to AWS Serverless Application Repository applications are referred to as application policies.
- [AWS Serverless Application Repository API Permissions Reference](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-api-permissions-ref.html): When you set up access control and write permissions policies that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference.
- [Troubleshooting](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with the AWS Serverless Application Repository and IAM.

### [Logging and Monitoring](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security-logging-monitoring.html)

Learn about logging and monitoring in the AWS Serverless Application Repository.

- [Logging AWS Serverless Application Repository API Calls with AWS CloudTrail](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/logging-using-cloudtrail.html): Learn about logging the AWS Serverless Application Repository with AWS CloudTrail.
- [Compliance Validation](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/SAR-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Serverless Application Repository features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/infrastructure-security.html): Learn how the AWS Serverless Application Repository isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Serverless Application Repository.


## [Resources](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/resources.html)

- [Applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html)
- [Applications applicationId](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)
- [Applications applicationId Changesets](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-changesets.html)
- [Applications applicationId Dependencies](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-dependencies.html)
- [Applications applicationId Policy](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-policy.html)
- [Applications applicationId Templates](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-templates.html)
- [Applications applicationId Templates templateId](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-templates-templateid.html)
- [Applications applicationId Unshare](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-unshare.html)
- [Applications applicationId Versions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-versions.html)
- [Applications applicationId Versions semanticVersion](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-versions-semanticversion.html)
