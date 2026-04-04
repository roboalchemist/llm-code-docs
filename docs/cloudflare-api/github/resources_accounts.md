# Accounts | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/accounts

[API Reference]
# Accounts

##### [List Accounts]
GET/accounts
##### [Account Details]
GET/accounts/{account_id}
##### [Create an account]
POST/accounts
##### [Update Account]
PUT/accounts/{account_id}
##### [Delete a specific account]
DELETE/accounts/{account_id}
##### ModelsExpand Collapse
Account  { id, name, type, 3 more } id: string
Identifier
maxLength32minLength32[]name: string
Account name
maxLength100[]type: "standard" or "enterprise"One of the following:"standard"[]"enterprise"[][]created_on: optional string
Timestamp for the creation of the account
formatdate-time[]managed_by: optional  { parent_org_id, parent_org_name }
Parent container details
parent_org_id: optional string
ID of the parent Organization, if one exists
maxLength32[]parent_org_name: optional string
Name of the parent Organization, if one exists
[][]settings: optional  { abuse_contact_email, enforce_twofactor }
Account settings
abuse_contact_email: optional string
Sets an abuse contact email to notify for abuse reports.
[]enforce_twofactor: optional boolean
Indicates whether membership in this account requires that
Two-Factor Authentication is enabled
[][][]AccountDeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]
#### AccountsAccount Organizations

##### [Move account]
POST/accounts/{account_id}/move
##### ModelsExpand Collapse
AccountOrganizationCreateResponse  { account_id, destination_organization_id, source_organization_id } account_id: string[]destination_organization_id: string[]source_organization_id: string[][]
#### AccountsAccount Profile

##### [Get account profile]
GET/accounts/{account_id}/profile
##### [Modify account profile]
PUT/accounts/{account_id}/profile
##### ModelsExpand Collapse
AccountProfile  { business_address, business_email, business_name, 2 more } business_address: string[]business_email: string[]business_name: string[]business_phone: string[]external_metadata: string[][]
#### AccountsMembers

##### [List Members]
GET/accounts/{account_id}/members
##### [Member Details]
GET/accounts/{account_id}/members/{member_id}
##### [Add Member]
POST/accounts/{account_id}/members
##### [Update Member]
PUT/accounts/{account_id}/members/{member_id}
##### [Remove Member]
DELETE/accounts/{account_id}/members/{member_id}
##### ModelsExpand Collapse
Status = "member" or "invited"
Whether the user is a member of the organization or has an invitation pending.
One of the following:"member"[]"invited"[][]MemberDeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]
#### AccountsRoles

##### [List Roles]
GET/accounts/{account_id}/roles
##### [Role Details]
GET/accounts/{account_id}/roles/{role_id}
#### AccountsSubscriptions

##### [List Subscriptions]
GET/accounts/{account_id}/subscriptions
##### [Create Subscription]
POST/accounts/{account_id}/subscriptions
##### [Update Subscription]
PUT/accounts/{account_id}/subscriptions/{subscription_identifier}
##### [Delete Subscription]
DELETE/accounts/{account_id}/subscriptions/{subscription_identifier}
##### ModelsExpand Collapse
SubscriptionDeleteResponse  { subscription_id } subscription_id: optional string
Subscription identifier tag.
maxLength32[][]
#### AccountsTokens

