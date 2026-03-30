# Source: https://docs.aws.amazon.com/eventbridge/latest/userguide/llms.txt

# Amazon EventBridge User Guide

> Describes key concepts of Amazon EventBridge and provides instructions for using the features of Amazon EventBridge.

- [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Get started with event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-rule-get-started.html)
- [Get started with pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-get-started.html)
- [Testing an event pattern](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-pattern-sandbox.html)
- [Dual-stack endpoints](https://docs.aws.amazon.com/eventbridge/latest/userguide/dual-stack.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/eventbridge/latest/userguide/sdk-general-information-section.html)
- [Troubleshooting](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html)
- [Feature availability](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html)
- [Tags](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tagging.html)
- [Document History](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-document-history.html)

## [Event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)

- [Event bus concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html): Discover the basic concepts of EventBridge event buses, including sources, rules, targets, and how these components relate to each other.
- [Creating an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html): Learn how to create a custom EventBridge event bus, including configuring features like encryption, archives, and permission policies.
- [Updating an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-update.html): Learn how to update a custom EventBridge event bus properties, such as encryption, archives, tags, and permission policies.
- [Updating a default bus using CloudFormation](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-update-default-cfn.html): Learn how to update a default EventBridge event bus properties, such as encryption, archives, tags, and permission policies, using a AWS CloudFormation template.
- [Deleting an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-delete.html): Learn how to delete an EventBridge custom or partner event bus, including the rules defined for that event bus.
- [Generating a CloudFormation template from an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-generate-event-bus-template.html): Learn how to generate a CloudFormation template from an Amazon EventBridge event bus, which you can then use to create additional event buses with the same configuration.

### [Permissions for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-perms.html)

Learn how to grant additional permissions to an event bus by attaching a resource-based policy, and use IAM conditions to scope the policy.

- [Managing event bus permissions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-permissions-manage.html): Learn how to modify the permissions for an existing event bus, including access for API actions and organizations.
- [Send events to a cross-account default bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account.html): Discover how to write an IAM policy to grant an account permission to send events to the default event bus in another account.
- [Send events to a cross-account custom bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account-custom-bus-source.html): Discover how to write an IAM policy to grant an account permission to send specific events to a custom event bus in another account.
- [Send events to event bus in the same account](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-same-account.html): Discover how to write an IAM policy to grant permission to send from one custom event bus to another in the same account and Region.
- [Send events from a specific rule cross-Region](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-restrict-rule.html): Discover how to write an IAM policy granting permission to send events from a rule to an EventBridge event bus in a different account and Region.
- [Send events from specific Regions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-specific-region.html): Discover how to write an IAM permission for an AWS account to send all events from specific Regions to an EventBridge event bus in another Region.
- [Deny sending events from specific Regions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-deny-regions.html): Discover how to write an IAM permission for an EventBridge event bus to receive events from another AWS account, except for events from a specific Region.

### [Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html)

Discover what events are, including how they are structured, and how you can use EventBridge to process and route them in your event-driven applications.

- [Sending events with PutEvents](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevents.html): Learn how to use the PutEvents API to batch and send events to an EventBridge event bus, including calculating batch size and handling errors.
- [Retrying event delivery](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html): Learn about how EventBridge retries delivering events to a target, and how you can configure a target retry policy.
- [Using dead-letter queues](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html): Learn how to configure a dead-letter queue (DLQ) for a rule target, and send all failed events to it for processing later.

### [Events via CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html)

Learn how to access AWS service events via AWS CloudTrail, including API calls and management events, in Amazon EventBridge.

- [Management events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail-management.html): Learn how to access AWS service events via AWS CloudTrail that represent management events.
- [Management event list](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-management-event-list.html): Discover a list of AWS services generate management (read-only) events that are delivered to the default Amazon EventBridge event bus.
- [EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-reference.html): Discover reference information about events EventBridge generates, including "Scheduled Event", "Schema Created", and "Schema Version Created".

### [Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

Discover the basics of EventBridge event bus rules, including rule types: rules that react to events, scheduled rules, and AWS service managed rules.

- [Creating rules (visual builder)](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-visual.html): Learn how to create a rule that reacts to events in EventBridge, including building event patterns, selecting targets, and applying tags.
- [Creating rules (wizard)](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-wizard.html): Learn how to create a rule that reacts to events in EventBridge, including building event patterns, selecting targets, and applying tags.
- [Disabling or deleting a rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-delete-rule.html): Learn how to stop a rule from processing events or running on a schedule, by deleting or disabling the rule.
- [Best practices for rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules-best-practices.html): Discover best practice guidance for defining Amazon EventBridge rules, such as one target per rule, set rule permissions, and monitor rule performance.
- [Using AWS SAM templates](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-sam.html): Learn how to use AWS SAM to launch EventBridge resources, using an example template that shows two different ways to integrate the Lambda functions with EventBridge.
- [Generating a CloudFormation template from a rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-generate-template.html): Learn how to generate a AWS CloudFormation template from a single or multiple Amazon EventBridge rules.

### [Targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)

Learn how to specify targets for EventBridge event bus rules, including what targets are available, target parameters, and permissions.

- [API Gateway targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-gateway-target.html): Learn how to specify an API Gateway endpoint as a rule target in Amazon EventBridge, including dynamic parameters, invocation retries, and timeouts.
- [AWS AppSync targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/target-appsync.html): Learn how to specify an AWS AppSync API mutation as a rule target in Amazon EventBridge.
- [Cross-account services as targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-cross-account.html): Learn how to configure EventBridge to send and receive events between event buses in AWS accounts.
- [Cross-account event buses as targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html): Learn how to configure EventBridge to send and receive events between event buses in AWS accounts.
- [Cross-Region event buses as targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-region.html): Learn how to configure EventBridge to send or receive events between AWS Regions, including allowing/denying events from specific Regions, rules, or sources.
- [Same account event buses as targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-bus-to-bus.html): Learn how to configure EventBridge to send and receive events between event buses in the same AWS account and Region.

### [Input transformation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html)

Learn how to use input transformers to transform events before they are delivered to rule targets in Amazon EventBridge.

- [Configuring an input transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-input-rule.html): Learn now to build an input transformer, to transform event data, as part of creating a rule in Amazon EventBridge.
- [Testing an input transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-sandbox-input-trans.html): Learn how to use the Sandbox to quickly configure and test an input transformer using a sample event, without having to create or edit a rule.

### [Archive and replay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive.html)

Discover how Amazon EventBridge archives enable you to save events so that you can easily replay them at a later time.

- [Creating archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive-event.html): Learn how to create an event archive in Amazon EventBridge, including building event patterns to filter events and setting a retention period.
- [Updating archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-update-archive.html): Learn how to update an event bus archive in Amazon EventBridge using the console or AWS CLI.
- [Deleting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-archive-delete.html): Learn how to delete an Amazon EventBridge event archive from an event bus.
- [Creating event replays](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-replay-archived-event.html): Learn how to replay events from an EventBridge archive, including setting event start and end time, the event bus, and which rules to replay the events to.
- [Canceling event replays](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-replay-cancel.html): Learn how to cancel a running replay events from an EventBridge archive.

### [Global endpoints](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html)

Learn how to improve your application's availability with Amazon EventBridge global endpoints.

- [Creating a global endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-create-endpoint.html): Learn how to create a global endpoint in Amazon EventBridge to help make your application regional-fault tolerant.
- [Best practices](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-best-practices.html): Learn best practices for working with global endpoints in Amazon EventBridge, including event replication, event throttling, and health check metrics.
- [Template for RouteÂ 53 health check](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ge-cfn.html): Learn how to use a CloudFormation template to provision a RouteÂ 53 health check to monitor the status of your Regions for an EventBridge global endpoint.

### [Logging event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html)

Configure EventBridge to send event bus performance logs to CloudWatch Logs, Firehose, or Amazon S3 for monitoring.

- [What gets logged](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-logs-execution-steps.html): Understand the event processing flow from ingestion to target invocation to troubleshoot EventBridge event bus issues.
- [Event bus log schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-logs-schema.html): Reference guide for EventBridge log schema fields including resourceArn, messageType, and error details.


## [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)

- [Event pattern syntax](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-pattern.html): Learn the syntax for creating EventBridge event patterns to select events, matching on event metadata and values.
- [Matching on field values](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-filtering-data-types.html): Learn how to create EventBridge event patterns that match event field values.
- [Matching on null values and empty strings](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-null-values.html): Learn how to create Amazon EventBridge event patterns that match on event values that are null or empty strings.
- [Matching on multiple field values](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-arrays.html): Learn how to create Amazon EventBridge event patterns that use arrays to match against multiple possible field values.
- [Comparison operators](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-pattern-operators.html): Discover the comparison operators you can use to match event values in Amazon EventBridge event patterns, including examples of each.
- [Best practices](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-patterns-best-practices.html): Learn best practices for defining EventBridge event patterns that are concise, scoped, and future-proof.


## [Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)

- [Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html): Discover how the components of EventBridge pipes work to route events from a single source to a single target.
- [Permissions for pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-permissions.html): Learn how to use existing or new execution roles to grant Amazon EventBridge Pipes permissions to event sources.
- [Creating a pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-create.html): Learn how to create an Amazon EventBridge pipe, including specifying a source, defining filtering and enrichment, and selecting a target.
- [Starting or stopping a pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-start-stop.html): Learn how to start or stop an existing Amazon EventBridge pipe, using the console or API.

### [Pipe sources](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-source.html)

Learn about the AWS and third-party services you can define as event sources for Amazon EventBridge Pipes.

- [DynamoDB stream](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-dynamodb.html): Learn how to define a Amazon DynamoDB stream as a source for Amazon EventBridge pipes, including polling, start position, and batch item failures.
- [Kinesis stream](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kinesis.html): Learn how to define a Amazon Kinesis stream as a source for Amazon EventBridge pipes, including polling, start position, and batch item failures.
- [Amazon MQ message broker](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-mq.html): Learn how to define a Amazon MQ message broker as a source for Amazon EventBridge pipes, including consumer group and network configuration.
- [Amazon MSK topic](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-msk.html): Learn how to define a Amazon Managed Streaming for Apache Kafka topic as a source for Amazon EventBridge pipes, including polling, cluster authentication, and network configuration.
- [Apache Kafka stream](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html): Learn how to define a Apache Kafka stream as a source for Amazon EventBridge pipes, including cluster authentication, network configuration, and consumer auto scaling.
- [Amazon SQS queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-sqs.html): Learn how to define a Amazon SQS queue as a source as a source for Amazon EventBridge pipes, including scaling, processing, configuring a queue, and batch failures.
- [Filtering](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-filtering.html): Learn how to select events sent to Amazon EventBridge Pipes, using event patterns composed of filter criteria matching against message and data fields.
- [Enrichment](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-enrichment.html): Learn how to enhance, or enrich, event source data before EventBridge Pipes sends it to the target.
- [Targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html): Learn about which AWS services can be targets for Amazon EventBridge Pipes, and how to configure them, including parameters, permissions, and invocation.
- [Batching and concurrency](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-batching-concurrency.html): Learn about Amazon EventBridge Pipes batching and concurrency, including batch behavior, supported targets, and throughput and concurrency behavior.
- [Input transformation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-input-transformation.html): Learn about using input transformers in Amazon EventBridge Pipes to reshape event JSON data, including reserved variables, data parsing, and common issues.

### [Logging pipe performance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html)

Learn about logging Amazon EventBridge Pipes performance with CloudWatch Logs Firehose, or Amazon S3, including setting log level, execution data, and error reporting.

- [Pipe execution steps](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs-execution-steps.html): Learn about the flow of pipe execution steps as an aid to troubleshoot or debug EventBridge pipe performance using logs.
- [Log schema reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs-schema.html): Learn about reference information on the fields available in the EventBridge Pipe logging schema.
- [Log and monitor](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-monitoring.html): Learn about the metrics and dimensions available to monitor Amazon EventBridge Pipes performance using Amazon CloudWatch Logs;.
- [Error handling & troubleshooting](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-error-troubleshooting.html): Learn about error handling and troubleshooting in Amazon EventBridge Pipes, including retry behavior, invocation errors, DLQ behavior, and failure states.
- [Tutorial: Create a pipe that filters events](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-tutorial-create-dynamodb-sqs.html): Use this tutorial to create an EventBridge pipe that connects a DynamoDB stream to an Amazon SQS queue, and includes an event pattern to filter events.
- [Generating a pipe template](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-generate-template.html): Learn how to generate a AWS CloudFormation template from an existing EventBridge pipe, to help you jumpstart developing templates.


## [Scheduler](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-eventbridge-scheduler.html)

- [Creating a scheduled rule (legacy)](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html): Learn how to create an EventBridge rule that runs on a schedule, either a regular rate or at specific times.
- [Setting a scheduled rule pattern (legacy)](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html): Learn how to use cron or rate expressions to schedule rules in EventBridge.


## [Schemas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html)

- [Finding a schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-find-schema.html): Learn how to find event schemas for AWS services using the Amazon EventBridge console.
- [Schema registries](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-registry.html): Learn how to use schema registries collect and organize schemas so that your schemas are in logical groups.

### [Creating a schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-create.html)

Learn about the different ways of creating custom event schemas using JSON in Amazon EventBridge.

- [Creating a schema using a template](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-template.html): Learn how to create an event schema from a template, either by downloading and editing a file, or working directly in the EventBridge console.
- [Creating a schema from event JSON](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schemas-infer-from-json.html): Learn how to create a schema from the JSON describing a specific event in Amazon EventBridge.
- [Inferring schemas on event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schemas-infer.html): Learn how to use Schema Discovery to infer schemas from the events on an event bus, including cross-account events.
- [Generating code bindings](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-code-bindings.html): Learn how to generate code bindings for EventBridge event schemas to speed up development in Golang, Java, Python, and TypeScript.


## [Services and tools integration](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-related-service.html)

- [AWS CloudFormation](https://docs.aws.amazon.com/eventbridge/latest/userguide/related-services-cfn.html): Learn how CloudFormation integrates with Amazon EventBridge to enable provision on resources such as event buses and rules, pipes, schemas, and schedules.
- [Kafka connector](https://docs.aws.amazon.com/eventbridge/latest/userguide/kafka-connector.html): Learn how to configure the Kafka sink connector to send records to EventBridge.
- [Interface VPC Endpoints](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-related-service-vpc.html): Learn how to establish a private connection between a VPC and EventBridge, so that resources on your VPC can communicate with EventBridge.
- [AWS X-Ray](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-related-service-xray.html): Learn how to AWS X-Ray to trace events that pass through Amazon EventBridge, so that target services can track, analyze, and debug.


## [Third-party integrations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-integrations.html)

### [API destinations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html)

Learn how to use API destinations to invoke HTTP targets for events in Amazon EventBridge.

- [Create an API destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-create.html): Learn how to create an API destination, so you can specify an HTTP endpoint as the target of a rule.
- [Creating rules with API destination targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-api-destination-target.html): Learn how to create an event bus rule that sends events to an API destination target in Amazon EventBridge.
- [CloudEvents](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations-cloudevents.html): Learn how to send events formatted according to the CloudEvents specification to target API destinations in Amazon EventBridge.
- [API destination partners](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html): Discover information provided by AWS Partners to configure an API destination and connection for their service or application.

### [Connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection.html)

Learn how to create connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.

### [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html)

Learn about connections for private APIs

- [Cross-account private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private-cross-region.html): Learn about connections for private APIs
- [Provider considerations](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private-rc-provider.html): Learn how to create connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [Creating connections to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private-create.html): Learn about connections for private APIs
- [Connection authorization methods](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html): Learn how to create connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [Connection states](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-states.html): Learn how to create connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [Creating connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-create.html): Learn how to create connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [Updating connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-edit.html): Learn how to update connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [De-authorizing connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-deauthorize.html): Learn how to delete connections that define the authorization method and credentials for EventBridge to use in connecting to a given HTTPS endpoint.
- [Deleting connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-delete.html): Learn how to delete connections for EventBridge to use in connecting to a given HTTPS endpoint.

### [SaaS partner event sources](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html)

Learn how to set up a partner event source and configure an EventBridge event bus to receive events from Software as a Service (SaaS) partners.

- [Receiving SaaS events through Lambda](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-furls.html): Learn how to set up an Amazon EventBridge event bus to use Lambda function URLs to receive events from supported software as a service (SaaS) providers.
- [Receiving events from Salesforce](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-salesforce.html): Learn how to use Amazon EventBridge to receive events from Salesforce, either using the Salesforce Event Bus Relay or Amazon AppFlow.


## [Tutorials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial.html)

- [Create a sample application](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-get-started.html): Learn how to create a simple application using Lambda functions that send events to EventBridge and are the targets of an rule in this tutorial.
- [Archive and replay events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-archive-replay.html): Learn how to archive and replay for EventBridge events, using a Lambda function at target, in this step-by-step tutorial.
- [Download code bindings](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-download-binding-tutorial.html): Learn how to download code bindings for events using the EventBridge schema registry in this step-by-step tutorial.
- [Use input transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-input-transformer-tutorial.html): Learn how to input transformers to customize the event data EventBridge passes to the rule target, an Amazon SNS topic, in this step-by-step tutorial.
- [Log Auto Scaling group states](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-log-as-group-state.html): Learn how to how to use Amazon EventBridge to log the state of an Auto Scaling group in this step-by-step tutorial.
- [Create rule for AWS API calls via CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-log-api-call.html): Learn how to create a Amazon EventBridge rule that reacts AWS API calls via CloudTrail, using a Lambda function as target, in this step-by-step tutorial.
- [Log Amazon EC2 instance states](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-log-ec2-instance-state.html): Learn how to use Amazon EventBridge to log the state of an Amazon EC2 instance.
- [Log Amazon S3 object operations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-log-s3-data-events.html): Learn how to use Amazon EventBridge to log Amazon S3 object-level operations.
- [Send events using schemas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-relay-events-kinesis-stream.html): Learn how to use Amazon EventBridge to send AWS API call events to a Kinesis stream.
- [Schedule automated Amazon EBS snapshots](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-snapshot.html): Learn how to schedule automated Amazon EBS snapshots using Amazon EventBridge Scheduler or Amazon Data Lifecycle Manager.
- [Send an email when events happen](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-s3-object-created-tutorial.html): Learn how to create a rule that triggers an Amazon SNS topic to send an email whenever an Amazon S3 object is created, in this step-by-step tutorial.
- [Schedule a Lambda function](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html): Learn how to schedule a Lambda function using Amazon EventBridge Scheduler.
- [Send events to Datadog](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-datadog.html): Learn how to send events to Datadog by creating a connection and API destination in Amazon EventBridge, in this step-by-step tutorial.
- [Send events to Salesforce](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-salesforce.html): Learn how to send events to Salesforce by creating a connection and API destination in Amazon EventBridge, in this step-by-step tutorial.
- [Send events to Zendesk](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-zendesk.html): Learn how to send events to Zendesk by creating a connection and API destination in Amazon EventBridge, in this step-by-step tutorial.


## [Code examples](https://docs.aws.amazon.com/eventbridge/latest/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/eventbridge/latest/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of EventBridge with AWS SDKs.

- [Hello EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_Hello_section.html): Hello EventBridge
- [Learn the basics](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_Scenario_GettingStarted_section.html): Learn the basics of EventBridge with an AWS SDK

### [Actions](https://docs.aws.amazon.com/eventbridge/latest/userguide/service_code_examples_actions.html)

The following code examples show how to use EventBridge with AWS SDKs.

- [DeleteRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_DeleteRule_section.html): Use DeleteRule with an AWS SDK or CLI
- [DescribeRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_DescribeRule_section.html): Use DescribeRule with an AWS SDK or CLI
- [DisableRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_DisableRule_section.html): Use DisableRule with an AWS SDK or CLI
- [EnableRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_EnableRule_section.html): Use EnableRule with an AWS SDK or CLI
- [ListRuleNamesByTarget](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_ListRuleNamesByTarget_section.html): Use ListRuleNamesByTarget with an AWS SDK or CLI
- [ListRules](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_ListRules_section.html): Use ListRules with an AWS SDK or CLI
- [ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_ListTargetsByRule_section.html): Use ListTargetsByRule with an AWS SDK or CLI
- [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_PutEvents_section.html): Use PutEvents with an AWS SDK or CLI
- [PutRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_PutRule_section.html): Use PutRule with an AWS SDK or CLI
- [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_PutTargets_section.html): Use PutTargets with an AWS SDK or CLI
- [RemoveTargets](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_RemoveTargets_section.html): Use RemoveTargets with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/eventbridge/latest/userguide/service_code_examples_scenarios.html)

The following code examples show how to use EventBridge with AWS SDKs.

- [Create and trigger a rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_eventbridge_Scenario_createAndTriggerARule_section.html): Create and trigger a rule in Amazon EventBridge using an AWS SDK
- [Send event notifications to EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_s3_Scenario_PutBucketNotificationConfiguration_section.html): Send S3 event notifications to Amazon EventBridge using an AWS SDK
- [Use scheduled events to invoke a Lambda function](https://docs.aws.amazon.com/eventbridge/latest/userguide/example_cross_LambdaScheduledEvents_section.html): Use scheduled events to invoke a Lambda function


## [Security](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-security.html)

### [Data protection](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-data-protection.html)

Learn about the shared responsibility model for protecting your data in EventBridge, and recommendations for securing your AWS account.

- [KMS key options](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-at-rest-key-options.html): Learn about the KMS key options for encrypting your EventBridge data, and the advantages of using AWS owned key or customer managed key.
- [Authorizing key use](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-key-policy.html): Learn how to create a policy containing permissions to authorize EventBridge to use a customer managed key to encrypt your data, and is scoped for security.
- [Maintaining key access](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-key-managment.html): Learn best practices in managing your customer managed key so that EventBridge always has access for encrypting your data.

### [Encrypting event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey.html)

Learn how to create or update an event bus to use an AWS owned key or customer managed key to encrypt your data.

- [Configuring event bus encryption](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey-configure.html): Learn how to configure AWS KMS encryption when creating on updating an EventBridge event bus.
- [Encryption for event bus targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-target.html): Learn how EventBridge decides which AWS KMS key to encrypt event data when the rule target is another event bus.
- [Encryption for managed rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-managed-rules.html): Learn how EventBridge decides which key to encrypt event data for managed rules, which are managed by other AWS services.
- [Encrypting event bus logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-bus-logs.html): Learn how to create or update an event bus to use an AWS owned key or customer managed key to encrypt your data.
- [DLQs for encrypted events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-dlq.html): Learn how to use a dead-letter queue in EventBridge to capture events for non-retriable encryption errors, so you can troubleshoot them later.
- [Decrypting DLQ events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-dlq-decrypt.html): Learn how t0 decrypt events in a dead-letter queue to process those events, once you've resolved the underlying issue.

### [Encrypting pipe data](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-pipes-cmkey.html)

Create or update a pipe to use an AWS owned key or customer managed key to encrypt your EventBridge Pipes data.

- [Configuring pipe encryption](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-pipe-cmkey-configure.html): Learn how to configure AWS KMS encryption when creating on updating an EventBridge pipe.

### [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html)

Create or update an archive to use an AWS owned key or customer managed key to encrypt your EventBridge event data.

- [Configuring archive encryption](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archive-configure.html): Learn how to configure AWS KMS encryption when creating on updating an EventBridge event archive.

### [Encrypting connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections.html)

Learn about the shared responsibility model for protecting your data in EventBridge, and recommendations for securing your AWS account.

- [Configuring connection encryption](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections-configure.html): Learn how to configure AWS KMS encryption when creating on updating an EventBridge HTTPS connection.
- [Tag-based policies](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tag-policies.html): Learn how to use policies based on tags to control access to resources in Amazon EventBridge.

### [IAM](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html)

Discover how you can use IAM and Amazon EventBridge to help secure your resources by controlling who can access them.

- [Managing access](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-manage-iam-access.html): Learn how you manage access to Amazon EventBridge resources such as rules or events by using identity-based or resource-based IAM policies.

### [Using identity-based policies](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-identity-based.html)

Learn about identity-based policies in Amazon EventBridge including managed policies provided by EventBridge.

- [Roles for sending events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-iam-roles.html): Learn about identity-based policies in Amazon EventBridge including managed policies provided by EventBridge.
- [Using resource-based policies](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html): Learn how to ensure Amazon EventBridge has permissions to make API calls against the resources you own.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/eventbridge/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how prevent cross-service confused deputy issues by using IAM resource policies to limit the permissions that Amazon EventBridge gives another service.
- [Resource-based policies for schemas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-resource-based-schemas.html): Learn how Amazon EventBridge schemas support IAM resource-based policies, including supported APIs and examples.
- [Permissions reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-permissions-reference.html): Learn reference information about Amazon EventBridge API calls and corresponding actions that you can specify in IAM policies.
- [IAM policy conditions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-conditions.html): Learn which IAM polciy condition keys that Amazon EventBridge supports, and see multiple examples of their usage.

### [Using service-linked roles](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give EventBridge access to resources in your AWS account.

- [API destination role](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-service-linked-roles-service-action-1.html): Learn how EventBridge uses an IAM service-linked role to enables access to the Secrets Manager secrets created by EventBridge.
- [Schema discovery role](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-service-linked-roles-service-action-2.html): Learn how EventBridge uses an IAM service-linked role to grant permissions to managed rules created by EventBridge schemas.
- [CloudTrail logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon EventBridge with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service.
- [Compliance validation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-compliance.html): Learn about your compliance responsibility when using Amazon EventBridge, and resources AWS provides to help with compliance.
- [Resilience](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-resilience.html): Learn about how Availability Zones can improve resilience in Amazon EventBridge.
- [Infrastructure security](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-infrastructure.html): Learn about how Amazon EventBridge is protected by AWS global network security.
- [Security and vulnerability analysis](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-analysis.html): Learn about how configuration and IT controls are a shared responsibility between AWS and you.


## [Monitoring](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-monitoring.html)

- [Monitoring event delivery](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-monitoring-events-best-practices.html): Learn best practices for monitoring EventBridge metrics in CloudWatch to ensure reliability event delivery.
- [CloudWatch Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cwe-now-eb.html): Discover how EventBridge is the successor to Amazon CloudWatch Events, and builds on its capabilities with features such as partner events, schema Registry, and pipes.
