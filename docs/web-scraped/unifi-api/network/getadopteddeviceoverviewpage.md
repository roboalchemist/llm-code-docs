# getadopteddeviceoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getadopteddeviceoverviewpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Adopted Devices

GET`/v1/sites/{siteId}/devices`

Retrieve a paginated list of all adopted devices on a site, including basic device information.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `macAddress` | `STRING` | `eq` `ne` `in` `notIn` |
| `ipAddress` | `STRING` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` `like` |
| `model` | `STRING` | `eq` `ne` `in` `notIn` |
| `state` | `STRING` | `eq` `ne` `in` `notIn` |
| `supported` | `BOOLEAN` | `eq` `ne` |
| `firmwareVersion` | `STRING` | `isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `like` `in` `notIn` |
| `firmwareUpdatable` | `BOOLEAN` | `eq` `ne` |
| `features` | `SET(STRING)` | `isEmpty` `contains` `containsAny` `containsAll` `containsExactly` |
| `interfaces` | `SET(STRING)` | `isEmpty` `contains` `containsAny` `containsAll` `containsExactly` |

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

Array of object (Adopted device overview)