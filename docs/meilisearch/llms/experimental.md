# Experimental
Source: https://www.meilisearch.com/docs/reference/api/experimental_features

The /experimental-features route allows you to manage some of Meilisearch's experimental features.

The `/experimental-features` route allows you to activate or deactivate some of Meilisearch's [experimental features](/learn/resources/experimental_features_overview).

This route is **synchronous**. This means that no task object will be returned, and any activated or deactivated features will be made available or unavailable immediately.

<Warning>
  The experimental API route is not compatible with all experimental features. Consult the [experimental feature overview](/learn/resources/experimental_features_overview) for a compatibility list.
</Warning>

## Experimental features object

```json theme={null}
{
  "metrics": false,
  "logsRoute": true,
  "containsFilter": false,
  "editDocumentsByFunction": false,
  "network": false,
  "chatCompletions": false,
  "multimodal": false,
  "vectorStoreSetting": false
}
```

| Name                          | Type    | Description                                    |
| :---------------------------- | :------ | :--------------------------------------------- |
| **`metrics`**                 | Boolean | `true` if feature is active, `false` otherwise |
| **`logsRoute`**               | Boolean | `true` if feature is active, `false` otherwise |
| **`containsFilter`**          | Boolean | `true` if feature is active, `false` otherwise |
| **`editDocumentsByFunction`** | Boolean | `true` if feature is active, `false` otherwise |
| **`network`**                 | Boolean | `true` if feature is active, `false` otherwise |
| **`chatCompletions`**         | Boolean | `true` if feature is active, `false` otherwise |
| **`multimodal`**              | Boolean | `true` if feature is active, `false` otherwise |
| **`vectorStoreSetting`**      | Boolean | `true` if feature is active, `false` otherwise |

## Get all experimental features

<RouteHighlighter method="GET" />

Get a list of all experimental features that can be activated via the `/experimental-features` route and whether or not they are currently activated.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/experimental-features/'
  ```

  ```ruby Ruby theme={null}
  client.experimental_features
  ```

  ```go Go theme={null}
  client.ExperimentalFeatures().Get()
  ```

  ```rust Rust theme={null}
  let client = Client::new("http://localhost:7700", Some("apiKey"));
  let features = ExperimentalFeatures::new(&client);
  let res = features
    .get()
    .await
    .unwrap();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "metrics": false,
  "logsRoute": true,
  "containsFilter": false,
  "editDocumentsByFunction": false,
  "network": false,
  "chatCompletions": false,
  "multimodal": false,
  "vectorStoreSetting": false
}
```

## Configure experimental features

<RouteHighlighter method="PATCH" />

Activate or deactivate experimental features.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json'  \
    --data-binary '{
      "metrics": true
    }'
  ```

  ```ruby Ruby theme={null}
  client.update_experimental_features(metrics: true)
  ```

  ```go Go theme={null}
  client.ExperimentalFeatures().SetMetrics(true).Update()
  ```

  ```rust Rust theme={null}
  let client = Client::new("http://localhost:7700", Some("apiKey"));
  let features = ExperimentalFeatures::new(&client);
  features.set_metrics(true)
  let res = features
    .update()
    .await
    .unwrap();
  ```
</CodeGroup>

Setting a field to `null` leaves its value unchanged.

### Body

```
{<featureName>: <Boolean>}
```

### Response: `200 Ok`

```json theme={null}
{
  "metrics": false,
  "logsRoute": true,
  "containsFilter": false,
  "editDocumentsByFunction": false,
  "network": false,
  "multimodal": false,
  "vectorStoreSetting": false
}
```