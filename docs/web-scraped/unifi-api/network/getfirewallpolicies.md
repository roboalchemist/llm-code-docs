# getfirewallpolicies

Source: https://developer.ui.com/network/v10.1.68/getfirewallpolicies

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Firewall Policies

GET`/v1/sites/{siteId}/firewall/policies`

Retrieve a list of all firewall policies on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `source.firewallZoneId` | `UUID` | `eq` `ne` `in` `notIn` |
| `destination.firewallZoneId` | `UUID` | `eq` `ne` `in` `notIn` |
| `metadata.origin` | `STRING` | `eq` `ne` `in` `notIn` |

path Parameters

siteId

required

string

query Parameters

offset

integer

limit

integer

filter

string

## Responses

200

Response Schema: application/json

offset

required

integer

limit

required

integer

count

required

integer

totalCount

required

integer

dataExpand

required

Array of object (Firewall policy)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/policies?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "id": "00000000-0000-0000-0000-000000000000",      "enabled": true,      "name": "string",      "description": "string",      "index": 0,      "action": {        "type": "string"      },      "source": {        "firewallZoneId": "00000000-0000-0000-0000-000000000000",        "trafficFilter": {          "type": "string"        }      },      "destination": {        "firewallZoneId": "00000000-0000-0000-0000-000000000000",        "trafficFilter": {          "type": "string"        }      },      "ipProtocolScope": {        "ipVersion": "string"      },      "connectionStateFilter": [        "NEW"      ],      "ipsecFilter": "MATCH_ENCRYPTED",      "loggingEnabled": true,      "schedule": {        "mode": "string"      },      "metadata": {        "origin": "string"      }    }  ]}
```