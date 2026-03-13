# Source: https://clickhouse.ferndocs.com/integrations/nifi.md

---
sidebar_label: NiFi
sidebar_position: 12
keywords:
  - clickhouse
  - NiFi
  - connect
  - integrate
  - etl
  - data integration
slug: /integrations/nifi
description: Stream data into ClickHouse using NiFi data pipelines
title: Connect Apache NiFi to ClickHouse
doc_type: guide
integration:
  - support_level: community
  - category: data_ingestion
---

import {CommunityMaintainedBadge} from '../../../../../components/Badges/CommunityMaintained'

<CommunityMaintainedBadge/>

<a href="https://nifi.apache.org/" target="_blank">Apache NiFi</a> is an open-source workflow management software designed to automate data flow between software systems. It allows the creation of ETL data pipelines and is shipped with more than 300 data processors. This step-by-step tutorial shows how to connect Apache NiFi to ClickHouse as both a source and destination, and to load a sample dataset.

<Steps>

## Gather your connection details [#1-gather-your-connection-details]

To connect to ClickHouse with HTTP(S) you need this information:

| Parameter(s)            | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
|`HOST` and `PORT`        | Typically, the port is 8443 when using TLS or 8123 when not using TLS.                                        |
|`DATABASE NAME`          | Out of the box, there is a database named `default`, use the name of the database that you want to connect to.|
|`USERNAME` and `PASSWORD`| Out of the box, the username is `default`. Use the username appropriate for your use case.                    |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select a service and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button" />

Choose **HTTPS**. Connection details are displayed in an example `curl` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/710d528cac4deb00e877550b033fe8d67e19e1a8f825c75889eb0573ab25f7b0/images/_snippets/connection-details-https.png" alt="ClickHouse Cloud HTTPS connection details" />

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


## Download and run Apache NiFi [#2-download-and-run-apache-nifi]

For a new setup, download the binary from https://nifi.apache.org/download.html and start by running `./bin/nifi.sh start`

## Download the ClickHouse JDBC driver [#3-download-the-clickhouse-jdbc-driver]

1. Visit the <a href="https://github.com/ClickHouse/clickhouse-java/releases" target="_blank">ClickHouse JDBC driver release page</a> on GitHub and look for  the latest JDBC release version
2. In the release version, click on "Show all xx assets" and look for the JAR file containing the keyword "shaded" or "all", for example, `clickhouse-jdbc-0.5.0-all.jar`
3. Place the JAR file in a folder accessible by Apache NiFi and take note of the absolute path

## Add `DBCPConnectionPool` Controller Service and configure its properties [#4-add-dbcpconnectionpool-controller-service-and-configure-its-properties]

1. To configure a Controller Service in Apache NiFi, visit the NiFi Flow Configuration page by clicking on the "gear" button

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/14598641d2bf84f58f238ece0a1938687e60bd395339db9fb9a39048dd08150b/images/integrations/data-ingestion/etl-tools/nifi_01.png" alt="NiFi Flow Configuration page with gear button highlighted"/>

2. Select the Controller Services tab and add a new Controller Service by clicking on the `+` button at the top right

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/65baed5b0b76acc061bd264bf950fe7018f67df9085a3cae9be0c54414ccdc5d/images/integrations/data-ingestion/etl-tools/nifi_02.png" alt="Controller Services tab with add button highlighted"/>

3. Search for `DBCPConnectionPool` and click on the "Add" button

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e524308e6fcc448ff8942c55e54ee00aba84e28ace4377efc3e8a33d74abf342/images/integrations/data-ingestion/etl-tools/nifi_03.png" alt="Controller Service selection dialog with DBCPConnectionPool highlighted"/>

4. The newly added `DBCPConnectionPool` will be in an Invalid state by default. Click on the "gear" button to start configuring

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ddc1411c8b5215712ab4c01ab5c191d30eafd9c081b877fd780905aff1876919/images/integrations/data-ingestion/etl-tools/nifi_04.png" alt="Controller Services list showing invalid DBCPConnectionPool with gear button highlighted"/>

5. Under the "Properties" section, input the following values

  | Property                    | Value                                                              | Remark                                                                        |
  | --------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
  | Database Connection URL     | jdbc:ch:https://HOSTNAME:8443/default?ssl=true                     | Replace HOSTNAME in the connection URL accordingly                            |
  | Database Driver Class Name  | com.clickhouse.jdbc.ClickHouseDriver                               ||
  | Database Driver Location(s) | /etc/nifi/nifi-X.XX.X/lib/clickhouse-jdbc-0.X.X-patchXX-shaded.jar | Absolute path to the ClickHouse JDBC driver JAR file                          |
  | Database User               | default                                                            | ClickHouse username                                                           |
  | Password                    | password                                                 | ClickHouse password                                                           |

6. In the Settings section, change the name of the Controller Service to "ClickHouse JDBC" for easy reference

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/98e1989214431e0d43cc998160b8068c8af4bd4e7babe9da557eccff87ad86c8/images/integrations/data-ingestion/etl-tools/nifi_05.png" alt="DBCPConnectionPool configuration dialog showing properties filled in"/>

