# updatednspolicy

Source: https://developer.ui.com/network/v10.1.68/updatednspolicy

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update DNS Policy

PUT`/v1/sites/{siteId}/dns/policies/{dnsPolicyId}`

Update an existing DNS policy on a site.

path Parameters

dnsPolicyId

required

string

siteId

required

string

request Body

type

required

string

A\_RECORDAAAA\_RECORDCNAME\_RECORDMX\_RECORDTXT\_RECORDSRV\_RECORDFORWARD\_DOMAIN

enabled

required

boolean

domain

string

ipv4Address

string

ttlSeconds

integer

Time to live in seconds.

## Responses

200

Response Schema: application/json

type

required

string

A\_RECORDAAAA\_RECORDCNAME\_RECORDMX\_RECORDTXT\_RECORDSRV\_RECORDFORWARD\_DOMAIN

id

required

string

enabled

required

boolean

domain

string

ipv4Address

string

ttlSeconds

integer

Time to live in seconds.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PUT "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"type\": \"string\",  \"enabled\": true}"
```

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "enabled": true,  "domain": "string"}
```