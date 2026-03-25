# Source: https://docs.knock.app/api-reference/recipients/preferences/schemas/preference_set_request.md

### PreferenceSetRequest

A request to set a preference set for a recipient.

#### Attributes

- **__persistence_strategy__** (string) - Controls how the preference set is persisted. 'replace' will completely replace the preference set, 'merge' will merge with existing preferences.
- **categories** (unknown) - An object where the key is the category and the values are the preference settings for that category.
- **channel_types** (unknown) - An object where the key is the channel type and the values are the preference settings for that channel type.
- **channels** (unknown) - An object where the key is the channel ID and the values are the preference settings for that channel ID.
- **commercial_subscribed** (boolean) - Whether the recipient is subscribed to commercial communications. When false, the recipient will not receive commercial workflow notifications.
- **workflows** (unknown) - An object where the key is the workflow key and the values are the preference settings for that workflow.

#### Example

```json
{
  "__persistence_strategy__": "merge",
  "categories": {
    "marketing": false,
    "transactional": {
      "channel_types": {
        "email": false
      }
    }
  },
  "channel_types": {
    "email": true
  },
  "channels": {
    "2f641633-95d3-4555-9222-9f1eb7888a80": {
      "conditions": [
        {
          "argument": "US",
          "operator": "equal_to",
          "variable": "recipient.country_code"
        }
      ]
    },
    "aef6e715-df82-4ab6-b61e-b743e249f7b6": true
  },
  "commercial_subscribed": true,
  "workflows": {
    "dinosaurs-loose": {
      "channel_types": {
        "email": false
      }
    }
  }
}
```

