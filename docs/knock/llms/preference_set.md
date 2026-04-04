# Source: https://docs.knock.app/api-reference/recipients/preferences/schemas/preference_set.md

### PreferenceSet

A preference set represents a specific set of notification preferences for a recipient. A recipient can have multiple preference sets.

#### Attributes

- **categories** (unknown) - An object where the key is the category and the values are the preference settings for that category.
- **channel_types** (unknown) - An object where the key is the channel type and the values are the preference settings for that channel type.
- **channels** (unknown) - An object where the key is the channel ID and the values are the preference settings for that channel ID.
- **commercial_subscribed** (boolean) - Whether the recipient is subscribed to commercial communications. When false, the recipient will not receive commercial workflow notifications.
- **id** (string) *required* - Unique identifier for the preference set.
- **workflows** (unknown) - An object where the key is the workflow key and the values are the preference settings for that workflow.

#### Example

```json
{
  "categories": {
    "marketing": false,
    "transactional": {
      "channel_types": {
        "email": false
      }
    }
  },
  "channel_types": {
    "email": true,
    "push": false,
    "sms": {
      "conditions": [
        {
          "argument": "US",
          "operator": "equal_to",
          "variable": "recipient.country_code"
        }
      ]
    }
  },
  "commercial_subscribed": true,
  "id": "default",
  "workflows": null
}
```

