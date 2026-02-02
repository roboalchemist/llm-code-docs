# getaclruleordering

Source: https://developer.ui.com/network/v10.1.68/getaclruleordering

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get User-Defined ACL Rule Ordering

GET`/v1/sites/{siteId}/acl-rules/ordering`

Retrieve user-defined ACL rule ordering on a site.

path Parameters

siteId

required

string

## Responses

200

Response Schema: application/json

orderedAclRuleIdsExpand

required

Array of string

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/acl-rules/ordering" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "orderedAclRuleIds": [    "00000000-0000-0000-0000-000000000000"  ]}
```