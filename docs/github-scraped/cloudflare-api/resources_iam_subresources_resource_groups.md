# Resource Groups | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups

[API Reference][IAM]
# Resource Groups

##### [List Resource Groups]
GET/accounts/{account_id}/iam/resource_groups
##### [Resource Group Details]
GET/accounts/{account_id}/iam/resource_groups/{resource_group_id}
##### [Create Resource Group]
POST/accounts/{account_id}/iam/resource_groups
##### [Update Resource Group]
PUT/accounts/{account_id}/iam/resource_groups/{resource_group_id}
##### [Remove Resource Group]
DELETE/accounts/{account_id}/iam/resource_groups/{resource_group_id}
##### ModelsExpand Collapse
ResourceGroupListResponse  { id, scope, meta, name }
A group of scoped resources.
id: string
Identifier of the resource group.
[]scope: array of  { key, objects }
The scope associated to the resource group
key: string
This is a combination of pre-defined resource name and identifier (like Account ID etc.)
[]objects: array of  { key }
A list of scope objects for additional context.
key: string
This is a combination of pre-defined resource name and identifier (like Zone ID etc.)
[][][]meta: optional  { key, value }
Attributes associated to the resource group.
key: optional string[]value: optional string[][]name: optional string
Name of the resource group.
[][]ResourceGroupGetResponse  { id, scope, meta, name }
A group of scoped resources.
id: string
Identifier of the resource group.
[]scope: array of  { key, objects }
The scope associated to the resource group
key: string
This is a combination of pre-defined resource name and identifier (like Account ID etc.)
[]objects: array of  { key }
A list of scope objects for additional context.
key: string
This is a combination of pre-defined resource name and identifier (like Zone ID etc.)
[][][]meta: optional  { key, value }
Attributes associated to the resource group.
key: optional string[]value: optional string[][]name: optional string
Name of the resource group.
[][]ResourceGroupCreateResponse  { id, scope, meta, name }
A group of scoped resources.
id: string
Identifier of the resource group.
[]scope: array of  { key, objects }
The scope associated to the resource group
key: string
This is a combination of pre-defined resource name and identifier (like Account ID etc.)
[]objects: array of  { key }
A list of scope objects for additional context.
key: string
This is a combination of pre-defined resource name and identifier (like Zone ID etc.)
[][][]meta: optional  { key, value }
Attributes associated to the resource group.
key: optional string[]value: optional string[][]name: optional string
Name of the resource group.
[][]ResourceGroupUpdateResponse  { id, scope, meta, name }
A group of scoped resources.
id: string
Identifier of the resource group.
[]scope: array of  { key, objects }
The scope associated to the resource group
key: string
This is a combination of pre-defined resource name and identifier (like Account ID etc.)
[]objects: array of  { key }
A list of scope objects for additional context.
key: string
This is a combination of pre-defined resource name and identifier (like Zone ID etc.)
[][][]meta: optional  { key, value }
Attributes associated to the resource group.
key: optional string[]value: optional string[][]name: optional string
Name of the resource group.
[][]ResourceGroupDeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]