# Create Api Key

Source: https://docs.nomic.ai/reference/api/create-api-key-v-1-user-authorization-keys-organization-id-create-post

# Create Api Key

```
POST /v1/user/authorization/keys/:organization_id/create
```

## /v1/user/authorization/keys/:organization_id/create

Creates a new API key with specified scope and permissions.

By default, API keys are scoped to an organization. Additionally, API keys can also be scoped to a specific dataset or a specific user.

If only key_name is provided in the request for creating an API key, the key will be scoped to the user's current organization.

To scope an API key to a specific organization by ID, set key_scope = "ORGANIZATION" and key_target_id with the UUID of the organization in the API key creation request.

To scope an API key to a specific dataset, set key_scope = "DATASET" and key_target_id with the UUID of the dataset in the API key creation request.

To scope an API key to a specific user, set key_scope = "USER" in the API key creation request.

## Request​

### Path Parameters

Path Parameters

- application/json
### Body

Body

required

The name of the API key to create.

key_role

object

The role associated to the API key scope

anyOf

- AccessRole
- DatasetRole
string

Possible values: [OWNER, ADMIN, MEMBER, VIEWER, EXTERNAL, GUEST, NONE]

```
OWNER
```

```
ADMIN
```

```
MEMBER
```

```
VIEWER
```

```
EXTERNAL
```

```
GUEST
```

```
NONE
```

string

Possible values: [ADMIN, EDITOR, VIEWER, EXTERNAL, NONE]

```
ADMIN
```

```
EDITOR
```

```
VIEWER
```

```
EXTERNAL
```

```
NONE
```

Possible values: [ORGANIZATION, DATASET, USER]

```
ORGANIZATION
```

```
DATASET
```

```
USER
```

Default value: ORGANIZATION

```
ORGANIZATION
```

The scope of the API key: ORGANIZATION, DATASET, or USER

key_target_id

object

The UUID representing a dataset id or an organization id

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

The API key that was created

```
{  "key": "string"}
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

