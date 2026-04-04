# getpendingdevicepage

Source: https://developer.ui.com/network/v10.1.68/getpendingdevicepage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Devices Pending Adoption

GET`/v1/pending-devices`

Retrieve a paginated list of devices pending adoption, including basic device information.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `macAddress` | `STRING` | `eq` `ne` `in` `notIn` |
| `ipAddress` | `STRING` | `eq` `ne` `in` `notIn` |
| `model` | `STRING` | `eq` `ne` `in` `notIn` |
| `state` | `STRING` | `eq` `ne` `in` `notIn` |
| `supported` | `BOOLEAN` | `eq` `ne` |
| `firmwareVersion` | `STRING` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `like` `in` `notIn` |
| `firmwareUpdatable` | `BOOLEAN` | `eq` `ne` |
| `features` | `SET(STRING)` | `isEmpty` `contains` `containsAny` `containsAll` `containsExactly` |

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

Array of object (Device pending adoption)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/pending-devices?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "macAddress": "string",      "ipAddress": "string",      "model": "string",      "state": "ONLINE",      "supported": true,      "firmwareVersion": "string",      "firmwareUpdatable": true,      "features": [        "switching"      ]    }  ]}
```