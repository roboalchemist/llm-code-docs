# Source: https://developers.webflow.com/browser/data-exports/destinations/sql-server.mdx

***

title: SQL Server
slug: data-exports/destinations/sql-server
description: Configure SQL Server as a destination for Data Exports
-------------------------------------------------------------------

This guide walks you through configuring SQL Server as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your SQL Server database is protected by security groups or other firewall settings, you will need to use the Webflow static IP address: `34.69.83.207/32` to complete Step 1.
* Confirm that your SQL Server database is configured to allow TCP/IP connections.

## Configuration steps

<Steps>
  ### Allow access

  Create a rule in a security group or firewall settings to allowlist:

  * Incoming connections to your host and port (usually `1433`) from the static IP.
  * Outgoing connections from ports `1024` to `65535` to the static IP.

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  ### Create writer user

  Create a database user to perform the writing of the source data.

  1. Open a connection to your SQL Server database.

  2. Create a user for the data transfer by executing the following SQL command. The `<database>` should be the target destination database.

     ```sql
     USE <database>;
     CREATE LOGIN <username> WITH PASSWORD = '<password>';
     CREATE USER <username> FOR LOGIN <username>;
     ```

  3. Grant user `CREATE TABLE` privileges on the database.

     ```sql
     GRANT CREATE TABLE TO <username>;
     ```

     <Warning>
       **Understanding the CREATE TABLE permission in SQL Server**

       The `CREATE TABLE` permission is a database level permission that allows for the creation of new tables in a given database. The user must also have the `ALTER` permission granted on a given schema in order to create new tables in that schema (see the next step for details).
     </Warning>

  4. Grant user `CREATE SCHEMA` privileges on the database *if the schema does not exist*.

     ```sql
     GRANT CREATE SCHEMA TO <username>;
     ```

     <Warning>
       **If the SCHEMA already exists**

       By default, the service creates a new schema based on the destination configuration. If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema, using:

       ```sql
       GRANT SELECT, INSERT, UPDATE, DELETE, ALTER ON SCHEMA :: <schema> TO <username>;
       ```

       If the `SCHEMA` already exists, the user does not need the `GRANT CREATE SCHEMA` permission.
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, **port**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269131104275)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271353703955)

  <Warning>
    **Credential character limitations**

    For user credentials containing special characters, please avoid using the following characters: `@`, `[`, `]`, `/`, `?`, `#`, `"`, `\\`, `+`, space, `&`, `:` as these characters can break connection string parsing.
  </Warning>
</Steps>

## Permissions checklist

* Network:
  * Inbound rule allows TCP `1433` from the static egress IP
  * Outbound rule allows ephemeral ports `1024-65535` to the static egress IP
* SQL Server:
  * `CREATE TABLE` on the target database
  * If schema is created by the service: `CREATE SCHEMA` on the database
  * If schema is pre-created: `SELECT, INSERT, UPDATE, DELETE, ALTER` on the target schema
  * TCP/IP connections are enabled
* Optional:
  * If connecting over a private network, SSH tunnel can be used (ensure tunnel host access and public key exchange, if applicable)

## FAQ

<Accordion title="How is the SQL Server connection secured?">
  The connection uses a dedicated, least-privileged SQL login scoped to the destination database and schema. Network access can be restricted to the static egress IP and SSH tunneling is optionally supported.
</Accordion>

<Accordion title="Which special characters should I avoid in credentials?">
  Avoid these characters in usernames and passwords because they can break connection string parsing: `@`, `[`, `]`, `/`, `?`, `#`, `"`, `\\`, `+`, space, `&`, `:`.
</Accordion>

<Accordion title="Which SQL Server flavors are supported?">
  Generic on-premises SQL Server, Azure SQL Database, and Azure Synapse are supported. For Azure dedicated SQL pools, we recommend using the [Azure Blob Storage](/browser/data-exports/destinations/azure-blob-storage) destination type and loading from Azure Data Lake Storage Gen2.
</Accordion>
