# Resource Sharing | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/resource_sharing

[API Reference]
# Resource Sharing

##### [List account shares]
GET/accounts/{account_id}/shares
##### [Get account share by ID]
GET/accounts/{account_id}/shares/{share_id}
##### [Create a new share]
POST/accounts/{account_id}/shares
##### [Update a share]
PUT/accounts/{account_id}/shares/{share_id}
##### [Delete a share]
DELETE/accounts/{account_id}/shares/{share_id}
##### ModelsExpand Collapse
ResourceSharingListResponse  { id, account_id, account_name, 12 more } id: string
Share identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]account_name: string
The display name of an account.
[]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]name: string
The name of the share.
[]organization_id: string
Organization identifier.
maxLength32[]status: "active" or "deleting" or "deleted"One of the following:"active"[]"deleting"[]"deleted"[][]target_type: "account" or "organization"One of the following:"account"[]"organization"[][]associated_recipient_count: optional number
The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]associating_recipient_count: optional number
The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociated_recipient_count: optional number
The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociating_recipient_count: optional number
The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]kind: optional "sent" or "received"One of the following:"sent"[]"received"[][]resources: optional array of  { id, created, meta, 6 more }
A list of resources that are part of the share. This field is only included when requested via the ‘include_resources’ parameter.
id: string
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
One of the following:"active"[]"deleting"[]"deleted"[][][][]ResourceSharingGetResponse  { id, account_id, account_name, 12 more } id: string
Share identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]account_name: string
The display name of an account.
[]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]name: string
The name of the share.
[]organization_id: string
Organization identifier.
maxLength32[]status: "active" or "deleting" or "deleted"One of the following:"active"[]"deleting"[]"deleted"[][]target_type: "account" or "organization"One of the following:"account"[]"organization"[][]associated_recipient_count: optional number
The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]associating_recipient_count: optional number
The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociated_recipient_count: optional number
The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociating_recipient_count: optional number
The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]kind: optional "sent" or "received"One of the following:"sent"[]"received"[][]resources: optional array of  { id, created, meta, 6 more }
A list of resources that are part of the share. This field is only included when requested via the ‘include_resources’ parameter.
id: string
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
One of the following:"active"[]"deleting"[]"deleted"[][][][]ResourceSharingCreateResponse  { id, account_id, account_name, 12 more } id: string
Share identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]account_name: string
The display name of an account.
[]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]name: string
The name of the share.
[]organization_id: string
Organization identifier.
maxLength32[]status: "active" or "deleting" or "deleted"One of the following:"active"[]"deleting"[]"deleted"[][]target_type: "account" or "organization"One of the following:"account"[]"organization"[][]associated_recipient_count: optional number
The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]associating_recipient_count: optional number
The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociated_recipient_count: optional number
The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociating_recipient_count: optional number
The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]kind: optional "sent" or "received"One of the following:"sent"[]"received"[][]resources: optional array of  { id, created, meta, 6 more }
A list of resources that are part of the share. This field is only included when requested via the ‘include_resources’ parameter.
id: string
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
One of the following:"active"[]"deleting"[]"deleted"[][][][]ResourceSharingUpdateResponse  { id, account_id, account_name, 12 more } id: string
Share identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]account_name: string
The display name of an account.
[]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]name: string
The name of the share.
[]organization_id: string
Organization identifier.
maxLength32[]status: "active" or "deleting" or "deleted"One of the following:"active"[]"deleting"[]"deleted"[][]target_type: "account" or "organization"One of the following:"account"[]"organization"[][]associated_recipient_count: optional number
The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]associating_recipient_count: optional number
The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociated_recipient_count: optional number
The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociating_recipient_count: optional number
The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]kind: optional "sent" or "received"One of the following:"sent"[]"received"[][]resources: optional array of  { id, created, meta, 6 more }
A list of resources that are part of the share. This field is only included when requested via the ‘include_resources’ parameter.
id: string
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
One of the following:"active"[]"deleting"[]"deleted"[][][][]ResourceSharingDeleteResponse  { id, account_id, account_name, 12 more } id: string
Share identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]account_name: string
The display name of an account.
[]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]name: string
The name of the share.
[]organization_id: string
Organization identifier.
maxLength32[]status: "active" or "deleting" or "deleted"One of the following:"active"[]"deleting"[]"deleted"[][]target_type: "account" or "organization"One of the following:"account"[]"organization"[][]associated_recipient_count: optional number
The number of recipients in the ‘associated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]associating_recipient_count: optional number
The number of recipients in the ‘associating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociated_recipient_count: optional number
The number of recipients in the ‘disassociated’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]disassociating_recipient_count: optional number
The number of recipients in the ‘disassociating’ state. This field is only included when requested via the ‘include_recipient_counts’ parameter.
[]kind: optional "sent" or "received"One of the following:"sent"[]"received"[][]resources: optional array of  { id, created, meta, 6 more }
A list of resources that are part of the share. This field is only included when requested via the ‘include_resources’ parameter.
id: string
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
One of the following:"active"[]"deleting"[]"deleted"[][][][]
#### Resource SharingRecipients

