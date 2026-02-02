# getsiteoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getsiteoverviewpage

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Local Sites

GET`/v1/sites`

Retrieve a paginated list of local sites managed by this Network application.
Site ID is required for other UniFi Network API calls.

Filterable properties (click to expand)

| Name | Type | Allowed functions |
| --- | --- | --- |
| `id` | `UUID` | `eq` `ne` `in` `notIn` |
| `internalReference` | `STRING` | `eq` `ne` `in` `notIn` |
| `name` | `STRING` | `eq` `ne` `in` `notIn` |

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

Array of object (Site overview)