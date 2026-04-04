# updateaclrule

Source: https://developer.ui.com/network/v10.1.68/updateaclrule

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Update ACL Rule

PUT`/v1/sites/{siteId}/acl-rules/{aclRuleId}`

Update an existing user defined ACL rule on a site.

path Parameters

aclRuleId

required

string

siteId

required

string

request Body

type

required

string

IPV4MAC

enabled

required

boolean

name

required

string

ACL rule name

description

string

ACL rule description

action

required

string

ACL rule action

enforcingDeviceFilterExpand

object (ACL rule device filter)

IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.

index

integer

ACL rule index. This property is deprecated and has no effect. Use the dedicated ACL rule reordering endpoint.

sourceFilterExpand

object (IP ACL rule endpoint)

Traffic source filter

destinationFilterExpand

object (IP ACL rule endpoint)

Traffic destination filter

protocolFilterExpand

Array of string

Protocols this ACL rule will be applied to. When null, the rule will be applied to all protocols.

## Responses

200

Response Schema: application/json

type

required

string

IPV4MAC

id

required

string

enabled

required

boolean

name

required

string

ACL rule name

description

string

ACL rule description

action

required

string

ACL rule action

enforcingDeviceFilterExpand

object (ACL rule device filter)

IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.

index

required

integer

ACL rule index. Lower index has higher priority

sourceFilter

any

Traffic source filter

destinationFilter

any

Traffic destination filter

metadataExpand

required

object (User defined or derived entity metadata)

Only user-defined rules can be deleted or modified

protocolFilterExpand

Array of string

Protocols this ACL rule will be applied to. When null, the rule will be applied to all protocols.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PUT "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"type\": \"string\",  \"enabled\": true,  \"name\": \"string\",  \"description\": \"string\",  \"action\": \"ALLOW|BLOCK\",  \"enforcingDeviceFilter\": {    \"type\": \"string\"  },  \"index\": 0}"
```

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "enabled": true,  "name": "string",  "description": "string",  "action": "ALLOW",  "enforcingDeviceFilter": {    "type": "string"  },  "index": 0,  "sourceFilter": null,  "destinationFilter": null,  "metadata": {    "origin": "string"  }}
```