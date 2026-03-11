# Source: https://docs.knock.app/mapi-reference/broadcasts/cancel.md

# Source: https://docs.knock.app/api-reference/workflows/cancel.md

### Cancel workflow

When invoked for a workflow using a specific workflow key and cancellation key, will cancel any queued workflow runs associated with that key/cancellation key pair. Can optionally be provided one or more recipients to scope the request to.

#### Endpoint

`POST /v1/workflows/{key}/cancel`

**Rate limit tier:** 5

#### Path parameters

- **key** (string) *required* - The key of the workflow to cancel.

#### Request body

When invoked using a specific workflow key and cancellation key, will cancel any queued workflow runs associated with that key/cancellation key pair. Can optionally provide one or more recipients to scope the request to.

##### Example

```json
{
  "cancellation_key": "cancel-workflow-123",
  "recipients": [
    "jhammond"
  ]
}
```

#### Responses

##### 204

No Content

