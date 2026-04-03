# Tokens | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/accounts/subresources/tokens

[API Reference][Accounts]
# Tokens

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
#### TokensPermission Groups

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
#### TokensValue

##### [Roll Token]
PUT/accounts/{account_id}/tokens/{token_id}/value