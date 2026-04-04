# Devices | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices

[API Reference][Zero Trust]
# Devices

##### [List devices (deprecated)]
DeprecatedGET/accounts/{account_id}/devices
##### [Get device (deprecated)]
DeprecatedGET/accounts/{account_id}/devices/{device_id}
##### ModelsExpand Collapse
Device  { id, created, deleted, 17 more } id: optional string
Registration ID. Equal to Device ID except for accounts which enabled [multi-user mode].
maxLength36[]created: optional string
When the device was created.
formatdate-time[]deleted: optional boolean
True if the device was deleted.
[]device_type: optional "windows" or "mac" or "linux" or 3 moreOne of the following:"windows"[]"mac"[]"linux"[]"android"[]"ios"[]"chromeos"[][]ip: optional string
IPv4 or IPv6 address.
[]key: optional string
The device’s public key.
[]last_seen: optional string
When the device last connected to Cloudflare services.
formatdate-time[]mac_address: optional string
The device mac address.
[]manufacturer: optional string
The device manufacturer name.
[]model: optional string
The device model name.
[]name: optional string
The device name.
[]os_distro_name: optional string
The Linux distro name.
[]os_distro_revision: optional string
The Linux distro revision.
[]os_version: optional string
The operating system version.
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[]revoked_at: optional string
When the device was revoked.
formatdate-time[]serial_number: optional string
The device serial number.
[]updated: optional string
When the device was updated.
formatdate-time[]user: optional  { id, email, name } id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][]version: optional string
The WARP client version.
[][]DeviceGetResponse  { id, account, created, 16 more } id: optional string
Registration ID. Equal to Device ID except for accounts which enabled [multi-user mode].
maxLength36[]account: optional  { id, account_type, name } Deprecatedid: optional string[]Deprecatedaccount_type: optional string[]name: optional string
The name of the enrolled account.
[][]created: optional string
When the device was created.
formatdate-time[]deleted: optional boolean
True if the device was deleted.
[]device_type: optional string[]Deprecatedgateway_device_id: optional string[]ip: optional string
IPv4 or IPv6 address.
[]key: optional string
The device’s public key.
[]key_type: optional string
Type of the key.
[]last_seen: optional string
When the device last connected to Cloudflare services.
formatdate-time[]mac_address: optional string
The device mac address.
[]model: optional string
The device model name.
[]name: optional string
The device name.
[]os_version: optional string
The operating system version.
[]serial_number: optional string
The device serial number.
[]tunnel_type: optional string
Type of the tunnel connection used.
[]updated: optional string
When the device was updated.
formatdate-time[]user: optional  { id, email, name } id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][]version: optional string
The WARP client version.
[][]
#### DevicesDevices

