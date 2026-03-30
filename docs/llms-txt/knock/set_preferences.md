# Source: https://docs.knock.app/api-reference/objects/set_preferences.md

# Source: https://docs.knock.app/api-reference/users/bulk/set_preferences.md

# Source: https://docs.knock.app/api-reference/users/set_preferences.md

### Update user preference set

Updates a complete preference set for a user. By default, this is a destructive operation and will replace any existing preferences with the preferences given. Use '__persistence_strategy__': 'merge' to merge with existing preferences instead.

#### Endpoint

`PUT /v1/users/{user_id}/preferences/{id}`

**Rate limit tier:** 3

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.
- **id** (string) *required* - Unique identifier for the preference set.

#### Request body

A request to set a preference set for a recipient.

##### Example

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

#### Responses

##### 200

OK

###### Example

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

