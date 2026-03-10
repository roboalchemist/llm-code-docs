# Source: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/llms.txt

# AWS SDK for C++ Developer Guide

> AWS SDK for C++ Developer Guide :keywords: AWS SDK for C++ code examples

- [What is the AWS SDK for C++ Developer Guide?](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/welcome.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/document-history.html)

## [Getting started](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/getting-started.html)

- [Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/credentials.html): Learn different ways to supply AWS credentials and authenticate with AWS services when using the AWS SDK for C++.

### [Getting the SDK from source](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-source.html)

SDK for C++ prerequisites and requirements to set up the SDK from the public source code.

- [Building on Windows](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/setup-windows.html): Prerequisites, requirements, and instructions to set up the AWS SDK for C++ for Windows by building and installing the source.
- [Building on Linux/macOS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/setup-linux.html): Prerequisites, requirements, and instructions to set up the AWS SDK for C++ for Linux/macOS by building and installing the source.
- [Creating a simple application](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/build-cmake.html): Building a sample S3 application using AWS SDK for C++ obtained from manually building the SDK source.
- [Getting the SDK from a package manager](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-pm.html): Use the vcpkg package manager to obtain the AWS SDK for C++ executables to utilize the SDK in your code.
- [Troubleshooting build issues](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/troubleshooting-cmake.html): Troubleshooting tips for building your AWS SDK for C++ application with CMake.


## [Configuring service clients](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/configuring.html)

- [SDK configuration](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdkoptions.html): Learn how to set SDK configuration and debug logging options.
- [Client configuration externally](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/config-external.html): Learn how to set environment variables or use shared configuration in the SDK for C++ to configure service client functionality in all applications.
- [Client configuration in code](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html): Use the client configuration to control various behaviors of the AWS SDK for C++ when making calls to AWS services.
- [AWS Region](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/region.html): Learn how to set AWS Region in the SDK for C++.
- [Credential providers](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/credproviders.html): Information about using credential providers with the SDK for C++.
- [CMake parameters](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cmake-params.html): Learn how to customize building the AWS SDK for C++ with CMake parameters.
- [Logging](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/logging.html): How to use AWS SDK for C++ logging to help debug your application.
- [HTTP](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/overriding-http-client.html): Creating a custom HttpClientFactory for the AWS SDK for C++.
- [Controlling iostreams used by the HttpClient and the AWSClient](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/configuring-iostreams.html): Learn how to override the default iostream behavior in AWS SDK for C++.
- [Using a custom libcrypto](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/libcrypto.html): How to use a custom libcrypto library for cryptographic functionality.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/programming-general.html)

- [Initializing and shutting down the SDK](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/basic-use.html): Learn how to initialize and shutdown the AWS SDK for C++.
- [Making AWS service requests](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/using-service-client.html): Using AWS SDK for C++ service client classes to invoke AWS services.
- [Asynchronous programming](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/async-methods.html): How to use the asynchronous methods in the AWS SDK for C++.
- [Utility modules](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/utility-modules.html): There are many C++ utility modules in the AWS SDK for C++ including string utils, hashing utils, a JSON parser, and an XML parser.
- [Memory management](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/memory-management.html): Providing a custom memory allocator and deallocator for the AWS SDK for C++.
- [Handling errors](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/error-handling.html): Using the outcome object to manage AWS SDK for C++ errors.


## [Calling AWS services](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/working-with-aws-services.html)

- [Getting started on code examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/getting-started-code-examples.html): Getting started with code examples using the AWS SDK for C++.
- [Getting started troubleshooting runtime errors](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/troubleshooting-runtime-errors.html): Getting started with using AWS tools to help troubleshoot runtime errors in the AWS SDK for C++.

### [Guided examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/programming-services.html)

Examples of how to access AWS services using the AWS SDK for C++.

### [Amazon CloudWatch examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch.html)

Programming Amazon CloudWatch using the AWS SDK for C++

- [Getting Metrics from CloudWatch](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-get-metrics.html): How to list metrics from Amazon CloudWatch using the AWS SDK for C++.
- [Publishing Custom Metric Data](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-publish-custom-metrics.html): How to publish custom metric data to Amazon CloudWatch using the AWS SDK for C++.
- [Working with CloudWatch Alarms](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-create-alarms.html): How to manage alarms in Amazon CloudWatch using the AWS SDK for C++.
- [Using Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-use-alarm-actions.html): How to enable or disable Amazon CloudWatch alarm actions using the AWS SDK for C++.
- [Sending Events to CloudWatch](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-cloudwatch-send-events.html): How to add custom events, add rules, and add targets to rules for Amazon CloudWatch using the AWS SDK for C++.

### [Amazon DynamoDB examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-dynamodb.html)

AWS SDK for C++ code examples for Amazon DynamoDB.

- [Working with Tables in DynamoDB](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-dynamodb-tables.html): How to create, describe, modify (update) and delete Amazon DynamoDB tables.
- [Working with Items in DynamoDB](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-dynamodb-items.html): How to retrieve (get), add, and update items in Amazon DynamoDB tables.

### [Amazon EC2 examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2.html)

AWS SDK for C++ code examples for Amazon Elastic Compute Cloud.

