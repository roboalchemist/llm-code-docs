# Source: https://docs.knock.app/api-reference/recipients/preferences/schemas/inline_preference_set_request.md

### InlinePreferenceSetRequest

Inline set preferences for a recipient, where the key is the preference set id. Preferences that are set inline will be merged into any existing preferences rather than replacing them.

#### Attributes

#### Example

```json
{
  "default": {
    "categories": {
      "transactional": {
        "channel_types": {
          "email": false
        }
      }
    },
    "channel_types": {
      "email": true
    }
  }
}
```

