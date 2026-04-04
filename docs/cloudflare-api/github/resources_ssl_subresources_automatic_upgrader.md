# Automatic Upgrader | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ssl/subresources/automatic_upgrader

[API Reference][SSL]
# Automatic Upgrader

##### [Get Automatic SSL/TLS enrollment status for the given zone]
GET/zones/{zone_id}/settings/ssl_automatic_mode
##### [Patch Automatic SSL/TLS Enrollment status for given zone]
PATCH/zones/{zone_id}/settings/ssl_automatic_mode
##### ModelsExpand Collapse
AutomaticUpgraderGetResponse  { id, editable, modified_on, 2 more } id: string[]editable: boolean
Whether this setting can be updated or not.
[]modified_on: string
Last time this setting was modified.
formatdate-time[]value: "auto" or "custom"
Current setting of the automatic SSL/TLS.
One of the following:"auto"[]"custom"[][]next_scheduled_scan: optional string
Next time this zone will be scanned by the Automatic SSL/TLS.
formatdate-time[][]AutomaticUpgraderPatchResponse  { id, editable, modified_on, 2 more } id: string[]editable: boolean
Whether this setting can be updated or not.
[]modified_on: string
Last time this setting was modified.
formatdate-time[]value: "auto" or "custom"
Current setting of the automatic SSL/TLS.
One of the following:"auto"[]"custom"[][]next_scheduled_scan: optional string
Next time this zone will be scanned by the Automatic SSL/TLS.
formatdate-time[][]