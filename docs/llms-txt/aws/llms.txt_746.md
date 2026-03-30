# Source: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/llms.txt

# AWS SDK for PHP Developer Guide for version 3

> Introduces the AWS SDK for PHP and walks you through simple examples to use the SDK for the first time. Also provides tips and links to advanced features and resources.

- [What is the AWS SDK for PHP?](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/welcome.html)
- [Migrating from Version 2](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_migration.html)
- [FAQ](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/faq.html)
- [Glossary](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/glossary.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/document-history.html)

## [Getting started](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_index.html)

- [Prerequisites](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_requirements.html): Set up your environment to use the AWS SDK for PHP Version 3.
- [Installing](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html): Installing the AWS SDK for PHP Version 3.
- [Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/credentials.html): Learn how to authenticate your code with AWS using different methods, including IAM Identity Center for local development.
- [Creating a simple application](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/hello.html): Learn how to list your Amazon S3 buckets using the AWS SDK for PHP in this getting started tutorial.
- [Use AWS Cloud9 with the SDK](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cloud9.html): Learn how to use AWS Cloud9 with the AWS SDK for PHP.


## [Configuring service clients](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_index.html)

- [Client configuration externally](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuring-service-clients-ext.html): Learn how to configure service clients for the AWS SDK for PHP Version 3 using external methods such as environment variables and shared config files.

### [Client configuration in code](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuring-service-clients-code.html)

Configure service clients programmatically in code for the AWS SDK for PHP Version 3 to control client behavior and customize settings like credentials, regions, and HTTP options.

- [Constructor options](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_configuration.html): Custom client configuration options for the AWS SDK for PHP Version 3 client.
- [AWS Region](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/aws-php-sdk-region-resolution.html): This section explains how the AWS SDK for PHP Version 3 determines which AWS Region to use when making service requests.

### [Credential providers](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html)

Learn how to configure and use credential providers in the AWS SDK for PHP Version 3 to authenticate and access AWS services securely through various authentication methods.

- [Understanding the default credential provider chain in the AWS SDK for PHP Version 3](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_default_chain.html): Learn how the AWS SDK for PHP Version 3 searches for credentials using the default credential provider chain, including environment variables, IAM roles, and instance profiles.

### [Built-in credential providers in the AWS SDK for PHP Version 3](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/built-in-providers-in-the-sdk.html)

Learn about built-in credential providers in the AWS SDK for PHP, how to specify them during service client creation, and best practices for optimizing credential loading performance.

- [login provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/login-provider.html): Learn how to use the login provider in the AWS SDK for PHP to load credentials from browser-based login sessions facilitated by the AWS CLI.
- [assumeRole provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/assumerole-provider.html): Learn how to use the AssumeRoleCredentialProvider in AWS SDK for PHP to create credentials by assuming a role, and optimize credential fetching with memoization.
- [sso provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sso-provider.html): Learn how to use the IAM Identity Center credential provider in the SDK for PHP to authenticate and create a service client using single sign-on (SSO) credentials.
- [defaultProvider provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/defaultprovider-provider.html): Learn how to use the defaultProvider credential provider in the AWS SDK for PHP to automatically load AWS credentials for your client.
- [ecsCredentials provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ecscredentials-provider.html): Learn how to use the ecsCredentials provider to load AWS credentials for containers using the AWS SDK for PHP.
- [env provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/env-provider.html): Learn how to use environment variables to securely store and access AWS credentials in your application, preventing accidental exposure of sensitive information.
- [assumeRoleWithWebIdentityCredentialProvider provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/assume-role-with-web-identity-provider.html): Learn how to assume an IAM role using web identity federation, configure the AWS STS client, and use a web identity token file in the default credential chain.
- [ini provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ini-provider.html): Learn how to use the ini credential provider in the AWS SDK for PHP Version 3 to load credentials from shared config and credentials files for AWS service access.
- [process provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/process-provider.html): Learn how to use process credentials provider in the AWS SDK for PHP Version 3 to load credentials by executing a credential process specified in AWS configuration profiles.
- [instanceProfile provider in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/instanceprofile-provider.html): Learn how to use the instanceProfile credential provider in the AWS SDK for PHP Version 3 to load credentials for an IAM role from an Amazon EC2 instance profile.
- [Chaining credential providers in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/chaining-providers.html): Learn how to chain credential providers in the AWS SDK for PHP Version 3 to check multiple authentication methods before failing.
- [Creating a custom credential provider to use with the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/creating-a-custom-provider.html): Learn how to create custom credential providers for the AWS SDK for PHP Version 3 by implementing functions that return promises fulfilled with credential objects.
- [Memoizing credentials in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/memoizing-credentials.html): Learn how to improve performance by implementing credential provider memoization in the AWS SDK for PHP Version 3 to cache and reuse credentials across multiple AWS clients.
- [Assume an IAM role](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_assume_role.html): How to load credentials for AWS using the AWS SDK for PHP.
- [Use temporary credentials from AWS STS in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_temporary.html): Learn how to use temporary security credentials from AWS STS to grant limited access privileges to AWS services when using the AWS SDK for PHP Version 3.
- [Create anonymous clients in the SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_anonymous.html): Learn how to create anonymous clients and make anonymous requests to AWS services using the AWS SDK for PHP Version 3.
- [Use the AWS CRT extension](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_crt.html): Learn how to use the AWS Common Runtime (AWS CRT) extension with the AWS SDK for PHP.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_basic-usage.html)

