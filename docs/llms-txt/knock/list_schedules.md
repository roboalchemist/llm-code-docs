# Source: https://docs.knock.app/api-reference/objects/list_schedules.md

# Source: https://docs.knock.app/api-reference/users/list_schedules.md

### List user schedules

Returns a paginated list of schedules for a specific user, in descending order.

#### Endpoint

`GET /v1/users/{user_id}/schedules`

**Rate limit tier:** 4

#### Path parameters

- **user_id** (string) *required* - The user ID to list schedules for.

#### Query parameters

- **workflow** (string) - The workflow key to filter schedules for.
- **tenant** (string) - The tenant ID to filter schedules for.
- **after** (string) - The cursor to fetch entries after.
- **before** (string) - The cursor to fetch entries before.
- **page_size** (integer) - The number of items per page (defaults to 50).

#### Responses

##### 200

OK

###### Example

```json
{
  "entries": [
    {
      "__typename": "Schedule",
      "actor": null,
      "data": null,
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "inserted_at": "2021-01-01T00:00:00Z",
      "last_occurrence_at": null,
      "next_occurrence_at": null,
      "recipient": {
        "__typename": "User",
        "avatar": null,
        "created_at": null,
        "email": "jane@ingen.net",
        "id": "jane",
        "name": "Jane Doe",
        "phone_number": null,
        "timezone": null,
        "updated_at": "2024-05-22T12:00:00Z"
      },
      "repeats": [
        {
          "__typename": "ScheduleRepeat",
          "day_of_month": null,
          "days": [
            "mon",
            "tue",
            "wed",
            "thu",
            "fri",
            "sat",
            "sun"
          ],
          "frequency": "daily",
          "hours": null,
          "interval": 1,
          "minutes": null
        }
      ],
      "tenant": null,
      "updated_at": "2021-01-01T00:00:00Z",
      "workflow": "workflow_123"
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

