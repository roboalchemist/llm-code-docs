# Source: https://plivo.com/docs/sip-trunking/api/ip-access-control-lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Access Control Lists

> Manage IP whitelists for authenticating outbound SIP trunks

The IP Access Control Lists API lets you create and manage IP address whitelists for authenticating outbound SIP trunks.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/
```

***

## The IP Access Control List Object

An IP Access Control List (IP ACL) contains a set of whitelisted IP addresses that can send SIP traffic to your outbound trunk.

### Attributes

<ParamField body="ipacl_uuid" type="string">
  Unique identifier for the IP ACL.
</ParamField>

<ParamField body="name" type="string">
  Friendly name for the IP ACL.
</ParamField>

<ParamField body="ip_addresses" type="array">
  List of whitelisted IP addresses.
</ParamField>

### Example Object

```json  theme={null}
{
  "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "production-servers",
  "ip_addresses": [
    "192.168.1.1",
    "192.168.1.2"
  ]
}
```

***

## List All IP Access Control Lists

Get all IP ACLs for your account.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/`

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
    "next": "v1/Account/{auth_id}/Zentrunk/IPAccessControlList/?limit=20&offset=20"
  },
  "objects": [
    {
      "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
      "name": "production-servers",
      "ip_addresses": ["192.168.1.1", "192.168.1.2"]
    },
    {
      "ipacl_uuid": "a19c4773-4ae6-4b75-92ea-9cf3ea4227d7",
      "name": "staging-servers",
      "ip_addresses": ["10.0.0.1", "10.0.0.2"]
    }
  ]
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  # List all IP ACLs
  response = client.zentrunk.ip_access_control_lists.list()
  print(response)

  # List with pagination
  response = client.zentrunk.ip_access_control_lists.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  // List all IP ACLs
  client.zentrunk.ipAccessControlLists.list()
    .then(response => console.log(response));

  // List with pagination
  client.zentrunk.ipAccessControlLists.list({limit: 10, offset: 0})
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Retrieve an IP Access Control List

Get details of a specific IP ACL.

### HTTP Request

`GET https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/{ipacl_uuid}/`

### Response

```json  theme={null}
{
  "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
  "name": "production-servers",
  "ip_addresses": [
    "192.168.1.1",
    "192.168.1.2"
  ]
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.ip_access_control_lists.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.ipAccessControlLists.get('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Create an IP Access Control List

Create a new IP whitelist for SIP trunk authentication.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/`

### Request Parameters

| Parameter      | Type   | Required | Default | Description                        |
| -------------- | ------ | -------- | ------- | ---------------------------------- |
| `name`         | string | No       | -       | Friendly name for the IP ACL       |
| `ip_addresses` | array  | Yes      | -       | Array of IP addresses to whitelist |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "IP access control list created successfully.",
  "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

### Error Codes

| Code | Description                                 |
| ---- | ------------------------------------------- |
| 400  | Invalid request parameters                  |
| 401  | Authentication failed                       |
| 422  | Missing required parameters (ip\_addresses) |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "production-servers",
        "ip_addresses": ["192.168.0.1", "192.168.0.2", "10.0.0.1"]
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.ip_access_control_lists.create(
      name='production-servers',
      ip_addresses=['192.168.0.1', '192.168.0.2', '10.0.0.1']
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.ipAccessControlLists.create({
    name: 'production-servers',
    ipAddresses: ['192.168.0.1', '192.168.0.2', '10.0.0.1']
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Update an IP Access Control List

Modify an existing IP ACL's name or IP addresses.

### HTTP Request

`POST https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/{ipacl_uuid}/`

### Request Parameters

| Parameter      | Type   | Required | Default | Description                                  |
| -------------- | ------ | -------- | ------- | -------------------------------------------- |
| `name`         | string | No       | -       | New friendly name                            |
| `ip_addresses` | array  | No       | -       | New list of IP addresses (replaces existing) |

### Response

```json  theme={null}
{
  "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
  "message": "IP access control list updated successfully.",
  "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

<Note>
  Updating `ip_addresses` replaces the entire list. Include all IP addresses you want whitelisted.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "updated-servers",
        "ip_addresses": ["192.168.0.1", "192.168.0.2", "192.168.0.3"]
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.ip_access_control_lists.update(
      'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6',
      name='updated-servers',
      ip_addresses=['192.168.0.1', '192.168.0.2', '192.168.0.3']
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.ipAccessControlLists.update('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6', {
    name: 'updated-servers',
    ipAddresses: ['192.168.0.1', '192.168.0.2', '192.168.0.3']
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## Delete an IP Access Control List

Permanently delete an IP ACL.

### HTTP Request

`DELETE https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/{ipacl_uuid}/`

### Response

HTTP 204 No Content

<Warning>
  Deleting an IP ACL that is attached to an active trunk will break authentication for that trunk.
</Warning>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/IPAccessControlList/f19c4773-4ae6-4b75-92ea-9cf3ea4227d6/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.ip_access_control_lists.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.ipAccessControlLists.delete('f19c4773-4ae6-4b75-92ea-9cf3ea4227d6')
    .then(response => console.log(response));
  ```
</CodeGroup>

***

## Usage with Trunks

After creating an IP ACL, attach it to an outbound trunk.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
        "name": "outbound-trunk",
        "trunk_direction": "outbound",
        "ipacl_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Zentrunk/Trunk/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.zentrunk.trunks.create(
      name='outbound-trunk',
      trunk_direction='outbound',
      ipacl_uuid='f19c4773-4ae6-4b75-92ea-9cf3ea4227d6'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.zentrunk.trunks.create({
    name: 'outbound-trunk',
    trunkDirection: 'outbound',
    ipaclUuid: 'f19c4773-4ae6-4b75-92ea-9cf3ea4227d6'
  }).then(response => console.log(response));
  ```
</CodeGroup>

***

## IP ACL vs Credentials

| Method          | Use Case                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------- |
| **IP ACL**      | When your PBX has static IP addresses. Simpler setup, no password management.                  |
| **Credentials** | When your PBX has dynamic IPs or you need additional security. Uses SIP digest authentication. |

You can use either method (or both) for outbound trunk authentication.

***

## Related

* [Trunks](/sip-trunking/api/trunks/) - Create and manage SIP trunks
* [Credentials](/sip-trunking/api/credentials/) - Alternative authentication via username/password