##### [List devices]
GET/accounts/{account_id}/devices/physical-devices
##### [Get device]
GET/accounts/{account_id}/devices/physical-devices/{device_id}
##### [Delete device]
DELETE/accounts/{account_id}/devices/physical-devices/{device_id}
##### [Revoke device registrations]
POST/accounts/{account_id}/devices/physical-devices/{device_id}/revoke
##### ModelsExpand Collapse
DeviceListResponse  { id, active_registrations, created_at, 16 more }
A WARP Device.
id: string
The unique ID of the device.
[]active_registrations: number
The number of active registrations for the device. Active registrations are those which haven’t been revoked or deleted.
[]created_at: string
The RFC3339 timestamp when the device was created.
[]last_seen_at: string
The RFC3339 timestamp when the device was last seen.
[]name: string
The name of the device.
[]updated_at: string
The RFC3339 timestamp when the device was last updated.
[]client_version: optional string
Version of the WARP client.
[]deleted_at: optional string
The RFC3339 timestamp when the device was deleted.
[]device_type: optional string
The device operating system.
[]hardware_id: optional string
A string that uniquely identifies the hardware or virtual machine (VM).
[]last_seen_registration: optional  { policy }
The last seen registration for the device.
policy: optional  { id, default, deleted, 2 more }
A summary of the device profile evaluated for the registration.
id: string
The ID of the device settings profile.
[]default: boolean
Whether the device settings profile is the default profile for the account.
[]deleted: boolean
Whether the device settings profile was deleted.
[]name: string
The name of the device settings profile.
[]updated_at: string
The RFC3339 timestamp of when the device settings profile last changed for the registration.
[][][]last_seen_user: optional  { id, email, name }
The last user to use the WARP device.
id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][]mac_address: optional string
The device MAC address.
[]manufacturer: optional string
The device manufacturer.
[]model: optional string
The model name of the device.
[]os_version: optional string
The device operating system version number.
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[]Deprecatedpublic_ip: optional string
**Deprecated**: IP information is provided by DEX - see [https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list/]
[]serial_number: optional string
The device serial number.
[][]DeviceGetResponse  { id, active_registrations, created_at, 16 more }
A WARP Device.
id: string
The unique ID of the device.
[]active_registrations: number
The number of active registrations for the device. Active registrations are those which haven’t been revoked or deleted.
[]created_at: string
The RFC3339 timestamp when the device was created.
[]last_seen_at: string
The RFC3339 timestamp when the device was last seen.
[]name: string
The name of the device.
[]updated_at: string
The RFC3339 timestamp when the device was last updated.
[]client_version: optional string
Version of the WARP client.
[]deleted_at: optional string
The RFC3339 timestamp when the device was deleted.
[]device_type: optional string
The device operating system.
[]hardware_id: optional string
A string that uniquely identifies the hardware or virtual machine (VM).
[]last_seen_registration: optional  { policy }
The last seen registration for the device.
policy: optional  { id, default, deleted, 2 more }
A summary of the device profile evaluated for the registration.
id: string
The ID of the device settings profile.
[]default: boolean
Whether the device settings profile is the default profile for the account.
[]deleted: boolean
Whether the device settings profile was deleted.
[]name: string
The name of the device settings profile.
[]updated_at: string
The RFC3339 timestamp of when the device settings profile last changed for the registration.
[][][]last_seen_user: optional  { id, email, name }
The last user to use the WARP device.
id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][]mac_address: optional string
The device MAC address.
[]manufacturer: optional string
The device manufacturer.
[]model: optional string
The model name of the device.
[]os_version: optional string
The device operating system version number.
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[]Deprecatedpublic_ip: optional string
**Deprecated**: IP information is provided by DEX - see [https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list/]
[]serial_number: optional string
The device serial number.
[][]DeviceDeleteResponse = unknown[]DeviceRevokeResponse = unknown[]
#### DevicesResilience

#### DevicesResilienceGlobal WARP Override

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
#### DevicesRegistrations

##### [List registrations]
GET/accounts/{account_id}/devices/registrations
##### [Get registration]
GET/accounts/{account_id}/devices/registrations/{registration_id}
##### [Delete registration]
DELETE/accounts/{account_id}/devices/registrations/{registration_id}
##### [Delete registrations]
DELETE/accounts/{account_id}/devices/registrations
##### [Revoke registrations]
POST/accounts/{account_id}/devices/registrations/revoke
##### [Unrevoke registrations]
POST/accounts/{account_id}/devices/registrations/unrevoke
##### ModelsExpand Collapse
RegistrationListResponse  { id, created_at, device, 9 more }
A WARP configuration tied to a single user. Multiple registrations can be created from a single WARP device.
id: string
The ID of the registration.
[]created_at: string
The RFC3339 timestamp when the registration was created.
[]device:  { id, name, client_version }
Device details embedded inside of a registration.
id: string
The ID of the device.
[]name: string
The name of the device.
[]client_version: optional string
Version of the WARP client.
[][]key: string
The public key used to connect to the Cloudflare network.
[]last_seen_at: string
The RFC3339 timestamp when the registration was last seen.
[]updated_at: string
The RFC3339 timestamp when the registration was last updated.
[]deleted_at: optional string
The RFC3339 timestamp when the registration was deleted.
[]key_type: optional string
The type of encryption key used by the WARP client for the active key. Currently ‘curve25519’ for WireGuard and ‘secp256r1’ for MASQUE.
[]policy: optional  { id, default, deleted, 2 more }
The device settings profile assigned to this registration.
id: string
The ID of the device settings profile.
[]default: boolean
Whether the device settings profile is the default profile for the account.
[]deleted: boolean
Whether the device settings profile was deleted.
[]name: string
The name of the device settings profile.
[]updated_at: string
The RFC3339 timestamp of when the device settings profile last changed for the registration.
[][]revoked_at: optional string
The RFC3339 timestamp when the registration was revoked.
[]tunnel_type: optional string
Type of the tunnel - wireguard or masque.
[]user: optional  { id, email, name } id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][][]RegistrationGetResponse  { id, created_at, device, 9 more }
A WARP configuration tied to a single user. Multiple registrations can be created from a single WARP device.
id: string
The ID of the registration.
[]created_at: string
The RFC3339 timestamp when the registration was created.
[]device:  { id, name, client_version }
Device details embedded inside of a registration.
id: string
The ID of the device.
[]name: string
The name of the device.
[]client_version: optional string
Version of the WARP client.
[][]key: string
The public key used to connect to the Cloudflare network.
[]last_seen_at: string
The RFC3339 timestamp when the registration was last seen.
[]updated_at: string
The RFC3339 timestamp when the registration was last updated.
[]deleted_at: optional string
The RFC3339 timestamp when the registration was deleted.
[]key_type: optional string
The type of encryption key used by the WARP client for the active key. Currently ‘curve25519’ for WireGuard and ‘secp256r1’ for MASQUE.
[]policy: optional  { id, default, deleted, 2 more }
The device settings profile assigned to this registration.
id: string
The ID of the device settings profile.
[]default: boolean
Whether the device settings profile is the default profile for the account.
[]deleted: boolean
Whether the device settings profile was deleted.
[]name: string
The name of the device settings profile.
[]updated_at: string
The RFC3339 timestamp of when the device settings profile last changed for the registration.
[][]revoked_at: optional string
The RFC3339 timestamp when the registration was revoked.
[]tunnel_type: optional string
Type of the tunnel - wireguard or masque.
[]user: optional  { id, email, name } id: optional string
UUID.
maxLength36[]email: optional string
The contact email address of the user.
maxLength90[]name: optional string
The enrolled device user’s name.
[][][]RegistrationDeleteResponse = unknown[]RegistrationBulkDeleteResponse = unknown[]RegistrationRevokeResponse = unknown[]RegistrationUnrevokeResponse = unknown[]
#### DevicesDEX Tests

