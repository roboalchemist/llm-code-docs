# Source: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/llms.txt

# AWS SDK for Java 2.x Developer Guide for version 2.x

> The AWS SDK for Java 2.x Developer guide provides developers with comprehensive coverage of the SDK that enables developers to build high-performance applications that interact with AWS services through both synchronous and asynchronous programming models, featuring non-blocking I/O, customizable HTTP clients, streamlined authentication mechanisms, and extensive code examples.

- [What is the AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html)
- [OpenPGP key](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/openpgp.html)
- [Document history](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/document-history.html)

## [Getting started](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html)

### [Setting up](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html)

Learn how to set up your development environment and configure projects to use the AWS SDK for Java 2.x, including installing Java, choosing a build tool, and managing credentials.

- [Install Java development prerequisites](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-java-buildtool.html): Learn how to set up your Java development environment with the required Java version and build tools to use the AWS SDK for Java 2.x.
- [Set up an Apache Maven project](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html): Learn how to use Apache Maven for a AWS SDK for Java 2.x project.
- [Set up a Gradle project](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-gradle.html): Learn the initial steps for how to use Gradle for an AWS SDK for Java 2.x project.
- [Set up a GraalVM Native Image project](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-graalvm.html): Set up a GraalVM Native Image project for the AWS SDK for Java 2.x using Maven archetype.
- [Authenticating with AWS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started-auth.html): Learn how to set up authentication for the AWS SDK for Java 2.x using AWS IAM Identity Center.
- [Creating a simple application](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started-tutorial.html): Create a simple Java application using the AWS SDK for Java 2.x to interact with Amazon S3.


## [Configuring service clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients.html)

- [Client configuration externally](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients-ext.html): Learn how to configure service clients for the AWS SDK for Java 2.x using external methods such as environment variables and shared config files.
- [Client configuration in code](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients-code.html): As an alternative toâor in addition toâconfiguring service clients externally, you can configure them programmatically in code.
- [Singleton service clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/singleton-service-clients.html): Create one service client instance and reuse it throughout your application to improve performance and manage resources efficiently.
- [AWS Region](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/region-selection.html): Learn how to configure a service clients with an AWS Region and optionally configure a specific endpoint within a Region.

### [Credentials providers](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials.html)

Learn how to enable the AWS SDK for Java 2.x to access temporary credentials for cryptographically signing requests to AWS services.

- [Interactive development work](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-temporary.html): Learn how to configure the SDK for Java 2.xto use temporary credentials for enhanced security, including IAM Identity Center setup and manual retrieval from the AWS access portal.
- [Default credentials provider chain](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html): Learn about the default credentials provider chain in AWS SDK for Java 2.x, including its implementation, credential retrieval order, and supported authentication methods.
- [Credentials caching](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credential-caching.html): Learn how credential caching works in the AWS SDK for Java 2.x and configure caching strategies to improve performance and reduce calls to credential sources.
- [Specify a specific credentials provider](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-providers.html): Learn how to configure a specific credentials provider for AWS SDK for Java 2.x service clients, bypassing the default provider chain for faster initialization.
- [Use shared configuration profiles](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-profiles.html): Learn how to use profiles with the AWS SDK for Java 2.x to manage multiple sets of credentials, set default profiles, and reload profile credentials dynamically.
- [Use an external process](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-process.html): Learn how to load temporary credentials from an external process using the AWS SDK for Java 2.x, including configuration methods and code examples for different operating systems.
- [Supply credentials in code](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-explicit.html): Learn how to supply temporary credentials in code for AWS services using IAM roles and AWS Security Token Service (STS).
- [Read IAM role credentials on Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ec2-iam-roles.html): Learn how to acquire and use IAM role credentials for Java applications running on Amazon EC2 instances, including methods for secure credential retrieval using IMDSv2.
- [Retries](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html): Configure retry strategies to handle failed calls to AWS services using standard, legacy, or adaptive modes.
- [Timeouts](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/timeouts.html): Configure service client timeouts and HTTP client timeouts to optimize performance and build resilient applications.

