# Permission Groups | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/permission_groups

[API Reference][Accounts][Tokens]
# Permission Groups

##### [List Permission Groups]
GET/accounts/{account_id}/tokens/permission_groups
##### [List Permission Groups]
GET/accounts/{account_id}/tokens/permission_groups
##### ModelsExpand Collapse
PermissionGroupListResponse  { id, name, scopes } id: optional string
Public ID.
[]name: optional string
Permission Group Name
[]scopes: optional array of "com.cloudflare.api.account" or "com.cloudflare.api.account.zone" or "com.cloudflare.api.user" or "com.cloudflare.edge.r2.bucket"
Resources to which the Permission Group is scoped
One of the following:"com.cloudflare.api.account"[]"com.cloudflare.api.account.zone"[]"com.cloudflare.api.user"[]"com.cloudflare.edge.r2.bucket"[][][]PermissionGroupGetResponse = array of  { id, name, scopes } id: optional string
Public ID.
[]name: optional string
Permission Group Name
[]scopes: optional array of "com.cloudflare.api.account" or "com.cloudflare.api.account.zone" or "com.cloudflare.api.user" or "com.cloudflare.edge.r2.bucket"
Resources to which the Permission Group is scoped
One of the following:"com.cloudflare.api.account"[]"com.cloudflare.api.account.zone"[]"com.cloudflare.api.user"[]"com.cloudflare.edge.r2.bucket"[][][]