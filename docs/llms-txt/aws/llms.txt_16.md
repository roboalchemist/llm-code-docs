# Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/llms.txt

# Amazon Simple Queue Service Developer Guide

> Queue messages that one component in the application generates to be consumed by another component using Amazon SQS.

- [What is Amazon SQS?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Related resources](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/related-resources.html)
- [Documentation history](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-release-notes.html)

## [Getting started](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)

- [Setting up](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html): Learn the initial steps required to start using Amazon SQS, including creating an AWS account, securing the root user, setting up IAM users for administrative access, and granting programmatic access to AWS services.
- [Understanding the Amazon SQS console](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-overview.html): Learn how to navigate the Amazon SQS console to view and manage queues, including distinguishing between standard and FIFO queues, performing quick actions, and accessing detailed configuration options.

### [Queue types](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html)

Offers comprehensive information about different types of Amazon SQS queues, including FIFO queues, standard queues, dead-letter queues, and delay queues.

- [Implementing request-response systems in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/implementing-request-response-systems.html): Provides detailed guidance on best practices for setting up efficient and reliable request-response or RPC systems using Amazon SQS, including creating reply queues on start-up and avoiding shared reply queues among producers.
- [Creating a standard queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.html): Learn how to create a standard queue using the Amazon SQS console by following essential steps, such as naming the queue, configuring key parameters (for example, visibility timeout, encryption, and access policies), and sending your first message.
- [Creating a FIFO queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-fifo-queues.html): Learn about Creating a Amazon SQS FIFO queue and sending a message
- [Common tasks](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/get-started.html): Provides a comprehensive list of common tasks and resources to explore and enhance your understanding of Amazon SQS.


## [Managing a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-managing-a-queue.html)

- [Editing a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-edit-queue.html): Edit an Amazon SQS queue using the Amazon SQS console.
- [Receiving and deleting a message](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/step-receive-delete-message.html): Learn how to receive and delete messages in Amazon SQS using long polling and visibility timeouts to effectively manage message retrieval and deletion.
- [Confirming a queue is empty](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/confirm-queue-is-empty.html): Understand how to confirm that an Amazon SQS queue is empty, using both the console and command line methods.
- [Deleting a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/step-delete-queue.html): Learn how to delete an Amazon SQS queue using the console, AWS CLI and AWS API.
- [Purging a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-purge-queue.html): Learn how to purge all messages from an Amazon SQS queue without deleting the queue itself using the Amazon SQS console.


## [Standard queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)

- [Amazon SQS at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html): Learn about the mechanisms and considerations involved in ensuring message delivery at least once.
- [Queue and message identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html): Learn about the unique identifiers assigned to messages in standard and FIFO queues, their formats, and how to effectively manage and track messages using these identifiers.


## [FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html)

- [FIFO queue key terms](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-key-terms.html): Learn important key terms about FIFO queue functionality.
- [FIFO delivery logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html): Learn about sending and receiving messages using Amazon SQS FIFO queues.
- [Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html): Learn how to avoid sending duplicate messages using Amazon SQS FIFO queues.
- [Moving from a standard queue to a FIFO queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html): Learn about moving from an Amazon SQS standard queue to a FIFO queue.
- [FIFO queue and Lambda concurrency behavior](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/fifo-queue-lambda-behavior.html): Use Amazon SQS FIFO queues with Lambda to ensure that messages are processed in the order they are received within each message group.

### [High throughput for FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html)

Learn how to optimize your Amazon SQS FIFO queues using high throughput mode.

- [Enabling high throughput for FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/enable-high-throughput-fifo.html): Learn how to enable your Amazon SQS FIFO queue to use high throughput mode.
- [Queue and message identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queue-message-identifiers.html): Learn about the identifiers of FIFO queues.


## [Quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html)

- [FIFO queue quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-fifo.html): Outlines various quotas and limitations related to FIFO queues in Amazon SQS, including delay queue duration, message group quotas, and maximum message backlog and in-flight message limits.
- [Standard queue quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-queues.html): Learn about the maximum number of messages and the maximum depth allowed in a queue, as well as other service quotas related to Amazon SQS.
- [Message quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html): Learn about various quotas related to Amazon SQS messages, including batch size limits, message group ID requirements, retention periods, and throughput capacities for both standard and FIFO queues.
- [Policy quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-policies.html): Learn about specific quotas related to Amazon SQS policies, including maximums for bytes, conditions, principals, statements, and actions per statement.


