# getfirewallpolicyordering

Source: https://developer.ui.com/network/v10.1.68/getfirewallpolicyordering

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get User-Defined Firewall Policy Ordering

GET`/v1/sites/{siteId}/firewall/policies/ordering`

Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

path Parameters

siteId

required

string

query Parameters

sourceFirewallZoneId

required

string

destinationFirewallZoneId

required

string

## Responses

200

Response Schema: application/json

orderedFirewallPolicyIdsExpand

required

object

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/policies/ordering?sourceFirewallZoneId={sourceFirewallZoneId}&destinationFirewallZoneId={destinationFirewallZoneId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "orderedFirewallPolicyIds": {    "beforeSystemDefined": [      "00000000-0000-0000-0000-000000000000"    ],    "afterSystemDefined": [      "00000000-0000-0000-0000-000000000000"    ]  }}
```