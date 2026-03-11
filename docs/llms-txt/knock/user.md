# Source: https://docs.knock.app/api-reference/users/schemas/user.md

### User

A [User](/concepts/users) represents an individual in your system who can receive notifications through Knock. Users are the most common recipients of notifications and are always referenced by your internal identifier.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **avatar** (string) - A URL for the avatar of the user.
- **created_at** (string) - The creation date of the user from your system.
- **email** (string) - The primary email address for the user.
- **id** (string) *required* - The unique identifier of the user.
- **name** (string) - Display name of the user.
- **phone_number** (string) - The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the user (required for SMS channels).
- **timezone** (string) - The timezone of the user. Must be a valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Used for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
- **updated_at** (string) *required* - The timestamp when the resource was last updated.

#### Example

```json
{
  "__typename": "User",
  "created_at": null,
  "email": "ian.malcolm@chaos.theory",
  "id": "user_id",
  "name": "Dr. Ian Malcolm",
  "updated_at": "2024-05-22T12:00:00Z"
}
```

