# Source: https://docs.knock.app/api-reference/schedules/schemas/schedule.md

### Schedule

A schedule represents a recurring workflow execution.

#### Attributes

- **__typename** (string) - The typename of the schema.
- **actor** (unknown) - A map of properties describing a user or an object to identify in Knock and mark as who or what performed the action.
- **data** (object) - An optional map of data to pass into the workflow execution. There is a 10MB limit on the size of the full `data` payload. Any individual string value greater than 1024 bytes in length will be [truncated](/developer-tools/api-logs#log-truncation) in your logs.
- **id** (string) *required* - Unique identifier for the schedule.
- **inserted_at** (string) *required* - Timestamp when the resource was created.
- **last_occurrence_at** (string) - The last occurrence of the schedule.
- **next_occurrence_at** (string) - The next occurrence of the schedule.
- **recipient** (object) *required* - A recipient of a notification, which is either a user or an object.
- **repeats** (array) *required* - The repeat rule for the schedule.
- **tenant** (string) - The tenant to trigger the workflow for. Triggering with a tenant will use any tenant-level overrides associated with the tenant object, and all messages produced from workflow runs will be tagged with the tenant.
- **updated_at** (string) *required* - The timestamp when the resource was last updated.
- **workflow** (string) *required* - The workflow the schedule is applied to.

#### Example

```json
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
```

