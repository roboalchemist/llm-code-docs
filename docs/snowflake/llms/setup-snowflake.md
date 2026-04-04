# Source: https://docs.snowflake.com/en/connectors/kafkahp/setup-snowflake.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/salesforce-bulk-api/setup-snowflake.md

# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/oracle/setup-snowflake.md

# Openflow Connector for Oracle: Set up Snowflake

> **Note:**
>
> This connector is subject to the [Snowflake Connector Terms](https://www.snowflake.com/legal/snowflake-connector-terms/).

> **Note:**
>
> The Openflow Connector for Oracle is also subject to additional terms of service beyond the standard
> connector terms of service. For more information, see the
> [Openflow Connector for Oracle Addendum](https://www.snowflake.com/en/legal/optional-offerings/offering-specific-terms/openflow-oracle-terms/).

This topic describes how to set up your Snowflake environment for the
Openflow Connector for Oracle.

As a Snowflake administrator, perform the following tasks:

1. Create a destination database in Snowflake to store the replicated data:

   ```sqlexample
   CREATE DATABASE <destination_database>;
   ```

2. Create a Snowflake [service user](../../../../../sql-reference/sql/create-user.md):

   ```sqlexample
   CREATE USER <openflow_user>
     TYPE = SERVICE
     COMMENT='Service user for automated access of Openflow';
   ```

3. Create a Snowflake role for the connector and grant the required
   privileges:

   ```sqlexample
   CREATE ROLE <openflow_role>;
   GRANT ROLE <openflow_role> TO USER <openflow_user>;
   GRANT USAGE ON DATABASE <destination_database> TO ROLE <openflow_role>;
   GRANT CREATE SCHEMA ON DATABASE <destination_database>
     TO ROLE <openflow_role>;
   ```

   Use this role to manage the connector’s access to the Snowflake database.

   To create objects in the destination database, you must grant the
   [USAGE and CREATE SCHEMA privileges](../../../../security-access-control-privileges.md)
   on the database to the role used to manage access.
4. Create a Snowflake warehouse for the connector and grant the required
   privileges:

   ```sqlexample
   CREATE WAREHOUSE <openflow_warehouse> WITH
     WAREHOUSE_SIZE = 'XSMALL'
     AUTO_SUSPEND = 300
     AUTO_RESUME = TRUE;
   GRANT USAGE, OPERATE ON WAREHOUSE <openflow_warehouse>
     TO ROLE <openflow_role>;
   ```

   Snowflake recommends starting with a XSMALL warehouse size, then
   experimenting with size depending on the number of tables being
   replicated and the amount of data transferred. Large numbers of tables
   typically scale better with multi-cluster warehouses, rather than a
   larger warehouse size. For more information, see
   [multi-cluster warehouses](../../../../warehouses-multicluster.md).
5. Set up the public and private keys for key pair authentication:

   1. Create a pair of secure keys (public and private).
   2. Store the private key for the user in a file to supply to the
      connector’s configuration.
   3. Assign the public key to the Snowflake service user:

      ```sqlexample
      ALTER USER <openflow_user> SET RSA_PUBLIC_KEY = 'thekey';
      ```

      For more information, see [Key-pair authentication and key-pair rotation](../../../../key-pair-auth.md).

## Next steps

[Configure the connector](setup-connector.md).