### [Observability](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/observability.html)

Telemetry is the automated collection and transmission of data from remote sources that enable you to monitor and analyze your system's behavior.

### [Metrics](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics.html)

Learn how to enable and configure metrics collection and publishing for the AWS SDK for Java 2.x

- [Long-running applications](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-cwmp.html): Learn how to publish SDK metrics for long-running Java applications using CloudWatchMetricPublisher in the AWS SDK for Java 2.x.
- [Lambda functions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-emf.html): Learn how to publish SDK metrics for AWS Lambda functions using EmfMetricLoggingPublisher, including setup, configuration, and implementation in Java.
- [Console output for SDK metrics](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-logging.html): Learn how to use LoggingMetricPublisher to output SDK metrics directly to the console for development, debugging, and troubleshooting purposes.
- [Metrics reference](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics-list.html): Learn about the metrics collected and published by the AWS SDK for Java 2.x for monitoring service client performance and request handling.
- [Monitoring](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/monitoring-overview.html): Monitor SDK for Java 2.x applications to maintain reliability, availability, and performance.
- [Logging](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/logging-slf4j.html): Learn how to configure logging for the SDK for Java 2.x including wire logging.
- [Endpoints](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/endpoint-config.html): The SDK for Java 2.x provides multiple ways to configure service endpoints.

### [Configure HTTP clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration.html)

Learn how to configure HTTP clients in the AWS SDK for Java 2.x.

- [Configure the Apache-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-apache.html): Learn how to configure the Apache-based HTTP client in the AWS SDK for Java 2.x.
- [Configure the URLConnection-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-url.html): Learn how to configure URLConnection-based HTTP client in the AWS SDK for Java 2.x.
- [Configure the Netty-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-netty.html): Learn how to configure the Netty-based HTTP clients in the AWS SDK for Java 2.x.
- [Configure AWS CRT-based HTTP clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html): Learn how to configure the synchronous and asynchronous AWS Common Runtime HTTP clients in the AWS SDK for Java 2.x.
- [Configure HTTP proxies](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-config-proxy-support.html): Learn how to use the AWS SDK for Java to configure HTTP proxies.
- [Configure the Apache 5.x based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-apache5.html): Learn how to configure the Apache5.x based HTTP client in the AWS SDK for Java 2.x.
- [Interceptors](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/interceptors.html): Learn how to use execution interceptors using the AWS SDK for Java 2.x to add custom logic at various stages of API call execution, including logging, metrics collection, and request modification.


## [Using the SDK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/using.html)

- [Making AWS service requests](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/work-witih-clients.html): Learn how to make service requests using the AWS SDK for Java 2.x, including how to create and configure service clients, make requests, and handle responses.
- [Asynchronous programming](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/asynchronous.html): Learn how to program with the asynchronous APIs in the AWS SDK for Java 2.x
- [Best practices](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices.html): Learn best practices for using AWS SDK for Java 2.x, including client reuse, input stream management, HTTP configuration tuning, and setting API timeouts.
- [Handling errors](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/handling-exceptions.html): Learn how to handle exceptions and errors when using the AWS SDK for Java 2.x, including service exceptions, client exceptions, and retry behavior.
- [Pagination](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/pagination.html): Learn how to work with paginated responses with AWS SDK for Java 2.x.
- [Waiters](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/waiters.html): Learn how to poll for AWS resource states using the waiters utility for the AWS SDK for Java v2.
- [Troubleshooting](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/troubleshooting.html): Learn how to troubleshoot common runtime errors in the AWS SDK for Java 2.x, including connection issues, timeouts, classpath problems, and signature mismatches.
- [Reduce SDK startup time for AWS Lambda](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/lambda-optimize-starttime.html): Learn how to minimize SDK cold startup time when using SDK for Java 2.x with AWS Lambda.
- [Implement ContentStreamProvider](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/content-stream-provider.html): Learn how to implement the ContentStreamProvider interface in AWS SDK for Java 2.x for multiple data reads.
- [Set the JVM TTL for DNS name lookups](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/jvm-ttl-dns.html): Learn how to set Java virtual machine (JVM) for DNS name lookups using the AWS SDK for Java.
- [Work with HTTP/2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http2.html): Basic information about the HTTP/2 protocol and how itâs implemented in the AWS SDK for Java 2.x.


