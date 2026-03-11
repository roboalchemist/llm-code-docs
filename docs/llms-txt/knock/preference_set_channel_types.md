# Source: https://docs.knock.app/api-reference/recipients/preferences/schemas/preference_set_channel_types.md

### PreferenceSetChannelTypes

Channel type preferences.

#### Attributes

- **chat** (unknown) - Whether the channel type is enabled for the preference set.
- **email** (unknown) - Whether the channel type is enabled for the preference set.
- **http** (unknown) - Whether the channel type is enabled for the preference set.
- **in_app_feed** (unknown) - Whether the channel type is enabled for the preference set.
- **push** (unknown) - Whether the channel type is enabled for the preference set.
- **sms** (unknown) - Whether the channel type is enabled for the preference set.

#### Example

```json
{
  "email": true,
  "sms": {
    "conditions": [
      {
        "argument": "US",
        "operator": "equal_to",
        "variable": "recipient.country_code"
      }
    ]
  }
}
```

