# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/llms.txt

# AWS SDK for Go v2 Developer Guide

> Developer guide for the AWS SDK for Go (version 2). Introduces the SDK and provides code examples that demonstrate how to use it.

- [What is the AWS SDK for Go v2?](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/welcome.html)
- [Get started](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/getting-started.html)
- [Middleware](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/middleware.html)
- [Unit Tests](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/unit-testing.html)
- [Migrate to v2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/migrate-gosdk.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/doc-history.html)

## [Configure the SDK](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-gosdk.html)

- [Authentication](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-auth.html): The AWS SDK for Go provides the ability to configure the authentication behavior service.
- [Client Endpoints](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-endpoints.html)
- [HTTP Client](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-http.html): The AWS SDK for Go uses a default HTTP client with default configuration values.
- [Interceptors](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/interceptors.html): Use HTTP interceptors to customize AWS SDK for Go v2 request and response processing with simple, HTTP-focused hooks
- [Logging](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-logging.html): The AWS SDK for Go has logging facilities available that allow your application to enable debugging information for debugging and diagnosing request issues or failures.
- [Retries and Timeouts](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-retries-timeouts.html): The AWS SDK for Go enables you to configure the retry behavior of requests to HTTP services.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/using.html)

- [Handling Errors in the SDK](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/handle-errors.html): The AWS SDK for Go returns errors that satisfy the Go error interface type.


## [Use AWS services](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/use-services.html)

- [Amazon S3 checksums](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/s3-checksums.html): Learn how to use checksums with Amazon S3 in AWS SDK for Go to ensure data integrity during object uploads and downloads.


## [SDK Utilities](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities.html)

- [Amazon RDS Utilities](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-rds.html)
- [Amazon CloudFront Utilities](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-cloudfront.html)
- [Amazon EC2 Instance Metadata Service](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-ec2-imds.html): You can use the AWS SDK for Go to access the Amazon EC2 Instance Metadata Service.
- [Amazon S3 Utilities](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-s3.html)


## [Frequently Asked Questions](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/faq-gosdk.html)

- [Timing SDK operations](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-timing.html): When debugging timeout/latency issues in the SDK, it is critical to identify the components of the operation lifecycle which are taking more time to execute than expected.


## [Code examples](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_code_examples.html)

- [API Gateway](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with API Gateway.
- [Aurora](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_aurora_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Aurora.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_bedrock_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon Bedrock Runtime.
- [CloudFormation](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_cloudformation_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with CloudFormation.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with CloudWatch Logs.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon Cognito Identity Provider.
- [Amazon DocumentDB](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_docdb_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with DynamoDB.
- [IAM](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_iam_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with IAM.
- [Kinesis](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_kinesis_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Kinesis.
- [Lambda](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_lambda_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Lambda.
- [Amazon MSK](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_kafka_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon MSK.
- [Partner Central](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_partnercentral-selling_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Partner Central.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_rds_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon RDS.
- [Amazon Redshift](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_redshift_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon Redshift.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_s3_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon S3.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_sns_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_sqs_code_examples.html): Code examples that show how to use AWS SDK for Go V2 with Amazon SQS.


## [Security](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS SDK for Go.
- [Compliance validation](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS SDK for Go features for data resiliency.
