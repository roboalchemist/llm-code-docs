# Metrics
Source: https://www.meilisearch.com/docs/reference/api/metrics

The /metrics endpoint is an experimental feature. It exposes data compatible with Prometheus and offers insight into Meilisearch's behavior and performance.

The `/metrics` route exposes data compatible with [Prometheus](https://prometheus.io/). You will also need to have Grafana installed in your system to make use of this feature.

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "metrics": true
    }'
  ```

  This feature is not available for Meilisearch Cloud users.
</Note>

## Exposed information

`/metrics` exposes the following information:

| Name                                     | Description                                                                                                                                                                                                                                                                                                                                                                             | Type      |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `meilisearch_http_requests_total`        | Returns the number of times an API resource is accessed.                                                                                                                                                                                                                                                                                                                                | counter   |
| `meilisearch_http_response_time_seconds` | Returns a time histogram showing the number of times an API resource call goes into a time bucket (expressed in second).                                                                                                                                                                                                                                                                | histogram |
| `meilisearch_db_size_bytes`              | Returns the “real” size of the database on disk in bytes. It includes all the lmdb memory mapped files plus all the files contained in the `data.ms` directory (mainly the updates files that were not processed yet).                                                                                                                                                                  | gauge     |
| `meilisearch_used_db_size_bytes`         | Returns the size of the database actually used by meilisearch in bytes. Include all the same files as `meilisearch_db_size_bytes` except that when it comes to an LMDB database, we only count the pages used by meilisearch. This means if you see a large gap between both metrics, adding documents will probably re-use freed pages instead of growing `meilisearch_db_size_bytes`. | gauge     |
| `meilisearch_index_docs_count`           | Returns the number of documents for an index.                                                                                                                                                                                                                                                                                                                                           | gauge     |
| `meilisearch_index_count`                | Returns the total number of index for the Meilisearch instance.                                                                                                                                                                                                                                                                                                                         | gauge     |
| `meilisearch_nb_tasks`                   | Returns the total number of tasks for the Meilisearch instance parametrized by the kind of task and its value (see the table below).                                                                                                                                                                                                                                                    | counter   |
| `meilisearch_last_update`                | Returns the timestamp of the last update.                                                                                                                                                                                                                                                                                                                                               | gauge     |
| `meilisearch_is_indexing`                | Returns `1` if Meilisearch is indexing or `0` if not.                                                                                                                                                                                                                                                                                                                                   | gauge     |

<Warning>
  API keys with access to `/metrics` are able to see all HTTP calls for all the routes in an instance. This may lead to leaking sensitive information such as index names, document's primary keys, and API keys.
</Warning>

## Get metrics

<RouteHighlighter method="GET" />

Get data for current status of your instance. In most cases, you should only query this endpoint via a Prometheus-compatible tool such as Grafana.

Refer to Meilisearch's sample configuration files for example of a [basic Prometheus scraper](https://github.com/orgs/meilisearch/discussions/assets/prometheus-basic-scraper.yml) and [Grafana dashboard](https://github.com/meilisearch/meilisearch/blob/main/assets/grafana-dashboard.json).

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/metrics'
  ```
</CodeGroup>

#### Response: `200 OK`

```