# Source: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/llms.txt

# AWS SDK for Go (version 1) Developer Guide

> Developer guide for the AWS SDK for Go (version 1). Introduces the SDK and provides code examples that demonstrate how to use it.

- [What is the AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/welcome.html)
- [Getting Started](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/setting-up.html)
- [Using Sessions](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sessions.html)
- [Using AWS Services](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/making-requests.html)
- [Handling Errors](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/handling-errors.html)
- [SDK Utilities](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sdk-utilities.html)
- [Document History](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/document-history.html)

## [Configuring the SDK](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html)

- [Custom HTTP Client](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/custom-http.html): Create a custom HTTP client with the AWS SDK for Go to specify custom timeout values.


## [Code Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/common-examples.html)

- [SDK Request Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-requests-with-go-sdk.html): Learn how to work with requests in Go applications using this AWS SDK for Go code example.

### [AWS CloudTrail Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-cloudtrail-with-go-sdk.html)

Use CloudTrail code examples to write your own Go applications.

- [Listing the CloudTrail Trails](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cloudtrail-example-describe-trails.html): List the AWS CloudTrail trails using this AWS SDK for Go code example.
- [Creating a CloudTrail Trail](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cloudtrail-example-create-trail.html): Create an AWS CloudTrail trail using this AWS SDK for Go code example.
- [Listing CloudTrail Trail Events](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cloudtrail-example-lookup-events.html): List the AWS CloudTrail trail events using this AWS SDK for Go code example.
- [Deleting a CloudTrail Trail](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cloudtrail-example-delete-trail.html): Delete an AWS CloudTrail trail using this AWS SDK for Go code example.

### [Amazon CloudWatch Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-cloudwatch-with-go-sdk.html)

Use Amazon CloudWatch code examples to write your Go applications.

- [Describing CloudWatch Alarms](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-describing-alarms.html): Learn to describe alarms in Amazon Cloudwatch using the AWS SDK for Go.
- [Using Alarms and Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-using-alarm-actions.html): Create alarms and alarm actions to change the state of EC2 instances using this AWS SDK for Go code example.
- [Getting Metrics from CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-getting-metrics.html): Retrieve a list of published CloudWatch metrics and publish data points to CloudWatch metrics using this AWS SDK for Go code example.
- [Sending Events to Amazon CloudWatch Events](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-sending-events.html): Work with the CloudWatch Events service using this AWS SDK for Go code example.
- [Getting Log Events from CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-getting-log-events.html): Retrieve the events for a CloudWatch log group's log stream using this AWS SDK for Go code example.

### [AWS CodeBuild Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-cb-with-go-sdk.html)

Use CodeBuild code examples to write your own Go applications.

- [Getting Information about All AWS CodeBuild Projects](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cb-example-list-projects.html): Get information about AWS CodeBuild projects using this AWS SDK for Go code example.
- [Building an AWS CodeBuild Project](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cb-example-build-project.html): Build AWS CodeBuild projects using this AWS SDK for Go code example.
- [Listing Your AWS CodeBuild Project Builds](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cb-example-list-builds.html): List AWS CodeBuild projects using this AWS SDK for Go code example.

### [Amazon DynamoDB Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-dynamodb-with-go-sdk.html)

Use DynamoDB code examples to write your own Go applications.

- [Listing all Amazon DynamoDB Tables](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-list-tables.html): List your DynamoDB tables using this AWS SDK for Go code example.
- [Creating an Amazon DynamoDB Table](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-create-table.html): Create a DynamoDB table using this AWS SDK for Go code example.
- [Creating an Amazon DynamoDB Table Item](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-create-table-item.html): Create a DynamoDB table item using this AWS SDK for Go code example.
- [Creating Amazon DynamoDB Table Items from a JSON File](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-load-table-items-from-json.html): Create DynamoDB table items from a JSON file using this AWS SDK for Go code example.
- [Reading an Amazon DynamoDB Table Item](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-read-table-item.html): Display information about an item in an Amazon DynamoDB tables using this AWS SDK for Go code example.
- [Getting Amazon DynamoDB Table Items Using Expression Builder](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-scan-table-item.html): Get Amazon DynamoDB table items using the new Expresion Builder with this AWS SDK for Go code example.
- [Updating an Amazon DynamoDB Table Item](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-update-table-item.html): Update an Amazon DynamoDB table item using this AWS SDK for Go code example.
- [Deleting an Amazon DynamoDB Table Item](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-delete-table-item.html): Delete an Amazon DynamoDB table item using this AWS SDK for Go code example.

