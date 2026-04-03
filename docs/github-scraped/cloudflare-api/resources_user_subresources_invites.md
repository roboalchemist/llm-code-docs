# Invites | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/invites

[API Reference][User]
# Invites

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