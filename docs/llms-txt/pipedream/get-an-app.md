# Source: https://pipedream.com/docs/rest-api/api-reference/apps/get-an-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an App

Retrieve metadata for a specific app.

#### Endpoint

```
GET /apps/{app_id}
```

#### Path Parameters

<ParamField body="app_id" type="string">
  The ID or name slug the app you’d like to retrieve. For example, Slack’s unique app ID is `app_OkrhR1`, and its name slug is `slack`.

  You can find the app’s ID in the response from the [List apps](/rest-api/#list-apps) endpoint, and the name slug under the **Authentication** section of any [app page](https://pipedream.com/apps).
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/apps/app_OkrhR1 \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": {
      "id": "app_OkrhR1",
      "name_slug": "slack",
      "name": "Slack",
      "auth_type": "oauth",
      "description": "Slack is a channel-based messaging platform. With Slack, people can work together more effectively, connect all their software tools and services, and find the information they need to do their best work — all within a secure, enterprise-grade environment.",
      "img_src": "https://assets.pipedream.net/s.v0/app_OkrhR1/logo/orig",
      "custom_fields_json": "[]",
      "categories": [
        "Communication"
      ],
      "featured_weight": 1000000001,
      "connect": {
        "proxy_enabled": true,
        "allowed_domains": ["slack.com"],
        "base_proxy_target_url": "https://slack.com"
      }
    }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
