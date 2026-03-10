# Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/llms.txt

# Amazon DynamoDB Developer Guide

> Amazon DynamoDB is a fast, fully managed NoSQL database as a service that makes it simple and cost-effective to store and retrieve any amount of data, and serve any level of request traffic.

- [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Migrating to DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/migration-guide.html)
- [API reference](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CurrentAPI.html)
- [Document history](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html)

## [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)

- [First-time user resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dynamodb-resources-first-time-users.html): A curated guide to essential DynamoDB learning resources, including documentation, tools, training, and best practices to help first-time users successfully get started with Amazon DynamoDB.
- [Accessing DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AccessingDynamoDB.html): You can access DynamoDB using the console, the AWS CLI, or the API.

### [Setting up DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html)

Set up the DynamoDB web service or its local downloadable version for developing and testing applications locally without accessing the cloud.

- [Setting up DynamoDB (web service)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.DynamoWebService.html): Set up the DynamoDB web service by signing up for AWS, getting your access and secret key, and installing the AWS CLI.

### [Setting up DynamoDB local (downloadable version)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

Learn how to set up and use DynamoDB local, a downloadable version of DynamoDB local that enables local, cost-effective development and testing.

- [Deploying](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html): Learn how to download and deploy Amazon DynamoDB locally on your computer.
- [Usage notes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.UsageNotes.html): Discover important tips for using and running DynamoDB local locally on your computer.
- [Release history](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html): Find the revision dates, related releases, and important changes to DynamoDB local.
- [DynamoDB local telemetry](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalTelemetry.html): Understand telemetry when using DynamoDB local.
- [Step 1: Create a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html): Create a DynamoDB table with partition and sort keys using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 2: Write data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-2.html): Populate data in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 3: Read data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-3.html): Read an item from a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 4: Update data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-4.html): Update an item in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 5: Query data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-5.html): Query the data in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 6: (Optional) clean up](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-6.html): Delete a DynamoDB table to clean up resources using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Next steps](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-NextSteps.html): Learn advanced DynamoDB concepts and best practices to build scalable, high-performance applications on AWS's fully managed NoSQL database service.
- [Console-to-Code](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/console-to-code.html): Transform manual DynamoDB table creation into reproducible automation code using Amazon Q Developer's Console-to-Code feature.


## [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html)

- [Cheat sheet](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CheatSheet.html): Explore a quick reference for working with DynamoDB and its various AWS SDKs, covering initial setup, SDK/CLI choices, basic actions like creating tables and querying data, naming rules, and key service basics.
- [Core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html): Learn about the building blocks of DynamoDB your app will need.
- [DynamoDB API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html): Learn how to work with the DynamoDB API.
- [Supported data types and naming rules](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html): Learn about the supported data types and naming rules for entities when using Amazon DynamoDB.
- [DynamoDB table classes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.TableClasses.html): Understand the basics of DynamoDB's table classes.
- [Partitions and data distribution in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html): Understand the basic concepts of partitions in DynamoDB.

### [Learn how to go from SQL to NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html)

Learn how to apply your existing SQL knowledge for performing similar tasks in Amazon DynamoDB.

- [Relational or NoSQL?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.WhyDynamoDB.html): Compare use cases and characteristics of relational (SQL) databases with Amazon DynamoDB to understand the two technologies and decide which is best for your workloads.
- [Accessing and authentication](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.Accessing.html): Understand the differences in connecting, interacting, accessing, authentication, authorization, requests, and responses in relational (SQL) vs.
- [Creating a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.CreateTable.html): Compare the CREATE TABLE statement in SQL with the CreateTable operation in Amazon DynamoDB.
- [Getting information about a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.GetTableInfo.html): Learn the key differences between the DESCRIBE TABLE statement in a Relational (SQL) database and the DescribeTable operation in Amazon DynamoDB
- [Writing data to a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.WriteData.html): Learn the key differences between the INSERT statement in a Relational (SQL) database, and the PutItem and ExecuteStatement operations in Amazon DynamoDB.

### [Reading data from a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.html)

Learn the key differences between the SELECT statement in a relational (SQL) database and the GetItem, Query, and Scan operations in Amazon DynamoDB.

- [Reading an item using its primary key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.SingleItem.html): Compare reading a single row (item) using the SELECT statement in a Relational (SQL) database with the GetItem operation in Amazon DynamoDB.
- [Querying a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.Query.html): Compare reading multiple rows (items) using the SELECT statement in a relational (SQL) database with the Query operation in Amazon DynamoDB.
- [Scanning a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.Scan.html): Compare full table scans using the SELECT statement in a relational (SQL) database with the Scan operation in Amazon DynamoDB.
- [Managing indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.Indexes.html): Compare the process of managing indexes in a relational (SQL) database with that in Amazon DynamoDB.
- [Modifying data in a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.UpdateData.html): Compare modifying data using the UPDATE statement in a relational (SQL) database with the UpdateItem operation and PartiQL Update statement in Amazon DynamoDB.
- [Deleting data from a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.DeleteData.html): Compare deleting data using the DELETE statement in a relational (SQL) database with the DeleteItem operation in Amazon DynamoDB.
- [Removing a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.RemoveTable.html): Compare removing a table using the DROP TABLE statement in a relational (SQL) database with the DeleteTable operation in Amazon DynamoDB.
- [Amazon DynamoDB learning resources and tools](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AdditionalResources.html): You can use the additional resources provided to better understand and work with DynamoDB.


## [Reads and writes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-reads-writes.html)

- [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html): Explore the differences between eventually consistent reads and strongly consistent reads for tables and indexes in DynamoDB.
- [Read and write operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html): Learn how DynamoDB read and write operations consume capacity units.


## [DynamoDB throughput capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)

### [DynamoDB on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)

Use DynamoDB on-demand capacity mode, a serverless, pay-per-request billing option, which automatically scales to your workloadâs traffic volume without capacity planning.

- [DynamoDB maximum throughput for on-demand tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode-max-throughput.html): Learn how to set maximum throughput for DynamoDB on-demand tables to optimize costs and protect against excessive usage, and safeguard downstream services.

### [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html)

Use DynamoDB provisioned capacity mode to specify the desired read and write throughput capacities when you create a table and enable capacity planning.

### [Managing throughput capacity with auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

DynamoDB auto scaling uses Application Auto Scaling to dynamically adjust provisioned throughput capacity, enabling tables or global secondary indexes to handle sudden traffic increases without throttling.

- [Using the AWS Management Console with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html): This section provides a comprehensive guide on using the AWS Console to manage DynamoDB auto scaling, including creating new tables with auto scaling enabled, enabling auto scaling on existing tables, viewing auto scaling activities, and modifying or disabling auto scaling settings.
- [Using the AWS CLI to manage DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.CLI.html): This tutorial demonstrates how to use the AWS CLI to manage DynamoDB auto scaling.
- [Using the AWS SDK to configure auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.HowTo.SDK.html): Learn how to add, change, and delete auto scaling values when in provisioned capacity mode for Amazon DynamoDB tables when using Python, Java, Node.js, Go, and other AWS SDKs.
- [Reserved capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/reserved-capacity.html): Learn how to reduce costs for DynamoDB provisioned capacity tables using reserved capacity.

### [Warm throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/warm-throughput.html)

Warm throughput refers to the number of read and write operations your DynamoDB table can instantaneously support.

- [Check your table's warm throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/check-warm-throughput.html): Use the following AWS CLI and AWS Console instructions to check your table or index's current warm throughput value.
- [Increase your table's warm throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/update-warm-throughput.html): Once you've checked your DynamoDB table's current warm throughput value, you can update it with the following steps:
- [Create a table with higher warm throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/create-table-warm-throughput.html): You can adjust the warm throughput values when you create your DynamoDB table by following the steps below.
- [Warm throughput scenarios](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/warm-throughput-scenarios.html): Here are some different scenarios you might encounter when working with DynamoDB warm throughput.
- [Burst and adaptive capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/burst-adaptive-capacity.html): Use burst capacity to temporarily exceed your provisioned throughput for brief periods of time.
- [Switching capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-switching-capacity-modes.html): Learn the best practices for switching between on-demand and provisioned capacity modes for your existing Amazon DynamoDB tables.


## [Programming with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.html)

### [Overview of AWS SDK support for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html)

Learn the basics of using AWS SDKs with Amazon DynamoDB.

- [Programmatic interfaces that work with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKs.Interfaces.html): Learn about the AWS SDK interfaces that are available for developing with Amazon DynamoDB.

### [Higher-level programming interfaces](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HigherLevelInterfaces.html)

Develop applications for Amazon DynamoDB using the AWS SDKs for Java, PHP, and .NET.

### [Java 1.x: DynamoDBMapper](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.html)

Explore how to map your client-side classes to the Amazon DynamoDB tables using the DynamoDBMapper class in the AWS SDK for Java.

- [DynamoDBMapper Class](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Methods.html): Use the DynamoDBMapper class to interact with data in Amazon DynamoDB tables.
- [Supported Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html): Learn about the data types supported when using DynamoDB Mapper and the AWS SDK for Java.
- [Java Annotations for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Annotations.html): Learn about the annotations that are available for mapping your classes and properties to tables and attributes in Amazon DynamoDB.
- [Optional configuration settings for DynamoDBMapper](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.OptionalConfig.html): Use optional configuration settings for DynamoDBMapper usage with Amazon DynamoDB.
- [Optimistic Locking With Version Number](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.OptimisticLocking.html): Ensure matching client-side and server-side items by using the optimistic locking with version number with the DynamoDBMapper class in the AWS SDK for Java.
- [Mapping Arbitrary Data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.ArbitraryDataMapping.html): Map arbitrary data to the Amazon DynamoDB types using the DynamoDBMapper class of the AWS SDK for Java.
- [DynamoDBMapper examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.Examples.html): Learn how to use a variety of Java code examples for the DynamoDBMapper class in the AWS SDK for Java.
- [Java 2.x: DynamoDB Enhanced Client](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBEnhanced.html): Explore how to map your client-side classes to the Amazon DynamoDB tables using the DynamoDB Enhanced Client in the AWS SDK for Java.
- [.NET: Document model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKMidLevel.html): Use the .NET SDK's document model classes to simplify your DynamoDB operations for efficient data handling.

### [.NET: Object persistence model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html)

Map your client-side classes to the Amazon DynamoDB tables using the object persistence model of the AWS SDK for .NET.

- [DynamoDB attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DeclarativeTagsList.html): Lists the attributes the object persistence model offers so you can map your .NET classes and properties to Amazon DynamoDB tables and attributes.
- [DynamoDBContext class](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetDynamoDBContext.html): Access your data in tables, perform various CRUD operations, and run queries with the DynamoDBContext class.
- [Optimistic locking using version number](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBContext.VersionSupport.html): Ensure matching client-side and server-side items by using the optimistic locking with version number with the AWS SDK for .NET object persistence model.
- [Mapping arbitrary data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBContext.ArbitraryDataMapping.html): Map arbitrary data to the Amazon DynamoDB types using the AWS SDK for .NET object persistence model.

### [Running the code examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CodeSamples.html)

Explore official code examples for Amazon DynamoDB in AWS SDKs like Java, .NET, Node.js, Python, Go, Ruby, JavaScript, and others.

- [Load sample data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SampleData.html): For code examples on creating tables in DynamoDB, loading a sample dataset to operate on, querying the data, and then cleaning up, see the links below.
- [Java code examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CodeSamples.Java.html): Develop applications for Amazon DynamoDB item and table operations using the AWS SDK for Java.
- [.NET code examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CodeSamples.DotNet.html): Develop applications for Amazon DynamoDB using the AWS SDKs for Java, PHP, and .NET.
- [Low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html): Learn about how Amazon DynamoDB processes requests and replies at the lowest API level.
- [Programming with Python](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html): Learn different concepts related to how to program DynamoDB with Python.
- [Programming with JavaScript](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-javascript.html): Learn different concepts related to how to program DynamoDB with JavaScript.
- [Programming with the AWS SDK for Java 2.x](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProgrammingWithJava.html): Learn different concepts about how to program DynamoDB with the AWS SDK for Java 2.x.
- [Error handling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html): Discover the best practices for handling client and server errors and exceptions returned by Amazon DynamoDB operations.
- [Working with AWS SDKs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Working with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithDynamo.html)

### [Working with tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html)

Learn how to work with DynamoDB tables using the AWS CLI and SDKs to optimize your database operations, build scalable applications, and improve their performance.

- [Basic operations on tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html): Learn how to perform basic CRUD operations to create, describe, update, and delete DynamoDB tables.
- [Considerations when choosing a table class in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.tableclasses.html): Learn how to choose between DynamoDB Standard and Standard-IA table classes to optimize costs based on your storage and throughput needs.

### [Tags and labels](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html)

Learn to use AWS tags to label and categorize resources in DynamoDB by purpose, owner, environment, or other criteria.

- [Tagging resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.Operations.html): Use the DynamoDB console, AWS CLI, or API to add, list, edit, or delete tags various Amazon DynamoDB resources.

### [Working with global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

DynamoDB global tables provide multi-Region, multi-active database replication for fast, localized performance and high availability in global applications.

- [Core concepts](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-CoreConcepts.html): Learn DynamoDB global tables core concepts.

### [Same-account global table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-SameAccount.html)

Same-account global tables automatically replicate your DynamoDB table data across AWS Regions within a single AWS account.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html): Learn how DynamoDB global tables enable multi-Region replication with automatic synchronization across replica tables.
- [Tutorials: Creating global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables.tutorial.html): Use the global tables feature in DynamoDB to create a multi-region, active/active group of tables to replicate your data using the console, AWS CLI, or API.
- [Security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-security.html): Learn how to grant access and secure DynamoDB global tables using IAM and AWS KMS encryption.

### [Multi-account global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-MultiAccount.html)

Learn how DynamoDB multi-account global tables replicate data across multiple AWS accounts and Regions for enhanced security, governance, and fault isolation.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_MA_HowItWorks.html): Learn how DynamoDB global tables enable multi-Region replication with automatic synchronization across replica tables.
- [Tutorials: Creating multi-account global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_MA.tutorial.html): Use the global tables feature in DynamoDB to create a multi-region, active/active group of tables to replicate your data using the console, AWS CLI, or API.
- [Security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html): Learn how to grant access and secure DynamoDB global tables using IAM and AWS KMS encryption.
- [Global tables billing](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/global-tables-billing.html): This guide describes how DynamoDB billing works for global tables, identifying the components that contribute to the cost of global tables, including a practical example.
- [Global tables versions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_versions.html): Learn about DynamoDB global tables versions and how to determine which version you're using.
- [Global tables best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-bestpractices.html): The following sections describe best practices for deploying and using global tables.

