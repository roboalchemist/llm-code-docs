# IP Profiles | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles

[API Reference][Zero Trust][Devices]
# IP Profiles

##### [List IP profiles]
GET/accounts/{account_id}/devices/ip-profiles
##### [Get IP profile]
GET/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Create IP profile]
POST/accounts/{account_id}/devices/ip-profiles
##### [Update IP profile]
PATCH/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Delete IP profile]
DELETE/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### ModelsExpand Collapse
IPProfile  { id, created_at, description, 6 more } id: string
The ID of the Device IP profile.
[]created_at: string
The RFC3339Nano timestamp when the Device IP profile was created.
[]description: string
An optional description of the Device IP profile.
[]enabled: boolean
Whether the Device IP profile is enabled.
[]match: string
The wirefilter expression to match registrations. Available values: “identity.name”, “identity.email”, “identity.groups.id”, “identity.groups.name”, “identity.groups.email”, “identity.saml_attributes”.
maxLength10000[]name: string
A user-friendly name for the Device IP profile.
[]precedence: number
The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.
[]subnet_id: string
The ID of the Subnet.
[]updated_at: string
The RFC3339Nano timestamp when the Device IP profile was last updated.
[][]IPProfileDeleteResponse  { id } id: optional string
ID of the deleted Device IP profile.
[][]