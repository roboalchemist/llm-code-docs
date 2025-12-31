# Amazon DynamoDB Developer Guide
> Amazon DynamoDB is a fast, fully managed NoSQL database as a service that makes it simple and cost-effective to store and retrieve any amount of data, and serve any level of request traffic.

## What is Amazon DynamoDB?
- [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html): Use DynamoDB, a fully managed NoSQL database service to store and retrieve any amount of data, and serve any level of request traffic.

## Getting started with DynamoDB
- [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html): Use these hands-on tutorials to get started with Amazon DynamoDB. 
- [First-time user resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dynamodb-resources-first-time-users.html): A curated guide to essential DynamoDB learning resources, including documentation, tools, training, and best practices to help first-time users successfully get started with Amazon DynamoDB.
- [Accessing DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AccessingDynamoDB.html): You can access DynamoDB using the console, the AWS CLI, or the API.
- [Setting up DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html): Set up the DynamoDB web service or its local downloadable version for developing and testing applications locally without accessing the cloud.
- [Step 1: Create a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html): Create a DynamoDB table with partition and sort keys using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 2: Write data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-2.html): Populate data in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more. 
- [Step 3: Read data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-3.html): Read an item from a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 4: Update data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-4.html): Update an item in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 5: Query data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-5.html): Query the data in a DynamoDB table using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Step 6: (Optional) clean up](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-6.html): Delete a DynamoDB table to clean up resources using the AWS Management Console, AWS CLI, or AWS SDKs for .NET, Java, Python, and more.
- [Next steps](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-NextSteps.html): Learn advanced DynamoDB concepts and best practices to build scalable, high-performance applications on AWS's fully managed NoSQL database service.
- [Console-to-Code](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/console-to-code.html): Transform manual DynamoDB table creation into reproducible automation code using Amazon Q Developer's Console-to-Code feature.

## How it works
- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html): Learn the basics, core components, and features of DynamoDB, a fully managed NoSQL database service for any scale application.
- [Cheat sheet](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CheatSheet.html): Explore a quick reference for working with DynamoDB and its various AWS SDKs, covering initial setup, SDK/CLI choices, basic actions like creating tables and querying data, naming rules, and key service basics.
- [Core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html): Learn about the building blocks of DynamoDB your app will need. 
- [DynamoDB API](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html): Learn how to work with the DynamoDB API.
- [Supported data types and naming rules](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html): Learn about the supported data types and naming rules for entities when using Amazon DynamoDB.
- [DynamoDB table classes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.TableClasses.html): Understand the basics of DynamoDB's table classes.
- [Partitions and data distribution in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html): Understand the basic concepts of partitions in DynamoDB.
- [Learn how to go from SQL to NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html): Learn how to apply your existing SQL knowledge for performing similar tasks in Amazon DynamoDB.
- [Amazon DynamoDB learning resources and tools](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AdditionalResources.html): You can use the additional resources provided to better understand and work with DynamoDB. 

## Reads and writes
- [Reads and writes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-reads-writes.html): Process reads and writes on your tables using DynamoDB read and write operations.
- [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html): Explore the differences between eventually consistent reads and strongly consistent reads for tables and indexes in DynamoDB.
- [Read and write operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html): Learn how DynamoDB read and write operations consume capacity units. 

## DynamoDB throughput capacity
- [DynamoDB throughput capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html): Learn about DynamoDB's capacity modes - on-demand and provisioned - and how to choose the right mode based on your application's throughput requirements, scalability needs, and cost optimization goals.
- [DynamoDB on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html): Use DynamoDB on-demand capacity mode, a serverless, pay-per-request billing option, which automatically scales to your workload’s traffic volume without capacity planning.
- [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html): Use DynamoDB provisioned capacity mode to specify the desired read and write throughput capacities when you create a table and enable capacity planning.
- [Warm throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/warm-throughput.html): Warm throughput refers to the number of read and write operations your DynamoDB table can instantaneously support. 
- [Burst and adaptive capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/burst-adaptive-capacity.html): Use burst capacity to temporarily exceed your provisioned throughput for brief periods of time. 
- [Switching capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-switching-capacity-modes.html): Learn the best practices for switching between on-demand and provisioned capacity modes for your existing Amazon DynamoDB tables.

