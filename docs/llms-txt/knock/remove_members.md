# Source: https://docs.knock.app/api-reference/audiences/remove_members.md

### Remove members

Removes one or more members from the specified audience.

#### Endpoint

`DELETE /v1/audiences/{key}/members`

**Rate limit tier:** 3

#### Path parameters

- **key** (string) *required* - The key of the audience.

#### Request body

A request to remove a list of audience members.

##### Example

```json
{
  "members": [
    {
      "tenant": "ingen_isla_nublar",
      "user": {
        "email": "ellie@ingen.net",
        "id": "dr_sattler",
        "name": "Dr. Ellie Sattler"
      }
    }
  ]
}
```

#### Responses

##### 204

No Content

