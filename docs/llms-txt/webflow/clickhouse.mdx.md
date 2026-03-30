# Source: https://developers.webflow.com/browser/data-exports/destinations/clickhouse.mdx

***

title: ClickHouse
slug: data-exports/destinations/clickhouse
description: Configure ClickHouse as a destination for Data Exports
-------------------------------------------------------------------

This guide walks you through configuring ClickHouse as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your ClickHouse security posture requires IP allowlisting, have the Webflow static IP: `34.69.83.207/32` available during the following steps. It will be required in Step 1.

## Configuration steps

<Steps>
  ### Allow access

  <Warning>
    **SSH Tunneling Not Supported**

    SSH Tunneling is currently unsupported for Clickhouse destinations. Please ensure your Clickhouse destination is accessible over the public internet.
  </Warning>

  Create a rule in a security group or firewall settings to allowlist:

  1. Incoming connections to your host and port (usually `9440`) from the static IP.
  2. Outgoing connections from ports `1024` to `65535` to the static IP.

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  ### Create writer user

  Create a database user to perform the writing of the data.

  1. Open a connection to your ClickHouse database.

  2. Create a user for the data transfer by executing the following SQL command.

     ```sql
     CREATE USER <username>@'%' IDENTIFIED BY '<some-password>';
     ```

     <Info>
       **Password Rules**

       Passwords may only include alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (\_).
     </Info>

  3. Grant user required privileges on the database.

     ```sql
     GRANT SELECT ON information_schema.columns TO <username>;
     GRANT CREATE, INSERT, DROP, ALTER, OPTIMIZE, SHOW, TRUNCATE ON <database>.* TO <username>@'%';
     grant CREATE TEMPORARY TABLE, S3 on *.* to <username>@'%';
     ```

     <Note>
       **Understanding the `CREATE TEMPORARY TABLE, S3` permissions**

       The `CREATE TEMPORARY TABLE` and `S3` permissions are required to efficiently transfer data to ClickHouse. Under the hood, these permissions are used to stage data in object storage as compressed files, COPY INTO temporary tables, and finally merge into the target tables. By definition, the temporary table will not exist outside of the session.
     </Note>

  ### Set up staging bucket

  ClickHouse destinations require a staging bucket to efficiently transfer data. Configure your staging bucket using one of the following types of ClickHouse supported object storage:

  * S3
  * GCS
  * Implicit

  <Note>
    **Using the `implicit` bucket option**

    ClickHouse supports the ability to configure staging resources with [environment credentials](https://clickhouse.com/docs/en/integrations/s3#managing-credentials). If this setting is enabled on your ClickHouse cluster, you may choose to use the configured implicit staging resources using the `implicit` option for the staging bucket selection.
  </Note>

  ### Add your destination

  <Info>
    **Connection Protocol**

    Use the ClickHouse TCP native protocol, not HTTPS. This is commonly exposed on port 9000.
  </Info>

  Use the following details to complete the connection setup: **host name**, **port**, **cluster**, **database name**, **schema name**, **username**, **password**, and staging bucket details.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268310282387)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49270940201619)

  <Note>
    **Understanding the `database` vs. `schema` fields (`connection database` vs. `write database`)**

    Depending on the version of your integration, you may be asked for both a `database` and `schema`, or a `connection database` and `write database`.

    * `database` (also referred to as `connection_database`): is the **database** used to establish the connection with ClickHouse.
    * `schema` (also referred to as `write_database`): is the **database/schema** within which data will be written

    These can be (and often are) the same values, but do not need to be.
  </Note>
</Steps>

## Using the ClickHouse data

<Note>
  **Querying ClickHouse data without duplicates**

  The resulting ClickHouse tables use the [ReplacingMergeTree](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replacingmergetree) table engine in order to efficiently upsert changes. To properly query this data, the `FINAL` keyword must be used when selecting from these tables guarantee duplicates are removed. For example:

  ```sql
  SELECT
    *
  FROM
    schema.table FINAL
  WHERE
    foo = bar
  ORDER BY foo
  LIMIT 10;
  ```
</Note>
