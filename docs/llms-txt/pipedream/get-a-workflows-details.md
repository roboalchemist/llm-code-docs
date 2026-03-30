# Source: https://pipedream.com/docs/rest-api/api-reference/workflows/get-a-workflows-details.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Workflow’s details

Retrieves the details of a specific workflow within an organization’s project.

#### Endpoint

```
GET /workflows/{workflow_id}
```

#### Path Parameters

<ParamField path="workflow_id" type="string" required>
  The ID of the workflow to retrieve.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/workflows/p_abc123?org_id=o_abc123' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "triggers": [
      {
        "id": "hi_ABpHKz",
        "key": "eabcdefghiklmnop",
        "endpoint_url": "http://eabcdefghiklmnop.m.d.pipedream.net",
        "custom_response": false
      }
    ],
    "steps": [
      {
        "id": "c_abc123",
        "namespace": "code",
        "disabled": false,
        "lang": "nodejs20.x",
        "appConnections": [],
        "component": true,
        "savedComponent": {
          "id": "sc_abc123",
          "codeHash": "long-hash-here",
          "configurableProps": [
            {
              "name": "channelId",
              "type": "string"
            },
            {
              "name": "message",
              "type": "string"
            },
            {
              "name": "slack",
              "type": "app",
              "app": "slack"
            }
          ],
          "version": ""
        },
        "component_key": null,
        "component_owner_id": "o_abc123",
        "configured_props_json": "{}"
      }
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
