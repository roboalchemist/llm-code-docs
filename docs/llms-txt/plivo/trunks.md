# Source: https://plivo.com/docs/sip-trunking/api/trunks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trunks

> Create and manage SIP trunks for inbound and outbound voice traffic

The Trunks API lets you create and manage SIP trunks that route voice traffic between your infrastructure and Plivo's network.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
```

***

## The Trunk Object

A trunk represents a SIP connection between your infrastructure and Plivo's network. Trunks can be inbound (receiving calls from Plivo) or outbound (sending calls to Plivo).

### Attributes

<ParamField body="trunk_id" type="string">
  Unique identifier for the trunk.
</ParamField>

<ParamField body="trunk_domain" type="string">
  Unique address on Plivo to route SIP traffic (e.g., `21784177241578.zt.plivo.com`).
</ParamField>

<ParamField body="name" type="string">
  Friendly name for the trunk.
</ParamField>

<ParamField body="trunk_status" type="string">
  Status of the trunk: `enabled` or `disabled`.
</ParamField>

<ParamField body="trunk_direction" type="string">
  Direction of the trunk: `inbound` or `outbound`.
</ParamField>

<ParamField body="secure" type="boolean">
  Whether SRTP (media) and TLS (signaling) encryption is enabled.
</ParamField>

<ParamField body="ipacl_uuid" type="string">
  IP access control list UUID (for outbound trunks).
</ParamField>

<ParamField body="credential_uuid" type="string">
  Credentials list UUID (for outbound trunks).
</ParamField>

<ParamField body="primary_uri_uuid" type="string">
  Primary origination URI UUID (for inbound trunks).
</ParamField>

<ParamField body="fallback_uri_uuid" type="string">
  Fallback origination URI UUID (for inbound trunks).
</ParamField>

### Example Object

```json  theme={null}
{
  "name": "trunk_name_1",
  "trunk_id": "21784177241578",
  "trunk_domain": "21784177241578.zt.plivo.com",
  "trunk_status": "enabled",
  "secure": true,
  "trunk_direction": "outbound",
  "ipacl_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
  "credential_uuid": "eb07-796c-4d86-a4fd-44ed11667ddb",
  "primary_uri_uuid": null,
  "fallback_uri_uuid": null
}
```

***

## List All Trunks

Get all trunks with optional filtering.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/`

### Query Parameters

| Parameter           | Type    | Required | Default | Description                                |
| ------------------- | ------- | -------- | ------- | ------------------------------------------ |
| `trunk_status`      | string  | No       | -       | Filter by status: `enabled`, `disabled`    |
| `trunk_direction`   | string  | No       | -       | Filter by direction: `inbound`, `outbound` |
| `secure`            | boolean | No       | -       | Filter by encryption: `true`, `false`      |
| `ipacl_uuid`        | string  | No       | -       | Filter by IP ACL                           |
| `credential_uuid`   | string  | No       | -       | Filter by credentials                      |
| `primary_uri_uuid`  | string  | No       | -       | Filter by primary URI                      |
| `fallback_uri_uuid` | string  | No       | -       | Filter by fallback URI                     |
| `limit`             | integer | No       | 20      | Results per page (1-20)                    |
| `offset`            | integer | No       | 0       | Pagination offset                          |

### Response

