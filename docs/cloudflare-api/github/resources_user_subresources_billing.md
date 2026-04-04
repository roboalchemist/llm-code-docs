# Billing | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/billing

[API Reference][User]
# Billing

#### BillingHistory

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
#### BillingProfile

##### [Billing Profile Details]
DeprecatedGET/user/billing/profile
##### ModelsExpand Collapse
ProfileGetResponse  { id, account_type, address, 36 more } id: optional string
Billing item identifier tag.
maxLength32[]account_type: optional string[]address: optional string[]address2: optional string[]balance: optional string[]card_expiry_month: optional number[]card_expiry_year: optional number[]card_number: optional string[]city: optional string[]company: optional string[]country: optional string[]created_on: optional stringformatdate-time[]device_data: optional string[]edited_on: optional stringformatdate-time[]enterprise_billing_email: optional string[]enterprise_primary_email: optional string[]first_name: optional string[]is_partner: optional boolean[]last_name: optional string[]next_bill_date: optional stringformatdate-time[]payment_address: optional string[]payment_address2: optional string[]payment_city: optional string[]payment_country: optional string[]payment_email: optional string[]payment_first_name: optional string[]payment_gateway: optional string[]payment_last_name: optional string[]payment_nonce: optional string[]payment_state: optional string[]payment_zipcode: optional string[]primary_email: optional string[]state: optional string[]tax_id_type: optional string[]telephone: optional string[]use_legacy: optional boolean[]validation_code: optional string[]vat: optional string[]zipcode: optional string[][]