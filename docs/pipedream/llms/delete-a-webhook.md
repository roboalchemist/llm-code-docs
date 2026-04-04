# Source: https://pipedream.com/docs/rest-api/api-reference/webhooks/delete-a-webhook.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a webhook

Use this endpoint to delete a webhook in your account.

#### Endpoint

```
DELETE /webhooks/{id}
```

#### Path Parameters

<ParamField body="id" type="string" required>
  The ID of a webhook in your account.
</ParamField>

***

<RequestExample>
  ```bash  theme={null}
  curl "https://api.pipedream.com/v1/webhooks/wh_abc123" \
    -X DELETE \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

Built with [Mintlify](https://mintlify.com).