### [Working with items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html)

The basic building blocks of Amazon DynamoDB start with tables, items, and attributes.

- [Item sizes and formats](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CapacityUnitCalculations.html): Learn how DynamoDB calculates item sizes and storage costs.

### [Using expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.html)

Use expressions in Amazon DynamoDB to indicate the attributes to retrieve (projection expressions), conditions under which to read or write them (condition expressions), and any updates or deletes to be performed (update expressions).

- [Specifying item attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.Attributes.html): Learn the basics of specifying item attributes in an expression in Amazon DynamoDB when you need to specify a condition that must be met for an operation to complete.
- [Expression attribute names](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html): When querying or scanning in Amazon DynamoDB, use an expression attribute name, a placeholder used as an alternative to an actual attribute name in an expression.
- [Expression attribute values](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeValues.html): If you need to compare an attribute with a value in a DynamoDB that you might not know until runtime, define an expression attribute value as a placeholder for an actual value.
- [Projection expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ProjectionExpressions.html): Learn how to use a projection expression in Amazon DynamoDB to indicate the attributes to retrieve.
- [Update expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html): To update a DynamoDB item's attributes, use an action of an update expression in an API call.
- [Condition and filter expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html): Learn about using operators and functions for filter expressions and condition expressions in DynamoDB.
- [CLI example](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html): Condition expressions in DynamoDB allow you to specify conditions for read and write operations, enabling conditional puts, deletes, and updates to control data access and modification.

### [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)

Learn how to set up and use Time to Live (TTL) on DynamoDB tables to automatically expire items from a table.

- [Enable TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html): Learn the information you need to enable Time to Live with DynamoDB tables using the DynamoDB console, AWS CLI, the AWS SDKs, or CloudFormation
- [Computing TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-before-you-start.html): Learn how to create and update TTL items in your DynamoDB table.
- [Working with expired items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ttl-expired-items.html): Learn about working with expired items in Time to Live and how you can filter them from read and write operations.

### [Querying tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html)

Learn to search DynamoDB table data where the query operations search only primary key attribute values.

- [Key condition expressions for queries](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.KeyConditionExpressions.html): Learn how to use a key condition expression to specify the search criteria.
- [Filter expressions for queries](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html): Learn how to use filter expressions to refine your query results.
- [Paginating query results](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.Pagination.html): Learn to use pagination when querying Amazon DynamoDB tables.
- [Other aspects of queries](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.Other.html): Learn how to limit the number of items returned, to receive a count of the number of items returned, to find out how many capacity units were consumed in the query, and how to receive strongly consistent reads if desired.
- [Scanning tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html): If you need to search in any item's attribute in a DynamoDB table, use a scan to examine all data in the entire table.

### [PartiQL query language](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html)

Learn how and when to use the DynamoDB implementation of the PartiQL query language, a SQL-compatible query language.

- [Getting started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-gettingstarted.html): Use PartiQL for DynamoDB using the console, AWS CLI, or API.
- [Data types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.data-types.html): Explore the supported data types, with examples of each, for the DynamoDB implementation of the PartiQL query language.

### [Statements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.statements.html)

Learn the basic CRUD operations supported by the PartiQL query language in Amazon DynamoDB and how they relate to SQL statements.

- [Select](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.select.html): Learn about the SELECT statement when using PartiQL query language for DynamoDB.
- [Update](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.update.html): Learn about the UPDATE statement when using the PartiQL query language for DynamoDB.
- [Delete](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.delete.html): Learn about the DELETE statement when using the PartiQL query language for DynamoDB.
- [Insert](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.insert.html): Learn about the INSERT statement when using the PartiQL query language for DynamoDB.

### [Functions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.html)

Learn how to use the functions supported by the PartiQL query language in Amazon DynamoDB and how they relate to SQL statements.

- [Exists](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.exists.html): Learn about the EXISTS function when using the PartiQL query language for DynamoDB.
- [Begins_with](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.beginswith.html): Learn about the BEGINS_WITH function when using the PartiQL query language for DynamoDB.
- [Missing](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.missing.html): Learn about the MISSING function when using the PartiQL query language for DynamoDB.
- [Attribute_type](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.attribute_type.html): Learn about the ATTRIBUTE_TYPE function when using the PartiQL query language for DynamoDB.
- [Contains](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.contains.html): Learn about the CONTAINS function when using the PartiQL query language for DynamoDB.
- [Size](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-functions.size.html): Learn about the SIZE function when using the PartiQL query language for DynamoDB.
- [Operators](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-operators.html): Learn about the supported operators and what you can accomplish with them using PartiQL for Amazon DynamoDB.
- [Transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.multiplestatements.transactions.html): Explore how to use transactions when using the PartiQL query language with Amazon DynamoDB.
- [Batch operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.multiplestatements.batching.html): Explore how to use batch operations when using the PartiQL query language with Amazon DynamoDB.
- [IAM policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-iam.html): Use IAM policies to configure PartiQL for DynamoDB.

### [Working with items: Java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/JavaDocumentAPIItemCRUD.html)

Learn to perform create, read, update, and delete (CRUD) operations on DynamoDB items using the AWS SDK for Java.

- [Example: CRUD operations - Java document API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/JavaDocumentAPICRUDExample.html): Java code example showing how to create, read, update, and delete (CRUD) operations on an item in DynamoDB using the AWS SDK for Java.
- [Example: Batch operations - Java document API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/batch-operation-document-api-java.html): Java code example showing how to perform batch write operations in DynamoDB using the AWS SDK for Java Document API.
- [Example: Handling binary type attributes - Java document API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/JavaDocumentAPIBinaryTypeExample.html): Java code example showing how to handle binary type attributes in DynamoDB using the AWS SDK for Java.

### [Working with items: .NET](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetItemCRUD.html)

Create, read, update, and delete (CRUD) operations on an item in a table with the AWS SDK for .NET.

- [Example: CRUD operations - .NET low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetItemsExample.html): A C# code example showing how to create, read, update, and delete (CRUD) operations on a DynamoDB item using the AWS SDK for .NET.
- [Example: Batch operations - .NET low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/batch-operation-lowlevel-dotnet.html): C# code example showing how to batch write operations on a DynamoDB item using the AWS SDK for .NET.
- [Example: Handling binary type attributes - .NET low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LowLevelDotNetBinaryTypeExample.html): C# code example showing how to handle binary type attributes using the AWS SDK for .NET.

### [Working with indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)

Improve data access in DynamoDB using secondary indexes.

### [Global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)

Use global secondary indexes to perform alternate queries from the base DynamoDB table to model your application's various access patterns.

### [Design patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.DesignPatterns.html)

Learn proven design patterns for using global secondary indexes effectively in your DynamoDB applications.

- [Multi-attribute keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.DesignPattern.MultiAttributeKeys.html): Use multi-attribute keys in global secondary indexes to create composite keys from multiple attributes without manual concatenation.
- [Managing Global Secondary Indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html): Create, modify, and delete global secondary indexes online in Amazon DynamoDB.
- [Detecting and correcting index key violations in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.ViolationDetection.html): Detect and correct violations in Amazon DynamoDB secondary indexes.

### [Global Secondary Indexes: Java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSIJavaDocumentAPI.html)

Create a table with one or more global secondary indexes in DynamoDB using the AWS SDK for Java.

- [Example: Global Secondary Indexes - Java document API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSIJavaDocumentAPI.Example.html): Provides a Java code example of how to work with global secondary indexes using the AWS SDK for Java Document API.

### [Global Secondary Indexes: .NET](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSILowLevelDotNet.html)

Create a table with one or more global secondary indexes in DynamoDB using the AWS SDK for .NET.

