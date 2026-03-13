# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/mysql/source/rds_maria.md

---
sidebar_label: Amazon RDS MariaDB
description: >-
  Step-by-step guide on how to set up Amazon RDS MariaDB as a source for
  ClickPipes
slug: /integrations/clickpipes/mysql/source/rds_maria
title: RDS MariaDB source setup guide
doc_type: guide
keywords:
  - clickpipes
  - mysql
  - cdc
  - data ingestion
  - real-time sync
---


This is a step-by-step guide on how to configure your RDS MariaDB instance for replicating its data via the MySQL ClickPipe.
<br/>
<Note>
We also recommend going through the MySQL FAQs [here](/integrations/data-ingestion/clickpipes/mysql/faq.md). The FAQs page is being actively updated.
</Note>

## Enable binary log retention [#enable-binlog-retention-rds]
The binary log is a set of log files that contain information about data modifications made to a MySQL server instance. Binary log files are required for replication. Both of the steps below must be followed:

### 1. Enable binary logging via automated backup[#enable-binlog-logging-rds]

The automated backups feature determines whether binary logging is turned on or off for MySQL. It can be set in the AWS console:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e1e617e7136840c20b4748dd57468d251fddb1f7ea1da06d0d56923f3e5c4476/images/integrations/data-ingestion/clickpipes/mysql/source/rds/rds-backups.png" alt="Enabling automated backups in RDS"/>

Setting backup retention to a reasonably long value depending on the replication use-case is advisable.

### 2. Binlog retention hours[#binlog-retention-hours-rds]
Amazon RDS for MariaDB has a different method of setting binlog retention duration, which is the amount of time a binlog file containing changes is kept. If some changes are not read before the binlog file is removed, replication will be unable to continue. The default value of binlog retention hours is NULL, which means binary logs aren't retained.

To specify the number of hours to retain binary logs on a DB instance, use the mysql.rds_set_configuration function with a binlog retention period long enough for replication to occur. `24 hours` is the recommended minimum.

```text
mysql=> call mysql.rds_set_configuration('binlog retention hours', 24);
```

## Configure binlog settings in the parameter group [#binlog-parameter-group-rds]

The parameter group can be found when you click on your MariaDB instance in the RDS Console, and then navigate to the `Configurations` tab.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6a66afc63fe9a93296eb2aebf80eb2a3c234820b1150212f6355312a1137a481/images/integrations/data-ingestion/clickpipes/mysql/parameter_group/rds_config.png" alt="Where to find parameter group in RDS"/>

Upon clicking on the parameter group link, you will be taken to the parameter group link page. You will see an Edit button in the top-right:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7b27bcd7c93115bb639ef74ced0a886ca7b8ae152b50c11664fb51ba83045bf5/images/integrations/data-ingestion/clickpipes/mysql/parameter_group/edit_button.png" alt="Edit parameter group"/>

Settings `binlog_format`, `binlog_row_metadata` and `binlog_row_image` need to be set as follows:

1. `binlog_format` to `ROW`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/89e013c92b924923cc5e210bdc61bc06466ccd3b977a78cc4b4eaccea1af0e0a/images/integrations/data-ingestion/clickpipes/mysql/parameter_group/binlog_format.png" alt="Binlog format to ROW"/>

2. `binlog_row_metadata` to `FULL`

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4ac831a921eab795ee58e37748615f912fa37264064aeca4f69f4cd272af4e65/images/integrations/data-ingestion/clickpipes/mysql/parameter_group/binlog_row_metadata.png" alt="Binlog row metadata to FULL"/>

3. `binlog_row_image` to `FULL`

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6f8551bda9cfb659887f203075229949de8b7cc42bd60cd178ec5a684ba0e5d5/images/integrations/data-ingestion/clickpipes/mysql/parameter_group/binlog_row_image.png" alt="Binlog row image to FULL"/>

Next, click on `Save Changes` in the top-right. You may need to reboot your instance for the changes to take effect. If you see `Pending reboot` next to the parameter group link in the Configurations tab of the RDS instance, this is a good indication that a reboot of your instance is needed.

<br/>
<Tip>
If you have a MariaDB cluster, the above parameters would be found in a [DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html) parameter group and not the DB instance group.
</Tip>

## Enabling GTID Mode [#gtid-mode-rds]
Global Transaction Identifiers (GTIDs) are unique IDs assigned to each committed transaction in MySQL/MariaDB. They simplify binlog replication and make troubleshooting more straightforward. MariaDB enables GTID mode by default, so no user action is needed to use it.

## Configure a database user [#configure-database-user-rds]

Connect to your RDS MariaDB instance as an admin user and execute the following commands:

1. Create a dedicated user for ClickPipes:

    ```sql
    CREATE USER 'clickpipes_user'@'host' IDENTIFIED BY 'some-password';
    ```

2. Grant schema permissions. The following example shows permissions for the `mysql` database. Repeat these commands for each database and host that you want to replicate:

    ```sql
    GRANT SELECT ON `mysql`.* TO 'clickpipes_user'@'host';
    ```

3. Grant replication permissions to the user:

    ```sql
    GRANT REPLICATION CLIENT ON *.* TO 'clickpipes_user'@'%';
    GRANT REPLICATION SLAVE ON *.* TO 'clickpipes_user'@'%';

## Configure network access [#configure-network-access]

### IP-based access control [#ip-based-access-control]

If you want to restrict traffic to your RDS instance, please add the [documented static NAT IPs](../../index.md#list-of-static-ips) to the `Inbound rules` of your RDS security group.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5b6e81216bfdb806f569b2b75833960732ea4cd9e267f26efcc1890c5cd0f71a/images/integrations/data-ingestion/clickpipes/mysql/source/rds/security-group-in-rds-mysql.png" alt="Where to find security group in RDS?"/>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4df7d459c15b42e15d672955fa550ddfcf6295ff009c8f55cdf30572df37c4f3/images/integrations/data-ingestion/clickpipes/postgres/source/rds/edit_inbound_rules.png" alt="Edit inbound rules for the above security group"/>

### Private access via AWS PrivateLink [#private-access-via-aws-privatelink]

To connect to your RDS instance through a private network, you can use AWS PrivateLink. Follow our [AWS PrivateLink setup guide for ClickPipes](/knowledgebase/aws-privatelink-setup-for-clickpipes) to set up the connection.
