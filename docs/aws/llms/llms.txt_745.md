# Source: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/llms.txt

# AWS SDK for .NET (V4) Developer Guide

> Developer Guide for the AWS SDK for .NET (version 4). Describes the features of the SDK and how to use them.

- [API reference](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sdk-api-ref.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/document-history.html)

## [What is the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html)

- [Related AWS tools](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/related-tools.html)
- [Supported platforms](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-supported-platforms.html): Information about the platforms supported by the AWS SDK for .NET.
- [SDKs and Tools Reference](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sdks-and-tools-ref.html): The AWS SDKs and Tools Reference Guide contains information that's relevant and important for many of the AWS SDKs and toolkits and the AWS CLI.
- [Revision history](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/revision-history.html): To find out what has changed in various releases, see the following:
- [What's new](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/whats-new.html): For high-level information about new developments related to the AWS SDK for .NET, see the product page at https://aws.amazon.com/sdk-for-net/ and the SDK change logs.
- [Additional resources](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-additional-resources.html): Supported services


## [Getting started](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-config.html)

- [Installing and configuring your toolchain](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-dev-env.html): Install and configure your toolchain for using the AWS SDK for .NET.
- [Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creds-idc.html): You must establish how your code authenticates with AWS when developing with AWS services.

### [Creating a simple application](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/quick-start.html)

Take a quick tour of the AWS SDK for .NET.

- [Simple cross-platform app](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/quick-start-s3-1-cross.html): Tutorial to create a simple cross-platform application using the AWS SDK for .NET.
- [Simple Windows-based app](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/quick-start-s3-1-winvs.html): Tutorial to create a simple Windows-based application using the AWS SDK for .NET.
- [Next steps](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/quick-start-next-steps.html): Be sure to clean up any leftover resources that you created while performing these tutorials.


## [Configuring](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/configuring-the-sdk.html)

- [Start a new project](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-start-new-project.html): Start a new project with the AWS SDK for .NET.
- [Install AWSSDK packages with NuGet](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-install-assemblies.html): Install AWSSDK packages with NuGet when using the AWS SDK for .NET.
- [Install AWSSDK assemblies without NuGet](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-install-without-nuget.html): This topic describes how you can use the AWSSDK assemblies that you obtained and stored locally (or on premises) as described in .
- [AWS Region](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-region-selection.html): Using AWS Regions to access AWS services in a specific geographic region.
- [Credential and profile resolution](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creds-assign.html): How to resolve credentials for the AWS SDK for .NET.
- [Retries and timeouts](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/retries-timeouts.html): Configure retries and timeouts in the AWS SDK for .NET.

### [Observability](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability.html)

Learn how to enable and configure telemetry output in the AWS SDK for .NET to increase the observability of your application.

- [Metrics](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability-metrics.html): The following table lists the telemetry metrics that the SDK emits.

### [Telemetry providers](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability-telemetry-providers.html)

The SDK provides an implementation of OpenTelemetry as a telemetry provider, which is described in the next section.

- [OpenTelemetry](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability-telemetry-providers-otel.html): The AWS SDK for .NET includes an implementation of an OpenTelemetry-based telemetry provider.
- [Users and roles](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-users-roles.html): For doing .NET development on AWS or for running .NET applications on AWS, you need to have some combination of users, permission sets, and service roles that are appropriate for these tasks.

### [Advanced configuration](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-advanced-config.html)

The topics in this section contain information about additional configuration tasks and methods that might be of interest to you.

- [AWSSDK.Extensions.NETCore.Setup and IConfiguration](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-config-netcore.html): Configuring the AWS SDK for .NET with .NET Core
- [Configuring Other Application Parameters](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-config-other.html)
- [Configuration Files Reference for AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-config-ref.html)

### [Using legacy credentials](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-legacy-creds.html)

The topics in this section provide information about using long-term or short-term credentials without using AWS IAM Identity Center.

- [Using the shared AWS credentials file](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creds-file.html): Use the shared AWS credentials file with the AWS SDK for .NET.
- [Using the SDK Store (Windows only)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sdk-store.html): Use the SDK Store for credentials in the AWS SDK for .NET.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-sdk-features.html)

- [Asynchronous programming](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sdk-net-async-api.html): Using asynchronous APIs with the AWS SDK for .NET.
- [Pagination](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/paginators.html): Some AWS services collect and store a large amount of data, which you can retrieve by using the API calls of the AWS SDK for .NET.
- [Support for HTTP 2](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/http2-support.html): Some AWS services and operations require HTTP 2.
- [Additional tools](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sdk-features-additional-tools.html): The following are some additional tools that you can use to ease the work of developing, deploying, and maintaining your .NET applications.


## [Advanced auth](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/advanced-auth.html)

### [Single sign-on](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sso.html)

Learn about single sign-on when using the AWS SDK for .NET.

