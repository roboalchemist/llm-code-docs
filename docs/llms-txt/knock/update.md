# Source: https://docs.knock.app/api-reference/schedules/update.md

# Source: https://docs.knock.app/api-reference/users/update.md

### Identify user

Create or update a user with the provided identification data. When you identify an existing user, the system merges the properties you specific with what is currently set on the user, updating only the fields included in your requests.

#### Endpoint

`PUT /v1/users/{user_id}`

**Rate limit tier:** 3

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.

#### Request body

A set of parameters to identify a user with. Does not include the user ID, as that's specified elsewhere in the request. You can supply any additional properties you'd like to upsert for the user.

##### Example

```json
{
  "channel_data": {
    "97c5837d-c65c-4d54-aa39-080eeb81c69d": {
      "tokens": [
        "push_token_123"
      ]
    }
  },
  "email": "ian.malcolm@chaos.theory",
  "name": "Dr. Ian Malcolm",
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

#### Responses

##### 200

OK

###### Example

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