## [Features and capabilities](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/features-capabilities.html)

### [Dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

Learn about dead-letter queues, which serve as targets for messages that fail processing, aiding in application debugging by isolating unconsumed messages.

- [Configuring a dead-letter queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue.html): Learn how to configure dead-letter queues (DLQs) in Amazon SQS for handling messages that cannot be processed successfully within their applications.
- [Configuring a dead-letter queue redrive](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue-redrive.html): Learn how to configure an Amazon SQS dead-letter queue redrive to move messages from a dead-letter queue to a source queue or other standard queue.
- [CloudTrail update and permission requirements](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues-cloudtrail.html): Learn about CloudTrail update and permission requirements for Amazon SQS dead-letter queue (DLQ) redrive to a source queue.
- [Creating alarms for dead-letter queues using Amazon CloudWatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/dead-letter-queues-alarms-cloudwatch.html): Set up a CloudWatch alarm to monitor messages in a dead-letter queue using the ApproximateNumberOfMessagesVisible metric.
- [Message metadata for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html): Learn about utilizing message attributes and system attributes in Amazon SQS to include custom metadata with messages.
- [Resources required to process messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-resources-required-process-messages.html): Learn how to estimate the resources required to process Amazon SQS messages by detailing how to determine the approximate number of delayed, visible, and not visible messages in a queue using the GetQueueAttributes action.
- [List queue pagination](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/list-all-queues-pagination.html): Learn how to use controls with the listQueues and listDeadLetterQueues API methods in Amazon SQS.
- [Cost allocation tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html): Understand how to use cost allocation tags to organize and identify Amazon SQS queues.
- [Short and long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html): Learn about the benefits of using Amazon SQS long polling to eliminate empty responses and false empty responses and to reduce your costs.
- [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html): Learn about visibility timeout, which Amazon SQS uses to prevent consumers from processing a message a second time.
- [Fair queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html): Learn about Amazon SQS fair queues, which improve message processing in multi-tenant queues by mitigating the impact of noisy neighbors and reducing dwell time for other tenants.
- [Delay queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html): Learn about postponing the delivery of new messages for a specific number of seconds using Amazon SQS delay queues.
- [Temporary queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-temporary-queues.html): Learn how to utilize Amazon SQS temporary queues to save development time and reduce deployment costs when using common message patterns like request-response.
- [Message timers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html): Learn about specifying an initial invisibility period for a message in a queue using Amazon SQS message timers.
- [Accessing EventBridge pipes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/eb-pipes-integration.html): Create pipes with a Amazon SQS queue as the source from within the Amazon SQS console.

### [Managing large messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-managing-large-messages.html)

Learn about using the Python and Java extended libraries with Amazon S3 to manage large message payloads

- [Using the Extended Client Library for Java](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html): Learn how to configure Amazon SQS to receive notifications from Amazon S3 when new objects are created or deleted in Amazon S3 buckets.
- [Using the Extended Client Library for Python](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/extended-client-library-python.html): Learn how to manage large Amazon SQS messages using the Amazon SQS Extended Client Library for Python and Amazon S3.


## [Configuring Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configuring.html)

### [ABAC for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-abac.html)

Learn about using attribute-based access control (ABAC) in Amazon SQS.

