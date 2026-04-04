# updatenetwork

Source: https://developer.ui.com/network/v10.1.68/updatenetwork

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update Network

PUT`/v1/sites/{siteId}/networks/{networkId}`

Update an existing network on a site.

path Parameters

networkId

required

string

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