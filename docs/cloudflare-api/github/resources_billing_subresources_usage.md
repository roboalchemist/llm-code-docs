# Usage | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/billing/subresources/usage

[API Reference][Billing]
# Usage

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