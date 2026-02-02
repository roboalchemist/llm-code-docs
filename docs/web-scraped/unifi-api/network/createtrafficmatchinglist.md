# createtrafficmatchinglist

Source: https://developer.ui.com/network/v10.1.68/createtrafficmatchinglist

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Create Traffic Matching List

POST`/v1/sites/{siteId}/traffic-matching-lists`

Create a new traffic matching list on a site.

path Parameters

siteId

required

string

request Body

type

required

string

PORTSIPV4\_ADDRESSESIPV6\_ADDRESSES

name

required

string

itemsExpand

Array of object (Port matching)

## Responses

201

Response Schema: application/json

type

required

string

PORTSIPV4\_ADDRESSESIPV6\_ADDRESSES

id

required

string

name

required

string

itemsExpand

Array of object (Port matching)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"type\": \"string\",  \"name\": \"Allowed port list|Protected IP list\"}"
```

Response Sample

201

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "name": "string"}
```