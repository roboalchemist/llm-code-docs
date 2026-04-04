# getsitetositevpntunnelpage

Source: https://developer.ui.com/network/v10.1.68/getsitetositevpntunnelpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Site-To-Site VPN Tunnels

GET`/v1/sites/{siteId}/vpn/site-to-site-tunnels`

Retrieve a paginated list of all site-to-site VPN tunnels on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `type` | `STRING` | `eq` `ne` `in` `notIn` |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `metadata.origin` | `STRING` | `eq` `ne` `in` `notIn` |
| `metadata.source` | `STRING` | `eq` `ne` `in` `notIn` `isNull` `isNotNull` |

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

Array of object (Site-to-site VPN tunnel overview)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/vpn/site-to-site-tunnels?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "type": "string",      "id": "00000000-0000-0000-0000-000000000000",      "name": "string",      "metadata": {        "origin": "string"      }    }  ]}
```