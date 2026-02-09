# deletevouchers

Source: https://developer.ui.com/network/v10.1.68/deletevouchers

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Delete Vouchers

DELETE`/v1/sites/{siteId}/hotspot/vouchers`

Remove Hotspot vouchers based on the specified filter criteria.

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

filter

required

string

## Responses

200

Response Schema: application/json

vouchersDeleted

integer

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X DELETE "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers?filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "vouchersDeleted": 0}
```