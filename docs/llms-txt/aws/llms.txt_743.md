# Source: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/llms.txt

# AWS SDK for Kotlin Developer Guide

- [What is the AWS SDK for Kotlin?](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/home.html)
- [Get started](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/get-started.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/document-history.html)

## [Set up](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html)

- [Basic set up](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup-basic-onetime-setup.html): Learn about the prerequisite steps that you need to take to work with the AWS SDK for Kotlin.
- [Create project build files](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup-create-project-file.html): Learn how to create a Gradle or Maven project file to use with the SDK for Kotlin.
- [Code your project](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/code-project.html): Use reference resources to help you code your application that uses the SDK for Kotlin.


## [Configure](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/configuration.html)

- [Create a service client](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/creating-clients.html): Learn about several ways to configure an AWS SDK for Kotlin service client.
- [AWS Region selection](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/region-selection.html): Learn how the AWS Region is configured.
- [Credentials providers](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/credential-providers.html): Learn how to configure and use credentials providers in the AWS SDK for Kotlin to authenticate requests to Amazon Web Services securely and efficiently.
- [Client endpoints](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/config-endpoint.html): Learn how to configure client endpoints in the AWS SDK for Kotlin.

### [HTTP](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/http.html)

Learn how to configure HTTP clients using AWS SDK for Kotlin.

- [HTTP client configuration](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/http-client-config.html): Learn how to configure an HTTP client in the AWS SDK for Kotlin.
- [Use an HTTP proxy](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/using-http-proxy.html): Learn how to configure HTTP proxy settings for the AWS SDK for Kotlin.
- [Interceptors](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/interceptors.html): Learn how to use HTTP interceptors with the AWS SDK for Kotlin.
- [Enforce a minimum TLS version](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/configure-http-tls.html): Learn how to enforce a minimum TLS version when connecting to AWS services using the AWS SDK for Kotlin.
- [Retries](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/retries.html): Learn how to configure automatic retries with the AWS SDK for Kotlin.

### [Observability](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability.html)

Learn how to enable and configure telemetry output in the AWS SDK for Kotlin to increase the observability of your application.

- [Metrics](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability-telemetry-metrics.html): Learn about the metrics that the AWS SDK for Kotlin emits.
- [Logging](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/logging.html): Learn how to enable and configure logging for the AWS SDK for Kotlin.

### [Telemetry providers](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability-telemetry-providers.html)

Learn about the telemetry providers that you can use with the SDK for Kotlin.

- [OpenTelemetry](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability-telemetry-providers-otel.html): Learn how to configure the OpenTelemetry-based telemetry provider in the AWS SDK for Kotlin.
- [Override client configuration](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/override-client-config.html): Learn how to override the configuration of a service client for one or more operations in the AWS SDK for Kotlin.


## [Use the SDK](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/using.html)

- [Make requests](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/making-requests.html): Learn how to use service clients to make request with AWS SDK for Kotlin.
- [Coroutines](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/coroutines.html): Learn how the AWS SDK for Kotlin uses coroutines.
- [Streaming operations](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/streaming-ops.html): Learn how to work with streaming operations in the AWS SDK for Kotlin.
- [Pagination](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/pagination.html): Learn how pagination is implemented in the AWS SDK for Kotlin.
- [Waiters](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/waiters.html): Learn about what waiters are in the AWS SDK for Kotlin and what advantages waiters provide.
- [Error handling](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/error-handling.html): Understand exceptions and how to work with errors in the AWS SDK for Kotlin.
- [Presign requests](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/presign-requests.html): Learn how to presign requests with the AWS SDK for Kotlin.

### [Troubleshooting FAQs](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/troubleshooting-faqs.html)

Use the FAQs in this topic to help you solve issues that come up when you use the AWS SDK for Kotlin.

- [How do I resolve dependency conflicts?](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ts-faq-dep-conflict-resolution.html): Learn how to resolve dependency conflicts when using the AWS SDK for Kotlin, including managing SDK/Smithy dependencies and addressing OkHttp version conflicts in your Gradle-based projects.
- [Mocking](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/mocking.html): Learn how to configure mocking frameworks when testing with the AWS SDK for Kotlin, particularly for extension functions like paginators, waiters, and presigners when you use the MockK testing framework.