## [Calling AWS services](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/work-with-services.html)

### [CloudWatch](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch.html)

How to use the AWS SDK for Java to work with Amazon CloudWatch

- [Get metrics from CloudWatch](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-get-metrics.html): How to list metrics from Amazon CloudWatch using the AWS SDK for Java 2.x
- [Publish custom metric data to CloudWatch](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-publish-custom-metrics.html): How to publish your own custom metric data to Amazon CloudWatch using the AWS SDK for Java 2.x
- [Work with CloudWatch alarms](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-create-alarms.html): How to create, list, and delete alarms in Amazon CloudWatch using the AWS SDK for Java 2.x
- [Use Amazon CloudWatch Events](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudwatch-send-events.html): Learn how to add events, rules and rule targets for Amazon CloudWatch Events using the AWS SDK for Java 2.x.
- [AWS database services](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-databases.html): Get an overview of using the SDK for Java 2.x to work with AWS databases.

### [DynamoDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb.html)

Create tables, manage items, and use object mapping with Amazon DynamoDB using the AWS SDK for Java.

- [Work with tables in DynamoDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb-tables.html): How to create, describe, modify (update) and delete Amazon DynamoDB tables.
- [Work with items in DynamoDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb-items.html): How to retrieve (get), add, and update items in Amazon DynamoDB tables.

### [Map objects to DynamoDB items](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html)

Learn about how to map Java objects to DynamoDB items by using the DynamoDB Enhanced Client API in the AWS SDK for Java 2.x.

### [Get started](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started.html)

Get started with the DynamoDB Enhanced Client API.

- [Generate a TableSchema from a data class](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html): Learn what a TableSchema is and how to generate one from a Java bean class.
- [Create an enhanced client and DynamoDbTable](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-getting-started-dynamodbTable.html): Learn about how to create a DynamoDB Enhanced Client and a DynamoDbTable.
- [Create a table](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-ddbtable.html): Learn how to create a DynamoDB table by using the DynamoDB Enhanced Client API.
- [Perform operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-use.html): See a first example of operations performed by using a DynamoDbTable instance.
- [Work with an existing table](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-existingtable.html): Learn how to use the DynamoDB Enhanced Client with an existing table.

### [Learn basics](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use.html)

Learn about the basics needed to work with the DynamoDB Enhanced Client API.

- [Work with immutable data classes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-immut.html): Learn how to work with immutable data class using DynamoDB Enhanced Client.
- [Use expressions and conditions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-expressions.html): Learn about expressions and how to expression conditions by using the DynamoDB Enhanced Client API.
- [Perform scans and queries](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-multirecord.html): Learn how to use the query and scan APIs of the DynamoDB Enhanced Client and learn how to process multiple items that are sent in the response.
- [Perform batch operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-multiop-batch.html): Learn about the batch API of the DynamoDB Enhanced Client and see examples.
- [Perform transaction operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-multiop-trans.html): Learn about the transaction API of DynamoDB Enhanced Client API and see examples.
- [Use secondary indices](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-use-secindex.html): Learn about using secondary indices in queries and scans made with the DynamoDB Enhanced Client.

### [Use advanced mapping features](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features.html)

Learn about advanced mapping features of table schemas in the DynamoDB Enhanced Client API.

