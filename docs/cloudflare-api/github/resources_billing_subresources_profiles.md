# Profiles | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/billing/subresources/profiles

[API Reference][Billing]
# Profiles

##### [Billing Profile Details]
DeprecatedGET/accounts/{account_id}/billing/profile
##### ModelsExpand Collapse
ProfileGetResponse  { id, account_type, address, 36 more } id: optional string
Billing item identifier tag.
maxLength32[]account_type: optional string[]address: optional string[]address2: optional string[]balance: optional string[]card_expiry_month: optional number[]card_expiry_year: optional number[]card_number: optional string[]city: optional string[]company: optional string[]country: optional string[]created_on: optional stringformatdate-time[]device_data: optional string[]edited_on: optional stringformatdate-time[]enterprise_billing_email: optional string[]enterprise_primary_email: optional string[]first_name: optional string[]is_partner: optional boolean[]last_name: optional string[]next_bill_date: optional stringformatdate-time[]payment_address: optional string[]payment_address2: optional string[]payment_city: optional string[]payment_country: optional string[]payment_email: optional string[]payment_first_name: optional string[]payment_gateway: optional string[]payment_last_name: optional string[]payment_nonce: optional string[]payment_state: optional string[]payment_zipcode: optional string[]primary_email: optional string[]state: optional string[]tax_id_type: optional string[]telephone: optional string[]use_legacy: optional boolean[]validation_code: optional string[]vat: optional string[]zipcode: optional string[][]