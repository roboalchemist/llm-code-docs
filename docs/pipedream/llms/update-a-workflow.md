# Source: https://pipedream.com/docs/rest-api/api-reference/workflows/update-a-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Workflow

### Update a Workflow

<Tip>
  This endpoint is only available when using [user API keys](/rest-api/auth/#user-api-keys), not yet for workspace [OAuth tokens](/rest-api/auth/#oauth).
</Tip>

Updates the workflow’s activation status. If you need to modify the workflow’s steps, triggers, or connected accounts [consider making a new workflow](/rest-api/#create-a-workflow).

#### Endpoint

```
PUT /workflows/{id}
```

#### Path Parameters

<ParamField path="id" type="string" required>
  The ID of the workflow to update.

  To find your workflow ID, navigate to your workflow.

  If the URL is [https://pipedream.com/@michael-testing/api-p\_13CDnxK/inspect](https://pipedream.com/@michael-testing/api-p_13CDnxK/inspect), your `workflow_id` begins with `p_` and would be `p_13CDnxK`.
</ParamField>

#### Request Body

<ParamField body="active" type="boolean" required>
  The activation status of a workflow. Set to `true` to activate the workflow, or `false` to deactivate it.
</ParamField>

<ParamField body="org_id" type="string" required>
  [Find your org’s ID](/workspaces/#finding-your-workspaces-id).
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl -X PUT 'https://api.pipedream.com/v1/workflows/p_abc123' \
    -H 'Authorization: Bearer <token>' \
    -H 'Content-Type: application/json' \
    -d '{"active": false, "org_id": "o_BYDI5y"}'
  ```
</RequestExample>

Built with [Mintlify](https://mintlify.com).
