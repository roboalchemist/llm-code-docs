# Quota | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/subresources/quota

[API Reference][SSL][Certificate Packs]
# Quota

##### [Get Certificate Pack Quotas]
GET/zones/{zone_id}/ssl/certificate_packs/quota
##### ModelsExpand Collapse
QuotaGetResponse  { advanced } advanced: optional  { allocated, used } allocated: optional number
Quantity Allocated.
[]used: optional number
Quantity Used.
[][][]