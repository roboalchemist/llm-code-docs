# updatetrafficmatchinglist

Source: https://developer.ui.com/network/v10.1.68/updatetrafficmatchinglist

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update Traffic Matching List

PUT`/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}`

Update an exist traffic matching list on a site.

path Parameters

trafficMatchingListId

required

string

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

200

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
curl -L -g -X PUT "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"type\": \"string\",  \"name\": \"Allowed port list|Protected IP list\"}"
```

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "name": "string"}
```