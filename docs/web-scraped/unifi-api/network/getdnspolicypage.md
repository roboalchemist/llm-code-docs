# getdnspolicypage

Source: https://developer.ui.com/network/v10.1.68/getdnspolicypage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List DNS Policies

GET`/v1/sites/{siteId}/dns/policies`

Retrieve a paginated list of all DNS policies on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `type` | `STRING` | `eq` `ne` `in` `notIn` |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `enabled` | `BOOLEAN` | `eq` `ne` |
| `domain` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `ipv4Address` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `ipv6Address` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `targetDomain` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `mailServerDomain` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `text` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `serverDomain` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `ipAddress` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `ttlSeconds` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `priority` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `service` | `STRING` | `eq` `ne` `in` `notIn` |
| `protocol` | `STRING` | `eq` `ne` `in` `notIn` |
| `port` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `weight` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |

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

Array of object (DNS policy)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/dns/policies?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "type": "string",      "id": "00000000-0000-0000-0000-000000000000",      "enabled": true,      "domain": "string"    }  ]}
```