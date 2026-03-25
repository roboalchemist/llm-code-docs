# Source: https://docs.snowflake.com/en/user-guide/cost-exploring-compute.md

# Exploring compute cost

Total compute cost consists of the overall use of:

* Virtual warehouses (user-managed compute resources)
* Serverless features such as Automatic Clustering and Snowpipe that use Snowflake-managed compute resources
* Cloud services layer of the Snowflake architecture
* vCPU usage for [Openflow BYOC cost and scaling considerations](data-integration/openflow/cost-byoc.md) and [Openflow Snowflake Deployment cost and scaling considerations](data-integration/openflow/cost-spcs.md).
  See [Openflow components](data-integration/openflow/about.md) for more information about Openflow components including runtimes.

This topic describes how to gain insight into historical compute costs using [Snowsight](ui-snowsight-gs.md), or by writing queries against views in
the [ACCOUNT_USAGE](../sql-reference/account-usage.md) and [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schemas.
Snowsight allows you to quickly and easily obtain information about cost from a visual dashboard. Queries against the usage views
allow you to drill down into cost data and can help generate custom reports and dashboards.

If you need more information about how compute costs are incurred, refer to [Understanding compute cost](cost-understanding-compute.md).

> **Note:**
>
> The cloud services layer consumes credits, but not all of those credits are actually billed. Usage for cloud services is charged only if
> the daily consumption of cloud services exceeds 10% of the daily usage of virtual warehouses. Snowsight and a majority of views
> show the total number of credits consumed by warehouses, serverless features, and cloud services without accounting for this daily
> adjustment to cloud services.
>
> To determine how many credits were actually billed for compute costs, run queries against the
> [METERING_DAILY_HISTORY view](../sql-reference/account-usage/metering_daily_history.md).

## Viewing credit usage

All compute resources (virtual warehouses, serverless, cloud services) consume Snowflake credits. Users can use Snowsight to
view the overall cost of compute usage for any given day, week, or month.

To explore compute cost:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role with [access to cost and usage data](cost-access-control.md).
3. In the navigation menu, select Admin » Cost management.
4. Select a warehouse to use to view the usage data. Snowflake recommends using an XS warehouse for this purpose.
5. Select Consumption.
6. Select Compute from the Usage Type drop-down.

For usage notes related to the Consumption page, see [Usage notes](cost-exploring-overall.md).

### Filter by tag

You can use tags to [attribute the cost](cost-attributing.md) of using resources to a logical
unit within your organization. A tag is a Snowflake object that can have one or more values associated with it. A user with the
appropriate privileges applies a tag/value pair to each resource that is used by a cost center or other logical unit (e.g. the Development
environment, a business unit, or business line). Once resources have been tagged, you can isolate costs based on a
specific tag/value pair, allowing you to attribute this cost to a specific logical unit.

To filter the Consumption dashboard to show costs associated with a specific tag/value combination:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role with [access to cost and usage data](cost-access-control.md).
3. In the navigation menu, select Admin » Cost management.
4. Select a warehouse to use to view the usage data. Snowflake recommends using an XS warehouse for this purpose.
5. Select Consumption.
6. Select Compute from the Usage Type drop-down.
7. From the Tags drop-down, select the tag.
8. Select the value from the list of the tag’s values.
9. Select Apply.

For example, you can use the drop-down to select the `COST_CENTER` tag and the `SALES` value to show usage associated with resources
tagged with `COST_CENTER = SALES` while excluding all other usage from the dashboard.

You can also display all resources with a tag regardless of their tag value. Use the drop down to select a
tag, then choose All instead of a specific value.

### View consumption by type, service, or resource

When viewing the bar graph that displays compute history, you can filter the data By Type, By Service or By Resource.

> By Type:
> :   Separates resource consumption into compute (virtual warehouses and serverless resources) and cloud services. For the purpose
> of this filter, cloud services is separated out from the other types of compute resources.
>
> By Service:
> :   Separates resource consumption into warehouse consumption and consumption by each serverless feature. For example,
> WAREHOUSE_METERING represents credits consumed by warehouses while PIPE represents credits consumed by the serverless Snowpipe feature.
> Cloud services compute is included in warehouse consumption.
>
> By Resource:
> :   Separates resource consumption by the Snowflake object that consumed credits. For example, each warehouse is represented,
> as is every table that incurred serverless costs.

## Querying data for compute cost

Snowflake provides two schemas, [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) and
[ACCOUNT_USAGE](../sql-reference/account-usage.md), that contain data related to usage and cost. The ORGANIZATION_USAGE schema provides
cost information for all of the accounts in the organization while the ACCOUNT_USAGE schema provides similar information for a single
account. Views in these schemas provide granular, analytics-ready usage data to build custom reports or dashboards.

Most views in the ORGANIZATION_USAGE and ACCOUNT_USAGE schemas contain the cost of compute resources in terms of
[credits](cost-understanding-compute.md) consumed. To explore compute cost in currency, rather than credits, write queries against the
[USAGE_IN_CURRENCY_DAILY view](../sql-reference/organization-usage/usage_in_currency_daily.md). This view converts credits consumed into cost in currency using the daily
price of a credit.

### General cost views

The following views contain information related to the compute costs of all Snowflake features. You can focus on a particular feature by filtering on the `service_type` column.

For additional views that focus on the cost of a specific feature, see Feature-specific cost views.

| View | Compute resource | Description | Schema |
| --- | --- | --- | --- |
| METERING_DAILY_HISTORY | Warehouses  Serverless  Cloud Services  Openflow runtimes | Credits consumed by all compute resources (warehouses, serverless, cloud services and Openflow) in a given day.  Can be used to determine whether cloud services compute costs were actually billed for a specific day (that is, cloud services credit consumption exceeded 10% of warehouse consumption). | [ORGANIZATION_USAGE](../sql-reference/organization-usage/metering_daily_history.md) [ACCOUNT_USAGE](../sql-reference/account-usage/metering_daily_history.md) |
| METERING_HISTORY | Warehouses  Serverless  Cloud Services  Openflow runtimes | Credits consumed by warehouses, cloud services, serverless, and Openflow features on an hourly basis. To see how many credits an individual warehouse is consuming, query the WAREHOUSE_METERING_HISTORY view. | [ACCOUNT_USAGE](../sql-reference/account-usage/metering_history.md) |
| [USAGE_IN_CURRENCY_DAILY](../sql-reference/organization-usage/usage_in_currency_daily.md) | Warehouses  Serverless  Cloud Services | Daily credit consumption by all compute resources along with the cost of that usage in the organization’s currency. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/usage_in_currency_daily.md) |

