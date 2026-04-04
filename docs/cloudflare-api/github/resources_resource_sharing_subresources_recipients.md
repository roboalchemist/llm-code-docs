# Recipients | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients

[API Reference][Resource Sharing]
# Recipients

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