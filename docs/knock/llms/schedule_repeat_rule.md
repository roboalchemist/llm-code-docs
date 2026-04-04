# Source: https://docs.knock.app/api-reference/schedules/schemas/schedule_repeat_rule.md

### ScheduleRepeatRule

The repeat rule for the schedule.

#### Attributes

- **__typename** (string) - The typename of the schema.
- **day_of_month** (integer) - The day of the month to repeat the schedule.
- **days** (array) - The days of the week to repeat the schedule.
- **frequency** (string) *required* - The frequency of the schedule.
- **hours** (integer) - The hour of the day to repeat the schedule.
- **interval** (integer) - The interval of the schedule.
- **minutes** (integer) - The minute of the hour to repeat the schedule.

#### Example

```json
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
```

