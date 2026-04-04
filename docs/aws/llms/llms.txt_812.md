# Source: https://docs.aws.amazon.com/streams/latest/dev/llms.txt

# Amazon Kinesis Data Streams Developer Guide

> This is official Amazon Web Services (AWS) documentation for Amazon Kinesis Data Streams. With Kinesis Data Streams, you can build custom applications that process or analyze streaming data for specialized needs. It can continuously capture and store terabytes of data per hour from hundreds of thousands of sources such as website clickstreams, financial transactions, social media feeds, IT logs, and location-tracking events. With the Kinesis Client Library (KCL), you can build Kinesis applications and use streaming data to power real-time dashboards, generate alerts, implement dynamic pricing and advertising, and more. You can also emit data from Kinesis Data Streams to other AWS services such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon EMR, and AWS Lambda. This guide provides a conceptual overview of Kinesis Data Streams and includes detailed instructions for using the service.

- [What is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Terminology and concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
- [Quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Complete prerequisites to set up Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/before-you-begin.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/streams/latest/dev/sdk-general-information-section.html)
- [Document history](https://docs.aws.amazon.com/streams/latest/dev/history.html)

## [Use the AWS CLI to perform Amazon Kinesis Data Streams operations](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)

- [Tutorial: Install and configure the AWS CLI for Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/kinesis-tutorial-cli-installation.html): Install and configure the AWS CLI.
- [Tutorial: Perform basic Kinesis Data Streams operations using the AWS CLI](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html): Learn how to perform basic Kinesis Data Streams operations using the AWS CLI.


## [Getting started tutorials](https://docs.aws.amazon.com/streams/latest/dev/examples.html)

### [Tutorial: Process real-time stock data using KPL and KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2.html)

Learn how to use Amazon Kinesis Data Streams with a real-time stock analysis simulation.

- [Complete prerequisites](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-begin.html): You must meet the following requirements to complete this tutorial:
- [Create a data stream](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-create-stream.html): First, you must create the data stream that you will use in subsequent steps of this tutorial.
- [Create an IAM policy and user](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-iam.html): Security best practices for AWS dictate the use of fine-grained permissions to control access to different resources.
- [Download and build the code](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-download.html): This topic provides sample implementation code for the sample stock trades ingestion into the data stream (producer) and the processing of this data (consumer).
- [Implement the producer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-producer.html): This tutorial uses the real-world scenario of stock market trade monitoring.
- [Implement the consumer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-consumer.html): The consumer application in this tutorial continuously processes the stock trades in your data stream.
- [(Optional) Extend the consumer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-consumer-extension.html): This optional section shows how you can extend the consumer code for a slightly more elaborate scenario.
- [Clean up resources](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-finish.html): Clean up resources by deleting the Kinesis data stream and DynamoDB table.

### [Tutorial: Process real-time stock data using KPL and KCL 1.x](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl.html)

Learn how to use Amazon Kinesis Data Streams with a real-time stock analysis simulation.

- [Complete prerequisites](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-begin.html): Steps to get started with the Analyzing Real-Time Stock Data tutorial for Kinesis Data Streams.
- [Create a data stream](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-create-stream.html): Create a data stream for the Kinesis Data Streams Analyzing Real-Time Stock Data tutorial.
- [Create an IAM policy and user](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-iam.html): Create an IAM policy and a user for the Kinesis Data Streams Analyzing Real-Time Stock Data tutorial.
- [Download and build the implementation code](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-download.html): Download and build the provided code for the Kinesis Data Streams Analyzing Real-Time Stock Data tutorial.
- [Implement the producer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-producer.html): Implement the producer code for ingesting data in the Kinesis Data Streams Analyzing Real-Time Stock Data tutorial.
- [Implement the consumer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-consumer.html): Walk through implementing the consumer code for processing data in the Kinesis Data Streams Analyzing Real-Time Stock Data tutorial.
- [(Optional) Extend the consumer](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-consumer-extension.html): Add functionality to the Kinesis Data Streams consumer code for different priorities.
- [Clean up resources](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-finish.html): Clean up resources by deleting the Kinesis data stream and DynamoDB table.

### [Tutorial: Analyze real-time stock data using Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data.html)

Learn how to use Amazon Kinesis Data Streams and Amazon Managed Service for Apache Flink with a real-time stock analysis simulation.

- [Step 1: Set up an account](https://docs.aws.amazon.com/streams/latest/dev/setting-up.html): Before you use Amazon Managed Service for Apache Flink for the first time, complete the following tasks:
- [Step 2: Set up the AWS CLI](https://docs.aws.amazon.com/streams/latest/dev/setup-awscli.html): In this step, you download and configure the AWS CLI to use with Amazon Managed Service for Apache Flink.
- [Step 3: Create an application](https://docs.aws.amazon.com/streams/latest/dev/get-started-exercise.html): In this exercise, you create a Managed Service for Apache Flink application with data streams as a source and a sink.
- [Tutorial: Use AWS Lambda with Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-lambda.html): Learn how to use a Lambda function to consume events from a Kinesis data stream
- [Use the AWS Streaming Data Solution for Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/examples-streaming-solution.html): The AWS Streaming Data Solution for Amazon Kinesis automatically configures the AWS services necessary to easily capture, store, process, and deliver streaming data.


## [Create and manage Kinesis data streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html)

- [Choose the right mode to stream in](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html): The following topics explain how to choose the best mode for your application and how to switch between modes, if needed.
- [Create a stream using the AWS Management Console](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-create-a-stream.html): You can create a stream using the Kinesis Data Streams console, the Kinesis Data Streams API, or the AWS Command Line Interface (AWS CLI).
- [Create a stream using the APIs](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-create-stream.html): Learn how to create Kinesis data streams with the AWS SDK for Java.
- [Update a stream](https://docs.aws.amazon.com/streams/latest/dev/updating-a-stream.html): You can update the details of a stream using the Kinesis Data Streams console, the Kinesis Data Streams API, or the AWS CLI.
- [List streams](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-streams.html): Learn how to list Kinesis data streams with the AWS SDK for Java.
- [List shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-shards.html): Learn how to list the shards of a stream with the AWS SDK for Java.
- [Delete a stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-delete-stream.html): Learn how to delete Kinesis data streams with the AWS SDK for Java.

### [Reshard a stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding.html)

Learn how to reshard Kinesis data streams with the AWS SDK for Java.

- [Decide on a strategy for resharding](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding-strategies.html): Learn strategies for resharding Kinesis data streams with the AWS SDK for Java.
- [Split a shard](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding-split.html): Learn how to split shards of Kinesis data streams with the AWS SDK for Java.
- [Merge two shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding-merge.html): Learn how to merge shards of Kinesis data streams with the AWS SDK for Java.
- [Complete the resharding action](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html): Learn what to do after resharding of Kinesis data streams with the AWS SDK for Java.
- [Change the data retention period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html): Learn how to change the record retention period for Kinesis data streams.
- [Tag your resources](https://docs.aws.amazon.com/streams/latest/dev/tagging.html): Assign your own metadata tags to your Amazon Kinesis Data Streams resources so that you can manage them.
- [Handle large records](https://docs.aws.amazon.com/streams/latest/dev/large-records.html): Amazon Kinesis Data Streams supports records up to 10 mebibytes (MiBs).

### [Perform resilience testing with AWS Fault Injection Service](https://docs.aws.amazon.com/streams/latest/dev/kinesis-fis.html)

AWS Fault Injection Service is a fully managed service that helps you perform fault injection experiments on your AWS workloads.

- [Provisioned throughput exception errors](https://docs.aws.amazon.com/streams/latest/dev/kinesis-fis-provisioned-throughput.html): Provisioned throughput exceeded exception errors (HTTP 400) occur when the request rate for a Kinesis stream surpasses the throughput limits of one or more shards.
- [Expired iterator exception errors](https://docs.aws.amazon.com/streams/latest/dev/kinesis-fis-expired-iterator.html): Expired iterator exception errors (HTTP 400) occur when the shard iterator is expired, and is no longer used to retrieve stream records when calling GetRecords.


## [Write data to Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-producers.html)

### [Develop producers using the Amazon Kinesis Producer Library (KPL)](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-kpl.html)

The KPL provides design patterns and code for Amazon Kinesis Data Streams producer applications.

- [Install the KPL](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-dl-install.html): Installation information for the KPL.
- [Migrate to KPL 1.x](https://docs.aws.amazon.com/streams/latest/dev/kpl-migration-1x.html): Migration information to KPL 1.x.
- [Transition to Amazon Trust Services (ATS) certificates for the KPL](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-upgrades.html): Upgrade your KPL installation to use a version that supports ATS certificates.
- [KPL supported platforms](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-supported-plats.html): The KPL currently supports the following platforms and source code information.
- [KPL key concepts](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html): The KPL introduces some new concepts and terminology.
- [Integrate the KPL with producer code](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-integration.html): Learn about running the KPL as a microservice.
- [Write to your Kinesis data stream using the KPL](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-writing.html): Many common use cases for producers can be implemented using the KPL.
- [Configure the KPL](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-config.html): Customize configuration parameters for the KPL.
- [Implement consumer de-aggregation](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-consumer-deaggregation.html): Consumer-side considerations and procedures should be considered when using the KPL.
- [Use the KPL with Amazon Data Firehose](https://docs.aws.amazon.com/streams/latest/dev/kpl-with-firehose.html): If you use the Kinesis Producer Library (KPL) to write data to a Kinesis data stream, you can use aggregation to combine the records that you write to that Kinesis data stream.
- [Use the KPL with the AWS Glue Schema Registry](https://docs.aws.amazon.com/streams/latest/dev/kpl-with-schemaregistry.html): You can integrate your Kinesis data streams with the AWS Glue Schema Registry.
- [Configure the KPL proxy configuration](https://docs.aws.amazon.com/streams/latest/dev/kpl-proxy-configuration.html): For applications that cannot directly connect to the internet, all AWS SDK clients support the use of HTTP or HTTPS proxies.
- [KPL version lifecycle policy](https://docs.aws.amazon.com/streams/latest/dev/kpl-version-lifecycle-policy.html): This topic outlines the version lifecycle policy for Amazon Kinesis Producer Library (KPL).

### [Develop producers using the Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html)

Examples and guidance for developing Amazon Kinesis Data Streams producers using the Amazon Kinesis Data Streams API.

- [Interact with data using the AWS Glue Schema Registry](https://docs.aws.amazon.com/streams/latest/dev/kinesis-integration-glue-schema-registry.html): You can integrate your Kinesis data streams with the AWS Glue Schema Registry.
- [Write to Amazon Kinesis Data Streams using Kinesis Agent](https://docs.aws.amazon.com/streams/latest/dev/writing-with-agents.html): Guide for using Amazon Kinesis Data Streams agent.

### [Write to Kinesis Data Streams using other AWS services](https://docs.aws.amazon.com/streams/latest/dev/using-other-services.html)

Writing to Kinesis Data Streams using other AWS Services

- [Write to Kinesis Data Streams using AWS Amplify](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-amplify.html): You can use Amazon Kinesis Data Streams to stream data from your mobile applications built with AWS Amplify for real-time processing.
- [Write to Kinesis Data Streams using Amazon Aurora](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-aurora.html): Amazon Aurora
- [Write to Kinesis Data Streams using Amazon CloudFront](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-CloudFront.html): Amazon CloudFront
- [Write to Kinesis Data Streams using Amazon CloudWatch Logs](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-cw-logs.html): Amazon CloudWatch Logs
- [Write to Kinesis Data Streams using Amazon Connect](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-connect.html): Amazon Connect
- [Write to Kinesis Data Streams using AWS Database Migration Service](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-migration.html): AWS Database Migration Service
- [Write to Kinesis Data Streams using Amazon DynamoDB](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-ddb.html): Amazon DynamoDB
- [Write to Kinesis Data Streams using Amazon EventBridge](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-eventbridges.html): Amazon EventBridge
- [Write to Kinesis Data Streams using AWS IoT Core](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-iot-core.html): You can write data in real time from MQTT messages in AWS IoT Core by using AWS IoT Rule actions.
- [Write to Kinesis Data Streams using Amazon Relational Database Service](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-rds.html): Amazon Relational Database Service
- [Write to Kinesis Data Streams usingAmazon Pinpoint](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-pinpoint.html): Amazon Pinpoint
- [Write to Kinesis Data Streams using Amazon Quantum Ledger Database (Amazon QLDB)](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-quantum-ledger.html): Amazon Quantum Ledger Database

### [Write to Kinesis Data Streams using third-party integrations](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-third-party.html)

Write to Kinesis Data Streams using third-party integrations

- [Apache Flink](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-flink.html): Apache Flink
- [Fluentd](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-Fluentd.html): Fluentd
- [Debezium](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-Debezium.html): Debezium
- [Oracle GoldenGate](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-Oracle-GoldenGate.html): Oracle GoldenGate
- [Kafka Connect](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-kafka-connect.html): Kafka Connect
- [Adobe Experience](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-adobe.html): Adobe Experience
- [Striim](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-Striim.html): Striim
- [Troubleshoot Kinesis Data Streams producers](https://docs.aws.amazon.com/streams/latest/dev/troubleshooting-producers.html): Get solutions to problems found while using Amazon Kinesis Data Streams producers.

### [Optimize Kinesis Data Streams producers](https://docs.aws.amazon.com/streams/latest/dev/advanced-producers.html)

Learn how to optimize your Amazon Kinesis Data Streams producer.

- [Customize KPL retries and rate limit behavior](https://docs.aws.amazon.com/streams/latest/dev/kinesis-producer-adv-retries-rate-limiting.html): Customize retry and rate limit behavior in Amazon Kinesis Data Streams.
- [Apply best practices to KPL aggregation](https://docs.aws.amazon.com/streams/latest/dev/kinesis-producer-adv-aggregation.html): Best practices for KPL aggregation in Amazon Kinesis Data Streams.


## [Read data from Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)

### [Develop enhanced fan-out consumers with dedicated throughput](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html)

Learn how to develop consumers that receive records from Kinesis data streams with dedicated throughput.

- [Manage enhanced fan-out consumers](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-console.html): Consumers that use enhanced fan-out in Amazon Kinesis Data Streams can receive records from a data stream with dedicated throughput of up to 2 MB of data per second per shard.
- [Use the Data Viewer in the Kinesis console](https://docs.aws.amazon.com/streams/latest/dev/data-viewer.html): The Data Viewer in the Kinesis Management Console lets you view data records within the specified shard of your data stream without having to develop a consumer application.
- [Query your data streams in the Kinesis console](https://docs.aws.amazon.com/streams/latest/dev/querying-data.html): The Data Analytics tab in the Kinesis Data Streams Console lets you query your data streams using SQL.

### [Use Kinesis Client Library](https://docs.aws.amazon.com/streams/latest/dev/kcl.html)

What is Kinesis Client Library and how it works.

- [KCL concepts](https://docs.aws.amazon.com/streams/latest/dev/kcl-concepts.html): Explains the basic Kinesis Client Library (KCL) concepts.
- [DynamoDB metadata tables and load balancing in KCL](https://docs.aws.amazon.com/streams/latest/dev/kcl-dynamoDB.html): Learn about DynamoDB metadata tables and load balancing in the Kinesis Client Library.

### [Develop consumers with KCL](https://docs.aws.amazon.com/streams/latest/dev/develop-kcl-consumers.html)

Develop consumers with KCL

- [Develop consumers with KCL in Java](https://docs.aws.amazon.com/streams/latest/dev/develop-kcl-consumers-java.html): Develop consumers with KCL in Java.
- [Develop consumers with KCL in non-Java languages](https://docs.aws.amazon.com/streams/latest/dev/develop-kcl-consumers-non-java.html): Guide for building consumers with KCL in non-Java languages
- [Multi-stream processing with KCL](https://docs.aws.amazon.com/streams/latest/dev/kcl-multi-stream.html): Learn about multi-stream processing with KCL.
- [Use the AWS Glue Schema registry with KCL](https://docs.aws.amazon.com/streams/latest/dev/kcl-glue-schema.html): You can integrate Kinesis Data Streams with the AWS Glue Schema registry.
- [IAM permissions required for KCL consumer applications](https://docs.aws.amazon.com/streams/latest/dev/kcl-iam-permissions.html): You must add the following permissions to the IAM role or user associated with your KCL consumer application.
- [KCL configurations](https://docs.aws.amazon.com/streams/latest/dev/kcl-configuration.html): You can set configuration properties to customize Kinesis Client Library's functionality to meet your specific requirements.
- [KCL version lifecycle policy](https://docs.aws.amazon.com/streams/latest/dev/kcl-version-lifecycle-policy.html): This topic outlines the version lifecycle policy for Amazon Kinesis Client Library (KCL).

### [Migrate from previous KCL versions](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-previous-versions.html)

Migrate from previous versions of KCL

- [Migrate from KCL 2.x to KCL 3.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-from-2-3.html): This topic provides step-by-step instructions to migrate your consumer from KCL 2.x to KCL 3.x.
- [Roll back to the previous KCL version](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-rollback.html): This topic explains the steps to roll back your consumer back to the previous version.
- [Roll forward to KCL 3.x after a rollback](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-rollforward.html): This topic explains the steps to roll forward your consumer back to KCL 3.x after a rollback.
- [Best practices for the lease table with provisioned capacity mode](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-lease-table.html): If the lease table of your KCL application was switched to provisioned capacity mode, KCL 3.x creates a global secondary index on the lease table with the provisioned billing mode and the same read capacity units (RCU) and write capacity units (WCU) as the base lease table.
- [Migrating from KCL 1.x to KCL 3.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-1-3.html): This topic explains the instructions to migrate your consumer from KCL 1.x to KCL 3.x.

### [Previous KCL version documentation](https://docs.aws.amazon.com/streams/latest/dev/kcl-archive.html)

Deprecated KCL documentation

- [KCL 1.x and 2.x information](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html): What is Kinesis Client Library and how it works.

### [Develop custom consumers with shared throughput](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-consumers.html)

Guide for building Amazon Kinesis Data Streams consumers that share throughput with other consumers reading from the same stream.

### [Develop custom consumers with shared throughput using KCL](https://docs.aws.amazon.com/streams/latest/dev/custom-kcl-consumers.html)

Developing Custom Consumers with Shared Throughput Using KCL

### [Develop KCL 1.x consumers](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-kcl.html)

The KCL provides design patterns and code for Amazon Kinesis Data Streams consumer applications.

- [Develop a Kinesis Client Library consumer in Java](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-java.html): Learn fundamentals of developing a consumer application in Java using KCL.
- [Develop a Kinesis Client Library consumer in Node.js](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-nodejs.html): Learn fundamentals of developing a consumer application in Node.js using KCL.
- [Develop a Kinesis Client Library consumer in .NET](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-dotnet.html): Learn fundamentals of developing a consumer application in .NET using KCL.
- [Develop a Kinesis Client Library consumer in Python](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-py.html): Learn the fundamentals of developing a consumer application in Python using KCL.
- [Develop a Kinesis Client Library consumer in Ruby](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-ruby.html): Learn fundamentals of developing a consumer application in Ruby using KCL.

### [Develop KCL 2.x Consumers](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-kcl-v2.html)

The KCL provides design patterns and code for Amazon Kinesis Data Streams consumer applications.

- [Develop a Kinesis Client Library consumer in Java](https://docs.aws.amazon.com/streams/latest/dev/kcl2-standard-consumer-java-example.html)
- [Develop a Kinesis Client Library consumer in Python](https://docs.aws.amazon.com/streams/latest/dev/kcl2-standard-consumer-python-example.html)

### [Develop enhanced fan-out consumers with KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-kcl-retired.html)

- [Develop enhanced fan-out consumers using KCL 2.x in Java](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-kcl-java.html)
- [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html): Migrate the record processor in Amazon Kinesis from Kinesis Client Library version 1.x to version 2.x.

### [Develop consumers with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/develop-consumers-sdk.html)

Examples and guidance for developing Amazon Kinesis Data Streams consumers using the Amazon Kinesis Data Streams API.

- [Develop shared-throughput consumers with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-sdk.html): Examples and guidance for developing Amazon Kinesis Data Streams consumers using the Amazon Kinesis Data Streams API.
- [Develop enhanced fan-out consumers with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html): Enhanced fan-out is an Amazon Kinesis Data Streams feature that enables consumers to receive records from a data stream with dedicated throughput of up to 2 MB of data per second per shard.
- [Interact with data using the AWS Glue Schema Registry](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-glue-schema-registry.html): You can integrate your Kinesis data streams with the AWS Glue Schema Registry.
- [Develop consumers using AWS Lambda](https://docs.aws.amazon.com/streams/latest/dev/lambda-consumer.html): You can use an AWS Lambda function to process records in a data stream.
- [Develop consumers using Managed Service for Apache Flink](https://docs.aws.amazon.com/streams/latest/dev/kda-consumer.html): You can use an Amazon Managed Service for Apache Flink application to process and analyze data in a Kinesis stream using SQL, Java, or Scala.
- [Develop consumers using Amazon Data Firehose](https://docs.aws.amazon.com/streams/latest/dev/kdf-consumer.html): You can use a Firehose to read and process records from a Kinesis stream.

### [Use other AWS services to read data from Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read.html)

Using other AWS Services to read data from Kinesis Data Streams

- [Read data from Kinesis Data Streams using Amazon EMR](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-emr.html): Using Amazon EMR
- [Read data from Kinesis Data Streams using Amazon EventBridge Pipes](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-ev-pipes.html): Using Amazon EventBridge Pipes
- [Read data from Kinesis Data Streams using AWS Glue](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-glue.html): Using AWS Glue
- [Read data from Kinesis Data Streams using Amazon Redshift](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-redshift.html): Using Amazon Redshift

### [Read from Kinesis Data Streams using third-party integrations](https://docs.aws.amazon.com/streams/latest/dev/using-services-third-party-read.html)

Using third-party integrations

- [Apache Flink](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-flink.html): Apache Flink
- [Adobe Experience Platform](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-adobe.html): Adobe Experience Platform
- [Apache Druid](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-druid.html): Apache Druid
- [Apache Spark](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-spark.html): Apache Spark
- [Databricks](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-databricks.html): Databricks
- [Kafka Confluent Platform](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-kafka.html): Kafka Confluent Platform
- [Kinesumer](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-kinesumer.html): Kinesumer
- [Talend](https://docs.aws.amazon.com/streams/latest/dev/using-other-services-read-talend.html): Talend
- [Troubleshoot Kinesis Data Streams consumers](https://docs.aws.amazon.com/streams/latest/dev/troubleshooting-consumers.html): Get solutions to problems found while using Amazon Kinesis Data Streams consumers.

### [Optimize Kinesis Data Streams consumers](https://docs.aws.amazon.com/streams/latest/dev/advanced-consumers.html)

Learn how to optimize your Amazon Kinesis Data Streams consumer.

- [Improve low-latency processing](https://docs.aws.amazon.com/streams/latest/dev/kinesis-low-latency.html): Learn how to poll your stream efficiently.
- [Process serialized data using AWS Lambda with the Amazon Kinesis Producer Library](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-deaggregation.html): Deaggregating KPL records when using AWS Lambda.
- [Use resharding, scaling, and parallel processing to change the number of shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html): Learn how to increase or decrease the number of shards in your stream.
- [Handle duplicate records](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-duplicates.html): Learn to understand duplicate record handling in your Kinesis data stream.
- [Handle startup, shutdown, and throttling](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-additional-considerations.html): Learn design tips for your Amazon Kinesis Data Streams applications.


## [Monitor Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring.html)

- [Monitor the Kinesis Data Streams service with CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html): View the metrics that the Amazon Kinesis Data Streams service sends to CloudWatch.
- [Monitor Kinesis Data Streams Agent health with CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/agent-health.html): Monitoring the agent using custom CloudWatch metrics.
- [Log Amazon Kinesis Data Streams API calls with AWS CloudTrail](https://docs.aws.amazon.com/streams/latest/dev/logging-using-cloudtrail.html): Amazon Kinesis Data Streams is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Kinesis Data Streams.
- [Monitor the KCL with CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-kcl.html): Understand the metrics provided in the Kinesis Client Library.
- [Monitor the KPL with CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-kpl.html): Understand the metrics provided in the Kinesis Producer Library.


## [Security](https://docs.aws.amazon.com/streams/latest/dev/security.html)

### [Data protection in Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)

Learn how to use server-side encryption with Amazon Kinesis Data Streams.

- [What is server-side encryption for Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/what-is-sse.html): Server-side encryption is a feature in Amazon Kinesis Data Streams that automatically encrypts data before it's at rest by using an AWS KMS customer master key (CMK) you specify.
- [Costs, Regions, and performance considerations](https://docs.aws.amazon.com/streams/latest/dev/costs-performance.html): When you apply server-side encryption, you are subject to AWS KMS API usage and key costs.
- [How do I get started with server-side encryption?](https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html): The easiest way to get started with server-side encryption is to use the AWS Management Console and the Amazon Kinesis KMS Service Key, aws/kinesis.
- [Create and use user-generated KMS keys](https://docs.aws.amazon.com/streams/latest/dev/creating-using-sse-master-keys.html): This section describes how to create and use your own KMS keys, instead of using the master key administered by Amazon Kinesis.
- [Permissions to use user-generated KMS keys](https://docs.aws.amazon.com/streams/latest/dev/permissions-user-key-KMS.html): Before you can use server-side encryption with a user-generated KMS key, you must configure AWS KMS key policies to allow encryption of streams and encryption and decryption of stream records.
- [Verify and Troubleshoot KMS key permissions](https://docs.aws.amazon.com/streams/latest/dev/sse-troubleshooting.html): After enabling encryption on a Kinesis stream, we recommend that you monitor the success of your putRecord, putRecords, and getRecords calls using the following Amazon CloudWatch metrics:
- [Use Kinesis Data Streams with interface VPC endpoints](https://docs.aws.amazon.com/streams/latest/dev/vpc.html): Learn how to use Amazon Kinesis Data Streams with interface VPC endpoints.

### [Controlling access to Kinesis Data Streams resources using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html)

Control access to your Amazon Kinesis Data Streams resources by using AWS Identity and Access Management (IAM).

- [Share access using resource-based policies](https://docs.aws.amazon.com/streams/latest/dev/resource-based-policy-examples.html)
- [Compliance validation for Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/akda-java-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience in Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific Kinesis Data Streams features for data resiliency.
- [Infrastructure security in Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/infrastructure-security.html): Learn how Amazon Kinesis Data Streams isolates service traffic.
- [Security best practices for Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/security-best-practices.html): Amazon Kinesis Data Streams provides a number of security features to consider as you develop and implement your own security policies.


## [Code examples](https://docs.aws.amazon.com/streams/latest/dev/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/streams/latest/dev/service_code_examples_basics.html)

The following code examples show how to use the basics of Kinesis with AWS SDKs.

- [Learn the basics](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_Scenario_GettingStarted_section.html): Learn the basics of Kinesis with an AWS SDK

### [Actions](https://docs.aws.amazon.com/streams/latest/dev/service_code_examples_actions.html)

The following code examples show how to use Kinesis with AWS SDKs.

- [AddTagsToStream](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_AddTagsToStream_section.html): Use AddTagsToStream with an AWS SDK or CLI
- [CreateStream](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_CreateStream_section.html): Use CreateStream with an AWS SDK or CLI
- [DeleteStream](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_DeleteStream_section.html): Use DeleteStream with an AWS SDK or CLI
- [DeregisterStreamConsumer](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_DeregisterStreamConsumer_section.html): Use DeregisterStreamConsumer with an AWS SDK or CLI
- [DescribeStream](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_DescribeStream_section.html): Use DescribeStream with an AWS SDK or CLI
- [GetRecords](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_GetRecords_section.html): Use GetRecords with an AWS SDK or CLI
- [GetShardIterator](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_GetShardIterator_section.html): Use GetShardIterator with a CLI
- [ListStreamConsumers](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_ListStreamConsumers_section.html): Use ListStreamConsumers with an AWS SDK
- [ListStreams](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_ListStreams_section.html): Use ListStreams with an AWS SDK or CLI
- [ListTagsForStream](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_ListTagsForStream_section.html): Use ListTagsForStream with an AWS SDK or CLI
- [PutRecord](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_PutRecord_section.html): Use PutRecord with an AWS SDK or CLI
- [PutRecords](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_PutRecords_section.html): Use PutRecords with an AWS SDK or CLI
- [RegisterStreamConsumer](https://docs.aws.amazon.com/streams/latest/dev/example_kinesis_RegisterStreamConsumer_section.html): Use RegisterStreamConsumer with an AWS SDK or CLI

### [Serverless examples](https://docs.aws.amazon.com/streams/latest/dev/service_code_examples_serverless_examples.html)

The following code examples show how to use Kinesis with AWS SDKs.

- [Invoke a Lambda function from a Kinesis trigger](https://docs.aws.amazon.com/streams/latest/dev/example_serverless_Kinesis_Lambda_section.html): Invoke a Lambda function from a Kinesis trigger
- [Reporting batch item failures for Lambda functions with a Kinesis trigger](https://docs.aws.amazon.com/streams/latest/dev/example_serverless_Kinesis_Lambda_batch_item_failures_section.html): Reporting batch item failures for Lambda functions with a Kinesis trigger
