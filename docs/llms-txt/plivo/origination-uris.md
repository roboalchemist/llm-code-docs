# Source: https://plivo.com/docs/sip-trunking/api/origination-uris.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Origination URIs

> Manage destination endpoints for inbound SIP trunks

The Origination URIs API lets you create and manage destination endpoints (your PBX/infrastructure) where Plivo sends inbound calls.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/
```

***

## The Origination URI Object

An origination URI represents a destination endpoint where Plivo forwards inbound calls on your SIP trunk.

### Attributes

<ParamField body="uri_uuid" type="string">
  Unique identifier for the origination URI.
</ParamField>

<ParamField body="name" type="string">
  Friendly name for the origination URI.
</ParamField>

<ParamField body="uri" type="string">
  FQDN or IP address of your VoIP infrastructure.
</ParamField>

<ParamField body="authentication_needed" type="boolean">
  Whether Plivo should authenticate when sending calls.
</ParamField>

<ParamField body="username" type="string">
  Username for authentication (if enabled).
</ParamField>

<ParamField body="password" type="string">
  Password for authentication (only set on create/update, never returned in responses).
</ParamField>

### Example Object

```json  theme={null}
{
  "uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "primary-pbx",
  "uri": "sip.example.com",
  "authentication_needed": true,
  "username": "plivo_inbound"
}
```

***

## List All Origination URIs

Get all origination URIs for your account.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/`

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
    "next": "v1/Account/{auth_id}/Zentrunk/URI/?limit=20&offset=20"
  },
  "objects": [
    {
      "uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
      "name": "primary-pbx",
      "uri": "sip.example.com",
      "authentication_needed": true,
      "username": "plivo_inbound"
    },
    {
      "uri_uuid": "aec4773-4ae6-4b75-92ea-9cf3ea4227d6",
      "name": "backup-pbx",
      "uri": "sip-backup.example.com",
      "authentication_needed": false,
      "username": null
    }
  ]
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  # List all origination URIs
  response = client.zentrunk.origination_uris.list()
  print(response)

  # List with pagination
  response = client.zentrunk.origination_uris.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  // List all origination URIs
  client.zentrunk.originationUris.list()
    .then(response => console.log(response));

  // List with pagination
  client.zentrunk.originationUris.list({limit: 10, offset: 0})
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Retrieve an Origination URI

Get details of a specific origination URI.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/{uri_uuid}/`

### Response

```json  theme={null}
{
  "uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "primary-pbx",
  "uri": "sip.example.com:5060",
  "authentication_needed": true,
  "username": "plivo_inbound"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.origination_uris.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.originationUris.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Create an Origination URI

Create a new destination endpoint for inbound calls.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/`

### Request Parameters

| Parameter               | Type    | Required    | Default | Description                                                 |
| ----------------------- | ------- | ----------- | ------- | ----------------------------------------------------------- |
| `name`                  | string  | No          | -       | Friendly name for the URI                                   |
| `uri`                   | string  | Yes         | -       | FQDN or IP address of your VoIP infrastructure              |
| `authentication_needed` | boolean | No          | `false` | Require authentication                                      |
| `username`              | string  | Conditional | -       | Username for auth. Required if `authentication_needed=true` |
| `password`              | string  | Conditional | -       | Password for auth. Required if `authentication_needed=true` |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "Origination URI created successfully.",
  "uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

### Error Codes

| Code | Description                                                               |
| ---- | ------------------------------------------------------------------------- |
| 400  | Invalid request parameters                                                |
| 401  | Authentication failed                                                     |
| 422  | Missing required parameters (uri, or username/password when auth enabled) |

### Without Authentication

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "primary-pbx",
        "uri": "sip.example.com:5060"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.origination_uris.create(
      name='primary-pbx',
      uri='sip.example.com:5060'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.originationUris.create({
    name: 'primary-pbx',
    uri: 'sip.example.com:5060'
  }).then(response => console.log(response));
  ```
</CodeGroup>

### With Authentication

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "secure-pbx",
        "uri": "sip.example.com:5060",
        "authentication_needed": true,
        "username": "plivo_inbound",
        "password": "securepassword123!"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.origination_uris.create(
      name='secure-pbx',
      uri='sip.example.com:5060',
      authentication_needed=True,
      username='plivo_inbound',
      password='securepassword123!'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.originationUris.create({
    name: 'secure-pbx',
    uri: 'sip.example.com:5060',
    authenticationNeeded: true,
    username: 'plivo_inbound',
    password: 'securepassword123!'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Update an Origination URI

Modify an existing origination URI's properties.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/{uri_uuid}/`

### Request Parameters

| Parameter               | Type    | Required | Default | Description                    |
| ----------------------- | ------- | -------- | ------- | ------------------------------ |
| `name`                  | string  | No       | -       | New friendly name              |
| `uri`                   | string  | No       | -       | New FQDN or IP address         |
| `authentication_needed` | boolean | No       | -       | Enable/disable authentication  |
| `username`              | string  | No       | -       | New username (if auth enabled) |
| `password`              | string  | No       | -       | New password (if auth enabled) |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "origination uri updated successfully.",
  "uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "uri": "new-sip.example.com:5060",
        "authentication_needed": true,
        "username": "new_user",
        "password": "new_password123!"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.origination_uris.update(
      'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6',
      uri='new-sip.example.com:5060',
      authentication_needed=True,
      username='new_user',
      password='new_password123!'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.originationUris.update('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6', {
    uri: 'new-sip.example.com:5060',
    authenticationNeeded: true,
    username: 'new_user',
    password: 'new_password123!'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Delete an Origination URI

Permanently delete an origination URI.

### HTTP Request

`DELETE https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/{uri_uuid}/`

### Response

HTTP 204 No Content

<Warning>
  Deleting an origination URI that is attached to an active trunk as primary or fallback will cause inbound calls to fail.
</Warning>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/URI/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.origination_uris.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.originationUris.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Usage with Inbound Trunks

After creating origination URIs, attach them to an inbound trunk.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "inbound-trunk",
        "trunk_direction": "inbound",
        "primary_uri_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
        "fallback_uri_uuid": "aec4773-4ae6-4b75-92ea-9cf3ea4227d6"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.create(
      name='inbound-trunk',
      trunk_direction='inbound',
      primary_uri_uuid='f19c4773-4ae6-4b75-92ea-9cf3ea4227d6',
      fallback_uri_uuid='aec4773-4ae6-4b75-92ea-9cf3ea4227d6'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.create({
    name: 'inbound-trunk',
    trunkDirection: 'inbound',
    primaryUriUuid: 'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6',
    fallbackUriUuid: 'aec4773-4ae6-4b75-92ea-9cf3ea4227d6'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Primary vs Fallback URIs

| Type             | Purpose                                           |
| ---------------- | ------------------------------------------------- |
| **Primary URI**  | Default destination for inbound calls             |
| **Fallback URI** | Used when primary is unreachable or returns error |

Configure both for high availability:

1. Create two origination URIs pointing to different servers
2. Assign one as `primary_uri_uuid` and the other as `fallback_uri_uuid`
3. If primary fails, Plivo automatically routes to fallback

***

## URI Format Examples

| Format         | Example                |
| -------------- | ---------------------- |
| IP address     | `192.168.1.100`        |
| IP with port   | `192.168.1.100:5060`   |
| FQDN           | `sip.example.com`      |
| FQDN with port | `sip.example.com:5060` |
| SIP URI        | `sip:pbx@example.com`  |

***

## Related

* [Trunks](/sip-trunking/api/trunks/) - Create and manage SIP trunks
* [Calls](/sip-trunking/api/calls/) - View SIP trunk call records
