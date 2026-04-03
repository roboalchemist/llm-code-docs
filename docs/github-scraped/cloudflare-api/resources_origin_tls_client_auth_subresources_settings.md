# Settings | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/settings

[API Reference][Origin TLS Client Auth]
# Settings

##### [Get Enablement Setting for Zone]
GET/zones/{zone_id}/origin_tls_client_auth/settings
##### [Set Enablement for Zone]
PUT/zones/{zone_id}/origin_tls_client_auth/settings
##### ModelsExpand Collapse
SettingGetResponse  { enabled } enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[][]SettingUpdateResponse  { enabled } enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[][]