- [Tagging for access control](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-abac-tagging-resource-control.html): Provides an example IAM policy demonstrating how tags can be utilized for access control in Amazon SQS.
- [Creating IAM users and Amazon SQS queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-abac-creating-queues.html): Learn how to create IAM and Amazon SQS queues using the AWS Management Console and in CloudFormation.
- [Testing attribute-based access control](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-abac-testing-access-control.html): Learn how to test attribute-based access control in Amazon SQS.
- [Configuring queue parameters](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-queue-parameters.html): Learn how to configure parameters for an Amazon SQS queue using the Amazon SQS console.
- [Configuring an access policy](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-add-permissions.html): Learn how to add permissions to an Amazon SQS queue.
- [Configuring SSE-SQS for a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html): Learn how to configure Amazon SQS managed server-side encryption (SSE) that uses SQS-managed encryption keys.
- [Configuring SSE-KMS for a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html): Learn how to configure server-side encryption (SSE-KMS) for an Amazon SQS queue.
- [Configuring tags for a queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-tag-queue.html): Learn how to add, modify, or remove cost allocation tags for an Amazon SQS queue using the Amazon SQS console.
- [Subscribing a queue to a topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.html): Learn how to subscribe an Amazon SQS queue to an Amazon SNS topic using the Amazon SQS console.
- [Configuring a Lambda trigger](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-lambda-function-trigger.html): Learn how to configure messages arriving in an Amazon SQS queue to trigger an AWS Lambda function.
- [Automating notifications using EventBridge](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-automating-using-eventbridge.html): Automate the sending of notifications from AWS services to Amazon SQS using EventBridge.
- [Message attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-send-message-with-attributes.html): Use the Amazon SQS console to send a message with attributes to a queue.


## [Best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-best-practices.html)

### [Error handling and problematic messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-error-handling.html)

Provides detailed instructions on managing and mitigating errors in Amazon SQS, including techniques for handling request errors, capturing problematic messages, and configuring dead-letter queue retention to ensure message reliability.

- [Handling request errors in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/handling-request-errors.html): To handle request errors, use one of the following strategies:
- [Capturing problematic messages in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/capturing-problematic-messages.html): To capture all messages that can't be processed, and to collect accurate CloudWatch metrics, configure a dead-letter queue.
- [Setting-up dead-letter queue retention in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/setting-up-dead-letter-queue-retention.html): For standard queues, the expiration of a message is always based on its original enqueue timestamp.

### [Message deduplication and grouping](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-message-deduplication.html)

Provides best practices for ensuring consistent message processing in Amazon SQS, including the use of message deduplication ID and message group ID properties to prevent duplicate messages and manage message groups effectively.

- [Avoiding inconsistent message processing in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoiding-inconsistent-message-processing.html): Because Amazon SQS is a distributed system, it is possible for a consumer to not receive a message even when Amazon SQS marks the message as delivered while returning successfully from a ReceiveMessage API method call.

### [Using the message deduplication ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html)

Learn about using the Amazon SQS message deduplication ID, including its role in preventing duplicate messages in various scenarios.

- [When to provide a message deduplication ID in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/providing-message-deduplication-id.html): A producer should specify a message deduplication ID in the following scenarios:
- [Enabling deduplication for a single-producer/consumer system in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/single-producer-single-consumer.html): If you have a single producer and a single consumer, and messages are unique because they include an application-specific message ID in the body, follow these best practices:
- [Outage recovery scenarios in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/designing-for-outage-recovery-scenarios.html): The deduplication process in FIFO queues is time-sensitive.
- [Configuring visibility timeouts in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/working-with-visibility-timeouts.html): To ensure reliable message processing, set the visibility timeout to be longer than the AWS SDK read timeout.

### [Using the message group ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html)

Learn about using message group IDs effectively in Amazon SQS to manage ordered message processing, avoid duplicates in multi-producer/consumer systems, handle backlog situations, and prevent message blocking in virtual queues.

- [Interleaving multiple ordered message groups in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/interleaving-multiple-ordered-message-groups.html): To interleave multiple ordered message groups within a single FIFO queue, assign a MessageGroupId to each group (for example, session data for different users).
- [Preventing duplicate processing in a multiple-producer/consumer system in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoding-processing-duplicates-in-multiple-producer-consumer-system.html): In a high-throughput, low-latency system where message ordering is not a priority, producers can assign a unique MessageGroupId to each message.
- [Avoid large message backlogs with the same message group ID in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoid-backlog-with-the-same-message-group-id.html): FIFO queues support a maximum of 120,000 in-flight messages (messages received by a consumer but not yet deleted).
- [Avoid reusing the same message group ID with virtual queues in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/avoiding-reusing-message-group-id-with-virtual-queues.html): When using virtual queues with a shared host queue, avoid reusing the same MessageGroupId across different virtual queues.
- [Using the receive request attempt ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html): Learn about the importance of using the receive request attempt ID for deduplication of ReceiveMessage calls, especially during long-lasting network outages causing connectivity issues.