- [Managing Amazon EC2 Instances](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-instances.html): How to manage EC2 instances using the AWS SDK for C++.
- [Using Elastic IP Addresses in Amazon EC2](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-elastic-ip.html): How to manage elastic IP addresses for EC2 instances with the AWS SDK for C++.
- [Using Regions and Availability Zones for Amazon EC2](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-regions-zones.html): How to list EC2 regions and availability zones using the AWS SDK for C++.
- [Working with Amazon EC2 Key Pairs](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-key-pairs.html): How to create, list and delete EC2 key pairs using the AWS SDK for C++.
- [Working with Security Groups in Amazon EC2](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-security-groups.html): How to create, configure and delete EC2 security groups with the AWS SDK for C++.

### [Amazon S3 examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3.html)

How to manage Amazon S3 buckets.

- [Creating, listing, and deleting buckets](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-buckets.html): Managing Amazon S3 buckets using the AWS SDK for C++.
- [Operations on objects](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-objects.html): Managing Amazon S3 object using the AWS SDK for C++.
- [Managing Amazon S3 Access Permissions](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-access-permissions.html): How to manage access control lists for an Amazon S3 bucket or object.
- [Managing Access to Amazon S3 Buckets Using Bucket Policies](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-bucket-policies.html): How to manage policies for an Amazon S3 bucket using the AWS SDK for C++.
- [Configuring an Amazon S3 Bucket as a Website](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-website-configuration.html): How to manage an S3 bucket's website configuration using the AWS SDK for C++.
- [Using TransferManager for Amazon S3 operations](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-transfermanager.html): Managing Amazon S3 objects using the AWS SDK for C++ and the TransferManager .
- [Using S3CrtClient for Amazon S3 operations](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-s3-crt.html): Managing Amazon S3 objects using the AWS SDK for C++ and the S3CrtClient .

### [Amazon SQS examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs.html)

AWS SDK for C++ code examples for Amazon Simple Queue Service.

- [Working with Amazon SQS Message Queues](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-message-queues.html): How to manage an Amazon SQS queue's URL with the AWS SDK for C++.
- [Sending, Receiving, and Deleting Amazon SQS Messages](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-messages.html): How to manage Amazon SQS messages with the AWS SDK for C++.
- [Enabling Long Polling for Amazon SQS Message Queues](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-long-polling.html): How to enable long polling for Amazon SQS message queues using the AWS SDK for C++.
- [Setting Visibility Timeout in Amazon SQS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-visibility-timeout.html): How to set visibility timeout for Amazon SQS queues with the AWS SDK for C++.
- [Using Dead Letter Queues in Amazon SQS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-sqs-dead-letter-queues.html): How to manage Amazon SQS dead letter queues.


## [Code examples](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_code_examples.html)

- [ACM](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_acm_code_examples.html): Code examples that show how to use AWS SDK for C++ with ACM.
- [API Gateway](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for C++ with API Gateway.
- [Aurora](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_aurora_code_examples.html): Code examples that show how to use AWS SDK for C++ with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for C++ with Auto Scaling.
- [CloudTrail](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_cloudtrail_code_examples.html): Code examples that show how to use AWS SDK for C++ with CloudTrail.
- [CloudWatch](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_cloudwatch_code_examples.html): Code examples that show how to use AWS SDK for C++ with CloudWatch.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for C++ with CloudWatch Logs.
- [CodeBuild](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_codebuild_code_examples.html): Code examples that show how to use AWS SDK for C++ with CodeBuild.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon Cognito Identity Provider.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for C++ with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_ec2_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon EC2.
- [EventBridge](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_eventbridge_code_examples.html): Code examples that show how to use AWS SDK for C++ with EventBridge.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_glue_code_examples.html): Code examples that show how to use AWS SDK for C++ with AWS Glue.
- [HealthImaging](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_medical-imaging_code_examples.html): Code examples that show how to use AWS SDK for C++ with HealthImaging.
- [IAM](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_iam_code_examples.html): Code examples that show how to use AWS SDK for C++ with IAM.
- [AWS IoT](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_iot_code_examples.html): Code examples that show how to use AWS SDK for C++ with AWS IoT.
- [AWS IoT data](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_iot-data-plane_code_examples.html): Code examples that show how to use AWS SDK for C++ with AWS IoT data.
- [Lambda](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_lambda_code_examples.html): Code examples that show how to use AWS SDK for C++ with Lambda.
- [MediaConvert](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_mediaconvert_code_examples.html): Code examples that show how to use AWS SDK for C++ with MediaConvert.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_rds_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_rds-data_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon RDS Data Service.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_rekognition_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon Rekognition.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_s3_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon S3.
- [Secrets Manager](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_secrets-manager_code_examples.html): Code examples that show how to use AWS SDK for C++ with Secrets Manager.
- [Amazon SES](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_ses_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon SES.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_sns_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_sqs_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon SQS.
- [AWS STS](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_sts_code_examples.html): Code examples that show how to use AWS SDK for C++ with AWS STS.
- [Amazon Transcribe Streaming](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/cpp_transcribe-streaming_code_examples.html): Code examples that show how to use AWS SDK for C++ with Amazon Transcribe Streaming.


## [Security](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/security.html)

- [Data Protection](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/enforcing-tls.html): Learn how to enforce TLS in this AWS product or service.
- [Amazon S3 Encryption Client Migration (V1 to V2)](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/s3-encryption-migration-v1-v2.html): Describes how to migrate to the latest Amazon S3 encryption clients for SDK for C++.
- [Amazon S3 Encryption Client Migration (V2 to V3)](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/s3-encryption-migration-v2-v3.html): Describes how to migrate from Version 2 (V2) to Version 3 (V3) of the Amazon S3 encryption client for SDK for C++.
