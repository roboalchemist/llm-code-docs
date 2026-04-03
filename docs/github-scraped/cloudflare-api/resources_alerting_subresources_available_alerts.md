# Available Alerts | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/available_alerts

[API Reference][Alerting]
# Available Alerts

##### [Get Alert Types]
GET/accounts/{account_id}/alerting/v3/available_alerts
##### ModelsExpand Collapse
AvailableAlertListResponse = map[array of  { description, display_name, filter_options, type } ]description: optional string
Describes the alert type.
[]display_name: optional string
Alert type name.
[]filter_options: optional array of unknown
Format of additional configuration options (filters) for the alert type. Data type of filters during policy creation: Array of strings.
[]type: optional string
Use this value when creating and updating a notification policy.
[][]