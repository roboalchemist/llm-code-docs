# getvouchers

Source: https://developer.ui.com/network/v10.1.68/getvouchers

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Vouchers

GET`/v1/sites/{siteId}/hotspot/vouchers`

Retrieve a paginated list of Hotspot vouchers.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `createdAt` | `TIMESTAMP` | `eq` `ne` `gt` `ge` `lt` `le` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `code` | `STRING` | `eq` `ne` `in` `notIn` |
| `authorizedGuestLimit` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` |
| `authorizedGuestCount` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` |
| `activatedAt` | `TIMESTAMP` | `eq` `ne` `gt` `ge` `lt` `le` |
| `expiresAt` | `TIMESTAMP` | `eq` `ne` `gt` `ge` `lt` `le` |
| `expired` | `BOOLEAN` | `eq` `ne` |
| `timeLimitMinutes` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` |
| `dataUsageLimitMBytes` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` |
| `rxRateLimitKbps` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` |
| `txRateLimitKbps` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` |

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

Array of object (Hotspot voucher details)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "id": "00000000-0000-0000-0000-000000000000",      "createdAt": "2024-01-01T00:00:00Z",      "name": "string",      "code": "string",      "authorizedGuestLimit": 0,      "authorizedGuestCount": 0,      "activatedAt": "2024-01-01T00:00:00Z",      "expiresAt": "2024-01-01T00:00:00Z",      "expired": true,      "timeLimitMinutes": 0,      "dataUsageLimitMBytes": 0,      "rxRateLimitKbps": 0,      "txRateLimitKbps": 0    }  ]}
```