## Programming with DynamoDB
- [Programming with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.html): Learn how to develop applications for DynamoDB using the AWS SDKs for Java, PHP, and .NET. 
- [Overview of AWS SDK support for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html): Learn the basics of using AWS SDKs with Amazon DynamoDB.
- [Programming with Python](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html): Learn different concepts related to how to program DynamoDB with Python.
- [Programming with JavaScript](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-javascript.html): Learn different concepts related to how to program DynamoDB with JavaScript.
- [Programming with the AWS SDK for Java 2.x](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProgrammingWithJava.html): Learn different concepts about how to program DynamoDB with the AWS SDK for Java 2.x.
- [Error handling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html): Discover the best practices for handling client and server errors and exceptions returned by Amazon DynamoDB operations.
- [Working with AWS SDKs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.

## Working with DynamoDB
- [Working with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithDynamo.html): Learn how to work with DynamoDB tables, items, queries, scans, and indexes. 
- [Working with tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html): Learn how to work with DynamoDB tables using the AWS CLI and SDKs to optimize your database operations, build scalable applications, and improve their performance.
- [Working with global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html): DynamoDB global tables provide multi-Region, multi-active database replication for fast, localized performance and high availability in global applications.
- [Working with items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html): The basic building blocks of Amazon DynamoDB start with tables, items, and attributes. 
- [Working with indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html): Improve data access in DynamoDB using secondary indexes. 
- [Working with transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html): Use DynamoDB transactions to manage complex workflows by grouping multiple actions into a single atomic and ACID operation.
- [Working with streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/streamsmain.html): Learn about capturing changes to items stored in a DynamoDB table at the point in time when changes occur.

## In-memory acceleration with DAX
- [In-memory acceleration with DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html): Accelerate your DynamoDB reads with DAX, a managed in-memory cache that provides microsecond latency and reduced operational complexity.
- [How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html): Explore how the DynamoDB in-memory cache service DAX can accelerate read access for your critical workloads, with information about Amazon VPC, node makeup, security groups, and networking.
- [DAX cluster components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html): Explore the key components and operational aspects of the DAX, a fully managed, highly available, in-memory data store that provides fast read performance for applications using DynamoDB. 
- [Creating a DAX cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.html): Set up and use DAX (the DynamoDB in-memory caching layer) in your default Amazon VPC environment by creating a basic cluster using the console or AWS CLI.
- [Consistency models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html): Understand the consistency models of DAX and DynamoDB to ensure your application behaves as expected when using the DAX caching service.
- [Developing with the DAX client](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.html): Learn to develop with the Amazon DynamoDB Accelerator (DAX) client to securely connect your applications to DAX and speed up your DynamoDB read throughput.
- [Managing DAX clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html): Discover the common management tasks necessary to operate and maintain a high-performance and scalable caching tier for Amazon DynamoDB with DynamoDB Accelerator (DAX)
- [Monitoring DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Monitoring.html): Monitoring DynamoDB Accelerator (DAX) is critical for maintaining reliability and performance. 
- [DAX T3/T2 burstable instances](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Burstable.html): DAX allows you to choose between fixed performance instances (such as R4 and R5) and burstable performance instances (such as T2 and T3). 
- [DAX access control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.html): Amazon DynamoDB and DAX are separate AWS services and have different security models implementation of AWS Identity and Access Management (IAM) security roles and policies. 
- [DAX encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html): DAX encryption at rest secures your data with AES-256 and integrates with AWS KMS, providing an additional layer of protection for your cloud applications.
- [DAX encryption in transit](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html): Learn how DynamoDB Accelerator (DAX) can enhance the security of your application with encryption in transit.
- [Using service-linked roles for DAX](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/using-service-linked-roles.html): Fine-grained security is crucial to a well-architected caching system. 
- [Accessing DAX across AWS accounts](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cross-account-access.html): Learn how to access a DAX cluster in a different AWS account using IAM roles and VPC peering to enable cross-account application access.
- [DAX cluster sizing guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.sizing-guide.html): Advice for choosing an appropriate DAX cluster size and node type.

## Data modeling
- [Data modeling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling.html): Explore best practices for designing flexible and optimized DynamoDB schemas, including single vs. multiple table design, key schema patterns, and secondary indexes. 
- [Working with Item Collections](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItemCollections.html): Learn how to work with item collections in your DynamoDB tables and secondary indexes.
- [Data modeling foundations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-foundations.html): Explore the foundations of data modeling in DynamoDB, examining the advantages and disadvantages of single table and multiple table design patterns to optimize data access, performance, and cost.
- [Data modeling building blocks](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-blocks.html): Explore the key building blocks for effective data modeling in DynamoDB, including composite sort keys, multi-tenancy, sparse indexes, time to live, vertical partitioning, and write sharding strategies.
- [Data modeling schema design packages](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-schemas.html): Learn about the different schema packages, their business use case, design, and access patterns that you can use in DynamoDB.
- [Relational modeling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-relational-modeling.html): Learn about best practices for modeling relational data in DynamoDB, including how DynamoDB eliminates the need for JOIN operations and reduces overhead compared to traditional relational database management systems.

## Migrating to DynamoDB
- [Migrating to DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/migration-guide.html): Learn about migrating from a relational database to DynamoDB, including reasons to migrate, considerations, and strategies for offline, hybrid, and online migrations.

## NoSQL Workbench
- [NoSQL Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html): Design, create, query, and manage using NoSQL Workbench for DynamoDB. 
- [Download](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html): Download the official version of NoSQL Workbench for Amazon DynamoDB. 
- [Install](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.install.html): Install the official version of NoSQL Workbench for Amazon DynamoDB. 
- [Data modeler](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.html): Use the data modeler functionality in NoSQL Workbench to build data models in NoSQL Workbench for Amazon DynamoDB.
- [Data visualizer](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Visualizer.html): Use the data visualizer functionality in NoSQL Workbench to map queries and visualize different access patterns of an application in DynamoDB.
- [Operation builder](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.html): Use the operation builder in NoSQL Workbench to view, explore, and query live datasets. 
- [Sample data models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.SampleModels.html): Sample Data Models for NoSQL Workbench
- [Release history](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkbenchDocumentHistory.html): Find the revision dates, related releases, and important changes to NoSQL Workbench for Amazon DynamoDB.

## Backup and restore
- [Backup and restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup-and-Restore.html): DynamoDB offers on-demand and point-in-time recovery backups to protect data, with no impact on performance, and provides options for creating, managing, and restoring backups using AWS Backup, the DynamoDB console, AWS CLI, or API.
- [Point-in-time backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html): Protect your DynamoDB tables from accidental write or delete operations with point-in-time recovery.
- [On-demand backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html): Learn how to use DynamoDB's backup and restore features, including on-demand backups, point-in-time recovery, and the ability to create full backups for long-term retention and regulatory compliance, all with zero impact on table performance or availability.
- [Billing for backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backup-restore-billing.html): Learn how DynamoDB's backup and restoration features are billed, including on-demand backups, point-in-time recovery, and the impact of backup retention policies on monthly charges.
- [Restores](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/pointintimerecovery_restores.html): Learn more about restoring tables in DynamoDB using point in time recovery.
- [Using AWS Backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorksAWS.html): Learn how DynamoDB can be backed up and restored using the AWS Backup service. 

## Code examples
- [Code examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples.html): Code examples that show how to use DynamoDB with an AWS SDK.
- [Basics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_basics.html): The following code examples show how to use the basics of DynamoDB with AWS SDKs.
- [Scenarios](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_scenarios.html): The following code examples show how to use DynamoDB with AWS SDKs.
- [Serverless examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_serverless_examples.html): The following code examples show how to use DynamoDB with AWS SDKs.
- [AWS community contributions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/service_code_examples_aws_community_contributions.html): AWS community contributions are examples that were created and are maintained by multiple teams across AWS. 

## Security
- [Security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html): Configure DynamoDB to meet your security and compliance objectives, and learn how to use other AWS services that can help you to secure your DynamoDB resources.
- [AWS managed policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-security-iam.awsmanpol.html): This page provides an overview of AWS managed policies for DynamoDB, including details on the DynamoDBReplicationServiceRolePolicy and AmazonDynamoDBReadOnlyAccess policies, and recent updates to these policies. 
- [Resource-based policies](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html): Learn how resource-based permissions policies for DynamoDB let you grant usage permissions to other AWS accounts or organizations on a per-resource basis.
- [Attribute-based access control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/attribute-based-access-control.html): Learn how to use attribute-based access control (ABAC) with DynamoDB tables and indexes to simplify permissions management and enhance security.
- [Data protection](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-protection.html): Explore the data protection features of DynamoDB, including encryption at rest and in transit, as well as the data protection capabilities of the DAX. 
- [IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/identity-and-access-mgmt.html): Authenticate requests and manage permissions to access your Amazon DynamoDB resources through the IAM API.
- [Compliance validation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Compliance.html): Learn what AWS services are in scope of a specific compliance program and where to go for more detailed information.
- [Resilience](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/disaster-recovery-resiliency.html): AWS architecture supports data redundancy and specific DynamoDB features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/network-isolation.html): Learn how Amazon DynamoDB isolates service traffic.
- [AWS PrivateLink for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html): Connect to DynamoDB by using AWS PrivateLink interface Amazon VPC endpoints in your virtual private cloud (Amazon VPC).
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/configuration-vulnerability.html): Learn about configuration and vulnerability analysis in DynamoDB. 
- [Security best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices-security.html): Explore security best practices for DynamoDB, including encryption, IAM policies, VPC endpoints, and monitoring tools like CloudTrail, Config, and Security Hub to detect and prevent security issues.