### Feature-specific cost views

The following views that are dedicated to the usage and cost information for a specific feature.

| View | Compute resource | Description |
| --- | --- | --- |
| APPLICATION_DAILY_USAGE_HISTORY | Warehouses  Serverless  Cloud Services | Daily credit usage for Snowflake Native Apps in an account within the last 365 days. |
| ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY | Serverless | Bytes retrieved from archive storage for storage lifecycle policies. See [Billing for storage lifecycle policies](storage-management/storage-lifecycle-policies-billing.md) for more information. |
| AUTOMATIC_CLUSTERING_HISTORY | Serverless | Credits consumed by automatic clustering. |
| CATALOG_LINKED_DATABASE_USAGE_HISTORY | Serverless | Credits consumed by catalog-linked databases. |
| CORTEX_AI_FUNCTIONS_USAGE_HISTORY | Serverless | Credits consumed by Cortex AI Functions. |
| CORTEX_AGENT_USAGE_HISTORY | Serverless | Credits consumed by Cortex Agents. |
| CORTEX_ANALYST_ USAGE_HISTORY | Serverless | Credits consumed by Cortex Analyst. |
| CORTEX_FINE_TUNING_USAGE_HISTORY | Serverless | Credits consumed for Cortex Fine-tuning. |
| CORTEX_FUNCTIONS_ QUERY_USAGE_HISTORY | Serverless | Credits consumed to run queries that use Cortex LLM functions. |
| CORTEX_FUNCTIONS_ DOCUMENT_PROCESSING_USAGE_HISTORY | Serverless | Credits consumed to process documents with Document AI. |
| CORTEX_FUNCTIONS_ USAGE_HISTORY | Serverless | Credits consumed to call Cortex LLM functions. |
| CORTEX_REST_API_USAGE_HISTORY | Serverless | Credits consumed by Cortex REST API calls. |
| CORTEX_SEARCH_DAILY_USAGE_HISTORY | Serverless | Daily credits consumed for Cortex Search for serving and text embeddings |
| CORTEX_SEARCH_SERVING_USAGE_HISTORY | Serverless | Credits consumed for Cortex Search serving |
| DATA_QUALITY_MONITORING_USAGE_HISTORY | Serverless | Credits consumed to call scheduled DMFs and ingest results into an event table. |
| DATABASE_REPLICATION_USAGE_ HISTORY | Serverless | Credits consumed for database replication. |
| DOCUMENT_AI_ USAGE_HISTORY | Serverless | Credits consumed by Document AI. |
| HYBRID_TABLE_USAGE_HISTORY | Serverless | Credits consumed for Hybrid Table Requests resources. (As of March 1, 2026, hybrid table requests are no longer billed as a separate category.) |
| LISTING_AUTO_FULFILLMENT_REFRESH_DAILY | Warehouses | Credits used to refresh data fulfilled to other regions by Cross-Cloud Auto-Fulfillment. |
| LISTING_AUTO_FULFILLMENT_USAGE_HISTORY | Warehouses | Estimated usage associated with fulfilling data products to other regions by using Cross-Cloud Auto-Fulfillment. Refer to the SERVICE_TYPE of REPLICATION. |
| MATERIALIZED_VIEW_REFRESH_ HISTORY | Serverless | Credits consumed the refreshing of materialized views. |
| OPENFLOW_USAGE_HISTORY | Openflow | Credits consumed by Openflow runtimes. This view is available in the ACCOUNT_USAGE schema only. |
| PIPE_USAGE_HISTORY | Serverless | Credits consumed by Snowpipe. |
| QUERY_ACCELERATION_HISTORY | Serverless | Credits consumed by the query acceleration service. |
| QUERY_ATTRIBUTION_HISTORY | Warehouses | Credits consumed [per query](cost-attributing.md) for warehouse usage. |
| REPLICATION_USAGE_HISTORY | Serverless | Credits consumed and number of bytes transferred during database replication. If possible, use the [DATABASE_REPLICATION_USAGE_HISTORY view](../sql-reference/account-usage/database_replication_usage_history.md) instead. |
| REPLICATION_GROUP_USAGE_ HISTORY | Serverless | Credits consumed and number of bytes transferred during replication for a specific replication group. |
| SEARCH_OPTIMIZATION_HISTORY | Serverless | Credits consumed by the search optimization service. |
| SERVERLESS_ALERT_HISTORY | Serverless | Credits consumed by serverless alerts. |
| SERVERLESS_TASK_HISTORY | Serverless | Credits consumed by serverless tasks. |
| SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY | Serverless | Credits consumed by Snowflake Intelligence. |
| SNOWPIPE_STREAMING_FILE_MIGRATION_HISTORY | Serverless | Credits consumed by Snowpipe Streaming compute (does not include client costs). |
| WAREHOUSE_METERING_HISTORY | Warehouses  Cloud Services | Hourly credit usage of each warehouse, including the cloud services cost associated with using the warehouse. |

