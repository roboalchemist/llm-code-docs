# Delete Api Key

Source: https://docs.nomic.ai/reference/api/delete-api-key-v-1-user-authorization-keys-organization-id-delete-post

# Delete Api Key

```
POST /v1/user/authorization/keys/:organization_id/delete
```

## /v1/user/authorization/keys/:organization_id/delete

Delete Api Key

## Request​

### Path Parameters

Path Parameters

- application/json
### Body

Body

required

The name of the key to deleted.

user_id

object

User id

anyOf

- MOD1
string

## Responses​

- 200
- 422
Successful Response

- application/json
- Schema
- Example (from schema)
Schema

Default value: ok

```
ok
```

```
{  "result": "ok"}
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

