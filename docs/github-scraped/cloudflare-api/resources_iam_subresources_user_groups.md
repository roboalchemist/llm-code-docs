# User Groups | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam/subresources/user_groups

[API Reference][IAM]
# User Groups

##### [List User Groups]
GET/accounts/{account_id}/iam/user_groups
##### [User Group Details]
GET/accounts/{account_id}/iam/user_groups/{user_group_id}
##### [Create User Group]
POST/accounts/{account_id}/iam/user_groups
##### [Update User Group]
PUT/accounts/{account_id}/iam/user_groups/{user_group_id}
##### [Remove User Group]
DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}
##### ModelsExpand Collapse
UserGroupListResponse  { id, created_on, modified_on, 2 more }
A group of policies resources.
id: string
User Group identifier tag.
maxLength32minLength32[]created_on: string
Timestamp for the creation of the user group
formatdate-time[]modified_on: string
Last time the user group was modified.
formatdate-time[]name: string
Name of the user group.
[]policies: optional array of  { id, access, permission_groups, resource_groups }
Policies attached to the User group
id: optional string
Policy identifier.
[]access: optional "allow" or "deny"
Allow or deny operations against the resources.
One of the following:"allow"[]"deny"[][]permission_groups: optional array of  { id, meta, name }
A set of permission groups that are specified to the policy.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]resource_groups: optional array of  { id, scope, meta, name }
A list of resource groups that the policy applies to.
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
[][][][]UserGroupGetResponse  { id, created_on, modified_on, 2 more }
A group of policies resources.
id: string
User Group identifier tag.
maxLength32minLength32[]created_on: string
Timestamp for the creation of the user group
formatdate-time[]modified_on: string
Last time the user group was modified.
formatdate-time[]name: string
Name of the user group.
[]policies: optional array of  { id, access, permission_groups, resource_groups }
Policies attached to the User group
id: optional string
Policy identifier.
[]access: optional "allow" or "deny"
Allow or deny operations against the resources.
One of the following:"allow"[]"deny"[][]permission_groups: optional array of  { id, meta, name }
A set of permission groups that are specified to the policy.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]resource_groups: optional array of  { id, scope, meta, name }
A list of resource groups that the policy applies to.
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
[][][][]UserGroupCreateResponse  { id, created_on, modified_on, 2 more }
A group of policies resources.
id: string
User Group identifier tag.
maxLength32minLength32[]created_on: string
Timestamp for the creation of the user group
formatdate-time[]modified_on: string
Last time the user group was modified.
formatdate-time[]name: string
Name of the user group.
[]policies: optional array of  { id, access, permission_groups, resource_groups }
Policies attached to the User group
id: optional string
Policy identifier.
[]access: optional "allow" or "deny"
Allow or deny operations against the resources.
One of the following:"allow"[]"deny"[][]permission_groups: optional array of  { id, meta, name }
A set of permission groups that are specified to the policy.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]resource_groups: optional array of  { id, scope, meta, name }
A list of resource groups that the policy applies to.
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
[][][][]UserGroupUpdateResponse  { id, created_on, modified_on, 2 more }
A group of policies resources.
id: string
User Group identifier tag.
maxLength32minLength32[]created_on: string
Timestamp for the creation of the user group
formatdate-time[]modified_on: string
Last time the user group was modified.
formatdate-time[]name: string
Name of the user group.
[]policies: optional array of  { id, access, permission_groups, resource_groups }
Policies attached to the User group
id: optional string
Policy identifier.
[]access: optional "allow" or "deny"
Allow or deny operations against the resources.
One of the following:"allow"[]"deny"[][]permission_groups: optional array of  { id, meta, name }
A set of permission groups that are specified to the policy.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]resource_groups: optional array of  { id, scope, meta, name }
A list of resource groups that the policy applies to.
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
[][][][]UserGroupDeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]
#### User GroupsMembers

##### [List User Group Members]
GET/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Add User Group Members]
POST/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Update User Group Members]
PUT/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Remove User Group Member]
DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}
##### ModelsExpand Collapse
MemberListResponse  { id, email, status }
Member attached to a User Group.
id: string
Account member identifier.
[]email: optional string
The contact email address of the user.
maxLength90[]status: optional "accepted" or "pending"
The member’s status in the account.
One of the following:"accepted"[]"pending"[][][]MemberCreateResponse  { id, email, status }
Member attached to a User Group.
id: string
Account member identifier.
[]email: optional string
The contact email address of the user.
maxLength90[]status: optional "accepted" or "pending"
The member’s status in the account.
One of the following:"accepted"[]"pending"[][][]MemberUpdateResponse  { id, email, status }
Member attached to a User Group.
id: string
Account member identifier.
[]email: optional string
The contact email address of the user.
maxLength90[]status: optional "accepted" or "pending"
The member’s status in the account.
One of the following:"accepted"[]"pending"[][][]MemberDeleteResponse  { id, email, status }
Member attached to a User Group.
id: string
Account member identifier.
[]email: optional string
The contact email address of the user.
maxLength90[]status: optional "accepted" or "pending"
The member’s status in the account.
One of the following:"accepted"[]"pending"[][][]