# Origin Post Quantum Encryption | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_post_quantum_encryption

[API Reference]
# Origin Post Quantum Encryption

##### [Get Origin Post-Quantum Encryption setting]
GET/zones/{zone_id}/cache/origin_post_quantum_encryption
##### [Change Origin Post-Quantum Encryption setting]
PUT/zones/{zone_id}/cache/origin_post_quantum_encryption
##### ModelsExpand Collapse
OriginPostQuantumEncryptionGetResponse  { id, editable, value, modified_on } id: "origin_pqe"
The identifier of the caching setting.
[]editable: boolean
Whether the setting is editable.
[]value: "preferred" or "supported" or "off"
Value of the Origin Post Quantum Encryption Setting.
One of the following:"preferred"[]"supported"[]"off"[][]modified_on: optional string
Last time this setting was modified.
formatdate-time[][]OriginPostQuantumEncryptionUpdateResponse  { id, editable, value, modified_on } id: "origin_pqe"
The identifier of the caching setting.
[]editable: boolean
Whether the setting is editable.
[]value: "preferred" or "supported" or "off"
Value of the Origin Post Quantum Encryption Setting.
One of the following:"preferred"[]"supported"[]"off"[][]modified_on: optional string
Last time this setting was modified.
formatdate-time[][]