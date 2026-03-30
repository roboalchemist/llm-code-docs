# Source: https://docs.knock.app/api-reference/users/schemas/inline_identify_user_request.md

### InlineIdentifyUserRequest

A set of parameters to inline-identify a user with. Inline identifying the user will ensure that the user is available before the request is executed in Knock. It will perform an upsert for the user you're supplying, replacing any properties specified.

#### Attributes

- **avatar** (string) - A URL for the avatar of the user.
- **channel_data** (unknown) - Channel-specific information that's needed to deliver a notification to an end provider.
- **created_at** (string) - The creation date of the user from your system.
- **email** (string) - The primary email address for the user.
- **id** (string) *required* - The unique identifier of the user.
- **locale** (string) - The locale of the user. Used for [message localization](/concepts/translations).
- **name** (string) - Display name of the user.
- **phone_number** (string) - The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the user (required for SMS channels).
- **preferences** (unknown) - A set of preferences for the user.
- **timezone** (string) - The timezone of the user. Must be a valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Used for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).

#### Example

```json
{
  "channel_data": {
    "97c5837d-c65c-4d54-aa39-080eeb81c69d": {
      "tokens": [
        "push_token_123"
      ]
    }
  },
  "email": "jane@ingen.net",
  "id": "user_1",
  "name": "Jane Doe",
  "preferences": {
    "default": {
      "channel_types": {
        "email": true
      },
      "workflows": {
        "dinosaurs-loose": {
          "channel_types": {
            "email": true
          }
        }
      }
    }
  },
  "timezone": "America/New_York"
}
```

