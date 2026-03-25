# Source: https://docs.knock.app/mapi-reference/workflows/schemas/send_window.md

### SendWindow

A send window time for a notification. Describes a single day.

#### Attributes

- **day** (string) *required* - The day of the week.
- **from** (string) - The start time of the send window.
- **type** (string) *required* - The type of send window.
- **until** (string) - The end time of the send window.

#### Example

```json
{
  "day": "monday",
  "from": "09:00",
  "type": "send",
  "until": "17:00"
}
```