##### [List Device DEX tests]
GET/accounts/{account_id}/dex/devices/dex_tests
##### [Get Device DEX test]
GET/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Create Device DEX test]
POST/accounts/{account_id}/dex/devices/dex_tests
##### [Update Device DEX test]
PUT/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Delete Device DEX test]
DELETE/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### ModelsExpand Collapse
SchemaData  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: optional string
The desired endpoint to test.
[]kind: optional string
The type of test.
[]method: optional string
The HTTP request method type.
[][]SchemaHTTP  { data, enabled, interval, 5 more } data: [SchemaData] { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
[]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
Device settings profiles targeted by this test.
id: optional string
The id of the device settings profile.
[]default: optional boolean
Whether the profile is the account default.
[]name: optional string
The name of the device settings profile.
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestListResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestGetResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestCreateResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestUpdateResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestDeleteResponse  { dex_tests } dex_tests: optional array of  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][][]
#### DevicesIP Profiles

##### [List IP profiles]
GET/accounts/{account_id}/devices/ip-profiles
##### [Get IP profile]
GET/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Create IP profile]
POST/accounts/{account_id}/devices/ip-profiles
##### [Update IP profile]
PATCH/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Delete IP profile]
DELETE/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### ModelsExpand Collapse
IPProfile  { id, created_at, description, 6 more } id: string
The ID of the Device IP profile.
[]created_at: string
The RFC3339Nano timestamp when the Device IP profile was created.
[]description: string
An optional description of the Device IP profile.
[]enabled: boolean
Whether the Device IP profile is enabled.
[]match: string
The wirefilter expression to match registrations. Available values: “identity.name”, “identity.email”, “identity.groups.id”, “identity.groups.name”, “identity.groups.email”, “identity.saml_attributes”.
maxLength10000[]name: string
A user-friendly name for the Device IP profile.
[]precedence: number
The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.
[]subnet_id: string
The ID of the Subnet.
[]updated_at: string
The RFC3339Nano timestamp when the Device IP profile was last updated.
[][]IPProfileDeleteResponse  { id } id: optional string
ID of the deleted Device IP profile.
[][]
#### DevicesNetworks

