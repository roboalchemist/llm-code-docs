# Source: https://fivetran.com/docs/logs/fivetran-platform

Title: Fivetran Platform Connector

URL Source: https://fivetran.com/docs/logs/fivetran-platform

Markdown Content:
Fivetran generates and logs several types of data related to your account and destinations:

*   [Log events](https://fivetran.com/docs/logs#logeventlist) related to connections, dashboard user actions, Fivetran API calls, and schema change data.
*   Account- and destination-related metadata that includes:
    *   Role/membership information
    *   Column lineage (available for [Enterprise and Business Critical accounts](https://www.fivetran.com/pricing))
    *   Granular consumption information

You can use this data for the following purposes:

*   Monitoring and troubleshooting of connections
*   Tracking your usage
*   Conducting audits

The Fivetran Platform Connector delivers your logs and account or destination metadata to a schema in your [destination](https://fivetran.com/docs/destinations). We automatically add a Fivetran Platform connection to every new destination you create. The schema name we use for these automatically created connections is `fivetran_metadata`. By default, we configure the connection to sync once a day, but you can set a different sync frequency and change other default settings on the **Setup** tab of the connection details page.

We automatically add a Fivetran Platform connection to every destination, but it doesn't start syncing logs and metadata until you add a [connection](https://fivetran.com/docs/connectors) to your destination.

If you are an Account Administrator, you can manually add the Fivetran Platform connection on an account level so that it syncs all the metadata and logs for all the destinations in your account to a single destination. If an account-level Fivetran Platform connection is already configured in a destination in your Fivetran account, then we don't add destination-level Fivetran Platform connections to the new destinations you create.

The MAR that Fivetran Platform connections generate is free, though you may incur costs in your destination. Learn more in our [pricing documentation](https://fivetran.com/docs/usage-based-pricing#fivetranplatformconnector).

* * *

Features[](https://fivetran.com/docs/logs/fivetran-platform#features)
---------------------------------------------------------------------

| Feature Name | Supported | Notes |
| --- | --- | --- |
| [Capture deletes](https://fivetran.com/docs/using-fivetran/features#capturedeletes) |  | `CONNECTION`, `RESOURCE_MEMBERSHIP`, `ROLE`, `ROLE_PERMISSION`, `TEAM`, `TEAM_MEMBERSHIP`, and `USER` tables |
| [History mode](https://fivetran.com/docs/using-fivetran/features#historymode) |  |  |
| [Custom data](https://fivetran.com/docs/getting-started/features#customdata) |  |  |
| [Data blocking](https://fivetran.com/docs/getting-started/features#datablocking) |  | Column level |
| [Column hashing](https://fivetran.com/docs/getting-started/features#columnhashing) |  |  |
| [Re-sync](https://fivetran.com/docs/getting-started/features#resync) |  | Connection level |
| [Row filtering](https://fivetran.com/docs/getting-started/features#rowfiltering) |  |  |
| [API configurable](https://fivetran.com/docs/getting-started/features#apiconfigurable) |  | [API configuration](https://fivetran.com/docs/rest-api/api-reference/connections/create-connection?service=fivetran_log) |
| [Priority-first sync](https://fivetran.com/docs/getting-started/features#priorityfirstsync) |  |  |
| [Fivetran data models](https://fivetran.com/docs/getting-started/features#fivetrandatamodels) |  | [Model details](https://fivetran.com/docs/transformations/data-models/fivetran-platform-connector-data-model) |
| [Private networking](https://fivetran.com/docs/getting-started/features#privatenetworking) |  |  |
| [Authorization via API](https://fivetran.com/docs/rest-api/getting-started#connectorssupportedbyapiandtheirauthorizationmethods) |  |  |

* * *

Supported deployment models[](https://fivetran.com/docs/logs/fivetran-platform#supporteddeploymentmodels)
---------------------------------------------------------------------------------------------------------

We support the [SaaS](https://fivetran.com/docs/deployment-models/saas-deployment) and [Hybrid](https://fivetran.com/docs/deployment-models/hybrid-deployment) deployment models for the connector.

* * *

Setup guide[](https://fivetran.com/docs/logs/fivetran-platform#setupguide)
--------------------------------------------------------------------------

Follow our step-by-step [setup guide](https://fivetran.com/docs/logs/fivetran-platform/setup-guide) to manually set up your Fivetran Platform connection account-wide.

* * *

Sync overview[](https://fivetran.com/docs/logs/fivetran-platform#syncoverview)
------------------------------------------------------------------------------

Most of the tables in the Fivetran Platform Connector use [incremental sync](https://fivetran.com/docs/getting-started/glossary#incrementalsync) so that they are updated when there is new or changed data.

For the `LOG` and `CONNECTOR_SDK_LOG` tables, new data is appended to the table. To ensure log data integrity, all connection data tables should have data present, complete, and valid following the [initial sync](https://fivetran.com/docs/getting-started/glossary#initialsync) of the relevant connection. Where the data exists, we sync the previous 7 days' worth of data prior to the date of the initial sync of the Fivetran Platform connection. This also means that when a [full re-sync](https://fivetran.com/docs/getting-started/glossary#resync) is triggered for the Fivetran Platform connection, the `LOG` and `CONNECTOR_SDK_LOG` tables will have 7 days' worth of historical data .

* * *

Schema information[](https://fivetran.com/docs/logs/fivetran-platform#schemainformation)
----------------------------------------------------------------------------------------

*   The `*_SCHEMA`, `*_TABLE`, `*_COLUMN`, `*_LINEAGE`, and `*_CHANGE_EVENT` tables are available only on the Enterprise and Business Critical plans.
*   The `SOURCE_TABLE` table stores metadata for all tables that have ever been synced to your destination — including both currently enabled and disabled tables.
*   The `*_CHANGE_EVENT` tables contain only creation and modification events. Deletion events are not supported yet.

This schema applies to all Fivetran Platform connections.

![Image 1: Explore Fivetran Platform schema ERD](https://fivetran.com/_/api/service-erd/fivetran_log/preview-image/public)

Explore Fivetran Platform schema ERD

If your Fivetran Platform connection was created before May 12, 2025, you may see some additional tables or columns, which have been deprecated:

*   `CONNECTOR` table - This table has been deprecated and replaced by `CONNECTION` table.
*   `connector_name` column in the `INCREMENTAL_MAR` table - This column has been deprecated and replaced by `connection_name`.
*   `connector_id` column in all applicable metadata tables - This column has been deprecated and replaced by `connection_id`.

* * *

Using Fivetran Platform Connector with its data models[](https://fivetran.com/docs/logs/fivetran-platform#usingfivetranplatformconnectorwithitsdatamodels)
----------------------------------------------------------------------------------------------------------------------------------------------------------

You can use our Fivetran Platform Connector along with the [Fivetran Platform Connector data model](https://fivetran.com/docs/transformations/data-models/fivetran-platform-connector-data-model), with each of the [model tables](https://fivetran.com/docs/transformations/data-models/fivetran-platform-connector-data-model#whatdoesthisdbtpackagedo) storing specific type of data.

You can also set up our free, pre-built Quickstart models. These models are autonomously created using the logic defined in our Fivetran Platform dbt Package, and prepare the data from the Fivetran Platform Connector in analysis-ready models covering spend, connection performance and status, and metadata/data lineage. If you are an advanced dbt user, you can also use the package for increased flexibility.

* * *

Important tables[](https://fivetran.com/docs/logs/fivetran-platform#importanttables)
------------------------------------------------------------------------------------

You can query the data in the different destination tables to monitor different metrics such as connection performance, destination and source metadata, and MAR usage.

### INCREMENTAL_MAR table[](https://fivetran.com/docs/logs/fivetran-platform#incrementalmartable)

The `INCREMENTAL_MAR` table provides incremental daily active rows (MAR) for each destination schema, the associated tables, and the time when the MAR is calculated.

| Column Name | Description |
| --- | --- |
| `destination_id` | The ID of the destination for which MAR is calculated. |
| `free_type` | If it is free MAR, the value indicates the type of free MAR. For paid MAR,the value is `PAID`. |
| `incremental_rows` | The number of new distinct primary keys on the current day synced for the connection. |
| `connector_name` | The name of the connection for which MAR is calculated. _Deprecated_ and replaced by `connection_name`. |
| `connection_name` | The name of the connection for which MAR is calculated. |
| `measured_date` | The date in UTC format of when MAR is calculated. |
| `schema_name` | The destination schema name for which MAR is calculated. |
| `sync_type` | This defines whether the sync for which MAR calculated is HISTORICAL or INCREMENTAL. Currently, the available value is `UNKNOWN`. |
| `table_name` | The table name associated with MAR. |
| `_fivetran_synced` | The timestamp of when Fivetran last successfully synced the row. |
| `updated_at` | The timestamp of when MAR is updated. |

### TRANSFORMATION_RUNS table[](https://fivetran.com/docs/logs/fivetran-platform#transformationrunstable)

A transformation job consists of one or several models run in sequence. The `TRANSFORMATION_RUNS` table provides the total number of successful transformation model runs in each job and destination schema. Additionally, it provides a timestamp of when the model run count was updated.

| Column Name | Description |
| --- | --- |
| `destination_id` | The ID of the destination for which model runs is calculated. |
| `free_type` | If it is a free model run, the value indicates the type of the free run. For paid runs, the value is `PAID`. |
| `job_id` | The unique identifier of a transformation job. |
| `job_name` | The name of the transformation job. |
| `measured_date` | The date in UTC format of when models were run. |
| `model_runs` | The total number of times the models have run. |
| `project_type` | The type of project associated with the job: `DBT_CORE`, `QUICKSTART`. |
| `updated_at` | The timestamp of when the model run count was updated. |
| `_fivetran_synced` | The timestamp of when Fivetran last successfully synced the row. |

### LOG table[](https://fivetran.com/docs/logs/fivetran-platform#logtable)

We write the [log events](https://fivetran.com/docs/logs#logeventlist) to the `LOG` table to your destination.

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | The ID of the log event (internal). | STRING |
| `time_stamp` | Indicates the time when the log event is created. | TIMESTAMP |
| `_fivetran_synced` | Indicates the time when Fivetran last successfully synced the row. | TIMESTAMP |
| `connector_id` | The ID of the connection for which the event is logged. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which the event is logged. | STRING |
| `event` | The event type. Events can be classified as a warning, an error, or just an information log. | STRING |
| `message_event` | The routine involved in the log. | STRING |
| `message_data` | The details of the event in JSON format. | STRING |

### AUDIT_TRAIL table[](https://fivetran.com/docs/logs/fivetran-platform#audittrailtable)

We write the audit trail events to the `AUDIT_TRAIL` table in your destination.

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | The ID of the log event (internal). | STRING |
| `captured_at` | Indicates the time when the action took place. | TIMESTAMP |
| `user_id` | The ID of the user who completed the action. | STRING |
| `action` | The action type (for example, CREATE, EDIT, DELETE). | STRING |
| `interaction_method` | The action method used to complete the action (for example, WEB_UI, API, SYSTEM). | STRING |
| `primary_resource_type` | The type of the primary resource (for example, ACCOUNT, DESTINATION, CONNECTOR, TEAM, USER, TRANSFORMATION). | STRING |
| `primary_resource_id` | The ID of the primary resource. | STRING |
| `secondary_resource_type` | the type of the secondary resource (for example, ACCOUNT, DESTINATION, CONNECTOR, TEAM, USER, TRANSFORMATION). | STRING |
| `secondary_resource_id` | The ID of the secondary resource. | STRING |
| `old_values` | The JSON representation of the old resource attributes. | STRING |
| `new_values` | The JSON representation of the new resource attributes. | STRING |

This table stores detailed information about user actions and their results.

This table has the `user_id`, `captured_at`, and `interaction_method` columns that store information about the user who completed an action, when they did it, and how they interacted with the system.Events are composed of `resources` and `actions` where a `resource` is used to represent any type of system entity and an `action` represents something a user does.

For a given event, we support a primary and optional secondary resource to represent actions involving multiple entities, for example, adding a user to a team. This approach allows to decompose any high-level business logic to a collection of basic actions. The primary and secondary resources are specified based on the entity hierarchy and composition. The primary resource is a container, and the secondary resource is a member.

Some examples using this approach are as follows:

*   An account (the container) is composed of destinations, connections, users, teams and transformations (members).
*   A team (the container) is composed of users (members).
*   A destination (the container) contains an external log service (members).

To track changes to a resource's attributes and settings, we use the `old_values` and `new_values` columns that contain minimally-spanning JSON objects. It allows auditors to easily identify how an entity has changed as a result of an action. An example can be a user-renaming log event that contains an old value: {“name”: “Alice”} and a new value: {“name”: “Eve”}.

The `AUDIT_TRAIL` table is available only on the Enterprise plan and above.

### CONNECTOR_SDK_LOG table[](https://fivetran.com/docs/logs/fivetran-platform#connectorsdklogtable)

We write the Connector SDK log events to the `CONNECTOR_SDK_LOG` table in your destination.

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | The ID of the log event (internal). | STRING |
| `event_time` | Indicates the time when the log event is created. | TIMESTAMP |
| `connector_id` | The ID of the connection for which the event is logged. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which the event is logged. | STRING |
| `level` | The event type. Events can be classified as a warning, an error, or just an information log. | STRING |
| `message` | The details of the event in plain text. | STRING |
| `message_origin` | The source of the log event. For example "connector_sdk". | STRING |
| `sync_id` | The ID of the sync durinc which the event is appeared. | STRING |

### SOURCE_SCHEMA table[](https://fivetran.com/docs/logs/fivetran-platform#sourceschematable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Schema ID. | BIGSERIAL NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `name` | The name of the table. | TEXT NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### DESTINATION_SCHEMA table[](https://fivetran.com/docs/logs/fivetran-platform#destinationschematable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Schema ID. | BIGSERIAL NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `destination_id` | The ID of the destination for which metadata is collected. | STRING |
| `name` | The name of the table. | TEXT NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### SOURCE_TABLE table[](https://fivetran.com/docs/logs/fivetran-platform#sourcetabletable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Table ID. | BIGSERIAL NOT NULL |
| `schema_id` | ID of the corresponding schema. | SERIAL NOT NULL |
| `name` | The name of the table. | TEXT NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### DESTINATION_TABLE table[](https://fivetran.com/docs/logs/fivetran-platform#destinationtabletable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Table ID. | BIGSERIAL NOT NULL |
| `schema_id` | ID of the corresponding schema. | SERIAL NOT NULL |
| `name` | The name of the table. | TEXT NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `destination_id` | The ID of the destination for which metadata is collected. | STRING |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### SOURCE_COLUMN table[](https://fivetran.com/docs/logs/fivetran-platform#sourcecolumntable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Column ID. | BIGSERIAL NOT NULL |
| `table_id` | The ID of the corresponding table. | BIGSERIAL NOT NULL |
| `name` | The name of the column. | TEXT NOT NULL |
| `type` | Column type (for example, `STRING`). | TEXT NOT NULL |
| `is_primary_key` | A flag indicating if this column is part of the primary key. | BOOLEAN NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |
| `updated_at` | Modification timestamp. | TIMESTAMPTZ NOT NULL |

### DESTINATION_COLUMN table[](https://fivetran.com/docs/logs/fivetran-platform#destinationcolumntable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Column ID. | BIGSERIAL NOT NULL |
| `table_id` | The ID of the corresponding table. | BIGSERIAL NOT NULL |
| `name` | The name of the column. | TEXT NOT NULL |
| `type` | Column type (for example, `STRING`). | TEXT NOT NULL |
| `connector_id` | The ID of the connection for which metadata is collected. _Deprecated_ and replaced by `connection_id`. | STRING |
| `connection_id` | The ID of the connection for which metadata is collected. | STRING |
| `destination_id` | The ID of the destination for which metadata is collected. | STRING |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |
| `updated_at` | Modification timestamp. | TIMESTAMPTZ NOT NULL |

### SOURCE_FOREIGN_KEY table[](https://fivetran.com/docs/logs/fivetran-platform#sourceforeignkeytable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `id` | Foreign key ID. | BIGSERIAL NOT NULL |
| `column_id` | The ID of the corresponding column. | BIGSERIAL NOT NULL |
| `ordinal` | The ordinal position of the column in the foreign key. | INTEGER |
| `foreign_key_reference` | String representation of the foreign key. | STRING NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |
| `updated_at` | Modification timestamp. | TIMESTAMPTZ NOT NULL |

### SCHEMA_LINEAGE table[](https://fivetran.com/docs/logs/fivetran-platform#schemalineagetable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `source_schema_id` | The ID of the corresponding source schema. | SERIAL NOT NULL |
| `destination_schema_id` | The ID of the corresponding destination schema. | SERIAL NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### TABLE_LINEAGE table[](https://fivetran.com/docs/logs/fivetran-platform#tablelineagetable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `source_table_id` | The ID of the corresponding source table. | BIGSERIAL NOT NULL |
| `destination_table_id` | The ID of the corresponding destination table. | BIGSERIAL NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

### COLUMN_LINEAGE table[](https://fivetran.com/docs/logs/fivetran-platform#columnlineagetable)

| Column Name | Description | Data Type |
| --- | --- | --- |
| `source_column_id` | The ID of the corresponding source column. | BIGSERIAL NOT NULL |
| `destination_column_id` | The ID of the corresponding destination column. | BIGSERIAL NOT NULL |
| `created_at` | Creation timestamp. | TIMESTAMPTZ NOT NULL |

To learn more about which queries you can use to check metadata, see our [Sample Queries page](https://fivetran.com/docs/logs/fivetran-platform/sample-queries#checkmetadata).

* * *

Error logs[](https://fivetran.com/docs/logs/fivetran-platform#errorlogs)
------------------------------------------------------------------------

These logs contain information about errors that connections encounter.You can track events, such as a failure or an authentication error from the logs.

The following table lists the errors with a `SEVERE` severity level:

| SEVERITY | EVENT_TYPE | PROPERTY_NAME | VALUE |
| --- | --- | --- | --- |
| SEVERE | status | status | FAILURE |
| SEVERE | status | status | FAILURE_WITH_TASK |
| SEVERE | error | type | dynamically obtained from response |
| SEVERE | error | type | open_file |
| SEVERE | error | type | null_primary_key |
| SEVERE | error | type | authentication_error |
| SEVERE | error | type | permission_denied |

* * *

Destination queries[](https://fivetran.com/docs/logs/fivetran-platform#destinationqueries)
------------------------------------------------------------------------------------------

You can query the data in your destination using simple SQL queries.For example, to track schema and table changes in your destination, query the `LOG` table for the following events:

*   `create_schema`
*   `create_table`
*   `drop_table`
*   `alter_table`

To learn more about the queries you can use, see our [Sample Queries page](https://fivetran.com/docs/logs/fivetran-platform/sample-queries).

### Sample query format[](https://fivetran.com/docs/logs/fivetran-platform#samplequeryformat)

```
SELECT * FROM project_id.schema_name.table_name
```

In this example,

*   `project_id` is your destination's project ID. To find the project ID, on your Fivetran dashboard, go to the **Destination** section.
*   `schema_name` is the destination schema name you chose while configuring your connection. The default is `fivetran_log`.
*   `table_name` is the name of the table you want to query. For example, `LOG`.

Thanks for your feedback!

Was this page helpful?
