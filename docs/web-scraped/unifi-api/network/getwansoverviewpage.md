# getwansoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getwansoverviewpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List WAN Interfaces

GET`/v1/sites/{siteId}/wans`

Returns available WAN interface definitions for a given site,
including identifiers and names. Useful for network and NAT configuration.

path Parameters

siteId

required

string

query Parameters

offset

integer

limit

integer

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

Array of object (WAN overview)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/wans?offset={offset}&limit={limit}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "id": "00000000-0000-0000-0000-000000000000",      "name": "string"    }  ]}
```