- [Example: Global Secondary Indexes - .NET low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSILowLevelDotNet.Example.html): Provides a C# code example of how to work with global secondary indexes using the AWS SDK for .NET low-level API.
- [Global Secondary Indexes: AWS CLI](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GCICli.html): Create a table with one or more global secondary indexes in DynamoDB using the AWS CLI.

### [Local secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html)

Learn how to use local secondary indexes to efficiently query table data using alternate sort keys.

### [Local Secondary Indexes: Java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSIJavaDocumentAPI.html)

Create a table with one or more local secondary indexes in DynamoDB using the AWS SDK for Java.

- [Example: Local Secondary Indexes - Java document API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSIJavaDocumentAPI.Example.html): Create a local secondary index in DynamoDB with this Java code example using the AWS SDK for Java Document API.

### [Local Secondary Indexes: .NET](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSILowLevelDotNet.html)

Create a table with one or more local secondary indexes in DynamoDB using the AWS SDK for .NET.

- [Example: Local Secondary Indexes - .NET low-level API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSILowLevelDotNet.Example.html): Create a local secondary index in DynamoDB with this C# code example using the AWS SDK for .NET low-level API.
- [Local Secondary Indexes: AWS CLI](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LCICli.html): Learn how to use the AWS CLI to create, describe, and query DynamoDB tables with local secondary indexes for efficient data access and querying by non-key attributes.

### [Working with transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html)

Use DynamoDB transactions to manage complex workflows by grouping multiple actions into a single atomic and ACID operation.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html): Learn how DynamoDB transactions work, including API operations, capacity management, error handling, best practices, and details for using transactional operations.
- [Using IAM with transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis-iam.html): Use IAM to restrict the actions that DynamoDB transactions can perform and enhance your database security and compliance.
- [Example code](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-example.html): An example Java application that demonstrates how to use DynamoDB transactions to manage a business workflow.

### [Working with streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/streamsmain.html)

Learn about capturing changes to items stored in a DynamoDB table at the point in time when changes occur.

### [Working with Kinesis Data Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html)

Use Kinesis Data Streams to capture changes to DynamoDB.

- [Getting started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds_gettingstarted.html): Learn how to capture data changes in DynamoDB table items using Kinesis Data Streams.
- [Using shards and monitoring shard-level metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds_using-shards-and-metrics.html): Learn how to use shards and metrics in DynamoDB Streams with Kinesis Data Streams.
- [Using IAM policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds_iam.html): Learn how to create custom AWS Identity and Access Management (IAM) policies to secure Amazon DynamoDB integrations with Kinesis Data Streams.

### [Working with DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)

Learn how DynamoDB Streams captures item-level modifications in tables in near-real time.

- [DynamoDB Streams and TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-streams.html): Learn how to use an external operation (e.g., a Lambda function) with DynamoDB Streams to capture when an item is deleted from a table and how to determine if it's a user or TTL expired system delete.

### [Using the DynamoDB Streams Kinesis adapter to process stream records](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.KCLAdapter.html)

Use the Kinesis Client Library (KCL) to process data from DynamoDB Streams.

- [Migrating from KCL 1.x to KCL 3.x](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/streams-migrating-kcl.html): This section provides instructions for migrating your consumer application from KCL 1.x to KCL 3.x.
- [Roll back to the previous KCL version](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kcl-migration-rollback.html): Learn how to roll back your consumer application to the previous KCL version.
- [Roll forward to KCL 3.x after a rollback](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kcl-migration-rollforward.html): Learn how to roll forward your consumer application to KCL 3.x after a rollback.

### [Walkthrough: DynamoDB Streams Kinesis adapter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.KCLAdapter.Walkthrough.html)

Create a Java application that uses the Amazon Kinesis Client Library and the Amazon DynamoDB Streams Kinesis Adapter.

- [Complete program: DynamoDB Streams Kinesis adapter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.KCLAdapter.Walkthrough.CompleteProgram.html): View a complete program for using the DynamoDB Streams Kinesis Adapter with DynamoDB.
- [DynamoDB Streams low-level API: Java example](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.LowLevel.Walkthrough.html): View java code to see and learn about using the low-level API for DynamoDB Streams.

### [DynamoDB Streams and AWS Lambda triggers](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html)

When you need database triggers in DynamoDB, use the combined power of DynamoDB Streams and Lambda functions.