- [Explicitly include or exclude attributes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-inex-attr.html): Learn how to explicitly include or exclude attributes.
- [Control attribute conversion](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-conversion.html): Learn how to control the conversion of mapped attributes.
- [Change update behavior of attributes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-upd-behavior.html): Learn about update behaviors that you can apply to attributes by using the DynamoDB Enhanced Client API.
- [Flatten attributes from other classes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-flatmap.html): Learn about ways to flatten attributes onto a single class when the classes use inheritance or composition.
- [Work with attributes that are beans, maps, lists and sets](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-nested.html): Learn how to work with attributes that are nested beans, maps, lists and sets by using DynamoDB Enhanced Client API.
- [Preserve empty objects](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-empty.html): Learn about the @DynamoDbPreserveEmptyObject annotation that recreates empty objects.
- [Ignore null attributes of nested objects](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-ignore-null.html): Learn about the @DynamoDbIgnoreNulls annotation that ignores null attributes of nested objects.

### [Work with JSON documents](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api.html)

Learn how to work with the JSON-style document model by using the DynamoDB Enhanced Client API.

- [Get started](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api-steps.html): Learn how to use an EnhancedDocument instance to perform DynamoDB CRUD operations.
- [Build enhanced documents](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api-steps-create-ed.html): Learn how to build an EnhancedDocument instance by using the Enhanced Document API.
- [Perform CRUD operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api-steps-use.html): Learn how to perform CRUD operations by using an EnhancedDocument.
- [Use custom objects](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api-convert.html): Learn how you can provide custom attribute converters to work with enhanced documents.
- [Enhanced documents for conversion](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-doc-api-standalone.html): Learn how you can use an EnhancedDocument instance for conversion.

### [Customize operations with extensions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-extensions.html)

Learn how extensions add functionality to the DynamoDB Enhanced Client API beyond basic mapping operations.

- [Custom extension example](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-extensions-custom.html): Create custom extensions by implementing the DynamoDbEnhancedClientExtension interface to add specialized functionality to DynamoDB Enhanced Client operations.
- [Go asynchronous](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-async.html): Learn about how to use DynamoDB Enhanced Client API with an asynchronous client.
- [Annotation reference](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-anno-index.html): Find examples and information about data class annotations used in this DynamoDB Enhanced Client API guide.

### [Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2.html)

Programming Amazon EC2 by using the AWS SDK for Java 2.x

- [Manage Amazon EC2 instances](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-instances.html): How to create, start, stop, reboot, list and monitor Amazon EC2 instances using the AWS SDK for Java 2.x.
- [Use AWS Regions and Availability Zones](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-regions-zones.html): Learn how to use Amazon EC2 API of the AWS SDK for Java 2.x to descibe AWS Regions, Availability Zones, and accounts.
- [Work with security groups in Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-security-groups.html): How to create, configure and delete Amazon EC2 security groups with the AWS SDK for Java 2.x.
- [Work with Amazon EC2 instance metadata](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-IMDS.html): Learn how to work with Amazon EC2 instance metadata using the AWS SDK for Java 2.x.

### [IAM](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-iam.html)

Programming AWS Identity and Access Management using the AWS SDK for Java 2.x

- [Manage IAM access keys](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-iam-access-keys.html): Learn how to manage IAM access keys with the AWS SDK for Java 2.x.
- [Manage IAM Users](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-iam-users.html): How to create, list, update and delete IAM users.
- [Create IAM policies](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/feature-iam-policy-builder.html): Learn how to build IAM policies using an object-oriented approach with AWS SDK for Java 2.x.
- [Work with IAM policies](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-iam-policies.html): How to create, attach and detach policies to IAM roles.
- [Work with IAM server certificates](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-iam-server-certificates.html): How to get, list, update and delete IAM server certificates.

### [Kinesis](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-kinesis.html)

Programming Amazon Kinesis using the AWS SDK for Java 2.x

