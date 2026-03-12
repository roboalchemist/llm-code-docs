# Source: https://pipedream.com/docs/rest-api/api-reference/workspaces/get-workspaces-subscriptions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workspaces’s Subscriptions

Retrieve all the [subscriptions](/rest-api/#subscriptions) configured for a specific workspace.

#### Endpoint

```
GET /workspaces/<org_id>/subscriptions
```

#### Path Parameters

<ParamField body="workspaces_id" type="string" required>
  [Switch to your workspace’s context](/workspaces/#switching-between-workspaces) and [find your org’s ID](/workspaces/#finding-your-workspaces-id).
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/workspaces/o_abc123/subscriptions' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": [
      {
        "id": "sub_abc123",
        "emitter_id": "dc_abc123",
        "listener_id": "p_abc123",
        "event_name": ""
      },
      {
        "id": "sub_def456",
        "emitter_id": "dc_def456",
        "listener_id": "p_def456",
        "event_name": ""
      }
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