## Monitoring and logging
- [Monitoring and logging](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/MonitoringAndLoggingInDynamoDB.html): How to monitor usage of your Amazon DynamoDB resources.
- [Monitoring metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Monitoring-metrics-with-Amazon-CloudWatch.html): You can monitor DynamoDB using CloudWatch, which collects and processes raw data from DynamoDB into readable, near real-time metrics.
- [Logging operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/logging-using-cloudtrail.html): Learn how to access the history of DynamoDB API calls by enabling CloudTrail, a service that provides a record of actions taken by users, roles, or AWS services. 
- [Contributor Insights](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights.html): Quickly identify the most frequently accessed and throttled keys in your DynamoDB table or index using CloudWatch Contributor Insights. 

## Best practices
- [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html): Learn about best practices for designing and architecting with Amazon DynamoDB, a NoSQL database service. 
- [NoSQL design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html): Review the key differences and design principles for NoSQL database systems like DynamoDB
- [The DynamoDB Well-Architected Lens](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-wal.html): Learn about the DynamoDB Well-Architected Lens, a collection of design principles and guidance for designing well-architected DynamoDB workloads, covering the six pillars of the AWS Well-Architected Framework: performance efficiency, cost optimization, operational excellence, reliability, security, and sustainability.
- [Partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html): Learn about best practices for designing and using partition keys effectively in DynamoDB. 
- [Sort key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-sort-keys.html): Design sort keys in DynamoDB to organize data for efficient querying. 
- [Secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes.html): Learn about the best practices for using secondary indexes in DynamoDB, including guidelines on efficient use, careful projection, and avoiding fetches. 
- [Large items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html): Read about best practices for storing large items and attribute values in DynamoDB. 
- [Time series data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html): Learn about best practices for handling time-series data in DynamoDB. 
- [Many-to-many relationships](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-adjacency-graphs.html): Learn best practices for modeling many-to-many relationships in DynamoDB using the adjacency list and materialized graph patterns, highlighting their advantages and use cases, and recommending Amazon Neptune for highly connected datasets requiring real-time graph queries.
- [Querying and scanning](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html): Learn about best practices for using Query and Scan operations in DynamoDB, including performance considerations, avoiding spikes in read activity, and leveraging parallel scans to improve efficiency while managing provisioned throughput.
- [Table design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-table-design.html): Explore best practices for designing DynamoDB tables, including recommendations to minimize the number of tables, considerations for account and service limits, and guidance on working with AWS solution architects for multi-tenant designs.
- [Using global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html): Learn about best practices for designing and deploying Amazon DynamoDB global tables, including guidance on write modes, request routing, Region evacuation, and capacity planning to achieve low-latency reads and writes with high availability and resiliency.
- [Control plane](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-control-plane.html): Explore best practices for managing the DynamoDB control plane, including avoiding excessive control plane calls, separating control and data plane operations, handling throttling, and caching data to optimize performance.
- [Bulk data operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_BulkDataOperations.html): Learn about best practices for using advanced design patterns when you need to perform bulk operations, implement robust version control mechanisms, or manage time-sensitive data.
- [Implementing version control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices_ImplementingVersionControl.html): Implement item version control in DynamoDB using optimistic locking to manage concurrent writes and ensure data integrity in distributed systems.
- [Billing and Usage Reports](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-understanding-billing.html): Explore the various usage types and billing codes for charges related to DynamoDB, including provisioned and on-demand capacity, streams, backups, data transfer, and the DynamoDB Accelerator (DAX). 
- [Migrating a DynamoDB table from one account to another](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-migrating-table-between-accounts.html): Explore guidance on migrating a DynamoDB table from one AWS account to another, using either the AWS Backup service for cross-account backup and restore, or DynamoDB's export to Amazon S3 and import from Amazon S3 features.
- [DAX prescriptive guidance](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-prescriptive-guidance.html): Explore comprehensive insights and best practices for integrating the DynamoDB Accelerator (DAX) with DynamoDB applications, including when to use DAX, configuring clusters, sizing, deploying, and monitoring strategies.