##### [List your device managed networks]
GET/accounts/{account_id}/devices/networks
##### [Get device managed network details]
GET/accounts/{account_id}/devices/networks/{network_id}
##### [Create a device managed network]
POST/accounts/{account_id}/devices/networks
##### [Update a device managed network]
PUT/accounts/{account_id}/devices/networks/{network_id}
##### [Delete a device managed network]
DELETE/accounts/{account_id}/devices/networks/{network_id}
##### ModelsExpand Collapse
DeviceNetwork  { config, name, network_id, type } config: optional  { tls_sockaddr, sha256 }
The configuration object containing information for the WARP client to detect the managed network.
tls_sockaddr: string
A network address of the form “host:port” that the WARP client will use to detect the presence of a TLS host.
[]sha256: optional string
The SHA-256 hash of the TLS certificate presented by the host found at tls_sockaddr. If absent, regular certificate verification (trusted roots, valid timestamp, etc) will be used to validate the certificate.
[][]name: optional string
The name of the device managed network. This name must be unique.
[]network_id: optional string
API UUID.
maxLength36[]type: optional "tls"
The type of device managed network.
[][]
#### DevicesFleet Status

##### [Get the live status of a latest device]
GET/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live
##### ModelsExpand Collapse
FleetStatusGetResponse  { colo, deviceId, mode, 35 more } colo: string
Cloudflare colo
[]deviceId: string
Device identifier (UUID v4)
[]mode: string
The mode under which the WARP client is run
[]platform: string
Operating system
[]status: string
Network status
[]timestamp: string
Timestamp in ISO format
[]version: string
WARP client version
[]alwaysOn: optional boolean[]batteryCharging: optional boolean[]batteryCycles: optional numberformatint64[]batteryPct: optional numberformatfloat[]connectionType: optional string[]cpuPct: optional numberformatfloat[]cpuPctByApp: optional array of array of  { cpu_pct, name } cpu_pct: optional numberformatfloat[]name: optional string[][]deviceIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]deviceIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]deviceName: optional string
Device identifier (human readable)
[]diskReadBps: optional numberformatint64[]diskUsagePct: optional numberformatfloat[]diskWriteBps: optional numberformatint64[]dohSubdomain: optional string[]estimatedLossPct: optional numberformatfloat[]firewallEnabled: optional boolean[]gatewayIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]gatewayIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]handshakeLatencyMs: optional numberformatint64[]ispIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]ispIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]metal: optional string[]networkRcvdBps: optional numberformatint64[]networkSentBps: optional numberformatint64[]networkSsid: optional string[]personEmail: optional string
User contact email address
[]ramAvailableKb: optional numberformatint64[]ramUsedPct: optional numberformatfloat[]ramUsedPctByApp: optional array of array of  { name, ram_used_pct } name: optional string[]ram_used_pct: optional numberformatfloat[][]switchLocked: optional boolean[]wifiStrengthDbm: optional numberformatint64[][]
#### DevicesPolicies

##### ModelsExpand Collapse
DevicePolicyCertificates  { enabled } enabled: boolean
The current status of the device policy certificate provisioning feature for WARP clients.
[][]FallbackDomain  { suffix, description, dns_server } suffix: string
The domain suffix to match when resolving locally.
[]description: optional string
A description of the fallback domain, displayed in the client UI.
maxLength100[]dns_server: optional array of string
A list of IP addresses to handle domain resolution.
[][]FallbackDomainPolicy = array of [FallbackDomain] { suffix, description, dns_server } suffix: string
The domain suffix to match when resolving locally.
[]description: optional string
A description of the fallback domain, displayed in the client UI.
maxLength100[]dns_server: optional array of string
A list of IP addresses to handle domain resolution.
[][]SettingsPolicy  { allow_mode_switch, allow_updates, allowed_to_leave, 24 more } allow_mode_switch: optional boolean
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
Whether the policy is the default policy for an account.
[]description: optional string
A description of the policy.
maxLength500[]disable_auto_fallback: optional boolean
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
maxLength100[][][]lan_allow_minutes: optional number
The amount of time in minutes a user is allowed access to their LAN. A value of 0 will allow LAN access until the next WARP reconnection, such as a reboot or a laptop waking from sleep. Note that this field is omitted from the response if null or unset.
[]lan_allow_subnet_size: optional number
The size of the subnet for the local access network. Note that this field is omitted from the response if null or unset.
[]match: optional string
The wirefilter expression to match devices. Available values: “identity.email”, “identity.groups.id”, “identity.groups.name”, “identity.groups.email”, “identity.service_token_uuid”, “identity.saml_attributes”, “network”, “os.name”, “os.version”.
maxLength500[]name: optional string
The name of the device settings profile.
maxLength100[]policy_id: optional stringmaxLength36[]precedence: optional number
The precedence of the policy. Lower values indicate higher precedence. Policies will be evaluated in ascending order of this field.
[]register_interface_ip_with_dns: optional boolean
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
[]target_tests: optional array of  { id, name } id: optional string
The id of the DEX test targeting this policy.
[]name: optional string
The name of the DEX test targeting this policy.
[][]tunnel_protocol: optional string
Determines which tunnel protocol to use.
[][]SplitTunnelExclude =  { address, description }  or  { host, description } One of the following:TeamsDevicesExcludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to exclude from the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesExcludeSplitTunnelWithHost  { host, description } host: string
The domain name to exclude from the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]SplitTunnelInclude =  { address, description }  or  { host, description } One of the following:TeamsDevicesIncludeSplitTunnelWithAddress  { address, description } address: string
The address in CIDR format to include in the tunnel. If `address` is present, `host` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][]TeamsDevicesIncludeSplitTunnelWithHost  { host, description } host: string
The domain name to include in the tunnel. If `host` is present, `address` must not be present.
[]description: optional string
A description of the Split Tunnel item, displayed in the client UI.
maxLength100[][][]
#### DevicesPoliciesDefault

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
#### DevicesPoliciesDefaultExcludes

