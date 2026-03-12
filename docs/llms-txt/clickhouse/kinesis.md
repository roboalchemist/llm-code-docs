# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/kinesis.md

---
sidebar_label: ClickPipes for Amazon Kinesis
description: Seamlessly connect your Amazon Kinesis data sources to ClickHouse Cloud.
slug: /integrations/clickpipes/kinesis
title: Integrating Amazon Kinesis with ClickHouse Cloud
doc_type: guide
integration:

- support_level: core
- category: clickpipes
keywords:
- clickpipes
- kinesis
- streaming
- aws
- data ingestion

---

## Prerequisite [#prerequisite]

You have familiarized yourself with the [ClickPipes intro](./index.md) and setup [IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) or an [IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Follow the [Kinesis Role-Based Access guide](/click-pipes/integrations/clickpipes/secure-kinesis) for information on how to setup a role that works with ClickHouse Cloud.

## Creating your first ClickPipe [#creating-your-first-clickpipe]

1. Access the SQL Console for your ClickHouse Cloud Service.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/278d51c8a0c83dbf4892efbd68771a0b8fc4dae70c88f20490cc788cf033c883/images/integrations/data-ingestion/clickpipes/cp_service.png" alt="ClickPipes service"/>

1. Select the `Data Sources` button on the left-side menu and click on "Set up a ClickPipe"

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/396d6745ffdbacf76e5c2e6e29caa3c102c2de5d5417b4605775815ce688ed9e/images/integrations/data-ingestion/clickpipes/cp_step0.png" alt="Select imports"/>

1. Select your data source.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2b03c0671bb4184a7e8f41da5fdd1a35ef50b7dde31cdef717fb20a0f803e727/images/integrations/data-ingestion/clickpipes/cp_step1.png" alt="Select data source type"/>

1. Fill out the form by providing your ClickPipe with a name, a description (optional), your IAM role or credentials, and other connection details.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/50bf360b91e5e8e76073b3f9179c82dcc13fa02ea0e0b609dc790e5258e18189/images/integrations/data-ingestion/clickpipes/cp_step2_kinesis.png" alt="Fill out connection details"/>

1. Select Kinesis Stream and starting offset. The UI will display a sample document from the selected source (Kafka topic, etc). You can also enable Enhanced Fan-out for Kinesis streams to improve the performance and stability of your ClickPipe (More information on Enhanced Fan-out can be found [here](https://aws.amazon.com/blogs/aws/kds-enhanced-fanout))

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f8174b6756ea57429062bcfe101aac2b8523ec8b372a6caf95a28c598481d4ea/images/integrations/data-ingestion/clickpipes/cp_step3_kinesis.png" alt="Set data format and topic"/>

1. In the next step, you can select whether you want to ingest data into a new ClickHouse table or reuse an existing one. Follow the instructions in the screen to modify your table name, schema, and settings. You can see a real-time preview of your changes in the sample table at the top.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bec7419d184713c8be882f68800db570c9f63cce9718c45d5160bddbb87e8ca7/images/integrations/data-ingestion/clickpipes/cp_step4a.png" alt="Set table, schema, and settings"/>

  You can also customize the advanced settings using the controls provided

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/481b35275ab057fbf55982892f628e080cd7eaa051d74bbcd75d48b54be95ba4/images/integrations/data-ingestion/clickpipes/cp_step4a3.png" alt="Set advanced controls"/>

1. Alternatively, you can decide to ingest your data in an existing ClickHouse table. In that case, the UI will allow you to map fields from the source to the ClickHouse fields in the selected destination table.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1ac34b98d68061c6fdc4a4a1c8487e8fe560a7f89dfd53a68b4c557426bb4528/images/integrations/data-ingestion/clickpipes/cp_step4b.png" alt="Use an existing table"/>

1. Finally, you can configure permissions for the internal ClickPipes user.

  **Permissions:** ClickPipes will create a dedicated user for writing data into a destination table. You can select a role for this internal user using a custom role or one of the predefined role:
    - `Full access`: with the full access to the cluster. It might be useful if you use materialized view or Dictionary with the destination table.
    - `Only destination table`: with the `INSERT` permissions to the destination table only.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/50ced45fd9a746cda9f39522b4b846971c660e76ba409a8794b7d72ff8c7e121/images/integrations/data-ingestion/clickpipes/cp_step5.png" alt="Permissions"/>

1. By clicking on "Complete Setup", the system will register you ClickPipe, and you'll be able to see it listed in the summary table.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/179951fd476a3f3199dfaf115f54b353adfe9cc3e231132da72d1af372a92099/images/integrations/data-ingestion/clickpipes/cp_success.png" alt="Success notice"/>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4f5abe399b7e5e849b8851d12435c18dd5cb31489ee568292019bf4f30c5bde4/images/integrations/data-ingestion/clickpipes/cp_remove.png" alt="Remove notice"/>

  The summary table provides controls to display sample data from the source or the destination table in ClickHouse

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e30e2b0eaf1b4b8bd3b3b4a4a4f705c8163eba07f6c29d8d1728a2169bdcc478/images/integrations/data-ingestion/clickpipes/cp_destination.png" alt="View destination"/>

  As well as controls to remove the ClickPipe and display a summary of the ingest job.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7ac0fcc0ff09376ea04b117dbc3c916dd39781c58b4c3a9384f3fbf9f2a2d186/images/integrations/data-ingestion/clickpipes/cp_overview.png" alt="View overview"/>

1. **Congratulations!** you have successfully set up your first ClickPipe. If this is a streaming ClickPipe it will be continuously running, ingesting data in real-time from your remote data source. Otherwise it will ingest the batch and complete.

## Supported data formats [#supported-data-formats]

The supported formats are:

- [JSON](/interfaces/formats/JSON)

## Supported data types [#supported-data-types]

### Standard types support [#standard-types-support]

The following ClickHouse data types are currently supported in ClickPipes:

- Base numeric types - \[U\]Int8/16/32/64, Float32/64, and BFloat16
- Large integer types - \[U\]Int128/256
- Decimal Types
- Boolean
- String
- FixedString
- Date, Date32
- DateTime, DateTime64 (UTC timezones only)
- Enum8/Enum16
- UUID
- IPv4
- IPv6
- all ClickHouse LowCardinality types
- Map with keys and values using any of the above types (including Nullables)
- Tuple and Array with elements using any of the above types (including Nullables, one level depth only)
- SimpleAggregateFunction types (for AggregatingMergeTree or SummingMergeTree destinations)

### Variant type support [#variant-type-support]

You can manually specify a Variant type (such as `Variant(String, Int64, DateTime)`) for any JSON field
in the source data stream.  Because of the way ClickPipes determines the correct variant subtype to use, only one integer or datetime
type can be used in the Variant definition - for example, `Variant(Int64, UInt32)` is not supported.

### JSON type support [#json-type-support]

JSON fields that are always a JSON object can be assigned to a JSON destination column.  You will have to manually change the destination
column to the desired JSON type, including any fixed or skipped paths.

## Kinesis virtual columns [#kinesis-virtual-columns]

The following virtual columns are supported for Kinesis stream.  When creating a new destination table virtual columns can be added by using the `Add Column` button.

| Name             | Description                                                   | Recommended Data Type |
|------------------|---------------------------------------------------------------|-----------------------|
| _key             | Kinesis Partition Key                                         | String                |
| _timestamp       | Kinesis Approximate Arrival Timestamp (millisecond precision) | DateTime64(3)         |
| _stream          | Kinesis Stream Name                                           | String                |
| _sequence_number | Kinesis Sequence Number                                       | String                |
| _raw_message     | Full Kinesis Message                                          | String                |

The _raw_message field can be used in cases where only full Kinesis JSON record is required (such as using ClickHouse [`JsonExtract*`](/sql-reference/functions/json-functions#jsonextract-functions) functions to populate a downstream materialized
view).  For such pipes, it may improve ClickPipes performance to delete all the "non-virtual" columns.

## Limitations [#limitations]

- [DEFAULT](/sql-reference/statements/create/table#default) is not supported.

## Performance [#performance]

### Batching [#batching]

ClickPipes inserts data into ClickHouse in batches. This is to avoid creating too many parts in the database which can lead to performance issues in the cluster.

Batches are inserted when one of the following criteria has been met:

- The batch size has reached the maximum size (100,000 rows or 32MB per 1GB of replica memory)
- The batch has been open for a maximum amount of time (5 seconds)

### Latency [#latency]

Latency (defined as the time between the Kinesis message being sent to the stream and the message being available in ClickHouse) will be dependent on a number of factors (i.e. Kinesis latency, network latency, message size/format). The [batching](#batching) described in the section above will also impact latency. We always recommend testing your specific use case to understand the latency you can expect.

If you have specific low-latency requirements, please [contact us](https://clickhouse.com/company/contact?loc=clickpipes).

### Scaling [#scaling]

ClickPipes for Kinesis is designed to scale both horizontally and vertically. By default, we create a consumer group with one consumer. This can be configured during ClickPipe creation, or at any other point under **Settings** -> **Advanced Settings** -> **Scaling**.

ClickPipes provides high-availability with an availability zone distributed architecture.
This requires scaling to at least two consumers.

Regardless number of running consumers, fault tolerance is available by design.
If a consumer or its underlying infrastructure fails,
the ClickPipe will automatically restart the consumer and continue processing messages.

## Authentication [#authentication]

To access Amazon Kinesis streams, you can use [IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) or an [IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). For more details on how to setup an IAM role, you can [refer to this guide](/click-pipes/integrations/clickpipes/secure-kinesis) for information on how to setup a role that works with ClickHouse Cloud