### [Amazon EC2 Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-ec2-with-go-sdk.html)

Use Amazon EC2 code examples to write your own Go applications.

- [Creating Amazon EC2 Instances with Tags or without Block Devices](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-create-images.html): Create Amazon EC2 instances with tags or no block devices using this AWS SDK for Go code example.
- [Managing Amazon EC2 Instances](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-manage-instances.html): Learn to manage Amazon EC2 instances using this AWS SDK for Go code example.
- [Working with Amazon EC2 Key Pairs](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-working-with-key-pairs.html): Manage Amazon EC2 key pairs using this AWS SDK for Go code example.
- [Using Regions and Availability Zones with Amazon EC2](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-regions-availability-zones.html): Work with regions and Availability Zones using this AWS SDK for Go code example.
- [Working with Security Groups in Amazon EC2](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-security-groups.html): Work with security groups in |EC2| using this AWS SDK for Go code example.
- [Using Elastic IP Addresses in Amazon EC2](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ec2-example-elastic-ip-addresses.html): Allocate Elastic IP addresses in Amazon EC2 using this AWS SDK for Go code example.
- [Amazon Glacier Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-glacier-with-go-sdk.html): Use Amazon Glacier code examples to write your own Go applications.

### [IAM Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-iam-with-go-sdk.html)

Use IAM code examples to write your own Go applications.

- [Managing IAM Users](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/iam-example-managing-users.html): Learn to manage IAM users with this AWS SDK for Go code example.
- [Managing IAM Access Keys](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/iam-example-managing-access-keys.html): Manage IAM access keys using this AWS SDK for Go code example.
- [Managing IAM Account Aliases](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/iam-example-account-aliases.html): Learn to manage IAM account aliases using this AWS SDK for Go code example.
- [Working with IAM Policies](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/iam-example-policies.html): Learn to manage IAM policies using this AWS SDK for Go code example.
- [Working with IAM Server Certificates](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/iam-example-server-certificates.html): Learn to manage IAM server certificates using this AWS SDK for Go code example.

### [AWS KMS Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-kms-with-go-sdk.html)

- [Creating a CMK in AWS Key Management Service](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/kms-example-create-key.html): Create a CMK data in AWS KMS using this AWS SDK for Go code example.
- [Encrypting Data with AWS Key Management Service](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/kms-example-encrypt-data.html): Encrypt data in AWS KMS using this AWS SDK for Go code example.
- [Decrypting a Data Blob in AWS Key Management Service](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/kms-example-decrypt-blob.html): Decrypt a data blob in AWS KMS using this AWS SDK for Go code example.
- [Re-encrypting a Data Blob in AWS Key Management Service](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/kms-example-re-encrypt-data.html): Re-encrypt data in AWS KMS using this AWS SDK for Go code example.

### [AWS Lambda Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-lambda-with-go-sdk.html)

AWS SDK for Go code examples for AWS Lambda.

- [Displaying Information about All Lambda Functions](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-show-functions.html): Display information about AWS Lambda functions using this AWS SDK for Go code example.
- [Creating a Lambda Function](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-create-function.html): Create AWS Lambda functions using this AWS SDK for Go code example.
- [Running a Lambda Function](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-run-function.html): Run AWS Lambda functions using this AWS SDK for Go code example.
- [Configuring a Lambda Function to Receive Notifications](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-configure-function-for-notification.html): Configure AWS Lambda functions using this AWS SDK for Go code example.

### [Amazon Polly Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-polly-with-go-sdk.html)

Use Amazon Polly code examples to write your own Go applications.

- [Getting a List of Voices](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/polly-example-describe-voices.html): Get the list of voices that are available for use when requesting speech synthesis using this AWS SDK for Go code example.
- [Getting a List of Lexicons](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/polly-example-list-lexicons.html): Get the list of pronunciation lexicons stored in an AWS Region using this AWS SDK for Go code example.
- [Synthesizing Speech](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/polly-example-synthesize-speech.html): Synthesizing speech using this AWS SDK for Go code example.

### [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-s3-with-go-sdk.html)

Use S3 code examples to write your own Go applications.

