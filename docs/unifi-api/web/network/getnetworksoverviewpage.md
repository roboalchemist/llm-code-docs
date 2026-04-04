# getnetworksoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getnetworksoverviewpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Networks

GET`/v1/sites/{siteId}/networks`

Retrieve a paginated list of all Networks on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `management` | `STRING` | `eq` `ne` `in` `notIn` |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `enabled` | `BOOLEAN` | `eq` `ne` |
| `vlanId` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `deviceId` | `UUID` | `eq` `ne` `in` `notIn` `isNull` `isNotNull` |
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

Array of object (Network overview)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/networks?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "management": "string",      "id": "00000000-0000-0000-0000-000000000000",      "name": "string",      "enabled": true,      "vlanId": 0,      "metadata": {        "origin": "string"      }    }  ]}
```