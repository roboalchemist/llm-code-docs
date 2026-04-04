# Source: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/llms.txt

# AWS SDK for Java 1.x Developer Guide for version 1.x

> Describes how to use the legacy version (1.x) of the AWS SDK for Java

- [AWS SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/welcome.html)
- [OpenPGP key](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/openpgp.html)
- [Document History](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/document-history.html)

## [Getting Started](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html)

- [Basic setup](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/signup-create-iam-user.html)
- [Ways to get the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-install.html): Learn ways to get the AWS SDK for Java for your project.

### [Use build tools](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-build-tools.html)

Learn how to use build tools to work with the AWS SDK for Java

- [Use the SDK with Apache Maven](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-project-maven.html): Learn how to set up an Apache Maven project for the AWS SDK for Java.
- [Use the SDK with Gradle](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-project-gradle.html): Learn how to use Gradle to set up your AWS SDK for Java project.
- [Temporary credentials and Region](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html): Learn how to set up default AWS credentials and AWS Region for development with the AWS SDK for Java.


## [Using the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/basics.html)

- [Best Practices for AWS Development with the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/best-practices.html): AWS coding best practices using the AWS SDK for Java.
- [Creating Service Clients](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/creating-clients.html): How to create service clients by using the AWS SDK for Java.
- [Provide temporary credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html): Learn how to provide temporary credentials in order to use AWS services using the AWS SDK for Java.
- [AWS Region Selection](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-region-selection.html): How to check service availability and choose an AWS Region and specific endpoints.
- [Exception Handling](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-exceptions.html): How to handle exceptions thrown by the AWS SDK for Java.
- [Asynchronous Programming](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/basics-async.html): How asynchronous programming works in the AWS SDK for Java and best practices for handling exceptions
- [Logging AWS SDK for Java Calls](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html): How to use Apache Log4j with the AWS SDK for Java.
- [Client Configuration](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html): How to change proxy configuration, HTTP transport configuration, and TCP socket buffer size hints by using the AWS SDK for Java.
- [Access Control Policies](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-access-control.html): How to specify access control policies using the AWS SDK for Java, with examples for Amazon S3, Amazon SQS, and Amazon SNS.
- [Set the JVM TTL for DNS name lookups](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/jvm-ttl-dns.html): Learn how to set Java virtual machine (JVM) for DNS name lookups using the AWS SDK for Java.
- [Enabling Metrics for the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/generating-sdk-metrics.html): The AWS SDK for Java can generate metrics for visualization and monitoring with Amazon CloudWatch that measure:


## [Code Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services.html)

### [Amazon CloudWatch Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch.html)

Programming Amazon CloudWatch using the AWS SDK for Java

- [Getting Metrics from CloudWatch](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch-get-metrics.html): How to list metrics from Amazon CloudWatch using the AWS SDK for Java.
- [Publishing Custom Metric Data](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch-publish-custom-metrics.html): How to publish your own custom metric data to Amazon CloudWatch using the AWS SDK for Java.
- [Working with CloudWatch Alarms](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch-create-alarms.html): How to create, list, and delete alarms in Amazon CloudWatch using the AWS SDK for Java
- [Using Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch-use-alarm-actions.html): How to enable or disable alarm actions for Amazon CloudWatch with the AWS SDK for Java.
- [Sending Events to CloudWatch](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-cloudwatch-send-events.html): How to add events, rules and rule targets for Amazon CloudWatch using the AWS SDK for Java.

### [Amazon DynamoDB Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-dynamodb.html)

Programming Amazon DynamoDB using the AWS SDK for Java

- [Working with Tables in DynamoDB](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-dynamodb-tables.html): How to create, describe, modify (update) and delete Amazon DynamoDB tables.
- [Working with Items in DynamoDB](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-dynamodb-items.html): How to retrieve (get), add, and update items in Amazon DynamoDB tables.

### [Amazon EC2 Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-ec2.html)

Programming Amazon EC2 using the AWS SDK for Java

### [Tutorial: Starting an EC2 Instance](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/how-to-ec2.html)

This tutorial demonstrates how to use the AWS SDK for Java to start an EC2 instance.

- [Create an Amazon EC2 Security Group](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/create-security-group.html)
- [Create a Key Pair](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/create-key-pair.html): You must specify a key pair when you launch an EC2 instance and then specify the private key of the key pair when you connect to the instance.
- [Run an Amazon EC2 Instance](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/run-instance.html): Use the following procedure to launch one or more identically configured EC2 instances from the same Amazon Machine Image (AMI).
- [Using IAM Roles to Grant Access to AWS Resources on Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-roles.html): All requests to Amazon Web Services (AWS) must be cryptographically signed using credentials issued by AWS.
- [Tutorial: Amazon EC2 Spot Instances](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/tutorial-spot-instances-java.html)
- [Tutorial: Advanced Amazon EC2 Spot Request Management](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/tutorial-spot-adv-java.html): Amazon EC2 Spot Instances allow you to bid on unused Amazon EC2 capacity and run those instances for as long as your bid exceeds the current spot price.
- [Managing Amazon EC2 Instances](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-instances.html): How to create, start, stop, reboot, list and monitor EC2 instances using the AWS SDK for Java.
- [Using Elastic IP Addresses in Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-elastic-ip.html): How to allocate, use, list, and release Elastic IP addresses for EC2 instances with the AWS SDK for Java.
- [Use regions and availability zones](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-regions-zones.html): How to list EC2 regions and availability zones using the AWS SDK for Java.
- [Working with Amazon EC2 Key Pairs](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-key-pairs.html): How to create, list and delete EC2 key pairs using the AWS SDK for Java.
- [Working with Security Groups in Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-ec2-security-groups.html): How to create, configure and delete EC2 security groups with the AWS SDK for Java.