### [Making AWS service requests](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/making-service-requests.html)

Learn how to make service requests using the AWS SDK for PHP Version 3, including creating service clients, executing operations, and processing results.

- [Command objects](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_commands.html): Fine-tune how the underlying HTTP handler executes the request to AWS services with the AWS SDK for PHP Version 3.

### [Asynchronous programming](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/asynchronous-requests.html)

Learn how to use asynchronous programming with promises in Version 3 of the AWS SDK for PHP Version 3 to execute concurrent API operations and manage HTTP requests efficiently.

- [Promises](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_promises.html): Learn how to use promises in the AWS SDK for PHP Version 3 to create asynchronous workflows and execute concurrent HTTP requests in a single thread.
- [Handling errors](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/handling-errors.html)
- [Handlers and middleware](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_handlers-and-middleware.html): Extend the AWS SDK for PHP Version 3 with handlers and middleware.
- [Streams](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_streams.html): Creating a Guzzle stream decorator with the AWS SDK for PHP Version 3.
- [Pagination](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_paginators.html): Learn how to work with paginated results in Version 3 of the AWS SDK for PHP, including using paginators to handle truncated API responses and process results asynchronously.
- [Waiters](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_waiters.html): Set up asynchronous work flow for AWS SDK for PHP Version 3.
- [JMESPath expressions](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_jmespath.html): Extract JSON data from the AWS SDK for PHP Version 3.


## [Calling AWS services](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/working-with-aws-services.html)

### [Use features and options](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/service_index.html)

High-level features of AWS Services supported by the AWS SDK for PHP.

- [Amazon DynamoDB](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/service_dynamodb-session-handler.html): Programing Amazon DynamoDB using the AWS SDK for PHP.

### [Amazon S3](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-sdk-features.html)

Learn about Amazon S3 features and options supported by the AWS SDK for PHP Version 3.

- [Multi-Region client](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-multiregion-client.html): Create a multi-region Amazon S3 client using the AWS SDK for PHP Version 3 .
- [Stream wrapper](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-stream-wrapper.html): Store and retrieve data from Amazon S3 with the AWS SDK for PHP Version 3.

### [Transfer files and directories](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfers.html)

The AWS SDK for PHP Version 3 provides two approaches for transferring files and directories to and from Amazon S3.

### [S3 Transfer Manager](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfer-manager.html)

Upload and download files to and from Amazon S3 with automatic multipart handling and progress tracking.