- [Subscribe to Amazon Kinesis Data Streams](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-kinesis-stream.html): How to use Amazon Kinesis Data Streams to get results from Amazon Kinesis using the AWS SDK for Java 2.x.
- [Lambda](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-lambda.html): Learn wow to invoke, list, and delete a Lambda function by using the AWS SDK for Java 2.x.

### [Amazon S3](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)

Learn about working with Amazon S3 using the AWS SDK for Java 2.x.

- [Uploading streams to S3](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices-s3-uploads.html): Learn best practices for uploading streams to Amazon S3 using the AWS SDK for Java 2.x, including handling known and unknown content lengths.
- [Pre-signed URLs](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-presign.html): Learn how to work with pres-igned URLs by using the AWS SDK for Java 2.x.
- [Cross-Region access](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/s3-cross-region.html): Learn about support for cross-Region access for Amazon S3 in the AWS SDK for Java 2.x.
- [Data integrity protection with checksums](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/s3-checksums.html): Learn how to use checksums with Amazon S3 in AWS SDK for Java to ensure data integrity during object uploads and downloads.
- [Use a performant S3 client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html): Learn about the advantages of using the AWS CRT-based S3 client as an asynchronous service client for S3 operations.
- [Configure parallel transfer support](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/s3-async-client-multipart.html): Configure parallel transfer support in the Java-based S3 asynchronous client to enable multipart uploads and downloads, including handling streams of unknown size.
- [Transfer files and directories](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/transfer-manager.html): Learn about using the Amazon S3 Transfer Manager to upload and download files and directories to and from Amazon Simple Storage Service (Amazon S3).
- [S3 Event Notifications](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3-event-notifications.html): Learn how to work with object-oriented S3 Event Notifications API by using the AWS SDK for Java 2.x.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-simple-notification-service.html): Learn how to use the AWS SDK for Java to work with Amazon Simple Notification Service (Amazon SNS).

### [Amazon SQS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-sqs.html)

Learn how to use the Amazon Simple Queue Service by using the AWS SDK for Java 2.x

- [Use automatic request batching](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/sqs-auto-batch.html): Learn how to use the Automatic Request Batching API for Amazon SQS with the AWS SDK for Java 2.x to improve throughput and reduce costs by efficiently batching and buffering requests.
- [Queue operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-sqs-message-queues.html): Learn how to create, list, delete, and get an Amazon Simple Queue Service queueâs URL.
- [Message operations](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-sqs-messages.html): Learn how to send, receive and delete Amazon Simple Queue Service messages.
- [Amazon Transcribe](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-transcribe.html): Learn how to set up bidirectional streaming for Amazon Transcribe by using the SDK for Java 2.x.


## [Code examples](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_code_examples.html)

