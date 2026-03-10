# Source: https://docs.aws.amazon.com/powershell/v4/userguide/llms.txt

# AWS Tools for PowerShell (version 4) User Guide

> Describes how to install and use the Tools, such as how to specify credentials and regions, find cmdlets for a service, and use aliases for cmdlets.

- [Cmdlet reference](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-cmdlet-ref.html)
- [Document history](https://docs.aws.amazon.com/powershell/v4/userguide/history-pst.html)

## [What are the AWS Tools for PowerShell?](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-welcome.html)

- [Revision history](https://docs.aws.amazon.com/powershell/v4/userguide/revision-history.html): To find out what has changed in various releases, see the following:
- [What's new](https://docs.aws.amazon.com/powershell/v4/userguide/whats-new.html): For high-level information about new developments related to the AWS Tools for PowerShell, see the product page at https://aws.amazon.com/powershell/ and the change logs.


## [Installation](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-set-up.html)

- [Installing on Windows](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-set-up-windows.html): A Windows-based computer can run any of the AWS Tools for PowerShell package options:
- [Installing on Linux or macOS](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-set-up-linux-mac.html): This topic provides instructions on how to install the AWS Tools for PowerShell on Linux or macOS.
- [Migrating from AWS Tools for PowerShell Version 3.3 to Version 4](https://docs.aws.amazon.com/powershell/v4/userguide/v4migration.html): AWS Tools for PowerShell version 4 is a backward-compatible update to AWS Tools for PowerShell version 3.3.


## [Get started](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-getting-started.html)

### [Configure tool authentication](https://docs.aws.amazon.com/powershell/v4/userguide/creds-idc.html)

You must establish how your code authenticates with AWS when developing with AWS services.

- [Use the AWS CLI](https://docs.aws.amazon.com/powershell/v4/userguide/creds-idc-cli.html): Starting with version 4.1.538 of the Tools for PowerShell, the recommended method to configure SSO credentials and start an AWS access portal session is to use the Initialize-AWSSSOConfiguration and Invoke-AWSSSOLogin cmdlets, as described in .
- [Specify AWS Regions](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-installing-specifying-region.html): There are two ways to specify the AWS Region to use when running AWS Tools for PowerShell commands:
- [Configure federated identity](https://docs.aws.amazon.com/powershell/v4/userguide/saml-pst.html): To let users in your organization access AWS resources, you must configure a standard and repeatable authentication method for purposes of security, auditability, compliance, and the capability to support role and account separation.
- [Cmdlet discovery and aliases](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-discovery-aliases.html): This section shows you how to list services that are supported by the AWS Tools for PowerShell, how to show the set of cmdlets provided by the AWS Tools for PowerShell in support of those services, and how to find alternative cmdlet names (also called aliases) to access those services.
- [Pipelining, output, and iteration](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-pipelines.html)
- [Credential and profile resolution](https://docs.aws.amazon.com/powershell/v4/userguide/creds-assign.html)
- [Users and roles](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-users-roles.html): In order to run Tools for PowerShell commands on AWS, you need to have some combination of users, permission sets, and service roles that are appropriate for your tasks.

### [Using legacy credentials](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-cred-legacy.html)

The topics in this section provide information about using long-term or short-term credentials without using AWS IAM Identity Center.

- [AWS Credentials](https://docs.aws.amazon.com/powershell/v4/userguide/specifying-your-aws-credentials.html): Each AWS Tools for PowerShell command must include a set of AWS credentials, which are used to cryptographically sign the corresponding web service request.
- [Shared Credentials](https://docs.aws.amazon.com/powershell/v4/userguide/shared-credentials-in-aws-powershell.html): The Tools for Windows PowerShell support the use of the AWS shared credentials file, similarly to the AWS CLI and other AWS SDKs.


## [Features](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-features.html)

- [Observability](https://docs.aws.amazon.com/powershell/v4/userguide/observability.html): Learn how to enable and configure telemetry output in the AWS Tools for PowerShell to increase the observability of your application.


## [Work with AWS services](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-using.html)

### [Amazon S3 and Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3.html)

In this section, we create a static website using the AWS Tools for Windows PowerShell using Amazon S3 and CloudFront.

- [Create an Amazon S3 Bucket, Verify Its Region, and Optionally Remove It](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3-bucket-create.html): Use the New-S3Bucket cmdlet to create a new Amazon S3 bucket.
- [Configure an Amazon S3 Bucket as a Website and Enable Logging](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3-create-website.html): Use the Write-S3BucketWebsite cmdlet to configure an Amazon S3 bucket as a static website.
- [Upload Objects to an Amazon S3 Bucket](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3-upload-object.html): Use the Write-S3Object cmdlet to upload files from your local file system to an Amazon S3 bucket as objects.
- [Delete Amazon S3 Objects and Buckets](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3-delete-website.html): This section describes how to delete the website that you created in preceding sections.
- [Upload In-Line Text Content to Amazon S3](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-s3-upload-in-line-text.html): The Write-S3Object cmdlet supports the ability to upload in-line text content to Amazon S3.

### [Amazon EC2 and Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-ec2.html)

- [Create a Key Pair](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-ec2-keypairs.html): The following New-EC2KeyPair example creates a key pair and stores in the PowerShell variable $myPSKeyPair
- [Create a Security Group](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-ec2-sg.html): You can use the AWS Tools for PowerShell to create and configure a security group.
- [Find an AMI](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-ec2-get-amis.html): When you launch an Amazon EC2 instance, you specify an Amazon Machine Image (AMI) to serve as a template for the instance.
- [Launch an Instance](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-ec2-launch.html): To launch an Amazon EC2 instance, you need the key pair and security group that you created in the previous sections.
- [AWS Lambda and AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-lambda.html): By using the AWSLambdaPSCore module, you can develop AWS Lambda functions in PowerShell Core 6.0 using the .NET Core 2.1 runtime.
- [Amazon SQS, Amazon SNS and Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-sqs-queue-sns-topic.html): This section provides examples that show how to:
- [CloudWatch from the AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-cw.html): This section shows an example of how to use the Tools for Windows PowerShell to publish custom metric data to CloudWatch.
- [Using ClientConfig](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-clientconfig.html): The ClientConfig parameter can be used to specify certain configuration settings when you connect to a service.


## [Code examples](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_code_examples.html)

- [ACM](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_acm_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with ACM.
- [Application Auto Scaling](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_application-auto-scaling_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Application Auto Scaling.
- [WorkSpaces Applications](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_appstream_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with WorkSpaces Applications.
- [Aurora](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_aurora_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_auto-scaling_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Auto Scaling.
- [AWS Budgets](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_budgets_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Budgets.
- [AWS Cloud9](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloud9_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Cloud9.
- [CloudFormation](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloudformation_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CloudFormation.
- [CloudFront](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloudfront_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CloudFront.
- [CloudTrail](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloudtrail_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CloudTrail.
- [CloudWatch](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cloudwatch_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CloudWatch.
- [CodeCommit](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_codecommit_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CodeCommit.
- [CodeDeploy](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_codedeploy_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CodeDeploy.
- [CodePipeline](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_codepipeline_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with CodePipeline.
- [Amazon Cognito Identity](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_cognito-identity_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon Cognito Identity.
- [AWS Config](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_config-service_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Config.
- [Device Farm](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_device-farm_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Device Farm.
- [Directory Service](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_directory-service_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Directory Service.
- [AWS DMS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_database-migration-service_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS DMS.
- [DynamoDB](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_dynamodb_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ec2_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon EC2.
- [Amazon ECR](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ecr_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon ECR.
- [Amazon ECS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ecs_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon ECS.
- [Amazon EFS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_efs_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon EFS.
- [Amazon EKS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_eks_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon EKS.
- [Elastic Load Balancing - Version 1](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_elastic-load-balancing_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Elastic Load Balancing - Version 1.
- [Elastic Load Balancing - Version 2](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_elastic-load-balancing-v2_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Elastic Load Balancing - Version 2.
- [Amazon FSx](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_fsx_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon FSx.
- [Amazon Glacier](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_glacier_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon Glacier.
- [AWS Glue](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_glue_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Glue.
- [AWS Health](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_health_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Health.
- [IAM](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_iam_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with IAM.
- [Kinesis](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_kinesis_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Kinesis.
- [Lambda](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_lambda_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Lambda.
- [Amazon ML](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_machine-learning_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon ML.
- [Macie](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_macie2_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Macie.
- [AWS Price List](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_pricing_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS Price List.
- [Resource Groups](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_resource-groups_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Resource Groups.
- [Resource Groups Tagging API](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_resource-groups-tagging-api_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Resource Groups Tagging API.
- [RouteÂ 53](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_route-53_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with RouteÂ 53.
- [Amazon S3](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_s3_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon S3.
- [Security Hub CSPM](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_securityhub_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Security Hub CSPM.
- [Amazon SES](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ses_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon SES.
- [Amazon SES API v2](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_sesv2_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon SES API v2.
- [Amazon SNS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_sns_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_sqs_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon SQS.
- [AWS STS](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_sts_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS STS.
- [Support](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_support_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Support.
- [Systems Manager](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ssm_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Systems Manager.
- [Amazon Translate](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_translate_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with Amazon Translate.
- [AWS WAFV2](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_wafv2_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with AWS WAFV2.
- [WorkSpaces](https://docs.aws.amazon.com/powershell/v4/userguide/powershell_workspaces_code_examples.html): Code examples that show how to use AWS Tools for PowerShell V4 with WorkSpaces.


## [Security](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-security.html)

- [Data protection](https://docs.aws.amazon.com/powershell/v4/userguide/pstools-security-data-protection.html): Learn how the AWS shared responsibility model applies to data protection when using the AWS Tools for PowerShell.
- [Identity and Access Management](https://docs.aws.amazon.com/powershell/v4/userguide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/powershell/v4/userguide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/powershell/v4/userguide/enforcing-tls.html): Learn how to enforce TLS version in the Tools for PowerShell.
- [Additional security considerations](https://docs.aws.amazon.com/powershell/v4/userguide/additional-security-considerations.html): Understand additional security considerations for the Tools for PowerShell.
