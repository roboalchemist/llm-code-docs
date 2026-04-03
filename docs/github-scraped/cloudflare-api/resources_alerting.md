# Alerting | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting

[API Reference]
# Alerting

#### AlertingAvailable Alerts

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
#### AlertingDestinations

#### AlertingDestinationsEligible

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
#### AlertingDestinationsPagerduty

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
#### AlertingDestinationsWebhooks

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
#### AlertingHistory

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
#### AlertingPolicies

##### [List Notification policies]
GET/accounts/{account_id}/alerting/v3/policies
##### [Get a Notification policy]
GET/accounts/{account_id}/alerting/v3/policies/{policy_id}
##### [Create a Notification policy]
POST/accounts/{account_id}/alerting/v3/policies
##### [Update a Notification policy]
PUT/accounts/{account_id}/alerting/v3/policies/{policy_id}
##### [Delete a Notification policy]
DELETE/accounts/{account_id}/alerting/v3/policies/{policy_id}
##### ModelsExpand Collapse
Mechanism  { email, pagerduty, webhooks }
List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
email: optional array of  { id } id: optional string
The email address
[][]pagerduty: optional array of  { id } id: optional string
UUID
maxLength32[][]webhooks: optional array of  { id } id: optional string
UUID
maxLength32[][][]Policy  { id, alert_interval, alert_type, 7 more } id: optional string
The unique identifier of a notification policy
maxLength32[]alert_interval: optional string
Optional specification of how often to re-alert from the same incident, not support on all alert types.
[]alert_type: optional "abuse_report_alert" or "access_custom_certificate_expiration_type" or "advanced_ddos_attack_l4_alert" or 66 more
Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which then will give you a list of possible values.
One of the following:"abuse_report_alert"[]"access_custom_certificate_expiration_type"[]"advanced_ddos_attack_l4_alert"[]"advanced_ddos_attack_l7_alert"[]"advanced_http_alert_error"[]"bgp_hijack_notification"[]"billing_usage_alert"[]"block_notification_block_removed"[]"block_notification_new_block"[]"block_notification_review_rejected"[]"bot_traffic_basic_alert"[]"brand_protection_alert"[]"brand_protection_digest"[]"clickhouse_alert_fw_anomaly"[]"clickhouse_alert_fw_ent_anomaly"[]"cloudforce_one_request_notification"[]"cni_maintenance_notification"[]"custom_analytics"[]"custom_bot_detection_alert"[]"custom_ssl_certificate_event_type"[]"dedicated_ssl_certificate_event_type"[]"device_connectivity_anomaly_alert"[]"dos_attack_l4"[]"dos_attack_l7"[]"expiring_service_token_alert"[]"failing_logpush_job_disabled_alert"[]"fbm_auto_advertisement"[]"fbm_dosd_attack"[]"fbm_volumetric_attack"[]"health_check_status_notification"[]"hostname_aop_custom_certificate_expiration_type"[]"http_alert_edge_error"[]"http_alert_origin_error"[]"image_notification"[]"image_resizing_notification"[]"incident_alert"[]"load_balancing_health_alert"[]"load_balancing_pool_enablement_alert"[]"logo_match_alert"[]"magic_tunnel_health_check_event"[]"magic_wan_tunnel_health"[]"maintenance_event_notification"[]"mtls_certificate_store_certificate_expiration_type"[]"pages_event_alert"[]"radar_notification"[]"real_origin_monitoring"[]"scriptmonitor_alert_new_code_change_detections"[]"scriptmonitor_alert_new_hosts"[]"scriptmonitor_alert_new_malicious_hosts"[]"scriptmonitor_alert_new_malicious_scripts"[]"scriptmonitor_alert_new_malicious_url"[]"scriptmonitor_alert_new_max_length_resource_url"[]"scriptmonitor_alert_new_resources"[]"secondary_dns_all_primaries_failing"[]"secondary_dns_primaries_failing"[]"secondary_dns_warning"[]"secondary_dns_zone_successfully_updated"[]"secondary_dns_zone_validation_warning"[]"security_insights_alert"[]"sentinel_alert"[]"stream_live_notifications"[]"synthetic_test_latency_alert"[]"synthetic_test_low_availability_alert"[]"traffic_anomalies_alert"[]"tunnel_health_event"[]"tunnel_update_event"[]"universal_ssl_event_type"[]"web_analytics_metrics_update"[]"zone_aop_custom_certificate_expiration_type"[][]created: optional stringformatdate-time[]description: optional string
Optional description for the Notification policy.
[]enabled: optional boolean
Whether or not the Notification policy is enabled.
[]filters: optional [PolicyFilter] { actions, affected_asns, affected_components, 40 more }
Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria. This is only available for select alert types. See alert type documentation for more details.
[]mechanisms: optional [Mechanism] { email, pagerduty, webhooks }
List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
[]modified: optional stringformatdate-time[]name: optional string
Name of the policy.
[][]PolicyFilter  { actions, affected_asns, affected_components, 40 more }
Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria. This is only available for select alert types. See alert type documentation for more details.
actions: optional array of string
Usage depends on specific alert type
[]affected_asns: optional array of string
Used for configuring radar_notification
[]affected_components: optional array of string
Used for configuring incident_alert
[]affected_locations: optional array of string
Used for configuring radar_notification
[]airport_code: optional array of string
Used for configuring maintenance_event_notification
[]alert_trigger_preferences: optional array of string
Usage depends on specific alert type
[]alert_trigger_preferences_value: optional array of string
Usage depends on specific alert type
[]enabled: optional array of string
Used for configuring load_balancing_pool_enablement_alert
[]environment: optional array of string
Used for configuring pages_event_alert
[]event: optional array of string
Used for configuring pages_event_alert
[]event_source: optional array of string
Used for configuring load_balancing_health_alert
[]event_type: optional array of string
Usage depends on specific alert type
[]group_by: optional array of string
Usage depends on specific alert type
[]health_check_id: optional array of string
Used for configuring health_check_status_notification
[]incident_impact: optional array of "INCIDENT_IMPACT_NONE" or "INCIDENT_IMPACT_MINOR" or "INCIDENT_IMPACT_MAJOR" or "INCIDENT_IMPACT_CRITICAL"
Used for configuring incident_alert
One of the following:"INCIDENT_IMPACT_NONE"[]"INCIDENT_IMPACT_MINOR"[]"INCIDENT_IMPACT_MAJOR"[]"INCIDENT_IMPACT_CRITICAL"[][]input_id: optional array of string
Used for configuring stream_live_notifications
[]insight_class: optional array of string
Used for configuring security_insights_alert
[]limit: optional array of string
Used for configuring billing_usage_alert
[]logo_tag: optional array of string
Used for configuring logo_match_alert
[]megabits_per_second: optional array of string
Used for configuring advanced_ddos_attack_l4_alert
[]new_health: optional array of string
Used for configuring load_balancing_health_alert
[]new_status: optional array of string
Used for configuring tunnel_health_event
[]packets_per_second: optional array of string
Used for configuring advanced_ddos_attack_l4_alert
[]pool_id: optional array of string
Usage depends on specific alert type
[]pop_names: optional array of string
Usage depends on specific alert type
[]product: optional array of string
Used for configuring billing_usage_alert
[]project_id: optional array of string
Used for configuring pages_event_alert
[]protocol: optional array of string
Used for configuring advanced_ddos_attack_l4_alert
[]query_tag: optional array of string
Usage depends on specific alert type
[]requests_per_second: optional array of string
Used for configuring advanced_ddos_attack_l7_alert
[]selectors: optional array of string
Usage depends on specific alert type
[]services: optional array of string
Used for configuring clickhouse_alert_fw_ent_anomaly
[]slo: optional array of string
Usage depends on specific alert type
[]status: optional array of string
Used for configuring health_check_status_notification
[]target_hostname: optional array of string
Used for configuring advanced_ddos_attack_l7_alert
[]target_ip: optional array of string
Used for configuring advanced_ddos_attack_l4_alert
[]target_zone_name: optional array of string
Used for configuring advanced_ddos_attack_l7_alert
[]traffic_exclusions: optional array of "security_events"
Used for configuring traffic_anomalies_alert
[]tunnel_id: optional array of string
Used for configuring tunnel_health_event
[]tunnel_name: optional array of string
Usage depends on specific alert type
[]type: optional array of string
Usage depends on specific alert type
[]where: optional array of string
Usage depends on specific alert type
[]zones: optional array of string
Usage depends on specific alert type
[][]PolicyCreateResponse  { id } id: optional string
UUID
maxLength32[][]PolicyUpdateResponse  { id } id: optional string
UUID
maxLength32[][]PolicyDeleteResponse  { errors, messages, success, result_info } errors: array of  { message, code } message: string[]code: optional numberminimum1000[][]messages: array of  { message, code } message: string[]code: optional numberminimum1000[][]success: true
Whether the API call was successful
[]result_info: optional  { count, page, per_page, total_count } count: optional number
Total number of results for the requested service
[]page: optional number
Current page within paginated list of results
[]per_page: optional number
Number of results per page of results
[]total_count: optional number
Total results available without any search parameters
[][][]
#### AlertingSilences