- [Tutorial #1: Processing all events](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html): Follow this step by step tutorial to create a database trigger with Lambda and Amazon DynamoDB using node.js, IAM, AWS CLI, and JSON with a real world example.
- [Tutorial #2: Processing some events](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial2.html): Follow this step by step tutorial to create a database trigger with Lambda and Amazon DynamoDB using node.js, IAM, AWS CLI, and JSON with a real world example.
- [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.BestPracticesWithDynamoDB.html): Explore the best practices when unleashing the combined power of AWS Lambda and Amazon DynamoDB.
- [DynamoDB Streams and Apache Flink](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/StreamsApacheFlink.xml.html): Learn more about using Amazon Managed Service for Apache Flink to process DynamoDB stream records.


## [In-memory acceleration with DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html): Explore how the DynamoDB in-memory cache service DAX can accelerate read access for your critical workloads, with information about Amazon VPC, node makeup, security groups, and networking.
- [DAX cluster components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html): Explore the key components and operational aspects of the DAX, a fully managed, highly available, in-memory data store that provides fast read performance for applications using DynamoDB.

### [Creating a DAX cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.html)

Set up and use DAX (the DynamoDB in-memory caching layer) in your default Amazon VPC environment by creating a basic cluster using the console or AWS CLI.

- [DAX and IPv6](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.DAX_and_IPV6.html): DynamoDB DAX now supports IPv6 addressing, that allows you to create clusters that operate in IPv4-only, IPv6-only, or dual-stack networking modes.
- [Using the AWS CLI](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.cli.html): Explore step-by-step instructions on how to create a DAX cluster using the AWS CLI, including setting up an IAM service role, creating a subnet group, and configuring security group inbound rules.
- [Using the console](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.console.html): Use the console to set up and use DAX (the DynamoDB in-memory caching layer) in your default Amazon VPC environment by creating a basic cluster.
- [Consistency models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html): Understand the consistency models of DAX and DynamoDB to ensure your application behaves as expected when using the DAX caching service.

### [Developing with the DAX client](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.html)

Learn to develop with the Amazon DynamoDB Accelerator (DAX) client to securely connect your applications to DAX and speed up your DynamoDB read throughput.

### [Tutorial: Running a sample application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.sample-app.html)

Run sample applications that use DAX to accelerate DynamoDB reads on an Amazon EC2 instance, configure AWS credentials, and test DAX performance.

- [Step 1: Launch an EC2 instance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.launch-ec2-instance.html): Launch an Amazon EC2 instance in your default Amazon VPC, and then install and run the DAX client software on that instance.
- [Step 2: Create a user and policy](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.create-user-policy.html): Learn how to create an administrative user and configure a policy that grants access to DAX clusters and DynamoDB for secure interaction with your DAX cluster.
- [Step 3: Configure an EC2 instance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.configure-ec2-instance.html): Configure an Amazon EC2 instance to use with DAX.

### [Step 4: Run a sample application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application.html)

Test the functionality of DAX by running sample applications in different programming languages on your Amazon EC2 instance and verify DAX performance.

### [Node.js and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs-3.html)

Test DAX functionality and performance by running the Node.js sample application on your Porting Assistant for .NET instance.

- [Client configuration](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX-client-config-JS.html): Explore the default configuration settings for the DAX JavaScript client, including key parameters for region, endpoint, timeouts, retries, credentials, and cluster health monitoring.
- [Migrating to DAX Node.js SDK V3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs-3-migrating.html): This migration guide will help you transition your existing DAX Node.js applications.
- [TryDax.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.tutorial-TryDax.html)

### [Go and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-go-2.html)

Test DAX functionality and performance by running the SDK for Go sample application on your Porting Assistant for .NET instance.

- [Client configuration](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX-client-config-Go.html): Explore the default configuration settings for the DAX Go client, including key parameters for region, endpoint, timeouts, retries, credentials, and cluster health monitoring.
- [Migrating to DAX Go SDK V2](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-go-migrating.html): This migration guide will help you transition your existing DAX Go applications.

### [Java and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-java.html)

Test DAX functionality and performance by running the Java sample application on your Porting Assistant for .NET instance.

- [TryDax.java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.TryDax.java.html): Test DAX functionality and performance by running the TryDax.java sample application on your Porting Assistant for .NET instance.

### [.NET and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.html)

Test DAX functionality and performance by running the .NET sample application on your Porting Assistant for .NET instance.

- [01-CreateTable.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.01-CreateTable.html): Test DAX functionality using the 01-CreateTable.cs program in the .NET sample application.
- [02-Write-Data.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.02-Write-Data.html): Test DAX functionality using the 02-Write-Data.cs program in the .NET sample application.
- [03-GetItem-Test.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.03-GetItem-Test.html): Test DAX functionality using the 03-GetItem-Test.cs program in the .NET sample application.
- [04-Query-Test.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.04-Query-Test.html): Test DAX functionality using the 04-Query-Test.cs program in the .NET sample application.
- [05-Scan-Test.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.05-Scan-Test.html): Test DAX functionality using the 05-Scan-Test.cs program in the .NET sample application.
- [06-DeleteTable.cs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-dotnet.06-DeleteTable.html): Test DAX functionality using the 06-DeleteTable.cs program in the .NET sample application.

### [Python and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.html)

Test DAX functionality and performance by running the Python sample application on your Porting Assistant for .NET instance.

- [01-create-table.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.01-create-table.html): Test DAX functionality using the 01-create-table.py program in the Python sample application.
- [02-write-data.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.02-write-data.html): Test DAX functionality using the 02-write-data.py program in the Python sample application.
- [03-getitem-test.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.03-getitem-test.html): Test DAX functionality using the 03-getitem-test.py program in the Python sample application.
- [04-query-test.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.04-query-test.html): Test DAX functionality using the 04-query-test.py program in the Python sample application.
- [05-scan-test.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.05-scan-test.html): Test DAX functionality using the 05-scan-test.py program in the Python sample application.
- [06-delete-table.py](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.06-delete-table.html): Test DAX functionality using the 06-delete-table.py program in the Python sample application.
- [Modifying an existing application to use DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.modify-your-app.html): Modify a Java application that uses DynamoDB so that it can access a DAX cluster.
- [Managing DAX clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html): Discover the common management tasks necessary to operate and maintain a high-performance and scalable caching tier for Amazon DynamoDB with DynamoDB Accelerator (DAX)

### [Monitoring DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Monitoring.html)

Monitoring DynamoDB Accelerator (DAX) is critical for maintaining reliability and performance.

- [DAX monitoring tools](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-monitoring-automated-manual.html): Learn how to monitor DAX using automated CloudWatch metrics, alarms, logs, and events.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-monitoring-cloudwatch.html)

You can monitor DAX using CloudWatch, which collects and processes raw data from DAX into readable, near real-time metrics.

- [Metrics and dimensions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-metrics-dimensions-dax.html): View DAX metrics and dimensions for CloudWatch.
- [Creating alarms](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-creating-alarms.html): You can create alarms that respond to observed metrics over time.
- [Production monitoring](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-production-monitoring.html): Learn about monitoring your production environment with DAX and CloudWatch.
- [Logging DAX operations using AWS CloudTrail](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-logging-using-cloudtrail.html): Learn how to access DAX API call history when you enable AWS CloudTrail.
- [DAX T3/T2 burstable instances](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Burstable.html): DAX allows you to choose between fixed performance instances (such as R4 and R5) and burstable performance instances (such as T2 and T3).
- [DAX access control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.html): Amazon DynamoDB and DAX are separate AWS services and have different security models implementation of AWS Identity and Access Management (IAM) security roles and policies.
- [DAX encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html): DAX encryption at rest secures your data with AES-256 and integrates with AWS KMS, providing an additional layer of protection for your cloud applications.
- [DAX encryption in transit](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html): Learn how DynamoDB Accelerator (DAX) can enhance the security of your application with encryption in transit.
- [Using service-linked roles for DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/using-service-linked-roles.html): Fine-grained security is crucial to a well-architected caching system.
- [Accessing DAX across AWS accounts](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cross-account-access.html): Learn how to access a DAX cluster in a different AWS account using IAM roles and VPC peering to enable cross-account application access.
- [DAX cluster sizing guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.sizing-guide.html): Advice for choosing an appropriate DAX cluster size and node type.


## [Data modeling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling.html)

- [Working with Item Collections](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItemCollections.html): Learn how to work with item collections in your DynamoDB tables and secondary indexes.
- [Data modeling foundations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-foundations.html): Explore the foundations of data modeling in DynamoDB, examining the advantages and disadvantages of single table and multiple table design patterns to optimize data access, performance, and cost.
- [Data modeling building blocks](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-blocks.html): Explore the key building blocks for effective data modeling in DynamoDB, including composite sort keys, multi-tenancy, sparse indexes, time to live, vertical partitioning, and write sharding strategies.

### [Data modeling schema design packages](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-schemas.html)

Learn about the different schema packages, their business use case, design, and access patterns that you can use in DynamoDB.

- [Social network](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-schema-social-network.html): Learn how to design a social network system using DynamoDB.
- [Gaming profile](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-schema-gaming-profile.html): Learn how to design a gaming profile system using DynamoDB.
- [Complaint management system](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-complaint-management.html): Learn how to design a complaint management system using DynamoDB.
- [Recurring payments](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-schema-recurring-payments.html): Learn how to design a recurring payments system using DynamoDB.
- [Device status updates](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-device-status.html): Learn how to design a schema to monitor device status updates using DynamoDB.
- [Online shop](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-online-shop.html): Learn how to design a DynamoDB schema for an online shop, including use cases, access patterns, and a step-by-step approach to achieve the required access patterns using a single table design and global secondary indexes.

### [Relational modeling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-relational-modeling.html)

Learn about best practices for modeling relational data in DynamoDB, including how DynamoDB eliminates the need for JOIN operations and reduces overhead compared to traditional relational database management systems.

- [First steps](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql.html): Learn about the steps for modeling relational data in DynamoDB, including the importance of understanding access patterns and using de-normalization and composite keys to design an efficient schema.
- [Example](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql-B.html): This example demonstrates how to model relational data in Amazon DynamoDB using entity types, compound primary keys, and global secondary indexes to support various access patterns efficiently.


## [NoSQL Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)

- [Download](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html): Download the official version of NoSQL Workbench for Amazon DynamoDB.

### [Data modeler](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.html)

Use the data modeler functionality in NoSQL Workbench to build data models in NoSQL Workbench for Amazon DynamoDB.

- [Creating a new model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.CreateNew.html): Learn how to create a new data model in DynamoDB using NoSQL Workbench.
- [Importing an existing model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.ImportExisting.html): Learn how to import existing data models into NoSQL Workbench for DynamoDB.
- [Editing an existing model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.Edit.html): Edit existing data models in NoSQL Workbench for DynamoDB.
- [Adding sample data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.AddData.html): Learn how to add sample data to your DynamoDB data model using NoSQL Workbench.
- [Adding and validating access patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.AccessPatterns.html): Learn how to add access patterns to your DynamoDB data model using NoSQL Workbench.
- [Importing from CSV](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.ImportCSV.html): Learn how to import sample data from a CSV file into NoSQL Workbench for DynamoDB.
- [Facets](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.Facets.html): Use facets in NoSQL Workbench to visualize data access patterns for DynamoDB.
- [Aggregate view](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.AggregateView.html): Use the aggregate view in NoSQL Workbench for DynamoDB to visualize all tables in your data model.
- [Exporting a model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.ExportModel.html): Learn how to export your data models in NoSQL Workbench model format or AWS CloudFormation JSON template format for further use or deployment.
- [Committing a data model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.Commit.html): Commit your data model to DynamoDB using NoSQL Workbench.

### [Operation builder](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.html)

Use the operation builder in NoSQL Workbench to view, explore, and query live datasets.

- [Connecting to datasets](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.connect.html): Learn how to connect NoSQL Workbench to your DynamoDB tables using AWS account credentials or DynamoDB local for local development and testing.

### [Building operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.operationbuilder.html)

Learn how to use NoSQL Workbench for DynamoDB to build and save complex data plane operations with visual tools and generate sample code.

- [PartiQL statements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.partiql.html): Learn how to build and run PartiQL statements in NoSQL Workbench for DynamoDB.
- [API operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.operationbuilder.api.html): Use NoSQL Workbench operation builder to run DynamoDB CRUD API operations.
- [Cloning tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.cloning-tables.html): Learn how to clone DynamoDB tables using NoSQL Workbench.
- [Exporting to CSV](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.exportcsv.html): Learn how to export the results from DynamoDB read API operations and PartiQL statements to a CSV file using the operation builder for NoSQL Workbench.
- [Sample data models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.SampleModels.html): Sample Data Models for NoSQL Workbench
- [Release history](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkbenchDocumentHistory.html): Find the revision dates, related releases, and important changes to NoSQL Workbench for Amazon DynamoDB.


## [Backup and restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup-and-Restore.html)

### [Point-in-time backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html)

Protect your DynamoDB tables from accidental write or delete operations with point-in-time recovery.

- [Enable point-in-time recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html): Get an overview of the point-in-time recovery functionality in DynamoDB and point-in-time restore times.

### [On-demand backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html)

Learn how to use DynamoDB's backup and restore features, including on-demand backups, point-in-time recovery, and the ability to create full backups for long-term retention and regulatory compliance, all with zero impact on table performance or availability.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackup.html): Learn how to easily back up and restore DynamoDB tables, including on-demand and continuous backups, point-in-time recovery, and cross-Region restores.
- [Backing up a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup.Tutorial.html): Explore an overview of how to create a backup for a DynamoDB table using the AWS Management Console, AWS CLI, or API.
- [Restoring a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html): In this tutorial, learn how to use the DynamoDB console or AWS CLI to restore a table from a backup.
- [Deleting a table backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Delete.Tutorial.html): In this tutorial, learn how to delete a specific Amazon DynamoDB table on-demand backup using the AWS Management Console or AWS CLI.
- [Using IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_IAM.html): Explore an overview of using IAM policies to configure backup and restore operations in DynamoDB, including examples of policies that allow or deny specific actions such as CreateBackup, RestoreTableFromBackup, ListBackups, and DeleteBackup.
- [Billing for backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backup-restore-billing.html): Learn how DynamoDB's backup and restoration features are billed, including on-demand backups, point-in-time recovery, and the impact of backup retention policies on monthly charges.

### [Restores](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/pointintimerecovery_restores.html)

Learn more about restoring tables in DynamoDB using point in time recovery.

- [Restoring a DynamoDB table to a point in time](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html): Use the DynamoDB console or AWS CLI to restore a table to a point in time.

### [Using AWS Backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorksAWS.html)

Learn how DynamoDB can be backed up and restored using the AWS Backup service.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedBackupsAWS.html): Backup and restore of DynamoDB tables is easy with AWS Backup.
- [Creating backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html): Learn how to create on-demand and scheduled backups of your DynamoDB tables using AWS Backup.
- [Copying backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CrossRegionAccountCopyAWS.html): Learn how to easily copy your DynamoDB table backups to other AWS Regions and Accounts using AWS Backup.
- [Restoring a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.TutorialAWS.html): This section describes how to restore a backup of a DynamoDB table from AWS Backup.
- [Deleting backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Delete.TutorialAWS.html): This section describes how to delete a backup of a DynamoDB table with AWS Backup.
- [On-demand backups managed by AWS Backup versus DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/UsageNotesAWS.html): This section describes the technical differences between on-demand backups managed by AWS Backup and DynamoDB.


## [Code examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_basics.html)

The following code examples show how to use the basics of DynamoDB with AWS SDKs.

- [Hello DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Hello_section.html): Hello DynamoDB
- [Learn the basics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_GettingStartedMovies_section.html): Learn the basics of DynamoDB with an AWS SDK

### [Actions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_actions.html)

The following code examples show how to use DynamoDB with AWS SDKs.

- [BatchExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_BatchExecuteStatement_section.html): Use BatchExecuteStatement with an AWS SDK
- [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_BatchGetItem_section.html): Use BatchGetItem with an AWS SDK or CLI
- [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_BatchWriteItem_section.html): Use BatchWriteItem with an AWS SDK or CLI
- [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_CreateTable_section.html): Use CreateTable with an AWS SDK or CLI
- [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_DeleteItem_section.html): Use DeleteItem with an AWS SDK or CLI
- [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_DeleteTable_section.html): Use DeleteTable with an AWS SDK or CLI
- [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_DescribeTable_section.html): Use DescribeTable with an AWS SDK or CLI
- [DescribeTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_DescribeTimeToLive_section.html): Use DescribeTimeToLive with an AWS SDK or CLI
- [ExecuteStatement](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_ExecuteStatement_section.html): Use ExecuteStatement with an AWS SDK
- [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_GetItem_section.html): Use GetItem with an AWS SDK or CLI
- [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_ListTables_section.html): Use ListTables with an AWS SDK or CLI
- [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PutItem_section.html): Use PutItem with an AWS SDK or CLI
- [Query](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Query_section.html): Use Query with an AWS SDK or CLI
- [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scan_section.html): Use Scan with an AWS SDK or CLI
- [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateItem_section.html): Use UpdateItem with an AWS SDK or CLI
- [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateTable_section.html): Use UpdateTable with an AWS SDK or CLI
- [UpdateTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateTimeToLive_section.html): Use UpdateTimeToLive with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_scenarios.html)

The following code examples show how to use DynamoDB with AWS SDKs.

