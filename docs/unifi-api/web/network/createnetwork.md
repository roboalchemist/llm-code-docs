# createnetwork

Source: https://developer.ui.com/network/v10.1.68/createnetwork

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Create Network

POST`/v1/sites/{siteId}/networks`

Create a new network on a site.

path Parameters

siteId

required

string

request Body

management

required

string

UNMANAGEDGATEWAYSWITCH

name

required

string

enabled

required

boolean

vlanId

required

integer

dhcpGuardingExpand

object

DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled

## Responses

201

Response Schema: application/json

management

required

string

UNMANAGEDGATEWAYSWITCH

id

required

string

name

required

string

enabled

required

boolean

vlanId

required

integer

metadataExpand

required

object (User or system defined or orchestrated entity metadata)

Orchestrated or System-defined configurable network support

dhcpGuardingExpand

object

DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/networks" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"management\": \"string\",  \"name\": \"Default Network\",  \"enabled\": true,  \"vlanId\": 0,  \"dhcpGuarding\": {    \"trustedDhcpServerIpAddresses\": [      \"string\"    ]  }}"
```

Response Sample

201

```
{  "management": "string",  "id": "00000000-0000-0000-0000-000000000000",  "name": "string",  "enabled": true,  "vlanId": 0,  "metadata": {    "origin": "string"  },  "dhcpGuarding": {    "trustedDhcpServerIpAddresses": [      "string"    ]  }}
```