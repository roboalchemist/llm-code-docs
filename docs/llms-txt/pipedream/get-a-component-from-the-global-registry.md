# Source: https://pipedream.com/docs/rest-api/api-reference/components/get-a-component-from-the-global-registry.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a component from the global registry

Pipedream operates a global registry of all public components (for example, for apps like GitHub, Google Calendar, and more). This endpoint returns the same data as the endpoint for [retrieving metadata on a component you own](/rest-api/#get-a-component), but allows you to fetch data for any globally-published component.

#### Endpoint

```
GET /components/registry/{key}
```

#### Parameters

<ParamField title="key" type="string">
  The component key (identified by the `key` property within the component’s source code) you’d like to fetch metadata for (example: `my-component`)
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/components/registry/github-new-repository \
    -H "Authorization: Bearer <token>"
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
