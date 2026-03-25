# Source: https://docs.knock.app/api-reference/tenants/bulk/set.md

# Source: https://docs.knock.app/api-reference/tenants/set.md

# Source: https://docs.knock.app/api-reference/objects/bulk/set.md

# Source: https://docs.knock.app/api-reference/objects/set.md

### Set an object

Creates a new object or updates an existing one in the specified collection. This operation is used to identify objects with their properties, as well as optional preferences and channel data.

#### Endpoint

`PUT /v1/objects/{collection}/{id}`

**Rate limit tier:** 3

#### Path parameters

- **collection** (string) *required* - The collection this object belongs to.
- **id** (string) *required* - Unique identifier for the object.

#### Request body

A set of parameters to set an object with. Does not include the object id or collection.

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
  "description": "My product description",
  "locale": "en-US",
  "name": "My product",
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
  "price": 100,
  "timezone": "America/New_York"
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "__typename": "Object",
  "collection": "assets",
  "created_at": null,
  "id": "specimen_25",
  "properties": {
    "classification": "Theropod",
    "config": {
      "biz": "baz",
      "foo": "bar"
    },
    "name": "Velociraptor",
    "status": "contained"
  },
  "updated_at": "2024-05-22T12:00:00Z"
}
```

