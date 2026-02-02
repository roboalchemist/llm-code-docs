# getaclrulepage

Source: https://developer.ui.com/network/v10.1.68/getaclrulepage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List ACL Rules

GET`/v1/sites/{siteId}/acl-rules`

Retrieve a paginated list of all ACL rules on a site.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `type` | `STRING` | `eq` `ne` `in` `notIn` |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `enabled` | `BOOLEAN` | `eq` `ne` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `description` | `STRING` | `isNull` `isNotNull` `eq` `ne` `in` `notIn` `like` |
| `action` | `STRING` | `eq` `ne` `in` `notIn` |
| `index` | `INTEGER` | `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `protocolsFilter` | `SET(STRING)` | `isNull` `isNotNull` `contains` `containsAny` `containsAll` `containsExactly` |
| `networkId` | `UUID` | `isNull` `isNotNull` `eq` `ne` `in` `notIn` |
| `enforcingDeviceFilter.deviceIds` | `SET(UUID)` | `isNull` `isNotNull` `contains` `containsAny` `containsAll` `containsExactly` |
| `metadata.origin` | `STRING` | `eq` `ne` `in` `notIn` |
| `sourceFilter.type` | `STRING` | `isNull` `isNotNull` `eq` `ne` `in` `notIn` |
| `sourceFilter.ipAddressesOrSubnets` | `SET(STRING)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `sourceFilter.portsFilter` | `SET(INTEGER)` | `isNull` `isNotNull` `contains` `containsAny` `containsAll` `containsExactly` |
| `sourceFilter.networkIds` | `SET(UUID)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `sourceFilter.macAddresses` | `SET(STRING)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `sourceFilter.prefixLength` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |
| `destinationFilter.type` | `STRING` | `isNull` `isNotNull` `eq` `ne` `in` `notIn` |
| `destinationFilter.ipAddressesOrSubnets` | `SET(STRING)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `destinationFilter.portsFilter` | `SET(INTEGER)` | `isNull` `isNotNull` `contains` `containsAny` `containsAll` `containsExactly` |
| `destinationFilter.networkIds` | `SET(UUID)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `destinationFilter.macAddresses` | `SET(STRING)` | `contains` `containsAny` `containsAll` `containsExactly` |
| `destinationFilter.prefixLength` | `INTEGER` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `in` `notIn` |

path Parameters

siteId

required

string

query Parameters

offset

integer

limit

integer

filter

string

## Responses

200

Response Schema: application/json

offset

required

integer

limit

required

integer

count

required

integer

totalCount

required

integer

dataExpand

required

Array of object (ACL ruleObject)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/acl-rules?offset={offset}&limit={limit}&filter={filter}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "offset": 0,  "limit": 0,  "count": 0,  "totalCount": 0,  "data": [    {      "type": "string",      "id": "00000000-0000-0000-0000-000000000000",      "enabled": true,      "name": "string",      "description": "string",      "action": "ALLOW",      "enforcingDeviceFilter": {        "type": "string"      },      "index": 0,      "sourceFilter": null,      "destinationFilter": null,      "metadata": {        "origin": "string"      }    }  ]}
```