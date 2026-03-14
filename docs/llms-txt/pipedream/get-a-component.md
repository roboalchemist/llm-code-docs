# Source: https://pipedream.com/docs/rest-api/api-reference/components/get-a-component.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a component

Retrieve a component saved or published in your account using its saved component ID **or** key.

This endpoint returns the component’s metadata and configurable props.

#### Endpoint

```
GET /components/{key|id}
```

#### Parameters

<ParamField title="key" type="string">
  The component key (identified by the `key` property within the component’s source code) you’d like to fetch metadata for (example: `my-component`)
</ParamField>

**or**

<ParamField title="id" type="string">
  The saved component ID you’d like to fetch metadata for (example: `sc_JDi8EB`)
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl https://api.pipedream.com/v1/components/my-component \
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
