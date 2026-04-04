# Organizations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/organizations

[API Reference][User]
# Organizations

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