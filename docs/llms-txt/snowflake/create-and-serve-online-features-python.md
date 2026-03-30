# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/create-and-serve-online-features-python.md

# Create and serve online features

Create and serve online features for latency-sensitive machine learning inference workflows. Enable online features on a feature view that you’re creating or update an existing feature view to enable online serving.

> **Important:**
>
> You must have Snowflake version 9.26 or later and `snowflake-ml-python` version 1.18.0 to use online feature serving.

Online feature serving provides the following benefits:

* Low-latency point lookups for real-time inference
* Automatic data synchronization from offline sources
* Fully managed infrastructure and maintenance
* Elastic scaling for demanding workloads

Online feature serving is backed by [online feature tables](../../../sql-reference/commands-feature-store.md).

## Data freshness

A feature view with online feature serving automatically synchronizes data from the offline store.

Use the `target_lag` parameter to configure how often data is synchronized to your online feature table. You can set this value from a minimum of 10 seconds to a maximum of 8 days.

The online feature tables are refreshed in the background using the value that you’ve specified. The online feature table is suspended if there are five consecutive refresh failures.
For information about troubleshooting the refresh failure, check your refresh history.

## Refresh modes

Snowflake uses the following refresh modes to update the data:

* Incremental Refresh: This is the preferred and most efficient mode. Snowflake tracks changes in the sources and merges only the new or updated rows into the online store. This minimizes compute and I/O costs.
* Full Refresh: This mode drops all existing data in the table and reloads everything from the source. It is more resource-intensive and is used when an incremental refresh is not possible.

You can explicitly set the refresh mode to INCREMENTAL or FULL, or set it to AUTO to let Snowflake determine the most efficient available refresh mode.

## Time series data handling

To ensure data consistency, you can specify a `timestamp_col`. When multiple rows with the same primary key are found in the source, Snowflake only ingests the version with the most recent timestamp. If you don’t specify a timestamp column, the most recently processed row takes precedence.

### Provide access to create and serve online features

Before you get started with using the online feature store, you must provide the necessary permissions to the relevant roles.

To provide permissions, use the access control script described in [Access control setup in SQL](rbac.md). After you’ve run the script, grant the following privileges:

```sqlexample
GRANT CREATE ONLINE FEATURE TABLE ON SCHEMA IDENTIFIER($SCHEMA_FQN) TO ROLE IDENTIFIER($FS_ROLE_PRODUCER);

GRANT SELECT, MONITOR ON FUTURE ONLINE FEATURE TABLES IN SCHEMA IDENTIFIER($SCHEMA_FQN) TO ROLE IDENTIFIER($FS_ROLE_CONSUMER);

GRANT SELECT, MONITOR ON ALL ONLINE FEATURE TABLES IN SCHEMA IDENTIFIER($SCHEMA_FQN) TO ROLE IDENTIFIER($FS_ROLE_CONSUMER);
```

### Manage and serve online features using the Python API

The following example shows how to configure online feature serving when creating a new feature view. You can use the `OnlineConfig` object to specify the online serving settings, such as the target data freshness lag.

```python
from snowflake.ml.feature_store import FeatureView
from snowflake.ml.feature_store.feature_view import OnlineConfig

online_config = OnlineConfig(enable=True, target_lag="30 seconds")

fv = FeatureView(
    name="MY_FV",
    entities=[entity],
    feature_df=my_df, # Snowpark DataFrame containing feature transformations
    timestamp_col="ts", # optional timestamp column name in the dataframe
    refresh_freq="5 minutes",
    refresh_mode="AUTO", # refresh mode of the feature data
    desc="my feature view", # optional description
    online_config=online_config
)

fv = fs.register_feature_view(feature_view=fv, version="v1")
```

The following are the `OnlineConfig` parameters:

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| enable | Boolean, optional | Specifies whether online feature serving should be enabled for the feature view. | Default: False |
| target_lag | Str, optional | String in a “<num> (seconds|minutes|hours|days|s|m|h|d)” format specifying the target data freshness lag. | Default: 10 seconds |

> **Note:**
>
> `refresh_freq` and `OnlineConfig.target_lag` act independently.
> In the example above, the effective target data propagation lag from the source data represented by `my_df` to the online data store will be `refresh_freq + online_config.target_lag`.

## Update a feature view to enable/disable online feature serving

For existing feature views, you can update the online feature serving configuration using the `update_feature_view` method.
You can use this method to enable online feature serving for existing feature views.

Use the following code to enable online feature serving.

```python
# Enable online feature serving

fs.update_feature_view(
    name="<name>",
    version="<version>",
    online_config=OnlineConfig(enable=True, target_lag="5 minutes")
)
```

Use the following code to disable online feature serving.

```python
# Disable online feature serving

fs.update_feature_view(
    name="<name>",
    version="<version>",
    online_config=OnlineConfig(enable=False)
)
```

## Retrieve features from online storage

To retrieve feature values from online storage for a given sample, use the `read_feature_view` method and pass the list of feature names as well as the join keys of the sample:

```python
fs.read_feature_view(
    feature_view=fv,
    keys=[["<k_1>", "<k_2>"]],
    feature_names=["<feature1>", "<feature2>", "<feature3>"],
    store_type=StoreType.ONLINE
)
```

## Suspend/resume online data refresh

Use the following code to temporarily suspend data refresh.

```python
fs.suspend_feature_view(feature_view=fv)
```

Use the following code to resume data refresh.

```python
fs.resume_feature_view(feature_view=fv)
```

These operations suspend/resume both the offline feature view (dynamic table and associated task) and the online feature table (if it exists) to ensure consistent state across all storage types.

## Manually refresh feature view

```python
fs.refresh_feature_view(
    feature_view=fv,
    store_type=<store_type>
)
```

The `store_type` argument specifies whether to refresh offline (`StoreType.OFFLINE`) or online (`StoreType.ONLINE`) feature data.

## View refresh history

```python
fs.get_refresh_history(
    feature_view=fv,
    store_type=store_type
)
```

The `store_type` argument specifies whether to return the offline (`StoreType.OFFLINE`) or online (`StoreType.ONLINE`) store refresh history.

### Understanding costs

Online Feature Tables incur costs across the following consumption modes:

* **Virtual warehouse compute**: Both key lookups and data ingestion operations consume virtual warehouse credits at standard rates. For more information, see [Virtual warehouse credit usage](../../../user-guide/cost-understanding-compute.md).
* **Cloud Services Compute**: Required to identify changes in underlying base objects and determine when refresh operations are needed. For more information, see [Cloud service credit usage](../../../user-guide/cost-understanding-compute.md).
* **Hybrid Table Storage**: Storage costs based on flat monthly rate per GB. It’s more expensive than the cost for traditional Snowflake storage, but identical to the cost to store hybrid tables. For more information, see Table 3(b) in the [Credit Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
* **Hybrid Table Requests**: These requests use [Serverless credit usage](../../../user-guide/cost-understanding-compute.md) for read/write operations to row storage clusters. The amount of data that is written to or read from these clusters is used to calculate the credit consumption, with a minimum 4 KB usage per operation. Credits are also consumed for the compute resources used to perform background operations, such as compaction. For more information, see Table 5 in the [Credit Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

> **Tip:**
>
> Incremental refresh can help reduce costs. Incremental updates are generally more cost-efficient than full refresh, resulting in lower compute and data ingestion costs.

## Cost monitoring

To monitor costs, use these views:

```sqlexample
-- Hybrid table request credits
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.HYBRID_TABLE_USAGE_HISTORY;

-- Storage consumption
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.STORAGE_USAGE;
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY;

-- Overall costs
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY;
```
