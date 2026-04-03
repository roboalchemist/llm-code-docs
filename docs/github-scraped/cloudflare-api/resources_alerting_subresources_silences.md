# Silences | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/alerting/subresources/silences

[API Reference][Alerting]
# Silences

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