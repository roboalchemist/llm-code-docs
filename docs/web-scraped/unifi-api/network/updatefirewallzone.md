# updatefirewallzone

Source: https://developer.ui.com/network/v10.1.68/updatefirewallzone

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update Firewall Zone

PUT`/v1/sites/{siteId}/firewall/zones/{firewallZoneId}`

Update a firewall zone on a site.

path Parameters

firewallZoneId

required

string

siteId

required

string

request Body

name

required

string

Name of a firewall zone

networkIdsExpand

required

Array of string

List of Network IDs

## Responses

200

Response Schema: application/json

id

required

string

name

required

string

Name of a firewall zone

networkIdsExpand

required

Array of string

List of Network IDs

metadataExpand

required

object (User or system defined entity metadata)

System-defined configurable zones support configuring only attached networks

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PUT "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"name\": \"Hotspot|My custom zone\",  \"networkIds\": [    \"dfb21062-8ea0-4dca-b1d8-1eb3da00e58b\"  ]}"
```

Response Sample

200

```
{  "id": "00000000-0000-0000-0000-000000000000",  "name": "string",  "networkIds": [    "00000000-0000-0000-0000-000000000000"  ],  "metadata": {    "origin": "string"  }}
```