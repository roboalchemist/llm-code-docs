# Source: https://developers.webflow.com/browser/data-exports/destinations/oracle.mdx

***

title: Oracle
slug: data-exports/destinations/oracle
description: Configure Oracle as a destination for Data Exports
---------------------------------------------------------------

This guide walks you through configuring Oracle as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your Oracle database is protected by security groups or other firewall settings, you will need to use the Webflow static IP address: `34.69.83.207/32` to complete Step 1.

## Configuration steps

<Steps>
  ### Allow access

  Create a rule in a security group or firewall settings to allowlist:

  * Incoming connections to your host and port (usually `1521`) from the static IP.
  * Outgoing connections from ports `1024` to `65535` to the static IP.

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  ### Create writer user

  Create a database user to perform the writing of the source data.

  1. Open a connection to your Oracle database.

  2. Create a user for the data transfer by executing the following SQL command.

     ```sql
     CREATE USER <username> IDENTIFIED BY '<some-password>';
     GRANT CREATE SESSION TO <username>;
     ```

  3. Grant user required privileges on the database.

     ```sql
     GRANT CREATE SESSION TO <username>;
     GRANT ALTER USER TO <username>;
     GRANT CREATE ANY TABLE TO <username>;
     GRANT CREATE ANY INDEX TO <username>;
     GRANT SELECT ANY TABLE TO <username>;
     GRANT INSERT ANY TABLE TO <username>;
     GRANT UPDATE ANY TABLE TO <username>;
     GRANT DELETE ANY TABLE TO <username>;
     GRANT DROP ANY TABLE TO <username>;
     GRANT COMMENT ANY TABLE TO <username>;
     ```

     <Warning>
       **If the schema/database already exists**

       By default, the service creates a new schema (in Oracle, `schema` is synonymous with `user`). If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema.
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, **port**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269124391443)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271342929171)
</Steps>
