# Source: https://pipedream.com/docs/rest-api/api-reference/components/create-a-component.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a component

<Tip>
  `/components` endpoints are only available when using [user API keys](/rest-api/auth/#user-api-keys), not yet for workspace [OAuth tokens](/rest-api/auth/#oauth).
</Tip>

Before you can create a source using the REST API, you must first create a **component** - the code for the source.

This route returns the components `id`, `code`, `configurable_props`, and other metadata you’ll need to [deploy a source](/rest-api/#create-a-source) from this component.

#### Endpoint

```
POST /components
```

#### Parameters

<ParamField body="component_code" type="string">
  The full code for a [Pipedream component](/components/contributing/api/).
</ParamField>

***

<ParamField body="component_url" type="string">
  A reference to the URL where the component is hosted.

  For example, to create an RSS component, pass `https://github.com/PipedreamHQ/pipedream/blob/master/components/rss/sources/new-item-in-feed/new-item-in-feed.ts`.
</ParamField>

***

One of `component_code` *or* `component_url` is required. If both are present, `component_code` is preferred and `component_url` will be used only as metadata to identify the location of the code.

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/components \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{"component_url": "https://github.com/PipedreamHQ/pipedream/blob/master/components/rss/sources/new-item-in-feed/new-item-in-feed.ts"}'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": {
      "id": "sc_JDi8EB",
      "code": "component code here",
      "code_hash": "685c7a680d055eaf505b08d5d814feef9fabd516d5960837d2e0838d3e1c9ed1",
      "name": "rss",
      "version": "0.0.1",
      "configurable_props": [
        {
          "name": "url",
          "type": "string",
          "label": "Feed URL",
          "description": "Enter the URL for any public RSS feed."
        },
        {
          "name": "timer",
          "type": "$.interface.timer",
          "default": {
            "intervalSeconds": 900
          }
        }
      ],
      "created_at": 1588866900,
      "updated_at": 1588866900
    }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
