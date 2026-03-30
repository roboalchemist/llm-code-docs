# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/connectors/oracle/setup-connector.md

# Install and configure the Openflow Connector for Oracle

> **Note:**
>
> This connector is subject to the [Snowflake Connector Terms](https://www.snowflake.com/legal/snowflake-connector-terms/).

> **Note:**
>
> The Openflow Connector for Oracle is also subject to additional terms of service beyond the standard
> connector terms of service. For more information, see the
> [Openflow Connector for Oracle Addendum](https://www.snowflake.com/en/legal/optional-offerings/offering-specific-terms/openflow-oracle-terms/).

This topic describes the steps to install and configure the Openflow Connector for Oracle connector.

As a data engineer, perform the following tasks to install and configure the connector:

## Install the connector

To install the connector, do the following as a data engineer:

1. Navigate to the Openflow overview page. In the Featured connectors section, select View more connectors.
2. On the Openflow connectors page, find the connector and select Add to runtime.
3. In the Select runtime dialog, select your runtime from the Available runtimes drop-down list and click Add.

   > **Note:**
   >
   > Before you install the connector, ensure that you have created a database and schema in Snowflake for the connector to store ingested data.
4. Authenticate to the deployment with your Snowflake account credentials and select Allow when prompted to allow the runtime application to access your Snowflake account. The connector installation process takes a few minutes to complete.
5. Authenticate to the runtime with your Snowflake account credentials.

The Openflow canvas appears with the connector process group added to it.

## Configure the connector

To configure the connector, do the following as a data engineer:

1. Right-click on the added runtime and select Parameters.
2. Populate the required parameter values.

   For more information on the required parameter values, see the following sections:

   * Snowflake Destination Parameters: Used to establish connection with Snowflake.
   * Oracle Ingestion Parameters: Used to specify the tables to replicate.
   * Oracle Source Parameters: Used to define the configuration of data downloaded from Oracle.

### Snowflake Destination Parameters

| Parameter | Description | Required |
| --- | --- | --- |
| Destination Database | The database where data will be persisted. It must already exist in Snowflake. The name is case-sensitive. For unquoted identifiers, provide the name in uppercase. | Yes |
| Snowflake Authentication Strategy | When using:   ***Snowflake Openflow Deployment** or **BYOC**: Use SNOWFLAKE_MANAGED_TOKEN.   This token is managed automatically by Snowflake.   BYOC deployments must have previously configured   [runtime roles](../../setup-openflow-byoc.md) to use SNOWFLAKE_MANAGED_TOKEN.* **BYOC:** Alternatively BYOC can use KEY_PAIR as the value for authentication strategy. | Yes |
| Snowflake Account Identifier | When using:   ***Session Token Authentication Strategy**: Must be blank.* **KEY_PAIR**: Snowflake account name formatted as [organization-name]-[account-name] where data will be persisted. | Yes |
| Snowflake Connection Strategy | When using KEY_PAIR, specify the strategy for connecting to Snowflake:   ***STANDARD** (default): Connect using standard public routing to Snowflake services.* **PRIVATE_CONNECTIVITY**: Connect using private addresses associated with the supporting cloud platform such as AWS PrivateLink. | Required for BYOC with KEY_PAIR only, otherwise ignored. |
| Snowflake Private Key | When using:   ***Session Token Authentication Strategy**: Must be blank.* **KEY_PAIR**: Must be the RSA private key used for authentication.  The RSA key must be formatted according to PKCS8 standards and have standard PEM headers and footers.   Note that either a Snowflake Private Key File or a Snowflake Private Key must be defined. | No |
| Snowflake Private Key File | When using:   ***Session token authentication strategy**: The private key file must be blank.* **KEY_PAIR**: Upload the file that contains the RSA private key used for authentication to Snowflake,   formatted according to PKCS8 standards and including standard PEM headers and footers.   The header line begins with `-----BEGIN PRIVATE`.   To upload the private key file, select the Reference asset checkbox. | No |
| Snowflake Private Key Password | When using   ***Session Token Authentication Strategy**: Must be blank.* **KEY_PAIR**: Provide the password associated with the Snowflake Private Key File. | No |
| Snowflake Role | When using   ***Session Token Authentication Strategy**: Use Snowflake Role assigned to the runtime or child role granted to this Snowflake Role.   You can find your runtime Snowflake Role in the Openflow UI, by expanding the More Options [⋮] button for your runtime and selecting Set Snowflake role.* **KEY_PAIR** Authentication Strategy: Use a valid role configured for your service user. | Yes |
| Snowflake Username | When using   ***Session Token Authentication Strategy**: Must be blank.* **KEY_PAIR**: Provide the user name used to connect to the Snowflake instance. | Yes |
| Oversized Value Strategy | Determines how the connector handles values that exceed its internal size limits (16 MB) during replication. Possible values are:  ***Fail Table** (default): The table is marked as permanently failed, and replication stops for that table.* **Set Null**: The value is replaced with `NULL` in the destination table.   Use this to prevent table failures when it is acceptable to lose data in tables beyond the oversized value. | No |
| Snowflake Warehouse | Snowflake warehouse used to run queries. | Yes |

### Oracle Ingestion Parameters

| Parameter | Description |
| --- | --- |
| Included Table Names | Comma-separated list of fully-qualified table paths. Tables must be specified using fully qualified database, schema and table name format: DATABASE_NAME.SCHEMA_NAME.TABLE_NAME.  For example: `MYPDB.SALES.CUSTOMERS, MYPDB.SALES.ORDERS` |
| Included Table Regex | A regular expression to match table paths for automatic inclusion of existing and new tables. The regex pattern must match the three-part naming convention: DATABASE_NAME.SCHEMA_NAME.TABLE_NAME.  For example: `MYPDB\.SALES\..*` to match all tables in the SALES schema within the MYPDB database. |
| Filter JSON | A JSON array to include specific columns based on a regex pattern for given tables. |
| Merge Task Schedule CRON | A CRON expression to define when merge operations from the Journal to the Destination Table are triggered. For example, \* \* \* \* \* ? for continuous merge. |
| Object Identifier Resolution | Specifies how source object identifiers such as schemas, tables, and column names are stored and queried in Snowflake. This setting determines if you must use double quotes in SQL queries.  Option 1: Default, case-insensitive (recommended).   ***Transformation**: All identifiers are converted to uppercase. For   example, `My_Table` becomes `MY_TABLE`.* **Queries**: SQL queries are case-insensitive and don’t require SQL   double quotes.  For example `SELECT * FROM my_table;` returns the same results as `SELECT * FROM MY_TABLE;`.   **Note:** Snowflake recommends using this option if database objects are not expected to have mixed case names.  Option 2: case-sensitive.   ***Transformation**: Case is preserved.   For example, `My_Table` remains `My_Table`.* **Queries**: SQL queries must use double quotes to match the exact   case for database objects.   For example, `SELECT * FROM "My_Table";`.   **Important:** Do not change this setting after connector ingestion has begun. Changing this setting after ingestion has begun breaks the existing ingestion. If you must change this setting, create a new connector instance. |
| Snapshot Fetching Strategy | Determines the snapshot load fetching strategy:   ***SEQUENTIAL_BY_PRIMARY_KEY** (default): Uses fixed-size batches retrieved sequentially by primary key.* **CONCURRENT_BY_ROWID**: Splits tables into chunks bound by ranges of physical row ids, and retrieves each chunk in parallel. |

### Oracle Source Parameters

| Parameter | Description | Required |
| --- | --- | --- |
| Oracle Connection URL | JDBC URL of the database connection to the DB. The URL must specify the target container (PDB or CDB) that contains the data to be replicated. For example `jdbc:oracle:thin@<host>:<port>/YOUR_DB_NAME` where YOUR_DB_NAME is the name of your PDB or CDB.  When SSL is enabled, use the TCPS protocol, for example `jdbc:oracle:thin:@tcps://<host>:<tcps_port>/YOUR_DB_NAME`.  **Note:** The connector works within a single database/container. Ensure the JDBC URL points directly to the container that holds the tables to be replicated. | Yes |
| Oracle Username | Username of the connect user that has access to the XStream Server. | Yes |
| Oracle Password | Password of the connect user that has access to the XStream Server. | Yes |
| Oracle SSL Mode | Controls SSL encryption for connections to the Oracle database.   ***DISABLED**, which is the default: Connect without SSL.* **VERIFY_CA**: Connect with SSL. Verifies that a trusted Certificate Authority   issued the server certificate. * **VERIFY_IDENTITY**: Connect with SSL. Verifies the CA certificate and that the   server hostname matches the certificate’s subject.   When set to VERIFY_CA or VERIFY_IDENTITY, you must also provide the Oracle Wallet Filename parameter. | Yes |
| Oracle Wallet Filename | Upload the file that contains the Oracle auto-login wallet file (`cwallet.sso`). The wallet must contain the trusted server certificate for SSL connections.  For information about creating the wallet, see [Configure SSL connections (optional)](setup-oracledb.md). | Required when SSL Mode is not DISABLED |
| Oracle Database Processor Multiplier | Core Processor Licensing Factor as described in [Oracle Processor Core Factor Table](https://www.oracle.com/contracts/docs/processor-core-factor-table-070634.pdf) | Required for Embedded License only |
| Oracle Database Processor Cores | The number of processor cores in your Oracle database. | Required for Embedded License only |
| XStream Billing Acknowledgement | A confirmation of the licensing agreement | Required for Embedded License only |
| XStream Out Server Name | The name of the XStream Server that must already exist in Oracle. | Yes |
| XStream Out Server URL | JDBC URL of the database connection for XStream, must use OCI driver. For example `jdbc:oracle:oci:@<host>:<port>/SID`.  When SSL is enabled, use the TCPS protocol, for example `jdbc:oracle:oci:@tcps://<host>:<tcps_port>/SID`.  **Note:** When SSL Mode is enabled, the connector automatically adds `SSL_SERVER_DN_MATCH` and `MY_WALLET_DIRECTORY` to the XStream URL. You do not need to include these manually. | Yes |

## Restart table replication

A table in FAILED state — for example, due to a missing primary key or unsupported schema change — does not restart automatically. If a table enters a FAILED state or you need to restart replication from scratch, use the following procedure to remove and re-add the table to replication.

> **Note:**
>
> If the failure was caused by an issue in the source table such as a missing primary key, resolve that issue in the source database before continuing.

1. Remove the table from flow parameters: In the Ingestion Parameters context, either remove the table from the Included Table Names or modify the Included Table Regex so the table is no longer matched.
2. Verify the table has been removed:

   1. In the Openflow runtime canvas, right-click a processor group and choose Controller Services.
   2. In the table listing controller services, locate the Table State Store row, click the three vertical dots on the right side of the row, then choose View State.
   > **Important:**
   >
   > You must wait until the table’s state is fully removed from this list before proceeding. Do not continue until this configuration change has completed.
3. Clean up the destination: Once the table’s state shows as fully removed, manually [DROP](../../../../../sql-reference/sql/drop-table.md) the destination table in Snowflake. Note that the connector will not overwrite an existing destination table during the snapshot phase; if the table still exists, replication will fail again. Optionally, the journal table and stream can also be removed if they are no longer needed.
4. Re-add the table: Update the Included Table Names or Included Table Regex parameters to include the table again.
5. Verify the restart: Check the Table State Store using the instructions given previously. The state of the table should appear with the status NEW, then transition to SNAPSHOT_REPLICATION, and finally INCREMENTAL_REPLICATION.

## Run the flow

1. Right-click on the plane and select Enable all Controller Services.
2. Right-click on the imported process group and select Start. The connector starts the data ingestion.

## Next steps

* (Optional) [Set up incremental replication without snapshots](incremental-replication.md).
* [Monitor the flow](../../monitor.md).