##### [List share recipients by share ID]
GET/accounts/{account_id}/shares/{share_id}/recipients
##### [Get share recipient by ID]
GET/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}
##### [Create a new share recipient]
POST/accounts/{account_id}/shares/{share_id}/recipients
##### [Delete a share recipient]
DELETE/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}
##### ModelsExpand Collapse
RecipientListResponse  { id, account_id, association_status, 3 more } id: string
Share Recipient identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]association_status: "associating" or "associated" or "disassociating" or "disassociated"
Share Recipient association status.
One of the following:"associating"[]"associated"[]"disassociating"[]"disassociated"[][]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]resources: optional array of  { error, resource_id, resource_version, terminal } error: string
Share Recipient error message.
[]resource_id: string
Share Resource identifier.
maxLength32[]resource_version: number
Resource Version.
[]terminal: boolean
Whether the error is terminal or will be continually retried.
[][][]RecipientGetResponse  { id, account_id, association_status, 3 more } id: string
Share Recipient identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]association_status: "associating" or "associated" or "disassociating" or "disassociated"
Share Recipient association status.
One of the following:"associating"[]"associated"[]"disassociating"[]"disassociated"[][]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]resources: optional array of  { error, resource_id, resource_version, terminal } error: string
Share Recipient error message.
[]resource_id: string
Share Resource identifier.
maxLength32[]resource_version: number
Resource Version.
[]terminal: boolean
Whether the error is terminal or will be continually retried.
[][][]RecipientCreateResponse  { id, account_id, association_status, 3 more } id: string
Share Recipient identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]association_status: "associating" or "associated" or "disassociating" or "disassociated"
Share Recipient association status.
One of the following:"associating"[]"associated"[]"disassociating"[]"disassociated"[][]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]resources: optional array of  { error, resource_id, resource_version, terminal } error: string
Share Recipient error message.
[]resource_id: string
Share Resource identifier.
maxLength32[]resource_version: number
Resource Version.
[]terminal: boolean
Whether the error is terminal or will be continually retried.
[][][]RecipientDeleteResponse  { id, account_id, association_status, 3 more } id: string
Share Recipient identifier tag.
maxLength32[]account_id: string
Account identifier.
maxLength32[]association_status: "associating" or "associated" or "disassociating" or "disassociated"
Share Recipient association status.
One of the following:"associating"[]"associated"[]"disassociating"[]"disassociated"[][]created: string
When the share was created.
formatdate-time[]modified: string
When the share was modified.
formatdate-time[]resources: optional array of  { error, resource_id, resource_version, terminal } error: string
Share Recipient error message.
[]resource_id: string
Share Resource identifier.
maxLength32[]resource_version: number
Resource Version.
[]terminal: boolean
Whether the error is terminal or will be continually retried.
[][][]
#### Resource SharingResources

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