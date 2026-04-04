# Source: https://docs.knock.app/api-reference/audiences/list_members.md

### List members

Returns a paginated list of members for the specified audience.

#### Endpoint

`GET /v1/audiences/{key}/members`

**Rate limit tier:** 4

#### Path parameters

- **key** (string) *required* - The key of the audience.

#### Responses

##### 200

OK

###### Example

```json
{
  "entries": [
    {
      "__typename": "AudienceMember",
      "added_at": "1993-06-10T14:30:00Z",
      "tenant": "ingen_isla_nublar",
      "user": {
        "__typename": "User",
        "created_at": null,
        "email": "alan.grant@dig.site.mt",
        "id": "dr_grant",
        "name": "Dr. Alan Grant",
        "updated_at": "1993-06-09T08:15:00Z"
      },
      "user_id": "dr_grant"
    }
  ],
  "page_info": {
    "__typename": "PageInfo",
    "after": null,
    "before": null,
    "page_size": 25
  }
}
```

