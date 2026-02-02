# getfirewallpolicy

Source: https://developer.ui.com/network/v10.1.68/getfirewallpolicy

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Firewall Policy

GET`/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}`

Retrieve specific firewall policy.

path Parameters

firewallPolicyId

required

string

siteId

required

string

## Responses

200

Response Schema: application/json

id

required

string

enabled

required

boolean

name

required

string

description

string

index

required

integer

actionExpand

required

object (Firewall policy action)

Defines action for matched traffic.

sourceExpand

required

object

destinationExpand

required

object

ipProtocolScopeExpand

required

object (Firewall policy IP protocol scope)

Defines rules for matching by IP version and protocol.

connectionStateFilterExpand

Array of string

Match on firewall connection state. If null, matches all connection states.

ipsecFilter

string

Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.

loggingEnabled

required

boolean

Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.

scheduleExpand

object (Firewall schedule)

Defines date and time when the entity is active. If null, the entity is always active.

metadataExpand

required

object (User or system defined or derived entity metadata)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "id": "00000000-0000-0000-0000-000000000000",  "enabled": true,  "name": "string",  "description": "string",  "index": 0,  "action": {    "type": "string"  },  "source": {    "firewallZoneId": "00000000-0000-0000-0000-000000000000",    "trafficFilter": {      "type": "string"    }  },  "destination": {    "firewallZoneId": "00000000-0000-0000-0000-000000000000",    "trafficFilter": {      "type": "string"    }  },  "ipProtocolScope": {    "ipVersion": "string"  },  "connectionStateFilter": [    "NEW"  ],  "ipsecFilter": "MATCH_ENCRYPTED",  "loggingEnabled": true,  "schedule": {    "mode": "string"  },  "metadata": {    "origin": "string"  }}
```