# Global WARP Override | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/resilience/subresources/global_warp_override

[API Reference][Zero Trust][Devices][Resilience]
# Global WARP Override

##### [Retrieve Global WARP override state]
GET/accounts/{account_id}/devices/resilience/disconnect
##### [Set Global WARP override state]
POST/accounts/{account_id}/devices/resilience/disconnect
##### ModelsExpand Collapse
GlobalWARPOverrideGetResponse  { disconnect, timestamp } disconnect: optional boolean
Disconnects all devices on the account using Global WARP override.
[]timestamp: optional string
When the Global WARP override state was updated.
formatdate-time[][]GlobalWARPOverrideCreateResponse  { disconnect, timestamp } disconnect: optional boolean
Disconnects all devices on the account using Global WARP override.
[]timestamp: optional string
When the Global WARP override state was updated.
formatdate-time[][]