- [Basic usage](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/basic-usage.html): Create a transfer manager and upload files to Amazon S3 with simple API calls.
- [Configuration](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/configuration.html): Customize S3 Transfer Manager behavior with configuration options for multipart operations and checksums.
- [File operations](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/file-operations.html): Upload and download individual files with customizable request parameters and progress tracking.
- [Directory operations](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/directory-operations.html): Transfer entire directories between local storage and Amazon S3 with filtering and custom request modifiers.
- [Transfer listeners](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-tm-transfer-listener.html): Implement custom listeners to monitor transfer events and track progress during file operations.
- [Progress tracking](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/progress-tracking.html): Monitor file and directory transfer progress with built-in trackers or custom implementations.
- [Class diagram](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/class-diagram-tracking.html): View the relationships between tracking components for implementing custom listeners and progress tracking.
- [Error handling](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/error-handling.html): Handle transfer errors with promises and implement failure policies for directory operations.
- [Advanced usage](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/advanced-usage.html): Customize multipart operations, implement filters, and modify request parameters for advanced transfer scenarios.
- [Ready-to-use examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/examples.html): Use the S3TransferHelper class for simplified file and directory transfers with common operations.
- [Directory transfers](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfer.html): Transfer entire directories between your local file system and Amazon S3 buckets using the Transfer class in the AWS SDK for PHP version 3.
- [Client side encryption](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-encryption-client.html): Client-side encryption for the Amazon S3 client with the AWS SDK for PHP Version 3.
- [Data integrity protection with checksums](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-checksums.html): Learn how to use checksums with Amazon S3 in AWS SDK for PHP to ensure data integrity during object uploads and downloads.

### [Code examples with guidance](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/examples_index.html)

Code examples with guidance for the AWS SDK for PHP.

### [Amazon CloudFront examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cf-examples.html)

Amazon CloudFront code examples for the AWS SDK for PHP Version 3.

- [Managing CloudFront distributions](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cloudfront-example-distribution.html): Amazon CloudFront code examples for the AWS SDK for PHP Version 3.
- [Managing CloudFront invalidations](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cloudfront-example-invalidation.html): Amazon CloudFront code examples for the AWS SDK for PHP Version 3.
- [Signing CloudFront URLs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cloudfront-example-signed-url.html): Programing CloudFront using the AWS SDK for PHP Version 3.
- [Amazon CloudSearch](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/service_cloudsearch-custom-requests.html): Making a Amazon CloudSearch domain request using the AWS SDK for PHP.

### [Amazon CloudWatch examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples.html)

Amazon CloudWatch code examples for the AWS SDK for PHP Version 3

- [Working with Amazon CloudWatch alarms](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples-work-with-alarms.html): Create Amazon CloudWatch alarms that automatically stop, terminate, reboot, or recover Amazon EC2 instances using the AWS SDK for PHP Version 3.
- [Getting metrics from CloudWatch](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples-getting-metrics.html): List Amazon CloudWatch metrics, retrieve alarms for metrics, and get metric statistics using the AWS SDK for PHP Version 3.
- [Publishing custom metrics in Amazon CloudWatch](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples-publishing-custom-metrics.html): Publish metric data and create alarms for Amazon CloudWatch using the AWS SDK for PHP Version 3.
- [Sending events to Amazon CloudWatch events](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples-sending-events.html): Create rules and add targets to them, and send custom events to Amazon CloudWatch Events using the AWS SDK for PHP Version 3.
- [Using alarm actions with Amazon CloudWatch alarms](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples-using-alarm-actions.html): Create Amazon CloudWatch alarms that automatically stop, terminate, reboot, or recover EC2 instances using the AWS SDK for PHP Version 3.

### [Amazon EC2 examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples.html)

Programing Elastic Compute Cloud using the AWS SDK for PHP Version 3.

- [Managing Amazon EC2 instances](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-managing-instances.html): Engage with Amazon EC2 instances using the AWS SDK for PHP Version 3.
- [Using Elastic IP addresses](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-using-elastic-ip-addresses.html): Describe Amazon EC2 instances and acquire, associate, and release Elastic IP addresses using the AWS SDK for PHP Version 3.
- [Using regions and availability zones](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-using-regions-and-zones.html): Describe AWS Regions and Availability Zones for Amazon EC2 using the AWS SDK for PHP Version 3.
- [Working with key pairs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-working-with-key-pairs.html): Create and delete key pairs for Amazon EC2 using the AWS SDK for PHP Version 3.
- [Working with security groups](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-using-security-groups.html): Create, describe, and delete security groups for Amazon EC2 using the AWS SDK for PHP Version 3.
- [Amazon OpenSearch Service](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/service_es-data-plane.html): Sign and use Amazon OpenSearch Service with the AWS SDK for PHP.

### [AWS Identity and Access Management examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples.html)

Programing Identity and Access Management using the AWS SDK for PHP Version 3.

