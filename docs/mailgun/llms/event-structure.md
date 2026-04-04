# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/event-structure.md

# Event Structure

Events are represented as loosely structured JSON documents. The exact event structure depends on the event type. But there are three fields that every event has. They are as follows:

| Field | Description |
|  --- | --- |
| event | The type of the event. Events of a particular type have an identical structure, though some fields may be optional. For the list of event types please refer to Event Types. |
| timestamp | The time when the event was generated in the system provided as Unix epoch seconds. |
| id | The event ID, unique within a day. It can be used to distinguish events that have already been retrieved when requests with overlapping time ranges are made. |


Events can change their structure as new features are added to Mailgun, but we only add new fields and never modify or remove existing ones.