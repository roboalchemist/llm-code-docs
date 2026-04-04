# Keyless Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/keyless_certificates

[API Reference]
# Keyless Certificates

##### [List Keyless SSL Configurations]
GET/zones/{zone_id}/keyless_certificates
##### [Get Keyless SSL Configuration]
GET/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
##### [Create Keyless SSL Configuration]
POST/zones/{zone_id}/keyless_certificates
##### [Edit Keyless SSL Configuration]
PATCH/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
##### [Delete Keyless SSL Configuration]
DELETE/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
##### ModelsExpand Collapse
KeylessCertificate  { id, created_on, enabled, 7 more } id: string
Keyless certificate identifier tag.
maxLength32[]created_on: string
When the Keyless SSL was created.
formatdate-time[]enabled: boolean
Whether or not the Keyless SSL is on or off.
[]host: string
The keyless SSL name.
formathostnamemaxLength253[]modified_on: string
When the Keyless SSL was last modified.
formatdate-time[]name: string
The keyless SSL name.
maxLength180[]permissions: array of string
Available permissions for the Keyless SSL for the current user requesting the item.
[]port: number
The keyless SSL port used to communicate between Cloudflare and the client’s Keyless SSL server.
maxLength65535[]status: "active" or "deleted"
Status of the Keyless SSL.
One of the following:"active"[]"deleted"[][]tunnel: optional [Tunnel] { private_ip, vnet_id }
Configuration for using Keyless SSL through a Cloudflare Tunnel
[][]Tunnel  { private_ip, vnet_id }
Configuration for using Keyless SSL through a Cloudflare Tunnel
private_ip: string
Private IP of the Key Server Host
[]vnet_id: string
Cloudflare Tunnel Virtual Network ID
[][]KeylessCertificateDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]