> **Note:**
>
> The views and table functions of the [Snowflake Information Schema](../sql-reference/info-schema.md) also provide usage data related to cost. Though
> the ACCOUNT_USAGE schema is preferred, the Information Schema can be faster in some circumstances.

### Example queries

The following queries drill-down into data in ACCOUNT_USAGE views to gain insight into compute costs.

> **Note:**
>
> Queries executed against views in the Account Usage schema can be modified to gain insight into cost for the entire organization by
> using the corresponding view in the Organization Usage schema. For example, both schemas include a WAREHOUSE_METERING_HISTORY view.

Click the name of a query below to see the full SQL example.

Compute for Warehouses:
:   *Query: Average hour-by-hour Snowflake spend (across all warehouses) over the past m days
    * Query: Credit consumption by warehouse over specific time period
    *Query: Warehouse usage over m-day average
    * [Query: Warehouse cost attribution by query tag](cost-attributing.md).
    * [Query: Warehouse cost attribution by user](cost-attributing.md).

Compute for Cloud Services:
:   *Query: Billed cloud services
    * Query: Total cloud services cost by type of query
    *Query: Cloud services cost for queries of a given type
    * Query: Warehouses with high cloud services usage
    * Query: Cloud services cost sorted by portion of query time

Compute for Automatic Clustering:
:   *Query: Automatic Clustering cost history (by day, by object)
    * Query: Automatic Clustering History & m-day average

Compute for Search Optimization:
:   *Query: Search Optimization cost history (by day, by object)
    * Query: Search Optimization History & m-day average

Compute for Materialized Views:
:   *Query: Materialized Views cost history (by day, by object)
    * Query: Materialized Views History & m-day average

Compute for Query Acceleration Service:
:   * Query: Query Acceleration Service cost by warehouse

Compute for Snowpipe:
:   *Query: Cumulative usage of data ingest (Snowpipe and “Copy”)
    * Query: Snowpipe cost history (by day, by object)
    * Query: Snowpipe History & m-day average

Compute and client costs for Snowpipe Streaming:
:   * Query: Snowpipe Streaming cost

Compute for Serverless Alerts:
:   * Query: Total serverless alert cost

Compute for Serverless Tasks:
:   * Query: Total serverless task cost

Compute for Replication:
:   *Query: Account replication cost
    * Query: Database replication cost history (by day, by object)
    * Query: Database replication History & m-day average

Compute for Partner Tools:
:   * Query: Credit consumption by partner tools

Compute for Hybrid Tables:
:   * Query: Credit consumption by hybrid tables

Compute for Cortex Agents:
:   * Query: Credit consumption by Cortex Agents

Compute for Cortex Analyst:
:   * Query: Credit consumption by Cortex Analyst

Compute for Cortex Fine-tuning:
:   * Query: Credit consumption by Cortex Fine-tuning

Compute for Cortex functions:
:   *Query: Credit consumption by Cortex functions
    * Query: Credit consumption by Cortex functions query

Compute for Cortex Search:
:   *Query: Daily credit consumption by Cortex Search
    * Query: Credit consumption by Cortex Search serving

Compute for Document AI:
:   * Query: Credit consumption by Document AI

Compute for Snowflake Intelligence:
:   * Query: Credit consumption by Snowflake Intelligence

Compute for Snowflake Notebooks:
:   *Query: Hourly credit consumption by notebooks
    * Query: Cost to run a specific notebook
    *Query: Total compute pool cost per notebook
    * Query: Identify users who ran a specific notebook

#### Compute for warehouses

