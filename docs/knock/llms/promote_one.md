# Source: https://docs.knock.app/mapi-reference/commits/promote_one.md

### Promote one commit

Promotes one change to the subsequent environment.

#### Endpoint

`PUT /v1/commits/{id}/promote`

#### Path parameters

- **id** (string) *required* - The target commit ID to promote to the subsequent environment.

#### Responses

##### 200

OK

###### Example

```json
{
  "commit": {
    "author": {
      "email": "john.doe@example.com",
      "name": "John Doe"
    },
    "commit_message": "This is a commit message",
    "created_at": "2021-01-01T00:00:00Z",
    "environment": "development",
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "resource": {
      "identifier": "my-email-layout",
      "type": "email_layout"
    }
  }
}
```