```json  theme={null}
{
  "api_id": "a04ad809-3b78-4bbe-9baf-acfc7800b10f",
  "meta": {
    "limit": 2,
    "offset": 0,
    "total_count": 10,
    "previous": null,
    "next": "v1/Account/{auth_id}/Zentrunk/Trunk/?limit=2&offset=2"
  },
  "objects": [
    {
      "name": "trunk_name_1",
      "trunk_id": "21784177241578",
      "trunk_domain": "21784177241578.zt.plivo.com",
      "trunk_status": "enabled",
      "secure": true,
      "trunk_direction": "outbound",
      "ipacl_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
      "credential_uuid": "eb07-796c-4d86-a4fd-44ed11667ddb",
      "primary_uri_uuid": null,
      "fallback_uri_uuid": null
    },
    {
      "name": "trunk_name_2",
      "trunk_id": "31784177241575",
      "trunk_domain": "31784177241575.zt.plivo.com",
      "trunk_status": "enabled",
      "secure": false,
      "trunk_direction": "inbound",
      "ipacl_uuid": null,
      "credential_uuid": null,
      "primary_uri_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
      "fallback_uri_uuid": "796c-4d86-a4fd-44ed11667ddb-eb07"
    }
  ]
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      "https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/?trunk_direction=outbound&limit=10"
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  # List all trunks
  response = client.zentrunk.trunks.list()
  print(response)

  # List with filters
  response = client.zentrunk.trunks.list(
      trunk_direction='outbound',
      limit=10
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  // List all trunks
  client.zentrunk.trunks.list()
    .then(response => console.log(response));

  // List with filters
  client.zentrunk.trunks.list({
    trunkDirection: 'outbound',
    limit: 10
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Retrieve a Trunk

Get details of a specific trunk.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/{trunk_id}/`

### Response

Returns the trunk object.

```json  theme={null}
{
  "name": "trunk_name_1",
  "trunk_id": "21784177241578",
  "trunk_domain": "21784177241578.zt.plivo.com",
  "trunk_status": "enabled",
  "secure": true,
  "trunk_direction": "outbound",
  "ipacl_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
  "credential_uuid": "eb07-796c-4d86-a4fd-44ed11667ddb",
  "primary_uri_uuid": null,
  "fallback_uri_uuid": null
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/21784177241578/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.get('21784177241578')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.get('21784177241578')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Create a Trunk

Create a new SIP trunk for inbound or outbound traffic.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/`

### Request Parameters

| Parameter           | Type    | Required    | Default   | Description                                          |
| ------------------- | ------- | ----------- | --------- | ---------------------------------------------------- |
| `name`              | string  | No          | -         | Friendly name for the trunk                          |
| `trunk_direction`   | string  | Yes         | -         | Direction: `inbound` or `outbound`                   |
| `trunk_status`      | string  | No          | `enabled` | Status: `enabled` or `disabled`                      |
| `secure`            | boolean | No          | `false`   | Enable SRTP/TLS encryption                           |
| `ipacl_uuid`        | string  | Conditional | -         | IP ACL UUID. Required for outbound trunks            |
| `credential_uuid`   | string  | Conditional | -         | Credentials UUID. Required for outbound trunks       |
| `primary_uri_uuid`  | string  | Conditional | -         | Primary origination URI. Required for inbound trunks |
| `fallback_uri_uuid` | string  | No          | -         | Fallback origination URI for inbound trunks          |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "Trunk created successfully.",
  "trunk_id": "986908123123411213"
}
```

### Error Codes

| Code | Description                                                        |
| ---- | ------------------------------------------------------------------ |
| 400  | Invalid request parameters                                         |
| 401  | Authentication failed                                              |
| 422  | Missing required parameters (e.g., ipacl\_uuid for outbound trunk) |

### Outbound Trunk Example

For outbound trunks (calls from your PBX to Plivo), you need either `ipacl_uuid` or `credential_uuid` for authentication.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "outbound-trunk",
        "trunk_direction": "outbound",
        "trunk_status": "enabled",
        "ipacl_uuid": "1c13de4c-423d-11e3-9899-22000abfa5d5"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.create(
      name='outbound-trunk',
      trunk_direction='outbound',
      trunk_status='enabled',
      ipacl_uuid='1c13de4c-423d-11e3-9899-22000abfa5d5'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.create({
    name: 'outbound-trunk',
    trunkDirection: 'outbound',
    trunkStatus: 'enabled',
    ipaclUuid: '1c13de4c-423d-11e3-9899-22000abfa5d5'
  }).then(response => console.log(response));
  ```
</CodeGroup>

