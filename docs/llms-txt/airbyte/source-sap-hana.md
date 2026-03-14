# Source: https://docs.airbyte.com/integrations/enterprise-connectors/source-sap-hana.md

![]()

# Source SAP HANA

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Enterprise](/integrations/connector-support-levels.md)

* Connector Version

  0.0.17

* Enterprise Connector

  **This premium connector is available to Enterprise customers at an additional cost**.

  <!-- -->

  [Talk to Sales](https://airbyte.com/company/talk-to-sales)

  <!-- -->

  [ ](https://airbyte.com/company/talk-to-sales).

* Definition ID

  `b6935898-aadb-46ae-99ca-d697207994c1`

Airbyte's incubating SAP HANA enterprise source connector currently offers Full Refresh and Incrementals syncs for streams. Support for Change Data Capture (CDC) is available using a trigger-based approach.

## Features[​](#features "Direct link to Features")

| Feature                   | Supported?(Yes/No) | Notes |
| ------------------------- | ------------------ | ----- |
| Full Refresh Sync         | Yes                |       |
| Incremental Sync - Append | Yes                |       |
| Change Data Capture (CDC) | Yes                |       |

## Prequisities[​](#prequisities "Direct link to Prequisities")

* Dedicated read-only Airbyte user with read-only access to tables needed for replication

* SAP HANA Host Name URL

  <!-- -->

  * In the SAP HANA Cloud Management Portal, this can be found under the **Connections** tab for you SAP HANA instance
  * The Host Name is the first portion of the SQL Endpoint before the Port
  * ie:**01234abce-1234-56fg.us-01-hanacloud.ondemand.com**:123
  * The **Host** is also a combination of the **Instance ID** and **Landscape**

* Port Number

  <!-- -->

  * Inside of the SAP HANA Cloud Management Portal, this can be found under the **Connections** tab for you SAP HANA instance
  * The **Port** is listed explicitly in addition to being part of the **SQL Endpoint**

## Setup Guide[​](#setup-guide "Direct link to Setup Guide")

1. Enter your SAP HANA Host Name

2. Enter the Port number

3. Provide the login credentials for the SAP HANA account with access to the tables

4. Specify the schemas for tables that you would like to replicate

5. Select your desired Update Method:

   <!-- -->

   * **User Defined Cursor**: For incremental syncs using a cursor column (e.g., updated\_at)
   * **Change Data Capture (CDC)**: For real-time change tracking using database triggers

## Change Data Capture (CDC)[​](#change-data-capture-cdc "Direct link to Change Data Capture (CDC)")

The SAP HANA source connector supports incremental syncs using Change Data Capture (CDC) through a trigger-based approach. This method captures INSERT, UPDATE, and DELETE operations on your source tables by creating database triggers that log changes to dedicated trigger tables.

### How CDC Works[​](#how-cdc-works "Direct link to How CDC Works")

When CDC is enabled, the connector:

1. **Reads from pre-configured trigger tables** in a dedicated `_ab_cdc` schema
2. **Uses trigger tables** to track all data modifications with before/after values
3. **Reads incrementally** from trigger tables using `_ab_trigger_change_time` as the cursor

Note: Trigger tables and database triggers must be manually created before enabling CDC.

### Trigger Table Structure[​](#trigger-table-structure "Direct link to Trigger Table Structure")

For each source table, a corresponding trigger table is created with the naming convention:

* **Schema**: `_ab_cdc`
* **Table name**: `_ab_trigger_{source_schema}_{source_table}`

Each trigger table contains:

* `_ab_trigger_change_id`: Unique identifier for each change (auto-incrementing)
* `_ab_trigger_change_time`: Timestamp when the change occurred (used as cursor)
* `_ab_trigger_operation_type`: Type of operation (INSERT, UPDATE, DELETE)
* `_ab_trigger_{column}_before`: Previous value for each source column (for UPDATE/DELETE)
* `_ab_trigger_{column}_after`: New value for each source column (for INSERT/UPDATE)

### CDC Configuration[​](#cdc-configuration "Direct link to CDC Configuration")

To use CDC:

1. **Select CDC method**: In the connector configuration, choose "Read Changes using Change Data Capture (CDC)" as your Update Method

2. **Configure CDC settings**:

   <!-- -->

   * **Initial Load Timeout**: How long the initial load can run before switching to CDC (4-24 hours, default: 8)
   * **Invalid CDC Position Behavior**: Whether to fail sync or re-sync data if cursor position becomes invalid

### CDC Prerequisites[​](#cdc-prerequisites "Direct link to CDC Prerequisites")

* **Manual trigger setup**: You must manually create trigger tables and database triggers before enabling CDC

* **Database permissions**: Your SAP HANA user must have permissions to:

  <!-- -->

  * Read from trigger tables in the `_ab_cdc` schema
  * Access source tables for initial discovery

* **Trigger table setup**: Trigger tables can be created manually or programatically by an administrator of the SAP HANA instance. The setup requires:

  <!-- -->

  * Create the `_ab_cdc` schema
  * Create trigger tables with the naming convention `_ab_trigger_{source_schema}_{source_table}`
  * Set up INSERT, UPDATE, and DELETE triggers on source tables to populate trigger tables
  * Ensure trigger tables contain the required meta fields (`_ab_trigger_change_id`, `_ab_trigger_change_time`, `_ab_trigger_operation_type`)

### CDC Limitations[​](#cdc-limitations "Direct link to CDC Limitations")

* **Manual trigger management**: If you need to modify source table schemas, you may need to recreate the corresponding triggers
* **Storage overhead**: Trigger tables store before/after values for all changes, which requires additional database storage
* **Performance impact**: Database triggers add some overhead to INSERT/UPDATE/DELETE operations on source tables

## Data type mapping[​](#data-type-mapping "Direct link to Data type mapping")

SAP HANA data types are mapped to the following Airbyte data types when synchronizing data.

| SAP HANA Type  | Airbyte Type                 | Notes |
| -------------- | ---------------------------- | ----- |
| `BOOLEAN`      | BOOLEAN                      |       |
| `DOUBLE`       | NUMBER                       |       |
| `FLOAT`        | NUMBER                       |       |
| `REAL`         | NUMBER                       |       |
| `SMALLDECIMAL` | NUMBER                       |       |
| `DECIMAL`      | NUMBER                       |       |
| `DEC`          | NUMBER                       |       |
| `INTEGER`      | INTEGER                      |       |
| `TINYINT`      | INTEGER                      |       |
| `SMALLINT`     | INTEGER                      |       |
| `BIGINT`       | INTEGER                      |       |
| `CHAR`         | STRING                       |       |
| `VARCHAR`      | STRING                       |       |
| `ALPHANUM`     | STRING                       |       |
| `NCHAR`        | STRING                       |       |
| `NVARCHAR`     | STRING                       |       |
| `SHORTTEXT`    | STRING                       |       |
| `TIME`         | TIME\_WITHOUT\_TIMEZONE      |       |
| `DATE`         | DATE                         |       |
| `SECONDDATE`   | TIMESTAMP\_WITHOUT\_TIMEZONE |       |
| `TIMESTAMP`    | TIMESTAMP\_WITHOUT\_TIMEZONE |       |
| `BINARY`       | BINARY                       |       |
| `VARBINARY`    | BINARY                       |       |
| `REAL_VECTOR`  | BINARY                       |       |
| `BLOB`         | BINARY                       |       |
| `CLOB`         | STRING                       |       |
| `NCLOB`        | STRING                       |       |
| `TEXT`         | STRING                       |       |
| `BINTEXT`      | STRING                       |       |
| `ST_POINT`     | BINARY                       |       |
| `ST_GEOMETRY`  | BINARY                       |       |

## Reference[​](#reference "Direct link to Reference")

### Configuration[​](#configuration "Direct link to Configuration")

| Input                                | Type    | Description                                                                                                                                      | Default Value                          |
| ------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| `host`                               | string  | Hostname of the database.                                                                                                                        |                                        |
| `port`                               | integer | Port of the database.                                                                                                                            | `443`                                  |
| `username`                           | string  | The username which is used to access the database.                                                                                               |                                        |
| `password`                           | string  | The password associated with the username.                                                                                                       |                                        |
| `schemas`                            | array   | The list of schemas to sync from. Defaults to user. Case sensitive.                                                                              |                                        |
| `jdbc_url_params`                    | string  | Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. |                                        |
| `encryption`                         | object  | The encryption method with is used when communicating with the database.                                                                         | `{"encryption_method": "unencrypted"}` |
| `tunnel_method`                      | object  | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                             | `{"tunnel_method": "NO_TUNNEL"}`       |
| `cursor`                             | object  | Configures how data is extracted from the database.                                                                                              | `{"cursor_method": "user_defined"}`    |
| `checkpoint_target_interval_seconds` | integer | How often (in seconds) a stream should checkpoint, when possible.                                                                                | `300`                                  |
| `concurrency`                        | integer | Maximum number of concurrent queries to the database.                                                                                            | `1`                                    |
| `check_privileges`                   | boolean | When enabled, the connector will query each table individually to check access privileges during schema discovery.                               | `true`                                 |

#### Update Method Configuration[​](#update-method-configuration "Direct link to Update Method Configuration")

**User Defined Cursor**:

```
{
  "cursor_method": "user_defined"
}
```

**Change Data Capture (CDC)**:

```
{
  "cursor_method": "cdc",
  "initial_load_timeout_hours": 8,
  "invalid_cdc_cursor_position_behavior": "Fail sync"
}
```
