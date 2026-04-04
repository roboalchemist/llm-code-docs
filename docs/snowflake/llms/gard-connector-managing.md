# Source: https://docs.snowflake.com/en/connectors/google/gard/gard-connector-managing.md

# Managing the Snowflake Connector for Google Analytics Raw Data

This topic describes typical tasks you might need to perform after installing and configuring the connector.

## Changing the ingestion interval for the connector

The connector periodically checks and downloads data from BigQuery. The check is done every 8 hours by default, but it can be changed. If you want to set the new interval
for checking and downloading data, please use the `CONFIGURE_INGESTION_INTERVAL` procedure defined in the `PUBLIC` schema:

```sqlsyntax
CALL CONFIGURE_INGESTION_INTERVAL(<interval_configuration_name>)
```

Possible interval configurations along with cron definitions which are used under the hood:

```none
EVERY_15_MINUTES   -   */15 * * * * UTC
EVERY_30_MINUTES   -   */30 * * * * UTC
EVERY_1_HOUR       -   0 * * * * UTC
EVERY_4_HOURS      -   0 3/4 * * * UTC
EVERY_8_HOURS      -   0 3/8 * * * UTC
EVERY_1_DAY        -   0 3 * * * UTC
```

> **Note:**
>
> It is not possible to set custom cron expression.

Example usage:

```sqlsyntax
CALL CONFIGURE_INGESTION_INTERVAL('EVERY_1_HOUR')
```

The list of supported intervals can be also printed using the `LIST_SUPPORTED_INGESTION_INTERVALS` procedure defined in the `PUBLIC` schema:

```sqlsyntax
CALL LIST_SUPPORTED_INGESTION_INTERVALS()
```

## Setting up alerts

To set up alerts, do the following:

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md) as a user with the ACCOUNTADMIN role.
2. In the navigation menu, select Catalog » Apps.
3. Search for the Snowflake Connector for Google Analytics Raw Data, then select the tile for the connector.
4. In the page for the Snowflake Connector for Google Analytics Raw Data, go to the Settings section and then select Email alerts from the menu on the left.

   This displays a page for the email alerts configuration.
5. In the Email Address field, provide a Snowflake verified email address.

> **Note:**
>
> You must specify an email address that is associated with the Snowflake account.

1. In the Email Frequency field, select how often you would like to receive alerts:

* Immediately - you will receive notifications according to the values set in table synchronization.
* Once per day - you will receive notifications once a day at 12PM UTC.

> **Note:**
>
> Alerts are sent only when an invalid action (such as an error) occurs.

1. Select Save changes to start receiving email alerts.

### Disabling alerts

To stop receiving alerts, select Stop receiving alerts in the email alerts configuration page.

## Upgrading the connector

The connector upgrades are managed automatically by the provider of the application.

## Scaling the Connector

You should start your work with the Connector using a `X-Small` as it will most likely give you a sufficient performance.
However, if you are experiencing any Connector slowdowns, you may want to try gradually increasing the warehouse size and evaluating
whether you see any performance boosts at each step. Whether the Connector gains anything from scaling the warehouse depends on
a few factors, such as the number of properties or the amount of data each of them has.

For insights on how to resize the warehouse see Resizing a warehouse in [Working with warehouses](../../../user-guide/warehouses-tasks.md).

> **Note:**
>
> If you are constantly experiencing ingestion errors related to insufficient memory and are already using a `LARGE` or `X-LARGE`
> warehouse, then you can try to resolve this issue by decreasing the `MAX_CONCURRENCY_LEVEL` parameter on a warehouse from 8 (default) to 4.

## Changing the warehouse for the Connector

It is possible to change the warehouse that the Snowflake Connector for Google Analytics Raw Data uses for its internal tasks without reinstalling the connector.
First, make sure that the Connector is paused. It can be done eiter via UI or using the `PAUSE_CONNECTOR` procedure.
Then, you need to grant the Connector access to the new warehouse:

```sqlsyntax
GRANT USAGE ON WAREHOUSE <new_warehouse_name> TO APPLICATION snowflake_connector_for_google_analytics_raw_data;
```

After the access is granted, execute the `UPDATE_WAREHOUSE` procedure defined in the `PUBLIC` schema:

```sqlsyntax
CALL UPDATE_WAREHOUSE('<new_warehouse_name');
```

## Re-authentication of the Connector

In order to change the secret, external access integration or the security integration used by the connector without re-installation,
you need to execute the `UPDATE_CONNECTION` procedure defined in the `PUBLIC` schema.
Ensure, that all of the new objects are defined as described in [Configuring the Snowflake Connector for Google Analytics Raw Data using SQL](gard-connector-configuring-sql.md) and that the connector has all of the required grants.

```sqlsyntax
CALL UPDATE_CONNECTION('<new external access integration>', '<new secret>', '<new security integration>');
```

## Automatically disabling inaccessible Google Analytics properties

The Connector has a mechanism to automatically disable inaccessible Google Analytics properties in order to prevent unnecessary
costs caused by attempting ingestions for data which does not exist indefinitely and alarm you that data is not being ingested anymore.
The property is considered inaccessible and might be automatically disabled if data ingestions have been failing for the last 7 days.

## Proceeding during disaster recovery and failover

If you want to ensure that the connector will be able to continue data ingestion during a deployment outage, you need to
set up the sink database failover to a replica account. For details, see [Failing over databases across multiple accounts](../../../user-guide/database-failover-config.md).

Moreover, after an outage you need to manually install the Snowflake Connector for Google Analytics Raw Data on your replica account, because the connector itself can not be replicated.
After the installation it will synchronize itself with the replicated sink database.

> **Note:**
>
> In order to prevent data corruption you can not have two connector instances, one on a primary account and one on a replica account
> ingesting data to the sink database at the same time.

When a deployment outage occurs and your sink database fails over to a replica account, perform the following steps:

1. Sign in to your secondary account, where the sink database is replicated.
2. Install the Snowflake Connector for Google Analytics Raw Data on your secondary account. The connector will synchronize itself with the replicated sink database. The instance
   on your primary account goes into a read-only state after an outage, so data will not be corrupted at this point.
3. If you want to go back to the primary account after the deployment is available again, you need to first drop both connectors. It’s necessary to ensure a consistent connector state.
4. Replicate the data back from the secondary account to the primary one using the replication mechanism.
5. Reinstall the connector on a primary account once the data in sink table synchronizes with the sink table on your secondary account.

## Updating data ingestion options

You can use the `UPDATE_INGESTION_OPTIONS` procedure defined in the `PUBLIC` schema to modify default ingestion options
for certain properties. This procedure allows you to change the following:

> * `EXCLUDE_NULLS` - Remove fields containing null values from the ingested data. Setting this value to `TRUE`
>   can improve the data ingestion throughput. The default value is `FALSE`.
> * `DISABLE_AUTO_RELOADS` - Disables auto reloading data. For more details about auto reload see [Data ingestion model for the Snowflake Connector for Google Analytics Raw Data](gard-connector-data-ingestion-model.md).
>   Setting this value to `TRUE` can reduce credit consumption, but late data won’t be ingested into Snowflake. This property
>   cannot be set to `true` for the `FRESH_DAILY` export type. The default value is `FALSE`.
> * `ENABLED_EXPORT_TYPES` - A list of export types, which connector will try to ingest data for. Possible values are: `DAILY`, `FRESH_DAILY`, `INTRADAY`, `USERS` and `PSEUDONYMOUS_USERS`.

```sqlsyntax
CALL UPDATE_INGESTION_OPTIONS(
    PROPERTY_IDS => ['<property_1>', '<property_2>'],
    EXCLUDE_NULLS => <boolean>,
    ENABLED_EXPORT_TYPES => ['DAILY', 'FRESH_DAILY' 'INTRADAY', 'USERS', 'PSEUDONYMOUS_USERS']
 );
```

> **Note:**
>
> To leave an ingestion option unchanged, omit the argument from the
> `UPDATE_INGESTION_OPTIONS` procedure call.

## Refreshing flattened views on demand

You can use the `REFRESH_VIEWS` procedure defined in the `PUBLIC` schema to trigger an on-demand refresh of the flattened views.
The flattened views are refreshed automatically daily by default.
For more details about views see [Accessing data ingested by Snowflake Connector for Google Analytics Raw Data](gard-connector-accessing-data.md).

```sqlsyntax
CALL REFRESH_VIEWS();
```
