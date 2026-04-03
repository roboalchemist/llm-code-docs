# User | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user

[API Reference]
# User

##### [User Details]
GET/user
##### [Edit User]
PATCH/user
##### ModelsExpand Collapse
UserGetResponse  { id, betas, country, 11 more } id: optional string
Identifier of the user.
[]betas: optional array of string
Lists the betas that the user is participating in.
[]country: optional string
The country in which the user lives.
maxLength30[]first_name: optional string
User’s first name
maxLength60[]has_business_zones: optional boolean
Indicates whether user has any business zones
[]has_enterprise_zones: optional boolean
Indicates whether user has any enterprise zones
[]has_pro_zones: optional boolean
Indicates whether user has any pro zones
[]last_name: optional string
User’s last name
maxLength60[]organizations: optional array of [Organization] { id, name, permissions, 2 more } id: optional string
Identifier
maxLength32minLength32[]name: optional string
Organization name.
maxLength100[]permissions: optional array of [Permission]
Access permissions for this User.
[]roles: optional array of string
List of roles that a user has within an organization.
[]status: optional [Status]
Whether the user is a member of the organization or has an invitation pending.
[][]suspended: optional boolean
Indicates whether user has been suspended
[]telephone: optional string
User’s telephone number
maxLength20[]two_factor_authentication_enabled: optional boolean
Indicates whether two-factor authentication is enabled for the user account. Does not apply to API authentication.
[]two_factor_authentication_locked: optional boolean
Indicates whether two-factor authentication is required by one of the accounts that the user is a member of.
[]zipcode: optional string
The zipcode or postal code where the user lives.
maxLength20[][]UserEditResponse  { id, betas, country, 11 more } id: optional string
Identifier of the user.
[]betas: optional array of string
Lists the betas that the user is participating in.
[]country: optional string
The country in which the user lives.
maxLength30[]first_name: optional string
User’s first name
maxLength60[]has_business_zones: optional boolean
Indicates whether user has any business zones
[]has_enterprise_zones: optional boolean
Indicates whether user has any enterprise zones
[]has_pro_zones: optional boolean
Indicates whether user has any pro zones
[]last_name: optional string
User’s last name
maxLength60[]organizations: optional array of [Organization] { id, name, permissions, 2 more } id: optional string
Identifier
maxLength32minLength32[]name: optional string
Organization name.
maxLength100[]permissions: optional array of [Permission]
Access permissions for this User.
[]roles: optional array of string
List of roles that a user has within an organization.
[]status: optional [Status]
Whether the user is a member of the organization or has an invitation pending.
[][]suspended: optional boolean
Indicates whether user has been suspended
[]telephone: optional string
User’s telephone number
maxLength20[]two_factor_authentication_enabled: optional boolean
Indicates whether two-factor authentication is enabled for the user account. Does not apply to API authentication.
[]two_factor_authentication_locked: optional boolean
Indicates whether two-factor authentication is required by one of the accounts that the user is a member of.
[]zipcode: optional string
The zipcode or postal code where the user lives.
maxLength20[][]
#### UserAudit Logs

##### [Get user audit logs]
GET/user/audit_logs
#### UserBilling

#### UserBillingHistory

##### [Billing History Details]
DeprecatedGET/user/billing/history
##### ModelsExpand Collapse
BillingHistory  { id, action, amount, 5 more } id: string
Billing item identifier tag.
maxLength32[]action: string
The billing item action.
maxLength30[]amount: number
The amount associated with this billing item.
[]currency: string
The monetary unit in which pricing information is displayed.
[]description: string
The billing item description.
maxLength255[]occurred_at: string
When the billing item was created.
formatdate-time[]type: string
The billing item type.
maxLength30[]zone:  { name } name: optional string[][][]
#### UserBillingProfile

