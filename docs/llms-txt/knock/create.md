# Source: https://docs.knock.app/mapi-reference/branches/create.md

# Source: https://docs.knock.app/cli/branch/create.md

# Source: https://docs.knock.app/api-reference/schedules/bulk/create.md

# Source: https://docs.knock.app/api-reference/schedules/create.md

### Create schedules

Creates one or more schedules for a workflow with the specified recipients, timing, and data. Schedules can be one-time or recurring. This endpoint also handles [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients) for the `actor`, `recipient`, and `tenant` fields.

#### Endpoint

`POST /v1/schedules`

**Rate limit tier:** 3

#### Request body

A request to create a schedule.

##### Example

```json
{
  "data": {
    "key": "value"
  },
  "ending_at": null,
  "recipients": [
    "user_123"
  ],
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
  "scheduled_at": null,
  "tenant": "acme_corp",
  "workflow": "comment-created"
}
```

#### Responses

##### 200

OK

###### Example

```json
[
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
]
```