Query: Average hour-by-hour Snowflake spend (across all warehouses) over the past m days
:   This query shows the total credit consumption on an hourly basis to help understand consumption trends (peaks, valleys) over the past m
    days. This helps identify times of day when there are spikes in consumption.

    ```sqlexample
    SELECT start_time,
      warehouse_name,
      credits_used_compute
    FROM snowflake.account_usage.warehouse_metering_history
    WHERE start_time >= DATEADD(day, -m, CURRENT_TIMESTAMP())
      AND warehouse_id > 0  -- Skip pseudo-VWs such as "CLOUD_SERVICES_ONLY"
    ORDER BY 1 DESC, 2;

    -- by hour
    SELECT DATE_PART('HOUR', start_time) AS start_hour,
      warehouse_name,
      AVG(credits_used_compute) AS credits_used_compute_avg
    FROM snowflake.account_usage.warehouse_metering_history
    WHERE start_time >= DATEADD(day, -m, CURRENT_TIMESTAMP())
      AND warehouse_id > 0  -- Skip pseudo-VWs such as "CLOUD_SERVICES_ONLY"
    GROUP BY 1, 2
    ORDER BY 1, 2;
    ```

Query: Credit consumption by warehouse over specific time period
:   This query shows the total credit consumption for each warehouse over a specific time period. This helps identify warehouses that are
    consuming more credits than others and specific warehouses that are consuming more credits than anticipated.

    ```sqlexample
    -- Credits used (all time = past year)
    SELECT warehouse_name,
      SUM(credits_used_compute) AS credits_used_compute_sum
    FROM snowflake.account_usage.warehouse_metering_history
    GROUP BY 1
    ORDER BY 2 DESC;

    -- Credits used (past N days/weeks/months)
    SELECT warehouse_name,
      SUM(credits_used_compute) AS credits_used_compute_sum
    FROM snowflake.account_usage.warehouse_metering_history
    WHERE start_time >= DATEADD(day, -m, CURRENT_TIMESTAMP())
    GROUP BY 1
    ORDER BY 2 DESC;
    ```

Query: Warehouse usage over m-day average
:   This query returns the daily average credit consumption grouped by week and warehouse. It can be used to identify anomalies in credit
    consumption for warehouses across weeks from the past year.

    ```sqlexample
    WITH cte_date_wh AS (
      SELECT TO_DATE(start_time) AS start_date,
        warehouse_name,
        SUM(credits_used) AS credits_used_date_wh
      FROM snowflake.account_usage.warehouse_metering_history
      GROUP BY start_date, warehouse_name
    )

    SELECT start_date,
      warehouse_name,
      credits_used_date_wh,
      AVG(credits_used_date_wh) OVER (PARTITION BY warehouse_name ORDER BY start_date ROWS m PRECEDING) AS credits_used_m_day_avg,
      100.0*((credits_used_date_wh / credits_used_m_day_avg) - 1) AS pct_over_to_m_day_average
    FROM cte_date_wh
      QUALIFY credits_used_date_wh > 100  -- Minimum N=100 credits
        AND pct_over_to_m_day_average >= 0.5  -- Minimum 50% increase over past m day average
    ORDER BY pct_over_to_m_day_average DESC;
    ```

#### Compute for cloud services

Query: Billed cloud services
:   [Usage for cloud services](cost-understanding-compute.md) is billed only if the daily consumption of cloud
    services exceeds 10% of the daily usage of virtual warehouses. This query returns how much of cloud services consumption was actually
    billed for a particular day, ordered by the highest billed amount.

    ```sqlexample
    SELECT
        usage_date,
        credits_used_cloud_services,
        credits_adjustment_cloud_services,
        credits_used_cloud_services + credits_adjustment_cloud_services AS billed_cloud_services
    FROM snowflake.account_usage.metering_daily_history
    WHERE usage_date >= DATEADD(month,-1,CURRENT_TIMESTAMP())
        AND credits_used_cloud_services > 0
    ORDER BY 4 DESC;
    ```

Query: Total cloud services cost by type of query
:   This query returns the total credits consumed for cloud services by a particular type of query.

    ```sqlexample
    SELECT query_type,
      SUM(credits_used_cloud_services) AS cs_credits,
      COUNT(1) num_queries
    FROM snowflake.account_usage.query_history
    WHERE true
      AND start_time >= TIMESTAMPADD(day, -1, CURRENT_TIMESTAMP)
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10;
    ```

Query: Cloud services cost for queries of a given type
:   This query returns the total credits consumed for cloud services by all queries of a specific type. Replace `'COPY'` if you want to focus on a different type of query and `day` if you want to explore a longer or shorter period of time.

    ```sqlexample
    SELECT *
    FROM snowflake.account_usage.query_history
    WHERE true
      AND start_time >= TIMESTAMPADD(day, -1, CURRENT_TIMESTAMP)
      AND query_type = 'COPY'
    ORDER BY credits_used_cloud_services DESC
    LIMIT 10;
    ```