## Using DynamoDB with other AWS services
- [Using DynamoDB with other AWS services](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OtherServices.html): Learn how to use and integrate Amazon DynamoDB with other AWS services.
- [Integrating with Amazon Cognito](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Cognito.Credentials.html): Learn how to configure Amazon Cognito credentials to integrate with DynamoDB and other AWS services for your web and mobile applications, using IAM roles to generate temporary credentials for authenticated and unauthenticated users.
- [Integrating with Amazon Redshift](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB.html): Copy data from Amazon Redshift to DynamoDB and run complex data analysis queries in Amazon Redshift, using real-time operations in DynamoDB and analytical operations in Amazon Redshift.
- [Integrating with Amazon EMR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.html): Use Amazon EMR to analyze, process and copy data in Amazon DynamoDB.
- [Integrating with S3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3forDynamoDB.html): In this section, discover what you need to know about integrating import from export to Amazon S3 with DynamoDB.
- [Integrating with Amazon SageMaker Lakehouse](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/amazon-sagemaker-lakehouse-for-DynamoDB.html): Explore how to integrate with Amazon SageMaker Lakehouse in DynamoDB zero-ETL.
- [Integrating with Amazon OpenSearch Service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OpenSearchIngestionForDynamoDB.html): Learn how DynamoDB integrates with Amazon OpenSearch Service with the DynamoDB plugin for OpenSearch Ingestion. 
- [Integrating with Amazon EventBridge](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/eventbridge-for-dynamodb.html): Learn how you can enable seamless data flow from DynamoDB to an EventBridge bus.
- [Integrating with Amazon MSK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/msk-for-dynamodb.html): Learn how Amazon Managed Streaming for Apache Kafka integrates with Amazon DynamoDB by reading data from Apache Kafka topics and storing it in DynamoDB. 
- [Integration best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-integration.html): Learn about best practices for integrating other AWS services with DynamoDB, including creating snapshots, capturing data changes, and using DynamoDB Streams or Amazon Kinesis Data Streams for near real-time change data capture.