### [Message processing and timing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-message-processing.html)

Provides comprehensive guidance on optimizing the speed and efficiency of message handling in Amazon SQS, including strategies for timely message processing, selecting the best polling mode, and configuring long polling for improved performance.

- [Processing messages in a timely manner in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-processing-messages-timely-manner.html): Setting the visibility timeout depends on how long it takes your application to process and delete a message.
- [Setting-up long polling in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-setting-up-long-polling.html): When the wait time for the ReceiveMessage API action is greater than 0, long polling is in effect.
- [Using the appropriate polling mode in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices-using-appropriate-polling-mode.html)


## [Java SDK examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-tutorials.html)

- [Using server-side encryption](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-configure-sse.html): Use the AWS SDK for Java to add server-side encryption (SSE) to an Amazon SQS queue.
- [Configuring tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-add-update-remove-tag-queue.html): Use the AWS SDK for Java to add, update, and remove tags from your Amazon SQS queues.
- [Sending message attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-send-message-with-attributes.html): Use the AWS SDK for Java to send a message with attributes to an Amazon SQS queue.


## [Using APIs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-working-with-apis.html)

### [Making query API requests using AWS JSON protocol](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests-json.html)

Learn how to make Amazon SQS query API requests with AWS JSON protocol.

- [Interpreting Amazon SQS JSON API responses](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-json-api-responses.html): Learn about the JSON data structure that Amazon SQS returns in response to an action request.
- [Amazon SQS AWS JSON protocol FAQs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-json-faqs.html): Covers frequently asked questions about using the AWS JSON protocol with Amazon SQS, including how it differs from existing Amazon SQS API requests, the supported AWS SDK versions for various programming languages, the benefits of using the JSON protocol, and potential compatibility issues.

### [Making query API requests using AWS query protocol](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests-xml.html)

Understand how to construct endpoints for working with Amazon SQS queues, detailing the structure and examples of GET and POST requests.

- [Interpreting Amazon SQS XML API responses](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-xml-api-responses.html): Learn about the XML data structure that Amazon SQS returns in response to an action request.
- [Authenticating requests](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-request-authentication.html): Learn how Amazon SQS authenticates your requests, how your AWS account and IDs support authentication, and how to create an HMAC-SHA signature.

### [Batch actions](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-batch-api-actions.html)

Learn about the batch actions that you can use with Amazon SQS.

- [Enabling client-side buffering and request batching with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-client-side-buffering-request-batching.html): Learn how to enable client-side buffering and how calls made from the client are first buffered and then sent as a batch request to Amazon SQS.
- [Increasing throughput using horizontal scaling and action batching with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-throughput-horizontal-scaling-and-batching.html): Learn how to increase the throughput of Amazon SQS using horizontal scaling and batching.
- [Working with AWS SDKs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Using JMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-message-service-jms-client.html)

- [Prerequisites](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/prerequisites.html): Understand the prerequisites for using the Amazon SQS Java Messaging Library, including having the SDK for Java, optionally using Maven for dependency management, and ensuring you have the correct version of J2SE Development Kit installed.
- [Using the Java Messaging Library](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/getting-started.html): Provides detailed instructions and examples for getting started with the Amazon SQS Java Messaging Library, including creating JMS connections and sessions, sending and receiving messages, and handling message acknowledgment modes.
- [Using the JMS Client with other Amazon SQS clients](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-jms-client-with-sqs-clients.html): Learn how to use the Amazon SQS Java Message Service (JMS) Client with other Amazon SQS clients, particularly for handling large messages by referencing payloads stored in Amazon S3.
- [Working Java examples for using JMS with standard queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-jms-code-examples.html): Provides code examples of how to use the Java Message Service (JMS) with Amazon SQS standard queues.
- [Supported JMS 1.1 implementations](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/supported-implementations.html): Discover supported JMS implementations, message types, and acknowledgment modes of the Amazon SQS Java Messaging Library.


