# Log customization
Source: https://www.meilisearch.com/docs/reference/api/logs

Customize Meilisearch logs with two experimental features: --experimental-logs-mode and --experimental-enable-logs-route.

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json'  \
    --data-binary '{
      "logsRoute": true
    }'
  ```

  This feature is not available for Meilisearch Cloud users.
</Note>

## Customize log levels

<RouteHighlighter method="POST" />

Customize logging levels for the default logging system.

### Body

| Name            | Type   | Default value | Description                                                |
| :-------------- | :----- | :------------ | :--------------------------------------------------------- |
| **`target`** \* | String | N/A           | A string specifying one or more log type and its log level |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST MEILISEARCH_URL/logs/stderr \
    -H 'Content-Type: application/json' \
    --data-binary '{
        "target": "milli=trace,index_scheduler=info,actix_web=off"
    }'
  ```
</CodeGroup>

## Start log stream

<RouteHighlighter method="POST" />

Opens a continuous stream of logs for focused debugging sessions. The stream will continue to run indefinitely until you [interrupt](#interrupt-log-stream) it.

### Body

| Name            | Type   | Default value | Description                                                |
| :-------------- | :----- | :------------ | :--------------------------------------------------------- |
| **`mode`** \*   | String | N/A           | Specifies either human-readabale or JSON output            |
| **`target`** \* | String | N/A           | A string specifying one or more log type and its log level |

## Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST MEILISEARCH_URL/logs/stream \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "mode": "human",
      "target": "index_scheduler=trace"
    }'
  ```
</CodeGroup>

<Warning>
  Certain HTTP clients such as `httpie` and `xh`, will only display data after you have interrupted the stream with the `DELETE` endpoint.
</Warning>

## Interrupt log stream

<RouteHighlighter method="DELETE" />

Interrupt a log stream.

## Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE MEILISEARCH_URL/logs/stream
  }'
  ```
</CodeGroup>