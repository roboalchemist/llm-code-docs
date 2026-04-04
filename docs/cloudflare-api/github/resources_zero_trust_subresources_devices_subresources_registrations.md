# Registrations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations

[API Reference][Zero Trust][Devices]
# Registrations

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