# Certificate Authorities | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/certificate_authorities

[API Reference]
# Certificate Authorities

#### Certificate AuthoritiesHostname Associations

##### [List Hostname Associations]
GET/zones/{zone_id}/certificate_authorities/hostname_associations
##### [Replace Hostname Associations]
PUT/zones/{zone_id}/certificate_authorities/hostname_associations
##### ModelsExpand Collapse
HostnameAssociation = string[]TLSHostnameAssociation  { hostnames, mtls_certificate_id } hostnames: optional array of [HostnameAssociation][]mtls_certificate_id: optional string
The UUID for a certificate that was uploaded to the mTLS Certificate Management endpoint. If no mtls_certificate_id is given, the hostnames will be associated to your active Cloudflare Managed CA.
maxLength36minLength36[][]HostnameAssociationGetResponse  { hostnames } hostnames: optional array of [HostnameAssociation][][]HostnameAssociationUpdateResponse  { hostnames } hostnames: optional array of [HostnameAssociation][][]