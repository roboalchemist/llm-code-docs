# Source: https://docs.knock.app/api-reference/recipients/preferences/schemas/preference_set_channel_type_setting.md

### PreferenceSetChannelTypeSetting

A set of settings for a channel type. Currently, this can only be a list of conditions to apply.

#### Attributes

- **conditions** (array) *required* - A list of conditions to apply to a channel type.

#### Example

```json
{
  "conditions": [
    {
      "argument": "US",
      "operator": "equal_to",
      "variable": "recipient.country_code"
    }
  ]
}
```

