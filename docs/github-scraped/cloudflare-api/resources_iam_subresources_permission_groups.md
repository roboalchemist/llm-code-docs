# Permission Groups | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups

[API Reference][IAM]
# Permission Groups

##### [List Account Permission Groups]
GET/accounts/{account_id}/iam/permission_groups
##### [Permission Group Details]
GET/accounts/{account_id}/iam/permission_groups/{permission_group_id}
##### ModelsExpand Collapse
PermissionGroupListResponse  { id, meta, name }
A named group of permissions that map to a group of operations against resources.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]PermissionGroupGetResponse  { id, meta, name }
A named group of permissions that map to a group of operations against resources.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]