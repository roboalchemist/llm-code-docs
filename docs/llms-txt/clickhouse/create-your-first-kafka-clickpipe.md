# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/kafka/create-your-first-kafka-clickpipe.md

---
sidebar_label: Create your first Kafka ClickPipe
description: Step-by-step guide to creating your first Kafka ClickPipe.
slug: /integrations/clickpipes/kafka/create-your-first-kafka-clickpipe
sidebar_position: 1
title: Creating your first Kafka ClickPipe
doc_type: guide
keywords:

- create kafka clickpipe
- kafka
- clickpipes
- data sources
- setup guide

---

> In this guide, we will walk you through the process of creating your first Kafka ClickPipe.

<Steps type="numbered" headerLevel="h2">

## Navigate to data sources [#1-load-sql-console]

Select the `Data Sources` button on the left-side menu and click on "Set up a ClickPipe".
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/396d6745ffdbacf76e5c2e6e29caa3c102c2de5d5417b4605775815ce688ed9e/images/integrations/data-ingestion/clickpipes/cp_step0.png" alt="Select imports"/>

## Select a data source [#2-select-data-source]

Select your Kafka data source from the list.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2b03c0671bb4184a7e8f41da5fdd1a35ef50b7dde31cdef717fb20a0f803e727/images/integrations/data-ingestion/clickpipes/cp_step1.png" alt="Select data source type"/>

## Configure the data source [#3-configure-data-source]

Fill out the form by providing your ClickPipe with a name, a description (optional), your credentials, and other connection details.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9797306b3b5b03d3cc955b013ebcf6c621765e71dff02e4aadcb88716265841f/images/integrations/data-ingestion/clickpipes/cp_step2.png" alt="Fill out connection details"/>

## Configure a schema registry (optional) [#4-configure-your-schema-registry]

A valid schema is required for Avro streams. See [Schema registries](/click-pipes/integrations/clickpipes/kafka/schema-registries) for more details on how to configure a schema registry.

## Configure a reverse private endpoint (optional) [#5-configure-reverse-private-endpoint]

Configure a Reverse Private Endpoint to allow ClickPipes to connect to your Kafka cluster using AWS PrivateLink.
See our [AWS PrivateLink documentation](../aws-privatelink.md) for more information.

## Select your topic [#6-select-your-topic]

Select your topic and the UI will display a sample document from the topic.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/df161242166964332ed08097c27189387af26b61c2c2595bc5c6fb79917f60e3/images/integrations/data-ingestion/clickpipes/cp_step3.png" alt="Set your topic"/>

## Configure your destination table [#7-configure-your-destination-table]

In the next step, you can select whether you want to ingest data into a new ClickHouse table or reuse an existing one. Follow the instructions in the screen to modify your table name, schema, and settings. You can see a real-time preview of your changes in the sample table at the top.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bec7419d184713c8be882f68800db570c9f63cce9718c45d5160bddbb87e8ca7/images/integrations/data-ingestion/clickpipes/cp_step4a.png" alt="Set table, schema, and settings"/>

You can also customize the advanced settings using the controls provided

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/481b35275ab057fbf55982892f628e080cd7eaa051d74bbcd75d48b54be95ba4/images/integrations/data-ingestion/clickpipes/cp_table_settings.png" alt="Set advanced controls"/>

## Configure permissions [#8-configure-permissions]

ClickPipes will create a dedicated user for writing data into a destination table. You can select a role for this internal user using a custom role or one of the predefined role:

- `Full access`: with the full access to the cluster. It might be useful if you use Materialized View or Dictionary with the destination table.
- `Only destination table`: with the `INSERT` permissions to the destination table only.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/50ced45fd9a746cda9f39522b4b846971c660e76ba409a8794b7d72ff8c7e121/images/integrations/data-ingestion/clickpipes/cp_step5.png" alt="Permissions"/>

## Complete setup [#9-complete-setup]

Clicking on "Create ClickPipe" will create and run your ClickPipe. It will now be listed in the Data Sources section.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7ac0fcc0ff09376ea04b117dbc3c916dd39781c58b4c3a9384f3fbf9f2a2d186/images/integrations/data-ingestion/clickpipes/cp_overview.png" alt="View overview"/>

</Steps>