- [ACM](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_acm_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with ACM.
- [API Gateway](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_api-gateway_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with API Gateway.
- [Application Auto Scaling](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_application-auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Application Auto Scaling.
- [Application Recovery Controller](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_route53-recovery-cluster_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Application Recovery Controller.
- [Aurora](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_aurora_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Aurora.
- [Auto Scaling](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_auto-scaling_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Auto Scaling.
- [AWS Batch](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_batch_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Batch.
- [Amazon Bedrock](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_bedrock_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Bedrock.
- [Amazon Bedrock Runtime](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_bedrock-runtime_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Bedrock Runtime.
- [CloudFront](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cloudfront_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with CloudFront.
- [CloudWatch](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cloudwatch_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with CloudWatch.
- [CloudWatch Events](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cloudwatch-events_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with CloudWatch Events.
- [CloudWatch Logs](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cloudwatch-logs_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with CloudWatch Logs.
- [Amazon Cognito Identity](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cognito-identity_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Cognito Identity.
- [Amazon Cognito Identity Provider](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cognito-identity-provider_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Cognito Identity Provider.
- [Amazon Comprehend](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_comprehend_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Comprehend.
- [AWS Control Tower](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_controltower_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Control Tower.
- [Firehose](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_firehose_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Firehose.
- [Amazon DocumentDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_docdb_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon DocumentDB.
- [DynamoDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_dynamodb_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with DynamoDB.
- [Amazon EC2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_ec2_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon EC2.
- [Amazon ECR](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_ecr_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon ECR.
- [Amazon ECS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_ecs_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon ECS.
- [Elastic Load Balancing - Version 2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_elastic-load-balancing-v2_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Elastic Load Balancing - Version 2.
- [MediaStore](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_mediastore_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with MediaStore.
- [AWS Entity Resolution](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_entityresolution_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Entity Resolution.
- [OpenSearch Service](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_opensearch_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with OpenSearch Service.
- [EventBridge](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_eventbridge_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with EventBridge.
- [EventBridge Scheduler](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_scheduler_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with EventBridge Scheduler.
- [Forecast](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_forecast_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Forecast.
- [Amazon Glacier](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_glacier_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Glacier.
- [AWS Glue](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_glue_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Glue.
- [HealthImaging](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_medical-imaging_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with HealthImaging.
- [IAM](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_iam_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with IAM.
- [Amazon Inspector](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_inspector_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Inspector.
- [AWS IoT](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_iot_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS IoT.
- [AWS IoT data](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_iot-data-plane_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS IoT data.
- [AWS IoT FleetWise](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_iotfleetwise_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS IoT FleetWise.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_iotsitewise_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS IoT SiteWise.
- [Amazon Keyspaces](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_keyspaces_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Keyspaces.
- [Kinesis](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_kinesis_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Kinesis.
- [AWS KMS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_kms_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS KMS.
- [Lambda](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_lambda_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Lambda.
- [Amazon Lex](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_lex_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Lex.
- [Amazon Location](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_location_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Location.
- [Location Service Places](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_geo-places_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Location Service Places.
- [AWS Marketplace Catalog API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_marketplace-catalog_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Marketplace Catalog API.
- [AWS Marketplace Agreement API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_marketplace-agreement_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS Marketplace Agreement API.
- [MediaConvert](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_mediaconvert_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with MediaConvert.
- [Migration Hub](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_migration-hub_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Migration Hub.
- [Amazon MSK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_kafka_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon MSK.
- [Neptune](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_neptune_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Neptune.
- [Partner Central](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_partnercentral-selling_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Partner Central.
- [Amazon Personalize](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_personalize_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Personalize.
- [Amazon Personalize Events](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_personalize-events_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Personalize Events.
- [Amazon Personalize Runtime](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_personalize-runtime_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Personalize Runtime.
- [Amazon Pinpoint](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_pinpoint_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Pinpoint.
- [Amazon Pinpoint SMS and Voice API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_pinpoint-sms-voice_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Pinpoint SMS and Voice API.
- [Amazon Polly](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_polly_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Polly.
- [Amazon RDS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_rds_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon RDS.
- [Amazon RDS Data Service](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_rds-data_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon RDS Data Service.
- [Amazon Redshift](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_redshift_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Redshift.
- [Amazon Rekognition](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_rekognition_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Rekognition.
- [RouteÂ 53 domain registration](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_route-53-domains_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with RouteÂ 53 domain registration.
- [Amazon S3](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_s3_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon S3.
- [Amazon S3 Control](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_s3-control_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon S3 Control.
- [S3 Directory Buckets](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_s3-directory-buckets_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with S3 Directory Buckets.
- [SageMaker AI](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sagemaker_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with SageMaker AI.
- [Secrets Manager](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_secrets-manager_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Secrets Manager.
- [Amazon SES](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_ses_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon SES.
- [Amazon SES API v2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sesv2_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon SES API v2.
- [Amazon SNS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sns_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon SNS.
- [Amazon SQS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sqs_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon SQS.
- [Step Functions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sfn_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Step Functions.
- [AWS STS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_sts_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with AWS STS.
- [Support](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_support_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Support.
- [Systems Manager](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_ssm_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Systems Manager.
- [Amazon Textract](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_textract_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Textract.
- [Amazon Transcribe](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_transcribe_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Transcribe.
- [Amazon Transcribe Streaming](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_transcribe-streaming_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Transcribe Streaming.
- [Amazon Translate](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_translate_code_examples.html): Code examples that show how to use AWS SDK for Java 2.x with Amazon Translate.


## [Migrate to version 2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html)

### [How to migrate](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-howto.html)

Learn about how to migrate your SDK for Java applications from version 1 to version 2.

### [Migration tool](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-tool.html)

Learn how to use the AWS SDK for Java migration tool to migrate your Java applications from version 1 to version 2 of the Java SDK.

- [Unsupported code patterns](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-tool-unsupported-patterns.html): Learn about code patterns that the migration tool cannot automatically convert from AWS SDK for Java v1 to v2, and how to manually migrate them.
- [Step-by-step instructions](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-steps.html): Follow the step-by-step instructions to migrate your application that uses the SDK for Java v1.x to the SDK for Java 2.x.

### [What's different between 1.x and 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-whats-different.html)

This section describes the main changes to be aware of when converting an application from using version 1.x to version 2.x.

### [Client changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-clients.html)

Learn about the differences in service clients between version 1.x and 2.x of the AWS SDK for Java.

- [Client creation defaults](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-creation-defaults.html): Learn about the changes in the defaults for client creation from the SDK for Java v1.x to 2.x.
- [Client configuration](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-configuration.html): Learn about the changes in client configurations from the SDK for Java v1.x to 2.x.
- [Credentials provider changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-credentials.html): Learn about the changes in credentials providers between version 1.x and 2.x of the AWS SDK for Java.
- [Region changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-region.html): Learn about the changes in classes for Regions from SDK for Java v1.x to v2.x.

### [Operations, requests and responses changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-operation-requests-responses.html)

Learn about the changes in operations, requests, and responses from SDK for Java version 1 to version 2.

- [Date parameter changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-date-parameters.html): Learn how to convert Date objects to Instant objects when you upgrade from version 1 to version 2.
- [Binary data handling changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-binary-data.html): Learn how to work with SdkBytes objects instead of ByteBuffer objects when you upgrade from version 1 to version 2.
- [Timeout parameter changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-timeout-parameters.html): Learn how to convert numeric timeout values to Duration objects when you upgrade from version 1 to version 2.
- [Streaming operation differences](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-streaming-ops.html): Learn about streaming operation differences between AWS SDK for Java 1.x and 2.x, including changes to Amazon S3 getObject and putObject methods for non-blocking I/O support.
- [Serialization differences](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-serialization-changes.html): Learn about the differences in object serialization between versions 1.x and 2.x of the AWS SDK for Java.
- [Deserialization differences](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-deserialization-changes.html): Learn about the differences in JSON deserialization between AWS SDK for Java v1 and v2, focusing on how empty collections are handled in API responses.
- [Exception changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-exception-changes.html): Learn about the changes in Exception classes from version 1.x of the SDK for Java to version 2.x.
- [Service-specific changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-service-changes.html): Learn about the changes of specific services between versions 1.x and 2.x of the AWS SDK for Java.

### [Working with Amazon S3](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3.html)

Learn about the changes in Amazon S3 from version 1 to version 2 of the AWS SDK for Java 2.x.

- [S3 client differences](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-client.html): Learn about the differences between S3 client methods in version 1 and version 2 of the AWS SDK for Java.
- [Transfer Manager](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-transfer-manager.html): Learn how to migrate from the v1 Transfer Manager to the v2 S3 Transfer Manager, including client constructors, methods, model objects, and configuration changes.
- [S3 URI parsing](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-uri-parser.html): Learn about the changes in parsing Amazon S3 URIs from version 1 to version 2 in the AWS SDK for Java.
- [S3 Event Notifications](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-event-notification.html): Learn about the changes in theS3 Event Notifications API from version 1 to version 2 in the AWS SDK for Java.
- [Profile file changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-profile-file.html): Learn about the differences in how profiles in the shared config and credentials files are handled between the SDK for Java v1.x and v2.x.
- [External configuration](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-env-and-system-props.html): View the differences in environment variables and system properties between the SDK for Java v1.x and v2.x.
- [Waiters](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-waiters.html): Learn about the changes in Waiter classes from version 1 to version 2 in the AWS SDK for Java.
- [EC2 metadata utility](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-imds.html): Learn about the changes in the EC2 metadata utility from version 1 to version 2 in the AWS SDK for Java.
- [CloudFront presigning](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-cloudfront-presigning.html): Learn about the changes in the Amazon CloudFront from version 1 to version 2 in the AWS SDK for Java.
- [IAM Policy Builder API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-iam-policy-builder.html): Learn about the changes in the IAM Policy Builder API from version 1 to version 2 in the AWS SDK for Java.

### [Working with DynamoDB](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-ddb-mapper.html)

Learn about the changes in the DynamoDB mapping and document APIs from version 1 to version 2 in the AWS SDK for Java.

### [DynamoDB mapping APIs](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-mapping.html)

Explore the significant changes in DynamoDB mapping APIs from version 1 to version 2 of the AWS SDK for Java.

- [High-level changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-high-level.html): Learn the key differences between DynamoDBMapper in version 1 and DynamoDB Enhanced Client in version 2 of the SDK for Java.
- [API changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-api-changes.html): Compare the DynamoDB mapping API methods and client creation between version 1 and version 2 of the SDK for Java.
- [String handling](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migration-string-handling.html): Understand how empty string handling differs between version 1 and version 2 of the DynamoDB mapping APIs of the SDK for Java.
- [Optimistic locking](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migrate-optimstic-locking.html): Compare optimistic locking implementation between version 1 and version 2 of the DynamoDB mapping APIs of the SDK for Java.
- [Fluent setters](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migrate-fluent-setters.html): Learn about fluent setter compatibility differences between version 1 and version 2 of the in the DynamoDB mapping APIs of SDK for Java.

### [Document API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-mapping-document-api.html)

Compare the Document API features between version 1 and version 2 of the SDK for Java.

- [V1 Xpec API to V2 Expressions API](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-v1-xspec-migrate.html): Migrate from the V1 Expression Specification API to the V2 Expression API for DynamoDB.
- [Encryption library migration](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-encryption-lib-migrate.html): Find guidance for migrating the DynamoDB encryption library to work with version 2 of the SDK for Java.
- [SQS automatic request batching](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-sqs-auto-batching.html): Learn about the changes in automatic Amazon SQS request batching between SDK for Java version 1 and version 2, including differences in configuration, usage, and asynchronous handling.
- [Use the SDK for Java 1.x and 2.x side-by-side](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-side-by-side.html): Describes how to use the AWS SDK for Java 1.x and 2.x side-by-side.
- [Find applications using 1.x clients](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-find-apps-using-v1.html): Identify applications using AWS SDK for Java 1.x clients by querying AWS CloudTrail events before migrating to version 2.


## [Security](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/security.html)

- [Data protection](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/security-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in the AWS SDK for Java.
- [Transport Layer Security (TLS)](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/security-java-tls.html): Learn how the AWS shared responsibility model applies to using TLS security in the SDK for Java.
- [Identity and Access Management](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/security-iam.html): How to authenticate requests and manage access to your AWS resources.
- [Compliance Validation](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/compliance-validation.html): Provides information about compliance validation for this AWS product or service.
- [Resilience](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/disaster-recovery-resiliency.html): Provides information about resilience for this AWS Product or Service.
- [Infrastructure Security](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/infrastructure-security.html): Provides information about infrastructure security for this AWS product or service.