##### [List Tokens]
GET/accounts/{account_id}/tokens
##### [Token Details]
GET/accounts/{account_id}/tokens/{token_id}
##### [Create Token]
POST/accounts/{account_id}/tokens
##### [Update Token]
PUT/accounts/{account_id}/tokens/{token_id}
##### [Delete Token]
DELETE/accounts/{account_id}/tokens/{token_id}
##### [Verify Token]
GET/accounts/{account_id}/tokens/verify
##### ModelsExpand Collapse
TokenCreateResponse  { id, condition, expires_on, 8 more } id: optional string
Token identifier tag.
maxLength32[]condition: optional  { request_ip } request_ip: optional  { in, not_in }
Client IP restrictions.
in: optional array of [TokenConditionCIDRList]
List of IPv4/IPv6 CIDR addresses.
[]not_in: optional array of [TokenConditionCIDRList]
List of IPv4/IPv6 CIDR addresses.
[][][]expires_on: optional string
The expiration time on or after which the JWT MUST NOT be accepted for processing.
formatdate-time[]issued_on: optional string
The time on which the token was created.
formatdate-time[]last_used_on: optional string
Last time the token was used.
formatdate-time[]modified_on: optional string
Last time the token was modified.
formatdate-time[]name: optional string
Token name.
maxLength120[]not_before: optional string
The time before which the token MUST NOT be accepted for processing.
formatdate-time[]policies: optional array of [TokenPolicy] { id, effect, permission_groups, resources }
List of access policies assigned to the token.
id: string
Policy identifier.
[]effect: "allow" or "deny"
Allow or deny operations against the resources.
One of the following:"allow"[]"deny"[][]permission_groups: array of  { id, meta, name }
A set of permission groups that are specified to the policy.
id: string
Identifier of the permission group.
[]meta: optional  { key, value }
Attributes associated to the permission group.
key: optional string[]value: optional string[][]name: optional string
Name of the permission group.
[][]resources: map[string] or map[map[string]]
A list of resource names that the policy applies to.
One of the following:IAMResourcesTypeObjectString = map[string]
Map of simple string resource permissions
[]IAMResourcesTypeObjectNested = map[map[string]]
Map of nested resource permissions
[][][]status: optional "active" or "disabled" or "expired"
Status of the token.
One of the following:"active"[]"disabled"[]"expired"[][]value: optional [TokenValue]
The token value.
maxLength80minLength40[][]TokenDeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]TokenVerifyResponse  { id, status, expires_on, not_before } id: string
Token identifier tag.
maxLength32[]status: "active" or "disabled" or "expired"
Status of the token.
One of the following:"active"[]"disabled"[]"expired"[][]expires_on: optional string
The expiration time on or after which the JWT MUST NOT be accepted for processing.
formatdate-time[]not_before: optional string
The time before which the token MUST NOT be accepted for processing.
formatdate-time[][]
#### AccountsTokensPermission Groups

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
#### AccountsTokensValue

##### [Roll Token]
PUT/accounts/{account_id}/tokens/{token_id}/value
#### AccountsLogs

#### AccountsLogsAudit

##### [Get account audit logs (Version 2)]
GET/accounts/{account_id}/logs/audit
##### ModelsExpand Collapse
AuditListResponse  { id, account, action, 4 more } id: optional string
A unique identifier for the audit log entry.
maxLength32[]account: optional  { id, name }
Contains account related information.
id: optional string
A unique identifier for the account.
[]name: optional string
A string that identifies the account name.
[][]action: optional  { description, result, time, type }
Provides information about the action performed.
description: optional string
A short description of the action performed.
[]result: optional string
The result of the action, indicating success or failure.
[]time: optional string
A timestamp indicating when the action was logged.
formatdate-time[]type: optional string
A short string that describes the action that was performed.
[][]actor: optional  { id, context, email, 4 more }
Provides details about the actor who performed the action.
id: optional string
The ID of the actor who performed the action. If a user performed the action, this will be their User ID.
[]context: optional "api_key" or "api_token" or "dash" or 2 moreOne of the following:"api_key"[]"api_token"[]"dash"[]"oauth"[]"origin_ca_key"[][]email: optional string
The email of the actor who performed the action.
formatemail[]ip_address: optional string
The IP address of the request that performed the action.
[]token_id: optional string
The API token ID when the actor context is an api_token or oauth.
[]token_name: optional string
The API token name when the actor context is an api_token or oauth.
[]type: optional "account" or "cloudflare_admin" or "system" or "user"
The type of actor.
One of the following:"account"[]"cloudflare_admin"[]"system"[]"user"[][][]raw: optional  { cf_ray_id, method, status_code, 2 more }
Provides raw information about the request and response.
cf_ray_id: optional string
The Cloudflare Ray ID for the request.
[]method: optional string
The HTTP method of the request.
[]status_code: optional number
The HTTP response status code returned by the API.
[]uri: optional string
The URI of the request.
[]user_agent: optional string
The client’s user agent string sent with the request.
[][]resource: optional  { id, product, request, 3 more }
Provides details about the affected resource.
id: optional string
The unique identifier for the affected resource.
[]product: optional string
The Cloudflare product associated with the resource.
[]request: optional unknown[]response: optional unknown[]scope: optional unknown
The scope of the resource.
[]type: optional string
The type of the resource.
[][]zone: optional  { id, name }
Provides details about the zone affected by the action.
id: optional string
A string that identifies the zone id.
[]name: optional string
A string that identifies the zone name.
[][][]