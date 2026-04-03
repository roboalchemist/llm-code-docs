# Recommendations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ssl/subresources/recommendations

[API Reference][SSL]
# Recommendations

##### [SSL/TLS Recommendation]
DeprecatedGET/zones/{zone_id}/ssl/recommendation
##### ModelsExpand Collapse
RecommendationGetResponse  { id, editable, modified_on, 2 more } id: string[]editable: boolean
Whether this setting can be updated or not.
[]modified_on: string
Last time this setting was modified.
formatdate-time[]value: "auto" or "custom"
Current setting of the automatic SSL/TLS.
One of the following:"auto"[]"custom"[][]next_scheduled_scan: optional string
Next time this zone will be scanned by the Automatic SSL/TLS.
formatdate-time[][]