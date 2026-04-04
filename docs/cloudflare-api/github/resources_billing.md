# Billing | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/billing

[API Reference]
# Billing

#### BillingProfiles

##### [Billing Profile Details]
DeprecatedGET/accounts/{account_id}/billing/profile
##### ModelsExpand Collapse
ProfileGetResponse  { id, account_type, address, 36 more } id: optional string
Billing item identifier tag.
maxLength32[]account_type: optional string[]address: optional string[]address2: optional string[]balance: optional string[]card_expiry_month: optional number[]card_expiry_year: optional number[]card_number: optional string[]city: optional string[]company: optional string[]country: optional string[]created_on: optional stringformatdate-time[]device_data: optional string[]edited_on: optional stringformatdate-time[]enterprise_billing_email: optional string[]enterprise_primary_email: optional string[]first_name: optional string[]is_partner: optional boolean[]last_name: optional string[]next_bill_date: optional stringformatdate-time[]payment_address: optional string[]payment_address2: optional string[]payment_city: optional string[]payment_country: optional string[]payment_email: optional string[]payment_first_name: optional string[]payment_gateway: optional string[]payment_last_name: optional string[]payment_nonce: optional string[]payment_state: optional string[]payment_zipcode: optional string[]primary_email: optional string[]state: optional string[]tax_id_type: optional string[]telephone: optional string[]use_legacy: optional boolean[]validation_code: optional string[]vat: optional string[]zipcode: optional string[][]
#### BillingUsage

##### [Get PayGo Account Billable Usage (Beta)]
GET/accounts/{account_id}/billing/usage/paygo
##### ModelsExpand Collapse
UsagePaygoResponse = array of  { BillingCurrency, BillingPeriodStart, ChargePeriodEnd, 8 more }
Contains the array of billable usage records.
BillingCurrency: string
Specifies the billing currency code (ISO 4217).
[]BillingPeriodStart: string
Indicates the start of the billing period.
formatdate-time[]ChargePeriodEnd: string
Indicates the end of the charge period.
formatdate-time[]ChargePeriodStart: string
Indicates the start of the charge period.
formatdate-time[]ConsumedQuantity: number
Specifies the quantity consumed during this charge period.
[]ConsumedUnit: string
Specifies the unit of measurement for consumed quantity.
[]ContractedCost: number
Specifies the cost for this charge period in the billing currency.
[]CumulatedContractedCost: number
Specifies the cumulated cost for the billing period in the billing currency.
[]CumulatedPricingQuantity: number
Specifies the cumulated pricing quantity for the billing period.
[]PricingQuantity: number
Specifies the pricing quantity for this charge period.
[]ServiceName: string
Identifies the Cloudflare service.
[][]