Query: Warehouses with high cloud services usage
:   This query shows the warehouses that are not using enough warehouse time to cover the cloud services portion of compute. This provides a
    launching point for additional investigation by isolating warehouses with a high ratio of cloud service use (>10% of overall credits).
    Investigation candidates include issues around cloning, listing files in S3, partner tools, setting session parameters, etc.

    ```sqlexample
    SELECT
      warehouse_name,
      SUM(credits_used) AS credits_used,
      SUM(credits_used_cloud_services) AS credits_used_cloud_services,
      SUM(credits_used_cloud_services)/SUM(credits_used) AS percent_cloud_services
    FROM snowflake.account_usage.warehouse_metering_history
    WHERE TO_DATE(start_time) >= DATEADD(month,-1,CURRENT_TIMESTAMP())
        AND credits_used_cloud_services > 0
    GROUP BY 1
    ORDER BY 4 DESC;
    ```

Query: Cloud services usage sorted by portion of query time
:   This query returns all queries run within the last minute and sorts them by parts of total query execution time (e.g. compilation time vs. queue time).

    ```sqlexample
    SELECT *
    FROM snowflake.account_usage.query_history
    WHERE true
      AND start_time >= TIMESTAMPADD(minute, -60, CURRENT_TIMESTAMP)
    ORDER BY compilation_time DESC,
      execution_time DESC,
      list_external_files_time DESC,
      queued_overload_time DESC,
      credits_used_cloud_services DESC
    LIMIT 10;
    ```

#### Compute for Automatic Clustering

Query: Automatic Clustering cost history (by day, by object)
:   This query provides a list of tables with Automatic Clustering and the volume of credits consumed via the service over the last 30 days,
    broken out by day. Any irregularities in the credit consumption or consistently high consumption are flags for additional investigation.

    ```sqlexample
    SELECT TO_DATE(start_time) AS date,
      database_name,
      schema_name,
      table_name,
      SUM(credits_used) AS credits_used
    FROM snowflake.account_usage.automatic_clustering_history
    WHERE start_time >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    GROUP BY 1,2,3,4
    ORDER BY 5 DESC;
    ```

Query: Automatic Clustering History & m-day average
:   This query shows the average daily credits consumed by Automatic Clustering grouped by week over the last year. It can help identify
    anomalies in daily averages over the year so you can investigate spikes or unexpected changes in consumption.

    ```sqlexample
    WITH credits_by_day AS (
      SELECT TO_DATE(start_time) AS date,
        SUM(credits_used) AS credits_used
      FROM snowflake.account_usage.automatic_clustering_history
      WHERE start_time >= DATEADD(year,-1,CURRENT_TIMESTAMP())
      GROUP BY 1
      ORDER BY 2 DESC
    )

    SELECT DATE_TRUNC('week',date),
          AVG(credits_used) AS avg_daily_credits
    FROM credits_by_day
    GROUP BY 1
    ORDER BY 1;
    ```

#### Compute for Search Optimization

Query: Search Optimization cost history (by day, by object)
:   This query provides a full list of tables with Search Optimization and the volume of credits consumed via the service over the last 30
    days, broken out by day. Any irregularities in the credit consumption or consistently high consumption are flags for additional
    investigation.

    ```sqlexample
    SELECT TO_DATE(start_time) AS date,
      database_name,
      schema_name,
      table_name,
      SUM(credits_used) AS credits_used
    FROM snowflake.account_usage.search_optimization_history
    WHERE start_time >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    GROUP BY 1,2,3,4
    ORDER BY 5 DESC;
    ```

Query: Search Optimization History & m-day average
:   This query shows the average daily credits consumed by Search Optimization grouped by week over the last year. It can help identify
    anomalies in daily averages over the year so you can investigate spikes or unexpected changes in
    consumption.

    ```sqlexample
    WITH credits_by_day AS (
      SELECT TO_DATE(start_time) AS date,
        SUM(credits_used) AS credits_used
      FROM snowflake.account_usage.search_optimization_history
      WHERE start_time >= DATEADD(year,-1,CURRENT_TIMESTAMP())
      GROUP BY 1
      ORDER BY 2 DESC
    )

    SELECT DATE_TRUNC('week', date),
      AVG(credits_used) as avg_daily_credits
    FROM credits_by_day
    GROUP BY 1
    ORDER BY 1;
    ```

#### Compute for Materialized Views

Query: Materialized Views cost history (by day, by object)
:   This query provides a full list of materialized views and the volume of credits consumed via the service over the last 30 days, broken
    out by day. Any irregularities in the credit consumption or consistently high consumption are flags for additional investigation.

    ```sqlexample
    SELECT TO_DATE(start_time) AS date,
      database_name,
      schema_name,
      table_name,
      SUM(credits_used) AS credits_used
    FROM snowflake.account_usage.materialized_view_refresh_history
    WHERE start_time >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    GROUP BY 1,2,3,4
    ORDER BY 5 DESC;
    ```

