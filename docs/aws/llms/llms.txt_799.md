# Source: https://docs.aws.amazon.com/sns/latest/dg/llms.txt

# Amazon Simple Notification Service Developer Guide

> Coordinate and manage the delivery or sending of messages to subscribing endpoints or clients using Amazon SNS. A concise overview of Amazon Simple Notification Service (Amazon SNS) concepts and programming information.

- [Message archiving and analytics](https://docs.aws.amazon.com/sns/latest/dg/message-archiving-and-analytics.html)
- [Amazon SNS documentation history](https://docs.aws.amazon.com/sns/latest/dg/sns-release-notes.html)

## [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

- [Amazon SNS features and capabilities](https://docs.aws.amazon.com/sns/latest/dg/welcome-features.html): Discover how Amazon SNS enhances messaging through features like application-to-application and application-to-person notifications, FIFO and standard topics, and message durability strategies.
- [Commonly shared services](https://docs.aws.amazon.com/sns/latest/dg/welcome-related.html): Learn how Amazon SQS supports Amazon SNS with dead-letter queues and topic subscriptions, how Lambda can be triggered by Amazon SNS messages, how IAM secures access to Amazon SNS resources, and how CloudFront can automate Amazon SNS resource setups.
- [Working with AWS SDKs](https://docs.aws.amazon.com/sns/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Create a topic and publish messages](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)

- [Setting up](https://docs.aws.amazon.com/sns/latest/dg/sns-setting-up.html): Learn what you need to do to start working with Amazon SNS.
- [Step 1: Creating a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html): Provides comprehensive instructions on creating an Amazon SNS topic using the AWS Management Console or AWS SDKs, detailing the steps for selecting topic types, naming conventions, enabling encryption, and setting permissions.
- [Step 2: Creating a subscription to a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html): Learn how to subscribe an endpoint to an Amazon SNS topic using the AWS Management Console, detailing the selection of a topic ARN, choosing an endpoint type (such as HTTP/HTTPS, email, Amazon SQS, or Lambda), and optionally configure settings such as raw message delivery, filter policies, and dead-letter queues.

### [Step 3: Publishing a message](https://docs.aws.amazon.com/sns/latest/dg/sns-publishing.html)

Learn how to publish messages to an Amazon SNS topic using both the AWS Management Console and AWS SDK.

### [Large message payloads](https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html)

Learn how to publish large Amazon SNS messages exceeding 256 KB by using the Amazon SNS Extended Client Libraries for Java and Python.

- [Amazon SNS Extended Client Library for Java](https://docs.aws.amazon.com/sns/latest/dg/extended-client-library-java.html): Learn how to use the Amazon SNS Extended Client Library for Java to publish large messages that exceed the standard size limit by storing the message payloads in Amazon S3.
- [Amazon SNS Extended Client Library for Python](https://docs.aws.amazon.com/sns/latest/dg/extended-client-library-python.html): Learn how both Amazon SNS and Amazon SQS use the Payload Offloading Java Common Library for AWS to handle message payloads stored in Amazon S3, enabling Java-enabled endpoints to access these payloads.
- [Message attributes](https://docs.aws.amazon.com/sns/latest/dg/sns-message-attributes.html): Learn how Amazon SNS message attributes allow you to attach structured metadata to messages, such as timestamps or geospatial data, which can be used for filtering and processing decisions. this topic also discusses the limitations and data types supported for message attributes, including the maximum number of attributes allowed and reserved attributes for mobile push notifications.
- [Message batching](https://docs.aws.amazon.com/sns/latest/dg/sns-batch-api-actions.html): Learn to use SNS's PublishBatch API to send up to 10 messages in a single API request, reducing costs and improving efficiency compared to sending individual messages.
- [Step 4: Deleting a subscription and topic](https://docs.aws.amazon.com/sns/latest/dg/sns-delete-subscription-topic.html): Explains the process of deleting an Amazon SNS topic and its associated subscriptions, highlighting that subscriptions are deleted asynchronously and become disassociated from the topic, even if a new topic with the same name is created.
- [Next steps](https://docs.aws.amazon.com/sns/latest/dg/sns-next-steps-getting-started.html): Provides next steps after setting up an Amazon SNS topic and subscription, such as exploring the AWS Developer Center, learning about data protection, enabling server-side encryption for topics, and subscribing AWS Event Fork Pipelines to a topic.


## [Message ordering and deduplication using FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html)

- [High throughput FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/fifo-high-throughput.html): Learn how high throughput FIFO topics in Amazon SNS efficiently manage high message volumes while maintaining strict order.
- [FIFO topic use case](https://docs.aws.amazon.com/sns/latest/dg/fifo-example-use-case.html): Highlights an example of an ecommerce platform created by an auto parts manufacturer using Amazon SNS FIFO topics and Amazon SQS queues, showing how different serverless applications, such as price management, wholesale, retail, and analytics, leverage these services for ordered message delivery and deduplication.
- [Message ordering details](https://docs.aws.amazon.com/sns/latest/dg/fifo-topic-message-ordering.html): Learn how Amazon SNS FIFO topics ensure strict message ordering and deduplication when delivering messages to Amazon SQS FIFO queues, maintaining the sequence in which messages are published.
- [Message grouping](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-grouping.html): Learn how Amazon SNS FIFO topics use message grouping to ensure that messages within the same group are processed in a strict, predetermined order.
- [Message delivery](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-delivery.html): Learn how Amazon SNS FIFO topics manage message delivery, emphasizing the flexibility and control it offers for integrating distributed applications that require real-time data consistency.
- [Message filtering](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-filtering.html): Learn how Amazon SNS FIFO topics utilize message filtering to enhance the efficiency and specificity of message delivery to different subscriber systems.
- [Message deduplication](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-dedup.html): Learn about the deduplication features of Amazon SNS FIFO topics which ensure messages are delivered exactly once by utilizing deduplication IDs.
- [Message security](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-security.html): Learn about the security features available for Amazon SNS and Amazon SQS FIFO topics and queues, focusing on encryption and privacy enhancements.
- [Message durability](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-durability.html): Learn about the robust durability and error handling features of Amazon SNS FIFO topics and Amazon SQS queues, including their ability to store messages across multiple Availability Zones and utilize dead-letter queues to manage message delivery failures.

### [Message archiving and replay](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-archiving-replay.html)

Learn about the functionalities of Amazon SNS FIFO topics related to message archiving and replay.

- [For topic owners](https://docs.aws.amazon.com/sns/latest/dg/message-archiving-and-replay-topic-owner.html): Learn how Amazon SNS FIFO topic owners can set up message archiving to store messages for a duration ranging from one day to a maximum of 365 days.
- [For topic subscribers](https://docs.aws.amazon.com/sns/latest/dg/message-archiving-and-replay-subscriber.html): Learn how the ReplayPolicy in Amazon SNS subscriptions can control message replay behavior by specifying or omitting an EndingPoint, allowing for either continuous message processing or temporary suspension of the subscription.
- [Code examples](https://docs.aws.amazon.com/sns/latest/dg/fifo-topic-code-examples.html): Provides code examples for integrating Amazon SNS FIFO topics with Amazon SQS FIFO and standard queues, demonstrating how to set up an auto parts price management system.


## [Message filtering](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html)

- [Subscription filter policy scope](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering-scope.html): Learn how the FilterPolicyScope attribute in Amazon SNS subscriptions allows you to set the scope of filtering either to MessageAttributes (default) or MessageBody, determining whether the filter policy is applied to the message's attributes or its content.

### [Subscription filter policies](https://docs.aws.amazon.com/sns/latest/dg/sns-subscription-filter-policies.html)

Learn how Amazon SNS subscription filter policies enable you to specify properties and values for filtering messages.

- [Amazon SNS example filter policies](https://docs.aws.amazon.com/sns/latest/dg/example-filter-policies.html): Learn how to use example filter policies with Amazon SNS to selectively accept or reject messages based on specific attributes or message content.
- [Filter policy constraints](https://docs.aws.amazon.com/sns/latest/dg/subscription-filter-policy-constraints.html): Learn how to create and apply filter policies for Amazon SNS subscriptions.
- [AND/OR logic](https://docs.aws.amazon.com/sns/latest/dg/and-or-logic.html): Learn how to use AND/OR logic in Amazon SNS filter policies to match message attributes or body properties based on complex conditions.
- [Key matching](https://docs.aws.amazon.com/sns/latest/dg/attribute-key-matching.html): Learn how to use the exists operator in Amazon SNS filter policies to match incoming messages based on the presence or absence of specific properties.
- [Numeric value matching](https://docs.aws.amazon.com/sns/latest/dg/numeric-value-matching.html): Learn how to filter messages in Amazon SNS by matching numeric values within message attributes or message body properties.
- [String value matching](https://docs.aws.amazon.com/sns/latest/dg/string-value-matching.html): Discover how to use string value matching in Amazon SNS filter policies to precisely filter messages based on exact matches, case-insensitive matches, prefixes, suffixes, and exclusions.
- [Applying a subscription filter policy](https://docs.aws.amazon.com/sns/latest/dg/message-filtering-apply.html): Learn how to configure filter policies in Amazon SNS so you can optimize message distribution for your applications, and enhance efficiency and relevance for subscribers.
- [Removing a subscription filter policy](https://docs.aws.amazon.com/sns/latest/dg/message-filtering-policy-remove.html): Discover how to remove a subscription filter policy in Amazon SNS by overwriting the existing policy with an empty JSON body.


## [Message data protection](https://docs.aws.amazon.com/sns/latest/dg/message-data-protection.html)

### [Data protection policies](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-policies.html)

Learn how data protection policies in Amazon SNS are structured to safeguard sensitive data, using predefined or custom data identifiers to audit, mask, redact, or block sensitive information during message transmission.

- [Data protection policy operations](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-operations.html): Learn how to use audit, de-identify and deny operations in your data protection policies.
- [Data protection policy examples](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-examples.html): Learn about various example data protection policies you can implement in Amazon SNS to handle sensitive data securely.

### [Creating data protection policies](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure.html)

Create Amazon SNS data protection policies to secure sensitive data.

- [Using API](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-api.html): Learn how to create Amazon SNS data protection policies using the AWS API, including how to set up a policy when creating a new Amazon SNS topic or modify it for an existing topic.
- [Using AWS CLI](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-cli.html): Learn how to use the AWS Command Line Interface to create data protection policies for Amazon SNS topics.
- [Using CloudFormation](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-cfn.html): Learn how to use CloudFormation to create data protection policies for Amazon SNS topics, emphasizing that you can define a data protection policy alongside a new Amazon SNS topic using the AWS::SNS::Topic resource.
- [Using the AWS Management Console](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-console.html): Learn how to create data protection policies for Amazon SNS topics using the AWS Management Console.
- [Using AWS SDK](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-sdk.html): Learn how to create and manage Amazon SNS data protection policies using the AWS SDK, including code examples for creating a new data protection policy with a topic, as well as retrieving and updating existing policies.
- [Deleting data protection policies](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-delete.html): Learn how to delete Amazon SNS data protection policies using various methods, including the AWS API, CLI, CloudFormation, and the AWS Management Console.

### [Data identifiers](https://docs.aws.amazon.com/sns/latest/dg/data-identifiers.html)

Learn how to use data protection policies and data identifiers to audit and block sensitive data in Amazon SNS.

### [Managed data identifiers](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-managed-data-identifiers.html)

Learn how Amazon SNS uses managed data identifiers to detect various types of sensitive data, such as credentials, financial information, health data, and personally identifiable information (PII).

- [Sensitive data types: Credentials](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-credentials.html): Learn about the types of credentials that Amazon SNS can detect using managed data identifiers.
- [Sensitive data types: Devices](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-devices.html): Learn about the types of device identifiers that Amazon SNS can detect using managed data identifiers.
- [Sensitive data types: Financial](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-financial.html): Learn about the types of financial information that Amazon SNS can detect using managed data identifiers.
- [Sensitive data types: Protected health information (PHI)](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-phi.html): Learn about the types of sensitive protected health information (PHI) data that Amazon SNS can detect using managed data identifiers.
- [Sensitive data types: Personally identifiable information (PII)](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-pii.html): Learn about the types of sensitive personally identifiable information (PII) data that Amazon SNS can detect using managed data identifiers.
- [Custom data identifiers](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-custom-data-identifiers.html): Learn how to use custom data identifiers (CDIs) in Amazon SNS to create data protection policies tailored to detect specific patterns, such as company-specific identifiers, by defining custom regular expressions.


## [Message delivery](https://docs.aws.amazon.com/sns/latest/dg/message-delivery.html)

- [Raw message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html): Learn how to enable raw message delivery in Amazon SNS, which strips metadata and sends messages without JSON formatting to Amazon SQS, , and HTTP/S endpoints.
- [Cross-account delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-send-message-to-sqs-cross-account.html): Learn how to publish a notification to an Amazon SNS topic with subscriptions to Amazon SQS queues in another account.
- [Cross-region delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-cross-region-delivery.html): Learn how Amazon SNS supports cross-region delivery of messages to Amazon SQS queues and Lambda functions, including specific instructions on adjusting service principals in resource policies when dealing with opt-in regions.

### [Message delivery status](https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html)

Learn about how Amazon SNS logs the delivery status of notifications sent to various endpoints, such as HTTP, Amazon SQS, and Lambda, by using Amazon CloudWatch Logs for better operational insights.

- [Prerequisites for delivery status logging](https://docs.aws.amazon.com/sns/latest/dg/topics-attrib-prereq.html): Learn about the IAM permissions required for enabling Amazon SNS delivery status logging to CloudWatch Logs and details the default log group naming convention used for storing logs.
- [Configuring delivery status logging using the AWS Management Console](https://docs.aws.amazon.com/sns/latest/dg/topics-attrib.html): Learn how to configure delivery status logging in the Amazon SNS console, which allows you to track the success and failure of message deliveries to endpoints such as Lambda by setting up CloudWatch Logs.
- [Configuring delivery status logging using the AWS SDKs](https://docs.aws.amazon.com/sns/latest/dg/msg-status-sdk.html): Learn how to use the AWS SDKs to configure message delivery status logging for Amazon SNS, detailing the specific attributes used for logging delivery success and failure across different endpoints such as HTTP, Amazon Data Firehose, Lambda, platform application endpoints, and Amazon SQS.
- [AWS SDK examples to configure topic attributes](https://docs.aws.amazon.com/sns/latest/dg/topic-attributes-sdks.html): This topic provides an example of how to use the AWS CLI to set attributes for an Amazon SNS topic using the SetTopicAttributes command, specifically demonstrating how to assign a display name to a topic.
- [Configuring delivery status logging using CloudFormation](https://docs.aws.amazon.com/sns/latest/dg/msg-status-cloudformation.html): Learn how to use ACloudFormation to configure DeliveryStatusLogging for an Amazon SNS topic by creating a stack with a JSON or YAML template.
- [Message delivery retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html): Learn how Amazon SNS handles message delivery retries for different endpoints and outlines the delivery policies that define retry behavior, including immediate retry, pre-backoff, backoff, and post-backoff phases.

### [Dead-letter queues](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html)

Learn how to use dead-letter queues (DLQs) in Amazon SNS to manage messages that cannot be successfully delivered to their subscribers.

- [Configuring a dead-letter queue](https://docs.aws.amazon.com/sns/latest/dg/sns-configure-dead-letter-queue.html): Learn how to configure a dead-letter queue for an Amazon SNS subscription using various AWS services.


## [Resource management and optimization](https://docs.aws.amazon.com/sns/latest/dg/sns-resource-management-optimization.html)

### [Tagging](https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html)

Learn how Amazon SNS topic tagging can be used to enhance cost management, access control, and resource organization by assigning tags to topics.

- [Configuring tags](https://docs.aws.amazon.com/sns/latest/dg/sns-tags-configuring.html): Explains how to configure tags for an Amazon SNS topic using the AWS Management Console, AWS SDK, and AWS CLI, emphasizing that tags should not contain personally identifiable information (PII) or sensitive data.


## [Amazon SNS event sources and destinations](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-and-destinations.html)

### [Event sources](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources.html)

Provides an overview of AWS services that can publish events to Amazon SNS topics, organized by AWS product categories, and explains the benefits of using each service with Amazon SNS.

- [Analytics](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-analytics.html): The following table describes how Amazon SNS integrates with AWS analytics services such as Athena, AWS Data Pipeline, and Amazon Redshift to provide real-time notifications for key events, including control limit breaches, pipeline status updates, and data warehouse activities.
- [Application integration](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-application-integration.html): The following table describes how Amazon SNS integrates with application integration services such as EventBridge and AWS Step Functions, enabling real-time data routing and notifications for business-critical applications.
- [Billing and cost management](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-billing-cost-management.html): The following table describes how AWS Billing and Cost Management integrates with Amazon SNS to provide notifications for budgets, price changes, and cost anomalies.
- [Business applications](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-business-applications.html): The following table describes how Amazon Chime integrates with Amazon SNS to send notifications for important meeting events, enabling you to stay informed about your communications and scheduling.
- [Compute](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-compute.html): The following table describes how Amazon SNS integrates with various AWS compute services, enabling you to receive notifications for key events such as Auto Scaling actions, EC2 Image Builder completions, Elastic Beanstalk environment changes, Lambda function outputs, and Lightsail metric thresholds.
- [Containers](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-containers.html): The following table describes how Amazon SNS integrates with AWS container services such as Amazon EKS Distro and Amazon ECS, allowing you to track updates and security patches for Amazon EKS clusters and receive notifications for new ECS-optimized AMI releases.
- [Customer engagement](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-customer-engagement.html): The following table describes how Amazon SNS enhances customer engagement services by integrating with Amazon Connect, AWS End User Messaging SMS, and Amazon Simple Email Service (SES), enabling you to receive alerts and validations, configure two-way SMS messaging, and monitor email notifications for bounces, complaints, and deliveries.
- [Database](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-database.html): The following table describes how Amazon SNS integrates with AWS database services such as AWS Database Migration Service (DMS), Amazon DynamoDB, Amazon ElastiCache, Amazon Neptune, Amazon Redshift, and Amazon Relational Database Service (RDS) to send notifications about important events such as data migrations, maintenance activities, cache updates, and database changes.
- [Developer tools](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-developer-tools.html): The following table describes how Amazon SNS integrates with AWS developer tools services, such as AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, Amazon CodeGuru, and AWS CodePipeline to provide notifications for critical events such as build status changes, repository updates, deployment progress, performance anomalies, and pipeline actions.
- [Front-end web & mobile](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-front-end-web-mobile.html): The following table describes how Amazon SNS integrates with AWS End User Messaging SMS to enhance customer engagement by sending emails, SMS, voice messages, and push notifications, including the ability to configure two-way SMS for receiving customer messages.
- [Game development](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-game-development.html): The following table describes how Amazon SNS integrates with Amazon GameLift Servers to provide notifications for matchmaking and queue events in session-based multiplayer game servers.
- [Internet of Things](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-iot.html): The following table descrives how Amazon SNS integrates with AWS IoT services, such as AWS IoT Core, AWS IoT Device Defender, AWS IoT Events, and AWS IoT Greengrass, to provide notifications for IoT events and alerts.
- [Machine learning](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-machine-learning.html): The following table describes how Amazon SNS integrates with AWS machine learning services, such as Amazon CodeGuru, Amazon DevOpsÂ Guru, Amazon Lookout for Metrics, Amazon Rekognition, and Amazon SageMaker AI, to provide notifications for anomalies, operational insights, and data labeling activities.
- [Management & governance](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-management-governance.html): The following table describes how Amazon SNS integrates with AWS management and governance services such as Amazon Q Developer in chat applications, CloudFormation, CloudTrail, CloudWatch, AWS Config, AWS Control Tower, AWS License Manager, AWS Service Catalog, and AWS Systems Manager, providing notifications for key events like infrastructure changes, compliance alerts, and operational insights.
- [Media](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-media.html): The following table describes how Amazon SNS integrates with Amazon Elastic Transcoder to send notifications when media transcoding jobs change status, enabling you to efficiently monitor and manage the conversion of media files stored in Amazon S3 into formats suitable for consumer playback devices.
- [Migration & transfer](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-migration-transfer.html): The following table describes how Amazon SNS integrates with AWS migration and transfer services, such as AWS Application Discovery Service, AWS Database Migration Service (DMS), and AWS Snowball Edge, to provide notifications for events like server data collection, database migration activities, and data transfer jobs.
- [Networking & content delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-networking-content-delivery.html): The following table describes how Amazon SNS integrates with AWS networking and content delivery services, such as Amazon API Gateway, Amazon CloudFront, Direct Connect, Elastic Load Balancing, Amazon Route 53, and Amazon VPC, to send notifications for events like API messages, CloudFront metric alarms, connection state changes, load balancer events, health check statuses, and VPC endpoint activities.
- [Security, identity, & compliance](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-security-identity-compliance.html): The following table describes how Amazon SNS integrates with AWS security, identity, and compliance services, such as Directory Service, Amazon GuardDuty, Amazon Inspector, and AWS Security Hub CSPM, to provide notifications for directory status changes, security findings, Inspector events, and security hub announcements.
- [Serverless](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-serverless.html): The following table describes how Amazon SNS integrates with services like Amazon DynamoDB, Amazon EventBridge, and Lambda to send notifications for key events such as maintenance updates, real-time data streams, and Lambda function outputs.
- [Storage](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-storage.html): The following table describes how Amazon SNS integrates with AWS storage services like AWS Backup, Amazon Elastic File System (EFS), Amazon Glacier, Amazon S3, and AWS Snowball Edge to provide notifications for various events such as backup activities, file system alarms, data retrieval jobs, bucket changes, and data transfer operations.
- [Additional event sources](https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-aws-wide.html): The following table describes how Amazon SNS can be used to receive timely notifications about AWS daily feature updates and changes to AWS IP address ranges, ensuring that you are informed about the latest AWS service releases, instance types, VPC endpoints, and public IP address changes.
- [Event destinations](https://docs.aws.amazon.com/sns/latest/dg/sns-event-destinations.html): Learn about Amazon SNS event destinations Learn how Amazon SNS delivers events to various destinations, categorized into application-to-application (A2A) messaging and application-to-person (A2P) notifications.


## [Application-to-application messaging](https://docs.aws.amazon.com/sns/latest/dg/sns-system-to-system-messaging.html)

### [Fanout to Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html)

Learn how to use Amazon SNS to fan out notifications to delivery streams, enabling the integration of Amazon SNS with various storage and analytics endpoints like Amazon S3, Amazon Redshift, and third-party services.

- [Prerequisites](https://docs.aws.amazon.com/sns/latest/dg/prereqs-kinesis-data-firehose.html): Learn about the prerequisites for subscribing delivery streams to Amazon SNS topics, including the necessary configurations for Amazon SNS topics, IAM roles, and permissions required to enable successful integration and message delivery.
- [Subscribing a delivery stream to a topic](https://docs.aws.amazon.com/sns/latest/dg/firehose-endpoints-subscribe.html): Learn the step-by-step process for subscribing an delivery stream to an Amazon SNS topic, including configuring the necessary settings such as topic ARN, protocol, and subscription role ARN.

### [Managing messages across multiple delivery stream destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-working-with-destinations.html)

Learn how to configure and work with various delivery stream destinations supported by , including Amazon S3, OpenSearch Service, Amazon Redshift, and HTTP endpoints.

### [Storing and analyzing messages in Amazon S3 destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-s3-destinations.html)

Learn about configuring delivery streams to publish data to Amazon S3, including the format of archived messages and methods for analyzing messages stored in Amazon S3 buckets.

- [Formatting notifications for storage in Amazon S3 destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-archived-message-format-S3.html): Learn about the structure and format of Amazon SNS notifications when they are archived to an Amazon S3 bucket, including how JSON metadata is added to each message when raw message delivery is disabled.
- [Analyzing messages stored in Amazon S3 using Athena](https://docs.aws.amazon.com/sns/latest/dg/firehose-message-analysis-s3.html): Learn learn how to analyze Amazon SNS messages that have been sent to Amazon S3 via delivery streams.

### [Integrating messages with Amazon OpenSearch Service destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-elasticsearch-destinations.html)

Learn about utilizing delivery streams to publish data from Amazon SNS topics directly to Amazon OpenSearch Service indices.

- [Archived message format](https://docs.aws.amazon.com/sns/latest/dg/firehose-archived-message-format-elasticsearch.html): Learn learn how Amazon SNS notifications are formatted and stored within Amazon OpenSearch Service indices when raw message delivery is disabled.
- [Analyzing messages](https://docs.aws.amazon.com/sns/latest/dg/firehose-message-analysis-elasticsearch.html): Learn how to configure and analyze Amazon SNS messages that are sent to Amazon OpenSearch Service destinations via .

### [Configuring message delivery and analysis in Amazon Redshift destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-redshift-destinations.html)

Learn how to configure to deliver Amazon SNS notifications to an Amazon Redshift cluster, enabling them to use SQL query tools to analyze messages stored in Amazon Redshift that meet specific criteria.

- [Structuring message archives in Amazon Redshift tables](https://docs.aws.amazon.com/sns/latest/dg/firehose-archive-table-structure-redshift.html): Learn how Amazon SNS messages are structured and archived in Amazon Redshift tables, including details on how JSON metadata is added when raw message delivery is disabled.
- [Analyzing messages stored in Amazon Redshift destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-message-analysis-redshift.html): Learn how to analyze Amazon SNS messages that have been sent to Amazon Redshift via delivery streams.

### [Configuring message delivery to HTTP destinations using](https://docs.aws.amazon.com/sns/latest/dg/firehose-http-destinations.html)

Learn how delivery streams can be used to publish data from Amazon SNS topics directly to HTTP endpoints, including details on the format of delivered messages.

- [Notification format for delivery to HTTP destinations](https://docs.aws.amazon.com/sns/latest/dg/firehose-delivered-message-format-http.html): Learn learn how Amazon SNS notifications are formatted and delivered to HTTP endpoints via delivery streams when raw message delivery is disabled.

### [Message archiving and analytics example use case](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-use-case.html)

Learn about a specific use case involving the archiving and analytics of Amazon SNS messages within an airline ticketing platform that requires compliance with data retention policies.

- [Setting-up initial AWS resources for message archiving and analytics](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-initial-resources.html): Learn how to set up the foundational AWS resources required for archiving and analyzing messages in an SNS-based application.
- [Setting-up a Firehose delivery stream for message archiving](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-create-delivery-stream.html): Learn the step-by-step process of setting up an delivery stream tailored for message archiving and analytics with Amazon S3 as the destination.
- [Subscribing the delivery stream to the topic](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-subscribe-delivery-stream-to-topic.html): Learn how to securely integrate Amazon SNS with by creating an IAM role and subscribing a Firehose delivery stream to an Amazon SNS topic.
- [Testing and querying a configuration for effective data management](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-test-and-query.html): Learn how to verify the setup of your Amazon SNS, Amazon SQS, Firehose, and Amazon S3 components by publishing and tracing a test message through the entire workflow.
- [Automating message archiving with an CloudFormation template](https://docs.aws.amazon.com/sns/latest/dg/firehose-example-cfn.html): Learn how to use an CloudFormation template to automate the deployment of a complex AWS setup for archiving and analyzing Amazon SNS messages.

### [Fanout to Lambda functions](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda-as-subscriber.html)

Learn how Amazon SNS integrates with Lambda to automatically trigger Lambda functions upon receiving Amazon SNS notifications, allowing for automated processing, manipulation, and forwarding of message payloads to other AWS services or Amazon SNS topics.

- [Prerequisites](https://docs.aws.amazon.com/sns/latest/dg/lambda-prereq.html): Learn the prerequisites for invoking Lambda functions using Amazon SNS notifications, including setting up a Lambda function and an Amazon SNS topic.
- [Subscribing a function to a topic](https://docs.aws.amazon.com/sns/latest/dg/lambda-console.html): Learn how to subscribe an Lambda function to an Amazon SNS topic by setting up the subscription in the Amazon SNS console, enabling automatic invocation of the Lambda function whenever a message is published to the topic.

### [Fanout to Amazon SQS queues](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

Learn how to integrate Amazon SNS with Amazon SQS to deliver time-sensitive messages to multiple subscribers via Amazon SNS while storing them in Amazon SQS queues for asynchronous processing.

- [Subscribing a queue to a topic](https://docs.aws.amazon.com/sns/latest/dg/subscribe-sqs-queue-to-sns-topic.html): Learn how to enable Amazon SNS to send messages to Amazon SQS by subscribing an Amazon SQS queue to an Amazon SNS topic.
- [Automate Amazon SNS to Amazon SQS messaging with AWS CloudFormation](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.cloudformation.html): Learn how to use an CloudFormation template to automate the creation and configuration of an Amazon SNS topic that sends messages to Amazon SQS queues, along with the necessary IAM users and permissions.

### [Fanout notifications to HTTPS endpoints](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html)

Learn how to use Amazon SNS to send notification messages to HTTP or HTTPS endpoints by subscribing these endpoints to an Amazon SNS topic, enabling the delivery of notifications via HTTP POST requests.

### [Subscribing an endpoint to a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-subscribe-https-s-endpoints-to-topic.html)

Learn how to subscribe HTTPS endpoints to Amazon SNS topics, including preparing the endpoint, confirming the subscription, setting delivery policies, and managing permissions for users to publish messages.

- [Make sure your endpoint is ready to process messages](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.prepare.html): Learn how to prepare an HTTP or HTTPS endpoint to process Amazon SNS messages.
- [Subscribe the HTTP/HTTPS endpoint to the topic](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.subscribe.html): Learn how to subscribe an HTTP or HTTPS endpoint to an Amazon SNS topic using the Amazon SNS console, ensuring that the endpoint is ready to handle confirmation and notification messages.
- [Confirm your subscription](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.confirm.html): Learn how to confirm an Amazon SNS subscription by utilizing the SubscribeURL provided in the confirmation message, either programmatically or manually, and how to verify the confirmation status through the AWS Management Console.
- [Set the delivery retry policy for the subscription](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.retry.html): Learn how to set the delivery policy for an Amazon SNS subscription, allowing you to customize the retry frequency and intervals for failed messages and specify the content type for HTTP/S notifications.
- [Give users permissions to publish to the topic](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.iam.permissions.html): Learn how to grant permission for users or applications to publish to an Amazon SNS topic by configuring AWS Identity and Access Management (IAM) policies.
- [Send messages to the HTTP/HTTPS endpoint](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.publish.html): You can send a message to a topic's subscriptions by publishing to the topic.

### [Verifying message signatures](https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message.html)

Learn how to confirm the authenticity of a message sent to your HTTP endpoint by Amazon SNS by verifying its signature.

- [Configuring the message signature version](https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message-configure-message-signature.html): Learn how to enhance the security and compatibility of your Amazon SNS message verification process by configuring the message signature version.
- [Verifying the signature of an Amazon SNS message](https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message-verify-message-signature.html): Learn how to verify the authenticity and integrity of Amazon SNS messages received via HTTP query-based requests.

### [Parsing message formats](https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html)

Learn about the message formats used by Amazon SNS when communicating with HTTP and HTTPS endpoints.

- [HTTP/HTTPS headers](https://docs.aws.amazon.com/sns/latest/dg/http-header.html): Learn how Amazon SNS uses specific HTTP/HTTPS headers in its POST messages to deliver subscription confirmations, notifications, and unsubscribe confirmations to endpoints.
- [HTTP/HTTPS subscription confirmation JSON format](https://docs.aws.amazon.com/sns/latest/dg/http-subscription-confirmation-json.html): Learn how Amazon SNS sends subscription confirmation messages to HTTP/HTTPS endpoints and how to interpret the key elements of the JSON document, such as the SubscribeURL and signature.
- [HTTP/HTTPS notification JSON format](https://docs.aws.amazon.com/sns/latest/dg/http-notification-json.html): Learn about the structure and components of the JSON format used by Amazon SNS when sending notifications to HTTP/HTTPS endpoints.
- [HTTP/HTTPS unsubscribe confirmation JSON format](https://docs.aws.amazon.com/sns/latest/dg/http-unsubscribe-confirmation-json.html): Learn about the structure of an unsubscribe confirmation message sent by Amazon SNS to an HTTP/HTTPS endpoint, including the essential elements such as the message type, unique identifiers, and signature details.
- [SetSubscriptionAttributes delivery policy JSON format](https://docs.aws.amazon.com/sns/latest/dg/set-sub-attributes-delivery-policy-json.html): Learn how to configure the delivery policy for Amazon SNS subscriptions using the SetSubscriptionAttributes action, including the required JSON format for setting retry policies, throttle policies, and content-type headers.
- [SetTopicAttributes delivery policy JSON format](https://docs.aws.amazon.com/sns/latest/dg/set-topic-attributes-delivery-policy-json.html): Learn how to configure delivery policies for Amazon SNS topics using the SetTopicAttributes action, including specifying JSON formats for retry strategies, throttling limits, and request policies.

### [Fanout events to AWS Event Fork Pipelines](https://docs.aws.amazon.com/sns/latest/dg/sns-fork-pipeline-as-subscriber.html)

Learn how to integrate Amazon SNS with AWS Event Fork Pipelines to efficiently manage event-driven applications, leveraging the native integration with Data Firehose for event archiving, analytics, and processing.

### [Deploying and testing the event fork pipelines sample application](https://docs.aws.amazon.com/sns/latest/dg/sns-deploy-test-fork-pipelines-sample-application.html)

Learn how to deploy and test the AWS Event Fork Pipelines sample application using the AWS Management Console, including steps for deployment, execution, and verification.

- [AWS Event Fork Pipelines use case example](https://docs.aws.amazon.com/sns/latest/dg/example-sns-fork-use-case.html): Learn how an e-commerce application uses AWS Event Fork Pipelines to enhance an event-driven, serverless architecture.
- [Deploying the sample application](https://docs.aws.amazon.com/sns/latest/dg/deploy-sample-application.html): Learn how to deploy a sample e-commerce checkout application using the Lambda console and the AWS Serverless Application Repository.
- [Executing the SNS-linked sample application](https://docs.aws.amazon.com/sns/latest/dg/execute-sample-application.html): Learn how to execute a sample application hosted on AWS, detailing steps to access and run an API endpoint in the Lambda console, including how to send a test JSON event to this API.
- [Verifying application and pipeline performance](https://docs.aws.amazon.com/sns/latest/dg/verify-sample-application-pipelines.html): Learn to validate the correct functioning of a sample AWS application and its associated pipelines.
- [Simulating an issue and replay events for recovery](https://docs.aws.amazon.com/sns/latest/dg/simulate-issue-replay-events-for-recovery.html): Learn how to simulate data corruption within a serverless application using Lambda and Amazon DynamoDB, enabling them to test recovery processes by replaying events from an Amazon SQS queue to restore data integrity.

### [Subscribing an event pipeline to a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-subscribe-event-fork-pipelines.html)

Learn how to deploy AWS Event Fork Pipelines and subscribe them to an Amazon SNS topic using the AWS Management Console, providing guidance on deploying different pipelines such as event storage, search and analytics, and event replay.

- [Deploying and subscribing the Event Storage and Backup Pipeline](https://docs.aws.amazon.com/sns/latest/dg/deploy-event-storage-backup-pipeline.html): Learn how to deploy and subscribe the Event Storage and Backup Pipeline to an Amazon SNS topic, enabling automated storage of Amazon SNS messages in an Amazon S3 bucket and archiving for analytics.
- [Deploying and subscribing the Event Search and Analytics Pipeline](https://docs.aws.amazon.com/sns/latest/dg/deploy-event-search-analytics-pipeline.html): Learn how to deploy the Event Storage and Backup Pipeline and subscribe it to an Amazon SNS topic, allowing for seamless integration with for event archiving and analytics.
- [Deploying the Event Replay Pipeline with Amazon SNS integration](https://docs.aws.amazon.com/sns/latest/dg/deploy-event-replay-pipeline.html): Learn how to deploy the Event Replay Pipeline and subscribe it to an Amazon SNS topic.
- [Using EventBridge Scheduler](https://docs.aws.amazon.com/sns/latest/dg/using-eventbridge-scheduler.html): Learn how to use Amazon EventBridge Scheduler to automate the publishing of messages from an Amazon SNS topic on a scheduled basis.


## [Application-to-person messaging](https://docs.aws.amazon.com/sns/latest/dg/sns-user-notifications.html)

### [Mobile text messaging](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-phone-number-as-subscriber.html)

Learn how to effectively use Amazon SNS for sending SMS messages, including how to manage SMS preferences, ensure compliance with regional regulations, and optimize message delivery for different scenarios.

### [Getting started](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-phone-number-getting-started.html)

Learn how to get started with Amazon SNS SMS, including setting up SMS accounts, managing phone numbers in the sandbox, creating origination numbers and sender IDs, and registering their company.

### [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html)

Learn how to manage your Amazon SNS SMS sandbox, including adding, verifying, and deleting phone numbers, troubleshooting OTP delivery issues, and moving your account out of the SMS sandbox.

- [Adding and verifying phone numbers](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-verifying-phone-numbers.html): Learn how to add and verify phone numbers in the Amazon SNS SMS sandbox, including creating an origination identity and troubleshooting common issues that may prevent OTP text delivery.
- [Deleting phone numbers](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-deleting-phone-numbers.html): Learn how to delete pending or verified phone numbers from the Amazon SNS SMS sandbox, including understanding the required waiting period and the step-by-step process for removing numbers from their account across multiple regions.
- [Moving out of the Amazon SNS SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-moving-to-production.html): Learn how to move your AWS account out of the Amazon SNS SMS sandbox, including the steps to verify phone numbers, test SMS messaging, and submit a support request to AWS.
- [Origination identities](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-originating-identities.html): Learn about the different types of origination identities available for sending SMS messages using Amazon SNS, including sender IDs and origination numbers.

### [Configurations](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-configurations.html)

Learn how to configure and manage SMS messaging in Amazon SNS.

- [Sending SMS messages](https://docs.aws.amazon.com/sns/latest/dg/sms_sending-overview.html): Learn how to send SMS messages using Amazon SNS, including publishing to a topic, subscribing phone numbers to topics, setting attributes on messages, and publishing directly to mobile phones.
- [Setting SMS preferences](https://docs.aws.amazon.com/sns/latest/dg/sms_preferences.html): Learn how to customize your SMS messaging preferences using Amazon SNS, including options like specifying default message types, setting spending limits, defining sender IDs, and configuring usage reports.
- [Managing SMS subscriptions](https://docs.aws.amazon.com/sns/latest/dg/sms_manage.html): Manage who receives SMS messages from your account.

### [Monitoring SMS activity](https://docs.aws.amazon.com/sns/latest/dg/sms_stats.html)

Learn how to monitor SMS activity and send daily SMS usage reports with Amazon SNS.

- [Viewing delivery statistics](https://docs.aws.amazon.com/sns/latest/dg/sms_stats_console.html): View SMS delivery statistics in the Amazon SNS console.
- [Viewing CloudWatch metrics and logs](https://docs.aws.amazon.com/sns/latest/dg/sms_stats_cloudwatch.html): Learn how to use Amazon CloudWatch and Amazon CloudWatch Logs to monitor SMS message deliveries sent through Amazon SNS.
- [Subscribing to daily SMS usage reports](https://docs.aws.amazon.com/sns/latest/dg/sms_stats_usage.html): Subscribe to daily SMS usage reports from Amazon SNS.

### [Requesting SMS support](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-awssupport.html)

Contact Support to request an SMS spending threshold increase, a move from the SMS sandbox, a dedicated origination number, or a sender ID.

- [Requesting spending quota increases](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-awssupport-spend-threshold.html): Learn how to increase your monthly SMS spending quota and move your AWS account out of the SMS sandbox by following specific steps outlined for interacting with Support.
- [Best practices for SMS messaging](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-best-practices.html): Discover best practices for sending SMS messages, including compliance with legal requirements, maintaining customer engagement, and optimizing message content to avoid penalties and ensure effective communication.

### [Sending mobile push notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html)

Learn how to use Amazon SNS to send push notifications to mobile apps, including the process of setting up credentials, creating platform applications, and publishing messages to mobile devices through various push notification services.

### [Setting up a mobile app](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send.html)

Learn about the process of setting up mobile applications using the AWS Management Console, covering prerequisites, platform application creation, and endpoint management.

- [Prerequisites](https://docs.aws.amazon.com/sns/latest/dg/sns-prerequisites-for-mobile-push-notifications.html): To begin using Amazon SNS mobile push notifications, you'll need the following:
- [Creating a platform application](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-register.html): Register your mobile app with AWS so that you can use Amazon SNS to send notification messages to mobile endpoints.
- [Setting up a platform endpoint](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html): Learn about the process of creating a platform endpoint in Amazon SNS, which involves registering a mobile app's device token with Amazon SNS to enable direct push notification messages to the app.
- [Integrating device tokens for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-devicetoken.html): Learn how to add device tokens or registration IDs to Amazon SNS for mobile push notifications, including manual methods, bulk uploads, and registering future app installations, ensuring that messages are sent to the correct mobile endpoints.
- [Apple authentication methods](https://docs.aws.amazon.com/sns/latest/dg/sns-apple-authentication-methods.html): Learn how to authenticate Amazon SNS to send push notifications to iOS or macOS apps using either a signing key or a TLS certificate from your Apple Developer account, including detailed instructions for both methods.
- [FCM authentication methods](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-authentication-methods.html): Learn how to how to authenticate Amazon SNS to send push notifications through Firebase Cloud Messaging (FCM) by obtaining and managing API keys or tokens.
- [FCM endpoint management](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-endpoint-management.html): Learn how to manage Firebase Cloud Messaging (FCM) device tokens in Amazon SNS, including detecting invalid tokens, removing stale tokens, and maintaining up-to-date device tokens for consistent push notification delivery.

### [Using Amazon SNS for mobile push notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-notifications.html)

Learn how to use Amazon SNS for sending mobile push notifications, including publishing messages to topics subscribed by mobile endpoints and directly sending notifications to individual mobile devices.

### [Publishing notifications with platform-specific payloads](https://docs.aws.amazon.com/sns/latest/dg/sns-send-custom-platform-specific-payloads-mobile-devices.html)

Learn learn how to send platform-specific push notification messages to mobile devices using Amazon SNS, including formatting JSON payloads, sending messages to multiple platforms, and specifying APNs header values for alert or background notifications.

- [FCM v1 API payloads](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-v1-payloads.html): Learn how to use Google Firebase Cloud Messaging (FCM) v1 API with Amazon SNS to send notifications to Android, iOS, and Webpush destinations, including details on constructing payloads, potential risks, and handling delivery failure events.
- [Mobile app attributes](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html): Configure and monitor the delivery status of push notification messages sent through Amazon SNS to mobile endpoints.
- [Mobile app events](https://docs.aws.amazon.com/sns/latest/dg/application-event-notifications.html): Learn how to set up and manage event notifications for mobile applications using Amazon SNS.
- [Mobile push API actions](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-api.html): Provides an overview of the Amazon SNS mobile push API actions, detailing how to create platform applications, endpoints, and topics, as well as how to manage and delete these resources to send notifications to mobile devices via services such as APNs and FCM.
- [Common mobile push API errors](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-api-error.html): Provides a detailed list of potential errors you may encounter when using Amazon SNS mobile push APIs, along with descriptions and corresponding HTTPS status codes.
- [Mobile push TTL](https://docs.aws.amazon.com/sns/latest/dg/sns-ttl.html): Learn how to use the Time To Live (TTL) message attribute in Amazon SNS for mobile push notifications.
- [Supported Regions](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-push-supported-regions.html): Provides a list of AWS Regions where you can create and manage mobile applications using Amazon SNS, covering regions across the Americas, Europe, Asia Pacific, the Middle East, and Africa.
- [Best practices for mobile push notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-notifications-best-practices.html): Provides best practices for managing mobile push notifications with Amazon SNS, including strategies for endpoint management, enabling delivery status logging, and using event notifications to improve customer engagement and troubleshoot delivery issues.
- [Email subscription setup and management](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html): Learn how to subscribe an email address to an Amazon SNS topic using the AWS Management Console or AWS SDKs.


## [Code examples](https://docs.aws.amazon.com/sns/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/sns/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon SNS with AWS SDKs.

- [Hello Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/example_sns_Hello_section.html): Hello Amazon SNS

### [Actions](https://docs.aws.amazon.com/sns/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Amazon SNS with AWS SDKs.

- [CheckIfPhoneNumberIsOptedOut](https://docs.aws.amazon.com/sns/latest/dg/example_sns_CheckIfPhoneNumberIsOptedOut_section.html): Use CheckIfPhoneNumberIsOptedOut with an AWS SDK or CLI
- [ConfirmSubscription](https://docs.aws.amazon.com/sns/latest/dg/example_sns_ConfirmSubscription_section.html): Use ConfirmSubscription with an AWS SDK or CLI
- [CreateTopic](https://docs.aws.amazon.com/sns/latest/dg/example_sns_CreateTopic_section.html): Use CreateTopic with an AWS SDK or CLI
- [DeleteTopic](https://docs.aws.amazon.com/sns/latest/dg/example_sns_DeleteTopic_section.html): Use DeleteTopic with an AWS SDK or CLI
- [GetSMSAttributes](https://docs.aws.amazon.com/sns/latest/dg/example_sns_GetSMSAttributes_section.html): Use GetSMSAttributes with an AWS SDK or CLI
- [GetTopicAttributes](https://docs.aws.amazon.com/sns/latest/dg/example_sns_GetTopicAttributes_section.html): Use GetTopicAttributes with an AWS SDK or CLI
- [ListPhoneNumbersOptedOut](https://docs.aws.amazon.com/sns/latest/dg/example_sns_ListPhoneNumbersOptedOut_section.html): Use ListPhoneNumbersOptedOut with an AWS SDK or CLI
- [ListSubscriptions](https://docs.aws.amazon.com/sns/latest/dg/example_sns_ListSubscriptions_section.html): Use ListSubscriptions with an AWS SDK or CLI
- [ListTopics](https://docs.aws.amazon.com/sns/latest/dg/example_sns_ListTopics_section.html): Use ListTopics with an AWS SDK or CLI
- [Publish](https://docs.aws.amazon.com/sns/latest/dg/example_sns_Publish_section.html): Use Publish with an AWS SDK or CLI
- [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/dg/example_sns_SetSMSAttributes_section.html): Use SetSMSAttributes with an AWS SDK or CLI
- [SetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/dg/example_sns_SetSubscriptionAttributes_section.html): Use SetSubscriptionAttributes with an AWS SDK or CLI
- [SetSubscriptionAttributesRedrivePolicy](https://docs.aws.amazon.com/sns/latest/dg/example_sns_SetSubscriptionAttributesRedrivePolicy_section.html): Use SetSubscriptionAttributesRedrivePolicy with an AWS SDK
- [SetTopicAttributes](https://docs.aws.amazon.com/sns/latest/dg/example_sns_SetTopicAttributes_section.html): Use SetTopicAttributes with an AWS SDK or CLI
- [Subscribe](https://docs.aws.amazon.com/sns/latest/dg/example_sns_Subscribe_section.html): Use Subscribe with an AWS SDK or CLI
- [TagResource](https://docs.aws.amazon.com/sns/latest/dg/example_sns_TagResource_section.html): Use TagResource with an AWS SDK or CLI
- [Unsubscribe](https://docs.aws.amazon.com/sns/latest/dg/example_sns_Unsubscribe_section.html): Use Unsubscribe with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/sns/latest/dg/service_code_examples_scenarios.html)

The following code examples show how to use Amazon SNS with AWS SDKs.

- [Build an app to submit data to a DynamoDB table](https://docs.aws.amazon.com/sns/latest/dg/example_cross_SubmitDataApp_section.html): Build an application to submit data to a DynamoDB table
- [Building an Amazon SNS application](https://docs.aws.amazon.com/sns/latest/dg/example_cross_SnsPublishSubscription_section.html): Build a publish and subscription application that translates messages
- [Create a platform endpoint for push notifications](https://docs.aws.amazon.com/sns/latest/dg/example_sns_CreatePlatformEndpoint_section.html): Create a platform endpoint for Amazon SNS push notifications using an AWS SDK
- [Create a serverless application to manage photos](https://docs.aws.amazon.com/sns/latest/dg/example_cross_PAM_section.html): Create a photo asset management application that lets users manage photos using labels
- [Create an Amazon Textract explorer application](https://docs.aws.amazon.com/sns/latest/dg/example_cross_TextractExplorer_section.html): Create an Amazon Textract explorer application
- [Create and publish to a FIFO topic](https://docs.aws.amazon.com/sns/latest/dg/example_sns_PublishFifoTopic_section.html): Create and publish to a FIFO Amazon SNS topic using an AWS SDK
- [Detect people and objects in a video](https://docs.aws.amazon.com/sns/latest/dg/example_cross_RekognitionVideoDetection_section.html): Detect people and objects in a video with Amazon Rekognition using an AWS SDK
- [Publish SMS messages to a topic](https://docs.aws.amazon.com/sns/latest/dg/example_sns_UsageSmsTopic_section.html): Publish SMS messages to an Amazon SNS topic using an AWS SDK
- [Publish a large message](https://docs.aws.amazon.com/sns/latest/dg/example_sns_PublishLargeMessage_section.html): Publish a large message to Amazon SNS with Amazon S3 using an AWS SDK
- [Publish an SMS text message](https://docs.aws.amazon.com/sns/latest/dg/example_sns_PublishTextSMS_section.html): Publish an Amazon SNS SMS text message using an AWS SDK
- [Publish messages to queues](https://docs.aws.amazon.com/sns/latest/dg/example_sqs_Scenario_TopicsAndQueues_section.html): Publish Amazon SNS messages to Amazon SQS queues using an AWS SDK
- [Use API Gateway to invoke a Lambda function](https://docs.aws.amazon.com/sns/latest/dg/example_cross_LambdaAPIGateway_section.html): Use API Gateway to invoke a Lambda function
- [Use scheduled events to invoke a Lambda function](https://docs.aws.amazon.com/sns/latest/dg/example_cross_LambdaScheduledEvents_section.html): Use scheduled events to invoke a Lambda function

### [Serverless examples](https://docs.aws.amazon.com/sns/latest/dg/service_code_examples_serverless_examples.html)

The following code examples show how to use Amazon SNS with AWS SDKs.

- [Invoke a Lambda function from an Amazon SNS trigger](https://docs.aws.amazon.com/sns/latest/dg/example_serverless_SNS_Lambda_section.html): Invoke a Lambda function from an Amazon SNS trigger


## [Security](https://docs.aws.amazon.com/sns/latest/dg/security.html)

### [Data encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-data-encryption.html)

Learn about the methods for protecting data in Amazon SNS, including encryption techniques for securing data both in transit and at rest, as well as best practices for enabling server-side encryption (SSE) and managing encryption keys.

- [Securing data with server-side encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html): Learn about implementing server-side encryption (SSE) for Amazon SNS topics using AWS Key Management Service (KMS), including key management, encryption scope, and compliance benefits, along with detailed instructions on setting up and managing encryption keys.
- [Key management](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html): Learn about key management in Amazon SNS, including configuring permissions, estimating AWS KMS costs, handling common AWS KMS errors, and ensuring compatibility with other AWS services when using encrypted topics.
- [Setting up topic encryption with server-side encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html): Learn how to enable and configure server-side encryption (SSE) for Amazon SNS topics, including using AWS KMS for key management, setting appropriate AWS KMS key policies, and understanding the impact on message consumption for subscribers.
- [Setting up topic encryption with encrypted Amazon SQS queue subscription](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic-sqs-queue-subscriptions.html): Learn how to enable server-side encryption (SSE) for an Amazon SNS topic that is subscribed to an encrypted Amazon SQS queue, including creating and configuring KMS keys, setting up encrypted Amazon SNS topics, and verifying encrypted message delivery to Amazon SQS queues.

### [Securing traffic with VPC endpoints](https://docs.aws.amazon.com/sns/latest/dg/sns-internetwork-traffic-privacy.html)

Learn how to establish private connectivity between Amazon SNS and an Amazon VPC using VPC endpoints, enabling secure message publishing without traversing the public internet.

- [Creating a VPC endpoint](https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-create-endpoint.html): Learn how to create an Amazon VPC endpoint for Amazon SNS, enabling secure message publishing within a private network, and how to test the connection between your VPC and Amazon SNS using an Amazon EC2 instance and the AWS CLI.
- [Creating a VPC policy](https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-endpoint-policy.html): Learn how to create a VPC endpoint policy for Amazon SNS that controls access by specifying which IAM users can perform specific actions, such as publishing to an Amazon SNS topic, within the VPC environment.
- [Publishing a message from a VPC](https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-tutorial.html): Learn how to publish messages to an Amazon SNS topic securely from within an Amazon VPC, including setting up a private network using CloudFormation, creating a VPC endpoint, and verifying message delivery through AWS Lambda and CloudWatch Logs.
- [Using dual-stack endpoints for connectivity](https://docs.aws.amazon.com/sns/latest/dg/sns-dual-stack.html): Learn how to establish connectivity between Amazon VPC and Amazon SNS using VPC dual-stack endpoints, ensuring internetwork traffic privacy.
- [Message Data Protection security](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection.html): Learn about SNS's Message Data Protection feature, which allows you to define rules and policies for auditing and controlling content in transit, ensuring governance, compliance, and the ability to track and log message content flows.

### [Identity and access management](https://docs.aws.amazon.com/sns/latest/dg/security-iam.html)

Learn how to use AWS Identity and Access Management (IAM) to securely control access to Amazon SNS resources, including creating and managing policies, roles, and permissions to enforce security best practices for Amazon SNS topics and messages.

- [Access control use cases](https://docs.aws.amazon.com/sns/latest/dg/sns-when-to-use-access-control.html): Learn specific use cases for applying access control in Amazon SNS, such as granting access to other AWS accounts, limiting subscriptions to specific protocols, and enabling Amazon SNS to publish messages to Amazon SQS queues.
- [Key access policy concepts](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-key-concepts.html): Provides an in-depth explanation of key concepts in the access policy language for Amazon SNS, including how permissions, statements, policies, and conditions work together to manage access to resources.
- [Architectural overview](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-architectural-overview.html): Learn about the key components involved in managing access control for AWS resources, including the roles of resource owners, policies, requesters, and the evaluation process that determines access permissions.
- [Using the Access Policy Language](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-using.html): Explains the general process of how access control works with the access policy language in AWS.
- [Evaluation logic](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-evaluation-logic.html): Explains the evaluation logic used byAWS services to determine whether a request to access a resource is allowed or denied based on applicable policies.
- [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html): Provides detailed examples of common access control scenarios for Amazon SNS, including how to grant AWS account access to a topic, limit subscriptions to HTTPS, and configure permissions for publishing messages from various AWS services like Amazon S3 and CloudWatch to an Amazon SNS topic.
- [How Amazon SNS works with IAM](https://docs.aws.amazon.com/sns/latest/dg/security_iam_service-with-iam.html): Provides an overview of how Amazon SNS integrates with various IAM features, detailing the support for identity-based policies, resource-based policies, and other IAM functionalities to manage access control.
- [AWS managed policies](https://docs.aws.amazon.com/sns/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon SNS and recent changes to those policies.
- [Identity-based policy examples](https://docs.aws.amazon.com/sns/latest/dg/security_iam_id-based-policy-examples.html): Provides an overview of how identity-based policies can be used to control access to Amazon SNS resources, including examples of policy best practices, different types of policies, and specific permissions management strategies.
- [Using identity-based policies](https://docs.aws.amazon.com/sns/latest/dg/sns-using-identity-based-policies.html): Explains how to use identity-based policies with Amazon SNS, covering the integration with IAM to control access to specific Amazon SNS actions and resources, including examples of how to configure and implement these policies effectively.
- [Managing custom IAM policies](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-custom-policies.html): Learn how to manage custom IAM policies to control access to Amazon SNS.
- [Using temporary credentials](https://docs.aws.amazon.com/sns/latest/dg/sns-using-temporary-credentials.html): Learn how to use temporary security credentials with Amazon SNS to securely authenticate and authorize requests, leveraging IAM roles, federated users, and AWS AWS STS.

### [API permissions reference](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-api-permissions-reference.html)

Provides detailed information on Amazon SNS API permissions, including the specific actions supported, policy structure requirements, and service-specific keys that can be used to control access to Amazon SNS topics and subscriptions.

- [Troubleshooting](https://docs.aws.amazon.com/sns/latest/dg/security_iam_troubleshoot.html): Provides guidance on troubleshooting common identity and access issues with Amazon SNS, including resolving authorization errors for specific actions and setting up cross-account access to Amazon SNS resources.

### [Logging and monitoring](https://docs.aws.amazon.com/sns/latest/dg/sns-logging-monitoring.html)

Learn how Amazon SNS integrates with CloudTrail to log and monitor API calls, detailing how to capture, view, and analyze Amazon SNS events for security and auditing purposes.

- [CloudTrail logs](https://docs.aws.amazon.com/sns/latest/dg/logging-using-cloudtrail.html): Learn about logging AWS SNS with AWS CloudTrail.
- [Monitoring topics using CloudWatch](https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html): Learn how to monitor Amazon SNS topics using CloudWatch, detailing how to collect, view, and analyze metrics related to Amazon SNS notifications, and set alarms for specific metrics to improve monitoring and performance management.
- [Compliance validation](https://docs.aws.amazon.com/sns/latest/dg/compliance-validation.html): Learn how Amazon SNS is assessed for security and compliance by third-party auditors as part of various AWS compliance programs, and outlines resources available for you to manage your own compliance responsibilities when using the service.
- [Resilience](https://docs.aws.amazon.com/sns/latest/dg/disaster-recovery-resiliency.html): Learn how Amazon SNS ensures resilience by utilizing AWS's global infrastructure, including Regions and Availability Zones, to provide fault tolerance, scalability, and reliable message delivery.
- [Infrastructure security](https://docs.aws.amazon.com/sns/latest/dg/infrastructure-security.html): Learn about the security measures in place for Amazon SNS, including the use of AWS global network security procedures, TLS encryption, IAM-based access controls, and resource-based policies to restrict access to Amazon SNS topics from specific network locations or VPCs.
- [Security best practices](https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html): Provides best practices for securing Amazon SNS, including recommendations such as implementing least-privilege access, using IAM roles for applications, enforcing encryption of data at rest and in transit, and securing subscriptions to avoid exposure to raw HTTP endpoints.


## [Troubleshooting topics using AWS X-Ray](https://docs.aws.amazon.com/sns/latest/dg/sns-troubleshooting.html)

- [Active tracing](https://docs.aws.amazon.com/sns/latest/dg/sns-active-tracing.html): Learn how to enable and use active tracing in Amazon SNS with AWS X-Ray to analyze and monitor message flow through Amazon SNS topics, including integration with other AWS services like Î, Amazon SQS, and HTTP/S endpoints.