- [Accelerate reads with DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Usage_DaxDemo_section.html): Accelerate DynamoDB reads with DAX using an AWS SDK
- [Advanced Global Secondary Index scenarios](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_GSIAdvanced_section.html): Work with advanced DynamoDB Global Secondary Index scenarios using AWS Command Line Interface v2
- [Build an app to submit data to a DynamoDB table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_SubmitDataApp_section.html): Build an application to submit data to a DynamoDB table
- [Compare multiple values with a single attribute](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_CompareMultipleValues_section.html): Compare multiple values with a single attribute in DynamoDB with an AWS SDK
- [Conditionally update an item's TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateItemConditionalTTL_section.html): Conditionally update a DynamoDB item with a TTL using an AWS SDK
- [Connect to a local instance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_local_section.html): Connect to a local DynamoDB instance using an AWS SDK
- [Count expression operators](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ExpressionOperatorCounting_section.html): Count expression operators in DynamoDB with an AWS SDK
- [Create a REST API to track COVID-19 data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_ApiGatewayDataTracker_section.html): Create an API Gateway REST API to track COVID-19 data
- [Create a messenger application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_StepFunctionsMessenger_section.html): Create a messenger application with Step Functions
- [Create a serverless application to manage photos](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_PAM_section.html): Create a photo asset management application that lets users manage photos using labels
- [Create a table with global secondary index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_CreateTableWithGlobalSecondaryIndex_section.html): Create a DynamoDB table with a Global Secondary Index using the AWS SDK
- [Create a table with warm throughput enabled](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_CreateTableWarmThroughput_section.html): Create a DynamoDB table with warm throughput setting using an AWS SDK
- [Create a web application to track DynamoDB data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_DynamoDBDataTracker_section.html): Create a web application to track DynamoDB data
- [Create a websocket chat application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_ApiGatewayWebsocketChat_section.html): Create a websocket chat application with API Gateway
- [Create an item with a TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PutItemTTL_section.html): Create a DynamoDB item with a TTL using an AWS SDK
- [Create and manage MRSC global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_MRSCGlobalTables_section.html): Create and manage DynamoDB global tables with Multi-Region Strong Consistency using an AWS SDK
- [Create and manage global tables demonstrating MREC](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_GlobalTableOperations_section.html): Create and manage DynamoDB global tables demonstrating MREC using an AWS SDK
- [Delete data using PartiQL DELETE](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PartiQLDelete_section.html): Delete DynamoDB data using PartiQL DELETE statements with an AWS SDK
- [Detect PPE in images](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_RekognitionPhotoAnalyzerPPE_section.html): Detect PPE in images with Amazon Rekognition using an AWS SDK
- [Insert data using PartiQL INSERT](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PartiQLInsert_section.html): Insert DynamoDB data using PartiQL INSERT statements with an AWS SDK
- [Invoke a Lambda function from a browser](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_LambdaForBrowser_section.html): Invoke a Lambda function from a browser
- [Manage Global Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_GSILifecycle_section.html): Manage DynamoDB Global Secondary Indexes using AWS Command Line Interface v2
- [Manage resource-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ResourcePolicyLifecycle_section.html): Manage DynamoDB resource-based policies using AWS Command Line Interface v2
- [Monitor DynamoDB performance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_MonitorDynamoDB_section.html): Monitor performance of Amazon DynamoDB using an AWS SDK
- [Perform advanced query operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_AdvancedQueryTechniques_section.html): Perform advanced DynamoDB query operations using an AWS SDK
- [Perform list operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ListOperations_section.html): Perform list operations in DynamoDB with an AWS SDK
- [Perform map operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_MapOperations_section.html): Perform map operations in DynamoDB with an AWS SDK
- [Perform set operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_SetOperations_section.html): Perform set operations in DynamoDB with an AWS SDK
- [Query a table by using batches of PartiQL statements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_PartiQLBatch_section.html): Query a DynamoDB table by using batches of PartiQL statements and an AWS SDK
- [Query a table using PartiQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_PartiQLSingle_section.html): Query a DynamoDB table using PartiQL and an AWS SDK
- [Query a table using a Global Secondary Index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithGlobalSecondaryIndex_section.html): Query a DynamoDB table using a Global Secondary Index with an AWS SDK
- [Query a table using a begins_with condition](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithBeginsWithCondition_section.html): Query a DynamoDB table using a begins_with condition with an AWS SDK
- [Query a table using a date range](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithDateRange_section.html): Query a DynamoDB table using a date range in the sort key with an AWS SDK
- [Query a table with a complex filter expression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithComplexFilter_section.html): Query a DynamoDB table with a complex filter expression with an AWS SDK
- [Query a table with a dynamic filter expression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithDynamicFilter_section.html): Query a DynamoDB table with a dynamic filter expression with an AWS SDK
- [Query a table with a filter expression and limit](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithFilterAndLimit_section.html): Query a DynamoDB table with a filter expression and limit with an AWS SDK
- [Query a table with nested attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithNestedAttributes_section.html): Query a DynamoDB table with nested attributes using an AWS SDK
- [Query a table with pagination](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithPagination_section.html): Query a DynamoDB table with pagination using an AWS SDK
- [Query a table with strongly consistent reads](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenarios_QueryWithStronglyConsistentReads_section.html): Query a DynamoDB table with strongly consistent reads using an AWS SDK
- [Query data using PartiQL SELECT](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PartiQLSelect_section.html): Query DynamoDB data using PartiQL SELECT statements with an AWS SDK
- [Query for TTL items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_QueryFilteredTTL_section.html): Query a DynamoDB table for TTL items using an AWS SDK
- [Query tables using date and time patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_DateTimeQueries_section.html): Query DynamoDB tables using date and time patterns with an AWS SDK
- [Save EXIF and other image information](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_DetectLabels_section.html): Save EXIF and other image information using an AWS SDK
- [Set up Attribute-Based Access Control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ABACSetup_section.html): Set up Attribute-Based Access Control for DynamoDB using AWS Command Line Interface v2
- [Understand update expression order](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_UpdateExpressionOrder_section.html): Understand update expression order in DynamoDB with an AWS SDK
- [Update a table's warm throughput setting](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateTableWarmThroughput_section.html): Update a DynamoDB table setting with warm throughput using an AWS SDK
- [Update an item's TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_UpdateItemTTL_section.html): Update a DynamoDB item with a TTL using an AWS SDK
- [Update data using PartiQL UPDATE](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_PartiQLUpdate_section.html): Update DynamoDB data using PartiQL UPDATE statements with an AWS SDK
- [Use API Gateway to invoke a Lambda function](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_LambdaAPIGateway_section.html): Use API Gateway to invoke a Lambda function
- [Use Step Functions to invoke Lambda functions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_ServerlessWorkflows_section.html): Use Step Functions to invoke Lambda functions
- [Use a document model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_MidLevelInterface_section.html): Use a document model for DynamoDB using an AWS SDK
- [Use a high-level object persistence model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_HighLevelInterface_section.html): Use a high-level object persistence model for DynamoDB using an AWS SDK
- [Use atomic counter operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_AtomicCounterOperations_section.html): Use atomic counter operations in DynamoDB with an AWS SDK
- [Use conditional operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ConditionalOperations_section.html): Use conditional operations in DynamoDB with an AWS SDK
- [Use expression attribute names](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_ExpressionAttributeNames_section.html): Use expression attribute names in DynamoDB with an AWS SDK
- [Use scheduled events to invoke a Lambda function](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_cross_LambdaScheduledEvents_section.html): Use scheduled events to invoke a Lambda function
- [Work with Local Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_LSIExamples_section.html): Work with DynamoDB Local Secondary Indexes using AWS Command Line Interface v2
- [Work with Streams and Time-to-Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_StreamsAndTTL_section.html): Work with DynamoDB Streams and Time-to-Live using AWS Command Line Interface v2
- [Work with global tables and multi-Region replication eventual consistency (MREC)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_MultiRegionReplication_section.html): Work with DynamoDB global tables and multi-Region replication with eventual consistency (MREC) using AWS Command Line Interface v2
- [Work with resource tagging](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_TaggingExamples_section.html): Work with DynamoDB resource tagging using AWS Command Line Interface v2
- [Work with table encryption](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_dynamodb_Scenario_EncryptionExamples_section.html): Work with DynamoDB table encryption using AWS Command Line Interface v2

### [Serverless examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_serverless_examples.html)

The following code examples show how to use DynamoDB with AWS SDKs.

- [Invoke a Lambda function from a DynamoDB trigger](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_serverless_DynamoDB_Lambda_section.html): Invoke a Lambda function from a DynamoDB trigger
- [Reporting batch item failures for Lambda functions with a DynamoDB trigger](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_serverless_DynamoDB_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with a DynamoDB trigger

### [AWS community contributions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_aws_community_contributions.html)

AWS community contributions are examples that were created and are maintained by multiple teams across AWS.

- [Build and test a serverless application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/example_tributary-lite_serverless-application_section.html): Build and test a serverless application


## [Security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html)

- [AWS managed policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-security-iam.awsmanpol.html): This page provides an overview of AWS managed policies for DynamoDB, including details on the DynamoDBReplicationServiceRolePolicy and AmazonDynamoDBReadOnlyAccess policies, and recent updates to these policies.

### [Resource-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html)

Learn how resource-based permissions policies for DynamoDB let you grant usage permissions to other AWS accounts or organizations on a per-resource basis.

- [Create table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-create-table.html): Create a table that contains a resource-based policy using the AWS Management Console, DynamoDB API, AWS CLI, AWS SDK, or an CloudFormation template.
- [Attach resource-based policy](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-attach-resource-based-policy.html): Attach a resource-based policy to an existing table using the AWS Management Console, DynamoDB API, AWS CLI, AWS SDK, or an CloudFormation template.
- [Attach policy to a stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-attach-resource-policy-streams.html): Attach a resource-based policy to an existing table's stream using the AWS Management Console, DynamoDB API, AWS CLI, AWS SDK, or an CloudFormation template.
- [Remove resource-based policy](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-delete-resource-based-policy.html): Remove a resource-based policy from a table using the AWS Management Console, DynamoDB API, AWS CLI, AWS SDK, or an CloudFormation template.
- [Cross-account access](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-cross-account-access.html): Learn how to set up cross-account access for DynamoDB resources using resource-based policies.
- [Blocking public access](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-bpa-rbp.html): Learn how Block Public Access (BPA) prevents resource-based policies from granting public access to DynamoDB tables, indexes, and streams.
- [API operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-iam-actions.html): View the DynamoDB API operations that support resource-based policies for cross-account access.
- [IAM authorization](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-auth-iam-id-based-policies-DDB.html): Learn about identity-based and resource-based policies for authorization.
- [Examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-examples.html): Use this library of resource-based policy examples to build your own policies.
- [Considerations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html): Learn key considerations to implement resource-based policies in DynamoDB.
- [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-best-practices.html): Best practices for DynamoDB resource-based policies.

### [Attribute-based access control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/attribute-based-access-control.html)

Learn how to use attribute-based access control (ABAC) with DynamoDB tables and indexes to simplify permissions management and enhance security.

- [Enabling ABAC in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-enable-ddb.html): Learn how to enable and manage attribute-based access control (ABAC) for DynamoDB.
- [Using ABAC](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-implementation-ddb-tables.html): Learn how to use attribute-based access control (ABAC) with DynamoDB tables and indexes.
- [Example use cases](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-example-use-cases.html): Explore various examples of using attribute-based access control (ABAC) with DynamoDB tables and indexes.
- [Troubleshooting](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-troubleshooting.html): Learn how to troubleshoot common errors when using attribute-based access control (ABAC) with DynamoDB tables and indexes, including service-specific condition key issues and ABAC opt-out conditions.

### [Data protection](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-protection.html)

Explore the data protection features of DynamoDB, including encryption at rest and in transit, as well as the data protection capabilities of the DAX.

### [Encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html)

Discover how Amazon DynamoDB helps protect your data by default using the fully managed encryption at rest functionality.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.howitworks.html): Overview of the encryption at rest functionality in DynamoDB.
- [Usage notes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.usagenotes.html): An overview of Amazon DynamoDB data encryption at rest and general considerations when using this feature.
- [Managing encrypted tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html): Learn to manage encryption at rest in Amazon DynamoDB by specifying the encryption key on new and existing DynamoDB tables using the AWS Management Console and AWS CLI.
- [Securing DynamoDB connections](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/inter-network-traffic-privacy.html): Describes how DynamoDB secures connections from the service to other locations.

### [IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/identity-and-access-mgmt.html)

Authenticate requests and manage permissions to access your Amazon DynamoDB resources through the IAM API.

### [Identity and Access Management](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security-iam.html)

Learn how to secure your DynamoDB data and meet compliance requirements using encryption, access control, and monitoring and logging capabilities.

- [How Amazon DynamoDB works with IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security_iam_service-with-iam.html): Learn how to use IAM to manage access to DynamoDB resources.

### [Identity-based policy examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security_iam_id-based-policy-examples.html)

Learn about identity-based policies for DynamoDB resources.

### [Using identity-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/using-identity-based-policies.html)

Learn how to use identity-based policies to control access to DynamoDB actions and resources.

- [Perform any actions on a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/grant-permissions-to-any-action-on-table.html): An example of a custom IAM policy you can create to grant permissions for a user, group, or role access to perform any action on a DynamoDB table.
- [Read-only access on items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-only-permissions-on-table-items.html): Grant read-only permission to a user, group, or role on items in a DynamoDB table with this example of a custom IAM user managed policy.
- [Access to a specific table and its indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-specific-table-indexes.html): A custom IAM managed policy to grant access to a specific table and its indexes, but nothing else.
- [CRUD operations on all data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-example-data-crud.html): An example IAM policy to grant full create, read, update, and delete (CRUD) access for data operations on a DynamoDB table.
- [Separate environments in the same AWS account](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-separate-environments.html): Learn from this example how to set an IAM policy to create separate prefixed named DynamoDB tables to give more granular permissions on environments in the same AWS account.
- [Prevent purchase of reserved capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-prevent-purchase-reserved-capacity.html): A custom IAM policy to restrict permissions for a user, group, or role to purchase reserved capacity for Amazon DynamoDB tables.
- [Read access for a stream only](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-read-stream-only.html): Create a custom IAM policy to grant permissions for a user, group, or role to read only a table's stream, but not the table itself.
- [Lambda function to process stream records](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-example-lamda-process-dynamodb-streams.html): With this IAM policy, grant read permissions to an AWS Lambda function to access only DynamoDB stream records.
- [CRUD operations on a DAX cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-example-read-write-dax-access.html): See a simple example of an IAM policy to allow read and write access on a DynamoDB Accelerator (DAX) cluster.
- [Troubleshooting](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security_iam_troubleshoot.html): Troubleshoot common identity and access issues in DynamoDB.
- [Prevent purchase of reserved capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html): Create an IAM policy to prevent users from purchasing DynamoDB reserved capacity, helping control costs and managing resource allocation in your AWS account.

### [Using conditions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html)

Create fine-grained access control to individual items and attributes in Amazon DynamoDB resources such as tables and indexes.

### [Using web identity federation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WIF.html)

Use web identity federation for authentication and authorization on your application.

- [Preparing to use web identity federation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WIF.PreparingForUse.html): Follow this process for setting up and using web identity federation for authentication and authorization on your application.
- [Writing your app to use web identity federation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WIF.RunningYourApp.html): Follow these steps to write your application using web identity federation for authentication and authorization.
- [DynamoDB API permissions reference](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/api-permissions-reference.html): Refer to this table of permissions for Amazon DynamoDB APIs.
- [Compliance validation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Compliance.html): Learn what AWS services are in scope of a specific compliance program and where to go for more detailed information.
- [Resilience](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/disaster-recovery-resiliency.html): AWS architecture supports data redundancy and specific DynamoDB features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/network-isolation.html): Learn how Amazon DynamoDB isolates service traffic.

### [AWS PrivateLink for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html)

Connect to DynamoDB by using AWS PrivateLinkÂ interface Amazon VPC endpoints in your virtual private cloud (Amazon VPC).

- [AWS PrivateLink for DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-streams.html): Learn more about AWS PrivateLink for DynamoDB Streams.
- [AWS PrivateLink for DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-private-link.html): Learn how AWS PrivateLink for DynamoDB Accelerator (DAX) provides private, secure connectivity to DAX management APIs within the same AWS Region, helping you access services privately without exposing traffic to the public internet.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/configuration-vulnerability.html): Learn about configuration and vulnerability analysis in DynamoDB.

### [Security best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices-security.html)

Explore security best practices for DynamoDB, including encryption, IAM policies, VPC endpoints, and monitoring tools like CloudTrail, Config, and Security Hub to detect and prevent security issues.

- [Preventative security best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices-security-preventative.html): Consider these preventative best practices in DynamoDB.
- [Detective security best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices-security-detective.html): Consider these best practices to help detect potential security issues in DynamoDB.


## [Monitoring and logging](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/MonitoringAndLoggingInDynamoDB.html)

### [Monitoring metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Monitoring-metrics-with-Amazon-CloudWatch.html)

You can monitor DynamoDB using CloudWatch, which collects and processes raw data from DynamoDB into readable, near real-time metrics.

- [Metrics and dimensions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html): Learn about metrics and dimensions for CloudWatch.
- [Creating CloudWatch alarms in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Monitoring-metrics-creating-cloudwatch-alarms.html): You can create alarms that respond to observed metrics over time.

### [Logging operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/logging-using-cloudtrail.html)

Learn how to access the history of DynamoDB API calls by enabling CloudTrail, a service that provides a record of actions taken by users, roles, or AWS services.

- [Understanding DynamoDB log file entries](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/understanding-ddb-log-entries.html): Learn how to interpret and analyze DynamoDB log file entries for monitoring performance, troubleshooting issues, and optimizing your database operations.

### [Contributor Insights](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights.html)

Quickly identify the most frequently accessed and throttled keys in your DynamoDB table or index using CloudWatch Contributor Insights.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights_HowItWorks.html): Explore an overview of DynamoDB's integration with CloudWatch Contributor Insights, including how it works, the generated rules, the graphs, and the billing model.
- [Getting started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights_tutorial.html): This tutorial covers how to use Amazon CloudWatch Contributor Insights with DynamoDB, including enabling it through the console or AWS CLI with different modes, creating CloudWatch alarms, and understanding the usage metrics and graphs provided by Contributor Insights.
- [Using IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Contributor_Insights_IAM.html): Learn about using IAM policies to configure CloudWatch Contributor Insights for DynamoDB operations, including enabling/disabling Contributor Insights, viewing reports, and managing permissions based on resources.