## [Tutorials](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-other-tutorials.html)

- [Creating an Amazon SQS queue using CloudFormation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/create-queue-cloudformation.html): Learn how to use the CloudFormation console and a JSON (or YAML) template to create an Amazon SQS queue.
- [Sending a message from a VPC](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-sending-messages-from-vpc.html): Send Amazon SQS messages from within Amazon VPC environment.


## [Code examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon SQS with AWS SDKs.

- [Hello Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Hello_section.html): Hello Amazon SQS

### [Actions](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples_actions.html)

The following code examples show how to use Amazon SQS with AWS SDKs.

- [AddPermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_AddPermission_section.html): Use AddPermission with a CLI
- [ChangeMessageVisibility](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ChangeMessageVisibility_section.html): Use ChangeMessageVisibility with an AWS SDK or CLI
- [ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ChangeMessageVisibilityBatch_section.html): Use ChangeMessageVisibilityBatch with a CLI
- [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_CreateQueue_section.html): Use CreateQueue with an AWS SDK or CLI
- [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_DeleteMessage_section.html): Use DeleteMessage with an AWS SDK or CLI
- [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_DeleteMessageBatch_section.html): Use DeleteMessageBatch with an AWS SDK or CLI
- [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_DeleteQueue_section.html): Use DeleteQueue with an AWS SDK or CLI
- [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_GetQueueAttributes_section.html): Use GetQueueAttributes with an AWS SDK or CLI
- [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_GetQueueUrl_section.html): Use GetQueueUrl with an AWS SDK or CLI
- [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ListDeadLetterSourceQueues_section.html): Use ListDeadLetterSourceQueues with a CLI
- [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ListQueues_section.html): Use ListQueues with an AWS SDK or CLI
- [PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_PurgeQueue_section.html): Use PurgeQueue with a CLI
- [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_ReceiveMessage_section.html): Use ReceiveMessage with an AWS SDK or CLI
- [RemovePermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_RemovePermission_section.html): Use RemovePermission with a CLI
- [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_SendMessage_section.html): Use SendMessage with an AWS SDK or CLI
- [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_SendMessageBatch_section.html): Use SendMessageBatch with an AWS SDK or CLI
- [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_SetQueueAttributes_section.html): Use SetQueueAttributes with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples_scenarios.html)

The following code examples show how to use Amazon SQS with AWS SDKs.

- [Create a messaging application](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_cross_SQSMessageApp_section.html): Create a web application that sends and retrieves messages by using Amazon SQS
- [Create a messenger application](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_cross_StepFunctionsMessenger_section.html): Create a messenger application with Step Functions
- [Create an Amazon Textract explorer application](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_cross_TextractExplorer_section.html): Create an Amazon Textract explorer application
- [Create and publish to a FIFO topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sns_PublishFifoTopic_section.html): Create and publish to a FIFO Amazon SNS topic using an AWS SDK
- [Detect people and objects in a video](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_cross_RekognitionVideoDetection_section.html): Detect people and objects in a video with Amazon Rekognition using an AWS SDK
- [Manage large messages using S3](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Scenario_SqsExtendedClient_section.html): Manage large Amazon SQS messages using Amazon S3 with an AWS SDK
- [Process S3 event notifications](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_s3_Scenario_ProcessS3EventNotification_section.html): Receive and process Amazon S3 event notifications by using an AWS SDK
- [Publish messages to queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Scenario_TopicsAndQueues_section.html): Publish Amazon SNS messages to Amazon SQS queues using an AWS SDK
- [Send and receive batches of messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Scenario_SendReceiveBatch_section.html): Send and receive batches of messages with Amazon SQS using an AWS SDK
- [Use the AWS Message Processing Framework for .NET with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_cross_MessageProcessingFrameworkTutorial_section.html): Use the AWS Message Processing Framework for .NET to publish and receive Amazon SQS messages
- [Use the Amazon SQS Java Messaging Library to work with the JMS interface](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Scenario_UseJMS_section.html): Use the Amazon SQS Java Messaging Library to work with the Java Message Service (JMS) interface for Amazon SQS
- [Work with queue tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_sqs_Scenario_WorkWithTags_section.html): Work with queue tags and Amazon SQS using an AWS SDK