## Using generative AI with DynamoDB
- [Using generative AI with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-ai-integration.html): Learn about the DynamoDB.
- [Leveraging DynamoDB Zero-ETL integration with OpenSearch Service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ddb-and-amazon-bedrock.html): You can use Amazon Bedrock with DynamoDB to provide serverless access to foundational models (FMs), such as Amazon Titan and other third-party models. 

## Quotas and constraints
- [Quotas and constraints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotasRevised.html): Explore the service, account, and table quotas in DynamoDB, including throughput, transactions, backup, and more, to optimize your workloads.
- [Requesting a quota increase](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RequestingQuotaIncrease.html): You can request a quota increase for each Region using the Service Quotas console, AWS CLI or a support case. 
- [Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html): Examine the service, account, and table level quotas in place with DynamoDB, and learn which are default values and which can be tuned for your workloads.
- [Constraints](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Constraints.html): Understand the constraints when working with DynamoDB.

## API reference
- [API reference](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CurrentAPI.html): Explore a comprehensive overview of the low-level DynamoDB API, including details on the various operations supported by DynamoDB, DynamoDB Streams, and DAX. 

## Troubleshooting
- [Troubleshooting](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Troubleshooting.html): Diagnose and resolve common issues with Amazon DynamoDB.
- [Internal server errors](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingInternalServerErrors.html): Explore a comprehensive guide on troubleshooting internal server errors (ISEs) in DynamoDB. 
- [Latency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingLatency.html): Learn different strategies to troubleshoot high latency on a Amazon DynamoDB table.
- [Throttling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TroubleshootingThrottling.html): Learn how to understand, diagnose, and resolve throttling issues in Amazon DynamoDB tables.