## [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)

- [NoSQL design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html): Review the key differences and design principles for NoSQL database systems like DynamoDB

### [The DynamoDB Well-Architected Lens](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-wal.html)

Learn about the DynamoDB Well-Architected Lens, a collection of design principles and guidance for designing well-architected DynamoDB workloads, covering the six pillars of the AWS Well-Architected Framework: performance efficiency, cost optimization, operational excellence, reliability, security, and sustainability.

### [Cost optimization](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-cost-optimization.html)

Identify strategies for optimizing costs on your existing Amazon DynamoDB tables.

- [Evaluate your costs at the table level](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_TableLevelCostAnalysis.html): Optimize DynamoDB costs by using Cost Explorer to analyze table-level costs.
- [Evaluate your table capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_TableCapacityMode.html): Explore an overview of how to select the appropriate capacity mode for your DynamoDB tables, evaluating factors such as workload predictability, cost optimization, and auto-scaling capabilities to determine the best mode for your use case.
- [Evaluate your table's auto scaling settings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_AutoScalingSettings.html): Evaluate your DynamoDB table's auto scaling settings to ensure proper provisioning and cost optimization.
- [Evaluate your table class selection](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_TableClass.html): Optimize costs for your DynamoDB tables by selecting the appropriate table class - Standard or Standard-IA.
- [Identify your unused resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_UnusedResources.html): Identify and optimize costs for unused DynamoDB resources, including tables, global secondary indexes, and backups, using CloudWatch metrics and techniques like on-demand capacity mode and table class selection.
- [Evaluate your table usage patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_TableUsagePatterns.html): Optimize your DynamoDB costs by evaluating table usage patterns, such as reducing strongly-consistent reads, transactions, scans, and using shorter attribute names.
- [Evaluate your streams usage](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_StreamsUsage.html): Optimize costs for Amazon DynamoDB Streams and Kinesis Data Streams by leveraging AWS Lambda, monitoring usage, choosing the right capacity mode, and tuning consumer applications.
- [Evaluate your provisioned capacity for right-sized provisioning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_RightSizedProvisioning.html): Evaluate your DynamoDB table provisioned capacity and identify over-provisioned or under-provisioned tables.

### [Partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

Learn about best practices for designing and using partition keys effectively in DynamoDB.

- [Distributing workloads](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html): Learn about best practices for designing partition keys in NoSQL databases like DynamoDB to distribute workloads effectively and avoid hot partitions that can lead to throttling and inefficient use of provisioned I/O capacity.
- [Write sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html): Learn about best practices for using write sharding in DynamoDB databases to distribute workloads evenly.
- [Uploading data efficiently](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-data-upload.html): Explore how efficient data uploads to DynamoDB tables require distributing write activity across partition key values to fully utilize provisioned throughput capacity.
- [Sort key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-sort-keys.html): Design sort keys in DynamoDB to organize data for efficient querying.

### [Secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes.html)

Learn about the best practices for using secondary indexes in DynamoDB, including guidelines on efficient use, careful projection, and avoiding fetches.

- [General guidelines](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general.html): Learn best practices for using secondary indexes in DynamoDB to optimize query performance, manage storage costs, and reduce costs.
- [Sparse indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general-sparse-indexes.html): Learn how to use sparse indexes in DynamoDB to improve query performance and reduce storage costs.
- [Aggregation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-aggregation.html): Learn about best practices for maintaining near real-time aggregations and key metrics on rapidly changing data in DynamoDB, using DynamoDB Streams, AWS Lambda, and sparse Global Secondary Indexes (GSIs) to pre-compute and efficiently query aggregated results such as the most popular songs in a music library.
- [GSI overloading](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-gsi-overloading.html): Learn about the concept of overloading global secondary indexes (GSIs) in DynamoDB.
- [GSI sharding](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-sharding.html): Learn about using Global Secondary Indexes (GSIs) with write sharding to enable selective queries on DynamoDB tables.
- [Creating a replica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-gsi-replica.html): Learn about best practices for creating an eventually consistent replica of a DynamoDB table using Global Secondary Indexes (GSIs), which can allow setting different read capacities for different applications and eliminating reads from the main table.
- [Large items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html): Read about best practices for storing large items and attribute values in DynamoDB.
- [Time series data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html): Learn about best practices for handling time-series data in DynamoDB.
- [Many-to-many relationships](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-adjacency-graphs.html): Learn best practices for modeling many-to-many relationships in DynamoDB using the adjacency list and materialized graph patterns, highlighting their advantages and use cases, and recommending Amazon Neptune for highly connected datasets requiring real-time graph queries.
- [Querying and scanning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html): Learn about best practices for using Query and Scan operations in DynamoDB, including performance considerations, avoiding spikes in read activity, and leveraging parallel scans to improve efficiency while managing provisioned throughput.
- [Table design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-table-design.html): Explore best practices for designing DynamoDB tables, including recommendations to minimize the number of tables, considerations for account and service limits, and guidance on working with AWS solution architects for multi-tenant designs.

### [Using global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html)

Learn about best practices for designing and deploying Amazon DynamoDB global tables, including guidance on write modes, request routing, Region evacuation, and capacity planning to achieve low-latency reads and writes with high availability and resiliency.

- [Write modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.prescriptive-guidance.writemodes.html): Write modes with global tables
- [Routing strategies in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.prescriptive-guidance.request-routing.html): Request routing with global tables
- [Evacuation processes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.prescriptive-guidance.evacuation.html): Evacuating a Region with global tables
- [Throughput capacity planning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.prescriptive-guidance.throughput.html): Throughput capacity planning for global tables
- [Preparation checklist](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.prescriptive-guidance.checklist-and-faq.html): Preparation checklist for deploying global tables and frequently asked questions.
- [Control plane](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-control-plane.html): Explore best practices for managing the DynamoDB control plane, including avoiding excessive control plane calls, separating control and data plane operations, handling throttling, and caching data to optimize performance.

### [Bulk data operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_BulkDataOperations.html)

Learn about best practices for using advanced design patterns when you need to perform bulk operations, implement robust version control mechanisms, or manage time-sensitive data.

- [Conditional batch update](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_ConditionalBatchUpdate.html): Learn about best practices for using conditional batch updates in DynamoDB.
- [Efficient bulk operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_EfficientBulkOperations.html): Learn about best practices for efficiently using bulk operations in DynamoDB.

### [Handling concurrent updates](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_ImplementingVersionControl.html)

Implement concurrency control in DynamoDB using optimistic locking, pessimistic locking with transactions, and distributed lock clients to manage concurrent writes and ensure data integrity.

- [Optimistic locking](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_OptimisticLocking.html): Optimistic locking is a strategy that detects conflicts at write time rather than preventing them.
- [Pessimistic locking with transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_PessimisticLocking.html): DynamoDB transactions provide an all-or-nothing approach to grouped operations.
- [Distributed locking](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_DistributedLocking.html): For applications that require traditional lock-acquire-release semantics, the DynamoDB Lock Client is an open-source library that implements distributed locking using a DynamoDB table as the lock store.
- [Billing and Usage Reports](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-understanding-billing.html): Explore the various usage types and billing codes for charges related to DynamoDB, including provisioned and on-demand capacity, streams, backups, data transfer, and the DynamoDB Accelerator (DAX).

### [Migrating a DynamoDB table from one account to another](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-migrating-table-between-accounts.html)

Explore guidance on migrating a DynamoDB table from one AWS account to another, using either the AWS Backup service for cross-account backup and restore, or DynamoDB's export to Amazon S3 and import from Amazon S3 features.

- [Migrate a table using AWS Backup for cross-account backup and restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-migrating-table-between-accounts-backup.html): Learn how to migrate a DynamoDB table between AWS accounts using AWS Backup for cross-account backup and restore.
- [Migrate a table using export to S3 and import from S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-migrating-table-between-accounts-s3.html): Migrate a DynamoDB table between AWS accounts using Amazon S3 export and import.

### [DAX prescriptive guidance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-prescriptive-guidance.html)

Explore comprehensive insights and best practices for integrating the DynamoDB Accelerator (DAX) with DynamoDB applications, including when to use DAX, configuring clusters, sizing, deploying, and monitoring strategies.

- [Evaluating the suitability of DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/evaluate-dax-suitability.html): Learn about the advantages of using DAX and various aspects to consider for determining its suitability for your use cases.
- [Configuring your DAX client](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-config-dax-client.html): Learn about the key considerations to configure your DAX client.
- [Configuring your DAX cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-config-considerations.html): Learn about the key considerations to configure your DAX cluster, including cost, cache types and behaviors, TTL settings, and Regional availability of clusters.
- [Sizing your DAX cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-cluster-sizing.html): Learn about the sizing strategies to balance performance, cost, and capacity of your DAX clusters.
- [Deploying a cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-deploy-cluster.html): Learn about the best practices to create and deploy a DAX cluster, replace a node in the cluster, and access control policies for the cluster.
- [Cluster operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-cluster-operations.html): Manage your DAX clusters using techniques, such as scaling, backing up, restoring, and decommissioning old clusters.
- [Monitoring DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/pres-guide-monitor-dax.html): Learn about the monitoring strategies for DAX clusters using using Amazon CloudWatch metrics, logs, and alarms to identify and resolve issues proactively.


## [Using DynamoDB with other AWS services](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OtherServices.html)

- [Integrating with Amazon Cognito](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Cognito.Credentials.html): Learn how to configure Amazon Cognito credentials to integrate with DynamoDB and other AWS services for your web and mobile applications, using IAM roles to generate temporary credentials for authenticated and unauthenticated users.

### [Integrating with Amazon Redshift](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB.html)

Copy data from Amazon Redshift to DynamoDB and run complex data analysis queries in Amazon Redshift, using real-time operations in DynamoDB and analytical operations in Amazon Redshift.

- [Cross-account integration considerations with CMK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/cross-account-integration-considerations.html): When you set up Zero-ETL integration between Amazon DynamoDB and Amazon Redshift across different AWS accounts, you need to ensure proper IAM permissions are configured in both accounts.

### [Zero-ETL integration with Amazon Redshift](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.html)

Copy data from Amazon Redshift to DynamoDB and run complex data analysis queries in Amazon Redshift, using real-time operations in DynamoDB and analytical operations in Amazon Redshift.

- [Creating DynamoDB zero-ETL integrations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl-getting-started.html): Before creating a zero-ETL integration, you must first set up your source DynamoDB table and then the target Amazon Redshift data warehouse.
- [Viewing DynamoDB zero-ETL integrations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl-viewing.html): You can view the details of a zero-ETL integration to see its configuration information and current status.
- [Deleting DynamoDB zero-ETL integrations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl-deleting.html): When you delete a zero-ETL integration, your data isn't deleted from DynamoDB or Amazon Redshift, but DynamoDB stops sending data from your source table to the Amazon Redshift target.
- [Loading data from DynamoDB into Amazon Redshift with COPY](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-copy-data.html): Copy data from Amazon Redshift to DynamoDB and run complex data analysis queries in Amazon Redshift, using real-time operations in DynamoDB and analytical operations in Amazon Redshift.

### [Integrating with Amazon EMR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.html)

Use Amazon EMR to analyze, process and copy data in Amazon DynamoDB.

### [Tutorial: Working with Amazon DynamoDB and Apache Hive](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.html)

Follow this tutorial for using Amazon EMR with Amazon DynamoDB.

- [Step 1: Create an Amazon EC2 key pair](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.EC2KeyPair.html): Learn how to create an Amazon EC2 key pair for use with Amazon EMR and Amazon DynamoDB.
- [Step 2: Launch an Amazon EMR cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.LaunchEMRCluster.html): Launch an Amazon EMR cluster so that you can process data in Amazon DynamoDB.
- [Step 3: Connect to the Leader node](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.ConnectToLeaderNode.html): Learn how to connect to the leader node in an Amazon EMR cluster so that you can begin working with data in Amazon DynamoDB
- [Step 4: Load data into HDFS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.LoadDataIntoHDFS.html): Use the Hive command line to prepare data for loading into Amazon DynamoDB.
- [Step 5: Copy data to DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.CopyDataToDDB.html): Copy data from HDFS on Amazon EMR to a Amazon DynamoDB table.
- [Step 6: Query the data in the DynamoDB table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.QueryDataInDynamoDB.html): Use HiveQL, a SQL-like language, to query data in Amazon DynamoDB.
- [Step 7: (Optional) clean up](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.CleanUp.html): Shut down resources you used during the Amazon EMR and Amazon DynamoDB tutorial.
- [Creating an external table in Hive](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.ExternalTableForDDB.html): Learn how to create an external Hive table that points to data in Amazon DynamoDB.
- [Processing HiveQL statements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.ProcessingHiveQL.html): Use HiveQL to query data in Amazon EMR and Amazon DynamoDB.
- [Querying data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Querying.html): Try different HiveQL (SQL-like) queries in Amazon EMR for Amazon DynamoDB.

### [Copying data to and from Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.html)

Use Amazon EMR to copy data to and from Amazon DynamoDB.

- [Copying data between DynamoDB and a native Hive table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.NativeHive.html): Use Amazon EMR to copy data between a native Hive table and Amazon DynamoDB.
- [Copying data between DynamoDB and Amazon S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.S3.html): Use Amazon EMR to copy data between Amazon S3 and Amazon DynamoDB.
- [Copying data between DynamoDB and HDFS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.HDFS.html): Use Amazon EMR to copy data between Hadoop Distributed File System (HDFS) and Amazon DynamoDB.
- [Using data compression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.Compression.html): Use data compression when using Amazon EMR to copy data to and from Amazon DynamoDB.
- [Reading non-printable UTF-8 character data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.NonPrintableData.html): Handle non-printable UTF-8 character data when using Amazon EMR to copy data to and from Amazon DynamoDB.

### [Performance tuning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.PerformanceTuning.html)

Optimize Amazon EMR for best performance with Amazon DynamoDB.

- [DynamoDB provisioned throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.PerformanceTuning.Throughput.html): Maximize data throughput between Amazon EMR and Amazon DynamoDB.
- [Adjusting the mappers](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.PerformanceTuning.Mappers.html): Adjust the number of mappers when using Amazon EMR with Amazon DynamoDB
- [Additional topics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.PerformanceTuning.Misc.html): Learn about additional performance tuning topics for Amazon EMR and Amazon DynamoDB.

### [Integrating with S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3forDynamoDB.html)

In this section, discover what you need to know about integrating import from export to Amazon S3 with DynamoDB.

### [Import from Amazon S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.HowItWorks.html)

How to import data directly from Amazon S3 into DynamoDB, and do more with the data you already have.

- [Importing a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.Requesting.html): Explore the process and IAM permissions necessary to import from S3 into DynamoDB.
- [Import formats](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.Format.html): S3 input formats for DynamoDB
- [Quotas and Validation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.Validation.html): Learn about DynamoDB import format quotas and validation.
- [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.BestPractices.html): Learn the best practices for importing from Amazon S3 into DynamoDB.

### [Export to Amazon S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html)

DynamoDB offers a fully managed solution to export your data to Amazon S3 at scale.

- [Requesting a table export](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport_Requesting.html): Explore the process and IAM permissions to request a DynamoDB table export to an S3 bucket, enabling analytics and complex queries using other AWS services.
- [Export format](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.Output.html): Review the output format and file manifest details used by the DynamoDB export to Amazon S3 process.

### [Integrating with Amazon SageMaker Lakehouse](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/amazon-sagemaker-lakehouse-for-DynamoDB.html)

Explore how to integrate with Amazon SageMaker Lakehouse in DynamoDB zero-ETL.

### [Zero-ETL integration with Amazon SageMaker Lakehouse](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl.html)

Explore the steps for integrating with DynamoDB zero-ETL with Amazon SageMaker Lakehouse.

- [Creating DynamoDB zero-ETL integrations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started.html): Learn about creating zero-ETL integrations in DynamoDB.

### [Integrating with Amazon OpenSearch Service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OpenSearchIngestionForDynamoDB.html)

Learn how DynamoDB integrates with Amazon OpenSearch Service with the DynamoDB plugin for OpenSearch Ingestion.

- [Handling breaking changes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/opensearch-for-dynamodb-change-index.html): Learn how to handle breaking changes to your OpenSearch index when using DynamoDB.
- [Zero-ETL integration with OpenSearch Service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-integration-opensearch.html): Learn about the best practices to optimize your DynamoDB and OpenSearch Service integration, improve performance, reduce costs, handle large datasets, and more.
- [Integrating with Amazon EventBridge](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/eventbridge-for-dynamodb.html): Learn how you can enable seamless data flow from DynamoDB to an EventBridge bus.
- [Integrating with Amazon MSK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/msk-for-dynamodb.html): Learn how Amazon Managed Streaming for Apache Kafka integrates with Amazon DynamoDB by reading data from Apache Kafka topics and storing it in DynamoDB.
- [Integration best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-integration.html): Learn about best practices for integrating other AWS services with DynamoDB, including creating snapshots, capturing data changes, and using DynamoDB Streams or Amazon Kinesis Data Streams for near real-time change data capture.


## [Using generative AI with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-ai-integration.html)

- [Leveraging DynamoDB Zero-ETL integration with OpenSearch Service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-and-amazon-bedrock.html): You can use Amazon Bedrock with DynamoDB to provide serverless access to foundational models (FMs), such as Amazon Titan and other third-party models.


## [Quotas and constraints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotasRevised.html)

- [Requesting a quota increase](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RequestingQuotaIncrease.html): You can request a quota increase for each Region using the Service Quotas console, AWS CLI or a support case.
- [Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html): Examine the service, account, and table level quotas in place with DynamoDB, and learn which are default values and which can be tuned for your workloads.
- [Constraints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Constraints.html): Understand the constraints when working with DynamoDB.


## [Troubleshooting](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Troubleshooting.html)

- [Internal server errors](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingInternalServerErrors.html): Explore a comprehensive guide on troubleshooting internal server errors (ISEs) in DynamoDB.
- [Latency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingLatency.html): Learn different strategies to troubleshoot high latency on a Amazon DynamoDB table.

### [Throttling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html)

Learn how to understand, diagnose, and resolve throttling issues in Amazon DynamoDB tables.

- [Diagnosing throttling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-diagnosing-workflow.html): Systematic approach to diagnosing and resolving DynamoDB throttling issues using exception analysis and CloudWatch metrics.

### [Resolution guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/troubleshooting-throttling-diagnostics.html)

Resolution guidance for specific throttling scenarios in Amazon DynamoDB.

- [1- Key range throughput exceeded (hot partitions)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-key-range-limit-exceeded-mitigation.html): Resolution guidance for throttling when individual partitions exceed their throughput limits, affecting both provisioned and on-demand capacity modes.
- [2- Provisioned throughput exceeded](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-provisioned-capacity-exceeded-mitigation.html): Resolution guidance for throttling when consumption rates exceed provisioned capacity limits in provisioned mode.
- [3- Account limits exceeded](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-account-limit-exceeded-mitigation.html): Resolution guidance for throttling when consumption rates exceed account-level throughput quotas in your AWS Region.
- [4- On-demand maximum throughput exceeded](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-ondemand-capacity-exceeded-mitigation.html): Resolution guidance for throttling when consumption rates exceed configured maximum throughput limits in on-demand mode.
- [GSI write throttling and back-pressure](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/gsi-throttling.html): GSI back-pressure throttling represents one of the most complex throttling scenarios in DynamoDB because it creates an indirect relationship between write operations and throttlingâyour application writes to a base table but experiences throttling due to capacity constraints on one or several indexes.
- [CloudWatch throttling metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling-cloudwatch.html): Describes the CloudWatch metrics you can use to monitor and investigate throttling issues.


## [Appendix](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.html)

- [Troubleshooting SSL/TLS connection establishment issues with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ats-certs.html): Learn more about troubleshooting SSL/TLS connection establishment issues.
- [Example tables and data for use in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleTables.html): This section presents sample tables and data for the DynamoDB Developer Guide, including the ProductCatalog, Forum, Thread, and Reply tables with their primary keys.

### [Creating example tables and uploading data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleDataCode.html)

Learn how to create example tables and upload data programmatically with DynamoDB.

- [Creating example tables and uploading data - Java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleDataCodeJava.html): Learn how to create example tables and upload data programmatically using the AWS SDK for Java with Amazon DynamoDB.
- [Creating example tables and uploading data - .NET](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleDataCodeDotNET.html): Learn more about creating example tables and upload data programmatically using the AWS SDK for .NET API with Amazon DynamoDB.

### [Example application using AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.html)

In this example application, the Tic-Tac-Toe game illustrates how to use the AWS SDK for Python (Boto3) to write a high performance and scalable application for Amazon DynamoDB.

- [Step 1: Deploy and test locally](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.Phase1.html): Set up the Tic-Tac-Toe game to run with DynamoDB on your local computer.
- [Step 2: Examine the data model and implementation details](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.Phase2.html): Learn about the Tic-Tac-Toe data model and implementation using Amazon DynamoDB.
- [Step 3: Deploy in production](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.Phase3.html): Run the Tic-Tac-Toe application in a production environment with Amazon DynamoDB.
- [Step 4: Clean up resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.AppClosure.html): Remove unused resources after you are done running the Tic-Tac-Toe application with Amazon DynamoDB.
- [Reserved words in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html): Learn about using reserved words in Amazon DynamoDB.

### [AWS SDK for Java 1.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.JavaSDKv1.html)

Learn more about example code for using DynamoDB and DAX with AWS SDK for Java 1.x.

### [DAX and Java SDK v1](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.java-sdk-v1.html)

Explore a detailed guide on using the DynamoDB Accelerator with the AWS Java 1.x SDK, including a sample application to test DAX functionality.

- [TryDax.java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-java.TryDax.html): Test DAX functionality using the TryDax.java file in the Java sample application for DAX.
- [TryDaxHelper.java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-java.TryDaxHelper.html): Test DAX functionality using the TryDaxHelper.java file in the Java sample application for DAX.
- [TryDaxTests.java](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-java.TryDaxTests.html): Test DAX functionality using the TryDaxTests.java file in the Java sample application for DAX.
- [Modifying an existing SDK for Java 1.x application to use DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.modify-your-app.java-sdk-v1.html): Learn how to modify an existing Java 1.x application to access a DynamoDB Accelerator cluster, including using the DynamoDB document API and the asynchronous DAX client.
- [Querying global secondary indexes with SDK for Java 1.x](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.QueryGSI.java-sdk-v1.html): Explore using DAX to query global secondary indexes (GSI) in DynamoDB using the Java 1.x SDK.

### [AWS SDK for Go 1.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.GoSDKv1.html)

Learn more about example code for using DynamoDB and DAX with AWS Go 1.x.

- [Go and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-go.html): Test DAX functionality and performance by running the SDK for Go sample application on your Porting Assistant for .NET instance.

### [AWS SDK for Node.js 2.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.SDKNodejsv2.html)

Learn more about example code for using DynamoDB and DAX with AWS SDK for Node.js 2.x.

### [Node.js and DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.html)

Test DAX functionality and performance by running the Node.js sample application on your Porting Assistant for .NET instance.

- [01-create-table.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.01-create-table.html): Test DAX functionality using the 01-create-table.js program in the Node.js sample application.
- [02-write-data.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.02-write-data.html): Test DAX functionality using the 02-write-data.js program in the Node.js sample application.
- [03-getitem-test.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.03-getitem-test.html): Test DAX functionality using the 03-getitem-test.js program in the Node.js sample application.
- [04-query-test.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.04-query-test.html): Test DAX functionality using the 04-query-test.js program in the Node.js sample application.
- [05-scan-test.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.05-scan-test.html): Test DAX functionality using the 05-scan-test.js program in the Node.js sample application.
- [06-delete-table.js](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-nodejs.06-delete-table.html): Test DAX functionality using the 06-delete-table.js program in the Node.js sample application.


## [Legacy features](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyFeatures.html)

### [Global tables version 2017.11.29 (Legacy)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V1.html)

Learn about Global Tables Version 2017.11.29 (Legacy), an older version of DynamoDB global tables that provides multi-Region, multi-active database replication.

- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html): Overview of the global tables functionality in DynamoDB.
- [Best Practices and Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html): Requirements and best practices for adding replicas and managing capacity in DynamoDB global tables.
- [Creating a global table (Version 2017.11.29)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.tutorial.html): Create a global table using Version 2017.11.29 (Legacy) in DynamoDB with the console, AWS CLI, or API.
- [Monitoring global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_monitoring.html): Monitor ongoing global table activity in Amazon DynamoDB.
- [Using IAM with global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/gt_IAM.html): Use IAM policies to configure global table operations in DynamoDB.

