# Networks | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks

[API Reference][Zero Trust][Devices]
# Networks

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