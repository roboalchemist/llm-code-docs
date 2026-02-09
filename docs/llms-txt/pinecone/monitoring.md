# Source: https://docs.pinecone.io/guides/production/monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor performance

> Monitor performance metrics in the Pinecone console or with Prometheus or Datadog.

Pinecone generates time-series performance metrics for each Pinecone index. You can monitor these metrics directly in the Pinecone console or with tools like Prometheus or Datadog.

## Monitor in the Pinecone Console

To view performance metrics in the Pinecone console:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project containing the index you want to monitor.
3. Go to **Database > Indexes**.
4. Select the index.
5. Go to the **Metrics** tab.

## Monitor with Datadog

To monitor Pinecone with Datadog, use Datadog's [Pinecone integration](/integrations/datadog).

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Monitor with Prometheus

<Note>
  This feature is available on [Standard and  Enterprise plans](https://www.pinecone.io/pricing/). When using [Bring Your Own Cloud](/guides/production/bring-your-own-cloud), you must configure Prometheus monitoring within your VPC.
</Note>

To monitor all serverless indexes in a project, insert the following snippet into the [`scrape_configs`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your `prometheus.yml` file and update it with values for your Prometheus integration:

<Note>
  This method uses [HTTP service discovery](https://prometheus.io/docs/prometheus/latest/http_sd/) to automatically discover and target all serverless indexes across all regions in a project.
</Note>

```YAML  theme={null}
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'pinecone-serverless-metrics'
    http_sd_configs:
      - url: https://api.pinecone.io/prometheus/projects/PROJECT_ID/metrics/discovery
        refresh_interval: 1m
        authorization:
          type: Bearer
          credentials: API_KEY
    authorization:
      type: Bearer
      credentials: API_KEY
```

* Replace `PROJECT_ID` with the unique ID of the project you want to monitor. You can [find the project ID](/guides/projects/understanding-projects#project-ids) in the Pinecone console.

* Replace both instances of `API_KEY` with an API key for the project you want to monitor. The first instance is for service discovery, and the second instance is for the discovered targets. If necessary, you can [create an new API key](/guides/projects/manage-api-keys) in the Pinecone console.

For more configuration details, see the [Prometheus docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Available metrics

The following metrics are available when you integrate Pinecone with Prometheus:

<div className="border border-gray-200 dark:border-gray-700 rounded-lg p-4 my-4">
  <Tabs>
    <Tab title="Metrics">
      | Name                                 | Type    | Description                                                                                                 |
      | :----------------------------------- | :------ | :---------------------------------------------------------------------------------------------------------- |
      | `pinecone_db_record_total`           | gauge   | The total number of records in the index.                                                                   |
      | `pinecone_db_storage_size_bytes`     | gauge   | The total size of the index in bytes.                                                                       |
      | `pinecone_db_op_upsert_count`        | counter | The number of [upsert](/guides/index-data/upsert-data) requests.                                            |
      | `pinecone_db_op_upsert_duration_sum` | counter | The total time taken processing [upsert](/guides/index-data/upsert-data) requests in milliseconds.          |
      | `pinecone_db_op_query_count`         | counter | The number of [query](/guides/search/search-overview) requests.                                             |
      | `pinecone_db_op_query_duration_sum`  | counter | The total time taken processing [query](/guides/search/search-overview) requests in milliseconds.           |
      | `pinecone_db_op_fetch_count`         | counter | The number of [fetch](/guides/manage-data/fetch-data) requests.                                             |
      | `pinecone_db_op_fetch_duration_sum`  | counter | The total time taken processing [fetch](/guides/manage-data/fetch-data) requests in milliseconds.           |
      | `pinecone_db_op_update_count`        | counter | The number of [update](/guides/manage-data/update-data) requests.                                           |
      | `pinecone_db_op_update_duration_sum` | counter | The total time taken processing [update](/guides/manage-data/update-data) requests in milliseconds.         |
      | `pinecone_db_op_delete_count`        | counter | The number of [delete](/guides/manage-data/delete-data) requests.                                           |
      | `pinecone_db_op_delete_duration_sum` | counter | The total time taken processing [delete](/guides/manage-data/delete-data) requests in milliseconds.         |
      | `pinecone_db_write_unit_count`       | counter | The total number of [write units](/guides/manage-cost/understanding-cost#write-units) consumed by an index. |
      | `pinecone_db_read_unit_count`        | counter | The total number of [read units](/guides/manage-cost/understanding-cost#read-units) consumed by an index.   |
    </Tab>

    <Tab title="Metric name migration">
      Some metric names changed on December 19, 2025. The following metrics were renamed:

      | Previous name (before Dec 19, 2025)    | Current name                                 |
      | :------------------------------------- | :------------------------------------------- |
      | `pinecone_db_record_total`             | `pinecone_db_record_total` (no change)       |
      | `pinecone_db_storage_size_bytes`       | `pinecone_db_storage_size_bytes` (no change) |
      | `pinecone_db_op_upsert_total`          | `pinecone_db_op_upsert_count`                |
      | `pinecone_db_op_upsert_duration_total` | `pinecone_db_op_upsert_duration_sum`         |
      | `pinecone_db_op_query_total`           | `pinecone_db_op_query_count`                 |
      | `pinecone_db_op_query_duration_total`  | `pinecone_db_op_query_duration_sum`          |
      | `pinecone_db_op_fetch_total`           | `pinecone_db_op_fetch_count`                 |
      | `pinecone_db_op_fetch_duration_total`  | `pinecone_db_op_fetch_duration_sum`          |
      | `pinecone_db_op_update_total`          | `pinecone_db_op_update_count`                |
      | `pinecone_db_op_update_duration_total` | `pinecone_db_op_update_duration_sum`         |
      | `pinecone_db_op_delete_total`          | `pinecone_db_op_delete_count`                |
      | `pinecone_db_op_delete_duration_total` | `pinecone_db_op_delete_duration_sum`         |
      | `pinecone_db_write_unit_total`         | `pinecone_db_write_unit_count`               |
      | `pinecone_db_read_unit_total`          | `pinecone_db_read_unit_count`                |
    </Tab>
  </Tabs>
</div>

### Metric labels

Each metric contains the following labels:

| Label           | Description                                                  |
| :-------------- | :----------------------------------------------------------- |
| `index_name`    | Name of the index to which the metric applies.               |
| `cloud`         | Cloud where the index is deployed: `aws`, `gcp`, or `azure`. |
| `region`        | Region where the index is deployed.                          |
| `capacity_mode` | Type of index: `serverless` or `byoc`.                       |
| `instance`      | Server instance (only available for counter metrics).        |

### Example queries

Return the total number of records per index:

```shell  theme={null}
sum by (index_name) (pinecone_db_record_total)
```

Return the total number of records in Pinecone index `docs-example`:

```shell  theme={null}
pinecone_db_record_total{index_name="docs-example"}
```

For each index, return the total number of upsert requests per second:

```shell  theme={null}
sum by (index_name) (rate(pinecone_db_op_upsert_count[5m]))
```

Return the average processing time in milliseconds for upsert requests per index:

```shell  theme={null}
(sum by (index_name) (rate(pinecone_db_op_upsert_duration_sum[1m])))/(sum by (index_name) (rate(pinecone_db_op_upsert_count[1m])))
```

For each index, return the total number of read units consumed per second:

```shell  theme={null}
sum by (index_name) (rate(pinecone_db_read_unit_count[5m]))
```

Return the total write units consumed per second for the Pinecone index `docs-example`:

```shell  theme={null}
sum (rate(pinecone_db_write_unit_count{index_name="docs-example"}[5m]))
```
