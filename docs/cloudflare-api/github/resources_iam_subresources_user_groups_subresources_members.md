# Members | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members

[API Reference][IAM][User Groups]
# Members

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