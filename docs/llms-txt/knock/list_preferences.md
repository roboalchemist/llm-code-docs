# Source: https://docs.knock.app/api-reference/objects/list_preferences.md

# Source: https://docs.knock.app/api-reference/users/list_preferences.md

### List user preference sets

Retrieves a list of all preference sets for a specific user.

#### Endpoint

`GET /v1/users/{user_id}/preferences`

**Rate limit tier:** 4

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.

#### Responses

##### 200

OK

###### Example

```json
[
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
]
```

