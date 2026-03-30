# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/feature-views.md

# Working with feature views

> **Note:**
>
> The Snowflake Feature Store API is available in the Snowpark ML Python package (`snowflake-ml-python`) v1.5.0 and later.

A *feature view* encapsulates the transformation of raw data into one or more related *features.* All features in a
feature view are refreshed on the same schedule. Feature stores are backed by a *feature table* that stores the features.

The Snowflake Feature Store supports two different kinds of feature views:

* Snowflake-managed feature view: The feature table is automatically
  refreshed from raw data by Snowflake on a schedule you specify. A feature view is considered Snowflake-managed if you
  provide a schedule for refreshing it.
* External feature view: If you don’t provide a schedule for
  refreshing the feature view, it’s considered external. You are responsible for maintaining the feature table,
  updating features from raw data as needed, for example using a tool such as [dbt](https://www.getdbt.com/).

The class `snowflake.ml.feature_store.FeatureView` is the Python API for interacting with feature views. The
`FeatureView` constructor accepts a Snowpark DataFrame that contains the feature generation logic. The provided
DataFrame must also contain the `join_keys` columns specified in the entities associated with the feature view. A
timestamp column name is required if your feature view includes time-series features.

See the [Feature Store API Reference](https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/feature_store)
for full details of the Python API.

## Creating a Snowflake-managed feature view

A Snowflake-managed feature view uses a [dynamic table](../../../user-guide/dynamic-tables-about.md) as the feature table.
Features are extracted from the source data on a schedule you specify, handling new data efficiently and incrementally.
The illustration below shows the flow of data from its source, through feature transformations, into a feature table.

To create a Snowflake-managed feature view, use code like the following Python block, where `entity` is the
[entity](entities.md) that the features are associated with, and `my_df` is the Snowpark DataFrame that contains
your feature transformation logic based on your source data.

Setting the `refresh_freq` parameter designates the feature view as Snowflake-managed. The value can be a time delta
(minimum value `1 minute`), or it can be a `cron` expression with time zone (e.g. `* * * * * America/Los_Angeles`).

```python
from snowflake.ml.feature_store import FeatureView

managed_fv = FeatureView(
    name="MY_MANAGED_FV",
    entities=[entity],
    feature_df=my_df,                   # Snowpark DataFrame containing feature transformations
    timestamp_col="ts",                 # optional timestamp column name in the dataframe
    refresh_freq="5 minutes",           # how often feature data refreshes
    desc="my managed feature view"      # optional description
)
```

You can write feature transformations using Snowpark Python or in SQL. The Snowpark Python API provides
[utility functions](https://docs.snowflake.com/developer-guide/snowpark/reference/python/latest/snowpark/api/snowflake.snowpark.DataFrameAnalyticsFunctions)
for defining common feature types such as windowed aggregations. See [Common feature and query patterns](examples.md) for examples of using
these functions.

To qualify for incremental refresh, each source table must have [change tracking enabled](../../../user-guide/dynamic-tables-create.md).
If change tracking is not already enabled on a source table, Snowflake attempts to enable it automatically when creating
the feature view’s dynamic table. This requires OWNERSHIP of the table. If you do not own the table, ask the owner to
enable change tracking, or create the feature view with `refresh_mode='FULL'`, which fully reads the source table
for each refresh.

## Creating an external feature view

Features generated outside of the Snowflake Feature Store can be registered by setting the `refresh_freq`
parameter to `None` when creating them. In this situation, you must create and maintain the feature table
yourself. The feature DataFrame is based on the feature table, not on the raw data source, and usually contains a simple
projection from this table, with no transformations.

> **Note:**
>
> You *can* perform feature transformations in the feature DataFrame; these calculations are carried out as needed when you
> retrieve data from the feature view. However, external feature views are primarily intended for use with tools such
> as [dbt](https://www.getdbt.com/) that you already use to perform feature transformations. Generally, you should use
> Snowflake-managed feature views if you want Snowflake to perform
> feature transformation.

The illustration below shows the flow of data from its source, through feature transformation by an external tool (here
dbt), into a feature table.

External feature views are implemented as [views](../../../user-guide/views-introduction.md) on your feature table, so they
incur no additional storage cost.

The code below shows how to create an external feature view.

```python
external_fv = FeatureView(
    name="MY_EXTERNAL_FV",
    entities=[entity],
    feature_df=my_df,                   # Snowpark DataFrame referencing the feature table
    timestamp_col="ts",                 # optional timestamp column name in the dataframe
    refresh_freq=None,                  # None means the feature view is external
    desc="my external feature view"     # optional description
)
```

## Making feature views more discoverable

Adding per-feature descriptions to the `FeatureView` makes it easier to find features using
[Snowsight Universal Search](../../../user-guide/ui-snowsight-universal-search.md). The following example uses a feature view’s
`attach_feature_desc` method to provide a short description of each included feature in a Python dictionary:

```python
external_fv = external_fv.attach_feature_desc(
    {
        "SENDERID": "Sender account ID for the transaction",
        "RECEIVERID": "Receiver account ID for the transaction",
        "IBAN": "International Bank Identifier for the receiver bank",
        "AMOUNT": "Amount of the transaction"
    }
)
```

Both kinds of feature views can be enriched with feature descriptions.

## Registering feature views

Once a feature view has been completely defined, you can register it in the feature store using the feature store’s
`register_feature_view` method, with a customized name and version. Incremental maintenance (for supported query
types) and automatic refresh occur based on the specified refresh frequency.

When the provided query cannot be maintained via incremental maintenance using a dynamic table, the table will be fully
refreshed from the query at the specified frequency. This may lead to greater lag in feature refresh and higher
maintenance costs. You can alter the query logic, breaking the query into multiple smaller queries that support
incremental maintenance, or provision a larger virtual warehouse for dynamic table maintenance. See
[General limitations](../../../user-guide/dynamic-tables-limitations.md) for the latest information on dynamic table limitations.

```python
registered_fv: FeatureView = fs.register_feature_view(
    feature_view=managed_fv,    # feature view created above, could also use external_fv
    version="1",
    block=True,         # whether function call blocks until initial data is available
    overwrite=False,    # whether to replace existing feature view with same name/version
)
```

A feature view pipeline definition is immutable after it has been registered, providing consistent feature computation as
long as the feature view exists.

## Retrieving feature views

Once a feature view has been registered with the feature store, you can retrieve it from there when you need it by using
the feature store’s `get_feature_view` method:

```python
retrieved_fv: FeatureView = fs.get_feature_view(
    name="MY_MANAGED_FV",
    version="1"
)
```

## Discovering feature views

You can list all registered feature views in the feature store, optionally filtering by entity name or feature view
name, using the `list_feature_views` method. Information about the matching features is returned as a Snowpark
DataFrame. The following code shows an example of getting a list of feature views; `fs` is a reference to the
feature store.

```python
fs.list_feature_views(
    entity_name="<entity_name>",                # optional
    feature_view_name="<feature_view_name>",    # optional
).show()
```

Features can also be discovered using the Snowsight Feature Store UI or Universal Search.

## Updating feature views

You can update some properties of a feature view you have registered in the feature store using the feature store’s
`update_feature_view` method. The updatable properties are:

* The feature view’s refresh frequency
* The warehouse where the feature transforms execute
* The description of the feature view

Feature definitions and columns cannot be modified. To change the features in a feature store, create a new version of
the feature view.

When you call `update_feature_view`, specify the feature view version to be updated by providing its name and
version. The additional parameters specify the properties to be updated; you can specify just the ones you want to
change. The following code shows an example of changing feature view properties; `fs` is a reference to the
feature store.

```python
fs.update_feature_view(
    name="<name>",
    version="<version>",
    refresh_freq="<new_fresh_freq>",    # optional
    warehouse="<new_warehouse>",        # optional
    desc="<new_description>",           # optional
)
```

## Deleting feature views

You can delete a feature view from the feature store with the feature store’s `delete_feature_view` method. The
following code shows an example of deleting a feature view; `fs` is a reference to the feature store.

```python
fs.delete_feature_view(
    feature_view="<name>",
    version="<version>",
)
```

> **Warning:**
>
> Deleting a feature view version breaks any pipelines that use it. Make sure the feature view version is not in use
> before deleting it.

## Cost considerations

Snowflake-managed feature views use Snowflake dynamic tables. See [Monitor dynamic tables](../../../user-guide/dynamic-tables-monitor.md) for information
on monitoring dynamic tables and [Understanding costs for dynamic tables](../../../user-guide/dynamic-tables-cost.md) for information on the costs of dynamic tables.
External feature views use views, which do not incur additional storage costs.

## Known limitations

* The maximum number of Snowflake-managed feature views and the feature transformation queries in feature views are subject to the
  [limitations of dynamic tables](../../../user-guide/dynamic-tables-limitations.md).
* Not all feature transformation queries are supported by dynamic incremental refresh.
  [See the limitations](../../../user-guide/dynamic-tables-limitations.md).
* Feature view names are SQL identifiers and subject to [Snowflake identifier requirements](../../../sql-reference/identifiers-syntax.md).
* Feature view versions are strings and have a maximum length of 128 characters. Some characters are not permitted and will
  produce an error message.
