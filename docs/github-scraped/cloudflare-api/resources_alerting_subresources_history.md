# History | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/history

[API Reference][Alerting]
# History

##### [List History]
GET/accounts/{account_id}/alerting/v3/history
##### ModelsExpand Collapse
History  { id, alert_body, alert_type, 6 more } id: optional string
UUID
maxLength32[]alert_body: optional string
Message body included in the notification sent.
[]alert_type: optional string
Type of notification that has been dispatched.
[]description: optional string
Description of the notification policy (if present).
[]mechanism: optional string
The mechanism to which the notification has been dispatched.
[]mechanism_type: optional "email" or "pagerduty" or "webhook"
The type of mechanism to which the notification has been dispatched. This can be email/pagerduty/webhook based on the mechanism configured.
One of the following:"email"[]"pagerduty"[]"webhook"[][]name: optional string
Name of the policy.
[]policy_id: optional string
The unique identifier of a notification policy
maxLength32[]sent: optional string
Timestamp of when the notification was dispatched in ISO 8601 format.
formatdate-time[][]