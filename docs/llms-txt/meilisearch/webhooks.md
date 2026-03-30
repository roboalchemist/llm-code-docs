# Webhooks
Source: https://www.meilisearch.com/docs/reference/api/webhooks

Use the /webhooks to trigger automatic workflows when Meilisearch finishes processing tasks.

Use the `/webhooks` to trigger automatic workflows when Meilisearch finishes processing tasks.

## The webhook object

```json theme={null}
{
  "uuid": "V4_UUID_GENERATED_BY_MEILISEARCH",
  "url": "WEBHOOK_NOTIFICATION_TARGET_URL",
  "headers": {
    "HEADER": "VALUE",
  },
  "isEditable": false
}
```

* `uuid`: a v4 uuid Meilisearch automatically generates when you create a new webhook
* `url`: a string indication the URL Meilisearch should notify whenever it completes a task, required
* `headers`: an object with HTTP headers and their values, optional, often used for authentication
  * `Authorization` headers: the value of authorization headers is redacted in `webhook` responses. Do not use authorization header values as returned by Meilisearch to update a webhook
* `isEditable`: read-only Boolean field indicating whether you can edit the webhook. Meilisearch automatically sets this to `true` for all webhooks created via the API and to `false` for reserved webhooks

## The webhook payload

When Meilisearch finishes processing a task, it sends the relevant [task object](/reference/api/tasks#task-object) to all configured webhooks.

## Get all webhooks

<RouteHighlighter method="GET" />

Get a list of all webhooks configured in the current Meilisearch instance.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/webhooks'
  ```

  ```javascript JS theme={null}
  client.getWebhooks()
  ```

  ```python Python theme={null}
  client.get_webhooks()
  ```

  ```go Go theme={null}
  client.ListWebhooks();
  ```

  ```rust Rust theme={null}
  let webhooks = client.get_webhooks().await.unwrap();
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{
  "results": [
    {
      "uuid": "UUID_V4",
      "url": "WEBHOOK_TARGET_URL",
      "headers": {
        "HEADER": "VALUE",
      },
      "isEditable": false
    },
    {
      "uuid": "UUID_V4",
      "url": "WEBHOOK_TARGET_URL",
      "headers": null,
      "isEditable": true
    }
  ]
}
```

## Get a single webhook

<RouteHighlighter method="GET" />

Get a single webhook configured in the current Meilisearch instance.

### Example

<CodeSamplesWebhooksGetSingle1 />

#### Response: `200 OK`

```json theme={null}
{
  "uuid": "UUID_V4",
  "url": "WEBHOOK_TARGET_URL",
  "headers": {
    "HEADER": "VALUE",
  },
  "isEditable": false
}
```

## Create a webhook

<RouteHighlighter method="POST" />

Create a new webhook. When Meilisearch finishes processing a task, it sends the relevant [task object](/reference/api/tasks#task-object) to all configured webhooks.

You can create up to 20 webhooks. Having multiple webhooks active at the same time may negatively impact performance.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/webhooks' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "url": "WEBHOOK_TARGET_URL",
      "headers": {
        "authorization": "SECURITY_KEY",
        "referer": "https://example.com"
      }
    }'
  ```

  ```javascript JS theme={null}
  client.createWebhook({
    url: 'WEBHOOK_TARGET_URL',
    headers: {
      authorization: 'SECURITY_KEY',
      referer: 'https://example.com'
    }
  })
  ```

  ```python Python theme={null}
  client.create_webhook({
    'url': 'https://example.com/webhook',
    'headers': {"Authorization":"", "X-Custom-Header":"test"},
  })
  ```

  ```go Go theme={null}
  client.AddWebhook(&meilisearch.AddWebhookRequest{
    URL: "WEBHOOK_TARGET_URL",
    Headers: map[string]string{
      "authorization": "SECURITY_KEY",
      "referer": "https://example.com"
    },
  });
  ```

  ```rust Rust theme={null}
  let mut payload = meilisearch_sdk::webhooks::WebhookCreate::new("WEBHOOK_TARGET_URL");
  payload
    .insert_header("authorization", "SECURITY_KEY")
    .insert_header("referer", "https://example.com");
  let webhook = client.create_webhook(&payload).await.unwrap();
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{
  "uuid": "627ea538-733d-4545-8d2d-03526eb381ce",
  "url": "WEBHOOK_TARGET_URL",
  "headers": {
    "authorization": "SECURITY_KEY",
    "referer": "https://example.com",
  },
  "isEditable": true
}
```

## Update a webhook

<RouteHighlighter method="PATCH" />

Update the configuration for the specified webhook. To remove a field, set its value to `null`.

When updating the `headers` field, Meilisearch only changes the headers you have explicitly submitted. All other headers remain unaltered.

<Note>
  It is not possible to edit webhooks whose `isEditable` field is set to `false`.

  Meilisearch Cloud may create internal webhooks to support features such as Analytics and monitoring. These webhooks are always `isEditable: false`.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/webhooks/WEBHOOK_UUID' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "header": {
        "referer": null
      }
    }'
  ```

  ```javascript JS theme={null}
  client.updateWebhook(WEBHOOK_UUID, {
    headers: {
      referer: null
    }
  })
  ```

  ```python Python theme={null}
  client.update_webhook('WEBHOOK_UID', {
    'url': 'https://example.com/new-webhook',
    'headers': {"Authorization":"", "X-Custom-Header":"test"},
  })
  ```

  ```go Go theme={null}
  client.UpdateWebhook("WEBHOOK_UUID", &meilisearch.UpdateWebhookRequest{
    Header: map[string]string{
      "referer": ""
    },
  });
  ```

  ```rust Rust theme={null}
  let mut update = meilisearch_sdk::webhooks::WebhookUpdate::new();
  update.remove_header("referer");
  let webhook = client
    .update_webhook("WEBHOOK_UUID", &update)
    .await
    .unwrap();
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{
  "uuid": "627ea538-733d-4545-8d2d-03526eb381ce",
  "url": "WEBHOOK_TARGET_URL",
  "headers": {
    "authorization": "SECURITY_KEY"
  },
  "isEditable": true
}
```

## Delete a webhook

<RouteHighlighter method="DELETE" />

Delete a webhook and stop sending task completion data to the target URL.

<Note>
  It is not possible to delete webhooks whose `isEditable` field is set to `false`.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/webhooks/WEBHOOK_UUID'
  ```

  ```javascript JS theme={null}
  client.deleteWebhook(WEBHOOK_UUID)
  ```

  ```python Python theme={null}
  client.delete_webhook('WEBHOOK_UID')
  ```

  ```go Go theme={null}
  client.DeleteWebhook("WEBHOOK_UUID");
  ```

  ```rust Rust theme={null}
  client.delete_webhook("WEBHOOK_UUID").await.unwrap();
  ```
</CodeGroup>

#### Response: `204 No Content`