- [Managing IAM access keys](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-managing-access-keys.html): Create, delete, and get information about IAM access keys.
- [Managing IAM users](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-managing-users.html): Create, list, update, or retrieve info about AWS Identity and Access Management users.
- [Using IAM account aliases](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-using-account-aliases.html): Create, list, and delete aliases for AWS account IDs using AWS Identity and Access Management.
- [Working with IAM policies](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-working-with-policies.html): Create, attach, or remove AWS Identity and Access Management user policies.
- [Working with IAM server certificates](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-working-with-certs.html): List, update, and get information about certificates using AWS Identity and Access Management.

### [AWS Key Management Service](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-examples.html)

AWS KMS code examples for the AWS SDK for PHP Version 3.

- [Working with keys](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-example-keys.html): Use AWS KMS API to create, view, enable and disable AWS KMS keys.
- [Encrypting and decrypting data keys](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-example-encrypt.html): Use the AWS KMS API to encrypt and decrypt data.
- [Working with key policies](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-example-key-policy.html): Use the AWS KMS API to view and change the key policies of AWS KMS keys (KMS keys).
- [Working with grants](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-example-grants.html): Use AWS KMS API to create, view, retire, and revoke grants.
- [Working with aliases](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kms-example-alias.html): Use AWS KMS API to create, view, update, and delete aliases.

### [Kinesis examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kinesis-examples.html)

Amazon Kinesis Data Streams and Amazon Kinesis Data Firehose code examples for the AWS SDK for PHP Version 3.

- [Kinesis data streams](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kinesis-example-data-stream.html): Amazon Kinesis Data Streams code examples for the AWS SDK for PHP Version 3.
- [Kinesis shards](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kinesis-example-shard.html): Kinesis Data Streams code examples for the AWS SDK for PHP Version 3.
- [Kinesis Data Firehose delivery streams](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/kinesis-firehose-example-delivery-stream.html): Kinesis Data Firehose delivery streams code examples for the AWS SDK for PHP Version 3.
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/emc-examples.html): Examples that show how to use the AWS Elemental MediaConvert client class using the AWS SDK for PHP Version 3.

### [Amazon S3 examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples.html)

Amazon S3 code examples for AWS SDK for PHP Version 3.

- [Creating and using Amazon S3 buckets](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-creating-buckets.html): Describes how to use Amazon S3 buckets with the AWS SDK for PHP Version 3.
- [Managing Amazon S3 bucket access permissions](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-access-permissions.html): Get access control lists (ACLs) and set permissions for Amazon S3 buckets using the AWS SDK for PHP Version 3.
- [Configuring Amazon S3 buckets](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-configuring-a-bucket.html): Get or set CORS configuration for an Amazon S3 bucket using the AWS SDK for PHP Version 3.
- [Amazon S3 multipart uploads](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-multipart-upload.html): Learn how to use multipart uploads with Amazon S3 and the AWS SDK for PHP.
- [Amazon S3 pre-signed URL](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-presigned-url.html): Learn how to create pre-signed URLs for Amazon S3 using the AWS SDK for PHP.
- [Creating S3 pre-signed POSTs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-presigned-post.html): Create write access to private Amazon S3 data using the AWS SDK for PHP Version 3.
- [Using an Amazon S3 bucket as a static web host](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-static-web-host.html): Get, set, and remove website configuration for an Amazon S3 bucket with the AWS SDK for PHP Version 3.
- [Working with Amazon S3 bucket policies](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-bucket-policies.html): Return, replace, or delete Amazon S3 bucket policies using the AWS SDK for PHP Version 3.
- [Using S3 access point ARNs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples-access-point-arn.html): Using Access Point ARNs in S3 requests with the AWS SDK for PHP Version 3.
- [Use Multi-Region Access Points](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-multi-region-access-points.html): Learn how to work with Amazon S3 Multi-Region Access Points with the AWS SDK for PHP Version 3.
- [AWS Secrets Manager](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/secretsmanager-examples-manage-secret.html): AWS Secrets Manager code examples for the AWS SDK for PHP Version 3.

### [Amazon SES examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-examples.html)

Amazon SES code examples for the AWS SDK for PHP Version 3.

