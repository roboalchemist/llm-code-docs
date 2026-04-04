# getdnspolicy

Source: https://developer.ui.com/network/v10.1.68/getdnspolicy

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get DNS Policy

GET`/v1/sites/{siteId}/dns/policies/{dnsPolicyId}`

Retrieve specific DNS policy.

path Parameters

dnsPolicyId

required

string

siteId

required

string

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
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "enabled": true,  "domain": "string"}
```