Query: Materialized Views History & m-day average
:   This query shows the average daily credits consumed by materialized views grouped by week over the last year. It can help identify
    anomalies in daily averages over the year so you can investigate spikes or unexpected changes in
    consumption.

    ```sqlexample
    WITH credits_by_day AS (
      SELECT TO_DATE(start_time) AS date,
        SUM(credits_used) AS credits_used
      FROM snowflake.account_usage.materialized_view_refresh_history
      WHERE start_time >= DATEADD(year,-1,CURRENT_TIMESTAMP())
      GROUP BY 1
      ORDER BY 2 DESC
    )

    SELECT DATE_TRUNC('week',date),
      AVG(credits_used) AS avg_daily_credits
    FROM credits_by_day
    GROUP BY 1
    ORDER BY 1;
    ```

#### Compute for Query Acceleration Service

Query: Query Acceleration Service cost by warehouse
:   This query returns the total number of credits used by each warehouse in your account for the query acceleration service
    (month-to-date):

    ```sqlexample
    SELECT warehouse_name,
           SUM(credits_used) AS total_credits_used
      FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ACCELERATION_HISTORY
      WHERE start_time >= DATE_TRUNC(month, CURRENT_DATE)
      GROUP BY 1
      ORDER BY 2 DESC;
    ```

#### Compute for Snowpipe and Snowpipe Streaming

Query: Cumulative usage of data ingest (Snowpipe and “Copy”)
:   This query returns an aggregated daily summary of all loads for each table in Snowflake showing average file size, total rows, total
    volume and the ingest method (copy or Snowpipe). If file sizes are too small or big for optimal ingest, additional
    investigation/optimization may be required. By mapping the volume to credit consumption, it is possible to determine which tables are
    consuming more credits per TB loaded.

    ```sqlexample
    SELECT TO_DATE(last_load_time) AS load_date,
      status,
      table_catalog_name AS database_name,
      table_schema_name AS schema_name,
      table_name,
      CASE
        WHEN pipe_name IS NULL THEN 'COPY'
        ELSE 'SNOWPIPE'
      END AS ingest_method,
      SUM(row_count) AS row_count,
      SUM(row_parsed) AS rows_parsed,
      AVG(file_size) AS avg_file_size_bytes,
      SUM(file_size) AS total_file_size_bytes,
      SUM(file_size)/POWER(1024,1) AS total_file_size_kb,
      SUM(file_size)/POWER(1024,2) AS total_file_size_mb,
      SUM(file_size)/POWER(1024,3) AS total_file_size_gb,
      SUM(file_size)/POWER(1024,4) AS total_file_size_tb
    FROM snowflake.account_usage.copy_history
    GROUP BY 1,2,3,4,5,6
    ORDER BY 3,4,5,1,2;
    ```

Query: Snowpipe cost history (by day, by object)
:   This query provides a full list of pipes and the volume of credits consumed via the service over the last 30 days, broken out by day.
    Any irregularities in the credit consumption or consistently high consumption are flags for additional investigation.

    ```sqlexample
    SELECT TO_DATE(start_time) AS date,
      pipe_name,
      SUM(credits_used) AS credits_used
    FROM snowflake.account_usage.pipe_usage_history
    WHERE start_time >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    GROUP BY 1,2
    ORDER BY 3 DESC;
    ```

Query: Snowpipe History & m-day average
:   This query shows the average daily credits consumed by Snowpipe grouped by week over the last year. It can help identify anomalies in
    daily averages over the year so you can investigate spikes or unexpected changes in consumption.

    ```sqlexample
    WITH credits_by_day AS (
      SELECT TO_DATE(start_time) AS date,
        SUM(credits_used) AS credits_used
      FROM snowflake.account_usage.pipe_usage_history
      WHERE start_time >= DATEADD(year,-1,CURRENT_TIMESTAMP())
      GROUP BY 1
      ORDER BY 2 DESC
    )

    SELECT DATE_TRUNC('week',date),
      AVG(credits_used) AS avg_daily_credits
    FROM credits_by_day
    GROUP BY 1
    ORDER BY 1;
    ```

Query: Total Snowpipe Streaming cost
:   This query lists the current credit usage for Snowpipe Streaming, including both Snowpipe Streaming compute and client costs.

    ```sqlexample
    SELECT start_time,
      end_time,
      SUM(credits_used) AS total_credits,
      name,
      IFF(CONTAINS(name,':'),'streaming client cost', 'streaming compute cost') AS streaming_cost_type
    FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY
    WHERE service_type ='SNOWPIPE_STREAMING'
    GROUP BY ALL;
    ```

#### Compute for serverless alerts

Query: Total serverless alert cost
:   This query lists the current credit usage for all serverless alerts:

    ```sqlexample
    SELECT
        start_time,
        end_time,
        alert_id,
        alert_name,
        credits_used,
        schema_id,
        schema_name,
        database_id,
        database_name
      FROM SNOWFLAKE.ACCOUNT_USAGE.serverless_alert_history
      ORDER BY start_time, alert_id;
    ```

#### Compute for serverless tasks

Query: Total serverless task cost
:   This query lists the current credit usage for all serverless tasks:

    ```sqlexample
    SELECT start_time,
      end_time,
      task_id,
      task_name,
      credits_used,
      schema_id,
      schema_name,
      database_id,
      database_name
    FROM snowflake.account_usage.serverless_task_history
    ORDER BY start_time, task_id;
    ```

