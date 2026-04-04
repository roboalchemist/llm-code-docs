# Memberships | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/memberships

[API Reference]
# Memberships

##### [List Memberships]
GET/memberships
##### [Membership Details]
GET/memberships/{membership_id}
##### [Update Membership]
PUT/memberships/{membership_id}
##### [Delete Membership]
DELETE/memberships/{membership_id}
##### ModelsExpand Collapse
Membership  { id, account, api_access_enabled, 3 more } id: optional string
Membership identifier tag.
maxLength32[]account: optional [Account] { id, name, type, 3 more } []api_access_enabled: optional boolean
Enterprise only. Indicates whether or not API access is enabled specifically for this user on a given account.
[]permissions: optional  { analytics, billing, cache_purge, 9 more }
All access permissions for the user at the account.
analytics: optional [PermissionGrant] { read, write } []billing: optional [PermissionGrant] { read, write } []cache_purge: optional [PermissionGrant] { read, write } []dns: optional [PermissionGrant] { read, write } []dns_records: optional [PermissionGrant] { read, write } []lb: optional [PermissionGrant] { read, write } []logs: optional [PermissionGrant] { read, write } []organization: optional [PermissionGrant] { read, write } []ssl: optional [PermissionGrant] { read, write } []waf: optional [PermissionGrant] { read, write } []zone_settings: optional [PermissionGrant] { read, write } []zones: optional [PermissionGrant] { read, write } [][]roles: optional array of string
List of role names the membership has for this account.
[]status: optional "accepted" or "pending" or "rejected"
Status of this membership.
One of the following:"accepted"[]"pending"[]"rejected"[][][]MembershipGetResponse  { id, account, api_access_enabled, 4 more } id: optional string
Membership identifier tag.
maxLength32[]account: optional [Account] { id, name, type, 3 more } []api_access_enabled: optional boolean
Enterprise only. Indicates whether or not API access is enabled specifically for this user on a given account.
[]permissions: optional  { analytics, billing, cache_purge, 9 more }
All access permissions for the user at the account.
analytics: optional [PermissionGrant] { read, write } []billing: optional [PermissionGrant] { read, write } []cache_purge: optional [PermissionGrant] { read, write } []dns: optional [PermissionGrant] { read, write } []dns_records: optional [PermissionGrant] { read, write } []lb: optional [PermissionGrant] { read, write } []logs: optional [PermissionGrant] { read, write } []organization: optional [PermissionGrant] { read, write } []ssl: optional [PermissionGrant] { read, write } []waf: optional [PermissionGrant] { read, write } []zone_settings: optional [PermissionGrant] { read, write } []zones: optional [PermissionGrant] { read, write } [][]policies: optional array of  { id, access, permission_groups, resource_groups }
Access policy for the membership
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
[][][]roles: optional array of string
List of role names the membership has for this account.
[]status: optional "accepted" or "pending" or "rejected"
Status of this membership.
One of the following:"accepted"[]"pending"[]"rejected"[][][]MembershipUpdateResponse  { id, account, api_access_enabled, 4 more } id: optional string
Membership identifier tag.
maxLength32[]account: optional [Account] { id, name, type, 3 more } []api_access_enabled: optional boolean
Enterprise only. Indicates whether or not API access is enabled specifically for this user on a given account.
[]permissions: optional  { analytics, billing, cache_purge, 9 more }
All access permissions for the user at the account.
analytics: optional [PermissionGrant] { read, write } []billing: optional [PermissionGrant] { read, write } []cache_purge: optional [PermissionGrant] { read, write } []dns: optional [PermissionGrant] { read, write } []dns_records: optional [PermissionGrant] { read, write } []lb: optional [PermissionGrant] { read, write } []logs: optional [PermissionGrant] { read, write } []organization: optional [PermissionGrant] { read, write } []ssl: optional [PermissionGrant] { read, write } []waf: optional [PermissionGrant] { read, write } []zone_settings: optional [PermissionGrant] { read, write } []zones: optional [PermissionGrant] { read, write } [][]policies: optional array of  { id, access, permission_groups, resource_groups }
Access policy for the membership
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
[][][]roles: optional array of string
List of role names the membership has for this account.
[]status: optional "accepted" or "pending" or "rejected"
Status of this membership.
One of the following:"accepted"[]"pending"[]"rejected"[][][]MembershipDeleteResponse  { id } id: optional string
Membership identifier tag.
maxLength32[][]