- [Tutorial: .NET application only](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sso-tutorial-app-only.html): This tutorial shows you how to enable SSO for a basic application and a test SSO user.
- [Tutorial: AWS CLI and .NET application](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sso-tutorial-cli-and-app.html): This tutorial shows you how to enable SSO for a basic .NET application and a test SSO user.


## [Deploy to AWS](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/deploying.html)

- [ASP.NET Core apps](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/deploying-asp-net.html): This topic shows you how to deploy your ASP.NET Core applications to AWS.
- [.NET Console apps](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/deploying-console.html): This topic shows you how to deploy your .NET Console applications to AWS.
- [Blazor WebAssembly apps](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/deploying-blazor.html): This topic shows you how to deploy your Blazor WebAssembly applications to AWS.
- [AWS Lambda projects](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/deploying-lambda.html): This topic shows you how to deploy your AWS Lambda projects applications to AWS.


## [Calling AWS services](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/working-with-aws-services.html)

### [Guided code examples](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/tutorials-examples.html)

Code examples for the AWS SDK for .NET that show how to use the SDK with AWS services.

### [CloudFormation](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cloudformation-apis-intro.html)

The AWS SDK for .NET supports AWS CloudFormation, which creates and provisions AWS infrastructure deployments predictably and repeatedly.

- [Listing AWS resources](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cfn-list-resources.html): This example shows you how to use the AWS SDK for .NET to list the resources in CloudFormation stacks.

### [Amazon Cognito](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cognito-apis-intro.html)

Use Amazon Cognito to create user identities and authenticate identities.

- [Credentials provider](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cognito-creds-provider.html): Use Amazon Cognito to create user identities and authenticate identities.
- [CognitoAuthentication extension library](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/cognito-authentication-extension.html): Use Amazon Cognito to create user identities and authenticate identities.

### [DynamoDB](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/dynamodb-intro.html)

- [Using expressions](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/dynamodb-expressions.html)
- [JSON support](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/dynamodb-json.html): Information about JSON support in Amazon DynamoDB when using the AWS SDK for .NET.

### [Amazon EC2](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/ec2-apis-intro.html)

The AWS SDK for .NET supports Amazon EC2, which is a web service that provides resizable computing capacity.

### [Security groups](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/security-groups.html)

Use this .NET code example to learn how to create Amazon EC2 security groups.

- [Enumerating security groups](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/enumerate-security-groups.html): This example shows you how to use the AWS SDK for .NET to enumerate security groups.
- [Creating security groups](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creating-security-group.html): This example shows you how to use the AWS SDK for .NET to create a security group.
- [Updating security groups](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/authorize-ingress.html): This example shows you how to use the AWS SDK for .NET to add a rule to a security group.

### [Key pairs](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/key-pairs.html)

Use this .NET code example to learn how to use key pairs in Amazon EC2.

- [Creating key pairs](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/create-save-key-pair.html): This example shows you how to use the AWS SDK for .NET to create a key pair.
- [Deleting key pairs](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/delete-key-pairs.html): This example shows you how to use the AWS SDK for .NET to delete a key pair.
- [Regions and Availability Zones](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/using-regions-and-availability-zones.html): Use this .NET code example to describe Regions and Availability Zones in Amazon EC2.

### [EC2 instances](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/how-to-ec2.html)

You can use the AWS SDK for .NET to control Amazon EC2 instances with operations such as create, start, and terminate.

- [Launching an EC2 instance](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/run-instance.html): Use this .NET code example to learn how to launch an Amazon EC2 instance.
- [Terminating an EC2 instance](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/terminate-instance.html): Use this .NET code example to learn how to terminate an Amazon EC2 instance.
- [Spot Instance tutorial](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/how-to-spot-instances.html): This tutorial shows you how to use the AWS SDK for .NET to manage Amazon EC2 Spot Instances.

### [IAM](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/iam-apis-intro.html)

.NET code examples for AWS Identity and Access Management (IAM)

- [Creating managed policies from JSON](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/iam-policies-create-json.html): Use this .NET code example to work with IAM policies.
- [Displaying policy documents](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/iam-policies-display.html): Use this .NET code example to work with IAM policies.
- [Granting access with a role](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-hosm.html): Use this .NET tutorial to learn how to grant access to an application running on Amazon EC2.

### [Amazon S3](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/s3-apis-intro.html)

The AWS SDK for .NET supports Amazon S3, which is storage for the Internet.

- [Using KMS keys for S3 encryption](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/kms-keys-s3-encryption.html): This example shows you how to use AWS Key Management Service keys to encrypt Amazon S3 objects.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sns-apis-intro.html): .NET code examples for Amazon SNS

### [Amazon SQS](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sqs-apis-intro.html)

.NET code examples for messaging with Amazon SQS