### [Serverless examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples_serverless_examples.html)

The following code examples show how to use Amazon SQS with AWS SDKs.

- [Invoke a Lambda function from an Amazon SQS trigger](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_serverless_SQS_Lambda_section.html): Invoke a Lambda function from an Amazon SQS trigger
- [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/example_serverless_SQS_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with an Amazon SQS trigger


## [Troubleshooting](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

- [Access denied error](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-access-denied.html): Learn how to troubleshoot access denied errors in Amazon SQS, covering topics such as queue and IAM policies, AWS KMS permissions, VPC endpoint policies, and Organization service control policies.
- [API errors](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-api-errors.html): Learn about common API errors in Amazon SQS, such as QueueDoesNotExist, InvalidAttributeValue, and ReceiptHandle errors, along with their potential causes and mitigations, including region configuration, queue deletion, DLQ migration, permission issues, and validation of resource policies and receipt handles.
- [DLQ and DLQ redrive issues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-dlq-redrive.html): Learn how to troubleshoot common issues you may encounter with Amazon SQS dead-letter queue (DLQ) redrive, including AccessDenied permissions, NonExistentQueue errors, and CouldNotDetermineMessageSource errors.
- [FIFO throttling issues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-fifo-throttling-issues.html): Learn learn about potential throttling issues in FIFO queues and how to mitigate them by enabling high throughput, utilizing batch actions, optimizing partition utilization, and increasing the number of unique MessageGroupId values.
- [Messages not returned for a ReceiveMessage API call](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-messages-not-returned-ReceiveMessage.html): Learn about common reasons why messages may not be returned for the ReceiveMessage API call in Amazon SQS.
- [Network errors](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/troubleshooting-network-errors.html): Learn how to troubleshoot common network errors such as ETIMEOUT and UnknownHostException when interacting with Amazon SQS endpoints.
- [Troubleshooting queues using X-Ray](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting-using-x-ray.html): Learn how to use AWS X-Ray can be used to troubleshoot Amazon SQS queues by collecting data about requests and identifying potential issues.


## [Security](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon SQS.

### [Data encryption](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-data-encryption.html)

Data protection refers to protecting data while in-transit (as it travels to and from Amazon SQS) and at rest (while it is stored on disks in Amazon SQS data centers).

- [Encryption at rest](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html): Learn how server-side encryption (SSE) in Amazon SQS protects message contents using SQS-managed encryption keys (SSE-SQS) or AWS Key Management Service (SSE-KMS).
- [Key management](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html): Learn about configuring permissions for KMS keys, understanding the data key reuse period, estimating AWS KMS costs, and handling AWS KMS errors when working with encrypted queues in Amazon SQS.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-internetwork-traffic-privacy.html): Learn how to establish connectivity between Amazon VPC and Amazon SQS using VPC endpoints, ensuring internetwork traffic privacy.
- [Using dual-stack endpoints for connectivity](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dual-stack.html): Learn how to establish connectivity between Amazon VPC and Amazon SQS using VPC dual-stack endpoints, ensuring internetwork traffic privacy.

### [Identity and access management](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/security-iam.html)

Learn about managing access to Amazon SQS resources using AWS IAM, including authentication methods, IAM roles, and various policy types for controlling access.

- [Overview](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html): Learn about managing access to Amazon SQS resources, including understanding resource ownership, creating permissions policies, and specifying policy elements such as actions, effects, resources, and principals.
- [How Amazon Simple Queue Service works with IAM](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/security_iam_service-with-iam.html): Learn about the various IAM features available for managing access to Amazon SQS, including identity-based and resource-based policies, policy actions, resources, and condition keys.
- [AWS managed policies](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-access-policy-aws-managed-policies.html): Provides IAM managed policies for Amazon SQS.
- [Troubleshooting](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/security_iam_troubleshoot.html): Learn how to troubleshoot common identity and access issues encountered when working with Amazon SQS and IAM.

### [Using policies](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-identity-based-policies.html)

Use IAM policies and Amazon SQS policies to manage access to Amazon SQS resources.

