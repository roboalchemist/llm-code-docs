# Integrations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations

[API Reference][Zero Trust][Devices][Posture]
# Integrations

##### [List your device posture integrations]
GET/accounts/{account_id}/devices/posture/integration
##### [Get device posture integration details]
GET/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Create a device posture integration]
POST/accounts/{account_id}/devices/posture/integration
##### [Update a device posture integration]
PATCH/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Delete a device posture integration]
DELETE/accounts/{account_id}/devices/posture/integration/{integration_id}
##### ModelsExpand Collapse
Integration  { id, config, interval, 2 more } id: optional string
API UUID.
maxLength36[]config: optional  { api_url, auth_url, client_id }
The configuration object containing third-party integration information.
api_url: string
The Workspace One API URL provided in the Workspace One Admin Dashboard.
[]auth_url: string
The Workspace One Authorization URL depending on your region.
[]client_id: string
The Workspace One client ID provided in the Workspace One Admin Dashboard.
[][]interval: optional string
The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
[]name: optional string
The name of the device posture integration.
[]type: optional "workspace_one" or "crowdstrike_s2s" or "uptycs" or 5 more
The type of device posture integration.
One of the following:"workspace_one"[]"crowdstrike_s2s"[]"uptycs"[]"intune"[]"kolide"[]"tanium_s2s"[]"sentinelone_s2s"[]"custom_s2s"[][][]IntegrationDeleteResponse = unknown or stringOne of the following:unknown[]string[][]