### Inbound Trunk Example

For inbound trunks (calls from Plivo to your PBX), you need a `primary_uri_uuid` pointing to your server.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "inbound-trunk",
        "trunk_direction": "inbound",
        "trunk_status": "enabled",
        "primary_uri_uuid": "90b6eb07-796c-4d86-a4fd-44ed11667ddb",
        "fallback_uri_uuid": "796c-4d86-a4fd-44ed11667ddb-eb07"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.create(
      name='inbound-trunk',
      trunk_direction='inbound',
      trunk_status='enabled',
      primary_uri_uuid='90b6eb07-796c-4d86-a4fd-44ed11667ddb',
      fallback_uri_uuid='796c-4d86-a4fd-44ed11667ddb-eb07'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.create({
    name: 'inbound-trunk',
    trunkDirection: 'inbound',
    trunkStatus: 'enabled',
    primaryUriUuid: '90b6eb07-796c-4d86-a4fd-44ed11667ddb',
    fallbackUriUuid: '796c-4d86-a4fd-44ed11667ddb-eb07'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Update a Trunk

Modify an existing trunk's properties.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/{trunk_id}/`

### Request Parameters

| Parameter           | Type    | Required | Default | Description                        |
| ------------------- | ------- | -------- | ------- | ---------------------------------- |
| `name`              | string  | No       | -       | New name for the trunk             |
| `trunk_status`      | string  | No       | -       | Status: `enabled` or `disabled`    |
| `trunk_direction`   | string  | No       | -       | Direction: `inbound` or `outbound` |
| `secure`            | boolean | No       | -       | Enable/disable SRTP/TLS encryption |
| `ipacl_uuid`        | string  | No       | -       | New IP ACL UUID                    |
| `credential_uuid`   | string  | No       | -       | New credentials UUID               |
| `primary_uri_uuid`  | string  | No       | -       | New primary origination URI        |
| `fallback_uri_uuid` | string  | No       | -       | New fallback origination URI       |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "Trunk updated successfully.",
  "trunk_id": "986908123123411213"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"name": "updated-trunk-name", "trunk_status": "disabled"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/{trunk_id}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.update(
      '<trunk_id>',
      name='updated-trunk-name',
      trunk_status='disabled'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.update('<trunk_id>', {
    name: 'updated-trunk-name',
    trunkStatus: 'disabled'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Delete a Trunk

Permanently delete a trunk.

### HTTP Request

`DELETE https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/{trunk_id}/`

### Response

HTTP 204 No Content

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/{trunk_id}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.delete('<trunk_id>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.delete('<trunk_id>')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Trunk Types

| Trunk Type   | Purpose                                           | Can Attach to Phone Numbers? |
| ------------ | ------------------------------------------------- | ---------------------------- |
| **Inbound**  | Route calls from Plivo to your PBX/infrastructure | Yes                          |
| **Outbound** | Route calls from your PBX/infrastructure to Plivo | No                           |

<Warning>
  **Only inbound trunks can be attached to phone numbers.** If you create an outbound trunk, it will not appear in the phone number configuration dropdown. To receive calls on a Plivo number via SIP, you must create an inbound trunk.
</Warning>

### Outbound Trunks

Route calls from your PBX/infrastructure to Plivo:

* Your system sends SIP INVITE to the trunk domain
* Authentication via IP ACL or credentials
* Calls terminate on PSTN via Plivo

### Inbound Trunks

Route calls from Plivo to your PBX/infrastructure:

* Calls arrive at Plivo (from PSTN or Plivo numbers)
* Plivo forwards to your origination URI
* Fallback URI used if primary fails
* **Can be attached to purchased phone numbers**

***

## Related

* [Credentials](/sip-trunking/api/credentials/) - Manage SIP credentials
* [IP Access Control Lists](/sip-trunking/api/ip-access-control-lists/) - Manage IP whitelists
* [Origination URIs](/sip-trunking/api/origination-uris/) - Manage destination URIs
