# Source: https://www.traceloop.com/docs/api-reference/privacy/delete_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete specific user data

You can delete traces data for a specific user of yours by specifying their association properties.

## Request Body

<ParamField body="associationProperties" type="JSON">
  A list of users to delete, each specific using a specific criterion for deletion like `{userId: "123"}`.
</ParamField>

```json  theme={null}
{
  "associationProperties": [
    {
      "userId": "123"
    }
  ]
}
```

## Response

<ResponseField name="requestId" type="string">
  The request ID for this deletion request. You can use it to query the status
  of the deletion.
</ResponseField>

```
```
