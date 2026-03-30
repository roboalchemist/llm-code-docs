# Source: https://docs.aws.amazon.com/appsync/latest/eventapi/llms.txt

# AWS AppSync Events Developer Guide

- [What is AWS AppSync Events?](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-welcome.html)
- [Core concepts](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-concepts.html)
- [Authorizing and authenticating Event APIs](https://docs.aws.amazon.com/appsync/latest/eventapi/configure-event-api-auth.html)
- [Event API WebSocket protocol](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-websocket-protocol.html)
- [Configuring custom domain names](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-custom-domains.html)
- [Using AWS WAF to protect APIs](https://docs.aws.amazon.com/appsync/latest/eventapi/using-waf-protect-apis.html)
- [Document History](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-document-history.html)

## [Getting started](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-prerequisites.html): Before you begin the getting started tutorials, confirm that you have completed the prerequisites to get set up with an AWS account.
- [Creating an Event API](https://docs.aws.amazon.com/appsync/latest/eventapi/create-event-api-tutorial.html): AWS AppSync Events allows you to create Event APIs to enable real-time capabilities in your applications.
- [Using the Amplify client](https://docs.aws.amazon.com/appsync/latest/eventapi/build-amplify-app.html): You can connect to your AWS AppSync Event API using any HTTP and WebSocket client, and you can also use the Amplify client for JavaScript.


## [Tutorials](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-tutorials.html)

- [Persist user messages with a DynamoDB table integration](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-table-integration-tutorial.html): Learn how to create an AWS AppSync Events API that stores user messages in a DynamoDB table as they are published and before they are broadcasted to connected users.
- [Create a wscat clone with with NodeJs and IAM auth](https://docs.aws.amazon.com/appsync/latest/eventapi/create-wscat-clone.html): AWS AppSync Events allows you to create Event APIs to enable real-time capabilities in your applications.
- [Publishing from a NodeJS Lambda function with IAM auth](https://docs.aws.amazon.com/appsync/latest/eventapi/lambda-iam-auth.html): Learn about Publishing from a NodeJS Lambda function with IAM auth using AppSyncJs


## [Channel namespaces](https://docs.aws.amazon.com/appsync/latest/eventapi/channel-namespaces.html)

- [Event handlers](https://docs.aws.amazon.com/appsync/latest/eventapi/channel-namespace-handlers.html): Learn how to use event handlers in AWS AppSync to process real-time events, filter and transform data, and manage subscriptions.

### [Data source integrations](https://docs.aws.amazon.com/appsync/latest/eventapi/data-source-integrations.html)

Learn how to integrate data sources with your AWS AppSync event handlers to interact with DynamoDB tables and Lambda functions.

- [Using Lambda](https://docs.aws.amazon.com/appsync/latest/eventapi/direct-lambda-integrations.html): Learn how to integreate Lambda functions directly with your channel namespace.


## [Data sources](https://docs.aws.amazon.com/appsync/latest/eventapi/data-sources-chapter.html)

- [Supported data sources](https://docs.aws.amazon.com/appsync/latest/eventapi/supported-datasources.html): AWS Lambda
- [Adding a data source](https://docs.aws.amazon.com/appsync/latest/eventapi/adding-a-data-source.html): Learn how to add one of the supported data sources to your Event API.


## [Publishing events](https://docs.aws.amazon.com/appsync/latest/eventapi/publish-events.html)

- [Publish events via HTTP](https://docs.aws.amazon.com/appsync/latest/eventapi/publish-http.html): Learn how to publsih events via your AWS AppSync Event APIâs HTTP endpoint.
- [Publish events via WebSocket](https://docs.aws.amazon.com/appsync/latest/eventapi/publish-websocket.html): Learn how to publsih events for your AWS AppSync Event API using WebSocket.


## [CloudWatch logging and monitoring](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-monitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/appsync/latest/eventapi/cw-metrics.html): Understand the CloudWatch metrics that you can monitor to understand the status of events.
- [Configuring CloudWatch Logs on Event APIs](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-monitoring-cw-logs.html): You can configure two types of logging on any new or existing API: request-level logs and and handler logs.


## [Runtime reference](https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-reference.html)

### [Runtime reference overview](https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-reference-overview.html)

Learn about the features available in the JavaScript runtime reference for AWS AppSync Events API.

- [Event handlers overview](https://docs.aws.amazon.com/appsync/latest/eventapi/event-handlers-overview.html): Understand how you can use event handlers to run code in response to onPublish and onSubscribe events.
- [Writing event handlers](https://docs.aws.amazon.com/appsync/latest/eventapi/writing-event-handlers.html): Learn the basic syntax for defining event handlers with and without data sources.
- [Configuring utilities for the APPSYNC_JS runtime](https://docs.aws.amazon.com/appsync/latest/eventapi/configure-utilities.html): Learn how to install utilities that help you with writing event handlers for the APPSYNC_JS runtime.
- [Bundling, TypeScript, and source maps for the APPSYNC_JS runtime](https://docs.aws.amazon.com/appsync/latest/eventapi/additional-utilities.html): TypeScript enhances AWS AppSync development by providing type safety and early error detection.
- [Context reference](https://docs.aws.amazon.com/appsync/latest/eventapi/context-reference.html): JavaScript resolver reference for AWS AppSync.

### [Runtime features](https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-features-overview.html)

Learn about the APPSYNC_JS runtime supported features and utilities that you can use to work with data, and write AWS AppSync Event API functions and handlers.

- [Supported runtime features](https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-supported-features.html): Learn about the JavaScript features supported by the APPSYNC_JS runtime.
- [Built-in utilities](https://docs.aws.amazon.com/appsync/latest/eventapi/built-in-util.html): Learn about the built-in utilities that you can use to work with data in your AWS AppSync Event APIs.
- [Built-in modules](https://docs.aws.amazon.com/appsync/latest/eventapi/built-in-modules.html): Learn about the APPSYNC_JS runtime modules that you can use to help write functions and handlers for your AWS AppSync Event APIs.
- [Runtime utilities](https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-utilities.html): Learn about the supported runtime utilities that you can use to control or modify the runtime properties of your AWS AppSync Event API handlers and functions

### [DynamoDB function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-function-reference.html)

Understand the DynamoDB function reference to interact with a DynamoDB data source from your AWS AppSync Event APIs.

- [GetItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-getitem.html)
- [PutItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-putitem.html)
- [UpdateItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-updateitem.html)
- [DeleteItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-deleteitem.html)
- [Query](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-query.html)
- [Scan](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-scan.html)
- [BatchGetItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-batchgetitem.html)
- [BatchDeleteItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-batchdeleteitem.html)
- [BatchPutItem](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-batchputitem.html)
- [TransactGetItems](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transactgetitems.html)
- [TransactWriteItems](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transactwriteitems.html)
- [Type system (request mapping)](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-typed-values-request.html): When using the AWS AppSync DynamoDB function to call your DynamoDB tables, you must specify your data using the DynamoDB type notation.
- [Type system (response mapping)](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-typed-values-responses.html): When receiving a response from DynamoDB, AWS AppSync automatically converts it into JSON primitive types.
- [Filters](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-filter.html)
- [Condition expressions](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-condition-expressions.html): When you mutate objects in DynamoDB by using the PutItem, UpdateItem, and DeleteItem DynamoDB operations, you can optionally specify a condition expression that controls whether the request should succeed or not, based on the state of the object already in DynamoDB before the operation is performed.
- [Transaction condition expressions](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-transaction-condition-expressions.html): Transaction condition expressions are available in requests of all four types of operations in TransactWriteItems, namely, PutItem, DeleteItem, UpdateItem, and ConditionCheck.
- [Projections](https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-projections.html): When reading objects in DynamoDB using the GetItem, Scan, Query, BatchGetItem, and TransactGetItems operations, you can optionally specify a projection that identifies the attributes that you want.
- [OpenSearch Service function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/opensearch-function-reference.html): JavaScript function reference for Amazon OpenSearch Service for AWS AppSync.
- [Lambda function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/lambda-function-reference.html): Understand the Lambda function reference to interact with a Lambda data source from your AWS AppSync Event APIs.
- [EventBridge function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/eventbridge-function-reference.html): Understand the Amazon EventBridge function reference to interact with a EventBridge data source from your AWS AppSync Event APIs.
- [HTTP function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/http-function-reference.html): JavaScript resolver reference for HTTP for AWS AppSync.
- [Amazon RDS function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/rds-function-reference.html): Resolver reference for Amazon RDS in AWS AppSync.
- [Amazon Bedrock function reference](https://docs.aws.amazon.com/appsync/latest/eventapi/bedrock-function-reference.html): Learn how to use AWS AppSync functions to invoke models on Amazon Bedrock with your AWS AppSync Event APIs.
