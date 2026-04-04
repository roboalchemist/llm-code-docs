# getfirewallzone

Source: https://developer.ui.com/network/v10.1.68/getfirewallzone

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Firewall Zone

GET`/v1/sites/{siteId}/firewall/zones/{firewallZoneId}`

Get a firewall zone on a site.

path Parameters

firewallZoneId

required

string

siteId

required

string

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
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "id": "00000000-0000-0000-0000-000000000000",  "name": "string",  "networkIds": [    "00000000-0000-0000-0000-000000000000"  ],  "metadata": {    "origin": "string"  }}
```