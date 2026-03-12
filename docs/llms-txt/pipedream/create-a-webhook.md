# Source: https://pipedream.com/docs/rest-api/api-reference/webhooks/create-a-webhook.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a webhook

Creates a webhook pointing to a URL. Configure a [subscription](/rest-api/#subscriptions) to deliver events to this webhook.

#### Endpoint

```
POST /webhooks?url={your_endpoint_url}&name={name}&description={description}
```

#### Parameters

<ParamField body="url" type="string" required>
  The endpoint URL where you’d like to deliver events. Any events sent to this webhook object will be delivered to this endpoint URL.

  This URL **must** contain, at a minimum, a protocol — one of `http` or `https` — and hostname, but can specify resources or ports. For example, these URLs work:

  ```
  https://example.com
  http://example.com
  https://example.com:12345/endpoint
  ```

  but these do not:

  ```
  # No protocol - needs http(s)://
  example.com

  # mysql protocol not supported. Must be an HTTP(S) endpoint
  mysql://user:pass@host:port
  ```

</ParamField>

***

<ParamField body="name" type="string" required>
  The name you’d like to assign to this webhook, which will appear when [listing your webhooks](/rest-api/#get-current-users-webhooks).
</ParamField>

***

<ParamField body="description" type="string" required>
  The description you’d like to assign to this webhook.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  # You can create a webhook that delivers events to `https://endpoint.m.pipedream.net` using the following command:
  curl "https://api.pipedream.com/v1/webhooks?url=https://endpoint.m.pipedream.net&name=name&description=description" \
    -X POST \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  // Successful API responses contain a webhook ID for the webhook that was created in `data.id` — the string that starts with `wh_` — which you can reference when creating [subscriptions](/rest-api/#subscriptions).
  {
    "data": {
      "id": "wh_abc123",
      "user_id": "u_abc123",
      "name": null,
      "description": null,
      "url": "https://endpoint.m.pipedream.net",
      "active": true,
      "created_at": 1611964025,
      "updated_at": 1611964025
    }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
