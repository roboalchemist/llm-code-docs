# deletednspolicy

Source: https://developer.ui.com/network/v10.1.68/deletednspolicy

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Delete DNS Policy

DELETE`/v1/sites/{siteId}/dns/policies/{dnsPolicyId}`

Delete an existing DNS policy on a site.

path Parameters

dnsPolicyId

required

string

siteId

required

string

## Responses

200

Response 200: No schema content available

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X DELETE "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

No example responses available