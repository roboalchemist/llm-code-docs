# Pagerduty | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty

[API Reference][Alerting][Destinations]
# Pagerduty

##### [List PagerDuty services]
GET/accounts/{account_id}/alerting/v3/destinations/pagerduty
##### [Create PagerDuty integration token]
POST/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect
##### [Delete PagerDuty Services]
DELETE/accounts/{account_id}/alerting/v3/destinations/pagerduty
##### [Connect PagerDuty]
GET/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}
##### ModelsExpand Collapse
Pagerduty  { id, name } id: optional string
UUID
maxLength32[]name: optional string
The name of the pagerduty service.
[][]PagerdutyCreateResponse  { id } id: optional string
token in form of UUID
maxLength32[][]PagerdutyDeleteResponse  { errors, messages, success } errors: array of  { message, code } message: string[]code: optional numberminimum1000[][]messages: array of  { message, code } message: string[]code: optional numberminimum1000[][]success: true
Whether the API call was successful
[][]PagerdutyLinkResponse  { id } id: optional string
UUID
maxLength32[][]