# Source: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/llms.txt

# AWS SDK for Rust Developer Guide

> Developer Guide for AWS SDK for Rust

- [What is the AWS SDK for Rust?](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/welcome.html)
- [Crates used by the SDK](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/appendix-crates.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/document-history.html)

## [Getting started](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/getting-started.html)

- [Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/credentials.html): Learn how to authenticate your code with AWS in the SDK for Rust.
- [Creating a simple application](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/hello.html): Tutorial to create your first project using SDK for Rust.
- [Fundamentals](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/fundamentals.html): Learn Rust basics necessary for learning the AWS SDK for Rust.


## [Configuring service clients](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/configure.html)

- [Client configuration externally](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/config-external.html): Learn various methods of setting configuration outside of code using the shared AWS config file and environment variables.
- [Client configuration in code](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/config-code.html): Learn how to create and use service clients in the SDK for Rust.
- [AWS Region](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/region.html): Information about setting region with the AWS SDK for Rust.
- [Credential providers](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/credproviders.html): Learn how to configure credential providers in the SDK for Rust.
- [Behavior versions](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/behavior-versions.html): Learn how to set behavior versions.
- [Retries](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/retries.html): How to specify retries in the SDK for Rust.
- [Timeouts](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/timeouts.html): This section describes some of the available timeout configuration and related options for the SDK for Rust, and how to configure them.

### [Observability](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/observability.html)

Learn how to enable observability features in the SDK for Rust.

- [Logging](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/logging.html): Learn what observability logging options are supported when using the AWS SDK for Rust.
- [Client endpoints](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/endpoints.html): Learn how to configure endpoint resolution for the AWS SDK for Rust.
- [Overriding an operation configuration](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/peroperation.html): Learn how to override certain configuration options on a per-operation basis after the client is constructed.
- [HTTP](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/http.html): How to configure HTTP in the SDK for Rust.
- [Interceptors](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/interceptors.html): Interceptors are mechanisms where you can inject behavior into the request/response lifecycle.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/using.html)

- [Making service requests](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/make-request.html): How to make requests to AWS services using the AWS SDK for Rust.
- [Best practices](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/best-practices.html): Learn best practices for applications using the SDK for Rust.
- [Concurrency](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/concurrency.html): How to work with synchronous and asynchronous tasks.
- [Creating Lambda functions](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/lambda.html): Information on how to use the AWS SDK for Rust in Lambda function.
- [Creating presigned URLs](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/presigned-urls.html): Learn techniques to create presigned URLs with the AWS SDK for Rust
- [Handling errors](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/error-handling.html): Learn how to handle errors in the SDK for Rust.
- [Pagination](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/paginating.html): How to implement pagination to process lengthy data results in chunks.

### [Unit testing](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing.html)

Describes a couple of approaches to unit testing code written with the SDK for Rust.

- [Unit testing using mockall](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing-automock.html): Learn how to use mockall to generate mocks for unit testing code developed with SDK for Rust.
- [Static replay](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing-replay.html): Learn how to use static replay to test code written with the SDK for Rust.
- [Unit testing using aws-smithy-mocks](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing-smithy-mocks.html): Learn how to use aws-smithy-mocks to unit test code written with the SDK for Rust.
- [Waiters](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/waiters.html): How to poll a resource until a desired state is reached, or until it is determined that the resource will not enter the desired state.


## [Code examples](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_code_examples.html)

- [API Gateway](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for Rust with API Gateway.
- [API Gateway Management API](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_apigatewaymanagementapi_code_examples.html): Code examples that show how to use AWS SDK for Rust with API Gateway Management API.
- [Application Auto Scaling](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_application-auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for Rust with Application Auto Scaling.
- [Aurora](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_aurora_code_examples.html): Code examples that show how to use AWS SDK for Rust with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for Rust with Auto Scaling.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Bedrock Runtime.
- [Amazon Bedrock Agents Runtime](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_bedrock-agent-runtime_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Bedrock Agents Runtime.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Cognito Identity Provider.
- [Amazon Cognito Sync](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_cognito-sync_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Cognito Sync.
- [Firehose](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_firehose_code_examples.html): Code examples that show how to use AWS SDK for Rust with Firehose.
- [Amazon DocumentDB](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_docdb_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for Rust with DynamoDB.
- [Amazon EBS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ebs_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon EBS.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ec2_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon EC2.
- [Amazon ECR](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ecr_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon ECR.
- [Amazon ECS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ecs_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon ECS.
- [Amazon EKS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_eks_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon EKS.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_glue_code_examples.html): Code examples that show how to use AWS SDK for Rust with AWS Glue.
- [IAM](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_iam_code_examples.html): Code examples that show how to use AWS SDK for Rust with IAM.
- [AWS IoT](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_iot_code_examples.html): Code examples that show how to use AWS SDK for Rust with AWS IoT.
- [Kinesis](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_kinesis_code_examples.html): Code examples that show how to use AWS SDK for Rust with Kinesis.
- [AWS KMS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_kms_code_examples.html): Code examples that show how to use AWS SDK for Rust with AWS KMS.
- [Lambda](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_lambda_code_examples.html): Code examples that show how to use AWS SDK for Rust with Lambda.
- [MediaLive](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_medialive_code_examples.html): Code examples that show how to use AWS SDK for Rust with MediaLive.
- [MediaPackage](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_mediapackage_code_examples.html): Code examples that show how to use AWS SDK for Rust with MediaPackage.
- [Amazon MSK](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_kafka_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon MSK.
- [Amazon Polly](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_polly_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Polly.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_rds_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_rds-data_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon RDS Data Service.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_rekognition_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Rekognition.
- [RouteÂ 53](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_route-53_code_examples.html): Code examples that show how to use AWS SDK for Rust with RouteÂ 53.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_s3_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon S3.
- [SageMaker AI](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sagemaker_code_examples.html): Code examples that show how to use AWS SDK for Rust with SageMaker AI.
- [Secrets Manager](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_secrets-manager_code_examples.html): Code examples that show how to use AWS SDK for Rust with Secrets Manager.
- [Amazon SES API v2](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sesv2_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon SES API v2.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sns_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sqs_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon SQS.
- [AWS STS](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sts_code_examples.html): Code examples that show how to use AWS SDK for Rust with AWS STS.
- [Systems Manager](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ssm_code_examples.html): Code examples that show how to use AWS SDK for Rust with Systems Manager.
- [Amazon Transcribe](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_transcribe_code_examples.html): Code examples that show how to use AWS SDK for Rust with Amazon Transcribe.


## [Security](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforce a minimum TLS version](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/enforcing-tls.html): Learn how to enforce a minimum version of TLS in the AWS SDK for Rust.
