# Source: https://clickhouse.ferndocs.com/integrations/bladepipe.md

---
sidebar_label: BladePipe
sidebar_position: 20
keywords:

- clickhouse
- BladePipe
- connect
- integrate
- cdc
- etl
- data integration
slug: /integrations/bladepipe
description: Stream data into ClickHouse using BladePipe data pipelines
title: Connect BladePipe to ClickHouse
doc_type: guide

---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

<a href="https://www.bladepipe.com/" target="_blank">BladePipe</a> is a real-time end-to-end data integration tool with sub-second latency, boosting seamless data flow across platforms.

ClickHouse is one of BladePipe's pre-built connectors, allowing users to integrate data from various sources into ClickHouse automatically. This page will show how to load data into ClickHouse in real time step by step.

## Supported sources [#supported-sources]

Currently BladePipe supports for data integration to ClickHouse from the following sources:

- MySQL/MariaDB/AuroraMySQL
- Oracle
- PostgreSQL/AuroraPostgreSQL
- MongoDB
- Kafka
- PolarDB-MySQL
- OceanBase
- TiDB

More sources are to be supported.

<Steps headerLevel="h2">
## Download and run BladePipe [#1-run-bladepipe]
1. Log in to <a href="https://www.bladepipe.com/" target="_blank">BladePipe Cloud</a>.

1. Follow the instructions in <a href="https://doc.bladepipe.com/productOP/byoc/installation/install_worker_docker" target="_blank">Install Worker (Docker)</a> or <a href="https://doc.bladepipe.com/productOP/byoc/installation/install_worker_binary" target="_blank">Install Worker (Binary)</a> to download and install a BladePipe Worker.

  :::note
  Alternatively, you can download and deploy <a href="https://doc.bladepipe.com/productOP/onPremise/installation/install_all_in_one_binary" target="_blank">BladePipe Enterprise</a>.
  :::

## Add ClickHouse as a target [#2-add-clickhouse-as-a-target]

  :::note

  1. BladePipe supports ClickHouse version `20.12.3.3` or above.
  2. To use ClickHouse as a target, make sure that the user has SELECT, INSERT and common DDL permissions.

  :::

1. In BladePipe, click "DataSource" > "Add DataSource".

2. Select `ClickHouse`, and fill out the settings by providing your ClickHouse host and port, username and password, and click "Test Connection".

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4266eda0e1ce548cacf55cef97086a45887c4997d2615f4c65be886c5dc891a8/images/integrations/data-ingestion/etl-tools/bp_ck_1.png" alt="Add ClickHouse as a target"/>

3. Click "Add DataSource" at the bottom, and a ClickHouse instance is added.

## Add MySQL as a source [#3-add-mysql-as-a-source]

In this tutorial, we use a MySQL instance as the source, and explain the process of loading MySQL data to ClickHouse.

<Note>
To use MySQL as a source, make sure that the user has the <a href="https://doc.bladepipe.com/dataMigrationAndSync/datasource_func/MySQL/privs_for_mysql" target="_blank">required permissions</a>.
</Note>

1. In BladePipe, click "DataSource" > "Add DataSource".

2. Select `MySQL`, and fill out the settings by providing your MySQL host and port, username and password, and click "Test Connection".

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d5bb08f6c4859a4992c362c970b2640f40b90071d9f6c7fbdec5f595e7cb8175/images/integrations/data-ingestion/etl-tools/bp_ck_2.png" alt="Add MySQL as a source"/>

3. Click "Add DataSource" at the bottom, and a MySQL instance is added.

## Create a pipeline [#4-create-a-pipeline]

1. In BladePipe, click "DataJob" > "Create DataJob".

2. Select the added MySQL and ClickHouse instances and click "Test Connection" to ensure BladePipe is connected to the instances. Then, select the databases to be moved.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8c97ed5d8e4506dc98975fb456b165454cc4bf594b8ec41db4ebff345aeb7de6/images/integrations/data-ingestion/etl-tools/bp_ck_3.png" alt="Select source and target"/>

3. Select "Incremental" for DataJob Type, together with the "Full Data" option.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8f63c05e027c5b937ff550b65d789d4e7af4946ff3d078f9c1e86e072b282732/images/integrations/data-ingestion/etl-tools/bp_ck_4.png" alt="Select sync type"/>

4. Select the tables to be replicated.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/414c746f9d5cabc159c4e0e2f3b4809c2c23584cfbbeb1058a013687e30d0911/images/integrations/data-ingestion/etl-tools/bp_ck_5.png" alt="Select tables"/>

5. Select the columns to be replicated.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f9fd9e70341b094928ec9ce1e51670a6c8f9811a29da4512c0f261d07b7fe9d8/images/integrations/data-ingestion/etl-tools/bp_ck_6.png" alt="Select columns"/>

6. Confirm the DataJob creation, and the DataJob runs automatically.
    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6d3b19bc648449e427b20427255ecd60bc0e8bb980e5a7fa4f77d8c567c21482/images/integrations/data-ingestion/etl-tools/bp_ck_8.png" alt="DataJob is running"/>

## Verify the data [#5-verify-the-data]

1. Stop data write in MySQL instance and wait for ClickHouse to merge data.
<Note>

Due to the unpredictable timing of ClickHouse's automatic merging, you can manually trigger a merging by running the `OPTIMIZE TABLE xxx FINAL;` command. Note that there is a chance that this manual merging may not always succeed.

Alternatively, you can run the `CREATE VIEW xxx_v AS SELECT * FROM xxx FINAL;` command to create a view and perform queries on the view to ensure the data is fully merged.
</Note>

1. Create a <a href="https://doc.bladepipe.com/operation/job_manage/create_job/create_period_verification_correction_job" target="_blank">Verification DataJob</a>. Once the Verification DataJob is completed, review the results to confirm that the data in ClickHouse is the same as the data in MySQL.
   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/06e877e698fab4ace2250ce492c20b83b8738af3362661c1be7f4a39ff0c69dd/images/integrations/data-ingestion/etl-tools/bp_ck_9.png" alt="Verify data"/>

</Steps>
