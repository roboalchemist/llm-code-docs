# getnetworkdetails

Source: https://developer.ui.com/network/v10.1.68/getnetworkdetails

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Network Details

GET`/v1/sites/{siteId}/networks/{networkId}`

Retrieve detailed information about a specific network.

path Parameters

networkId

required

string

siteId

required

string

## Responses

200

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