## [Work with AWS services](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services.html)

### [Amazon S3](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-s3.html)

Learn how to work with Amazon S3 by using the AWS SDK for Kotlin.

- [Data integrity protection with checksums](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/s3-checksums.html): Learn how to use checksums with Amazon S3 in AWS SDK for Kotlin to ensure data integrity during object uploads and downloads.
- [Work with Multi-Region Access Points](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-s3-mrap.html): Learn how to work with Amazon S3 Multi-Region Access Points by using the AWS SDK for Kotlin.

### [DynamoDB](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-ddb.html)

Learn how to work with DynamoDB by using the AWS SDK for Kotlin.

### [Use DynamoDB Mapper (Developer Preview)](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper.html)

Learn how to use DynamoDB Mapper to map Kotlin classes to DynamoDB tables and perform CRUD operations with ease in your AWS applications.

- [Get started](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-get-started.html): Learn how to use DynamoDB Mapper in the SDK for Kotlin to interact with Amazon DynamoDB in an object-oriented way.
- [Configure DynamoDB Mapper](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-configuration.html): Learn how to customize DynamoDB Mapper behavior using interceptors, including understanding the request pipeline, hooks, and execution order for enhanced control over data operations.
- [Generate a schema](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-anno-schema-gen.html): Learn how to use the DynamoDB Mapper schema generator Gradle plugin to create schemas for Kotlin classes, configure the plugin, and annotate classes.
- [Manually define schemas](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-code-schemas.html): Learn how to manually define and customize schemas for DynamoDB tables in code using the AWS SDK for Kotlin, including creating item converters and key specifications.
- [Use secondary indices](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-secondary-indices.html): Learn how to define schemas for secondary indexes to query and scan DynamoDB tables using the AWS SDK for Kotlin.
- [Use expressions](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-expressions.html): Learn how to use the DynamoDB Mapper Kotlin DSL to create expressions for filtering and querying data in Amazon DynamoDB operations with greater structure and readability.


## [Code examples](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_code_examples.html)

- [API Gateway](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with API Gateway.
- [Aurora](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_aurora_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Auto Scaling.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_bedrock_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Bedrock Runtime.
- [CloudWatch](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_cloudwatch_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with CloudWatch.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with CloudWatch Logs.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Cognito Identity Provider.
- [Amazon Comprehend](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_comprehend_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Comprehend.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_ec2_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon EC2.
- [Amazon ECR](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_ecr_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon ECR.
- [OpenSearch Service](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_opensearch_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with OpenSearch Service.
- [EventBridge](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_eventbridge_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with EventBridge.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_glue_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with AWS Glue.
- [IAM](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_iam_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with IAM.
- [AWS IoT](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_iot_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with AWS IoT.
- [AWS IoT data](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_iot-data-plane_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with AWS IoT data.
- [AWS IoT FleetWise](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_iotfleetwise_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with AWS IoT FleetWise.
- [Amazon Keyspaces](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_keyspaces_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Keyspaces.
- [AWS KMS](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_kms_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with AWS KMS.
- [Lambda](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_lambda_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Lambda.
- [Amazon Location](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_location_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Location.
- [MediaConvert](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_mediaconvert_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with MediaConvert.
- [Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_pinpoint_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Pinpoint.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_rds_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_rds-data_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon RDS Data Service.
- [Amazon Redshift](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_redshift_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Redshift.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_rekognition_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Rekognition.
- [RouteÂ 53 domain registration](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_route-53-domains_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with RouteÂ 53 domain registration.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_s3_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon S3.
- [SageMaker AI](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_sagemaker_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with SageMaker AI.
- [Secrets Manager](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_secrets-manager_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Secrets Manager.
- [Amazon SES](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_ses_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon SES.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_sns_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_sqs_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon SQS.
- [Step Functions](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_sfn_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Step Functions.
- [Support](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_support_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Support.
- [Amazon Translate](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_translate_code_examples.html): Code examples that show how to use AWS SDK for Kotlin with Amazon Translate.


## [Security](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/security-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in SDK for Kotlin.
- [Enforcing TLS 1.2](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/security-kotlin-tls.html): Lean how to set the TLS version when your application targets the JVM
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
