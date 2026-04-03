# Eligible | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/eligible

[API Reference][Alerting][Destinations]
# Eligible

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