# getdpiapplicationcategories

Source: https://developer.ui.com/network/v10.1.68/getdpiapplicationcategories

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List DPI Application Categories

GET`/v1/dpi/categories`

Returns predefined Deep Packet Inspection (DPI) application categories used for traffic identification and filtering.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `id` | `INTEGER` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |

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

Array of object (DPI category)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/dpi/categories?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "id": 0,      "name": "string"    }  ]}
```