7. Activate the `DBCPConnectionPool` Controller Service by clicking on the "lightning" button and then the "Enable" button

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/95b373931deb5223f6e15f8c67fc9dfb26f931702050ec0eeb3a055aec3fb19d/images/integrations/data-ingestion/etl-tools/nifi_06.png" alt="Controller Services list with lightning button highlighted"/>

    <br/>

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/952f4e2985db360ca652828ecce5647a6b890d333df7be78e25fba0f6e1551f5/images/integrations/data-ingestion/etl-tools/nifi_07.png" alt="Enable Controller Service confirmation dialog"/>

8. Check the Controller Services tab and ensure that the Controller Service is enabled

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/65baed5b0b76acc061bd264bf950fe7018f67df9085a3cae9be0c54414ccdc5d/images/integrations/data-ingestion/etl-tools/nifi_08.png" alt="Controller Services list showing enabled ClickHouse JDBC service"/>

## Read from a table using the `ExecuteSQL` processor [#5-read-from-a-table-using-the-executesql-processor]

1. Add an ​`​ExecuteSQL` processor, along with the appropriate upstream and downstream processors

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9cc048272d6293b1437f1276a190372a281cd9f15c19b11b75a2d8e9fa83a6f7/images/integrations/data-ingestion/etl-tools/nifi_09.png" alt="NiFi canvas showing ExecuteSQL processor in a workflow"/>

2. Under the "Properties" section of the ​`​ExecuteSQL` processor, input the following values

    | Property                            | Value                                | Remark                                                  |
    |-------------------------------------|--------------------------------------|---------------------------------------------------------|
    | Database Connection Pooling Service | ClickHouse JDBC                      | Select the Controller Service configured for ClickHouse |
    | SQL select query                    | SELECT * FROM system.metrics         | Input your query here                                   |

3. Start the `​​ExecuteSQL` processor

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6a6702d0cc25aea1ffd688c8b94395188120efee23934ee96f976d4db5c4ec43/images/integrations/data-ingestion/etl-tools/nifi_10.png" alt="ExecuteSQL processor configuration with properties filled in"/>

4. To confirm that the query has been processed successfully, inspect one of the `FlowFile` in the output queue

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/53c2517214efb533fbd2aefdb0872f99c128687b360fe3be70d01681b30e9fd8/images/integrations/data-ingestion/etl-tools/nifi_11.png" alt="List queue dialog showing flowfiles ready for inspection"/>

5. Switch view to "formatted" to view the result of the output `FlowFile`

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7d2db5d8013acba6db68a3d4905af50345fff79d1da27c573ed7f8984ea9b62b/images/integrations/data-ingestion/etl-tools/nifi_12.png" alt="FlowFile content viewer showing query results in formatted view"/>

## Write to a table using `MergeRecord` and `PutDatabaseRecord` processor [#6-write-to-a-table-using-mergerecord-and-putdatabaserecord-processor]

1. To write multiple rows in a single insert, we first need to merge multiple records into a single record. This can be done using the `MergeRecord` processor

2. Under the "Properties" section of the `MergeRecord` processor, input the following values

    | Property                  | Value             | Remark                                                                                                                          |
    |---------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------|
    | Record Reader             | `JSONTreeReader`    | Select the appropriate record reader                                                                                            |
    | Record Writer             | `JSONReadSetWriter` | Select the appropriate record writer                                                                                            |
    | Minimum Number of Records | 1000              | Change this to a higher number so that the minimum number of rows are merged to form a single record. Default to 1 row |
    | Maximum Number of Records | 10000             | Change this to a higher number than "Minimum Number of Records". Default to 1,000 rows                                         |

3. To confirm that multiple records are merged into one, examine the input and output of the `MergeRecord` processor. Note that the output is an array of multiple input records

    Input
    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/152f457aac5712a1a9cad85d758d976c274434c2d2d7f1980542672fa73fc718/images/integrations/data-ingestion/etl-tools/nifi_13.png" alt="MergeRecord processor input showing single records"/>

    Output
    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b199305c701640ddd7f1335e64801b7bd56154e5170e6fdbdc444cf01d4f63dd/images/integrations/data-ingestion/etl-tools/nifi_14.png" alt="MergeRecord processor output showing merged array of records"/>

4. Under the "Properties" section of the `PutDatabaseRecord` processor, input the following values

    | Property                            | Value           | Remark                                                                                                                                   |
    | ----------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
    | Record Reader                       | `JSONTreeReader`  | Select the appropriate record reader                                                                                                     |
    | Database Type                       | Generic         | Leave as default                                                                                                                         |
    | Statement Type                      | INSERT          |                                                                                                                                          |
    | Database Connection Pooling Service | ClickHouse JDBC | Select the ClickHouse controller service                                                                                                 |
    | Table Name                          | tbl             | Input your table name here                                                                                                               |
    | Translate Field Names               | false           | Set to "false" so that field names inserted must match the column name                                                                                      |
    | Maximum Batch Size                  | 1000            | Maximum number of rows per insert. This value should not be lower than the value of "Minimum Number of Records" in `MergeRecord` processor |

4. To confirm that each insert contains multiple rows, check that the row count in the table is incrementing by at least the value of "Minimum Number of Records" defined in `MergeRecord`.

    <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/be1b8d40f0bd70e71159735268b69a2a15051ea726f93965b97a8e40433a8d0d/images/integrations/data-ingestion/etl-tools/nifi_15.png" alt="Query results showing row count in the destination table"/>

5. Congratulations - you have successfully loaded your data into ClickHouse using Apache NiFi !

</Steps>
