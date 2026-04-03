# Permission Groups | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/tokens/subresources/permission_groups

[API Reference][User][Tokens]
# Permission Groups

##### [List Token Permission Groups]
GET/user/tokens/permission_groups
##### ModelsExpand Collapse
PermissionGroupListResponse  { id, name, scopes } id: optional string
Public ID.
[]name: optional string
Permission Group Name
[]scopes: optional array of "com.cloudflare.api.account" or "com.cloudflare.api.account.zone" or "com.cloudflare.api.user" or "com.cloudflare.edge.r2.bucket"
Resources to which the Permission Group is scoped
One of the following:"com.cloudflare.api.account"[]"com.cloudflare.api.account.zone"[]"com.cloudflare.api.user"[]"com.cloudflare.edge.r2.bucket"[][][]