# Source: https://developers.webflow.com/browser/data-exports/destinations/postgres.mdx

***

title: PostgreSQL
slug: data-exports/destinations/postgres
description: Configure PostgreSQL as a destination for Data Exports
-------------------------------------------------------------------

This guide walks you through configuring PostgreSQL as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your Postgres database is protected by security groups or other firewall settings, you will need to use the Webflow static IP address: `34.69.83.207/32` to complete Step 1.

## Configuration steps

<Steps>
  ### Allow access

  Create a rule in a security group or firewall settings to allowlist:

  * Incoming connections to your host and port (usually `5432`) from the static IP.
  * Outgoing connections from ports `1024` to `65535` to the static IP.

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  ### Create writer user

  Create a database user to perform the writing of the source data.

  1. Open a connection to your PostgreSQL database.

  2. Create a user for the data transfer by executing the following SQL command.

     ```sql
     CREATE USER <username> PASSWORD '<some-password>';
     ```

     <Warning>
       **Credential character limitations**

       For user credentials containing special characters, please avoid using the following characters: `@`, `[`, `]`, `/`, `?`, `#`, `"`, `\\`, `+`, space, `&`, `:` as these characters can break connection string parsing.
     </Warning>

  3. Grant user `create` and `temporary` privileges on the database. `create` allows the service to create new schemas and `temporary` allows the service to create temporary tables.

     ```sql
     GRANT CREATE, TEMPORARY ON DATABASE <database> TO <username>;
     ```

     <Warning>
       **If the schema already exists**

       By default, the service creates a new schema based on the destination configuration (in the next step). If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema, using `GRANT ALL ON schema <schema> TO <username>;`
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, **port**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268532980627)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271125483283)
</Steps>
