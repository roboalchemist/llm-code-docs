# History | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/billing/subresources/history

[API Reference][User][Billing]
# History

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