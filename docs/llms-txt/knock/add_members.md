# Source: https://docs.knock.app/api-reference/audiences/add_members.md

### Add members

Adds one or more members to the specified audience.

#### Endpoint

`POST /v1/audiences/{key}/members`

**Rate limit tier:** 3

#### Path parameters

- **key** (string) *required* - The key of the audience.

#### Query parameters

- **create_audience** (boolean) - Create the audience if it does not exist.

#### Request body

A request to add a list of audience members.

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

