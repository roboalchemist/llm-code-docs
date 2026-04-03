# Fallback Origin | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin

[API Reference][Custom Hostnames]
# Fallback Origin

##### [Get Fallback Origin for Custom Hostnames]
GET/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Update Fallback Origin for Custom Hostnames]
PUT/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Delete Fallback Origin for Custom Hostnames]
DELETE/zones/{zone_id}/custom_hostnames/fallback_origin
##### ModelsExpand Collapse
FallbackOriginGetResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]FallbackOriginUpdateResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]FallbackOriginDeleteResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]