##### [Get the Split Tunnel exclude list]
GET/accounts/{account_id}/devices/policy/exclude
##### [Set the Split Tunnel exclude list]
PUT/accounts/{account_id}/devices/policy/exclude
#### DevicesPoliciesDefaultIncludes

##### [Get the Split Tunnel include list]
GET/accounts/{account_id}/devices/policy/include
##### [Set the Split Tunnel include list]
PUT/accounts/{account_id}/devices/policy/include
#### DevicesPoliciesDefaultFallback Domains

##### [Get your Local Domain Fallback list]
GET/accounts/{account_id}/devices/policy/fallback_domains
##### [Set your Local Domain Fallback list]
PUT/accounts/{account_id}/devices/policy/fallback_domains
#### DevicesPoliciesDefaultCertificates

##### [Get device certificate provisioning status]
GET/zones/{zone_id}/devices/policy/certificates
##### [Update device certificate provisioning status]
PATCH/zones/{zone_id}/devices/policy/certificates
#### DevicesPoliciesCustom

##### [List device settings profiles]
GET/accounts/{account_id}/devices/policies
##### [Get device settings profile by ID]
GET/accounts/{account_id}/devices/policy/{policy_id}
##### [Create a device settings profile]
POST/accounts/{account_id}/devices/policy
##### [Update a device settings profile]
PATCH/accounts/{account_id}/devices/policy/{policy_id}
##### [Delete a device settings profile]
DELETE/accounts/{account_id}/devices/policy/{policy_id}
#### DevicesPoliciesCustomExcludes

##### [Get the Split Tunnel exclude list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/exclude
##### [Set the Split Tunnel exclude list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/exclude
#### DevicesPoliciesCustomIncludes

##### [Get the Split Tunnel include list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/include
##### [Set the Split Tunnel include list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/include
#### DevicesPoliciesCustomFallback Domains

##### [Get the Local Domain Fallback list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains
##### [Set the Local Domain Fallback list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains
#### DevicesPosture