- [Verifying email addresses](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-verify.html): Use Amazon SES API to verify email addresses and domains.
- [Working with email templates](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-template.html): Use the Amazon SES API to create and use email templates.
- [Managing email filters](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-filters.html): Use the Amazon SES API to manage email filters.
- [Using email rules](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-rules.html): Use the Amazon SES API to manage email rules.
- [Monitor your sending activity](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-send-email.html): Use the Amazon SES API to monitor your sending reputation.
- [Authorizing senders](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ses-sender-policy.html): Use the Amazon SES API to authorize other users to send emails from addresses or domains.

### [Amazon SNS examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples.html)

Amazon SNS code examples for the AWS SDK for PHP Version 3.

- [Managing topics](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-managing-topics.html): How to create, list, and delete Amazon SNS topics, and how to handle topic attributes using the AWS SDK for PHP Version 3.
- [Managing subscriptions](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-subscribing-unsubscribing-topics.html): List all subscriptions, subscribe to an email address, an application endpoint, or an AWS Lambda function, or unsubscribe from Amazon Simple Notification Service topics using the AWS SDK for PHP version 3.
- [Sending amazon SMS messages](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-sending-sms.html): Get and set SMS messaging preferences, check a phone number, and get a list of phone numbers for Amazon SNS using the AWS SDK for PHP Version 3.

### [Amazon SQS examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples.html)

Amazon SQS code examples for the AWS SDK for PHP Version 3.

- [Enabling long polling](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples-enable-long-polling.html): Enable long polling, retrieve messages with long pulling, and create a long polling queue using the AWS SDK for PHP Version 3.
- [Managing visibility timeout](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples-managing-visibility-timeout.html): Change the visibility timeout for messages in using the AWS SDK for PHP Version 3.
- [Sending and receiving messages](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples-send-receive-messages.html): Deliver, delete, or retrieve messages using Amazon SQS with the AWS SDK for PHP Version 3.
- [Using dead-letter queues](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples-dead-letter-queues.html): Enable dead-letter queues with Amazon SQS using the AWS SDK for PHP Version 3.
- [Using queues](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sqs-examples-using-queues.html): Create or delete Amazon SQS queues, and return lists and URLs for queues using the AWS SDK for PHP Version 3.
- [Amazon EventBridge](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/eventbridge-examples.html): Learn how to send events to an Amazon EventBridge global endpoints by using AWS SDK for PHP Version 3


## [Code examples](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_code_examples.html)

- [API Gateway](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for PHP with API Gateway.
- [Aurora](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_aurora_code_examples.html): Code examples that show how to use AWS SDK for PHP with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for PHP with Auto Scaling.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_bedrock_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon Bedrock Runtime.
- [Amazon DocumentDB](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_docdb_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for PHP with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_ec2_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon EC2.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_glue_code_examples.html): Code examples that show how to use AWS SDK for PHP with AWS Glue.
- [IAM](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_iam_code_examples.html): Code examples that show how to use AWS SDK for PHP with IAM.
- [Kinesis](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_kinesis_code_examples.html): Code examples that show how to use AWS SDK for PHP with Kinesis.
- [AWS KMS](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_kms_code_examples.html): Code examples that show how to use AWS SDK for PHP with AWS KMS.
- [Lambda](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_lambda_code_examples.html): Code examples that show how to use AWS SDK for PHP with Lambda.
- [Amazon MSK](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_kafka_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon MSK.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_rds_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_rds-data_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon RDS Data Service.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_rekognition_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon Rekognition.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_s3_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon S3.
- [S3 Directory Buckets](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_s3-directory-buckets_code_examples.html): Code examples that show how to use AWS SDK for PHP with S3 Directory Buckets.
- [Amazon SES](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_ses_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon SES.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_sns_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_sqs_code_examples.html): Code examples that show how to use AWS SDK for PHP with Amazon SQS.


## [Security](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in the AWS SDK for PHP Version 3.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [Amazon S3 encryption client migration (V1 to V2)](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-encryption-migration-v1-v2.html): Learn how to migrate applications from Version 1 to Version 2 of the Amazon S3 encryption client in a AWS SDK for PHP Version 3 application while maintaining application availability throughout the process.
- [Amazon S3 encryption client migration (V2 to V3)](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-encryption-migration-v2-v3.html): Learn how to migrate applications from Version 2 to Version 3 of the Amazon S3 encryption client in a AWS SDK for PHP Version 3 application while maintaining application availability throughout the process.
