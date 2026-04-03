# Devices | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/devices

[API Reference][Zero Trust][Devices]
# Devices

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