##### [List Silences]
GET/accounts/{account_id}/alerting/v3/silences
##### [Get Silence]
GET/accounts/{account_id}/alerting/v3/silences/{silence_id}
##### [Create Silences]
POST/accounts/{account_id}/alerting/v3/silences
##### [Update Silences]
PUT/accounts/{account_id}/alerting/v3/silences
##### [Delete Silence]
DELETE/accounts/{account_id}/alerting/v3/silences/{silence_id}
##### ModelsExpand Collapse
SilenceListResponse  { id, created_at, end_time, 3 more } id: optional string
Silence ID
maxLength32[]created_at: optional string
When the silence was created.
[]end_time: optional string
When the silence ends.
[]policy_id: optional string
The unique identifier of a notification policy
maxLength32[]start_time: optional string
When the silence starts.
[]updated_at: optional string
When the silence was modified.
[][]SilenceGetResponse  { id, created_at, end_time, 3 more } id: optional string
Silence ID
maxLength32[]created_at: optional string
When the silence was created.
[]end_time: optional string
When the silence ends.
[]policy_id: optional string
The unique identifier of a notification policy
maxLength32[]start_time: optional string
When the silence starts.
[]updated_at: optional string
When the silence was modified.
[][]SilenceCreateResponse  { errors, messages, success } errors: array of  { message, code } message: string[]code: optional numberminimum1000[][]messages: array of  { message, code } message: string[]code: optional numberminimum1000[][]success: true
Whether the API call was successful
[][]SilenceUpdateResponse  { id, created_at, end_time, 3 more } id: optional string
Silence ID
maxLength32[]created_at: optional string
When the silence was created.
[]end_time: optional string
When the silence ends.
[]policy_id: optional string
The unique identifier of a notification policy
maxLength32[]start_time: optional string
When the silence starts.
[]updated_at: optional string
When the silence was modified.
[][]SilenceDeleteResponse  { errors, messages, success } errors: array of  { message, code } message: string[]code: optional numberminimum1000[][]messages: array of  { message, code } message: string[]code: optional numberminimum1000[][]success: true
Whether the API call was successful
[][]