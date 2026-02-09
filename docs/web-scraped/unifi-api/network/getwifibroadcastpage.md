# getwifibroadcastpage

Source: https://developer.ui.com/network/v10.1.68/getwifibroadcastpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Wifi Broadcasts

GET`/v1/sites/{siteId}/wifi/broadcasts`

Retrieve a paginated list of all Wifi Broadcasts on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `type` | `STRING` | `eq` `ne` `in` `notIn` |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `enabled` | `BOOLEAN` | `eq` `ne` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `broadcastingFrequenciesGHz` | `SET(DECIMAL)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `metadata.origin` | `STRING` | `eq` `ne` `in` `notIn` |
| `network.type` | `STRING` | `eq` `ne` `in` `notIn` `isNull` `isNotNull` |
| `network.networkId` | `UUID` | `eq` `ne` `in` `notIn` |
| `securityConfiguration.type` | `STRING` | `eq` `ne` `in` `notIn` |
| `broadcastingDeviceFilter.type` | `STRING` | `eq` `ne` `in` `notIn` `isNull` `isNotNull` |
| `broadcastingDeviceFilter.deviceIds` | `SET(UUID)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `broadcastingDeviceFilter.deviceTagIds` | `SET(UUID)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `hotspotConfiguration.type` | `STRING` | `eq` `ne` `in` `notIn` |

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

Array of object (Wifi broadcast overview)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "type": "string",      "id": "00000000-0000-0000-0000-000000000000",      "name": "string",      "enabled": true,      "metadata": {        "origin": "string"      },      "network": {        "type": "string"      },      "securityConfiguration": {        "type": "string"      },      "broadcastingDeviceFilter": {        "type": "string"      }    }  ]}
```