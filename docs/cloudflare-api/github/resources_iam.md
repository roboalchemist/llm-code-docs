# IAM | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam

[API Reference]
# IAM

#### IAMPermission Groups

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
#### IAMResource Groups

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
#### IAMUser Groups

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
#### IAMUser GroupsMembers

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
#### IAMSSO

##### [Get all SSO connectors]
GET/accounts/{account_id}/sso_connectors
##### [Get single SSO connector]
GET/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Initialize new SSO connector]
POST/accounts/{account_id}/sso_connectors
##### [Update SSO connector state]
PATCH/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Delete SSO connector]
DELETE/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Begin SSO connector verification]
POST/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification
##### ModelsExpand Collapse
SSOListResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOGetResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOCreateResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOUpdateResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSODeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]SSOBeginVerificationResponse  { errors, messages, success } errors: array of  { code, message, documentation_url, source } code: numberminimum1000[]message: string[]documentation_url: optional string[]source: optional  { pointer } pointer: optional string[][][]messages: array of  { code, message, documentation_url, source } code: numberminimum1000[]message: string[]documentation_url: optional string[]source: optional  { pointer } pointer: optional string[][][]success: true
Whether the API call was successful.
[][]