##### [List device posture rules]
GET/accounts/{account_id}/devices/posture
##### [Get device posture rule details]
GET/accounts/{account_id}/devices/posture/{rule_id}
##### [Create a device posture rule]
POST/accounts/{account_id}/devices/posture
##### [Update a device posture rule]
PUT/accounts/{account_id}/devices/posture/{rule_id}
##### [Delete a device posture rule]
DELETE/accounts/{account_id}/devices/posture/{rule_id}
##### ModelsExpand Collapse
CarbonblackInput = string[]ClientCertificateInput  { certificate_id, cn } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]cn: string
Common Name that is protected by the certificate.
[][]CrowdstrikeInput  { connection_id, last_seen, operator, 6 more } connection_id: string
Posture Integration ID.
[]last_seen: optional string
For more details on last seen, please refer to the Crowdstrike documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]os: optional string
Os Version.
[]overall: optional string
Overall.
[]sensor_config: optional string
SensorConfig.
[]state: optional "online" or "offline" or "unknown"
For more details on state, please refer to the Crowdstrike documentation.
One of the following:"online"[]"offline"[]"unknown"[][]version: optional string
Version.
[]versionOperator: optional "<" or "<=" or ">" or 2 more
Version Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]DeviceInput = [FileInput] { operating_system, path, exists, 2 more }  or [UniqueClientIDInput] { id, operating_system }  or [DomainJoinedInput] { operating_system, domain }  or 17 more
The value to be checked against.
One of the following:FileInput  { operating_system, path, exists, 2 more } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]exists: optional boolean
Whether or not file exists.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]UniqueClientIDInput  { id, operating_system } id: string
List ID.
[]operating_system: "android" or "ios" or "chromeos"
Operating System.
One of the following:"android"[]"ios"[]"chromeos"[][][]DomainJoinedInput  { operating_system, domain } operating_system: "windows"
Operating System.
[]domain: optional string
Domain.
[][]OSVersionInput  { operating_system, operator, version, 3 more } operating_system: "windows"
Operating System.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]version: string
Version of OS.
[]os_distro_name: optional string
Operating System Distribution Name (linux only).
[]os_distro_revision: optional string
Version of OS Distribution (linux only).
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[][]FirewallInput  { enabled, operating_system } enabled: boolean
Enabled.
[]operating_system: "windows" or "mac"
Operating System.
One of the following:"windows"[]"mac"[][][]SentineloneInput  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]TeamsDevicesCarbonblackInputRequest  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]TeamsDevicesAccessSerialNumberListInputRequest  { id } id: string
UUID of Access List.
maxLength36[][]DiskEncryptionInput  { checkDisks, requireAll } checkDisks: optional array of [CarbonblackInput]
List of volume names to be checked for encryption.
[]requireAll: optional boolean
Whether to check all disks for encryption.
[][]TeamsDevicesApplicationInputRequest  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
Path for the application.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]ClientCertificateInput  { certificate_id, cn } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]cn: string
Common Name that is protected by the certificate.
[][]TeamsDevicesClientCertificateV2InputRequest  { certificate_id, check_private_key, operating_system, 4 more } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]check_private_key: boolean
Confirm the certificate was not imported from another device. We recommend keeping this enabled unless the certificate was deployed without a private key.
[]operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]cn: optional string
Certificate Common Name. This may include one or more variables in the ${ } notation. Only ${serial_number} and ${hostname} are valid variables.
[]extended_key_usage: optional array of "clientAuth" or "emailProtection"
List of values indicating purposes for which the certificate public key can be used.
One of the following:"clientAuth"[]"emailProtection"[][]locations: optional  { paths, trust_stores } paths: optional array of string
List of paths to check for client certificate on linux.
[]trust_stores: optional array of "system" or "user"
List of trust stores to check for client certificate.
One of the following:"system"[]"user"[][][]subject_alternative_names: optional array of string
List of certificate Subject Alternative Names.
[][]TeamsDevicesAntivirusInputRequest  { update_window_days } update_window_days: optional number
Number of days that the antivirus should be updated within.
[][]WorkspaceOneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown"
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[][]connection_id: string
Posture Integration ID.
[][]CrowdstrikeInput  { connection_id, last_seen, operator, 6 more } connection_id: string
Posture Integration ID.
[]last_seen: optional string
For more details on last seen, please refer to the Crowdstrike documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]os: optional string
Os Version.
[]overall: optional string
Overall.
[]sensor_config: optional string
SensorConfig.
[]state: optional "online" or "offline" or "unknown"
For more details on state, please refer to the Crowdstrike documentation.
One of the following:"online"[]"offline"[]"unknown"[][]version: optional string
Version.
[]versionOperator: optional "<" or "<=" or ">" or 2 more
Version Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]IntuneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown" or 3 more
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[]"notapplicable"[]"ingraceperiod"[]"error"[][]connection_id: string
Posture Integration ID.
[][]KolideInput  { connection_id, countOperator, issue_count } connection_id: string
Posture Integration ID.
[]countOperator: "<" or "<=" or ">" or 2 more
Count Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]issue_count: string
The Number of Issues.
[][]TaniumInput  { connection_id, eid_last_seen, operator, 3 more } connection_id: string
Posture Integration ID.
[]eid_last_seen: optional string
For more details on eid last seen, refer to the Tanium documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator to evaluate risk_level or eid_last_seen.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]risk_level: optional "low" or "medium" or "high" or "critical"
For more details on risk level, refer to the Tanium documentation.
One of the following:"low"[]"medium"[]"high"[]"critical"[][]scoreOperator: optional "<" or "<=" or ">" or 2 more
Score Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]total_score: optional number
For more details on total score, refer to the Tanium documentation.
[][]SentineloneS2sInput  { connection_id, active_threats, infected, 4 more } connection_id: string
Posture Integration ID.
[]active_threats: optional number
The Number of active threats.
[]infected: optional boolean
Whether device is infected.
[]is_active: optional boolean
Whether device is active.
[]network_status: optional "connected" or "disconnected" or "disconnecting" or "connecting"
Network status of device.
One of the following:"connected"[]"disconnected"[]"disconnecting"[]"connecting"[][]operational_state: optional "na" or "partially_disabled" or "auto_fully_disabled" or 4 more
Agent operational state.
One of the following:"na"[]"partially_disabled"[]"auto_fully_disabled"[]"fully_disabled"[]"auto_partially_disabled"[]"disabled_error"[]"db_corruption"[][]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]TeamsDevicesCustomS2sInputRequest  { connection_id, operator, score } connection_id: string
Posture Integration ID.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]score: number
A value between 0-100 assigned to devices set by the 3rd party posture provider.
[][][]DeviceMatch  { platform } platform: optional "windows" or "mac" or "linux" or 3 moreOne of the following:"windows"[]"mac"[]"linux"[]"android"[]"ios"[]"chromeos"[][][]DevicePostureRule  { id, description, expiration, 5 more } id: optional string
API UUID.
maxLength36[]description: optional string
The description of the device posture rule.
[]expiration: optional string
Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client.
[]input: optional [DeviceInput]
The value to be checked against.
[]match: optional array of [DeviceMatch] { platform }
The conditions that the client must match to run the rule.
platform: optional "windows" or "mac" or "linux" or 3 moreOne of the following:"windows"[]"mac"[]"linux"[]"android"[]"ios"[]"chromeos"[][][]name: optional string
The name of the device posture rule.
[]schedule: optional string
Polling frequency for the WARP client posture check. Default: `5m` (poll every five minutes). Minimum: `1m`.
[]type: optional "file" or "application" or "tanium" or 20 more
The type of device posture rule.
One of the following:"file"[]"application"[]"tanium"[]"gateway"[]"warp"[]"disk_encryption"[]"serial_number"[]"sentinelone"[]"carbonblack"[]"firewall"[]"os_version"[]"domain_joined"[]"client_certificate"[]"client_certificate_v2"[]"antivirus"[]"unique_client_id"[]"kolide"[]"tanium_s2s"[]"crowdstrike_s2s"[]"intune"[]"workspace_one"[]"sentinelone_s2s"[]"custom_s2s"[][][]DiskEncryptionInput  { checkDisks, requireAll } checkDisks: optional array of [CarbonblackInput]
List of volume names to be checked for encryption.
[]requireAll: optional boolean
Whether to check all disks for encryption.
[][]DomainJoinedInput  { operating_system, domain } operating_system: "windows"
Operating System.
[]domain: optional string
Domain.
[][]FileInput  { operating_system, path, exists, 2 more } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]exists: optional boolean
Whether or not file exists.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]FirewallInput  { enabled, operating_system } enabled: boolean
Enabled.
[]operating_system: "windows" or "mac"
Operating System.
One of the following:"windows"[]"mac"[][][]IntuneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown" or 3 more
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[]"notapplicable"[]"ingraceperiod"[]"error"[][]connection_id: string
Posture Integration ID.
[][]KolideInput  { connection_id, countOperator, issue_count } connection_id: string
Posture Integration ID.
[]countOperator: "<" or "<=" or ">" or 2 more
Count Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]issue_count: string
The Number of Issues.
[][]OSVersionInput  { operating_system, operator, version, 3 more } operating_system: "windows"
Operating System.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]version: string
Version of OS.
[]os_distro_name: optional string
Operating System Distribution Name (linux only).
[]os_distro_revision: optional string
Version of OS Distribution (linux only).
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[][]SentineloneInput  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]SentineloneS2sInput  { connection_id, active_threats, infected, 4 more } connection_id: string
Posture Integration ID.
[]active_threats: optional number
The Number of active threats.
[]infected: optional boolean
Whether device is infected.
[]is_active: optional boolean
Whether device is active.
[]network_status: optional "connected" or "disconnected" or "disconnecting" or "connecting"
Network status of device.
One of the following:"connected"[]"disconnected"[]"disconnecting"[]"connecting"[][]operational_state: optional "na" or "partially_disabled" or "auto_fully_disabled" or 4 more
Agent operational state.
One of the following:"na"[]"partially_disabled"[]"auto_fully_disabled"[]"fully_disabled"[]"auto_partially_disabled"[]"disabled_error"[]"db_corruption"[][]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]TaniumInput  { connection_id, eid_last_seen, operator, 3 more } connection_id: string
Posture Integration ID.
[]eid_last_seen: optional string
For more details on eid last seen, refer to the Tanium documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator to evaluate risk_level or eid_last_seen.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]risk_level: optional "low" or "medium" or "high" or "critical"
For more details on risk level, refer to the Tanium documentation.
One of the following:"low"[]"medium"[]"high"[]"critical"[][]scoreOperator: optional "<" or "<=" or ">" or 2 more
Score Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]total_score: optional number
For more details on total score, refer to the Tanium documentation.
[][]UniqueClientIDInput  { id, operating_system } id: string
List ID.
[]operating_system: "android" or "ios" or "chromeos"
Operating System.
One of the following:"android"[]"ios"[]"chromeos"[][][]WorkspaceOneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown"
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[][]connection_id: string
Posture Integration ID.
[][]PostureDeleteResponse  { id } id: optional string
API UUID.
maxLength36[][]
#### DevicesPostureIntegrations

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
#### DevicesRevoke

