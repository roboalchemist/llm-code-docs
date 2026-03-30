# Source: https://pipedream.com/docs/rest-api/api-reference/workspaces/get-workspaces-sources.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workspaces’s Sources

Retrieve all the [event sources](/rest-api/#sources) configured for a specific workspace.

#### Endpoint

```
GET /orgs/<org_id>/sources
```

#### Path Parameters

<ParamField path="org_id" type="string" required>
  [Switch to your workspace’s context](/workspaces/#switching-between-workspaces) and [find your org’s ID](/workspaces/#finding-your-workspaces-id).
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/orgs/o_abc123/sources' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "page_info": {
      "total_count": 19,
      "count": 10,
      "start_cursor": "ZGNfSzB1QWVl",
      "end_cursor": "ZGNfeUx1alJx"
    },
    "data": [
      {
        "id": "dc_abc123",
        "component_id": "sc_def456",
        "configured_props": {
          "http": {
            "endpoint_url": "https://myendpoint.m.pipedream.net"
          }
        },
        "active": true,
        "created_at": 1587679599,
        "updated_at": 1587764467,
        "name": "test",
        "name_slug": "test"
      }
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