#### Compute for replication

Query: Account replication cost
:   This query lists the credits used by a replication or failover group for account replication in the current month:

    ```sqlexample
    SELECT start_time,
      end_time,
      replication_group_name,
      credits_used,
      bytes_transferred
    FROM snowflake.account_usage.replication_group_usage_history
    WHERE start_time >= DATE_TRUNC('month', CURRENT_DATE());
    ```

Query: Database replication cost history (by day, by object)
:   This query provides a full list of replicated databases and the volume of credits consumed via the replication service over the last 30
    days, broken out by day. Any irregularities in the credit consumption or consistently high consumption are flags for additional
    investigation.

    ```sqlexample
    SELECT TO_DATE(start_time) AS date,
      database_name,
      SUM(credits_used) AS credits_used
    FROM snowflake.account_usage.database_replication_usage_history
    WHERE start_time >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    GROUP BY 1,2
    ORDER BY 3 DESC;
    ```

Query: Database replication History & m-day average
:   This query shows the average daily credits consumed by Replication grouped by week over the last year. This helps identify any
    anomalies in the daily average so you can investigate any spikes or changes in consumption.

    ```sqlexample
    WITH credits_by_day AS (
      SELECT TO_DATE(start_time) AS date,
        SUM(credits_used) AS credits_used
      FROM snowflake.account_usage.database_replication_usage_history
      WHERE start_time >= DATEADD(year,-1,CURRENT_TIMESTAMP())
      GROUP BY 1
      ORDER BY 2 DESC
    )

    SELECT DATE_TRUNC('week',date),
      AVG(credits_used) AS avg_daily_credits
    FROM credits_by_day
    GROUP BY 1
    ORDER BY 1;
    ```

#### Compute for partner tools

Query: Credit consumption by partner tools
:   This query identifies which of Snowflake’s partner tools/solutions (e.g. BI, ETL, etc.) are consuming the most credits. This can help
    identify partner solutions that are consuming more credits than anticipated, which can be a starting point for additional investigation.

    ```sqlexample
    -- This Is Approximate Credit Consumption By Client Application
    WITH
      client_hour_execution_cte AS (
        SELECT
          CASE
            WHEN client_application_id LIKE 'Go %' THEN 'Go'
            WHEN client_application_id LIKE 'Snowflake UI %' THEN 'Snowflake UI'
            WHEN client_application_id LIKE 'Snowflake CLI %' THEN 'Snowflake CLI'
            WHEN client_application_id LIKE 'SnowSQL %' THEN 'SnowSQL'
            WHEN client_application_id LIKE 'JDBC %' THEN 'JDBC'
            WHEN client_application_id LIKE 'PythonConnector %' THEN 'Python'
            WHEN client_application_id LIKE 'ODBC %' THEN 'ODBC'
            ELSE 'NOT YET MAPPED: ' || CLIENT_APPLICATION_ID
          END AS client_application_name,
          warehouse_name,
          DATE_TRUNC('hour',start_time) AS start_time_hour,
          SUM(execution_time)  AS client_hour_execution_time
        FROM snowflake.account_usage.query_history qh
          JOIN snowflake.account_usage.sessions se
            ON se.session_id = qh.session_id
        WHERE warehouse_name IS NOT NULL
          AND execution_time > 0
          AND start_time > DATEADD(month,-1,CURRENT_TIMESTAMP())
        GROUP BY 1,2,3
      ),
      hour_execution_cte AS (
        SELECT start_time_hour,
          warehouse_name,
          SUM(client_hour_execution_time) AS hour_execution_time
        FROM client_hour_execution_cte
        GROUP BY 1,2
      ),
      approximate_credits AS (
        SELECT A.client_application_name,
          C.warehouse_name,
          (A.client_hour_execution_time/B.hour_execution_time)*C.credits_used AS approximate_credits_used
        FROM client_hour_execution_cte A
          JOIN hour_execution_cte B
            ON A.start_time_hour = B.start_time_hour and B.warehouse_name = A.warehouse_name
          JOIN snowflake.account_usage.warehouse_metering_history C
            ON C.warehouse_name = A.warehouse_name AND C.start_time = A.start_time_hour
      )

    SELECT client_application_name,
      warehouse_name,
      SUM(approximate_credits_used) AS approximate_credits_used
    FROM approximate_credits
    GROUP BY 1,2
    ORDER BY 3 DESC;
    ```

#### Compute for hybrid tables