### [Previous low-level DynamoDB API version (2011-12-05)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.APIv20111205.html)

Learn about document operations from the previous version of the Amazon DynamoDB API for backward compatibility with existing applications.

- [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_BatchGetItem_v20111205.html): Deprecated
- [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_BatchWriteItem_v20111205.html): Deprecated
- [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_CreateTable_v20111205.html): Deprecated
- [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_DeleteItem_v20111205.html): Deprecated
- [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_DeleteTable_v20111205.html): Deprecated
- [DescribeTables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_DescribeTables_v20111205.html): Deprecated
- [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_GetItem_v20111205.html): Deprecated
- [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_ListTables_v20111205.html): Deprecated
- [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_PutItem_v20111205.html): Deprecated
- [Query](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_Query_v20111205.html): Deprecated
- [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_Scan_v20111205.html): Deprecated
- [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_UpdateItem_v20111205.html): Deprecated
- [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/API_UpdateTable_v20111205.html): Deprecated

### [Legacy DynamoDB conditional parameters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html)

Learn how to use legacy conditional parameters for backward compatibility in Amazon DynamoDB requests.

- [AttributesToGet](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html): Learn the details of the legacy AttributesToGet parameter in Amazon DynamoDB.
- [AttributeUpdates](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributeUpdates.html): Learn the details of the legacy AttributeUpdates parameter in Amazon DynamoDB.
- [ConditionalOperator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html): Learn the details of the legacy ConditionalOperator parameter in Amazon DynamoDB.
- [Expected](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html): Learn the details of the legacy Expected parameter in Amazon DynamoDB.
- [KeyConditions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html): Learn the details of the legacy KeyConditions parameter in Amazon DynamoDB.
- [QueryFilter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html): Learn the details of the legacy QueryFilter parameter in Amazon DynamoDB.
- [ScanFilter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html): Learn the details of the legacy ScanFilter parameter in Amazon DynamoDB.
- [Writing conditions with legacy parameters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Conditions.html): Learn about legacy conditional parameters in Amazon DynamoDB.