- [Creating queues](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/CreateQueue.html): This example shows you how to use the AWS SDK for .NET to create an Amazon SQS queue.
- [Updating queues](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/UpdateSqsQueue.html): This example shows you how to use the AWS SDK for .NET to update an Amazon SQS queue.
- [Deleting queues](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/DeleteSqsQueue.html): This example shows you how to use the AWS SDK for .NET to delete an Amazon SQS queue.
- [Sending messages](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/SendMessage.html): This example shows you how to use the AWS SDK for .NET to send messages to an Amazon SQS queue, which you can create programmatically or by using the Amazon SQS console.
- [Receiving messages](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/ReceiveMessage.html): This example shows you how to use the AWS SDK for .NET to receive messages from an Amazon SQS queue, which you can create programmatically or by using the Amazon SQS console.

### [AWS Lambda](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/aws-lambda.html)

The AWS SDK for .NET supports AWS Lambda, which lets you run code without provisioning or managing servers.

- [Lambda Annotations](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/aws-lambda-annotations.html): When writing Lambda functions, you sometimes need to write a large amount of handler code and update AWS CloudFormation templates, among other tasks.

### [High-level libraries and frameworks](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/high-level-libraries.html)

The following sections contain information about high-level libraries and frameworks that aren't part of the core SDK functionality.

### [Message Processing Framework](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw.html)

Information about the AWS Message Processing Framework for .NET.

- [Get started](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-get-started.html): Before you begin, be sure you have set up your environment and configured your project.
- [Publish messages](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-publish.html): The AWS Message Processing Framework for .NET supports publishing one or more message types, processing one or more message types, or doing both in the same application.
- [Consume messages](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-consume.html): The AWS Message Processing Framework for .NET allows you to consume messages that have been published by using the framework or one of the messaging services.
- [FIFO](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-fifo.html): For use cases where message ordering and message deduplication are critical, the AWS Message Processing Framework for .NET supports first-in-first-out (FIFO) Amazon SQS queues and Amazon SNS topics.
- [Logging and Open Telemetry](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-telemetry.html): The AWS Message Processing Framework for .NET is instrumented for OpenTelemetry to log traces for each message that is published or handled by the framework.
- [Customize](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-customize.html): The AWS Message Processing Framework for .NET builds, sends, and handles messages in three different "layers":
- [Security](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-security.html): The AWS Message Processing Framework for .NET relies on the AWS SDK for .NET for communicating with AWS.
- [Integrating AWS with .NET Aspire](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/aspire-integrations.html): Information about the integrating AWS with .NET Aspire.
- [Other services and configuration](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/other-apis-intro.html): The AWS SDK for .NET supports AWS services in addition to those described in the preceding sections.


## [Code examples](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_code_examples.html)

- [Aurora](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_aurora_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Auto Scaling.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_bedrock_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon Bedrock Runtime.
- [CloudFormation](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_cloudformation_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with CloudFormation.
- [CloudWatch](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_cloudwatch_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with CloudWatch.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with CloudWatch Logs.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon Cognito Identity Provider.
- [AWS Control Tower](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_controltower_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with AWS Control Tower.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_ec2_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon EC2.
- [Amazon ECS](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_ecs_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon ECS.
- [AWS IoT](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_iot_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with AWS IoT.
- [AWS IoT data](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_iot-data-plane_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with AWS IoT data.
- [Amazon Redshift](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_redshift_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon Redshift.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/csharp_s3_code_examples.html): Code examples that show how to use AWS SDK for .NET (v4) with Amazon S3.


## [Migrating your project](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-migrating.html)

- [Migrating to version 4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html): Migrate to version 4 of the AWS SDK for .NET.
- [Migrating from .NET Standard 1.3](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/migration-from-net-standard-1-3.html): On June 27 2019 Microsoft ended support for .NET Core 1.0 and .NET Core 1.1 versions.


## [Security](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/enforcing-tls.html): Learn how to enforce TLS 1.2 in the AWS SDK for .NET.
- [S3 Encryption Client Migration (V1 to V2)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/s3-encryption-migration-v1-v2.html): Learn how to migrate your S3 encryption clients from V1 to V2.
- [S3 Encryption Client Migration (V2 to V4)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/s3-encryption-migration-v2-v4.html): Learn how to migrate your S3 encryption clients from V2 to V4.


## [Special considerations](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/special-considerations.html)

- [Obtaining AWSSDK assemblies](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-obtain-assemblies.html): Obtain AWSSDK assemblies for the AWS SDK for .NET.
- [Accessing credentials and profiles in an application](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/creds-locate.html): The preferred method for using credentials is to allow the AWS SDK for .NET to find and retrieve them for you, as described in .
- [Unity support](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/unity-special.html): When using the AWS SDK for .NET and .NET Standard 2.0 for your Unity application, your application must reference the AWS SDK for .NET assemblies (DLL files) directly rather than using NuGet.
- [Xamarin support](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/xamarin-special.html): Xamarin projects (new and existing) must target .NET Standard 2.0.
