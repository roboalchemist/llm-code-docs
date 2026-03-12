# Source: https://pipedream.com/docs/rest-api/api-reference/workspaces/get-a-workspace.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a Workspace

Programmatically view your workspace’s current credit usage for the billing period in real time.

#### Endpoint

```
GET /v1/workspaces/<org_id>
```

#### Path Parameters

<ParamField path="workspaces_id" type="string">
  [Switch to your workspace’s context](/workspaces/#switching-between-workspaces) and [find your org’s ID](/workspaces/#finding-your-workspaces-id).
</ParamField>

<ResponseExample>
  ```json  theme={null}
  {
   "data": {
    "id": "o_Qa8I1Z",
    "orgname": "asdf",
    "name": "asdf",
    "email": "dev@pipedream.com",
    "daily_credits_quota": 100,
    "daily_credits_used": 0
   }
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
