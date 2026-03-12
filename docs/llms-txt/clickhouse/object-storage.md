# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/object-storage.md

---
sidebar_label: Create your first object storage ClickPipe
description: Seamlessly connect your object storage to ClickHouse Cloud.
slug: /integrations/clickpipes/object-storage
title: Creating your first object storage ClickPipe
doc_type: guide
integration:

- support_level: core
- category: clickpipes

---

Object Storage ClickPipes provide a simple and resilient way to ingest data from Amazon S3, Google Cloud Storage, Azure Blob Storage, and DigitalOcean Spaces into ClickHouse Cloud. Both one-time and continuous ingestion are supported with exactly-once semantics.

## Prerequisite [#prerequisite]

- You have familiarized yourself with the [ClickPipes intro](../index.md).

## Navigate to data sources [#1-load-sql-console]

In the cloud console, select the `Data Sources` button on the left-side menu and click on "Set up a ClickPipe"

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/396d6745ffdbacf76e5c2e6e29caa3c102c2de5d5417b4605775815ce688ed9e/images/integrations/data-ingestion/clickpipes/cp_step0.png" alt="Select imports"/>

## Select a data source [#2-select-data-source]

Select your data source.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2b03c0671bb4184a7e8f41da5fdd1a35ef50b7dde31cdef717fb20a0f803e727/images/integrations/data-ingestion/clickpipes/cp_step1.png" alt="Select data source type"/>

## Configure the ClickPipe [#3-configure-clickpipe]

Fill out the form by providing your ClickPipe with a name, a description (optional), your IAM role or credentials, and bucket URL.
You can specify multiple files using bash-like wildcards.
For more information, [see the documentation on using wildcards in path](/integrations/clickpipes/object-storage/reference/#limitations).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b6fe4ae1a8157bc8d99c7fa6b2af406b9c29f8a52633e86a403efa4fc67a25a9/images/integrations/data-ingestion/clickpipes/cp_step2_object_storage.png" alt="Fill out connection details"/>

## Select data format [#4-select-format]

The UI will display a list of files in the specified bucket.
Select your data format (we currently support a subset of ClickHouse formats) and if you want to enable continuous ingestion.
([More details below](/integrations/clickpipes/object-storage/reference/#continuous-ingest)).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6d26a7f37d8bd85270264448a81ad758061fb81da3a3027c30efd32bd4e9e068/images/integrations/data-ingestion/clickpipes/cp_step3_object_storage.png" alt="Set data format and topic"/>

## Configure table, schema and settings [#5-configure-table-schema-settings]

In the next step, you can select whether you want to ingest data into a new ClickHouse table or reuse an existing one.
Follow the instructions in the screen to modify your table name, schema, and settings.
You can see a real-time preview of your changes in the sample table at the top.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bec7419d184713c8be882f68800db570c9f63cce9718c45d5160bddbb87e8ca7/images/integrations/data-ingestion/clickpipes/cp_step4a.png" alt="Set table, schema, and settings"/>

You can also customize the advanced settings using the controls provided

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/481b35275ab057fbf55982892f628e080cd7eaa051d74bbcd75d48b54be95ba4/images/integrations/data-ingestion/clickpipes/cp_step4a3.png" alt="Set advanced controls"/>

Alternatively, you can decide to ingest your data in an existing ClickHouse table.
In that case, the UI will allow you to map fields from the source to the ClickHouse fields in the selected destination table.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1ac34b98d68061c6fdc4a4a1c8487e8fe560a7f89dfd53a68b4c557426bb4528/images/integrations/data-ingestion/clickpipes/cp_step4b.png" alt="Use an existing table"/>

<Note>
You can also map [virtual columns](../../sql-reference/table-functions/s3#virtual-columns), like `_path` or `_size`, to fields.
</Note>

## Configure permissions [#6-configure-permissions]

Finally, you can configure permissions for the internal ClickPipes user.

**Permissions:** ClickPipes will create a dedicated user for writing data into a destination table. You can select a role for this internal user using a custom role or one of the predefined role:

- `Full access`: with the full access to the cluster. Required if you use materialized view or Dictionary with the destination table.
- `Only destination table`: with the `INSERT` permissions to the destination table only.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/50ced45fd9a746cda9f39522b4b846971c660e76ba409a8794b7d72ff8c7e121/images/integrations/data-ingestion/clickpipes/cp_step5.png" alt="Permissions"/>

## Complete setup [#7-complete-setup]

By clicking on "Complete Setup", the system will register your ClickPipe, and you'll be able to see it listed in the summary table.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/179951fd476a3f3199dfaf115f54b353adfe9cc3e231132da72d1af372a92099/images/integrations/data-ingestion/clickpipes/cp_success.png" alt="Success notice"/>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4f5abe399b7e5e849b8851d12435c18dd5cb31489ee568292019bf4f30c5bde4/images/integrations/data-ingestion/clickpipes/cp_remove.png" alt="Remove notice"/>

The summary table provides controls to display sample data from the source or the destination table in ClickHouse

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e30e2b0eaf1b4b8bd3b3b4a4a4f705c8163eba07f6c29d8d1728a2169bdcc478/images/integrations/data-ingestion/clickpipes/cp_destination.png" alt="View destination"/>

As well as controls to remove the ClickPipe and display a summary of the ingest job.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7ac0fcc0ff09376ea04b117dbc3c916dd39781c58b4c3a9384f3fbf9f2a2d186/images/integrations/data-ingestion/clickpipes/cp_overview.png" alt="View overview"/>

**Congratulations!** you have successfully set up your first ClickPipe.
If this is a streaming ClickPipe, it will be continuously running, ingesting data in real-time from your remote data source.
Otherwise, it will ingest the batch and complete.
