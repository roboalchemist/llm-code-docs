# deletefirewallzone

Source: https://developer.ui.com/network/v10.1.68/deletefirewallzone

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Delete Custom Firewall Zone

DELETE`/v1/sites/{siteId}/firewall/zones/{firewallZoneId}`

Delete a custom firewall zone from a site.

path Parameters

firewallZoneId

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
curl -L -g -X DELETE "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

No example responses available