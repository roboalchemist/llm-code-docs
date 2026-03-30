# Source: https://pipedream.com/docs/rest-api/api-reference/sources/create-a-source.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Source

<Tip>
  This endpoint is only available when using [user API keys](/rest-api/auth/#user-api-keys), not yet for workspace [OAuth tokens](/rest-api/auth/#oauth).
</Tip>

#### Endpoint

```
POST /sources/
```

#### Parameters

<ParamField body="component_id" type="string">
  The ID of a component previously created in your account. [See the component endpoints](/rest-api/#components) for information on how to retrieve this ID.
</ParamField>

***

<ParamField body="component_code" type="string">
  The full code for a [Pipedream component](/components/contributing/api/).
</ParamField>

***

<ParamField body="component_url" type="string">
  A reference to the URL where the component is hosted.

  For example, to create an RSS component, pass `https://github.com/PipedreamHQ/pipedream/blob/master/components/rss/sources/new-item-in-feed/new-item-in-feed.ts`.
</ParamField>

***

One of `component_id`, `component_code`, or `component_url` is required. If all are present, `component_id` is preferred and `component_url` will be used only as metadata to identify the location of the code.

***

<ParamField body="name" type="string">
  The name of the source.

  If absent, this defaults to using the [name slug](/components/contributing/api/#component-structure) of the component used to create the source.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/sources \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{"component_url": "https://github.com/PipedreamHQ/pipedream/blob/master/components/rss/sources/new-item-in-feed/new-item-in-feed.ts", "name": "your-name-here", "configured_props": { "url": "https://rss.m.pipedream.net", "timer": { "intervalSeconds": 60 }}}'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  // Example response from creating an RSS source that runs once a minute:
  {
    "data": {
      "id": "dc_abc123",
      "user_id": "u_abc123",
      "component_id": "sc_abc123",
      "configured_props": {
        "url": "https://rss.m.pipedream.net",
        "timer": {
          "cron": null,
          "interval_seconds": 60
        }
      },
      "active": true,
      "created_at": 1589486978,
      "updated_at": 1589486978,
      "name": "your-name-here",
      "name_slug": "your-name-here"
    }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