- [Identity-based policy examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-examples-of-iam-policies.html): Learn about creating identity-based policies to manage permissions for accessing Amazon SQS resources.
- [Basic Amazon SQS policy examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-examples-of-sqs-policies.html): Learn various examples of Amazon SQS policies for different scenarios, such as granting permissions to specific AWS accounts, allowing actions for all users, setting time-limited permissions, and controlling access based on IP addresses.

### [Using custom policies with the Access Policy Language](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies.html)

Use the Access Policy Language to write your own access control policies in access policy language for use in Amazon SQS.

- [Access control architecture](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-architecture.html): Understand the access control architecture for Amazon SQS resources, including the roles of the resource owner, AWS service, policies, and requesters.
- [Access control process workflow](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-process-workflow.html): Understand the general workflow of the process and how access control works with the access policy language.
- [Access Policy Language key concepts](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-key-concepts.html): learn about key concepts related to the Amazon SQS Access Policy Language, including definitions of terms like Allow, Action, Effect, Condition, and Permission.
- [Access Policy Language evaluation logic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-evaluation-logic.html): Learn about the evaluation logic used in Amazon SQS custom policies.
- [Relationships between explicit and default denials](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-relationships-between-explicit-default-denials.html): Learn about the relationship between explicit and default denials in Amazon SQS Custom Policies.
- [Custom policy limitations](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limitations-of-custom-policies.html): Learn about the limitations of custom policies in Amazon SQS, particularly regarding cross-account access and condition keys.

### [Custom Access Policy Language examples](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies-access-policy-examples.html)

View examples of custom Amazon SQS access policies, demonstrating how to grant or deny permissions to specific AWS accounts, restrict access based on conditions like time or IP address, and deny access from specific accounts or sources.

- [Using temporary security credentials](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-temporary-security-credentials.html): Learn how to utilize temporary security credentials with Amazon SQS to grant access to AWS services and resources.
- [Access management for encrypted Amazon SQS queues with least privilege policies](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-least-privilege-policy.html): Learn how to control access to your encrypted Amazon SQS queue using the Amazon SQS policy and the AWS KMS key policy.
- [API permissions reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-permissions-reference.html): Learn the Amazon SQS actions and the AWS resource for which you can grant permissions.

### [Logging and monitoring](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/logging-and-monitoring.html)

Learn how Amazon SQS integrates with AWS monitoring and logging tools like CloudTrail, CloudWatch Alarms, CloudWatch Logs, and Trusted Advisor to track API activity, analyze message processing, and optimize queue configurations.

- [Logging API calls](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/logging-using-cloudtrail.html): Learn how to use AWS CloudTrail to log and monitor Amazon SQS API operations.

### [Monitoring queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/monitoring-using-cloudwatch.html)

Monitor metrics for Amazon SQS using the Amazon SQS console, the CloudWatch console, or programmatically using CloudWatch actions.

- [Accessing CloudWatch metrics for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-access-metrics.html): Learn about accessing CloudWatch metrics for Amazon SQS queues, including how to view and analyze metrics using various methods such as the Amazon SQS console, the CloudWatch console, AWS CLI, and CloudWatch API.
- [Creating CloudWatch alarms for Amazon SQS metrics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/set-cloudwatch-alarms-for-metrics.html): Learn how to create CloudWatch alarms for Amazon SQS metrics to trigger based on a metric threshold.
- [Available CloudWatch metrics for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html): Learn about various CloudWatch metrics available for monitoring Amazon SQS queues, including metrics like ApproximateAgeOfOldestMessage, NumberOfMessagesReceived, and SentMessageSize.
- [Compliance validation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/disaster-recovery-resiliency.html): Learn how AWS and Amazon SQS architectures support data redundancy and resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/infrastructure-security.html): Learn about the infrastructure security measures in place for Amazon SQS, including the use of AWS global network security procedures, TLS 1.2 or later, and secure cipher suites.
- [Best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security-best-practices.html): Learn about the security best practices for Amazon SQS, emphasizing preventative measures such as ensuring queues are not publicly accessible, implementing least-privilege access, using IAM roles, and enforcing encryption for both data at rest and in transit.