- [Performing Basic Amazon S3 Bucket Operations](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-basic-bucket-operations.html): Create and use Amazon S3 buckets using this AWS SDK for Go code example.
- [Creating Pre-Signed URLs for Amazon S3 Buckets](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-presigned-urls.html): Create presigned URLS to Amazon S3 buckets using this AWS SDK for Go code example.
- [Using an Amazon S3 Bucket as a Static Web Host](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-static-web-host.html): Set up an Amazon S3 bucket as a static web host using this AWS SDK for Go code example.
- [Working with Amazon S3 CORS Permissions](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-cors.html): Learn to work with cross-origin resource sharing (CORS) for an Amazon S3 bucket using this AWS SDK for Go code example.
- [Working with Amazon S3 Bucket Policies](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-bucket-policy.html): Work with Amazon S3 bucket policies using this AWS SDK for Go code example.
- [Working with Amazon S3 Bucket ACLs](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-bucket-acls.html): Manage Amazon S3 bucket ACLs in using this AWS SDK for Go code example.

### [Encrypting Amazon S3 Bucket Items](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-examples-encryption.html)

Encrypt Amazon S3 bucket items using these AWS SDK for Go code examples.

- [Setting Default Server-Side Encryption for an Amazon S3 Bucket](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-default-server-side-encryption.html): Encrypt Amazon S3 bucket objects by default using this AWS SDK for Go code example.
- [Requiring Encryption on the Server to Upload Amazon S3 Bucket Objects](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-enforce-server-side-encryption.html): Require server-side encryption to upload Amazon S3 bucket using this AWS SDK for Go code example.
- [Encrypting an Amazon S3 Bucket Object on the Server Using AWS KMS](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-example-server-side-encryption-with-kms.html): Encrypt Amazon S3 bucket objects on the server with AWS KMS using this AWS SDK for Go code example.

### [Amazon SES Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-ses-with-go-sdk.html)

Use Amazon SES code examples to write your Go applications.

- [Listing Valid Amazon SES Email Addresses](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ses-example-list-emails.html): Learn to list the Amazon SES email addresses through this AWS SDK for Go code example.
- [Verifying an Email Address in Amazon SES](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ses-example-send-verification.html): Learn how to verify an email address in Amazon SES through this AWS SDK for Go code example.
- [Sending a Message to an Email Address in Amazon SES](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ses-example-send-email.html): Learn how to send a message to an email address in Amazon SES through this AWS SDK for Go code example.
- [Deleting an Email Address in Amazon SES](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ses-example-delete-address.html): Learn how to delete an email address in Amazon SES through this AWS SDK for Go code example.
- [Getting Amazon SES Statistics](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/ses-example-get-statistics.html): Learn how to get statistics about Amazon SES through this AWS SDK for Go code example.

### [Amazon SNS Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-sns-with-go-sdk.html)

AWS SDK for Go code examples for Amazon SNS.

- [Listing Your Amazon SNS Topics](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-list-topics.html): List the ARNs of your Amazon SNS topics using this AWS SDK for Go code example.
- [Creating an Amazon SNS Topic](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-create-topic.html): Create an Amazon SNS topic using this AWS SDK for Go code example.
- [List Your Amazon SNS Subscriptions](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-list-subscriptions.html): List the ARNs for your Amazon SNS topic subscriptions and the topic using this AWS SDK for Go code example.
- [Subscribe to an Amazon SNS Topic](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-subscribe.html): Create a subscription in an Amazon SNS topic using the AWS SDK for Go.
- [Sending a Message to All Amazon SNS Topic Subscribers](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-publish.html): Send messages to all Amazon SNS topic subscribers using this AWS SDK for Go code example.

### [Amazon SQS Examples](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-sqs-with-go-sdk.html)

Use Amazon SQS code examples to write your own Go applications.

- [Using Amazon SQS Queues](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-create-queue.html): Learn to work with Amazon SQS queues using this AWS SDK for Go.
- [Sending and Receiving Messages in Amazon SQS](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-receive-message.html): Send or receive a message from an Amazon SQS queue using this AWS SDK for Go code example.
- [Managing Visibility Timeout in Amazon SQS Queues](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-managing-visibility-timeout.html): Manage visibility timeout with Amazon SQS queues using this AWS SDK for Go code exammple.
- [Enabling Long Polling in Amazon SQS Queues](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-enable-long-polling.html): Enable long polling with Amazon SQS queues using this AWS SDK code example.
- [Using Dead Letter Queues in Amazon SQS](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sqs-example-dead-letter-queues.html): Use an Amazon SQS queue to receive and hold messages with this AWS SDK for Go code example.


## [Security](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/security.html)

- [Data Protection](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in the AWS SDK for Go.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/tls.html): Describes how to set the TLS version for the AWS SDK for Go.
- [S3 Encryption Client Migration](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/s3-encryption-migration.html): Describes how to migrate to the latest Amazon S3 encryption clients for |sdk-go}.
