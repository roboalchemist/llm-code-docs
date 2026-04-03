# Destinations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/destinations

[API Reference][Alerting]
# Destinations

#### DestinationsEligible

##### [Get delivery mechanism eligibility]
GET/accounts/{account_id}/alerting/v3/destinations/eligible
##### ModelsExpand Collapse
EligibleGetResponse = map[array of  { eligible, ready, type } ]eligible: optional boolean
Determines whether or not the account is eligible for the delivery mechanism.
[]ready: optional boolean
Beta flag. Users can create a policy with a mechanism that is not ready, but we cannot guarantee successful delivery of notifications.
[]type: optional "email" or "pagerduty" or "webhook"
Determines type of delivery mechanism.
One of the following:"email"[]"pagerduty"[]"webhook"[][][]
#### DestinationsPagerduty

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
#### DestinationsWebhooks

##### [List webhooks]
GET/accounts/{account_id}/alerting/v3/destinations/webhooks
##### [Get a webhook]
GET/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
##### [Create a webhook]
POST/accounts/{account_id}/alerting/v3/destinations/webhooks
##### [Update a webhook]
PUT/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
##### [Delete a webhook]
DELETE/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
##### ModelsExpand Collapse
Webhooks  { id, created_at, last_failure, 5 more } id: optional string
The unique identifier of a webhook
maxLength32[]created_at: optional string
Timestamp of when the webhook destination was created.
formatdate-time[]last_failure: optional string
Timestamp of the last time an attempt to dispatch a notification to this webhook failed.
formatdate-time[]last_success: optional string
Timestamp of the last time Cloudflare was able to successfully dispatch a notification using this webhook.
formatdate-time[]name: optional string
The name of the webhook destination. This will be included in the request body when you receive a webhook notification.
[]secret: optional string
Optional secret that will be passed in the `cf-webhook-auth` header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.
[]type: optional "datadog" or "discord" or "feishu" or 5 more
Type of webhook endpoint.
One of the following:"datadog"[]"discord"[]"feishu"[]"gchat"[]"generic"[]"opsgenie"[]"slack"[]"splunk"[][]url: optional string
The POST endpoint to call when dispatching a notification.
[][]WebhookCreateResponse  { id } id: optional string
UUID
maxLength32[][]WebhookUpdateResponse  { id } id: optional string
UUID
maxLength32[][]WebhookDeleteResponse  { errors, messages, success } errors: array of  { message, code } message: string[]code: optional numberminimum1000[][]messages: array of  { message, code } message: string[]code: optional numberminimum1000[][]success: true
Whether the API call was successful
[][]