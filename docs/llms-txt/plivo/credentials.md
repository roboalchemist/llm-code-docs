# Source: https://plivo.com/docs/sip-trunking/api/credentials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Credentials

> Manage SIP credentials for digest authentication on outbound trunks

The Credentials API lets you create and manage username/password pairs for SIP digest authentication on outbound trunks.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/
```

***

## The Credentials Object

A credentials object contains username and password for SIP digest authentication when your PBX sends calls to Plivo.

### Attributes

<ParamField body="credential_uuid" type="string">
  Unique identifier for the credentials.
</ParamField>

<ParamField body="name" type="string">
  Friendly name for the credentials.
</ParamField>

<ParamField body="username" type="string">
  Username for SIP authentication.
</ParamField>

<ParamField body="password" type="string">
  Password for SIP authentication (only set on create/update, never returned in responses).
</ParamField>

### Example Object

```json  theme={null}
{
  "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "my-credentials",
  "username": "sip_user_1"
}
```

<Note>
  The password is never returned in API responses for security. It is only used when creating or updating credentials.
</Note>

***

## List All Credentials

Get all credentials for your account.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/`

### Query Parameters

| Parameter | Type    | Required | Default | Description             |
| --------- | ------- | -------- | ------- | ----------------------- |
| `limit`   | integer | No       | 20      | Results per page (1-20) |
| `offset`  | integer | No       | 0       | Pagination offset       |

### Response

```json  theme={null}
{
  "api_id": "a04ad809-3b78-4bbe-9baf-acfc7800b10f",
  "meta": {
    "limit": 20,
    "offset": 0,
    "total_count": 109,
    "previous": null,
    "next": "v1/Account/{auth_id}/Zentrunk/Credential/?limit=20&offset=20"
  },
  "objects": [
    {
      "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
      "name": "production-credentials",
      "username": "sipuser123"
    },
    {
      "credential_uuid": "c4773-4ae6-4b75-92ea-9cf3ea4227d6",
      "name": "staging-credentials",
      "username": "sipuser456"
    }
  ]
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  # List all credentials
  response = client.zentrunk.credentials.list()
  print(response)

  # List with pagination
  response = client.zentrunk.credentials.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  // List all credentials
  client.zentrunk.credentials.list()
    .then(response => console.log(response));

  // List with pagination
  client.zentrunk.credentials.list({limit: 10, offset: 0})
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Retrieve Credentials

Get details of specific credentials.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/{credential_uuid}/`

### Response

```json  theme={null}
{
  "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "my-credentials",
  "username": "sip_user_1"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.credentials.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.credentials.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Create Credentials

Create a new credential set for SIP digest authentication.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/`

### Request Parameters

| Parameter  | Type   | Required | Default | Description                       |
| ---------- | ------ | -------- | ------- | --------------------------------- |
| `name`     | string | No       | -       | Friendly name for the credentials |
| `username` | string | Yes      | -       | Username for SIP authentication   |
| `password` | string | Yes      | -       | Password for SIP authentication   |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "credential created successfully.",
  "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

### Error Codes

| Code | Description                                        |
| ---- | -------------------------------------------------- |
| 400  | Invalid request parameters                         |
| 401  | Authentication failed                              |
| 422  | Missing required parameters (username or password) |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "production-credentials",
        "username": "sipuser123",
        "password": "securepassword123!"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.credentials.create(
      name='production-credentials',
      username='sipuser123',
      password='securepassword123!'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.credentials.create({
    name: 'production-credentials',
    username: 'sipuser123',
    password: 'securepassword123!'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Update Credentials

Modify an existing credential's name, username, or password.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/{credential_uuid}/`

### Request Parameters

| Parameter  | Type   | Required | Default | Description       |
| ---------- | ------ | -------- | ------- | ----------------- |
| `name`     | string | No       | -       | New friendly name |
| `username` | string | No       | -       | New username      |
| `password` | string | No       | -       | New password      |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "Credential updated successfully.",
  "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"username": "newuser", "password": "newpassword123!"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.credentials.update(
      'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6',
      username='newuser',
      password='newpassword123!'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.credentials.update('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6', {
    username: 'newuser',
    password: 'newpassword123!'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Delete Credentials

Permanently delete credentials.

### HTTP Request

`DELETE https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/{credential_uuid}/`

### Response

HTTP 204 No Content

<Warning>
  Deleting credentials that are attached to an active trunk will break authentication for that trunk.
</Warning>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Credential/{credential_uuid}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.credentials.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.credentials.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Usage with Trunks

After creating credentials, attach them to an outbound trunk.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "outbound-trunk",
        "trunk_direction": "outbound",
        "credential_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.create(
      name='outbound-trunk',
      trunk_direction='outbound',
      credential_uuid='f19c4773-4ae6-4b75-92ea-9cf3ea4227d6'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.create({
    name: 'outbound-trunk',
    trunkDirection: 'outbound',
    credentialUuid: 'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Related

* [Trunks](/sip-trunking/api/trunks/) - Create and manage SIP trunks
* [IP Access Control Lists](/sip-trunking/api/ip-access-control-lists/) - Alternative authentication via IP whitelisting
