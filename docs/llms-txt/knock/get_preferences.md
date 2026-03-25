# Source: https://docs.knock.app/api-reference/objects/get_preferences.md

# Source: https://docs.knock.app/api-reference/users/get_preferences.md

### Get user preference set

Retrieves a specific preference set for a user identified by the preference set ID.

#### Endpoint

`GET /v1/users/{user_id}/preferences/{id}`

**Rate limit tier:** 4

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.
- **id** (string) *required* - Unique identifier for the preference set.

#### Query parameters

- **tenant** (string) - The unique identifier for the tenant.

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

