# TLS | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/hostnames/subresources/settings/subresources/tls

[API Reference][Hostnames][Settings]
# TLS

##### [List TLS setting for hostnames]
GET/zones/{zone_id}/hostnames/settings/{setting_id}
##### [Edit TLS setting for hostname]
PUT/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
##### [Delete TLS setting for hostname]
DELETE/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
##### ModelsExpand Collapse
Setting  { created_at, hostname, status, 2 more } created_at: optional string
This is the time the tls setting was originally created for this hostname.
formatdate-time[]hostname: optional string
The hostname for which the tls settings are set.
[]status: optional string
Deployment status for the given tls setting.
[]updated_at: optional string
This is the time the tls setting was updated.
formatdate-time[]value: optional [SettingValue]
The TLS setting value. The type depends on the `setting_id` used in the request path:

- `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g., `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)

- `min_tls_version`: a string indicating the minimum TLS version — one of `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)

- `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"` (e.g., `"on"`)

[][]SettingValue = "1.0" or "1.1" or "1.2" or 3 more or array of string
The TLS setting value. The type depends on the `setting_id` used in the request path:

- `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g., `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)

- `min_tls_version`: a string indicating the minimum TLS version — one of `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)

- `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"` (e.g., `"on"`)

One of the following:"1.0" or "1.1" or "1.2" or 3 moreOne of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[]"on"[]"off"[][]array of string
Used when `setting_id` is `ciphers`. An array of allowed cipher suite strings.
[][]TLSGetResponse  { created_at, hostname, status, 2 more } created_at: optional string
This is the time the tls setting was originally created for this hostname.
formatdate-time[]hostname: optional string
The hostname for which the tls settings are set.
[]status: optional string
Deployment status for the given tls setting.
[]updated_at: optional string
This is the time the tls setting was updated.
formatdate-time[]value: optional [SettingValue]
The TLS setting value. The type depends on the `setting_id` used in the request path:

- `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g., `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)

- `min_tls_version`: a string indicating the minimum TLS version — one of `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)

- `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"` (e.g., `"on"`)

[][]TLSDeleteResponse  { created_at, hostname, status, 2 more } created_at: optional string
This is the time the tls setting was originally created for this hostname.
formatdate-time[]hostname: optional string
The hostname for which the tls settings are set.
[]status: optional string
Deployment status for the given tls setting.
[]updated_at: optional string
This is the time the tls setting was updated.
formatdate-time[]value: optional [SettingValue]
The TLS setting value. The type depends on the `setting_id` used in the request path:

- `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g., `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)

- `min_tls_version`: a string indicating the minimum TLS version — one of `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)

- `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"` (e.g., `"on"`)

[][]