### [AWS Identity and Access Management (IAM) Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam.html)

Programming AWS Identity and Access Management using the AWS SDK for Java

- [Managing IAM Access Keys](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam-access-keys.html): How to manage IAM access keys with the AWS SDK for Java.
- [Managing IAM Users](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam-users.html): How to set, get, and delete a policy for an Amazon S3 bucket.
- [Using IAM Account Aliases](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam-account-aliases.html): How to set, get, and delete a policy for an Amazon S3 bucket.
- [Working with IAM Policies](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam-policies.html): How to set, get, and delete a policy for an Amazon S3 bucket.
- [Working with IAM Server Certificates](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-iam-server-certificates.html): How to set, get, and delete a policy for an Amazon S3 bucket.

### [Amazon Lambda Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/lambda-examples.html)

Programming Amazon Lambda using the AWS SDK for Java.

- [Service operations](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-lambda.html): How to invoke, list, and delete a Lambda function by using the AWS SDK for Java 2.x.

### [Amazon Pinpoint Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint.html)

Programming Amazon Pinpoint using the AWS SDK for Java

- [Creating and Deleting Apps in Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint-create-app.html): How to create or delete an app in Amazon pinpoint.
- [Creating Endpoints in Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint-create-endpoint.html): How to update an app endpoint in Amazon pinpoint.
- [Creating Segments in Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint-create-segment.html): How to update an app segment in Amazon pinpoint.
- [Creating Campaigns in Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint-create-campaign.html): How to create a campaign in Amazon pinpoint.
- [Updating Channels in Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-pinpoint-update-channel.html): How to update an app channel in Amazon pinpoint.

### [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3.html)

Programming Amazon S3 using the AWS SDK for Java

- [Creating, Listing, and Deleting Amazon S3 Buckets](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-buckets.html): How to create, list, or delete a bucket using the AWS SDK for Java.
- [Performing Operations on Amazon S3 Objects](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-objects.html): How to list, upload, download, copy, rename, move or delete objects in an Amazon S3 bucket using the AWS SDK for Java.
- [Managing Amazon S3 Access Permissions for Buckets and Objects](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-access-permissions.html): How to retrieve or set the access control list for an Amazon S3 bucket.
- [Managing Access to Amazon S3 Buckets Using Bucket Policies](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-bucket-policies.html): How to set, get, and delete a policy for an Amazon S3 bucket.
- [Using TransferManager for Amazon S3 Operations](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-transfermanager.html): How to use the AWS SDK for Java's TransferManager class to upload, download, and copy files and directories using Amazon S3.
- [Configuring an Amazon S3 Bucket as a Website](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-website-configuration.html): How to set, retrieve, or delete an S3 bucketâs website configuration.

### [Use Amazon S3 client-side encryption](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-crypto.html)

How to use the cryptography configuration settings for the AWS SDK for Java

- [Amazon S3 client-side encryption with client master keys](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-crypto-masterkey.html): How to use the cryptography configuration settings for the AWS SDK for Java
- [Amazon S3 client-side encryption with AWS KMS managed keys](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-crypto-kms.html): How to use the cryptography configuration settings for the AWS SDK for Java

### [Amazon SQS Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs.html)

Programming Amazon SQS using the AWS SDK for Java

- [Working with Amazon SQS Message Queues](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs-message-queues.html): How to create, list, delete, and get an Amazon SQS queueâs URL.
- [Sending, Receiving, and Deleting Amazon SQS Messages](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs-messages.html): How to send, receive and delete Amazon SQS messages.
- [Enabling Long Polling for Amazon SQS Message Queues](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs-long-polling.html): How to enable long polling for Amazon SQS message queues.
- [Setting Visibility Timeout in Amazon SQS](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs-visibility-timeout.html): How to set visibility timeout for Amazon SQS queues with the AWS SDK for Java.
- [Using Dead Letter Queues in Amazon SQS](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-sqs-dead-letter-queues.html): How to enable long polling for Amazon SQS message queues.

### [Amazon SWF Examples](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-swf.html)

Amazon SWF is a workflow-management service that helps developers build and scale distributed workflows that can have parallel or sequential steps consisting of activities, child workflows or even Lambda tasks.

- [SWF basics](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/swf-basics.html): These are general patterns for working with Amazon SWF using the AWS SDK for Java.
- [Building a Simple Amazon SWF Application](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/swf-hello.html): This topic will introduce you to programming Amazon SWF applications with the AWS SDK for Java, while presenting a few important concepts along the way.
- [Lambda Tasks](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/swf-lambda-task.html): As an alternative to, or in conjunction with, Amazon SWF activities, you can use Lambda functions to represent units of work in your workflows, and schedule them similarly to activities.
- [Shutting Down Activity and Workflow Workers Gracefully](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/swf-graceful-shutdown.html): The Building a Simple Amazon SWF Application topic provided a complete implementation of a simple workflow application consisting of a registration application, an activity and workflow worker, and a workflow starter.
- [Registering Domains](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-swf-register-domain.html): Every workflow and activity in Amazon SWF needs a domain to run in.
- [Listing Domains](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-swf-list-domains.html): You can list the Amazon SWF domains associated with your account and AWS region by registration type.
- [Code Samples included with the SDK](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-samples.html): The AWS SDK for Java comes packaged with code samples that demonstrate many of the features of the SDK in buildable, runnable programs.


## [Security](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/security-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in this AWS product or service.
- [Enforcing a minimum TLS version](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/security-java-tls.html): Applies to Java SSL implementation (default SSL implementation in the SDK).
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
- [S3 Encryption Client Migration](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/s3-encryption-migration.html): How to migrate your applications from v1 to v2 of the AWS S3 client-side encryption
