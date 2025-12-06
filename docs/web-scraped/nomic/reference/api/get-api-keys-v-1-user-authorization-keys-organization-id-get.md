# Get Api Keys

Source: https://docs.nomic.ai/reference/api/get-api-keys-v-1-user-authorization-keys-organization-id-get

# Get Api Keys

```
GET /v1/user/authorization/keys/:organization_id
```

## /v1/user/authorization/keys/:organization_id

Get Api Keys

## Request​

### Path Parameters

Path Parameters

## Responses​

- 200
- 422
Successful Response

- application/json
- Schema
- Example (from schema)
Schema

keys

object[]

- Array [
Array [

- ]
]

```
{  "keys": [    {      "key_name": "string",      "expiration": "2024-07-29T15:51:28.071Z",      "creation": "2024-07-29T15:51:28.071Z",      "suffix": "string",      "user_id": "string"    }  ]}
```

Validation Error

- application/json
- Schema
- Example (from schema)
Schema

detail

object[]

- Array [
Array [

loc

object[]

required

- Array [
Array [

anyOf

- MOD1
- MOD2
string

integer

- ]
]

- ]
]

```
{  "detail": [    {      "loc": [        "string",        0      ],      "msg": "string",      "type": "string"    }  ]}
```

