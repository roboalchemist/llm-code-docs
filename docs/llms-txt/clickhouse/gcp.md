# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mysql/source/gcp.md

---
sidebar_label: 'Cloud SQL For MySQL '
description: >-
  Step-by-step guide on how to set up Cloud SQL for MySQL as a source for
  ClickPipes
slug: /integrations/clickpipes/mysql/source/gcp
title: Cloud SQL for MySQL source setup guide
keywords:

- google cloud sql
- mysql
- clickpipes
- pitr
- root ca certificate
doc_type: guide

---

This is a step-by-step guide on how to configure your Cloud SQL for MySQL instance for replicating its data via the MySQL ClickPipe.

## Enable binary log retention [#enable-binlog-retention-gcp]

The binary log is a set of log files that contain information about data modifications made to an MySQL server instance, and binary log files are required for replication.

### Enable binary logging via PITR[#enable-binlog-logging-gcp]

The PITR feature determines whether binary logging is turned on or off for MySQL in Google Cloud. It can be set in the Cloud console, by editing your Cloud SQL instance and scrolling down to the below section.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1d3e6a5feb8774ef046f5c46581330ff2725125f2df9d4122cf128a8f81378d2/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/gcp-mysql-pitr.png" alt="Enabling PITR in Cloud SQL"/>

Setting the value to a reasonably long value depending on the replication use-case is advisable.

If not already configured, make sure to set these in the database flags section by editing the Cloud SQL:

1. `binlog_expire_logs_seconds` to a value >= `86400` (1 day).
2. `binlog_row_metadata` to `FULL`
3. `binlog_row_image` to `FULL`

To do this, click on the `Edit` button in the top right corner of the instance overview page.
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/28667ae885041c916853cfc6f078f1d18773722d3ac6a6a110c74667132bb8e5/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/gcp-mysql-edit-button.png" alt="Edit button in GCP MySQL"/>

Then scroll down to the `Flags` section and add the above flags.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d2a277fdb8c4a0f9ba5b3a4619f7501ec5755242cb5d7e255c504fee680b1885/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/gcp-mysql-flags.png" alt="Setting binlog flags in GCP"/>

## Configure a database user [#configure-database-user-gcp]

Connect to your Cloud SQL MySQL instance as the root user and execute the following commands:

1. Create a dedicated user for ClickPipes:

    ```sql
    CREATE USER 'clickpipes_user'@'host' IDENTIFIED BY 'some-password';
    ```

2. Grant schema permissions. The following example shows permissions for the `clickpipes` database. Repeat these commands for each database and host you want to replicate:

    ```sql
    GRANT SELECT ON `clickpipes`.* TO 'clickpipes_user'@'host';
    ```

3. Grant replication permissions to the user:

    ```sql
    GRANT REPLICATION CLIENT ON *.* TO 'clickpipes_user'@'%';
    GRANT REPLICATION SLAVE ON *.* TO 'clickpipes_user'@'%';
    ```

## Configure network access [#configure-network-access-gcp-mysql]

If you want to restrict traffic to your Cloud SQL instance, please add the [documented static NAT IPs](../../index.md#list-of-static-ips) to the allowlisted IPs of your Cloud SQL MySQL instance.
This can be done either by editing the instance or by heading over to the `Connections` tab in the sidebar in Cloud console.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bc419b8b2e811b8bec807508e8d9642b39d1ca077d0b0cf4b617474677e64d66/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/gcp-mysql-ip.png" alt="IP allowlisting in GCP MySQL"/>

## Download and use root CA certificate [#download-root-ca-certificate-gcp-mysql]

To connect to your Cloud SQL instance, you need to download the root CA certificate.

1. Go to your Cloud SQL instance in the Cloud console.
2. Click on `Connections` in the sidebar.
3. Click on the `Security` tab.
4. In the `Manage server CA certificates` section, click on the `DOWNLOAD CERTIFICATES` button at the bottom.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/713a7004879af41f77cf2fe18a51300152d3a27ecb7f40b7e26ede0073d963a2/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/gcp-mysql-cert.png" alt="Downloading GCP MySQL Cert"/>

1. In the ClickPipes UI, upload the downloaded certificate when creating a new MySQL ClickPipe.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6076b3528f3ac152af811f718093973e5823e0ab3a0ecfc020f7b92e7d40ab9e/images/integrations/data-ingestion/clickpipes/mysql/source/gcp/rootca.png" alt="Using GCP MySQL Cert"/>