##### [Revoke devices (deprecated)]
DeprecatedPOST/accounts/{account_id}/devices/revoke
##### ModelsExpand Collapse
RevokeCreateResponse = unknown or stringOne of the following:unknown[]string[][]
#### DevicesSettings

##### [Get device settings for a Zero Trust account]
GET/accounts/{account_id}/devices/settings
##### [Update device settings for a Zero Trust account]
PUT/accounts/{account_id}/devices/settings
##### [Patch device settings for a Zero Trust account]
PATCH/accounts/{account_id}/devices/settings
##### [Reset device settings for a Zero Trust account with defaults. This turns off all proxying.]
DELETE/accounts/{account_id}/devices/settings
##### ModelsExpand Collapse
DeviceSettings  { disable_for_time, external_emergency_signal_enabled, external_emergency_signal_fingerprint, 6 more } disable_for_time: optional number
Sets the time limit, in seconds, that a user can use an override code to bypass WARP.
[]external_emergency_signal_enabled: optional boolean
Controls whether the external emergency disconnect feature is enabled.
[]external_emergency_signal_fingerprint: optional string
The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server certificate for the external_emergency_signal_url. If provided, the WARP client will use this value to verify the server’s identity. The device will ignore any response if the server’s certificate fingerprint does not exactly match this value.
[]external_emergency_signal_interval: optional string
The interval at which the WARP client fetches the emergency disconnect signal, formatted as a duration string (e.g., “5m”, “2m30s”, “1h”). Minimum 30 seconds.
[]external_emergency_signal_url: optional string
The HTTPS URL from which to fetch the emergency disconnect signal. Must use HTTPS and have an IPv4 or IPv6 address as the host.
[]gateway_proxy_enabled: optional boolean
Enable gateway proxy filtering on TCP.
[]gateway_udp_proxy_enabled: optional boolean
Enable gateway proxy filtering on UDP.
[]root_certificate_installation_enabled: optional boolean
Enable installation of cloudflare managed root certificate.
[]use_zt_virtual_ip: optional boolean
Enable using CGNAT virtual IPv4.
[][]
#### DevicesUnrevoke

##### [Unrevoke devices (deprecated)]
DeprecatedPOST/accounts/{account_id}/devices/unrevoke
##### ModelsExpand Collapse
UnrevokeCreateResponse = unknown or stringOne of the following:unknown[]string[][]
#### DevicesOverride Codes

##### [Get override codes (deprecated)
]
DeprecatedGET/accounts/{account_id}/devices/{device_id}/override_codes
##### [Get override codes]
GET/accounts/{account_id}/devices/registrations/{registration_id}/override_codes
##### ModelsExpand Collapse
OverrideCodeListResponse = unknown[]OverrideCodeGetResponse  { disable_for_time } disable_for_time: optional map[string][][]