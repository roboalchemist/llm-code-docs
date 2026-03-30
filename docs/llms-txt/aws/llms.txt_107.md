# Source: https://docs.aws.amazon.com/appsync/latest/devguide/llms.txt

# AWS AppSync GraphQL Developer Guide

- [What is AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)
- [Building a client application](https://docs.aws.amazon.com/appsync/latest/devguide/building-a-client-app.html)
- [Troubleshooting and common mistakes](https://docs.aws.amazon.com/appsync/latest/devguide/troubleshooting-and-common-mistakes.html)

## [GraphQL and AWS AppSync architecture](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-overview.html)

- [What is an API](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-an-api.html): An application programming interface (API) defines the rules that you must follow to communicate with other software systems.
- [What is REST](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-rest.html): At a high level, representational State Transfer (REST) is a software architecture that imposes conditions on how an API should work.
- [What is GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-graphql.html): GraphQL is both a query language for APIs and a runtime for executing those queries.
- [Comparing REST and GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/comparing-rest-graphql.html): APIs (Application Programming Interfaces) play a crucial role in facilitating data exchange between applications.
- [Why Use GraphQL over REST](https://docs.aws.amazon.com/appsync/latest/devguide/why-use-graphql.html): REST is one of the cornerstone architectural styles of web APIs.

### [Components of a GraphQL API](https://docs.aws.amazon.com/appsync/latest/devguide/api-components.html)

A standard GraphQL API is composed of a single schema that handles the shape of the data that will be queried.

### [GraphQL schemas](https://docs.aws.amazon.com/appsync/latest/devguide/schema-components.html)

The GraphQL schema is the foundation of a GraphQL API.

- [GraphQL types](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-types.html): GraphQL supports many different types.
- [GraphQL fields](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-fields.html): Fields exist within the scope of a type and hold the value that's requested from the GraphQL service.
- [Data sources](https://docs.aws.amazon.com/appsync/latest/devguide/data-source-components.html): In the previous section, we learned that a schema defines the shape of your data.
- [Resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-components.html): From the previous sections, you learned about the components of the schema and data source.
- [Additional properties of GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-properties.html): GraphQL consists of several design principles to maintain simplicity and robustness at scale.


## [Getting started: Creating your first GraphQL API](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html)

- [Launching a schema](https://docs.aws.amazon.com/appsync/latest/devguide/schema-launch-start.html): In this example, you will create a Todo API that allows users to create Todo items for daily chore reminders like Finish task or Pick up groceries.
- [Taking a tour of the AWS AppSync console](https://docs.aws.amazon.com/appsync/latest/devguide/console-tour.html): Before we add data to our DynamoDB table, we should review the basic features of the AWS AppSync console experience.
- [Using GraphQL mutations to add data to a DynamoDB table](https://docs.aws.amazon.com/appsync/latest/devguide/add-data-with-graphql-mutation.html): Your next step is to add data to your blank DynamoDB table using a GraphQL mutation.
- [Using GraphQL queries to retrieve data from a DynamoDB table](https://docs.aws.amazon.com/appsync/latest/devguide/retrieve-data-with-graphql-query.html): Now that a record exists in your database, you'll get results when you run a query.
- [Supplemental sections](https://docs.aws.amazon.com/appsync/latest/devguide/next-steps.html): These sections are a reference for more advanced AWS AppSync topics.


## [Designing GraphQL APIs](https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html)

### [Structuring a GraphQL API (blank or imported APIs)](https://docs.aws.amazon.com/appsync/latest/devguide/blank-import-api.html)

Before you create your GraphQL API from a blank template, it would help to review the concepts surrounding GraphQL.

- [Designing your GraphQL schema](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html): Designing your schema for AWS AppSync.
- [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html): Getting started: build a schema from scratch for AWS AppSync.

### [Configuring AWS AppSync resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-config-overview.html)

In the previous sections, you learned how to create your GraphQL schema and data source, then linked them together in the AWS AppSync service.

### [Creating basic queries (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers-js.html)

Quick start guide prerequisites for AWS AppSync.

- [Testing and debugging resolvers (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/test-debug-resolvers-js.html): Testing and debugging resolvers in AWS AppSync.
- [Configuring and using pipeline resolvers (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers-js.html): Pipeline Resolvers in AWS AppSync.

### [Creating basic queries (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html)

Quick start guide prerequisites for AWS AppSync.

- [Disabling VTL mapping templates with direct Lambda resolvers (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/direct-lambda-reference.html): Describes how to use direct Lambda resolvers to bypass the of VTL templates.
- [Testing and debugging resolvers (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/test-debug-resolvers.html): Testing and debugging resolvers in AWS AppSync.
- [Configuring and using pipeline resolvers (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html): Pipeline Resolvers in AWS AppSync.
- [Using APIs with the CDK](https://docs.aws.amazon.com/appsync/latest/devguide/using-your-api.html): Using your API in AWS AppSync.

### [Using subscriptions for real-time data applications](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html)

Learn about real-time data for AWS AppSync.

- [Creating generic pub/sub APIs powered by serverless WebSockets](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-create-generic-api-serverless-websocket.html): Learn about how pub/sub APIs work in AWS AppSync.
- [Defining enhanced subscriptions filters](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-enhanced-filtering.html): Learn about enhanced subscription filtering in AWS AppSync.
- [Unsubscribing WebSocket connections using filters](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-invalidation.html): Learn how to forcible unsubscribe and close WebSocket connections in AWS AppSync.
- [Building a real-time WebSocket client](https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html): AWS AppSync real-time WebSocket client setup
- [Merging APIs](https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html): Learn about the AWS AppSync merged APIs feature.
- [Building GraphQL APIs with RDS introspection](https://docs.aws.amazon.com/appsync/latest/devguide/rds-introspection.html): Getting started: using RDS to build a schema.


## [JavaScript resolver tutorials](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html)

- [Creating a simple post application using DynamoDB JavaScript resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-resolvers-js.html): JavaScript resolvers tutorial for AWS AppSync.
- [Using AWS Lambda resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-lambda-resolvers-js.html): Lambda resolvers tutorial for AWS AppSync
- [Using local resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-local-resolvers-js.html): Local Resolvers tutorial for AWS AppSync.
- [Combining GraphQL resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-combining-graphql-resolvers-js.html): Combining GraphQL Resolvers tutorial for AWS AppSync.
- [Using OpenSearch Service resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-elasticsearch-resolvers-js.html): Amazon OpenSearch Service Resolvers tutorial for AWS AppSync.
- [Performing DynamoDB transactions](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-transact-js.html): Amazon DynamoDB Transaction Resolvers tutorial for AWS AppSync.
- [Using DynamoDB batch operations](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-batch-js.html): Amazon DynamoDB Batch Resolvers tutorial for AWS AppSync.
- [Using HTTP resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-http-resolvers-js.html): HTTP resolvers tutorial for AWS AppSync.
- [Using Aurora PostgreSQL with Data API](https://docs.aws.amazon.com/appsync/latest/devguide/aurora-serverless-tutorial-js.html): Learn more about the serverless process in AWS AppSync.


## [VTL resolver tutorials](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials.html)

- [Creating a simple post application using DynamoDB resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-resolvers.html): DynamoDB resolvers tutorial for AWS AppSync.
- [Using AWS Lambda resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-lambda-resolvers.html): Lambda resolvers tutorial for AWS AppSync
- [Using OpenSearch Service resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-elasticsearch-resolvers.html): Amazon OpenSearch Service Resolvers tutorial for AWS AppSync.
- [Using local resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-local-resolvers.html): Local Resolvers tutorial for AWS AppSync.
- [Combining GraphQL resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-combining-graphql-resolvers.html): Combining GraphQL Resolvers tutorial for AWS AppSync.
- [Using DynamoDB batch operations](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-batch.html): Amazon DynamoDB Batch Resolvers tutorial for AWS AppSync.
- [Performing DynamoDB transactions](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-dynamodb-transact.html): Amazon DynamoDB Transaction Resolvers tutorial for AWS AppSync.
- [Using HTTP resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-http-resolvers.html): HTTP resolvers tutorial for AWS AppSync.
- [Using Aurora Serverless v2 resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-rds-resolvers.html): Aurora Serverless v2 tutorial for AWS AppSync.
- [Using pipeline resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-pipeline-resolvers.html): Pipeline Resolvers tutorial for AWS AppSync.
- [Using Delta Sync operations on versioned data sources](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-delta-sync.html): Pipeline resolvers tutorial for AWS AppSync.


## [Configuration and settings](https://docs.aws.amazon.com/appsync/latest/devguide/configuration-and-settings.html)

- [Configuring server-side caching and API payload compression](https://docs.aws.amazon.com/appsync/latest/devguide/enabling-caching.html): Learn about server-side data caching and compression capabilities in AWS AppSync.
- [Configuring custom domain names for GraphQL and real-time APIs](https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html): AWS AppSync custom domain name setup

### [Versioning, conflict detection, and sync operations for DynamoDB](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html)

Conflict Detection and Sync for AWS AppSync.

- [Versioning DynamoDB data sources](https://docs.aws.amazon.com/appsync/latest/devguide/versioned-data-sources.html): AWS AppSync currently supports versioning on DynamoDB data sources.
- [Conflict detection and resolution](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-resolution.html): When concurrent writes happen with AWS AppSync, you can configure Conflict Detection and Conflict Resolution strategies to handle updates appropriately.
- [Using DynamoDB sync operations on versioned data sources](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-conflict-detection-and-sync-sync-operations.html): Versioned data sources support Sync operations that allow you to retrieve all the results from a DynamoDB table and then receive only the data altered since your last query (the delta updates).
- [Using CloudWatch to monitor and log GraphQL API data](https://docs.aws.amazon.com/appsync/latest/devguide/monitoring.html): Learn how to use CloudWatch to monitor your AWS AppSync GraphQL API operations.
- [Tracing requests in AWS X-Ray](https://docs.aws.amazon.com/appsync/latest/devguide/x-ray-tracing.html): Tracing AWS AppSync APIs with AWS X-Ray integration.
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/appsync/latest/devguide/cloudtrail-logging.html): Learn about integrating AWS AppSync with CloudTrail.
- [Using AWS AppSync Private APIs](https://docs.aws.amazon.com/appsync/latest/devguide/using-private-apis.html): Learn about the AWS AppSync Private API features.
- [Sharing GraphQL APIs](https://docs.aws.amazon.com/appsync/latest/devguide/sharing-graphql-apis.html): Learn how to use the integration with AWS Resource Access Manager to share your AWS AppSync GraphQL APIs.
- [Configuring GraphQL run complexity, query depth, and introspection](https://docs.aws.amazon.com/appsync/latest/devguide/configuration-limits.html): Learn about configuring introspection and limits in AWS AppSync.
- [Using environment variables](https://docs.aws.amazon.com/appsync/latest/devguide/environment-variables.html): Learn about configuring environment variables in AWS AppSync.


## [Authorizing and authenticating GraphQL APIs](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html)

- [Access control use cases for securing requests and responses](https://docs.aws.amazon.com/appsync/latest/devguide/security-authorization-use-cases.html): Authorization scenarios for AWS AppSync.
- [Using AWS WAF to protect APIs](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html): Describes how to create an AWS WAF web ACL and associate it with an AppSync API to protect it from an attack.


## [Security](https://docs.aws.amazon.com/appsync/latest/devguide/security.html)

- [Data protection](https://docs.aws.amazon.com/appsync/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS AppSync.
- [Compliance validation](https://docs.aws.amazon.com/appsync/latest/devguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/appsync/latest/devguide/infrastructure-security.html): Learn how AWS AppSync isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/appsync/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS AppSync features for data resiliency.

### [Identity and access management](https://docs.aws.amazon.com/appsync/latest/devguide/security-iam.html)

Learn how to authenticate requests and manage access to your AWS AppSync resources.

- [How AWS AppSync works with IAM](https://docs.aws.amazon.com/appsync/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS AppSync, learn what IAM features are available to use with AWS AppSync.

### [Identity-based policies](https://docs.aws.amazon.com/appsync/latest/devguide/security_iam_id-based-policy-examples.html)

By default, users and roles don't have permission to create or modify AWS AppSync resources.

- [AWS managed policies](https://docs.aws.amazon.com/appsync/latest/devguide/security_iam_policy_list.html): To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself.
- [Troubleshooting](https://docs.aws.amazon.com/appsync/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS AppSync and IAM.
- [Logging AWS AppSync API calls with AWS CloudTrail](https://docs.aws.amazon.com/appsync/latest/devguide/logging-using-cloudtrail.html): Learn about logging AWS AppSync with AWS CloudTrail.
- [Best practices](https://docs.aws.amazon.com/appsync/latest/devguide/best-practices.html): Learn some best practices for securely using AWS AppSync.


## [Resolver reference (JavaScript)](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html)

### [JavaScript resolvers overview](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-overview-js.html)

JavaScript resolvers overview for AWS AppSync.

- [Example pipeline resolver with Amazon DynamoDB](https://docs.aws.amazon.com/appsync/latest/devguide/writing-code.html): Suppose you wanted to attach a pipeline resolver on a field named getPost(id:ID!) that returns a Post type from an Amazon DynamoDB data source with the following GraphQL query:
- [Configuring utilities for the APPSYNC_JS runtime](https://docs.aws.amazon.com/appsync/latest/devguide/utility-resolvers.html): AWS AppSync provides two libraries that aid in the development of resolvers with the APPSYNC_JS runtime:
- [Bundling, TypeScript, and source maps for the APPSYNC_JS runtime](https://docs.aws.amazon.com/appsync/latest/devguide/additional-utilities.html): TypeScript enhances AWS AppSync development by providing type safety and early error detection.
- [Testing your resolver and function handlers](https://docs.aws.amazon.com/appsync/latest/devguide/test-resolvers.html): You can use the EvaluateCode API command to remotely test your resolver and function handlers with mocked data before ever saving your code to a resolver or function.
- [Migrating from VTL to JavaScript](https://docs.aws.amazon.com/appsync/latest/devguide/migrating-resolvers.html): AWS AppSync allows you to write your business logic for your resolvers and functions using VTL or JavaScript.
- [Choosing between direct data source access and proxying via a Lambda data source](https://docs.aws.amazon.com/appsync/latest/devguide/choosing-data-source.html): With AWS AppSync and the APPSYNC_JS runtime, you can write your own code that implements your custom business logic by using AWS AppSync functions to access your data sources.
- [JavaScript resolver context object reference](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference-js.html): JavaScript resolver reference for AWS AppSync.

### [JavaScript runtime features for resolvers and functions](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-util-reference-js.html)

Learn about JavaScript resolver utility helpers for AWS AppSync.

- [Supported runtime features](https://docs.aws.amazon.com/appsync/latest/devguide/supported-features.html): The sections below describe the supported feature set of the APPSYNC_JS runtime.
- [Built-in utilities](https://docs.aws.amazon.com/appsync/latest/devguide/built-in-util-js.html): The util variable contains general utility methods to help you work with data.
- [Built-in modules](https://docs.aws.amazon.com/appsync/latest/devguide/built-in-modules-js.html): Modules are a part of the APPSYNC_JS runtime and provide utilities to help write JavaScript resolvers and functions.
- [Runtime utilities](https://docs.aws.amazon.com/appsync/latest/devguide/runtime-utils-js.html): The runtime library provides utilities to control or modify the runtime properties of your resolvers and functions.
- [Time helpers in util.time](https://docs.aws.amazon.com/appsync/latest/devguide/time-helpers-in-util-time-js.html): The util.time variable contains datetime methods to help generate timestamps, convert between datetime formats, and parse datetime strings.
- [DynamoDB helpers in util.dynamodb](https://docs.aws.amazon.com/appsync/latest/devguide/dynamodb-helpers-in-util-dynamodb-js.html): util.dynamodb contains helper methods that make it easier to write and read data to Amazon DynamoDB, such as automatic type mapping and formatting.
- [HTTP helpers in util.http](https://docs.aws.amazon.com/appsync/latest/devguide/http-helpers-in-utils-http-js.html): The util.http utility provides helper methods that you can use to manage HTTP request parameters and to add response headers.
- [Transformation helpers in util.transform](https://docs.aws.amazon.com/appsync/latest/devguide/transformation-helpers-in-utils-transform-js.html): util.transform contains helper methods that make it easier to perform complex operations against data sources.
- [String helpers in util.str](https://docs.aws.amazon.com/appsync/latest/devguide/str-helpers-in-util-str-js.html): util.str contains methods to help with common String operations.
- [Extensions](https://docs.aws.amazon.com/appsync/latest/devguide/extensions-js.html): extensions contains a set of methods to make additional actions within your resolvers.
- [XML helpers in util.xml](https://docs.aws.amazon.com/appsync/latest/devguide/xml-helpers-in-util-xml-js.html): util.xml contains methods to help with XML string conversion.

### [JavaScript resolver function reference for DynamoDB](https://docs.aws.amazon.com/appsync/latest/devguide/js-resolver-reference-dynamodb.html)

Resolver Reference for DynamoDB for AWS AppSync.

- [GetItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-getitem.html): The GetItem request lets you tell the AWS AppSync DynamoDB function to make a GetItem request to DynamoDB, and enables you to specify:
- [PutItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-putitem.html): The PutItem request mapping document lets you tell the AWS AppSync DynamoDB function to make a PutItem request to DynamoDB, and enables you to specify the following:
- [UpdateItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-updateitem.html): The UpdateItem request enables you to tell the AWS AppSync DynamoDB function to make a UpdateItem request to DynamoDB and allows you to specify the following:
- [DeleteItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-deleteitem.html): The DeleteItem request lets you tell the AWS AppSync DynamoDB function to make a DeleteItem request to DynamoDB, and enables you to specify the following:
- [Query](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-query.html): The Query request object lets you tell the AWS AppSync DynamoDB resolver to make a Query request to DynamoDB, and enables you to specify the following:
- [Scan](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-scan.html): The Scan request lets you tell the AWS AppSync DynamoDB function to make a Scan request to DynamoDB, and enables you to specify the following:
- [Sync](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-sync.html): The Sync request object lets you retrieve all the results from a DynamoDB table and then receive only the data altered since your last query (the delta updates).
- [BatchGetItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-batch-get-item.html): The BatchGetItem request object lets you tell the AWS AppSync DynamoDB function to make a BatchGetItem request to DynamoDB to retrieve multiple items, potentially across multiple tables.
- [BatchDeleteItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-batch-delete-item.html): The BatchDeleteItem request object lets you tell the AWS AppSync DynamoDB function to make a BatchWriteItem request to DynamoDB to delete multiple items, potentially across multiple tables.
- [BatchPutItem](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-batch-put-item.html): The BatchPutItem request object lets you tell the AWS AppSync DynamoDB function to make a BatchWriteItem request to DynamoDB to put multiple items, potentially across multiple tables.
- [TransactGetItems](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-transact-get-items.html): The TransactGetItems request object lets you to tell the AWS AppSync DynamoDB function to make a TransactGetItems request to DynamoDB to retrieve multiple items, potentially across multiple tables.
- [TransactWriteItems](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-transact-write-items.html): The TransactWriteItems request object lets you tell the AWS AppSync DynamoDB function to make a TransactWriteItems request to DynamoDB to write multiple items, potentially to multiple tables.
- [Type system (request mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-typed-values-request.html): When using the AWS AppSync DynamoDB function to call your DynamoDB tables, AWS AppSync needs to know the type of each value to use in that call.
- [Type system (response mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-typed-values-responses.html): When receiving a response from DynamoDB, AWS AppSync automatically converts it into GraphQL and JSON primitive types.
- [Filters](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-filter.html): When querying objects in DynamoDB using the Query and Scan operations, you can optionally specify a filter that evaluates the results and returns only the desired values.
- [Condition expressions](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-condition-expressions.html): When you mutate objects in DynamoDB by using the PutItem, UpdateItem, and DeleteItem DynamoDB operations, you can optionally specify a condition expression that controls whether the request should succeed or not, based on the state of the object already in DynamoDB before the operation is performed.
- [Transaction condition expressions](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-transaction-condition-expressions.html): Transaction condition expressions are available in requests of all four types of operations in TransactWriteItems, namely, PutItem, DeleteItem, UpdateItem, and ConditionCheck.
- [Projections](https://docs.aws.amazon.com/appsync/latest/devguide/js-aws-appsync-resolver-reference-dynamodb-projections.html): When reading objects in DynamoDB using the GetItem, Scan, Query, BatchGetItem, and TransactGetItems operations, you can optionally specify a projection that identifies the attributes that you want.
- [JavaScript resolver function reference for OpenSearch](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-elasticsearch-js.html): JavaScript resolver reference for Amazon OpenSearch Service for AWS AppSync.
- [JavaScript resolver function reference for Lambda](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-lambda-js.html): AWS AppSync JavaScript resolver reference for Lambda
- [JavaScript resolver function reference for EventBridge data source](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-eventbridge-js.html): JavaScript resolver reference for Amazon EventBridge for AWS AppSync.
- [JavaScript resolver function reference for None data source](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-none-js.html): JavaScript resolver reference for data source of type None.
- [JavaScript resolver function reference for HTTP](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-http-js.html): JavaScript resolver reference for HTTP for AWS AppSync.
- [JavaScript resolver function reference for Amazon RDS](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-rds-js.html): Resolver reference for Amazon RDS in AWS AppSync.
- [JavaScript resolver function reference for Amazon Bedrock](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-bedrock-js.html): Learn how to use AWS AppSync functions and resolvers to invoke models on Amazon Bedrock.


## [Resolver mapping template reference (VTL)](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html)

- [Resolver mapping template overview](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-overview.html): Resolver mapping template overview for AWS AppSync.
- [Resolver mapping template programming guide](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-programming-guide.html): Resolver mapping template programming guide for AWS AppSync.
- [Resolver mapping template context reference](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html): Resolver mapping template context reference for AWS AppSync.

### [Resolver mapping template utility reference](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-util-reference.html)

Learn about resolver mapping template utility helpers for AWS AppSync.

- [Utility helpers in $util](https://docs.aws.amazon.com/appsync/latest/devguide/utility-helpers-in-util.html)
- [AWS AppSync directives](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-directives.html)
- [Time helpers in $util.time](https://docs.aws.amazon.com/appsync/latest/devguide/time-helpers-in-util-time.html)
- [List helpers in $util.list](https://docs.aws.amazon.com/appsync/latest/devguide/list-helpers-in-util-list.html)
- [Map helpers in $util.map](https://docs.aws.amazon.com/appsync/latest/devguide/utility-helpers-in-map.html)
- [DynamoDB helpers in $util.dynamodb](https://docs.aws.amazon.com/appsync/latest/devguide/dynamodb-helpers-in-util-dynamodb.html)
- [Amazon RDS helpers in $util.rds](https://docs.aws.amazon.com/appsync/latest/devguide/rds-helpers-in-util-rds.html)
- [HTTP helpers in $util.http](https://docs.aws.amazon.com/appsync/latest/devguide/http-helpers-in-utils-http.html)
- [XML helpers in $util.xml](https://docs.aws.amazon.com/appsync/latest/devguide/xml-helpers-in-utils-xml.html)
- [Transformation helpers in $util.transform](https://docs.aws.amazon.com/appsync/latest/devguide/transformation-helpers-in-utils-transform.html)
- [Math helpers in $util.math](https://docs.aws.amazon.com/appsync/latest/devguide/math-helpers-in-util-math.html)
- [String helpers in $util.str](https://docs.aws.amazon.com/appsync/latest/devguide/str-helpers-in-util-str.html)
- [Extensions](https://docs.aws.amazon.com/appsync/latest/devguide/extensions.html)

### [Resolver mapping template reference for DynamoDB](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html)

Resolver Mapping Template Reference for DynamoDB for AWS AppSync.

- [GetItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-getitem.html): The GetItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a GetItem request to DynamoDB, and enables you to specify:
- [PutItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-putitem.html): The PutItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a PutItem request to DynamoDB, and enables you to specify the following:
- [UpdateItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem.html): The UpdateItem request mapping document enables you to tell the AWS AppSync DynamoDB resolver to make a UpdateItem request to DynamoDB and allows you to specify the following:
- [DeleteItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-deleteitem.html): The DeleteItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a DeleteItem request to DynamoDB, and enables you to specify the following:
- [Query](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-query.html): The Query request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a Query request to DynamoDB, and enables you to specify the following:
- [Scan](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-scan.html): The Scan request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a Scan request to DynamoDB, and enables you to specify the following:
- [Sync](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-sync.html): The Sync request mapping document lets you retrieve all the results from a DynamoDB table and then receive only the data altered since your last query (the delta updates).
- [BatchGetItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-batch-get-item.html): The BatchGetItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a BatchGetItem request to DynamoDB to retrieve multiple items, potentially across multiple tables.
- [BatchDeleteItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-batch-delete-item.html): The BatchDeleteItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a BatchWriteItem request to DynamoDB to delete multiple items, potentially across multiple tables.
- [BatchPutItem](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-batch-put-item.html): The BatchPutItem request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a BatchWriteItem request to DynamoDB to put multiple items, potentially across multiple tables.
- [TransactGetItems](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-transact-get-items.html): The TransactGetItems request mapping document lets you to tell the AWS AppSync DynamoDB resolver to make a TransactGetItems request to DynamoDB to retrieve multiple items, potentially across multiple tables.
- [TransactWriteItems](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-transact-write-items.html): The TransactWriteItems request mapping document lets you tell the AWS AppSync DynamoDB resolver to make a TransactWriteItems request to DynamoDB to write multiple items, potentially to multiple tables.
- [Type system (request mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-request.html): When using the AWS AppSync DynamoDB resolver to call your DynamoDB tables, AWS AppSync needs to know the type of each value to use in that call.
- [Type system (response mapping)](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-typed-values-responses.html): When receiving a response from DynamoDB, AWS AppSync automatically converts it into GraphQL and JSON primitive types.
- [Filters](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-filter.html): When querying objects in DynamoDB using the Query and Scan operations, you can optionally specify a filter that evaluates the results and returns only the desired values.
- [Condition expressions](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-condition-expressions.html): When you mutate objects in DynamoDB by using the PutItem, UpdateItem, and DeleteItem DynamoDB operations, you can optionally specify a condition expression that controls whether the request should succeed or not, based on the state of the object already in DynamoDB before the operation is performed.
- [Transaction condition expressions](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-transaction-condition-expressions.html): Transaction condition expressions are available in request mapping templates of all four types of operations in TransactWriteItems, namely, PutItem, DeleteItem, UpdateItem, and ConditionCheck.
- [Projections](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-resolver-mapping-template-reference-dynamodb-projections.html): When reading objects in DynamoDB using the GetItem, Scan, Query, BatchGetItem, and TransactGetItems operations, you can optionally specify a projection that identifies the attributes that you want.
- [Resolver mapping template reference for RDS](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-rds.html): Resolver mapping template reference for RDS for AWS AppSync.
- [Resolver mapping template reference for OpenSearch](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-elasticsearch.html): Resolver Mapping Template Reference for Amazon OpenSearch Service for AWS AppSync.
- [Resolver mapping template reference for Lambda](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-lambda.html): AWS AppSync resolver mapping template reference for Lambda
- [Resolver mapping template reference for EventBridge](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-eventbridge.html): Resolver Mapping Template Reference for Amazon EventBridge for AWS AppSync.
- [Resolver mapping template reference for None data source](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-none.html): Resolver mapping template reference for data source of type *None*.

### [Resolver mapping template reference for HTTP](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-http.html)

Resolver mapping template reference for HTTP for AWS AppSync.

- [Certificate Authorities (CA) Recognized by AWS AppSync for HTTPS Endpoints](https://docs.aws.amazon.com/appsync/latest/devguide/http-cert-authorities.html): Certificate authorities (CA) recognized by AWS AppSync for HTTPS endpoints.
- [Resolver mapping template changelog](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-changelog.html): Resolver mapping template changelog for AWS AppSync.


## [GraphQL type reference](https://docs.aws.amazon.com/appsync/latest/devguide/type-reference.html)

- [Scalar types in GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/scalars.html): Learn about GraphQL scalar types in AWS AppSync.
- [Interfaces and unions in GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/interfaces-and-unions.html): Interface and union types in GraphQL.
