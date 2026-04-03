# Default | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default

[API Reference][Zero Trust][Devices][Policies]
# Default

##### [Get the default device settings profile]
GET/accounts/{account_id}/devices/policy
##### [Update the default device settings profile]
PATCH/accounts/{account_id}/devices/policy
##### ModelsExpand Collapse
DefaultGetResponse  { allow_mode_switch, allow_updates, allowed_to_leave, 16 more } allow_mode_switch: optional boolean
Whether to allow the user to switch WARP between modes.
[]allow_updates: optional boolean
Whether to receive update notifications when a new version of the client is available.
[]allowed_to_leave: optional boolean
Whether to allow devices to leave the organization.
[]auto_connect: optional number
The amount of time in seconds to reconnect after having been disabled.
[]captive_portal: optional number
Turn on the captive portal after the specified amount of time.
[]default: optional boolean
Whether the policy will be applied to matching devices.
[]disable_auto_fallback: optional boolean
If the `dns_server` field of a fallback domain is not present, the client will fall back to a best guess of the default/system DNS resolvers unless this policy option is set to `true`.
[]enabled: optional boolean
Whether the policy will be applied to matching devices.
[]exclude: optional array of [SplitTunnelExclude]
List of routes excluded in the WARP client’s tunnel.
One of the following:TeamsDevicesExcludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to exclude from the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesExcludeSplitTunnelWithHost  { host, description } host: string
The domain name to exclude from the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]exclude_office_ips: optional boolean
Whether to add Microsoft IPs to Split Tunnel exclusions.
[]fallback_domains: optional array of [FallbackDomain] { suffix, description, dns_server } suffix: string
The domain suffix to match when resolving locally.
[]description: optional string
A description of the fallback domain, displayed in the client UI.
maxLength100[]dns_server: optional array of string
A list of IP addresses to handle domain resolution.
[][]gateway_unique_id: optional string[]include: optional array of [SplitTunnelInclude]
List of routes included in the WARP client’s tunnel.
One of the following:TeamsDevicesIncludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to include in the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesIncludeSplitTunnelWithHost  { host, description } host: string
The domain name to include in the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]register_interface_ip_with_dns: optional boolean
Determines if the operating system will register WARP’s local interface IP with your on-premises DNS server.
[]sccm_vpn_boundary_support: optional boolean
Determines whether the WARP client indicates to SCCM that it is inside a VPN boundary. (Windows only).
[]service_mode_v2: optional  { mode, port } mode: optional string
The mode to run the WARP client under.
[]port: optional number
The port number when used with proxy mode.
[][]support_url: optional string
The URL to launch when the Send Feedback button is clicked.
[]switch_locked: optional boolean
Whether to allow the user to turn off the WARP switch and disconnect the client.
[]tunnel_protocol: optional string
Determines which tunnel protocol to use.
[][]DefaultEditResponse  { allow_mode_switch, allow_updates, allowed_to_leave, 16 more } allow_mode_switch: optional boolean
Whether to allow the user to switch WARP between modes.
[]allow_updates: optional boolean
Whether to receive update notifications when a new version of the client is available.
[]allowed_to_leave: optional boolean
Whether to allow devices to leave the organization.
[]auto_connect: optional number
The amount of time in seconds to reconnect after having been disabled.
[]captive_portal: optional number
Turn on the captive portal after the specified amount of time.
[]default: optional boolean
Whether the policy will be applied to matching devices.
[]disable_auto_fallback: optional boolean
If the `dns_server` field of a fallback domain is not present, the client will fall back to a best guess of the default/system DNS resolvers unless this policy option is set to `true`.
[]enabled: optional boolean
Whether the policy will be applied to matching devices.
[]exclude: optional array of [SplitTunnelExclude]
List of routes excluded in the WARP client’s tunnel.
One of the following:TeamsDevicesExcludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to exclude from the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesExcludeSplitTunnelWithHost  { host, description } host: string
The domain name to exclude from the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]exclude_office_ips: optional boolean
Whether to add Microsoft IPs to Split Tunnel exclusions.
[]fallback_domains: optional array of [FallbackDomain] { suffix, description, dns_server } suffix: string
The domain suffix to match when resolving locally.
[]description: optional string
A description of the fallback domain, displayed in the client UI.
maxLength100[]dns_server: optional array of string
A list of IP addresses to handle domain resolution.
[][]gateway_unique_id: optional string[]include: optional array of [SplitTunnelInclude]
List of routes included in the WARP client’s tunnel.
One of the following:TeamsDevicesIncludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to include in the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesIncludeSplitTunnelWithHost  { host, description } host: string
The domain name to include in the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]register_interface_ip_with_dns: optional boolean
Determines if the operating system will register WARP’s local interface IP with your on-premises DNS server.
[]sccm_vpn_boundary_support: optional boolean
Determines whether the WARP client indicates to SCCM that it is inside a VPN boundary. (Windows only).
[]service_mode_v2: optional  { mode, port } mode: optional string
The mode to run the WARP client under.
[]port: optional number
The port number when used with proxy mode.
[][]support_url: optional string
The URL to launch when the Send Feedback button is clicked.
[]switch_locked: optional boolean
Whether to allow the user to turn off the WARP switch and disconnect the client.
[]tunnel_protocol: optional string
Determines which tunnel protocol to use.
[][]
#### DefaultExcludes

##### [Get the Split Tunnel exclude list]
GET/accounts/{account_id}/devices/policy/exclude
##### [Set the Split Tunnel exclude list]
PUT/accounts/{account_id}/devices/policy/exclude
#### DefaultIncludes

##### [Get the Split Tunnel include list]
GET/accounts/{account_id}/devices/policy/include
##### [Set the Split Tunnel include list]
PUT/accounts/{account_id}/devices/policy/include
#### DefaultFallback Domains

##### [Get your Local Domain Fallback list]
GET/accounts/{account_id}/devices/policy/fallback_domains
##### [Set your Local Domain Fallback list]
PUT/accounts/{account_id}/devices/policy/fallback_domains
#### DefaultCertificates

##### [Get device certificate provisioning status]
GET/zones/{zone_id}/devices/policy/certificates
##### [Update device certificate provisioning status]
PATCH/zones/{zone_id}/devices/policy/certificates