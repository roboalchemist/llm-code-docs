# Source: https://ngrok.com/docs/iam/service-users.md

# Source: https://ngrok.com/docs/api-reference/service-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Service Users (Bot Users)

> Service Users API reference.

<Note>
  Service Users were previously called Bot Users.

  The Bot User API endpoint is still available but will be deprecated in the future.
  If you need the Bot Users API reference, you can find it [here](/api-reference/botusers/get).
</Note>

## Create Service User

Create a new Service User.

### Request

`POST /service_users`

#### Example request

```bash  theme={null}
curl \
-X POST \
-H "Authorization: Bearer {API_KEY}" \
-H "Content-Type: application/json" \
-H "Ngrok-Version: 2" \
-d '{"name":"new service user from API"}' \
https://api.ngrok.com/service_users
```

#### Parameters

| Name     | Type    | Description                                            |
| -------- | ------- | ------------------------------------------------------ |
| `name`   | string  | Human-readable name used to identify the Service User. |
| `active` | boolean | Whether or not the Service User is active.             |

### Response

Returns a 201 response on success.

#### Example response

```json  theme={null}
{
  "active": true,
  "created_at": "2025-09-04T10:11:43Z",
  "id": "service_32ELIFubEAAGUeRtreNW6kr94Od",
  "name": "new service user from API",
  "uri": "https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od"
}
```

#### Fields

| Name         | Type    | Description                                                 |
| ------------ | ------- | ----------------------------------------------------------- |
| `id`         | string  | Unique API key resource identifier.                         |
| `uri`        | string  | URI to the API resource of this Service User                |
| `name`       | string  | Human-readable name used to identify the Service User.      |
| `active`     | boolean | Whether or not the Service User is active.                  |
| `created_at` | string  | Timestamp when the API key was created, in RFC 3339 format. |

## Delete Service User

Delete a Service User by ID.

### Request

`DELETE /service_users/\{id\}`

#### Example request

```bash  theme={null}
curl \
-X DELETE \
-H "Authorization: Bearer {API_KEY}" \
-H "Ngrok-Version: 2" \
https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od
```

### Response

Returns a 204 response with no body on success.

## Get Service User

Get the details of a Service User by ID.

### Request

`GET /service_users/\{id\}`

#### Example request

```bash  theme={null}
curl \
-X GET \
-H "Authorization: Bearer {API_KEY}" \
-H "Ngrok-Version: 2" \
https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od
```

### Response

Returns a 200 response on success.

#### Example response

```json  theme={null}
{
  "active": true,
  "created_at": "2025-09-04T10:11:43Z",
  "id": "service_32ELIFubEAAGUeRtreNW6kr94Od",
  "name": "new service user from API",
  "uri": "https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od"
}
```

#### Fields

| Name         | Type    | Description                                                 |
| ------------ | ------- | ----------------------------------------------------------- |
| `id`         | string  | Unique API key resource identifier.                         |
| `uri`        | string  | URI to the API resource of this Service User.               |
| `name`       | string  | Human-readable name used to identify the Service User.      |
| `active`     | boolean | Whether or not the Service User is active.                  |
| `created_at` | string  | Timestamp when the API key was created, in RFC 3339 format. |

## List Service Users

List all Service Users in this account.

### Request

`GET /service_users`

#### Example request

```bash  theme={null}
curl \
-X GET \
-H "Authorization: Bearer {API_KEY}" \
-H "Ngrok-Version: 2" \
https://api.ngrok.com/service_users?limit=1
```

### Response

Returns a 200 response on success.

#### Example response

```json  theme={null}
{
  "service_users": [
    {
      "active": true,
      "created_at": "2025-09-04T10:11:43Z",
      "id": "service_32ELIKFMeMYDQm0tERqc5MmICl4",
      "name": "API example service user",
      "uri": "https://api.ngrok.com/service_users/service_32ELIKFMeMYDQm0tERqc5MmICl4"
    }
  ],
  "next_page_uri": "https://api.ngrok.com/service_users?before_id=service_32ELIKFMeMYDQm0tERqc5MmICl4&limit=1",
  "uri": "https://api.ngrok.com/service_users"
}
```

#### Fields

| Name            | Type                               | Description                                             |
| --------------- | ---------------------------------- | ------------------------------------------------------- |
| `service_users` | [ServiceUser](#serviceuser-fields) | List of all Service Users on this account.              |
| `uri`           | string                             | URI of the Service Users list API resource.             |
| `next_page_uri` | string                             | URI of the next page, or null if there is no next page. |

#### ServiceUser fields

| Name         | Type    | Description                                                 |
| ------------ | ------- | ----------------------------------------------------------- |
| `id`         | string  | Unique API key resource identifier.                         |
| `uri`        | string  | URI to the API resource of this Service User.               |
| `name`       | string  | Human-readable name used to identify the Service User.      |
| `active`     | boolean | Whether or not the Service User is active.                  |
| `created_at` | string  | Timestamp when the API key was created, in RFC 3339 format. |

## Update Service User

Update attributes of a Service User by ID.

### Request

`PATCH /service_users/\{id\}`

#### Example request

```bash  theme={null}
curl \
-X PATCH \
-H "Authorization: Bearer {API_KEY}" \
-H "Content-Type: application/json" \
-H "Ngrok-Version: 2" \
-d '{"active":false,"name":"inactive service user from API"}' \
https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od
```

#### Parameters

| Name     | Type    | Description                                            |
| -------- | ------- | ------------------------------------------------------ |
| `id`     | string  |                                                        |
| `name`   | string  | Human-readable name used to identify the Service User. |
| `active` | boolean | Whether or not the Service User is active.             |

### Response

Returns a 200 response and a copy of the updated entity on success.

#### Example response

```json  theme={null}
{
  "active": false,
  "created_at": "2025-09-04T10:11:43Z",
  "id": "service_32ELIFubEAAGUeRtreNW6kr94Od",
  "name": "inactive service user from API",
  "uri": "https://api.ngrok.com/service_users/service_32ELIFubEAAGUeRtreNW6kr94Od"
}
```

#### Fields

| Name         | Type    | Description                                                 |
| ------------ | ------- | ----------------------------------------------------------- |
| `id`         | string  | Unique API key resource identifier.                         |
| `uri`        | string  | URI to the API resource of this Service User.               |
| `name`       | string  | Human-readable name used to identify the Service User.      |
| `active`     | boolean | Whether or not the Service User is active.                  |
| `created_at` | string  | Timestamp when the API key was created, in RFC 3339 format. |


Built with [Mintlify](https://mintlify.com).