Query: Credit consumption for hybrid tables over a specific period of time
:   This query shows the total credit consumption for hybrid tables in your account over a
    specific period of time. This helps track hybrid table credit usage
    against expectations.

    > **Note:**
    >
    > As of March 1, 2026, Snowflake no longer bills customers for hybrid table requests;
    > however, you can still query this view to see historical consumption data.
    > For information about hybrid table storage costs, see [Evaluate cost for hybrid tables](tables-hybrid-cost.md).

    ```sqlexample
    -- Credits used (all time = past year)

    SELECT SUM(credits_used) AS total_credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.HYBRID_TABLE_USAGE_HISTORY;

    -- Credits used (past N days/weeks/months)

    SELECT SUM(credits_used) AS total_credits
      FROM SNOWFLAKE.ACCOUNT_USAGE.HYBRID_TABLE_USAGE_HISTORY
      WHERE start_time >= DATEADD(day, -5, CURRENT_TIMESTAMP());
    ```

#### Compute for Cortex Agents

Query: Credit consumption by Cortex Agents.
:   This query shows the credit consumption for Cortex Agents.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_AGENT_USAGE_HISTORY;
    ```

#### Compute for Cortex Analyst

Query: Credit consumption by Cortex Analyst.
:   This query shows the credit consumption for Cortex Analyst.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_ANALYST_USAGE_HISTORY;
    ```

#### Compute for Cortex Fine-tuning

Query: Credit consumption by Cortex Fine-tuning.
:   This query shows the training credit consumption for each Cortex Fine-tuning,
    aggregated in one hour increments.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FINE_TUNING_USAGE_HISTORY;
    ```

#### Compute for Cortex functions

Query: Credit consumption by Cortex functions.
:   This query shows the credit consumption for each Cortex function call, aggregated in one hour increments based on
    function and model.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FUNCTIONS_USAGE_HISTORY;
    ```

Query: Credit consumption by Cortex function called with the `mistral-large` model.
:   This query shows the credit consumption for each Cortex function called with the `mistral-large` model, aggregated in one
    hour increments based on function and model.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FUNCTIONS_USAGE_HISTORY
      WHERE model_name = 'mistral-large';
    ```

Query: Credit consumption by Cortex functions query.
:   This query shows the credit consumption for each Cortex functions query, aggregated in one hour increments based on
    function and model.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY
      WHERE query_id = 'query-id';
    ```

#### Compute for Cortex REST API

Query: Credit consumption by Cortex REST API.
:   This query shows the credit consumption for Cortex REST API calls, including the number of tokens processed
    and the model used for each request.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_REST_API_USAGE_HISTORY;
    ```

#### Compute for Cortex Search

Query: Daily credit consumption by Cortex Search.
:   This query shows the credit consumption for each Cortex Search Service,
    aggregated daily, including both serving and embed text token consumption.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_SEARCH_DAILY_USAGE_HISTORY;
    ```

Query: Credit consumption by Cortex Search serving.
:   This query shows the serving credit consumption for each Cortex Search Service,
    aggregated in one hour increments.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_SEARCH_SERVING_USAGE_HISTORY;
    ```

#### Compute for Document AI

Query: Credit consumption by Document AI.
:   This query shows the credit consumption for Document AI.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.DOCUMENT_AI_USAGE_HISTORY;
    ```

Query: Credit consumption per Document AI query.
:   This query retrieves records from the CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view where the CREDITS_USED is greater than 0.072.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY
      WHERE CREDITS_USED > 0.072
    ```

#### Compute for Snowflake Intelligence

Query: Credit consumption by Snowflake Intelligence.
:   This query shows the credit consumption for Snowflake Intelligence.

    ```sqlexample
    SELECT *
      FROM SNOWFLAKE.ACCOUNT_USAGE.SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY;
    ```

#### Compute for Snowflake Notebooks

Query: Hourly credit consumption by notebook
:   This query retrieves runtime history for a specific notebook, including credit usage and execution timestamps. Use this data to understand how
    often and how long a notebook runs, and to identify patterns or spikes in credit consumption by hour.

    ```sqlexample
    SELECT * FROM snowflake.account_usage.notebooks_container_runtime_history
    WHERE notebook_name = '<example_nb_name>';
    ```

Query: Cost to run a specific notebook
:   This query shows the total credits consumed by a specific notebook. Use this to estimate a notebook’s cost and identify high-cost notebooks.

    ```sqlexample
    SELECT
      notebook_name,
      SUM(credits) AS total_credits
    FROM snowflake.account_usage.notebooks_container_runtime_history
    WHERE notebook_name = '<example_nb_name>'
    GROUP BY notebook_name;
    ```

Query: Total compute pool cost per notebook
:   This query shows the total credits consumed by each notebook running on a specific compute pool. Use this to break down compute usage by
    notebook, which can help identify which notebooks contribute most to the compute pool’s overall cost.

    ```sqlexample
    SELECT
      notebook_name,
      SUM(credits) AS total_credits
    FROM snowflake.account_usage.notebooks_container_runtime_history
    WHERE compute_pool_name = '<example_cp_name>'
    GROUP BY notebook_name;
    ```

Query: Identify users who ran a specific notebook
:   This query returns a list of users who have executed a specific notebook. Use this to understand usage patterns, or identify collaborators
    and consumers of shared notebooks.

    ```sqlexample
    SELECT
      DISTINCT user_name
    FROM snowflake.account_usage.notebooks_container_runtime_history
    WHERE notebook_name = '<example_nb_name>';
    ```
