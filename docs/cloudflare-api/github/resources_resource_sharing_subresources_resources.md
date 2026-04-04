# Resources | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources

[API Reference][Resource Sharing]
# Resources

##### [List share resources by share ID]
GET/accounts/{account_id}/shares/{share_id}/resources
##### [Get share resource by ID]
GET/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
##### [Create a new share resource]
POST/accounts/{account_id}/shares/{share_id}/resources
##### [Update a share resource]
PUT/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
##### [Delete a share resource]
DELETE/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
##### ModelsExpand Collapse
ResourceListResponse  { id, created, meta, 6 more } id: string
Share Resource identifier.
maxLength32[]created: string
When the share was created.
formatdate-time[]meta: unknown
Resource Metadata.
[]modified: string
When the share was modified.
formatdate-time[]resource_account_id: string
Account identifier.
maxLength32[]resource_id: string
Share Resource identifier.
maxLength32[]resource_type: "custom-ruleset" or "gateway-policy" or "gateway-destination-ip" or 2 more
Resource Type.
One of the following:"custom-ruleset"[]"gateway-policy"[]"gateway-destination-ip"[]"gateway-block-page-settings"[]"gateway-extended-email-matching"[][]resource_version: number
Resource Version.
[]status: "active" or "deleting" or "deleted"
Resource Status.
One of the following:"active"[]"deleting"[]"deleted"[][][]ResourceGetResponse  { id, created, meta, 6 more } id: string
Share Resource identifier.
maxLength32[]created: string
When the share was created.
formatdate-time[]meta: unknown
Resource Metadata.
[]modified: string
When the share was modified.
formatdate-time[]resource_account_id: string
Account identifier.
maxLength32[]resource_id: string
Share Resource identifier.
maxLength32[]resource_type: "custom-ruleset" or "gateway-policy" or "gateway-destination-ip" or 2 more
Resource Type.
One of the following:"custom-ruleset"[]"gateway-policy"[]"gateway-destination-ip"[]"gateway-block-page-settings"[]"gateway-extended-email-matching"[][]resource_version: number
Resource Version.
[]status: "active" or "deleting" or "deleted"
Resource Status.
One of the following:"active"[]"deleting"[]"deleted"[][][]ResourceCreateResponse  { id, created, meta, 6 more } id: string
Share Resource identifier.
maxLength32[]created: string
When the share was created.
formatdate-time[]meta: unknown
Resource Metadata.
[]modified: string
When the share was modified.
formatdate-time[]resource_account_id: string
Account identifier.
maxLength32[]resource_id: string
Share Resource identifier.
maxLength32[]resource_type: "custom-ruleset" or "gateway-policy" or "gateway-destination-ip" or 2 more
Resource Type.
One of the following:"custom-ruleset"[]"gateway-policy"[]"gateway-destination-ip"[]"gateway-block-page-settings"[]"gateway-extended-email-matching"[][]resource_version: number
Resource Version.
[]status: "active" or "deleting" or "deleted"
Resource Status.
One of the following:"active"[]"deleting"[]"deleted"[][][]ResourceUpdateResponse  { id, created, meta, 6 more } id: string
Share Resource identifier.
maxLength32[]created: string
When the share was created.
formatdate-time[]meta: unknown
Resource Metadata.
[]modified: string
When the share was modified.
formatdate-time[]resource_account_id: string
Account identifier.
maxLength32[]resource_id: string
Share Resource identifier.
maxLength32[]resource_type: "custom-ruleset" or "gateway-policy" or "gateway-destination-ip" or 2 more
Resource Type.
One of the following:"custom-ruleset"[]"gateway-policy"[]"gateway-destination-ip"[]"gateway-block-page-settings"[]"gateway-extended-email-matching"[][]resource_version: number
Resource Version.
[]status: "active" or "deleting" or "deleted"
Resource Status.
One of the following:"active"[]"deleting"[]"deleted"[][][]ResourceDeleteResponse  { id, created, meta, 6 more } id: string
Share Resource identifier.
maxLength32[]created: string
When the share was created.
formatdate-time[]meta: unknown
Resource Metadata.
[]modified: string
When the share was modified.
formatdate-time[]resource_account_id: string
Account identifier.
maxLength32[]resource_id: string
Share Resource identifier.
maxLength32[]resource_type: "custom-ruleset" or "gateway-policy" or "gateway-destination-ip" or 2 more
Resource Type.
One of the following:"custom-ruleset"[]"gateway-policy"[]"gateway-destination-ip"[]"gateway-block-page-settings"[]"gateway-extended-email-matching"[][]resource_version: number
Resource Version.
[]status: "active" or "deleting" or "deleted"
Resource Status.
One of the following:"active"[]"deleting"[]"deleted"[][][]