##### [Billing Profile Details]
DeprecatedGET/user/billing/profile
##### ModelsExpand Collapse
ProfileGetResponse  { id, account_type, address, 36 more } id: optional string
Billing item identifier tag.
maxLength32[]account_type: optional string[]address: optional string[]address2: optional string[]balance: optional string[]card_expiry_month: optional number[]card_expiry_year: optional number[]card_number: optional string[]city: optional string[]company: optional string[]country: optional string[]created_on: optional stringformatdate-time[]device_data: optional string[]edited_on: optional stringformatdate-time[]enterprise_billing_email: optional string[]enterprise_primary_email: optional string[]first_name: optional string[]is_partner: optional boolean[]last_name: optional string[]next_bill_date: optional stringformatdate-time[]payment_address: optional string[]payment_address2: optional string[]payment_city: optional string[]payment_country: optional string[]payment_email: optional string[]payment_first_name: optional string[]payment_gateway: optional string[]payment_last_name: optional string[]payment_nonce: optional string[]payment_state: optional string[]payment_zipcode: optional string[]primary_email: optional string[]state: optional string[]tax_id_type: optional string[]telephone: optional string[]use_legacy: optional boolean[]validation_code: optional string[]vat: optional string[]zipcode: optional string[][]
#### UserInvites

##### [List Invitations]
GET/user/invites
##### [Invitation Details]
GET/user/invites/{invite_id}
##### [Respond to Invitation]
PATCH/user/invites/{invite_id}
##### ModelsExpand Collapse
Invite  { invited_member_id, organization_id, id, 8 more } invited_member_id: string
ID of the user to add to the organization.
maxLength32[]organization_id: string
ID of the organization the user will be added to.
maxLength32[]id: optional string
Invite identifier tag.
maxLength32[]expires_on: optional string
When the invite is no longer active.
formatdate-time[]invited_by: optional string
The email address of the user who created the invite.
maxLength90[]invited_member_email: optional string
Email address of the user to add to the organization.
maxLength90[]invited_on: optional string
When the invite was sent.
formatdate-time[]organization_is_enforcing_twofactor: optional boolean[]organization_name: optional string
Organization name.
maxLength100[]roles: optional array of string
List of role names the membership has for this account.
[]status: optional "pending" or "accepted" or "rejected" or "expired"
Current status of the invitation.
One of the following:"pending"[]"accepted"[]"rejected"[]"expired"[][][]
#### UserOrganizations

##### [List Organizations]
DeprecatedGET/user/organizations
##### [Organization Details]
DeprecatedGET/user/organizations/{organization_id}
##### [Leave Organization]
DeprecatedDELETE/user/organizations/{organization_id}
##### ModelsExpand Collapse
Organization  { id, name, permissions, 2 more } id: optional string
Identifier
maxLength32minLength32[]name: optional string
Organization name.
maxLength100[]permissions: optional array of [Permission]
Access permissions for this User.
[]roles: optional array of string
List of roles that a user has within an organization.
[]status: optional [Status]
Whether the user is a member of the organization or has an invitation pending.
[][]OrganizationGetResponse = unknown[]OrganizationDeleteResponse  { id } id: optional string
Identifier
maxLength32minLength32[][]
#### UserSubscriptions

##### [Get User Subscriptions]
GET/user/subscriptions
##### [Update User Subscription]
PUT/user/subscriptions/{identifier}
##### [Delete User Subscription]
DELETE/user/subscriptions/{identifier}
##### ModelsExpand Collapse
SubscriptionUpdateResponse = unknown or stringOne of the following:unknown[]string[][]SubscriptionDeleteResponse  { subscription_id } subscription_id: optional string
Subscription identifier tag.
maxLength32[][]
#### UserTokens

##### [List Tokens]
GET/user/tokens
##### [Token Details]
GET/user/tokens/{token_id}
##### [Create Token]
POST/user/tokens
##### [Update Token]
PUT/user/tokens/{token_id}
##### [Delete Token]
DELETE/user/tokens/{token_id}
##### [Verify Token]
GET/user/tokens/verify
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
#### UserTokensPermission Groups

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
#### UserTokensValue

##### [Roll Token]
PUT/user/tokens/{token_id}/value