## Appendix
- [Appendix](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.html): In this appendix, you'll find additional information on sample tables and data, uploading data, and older API references for DynamoDB. 
- [Troubleshooting SSL/TLS connection establishment issues with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ats-certs.html): Learn more about troubleshooting SSL/TLS connection establishment issues.
- [Example tables and data for use in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleTables.html): This section presents sample tables and data for the DynamoDB Developer Guide, including the ProductCatalog, Forum, Thread, and Reply tables with their primary keys. 
- [Creating example tables and uploading data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AppendixSampleDataCode.html): Learn how to create example tables and upload data programmatically with DynamoDB.
- [Example application using AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.html): In this example application, the Tic-Tac-Toe game illustrates how to use the AWS SDK for Python (Boto3) to write a high performance and scalable application for Amazon DynamoDB.
- [Reserved words in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html): Learn about using reserved words in Amazon DynamoDB.
- [AWS SDK for Java 1.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.JavaSDKv1.html): Learn more about example code for using DynamoDB and DAX with AWS SDK for Java 1.x.
- [AWS SDK for Go 1.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.GoSDKv1.html): Learn more about example code for using DynamoDB and DAX with AWS Go 1.x.
- [AWS SDK for Node.js 2.x examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.SDKNodejsv2.html): Learn more about example code for using DynamoDB and DAX with AWS SDK for Node.js 2.x.

## Document history
- [Document history](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html): Find the revision dates, related releases, and important changes to the DynamoDB Developer Guide.

## Legacy features
- [Legacy features](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyFeatures.html): Learn which DynamoDB features are still supported, but no longer actively developed. 
- [Global tables version 2017.11.29 (Legacy)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V1.html): Learn about Global Tables Version 2017.11.29 (Legacy), an older version of DynamoDB global tables that provides multi-Region, multi-active database replication.
- [Previous low-level DynamoDB API version (2011-12-05)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Appendix.APIv20111205.html): Learn about document operations from the previous version of the Amazon DynamoDB API for backward compatibility with existing applications.
- [Legacy DynamoDB conditional parameters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html): Learn how to use legacy conditional parameters for backward compatibility in Amazon DynamoDB requests.
