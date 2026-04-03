# Custom | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom

[API Reference][Zero Trust][Devices][Policies]
# Custom

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
#### CustomExcludes

##### [Get the Split Tunnel exclude list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/exclude
##### [Set the Split Tunnel exclude list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/exclude
#### CustomIncludes

##### [Get the Split Tunnel include list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/include
##### [Set the Split Tunnel include list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/include
#### CustomFallback Domains

##### [Get the Local Domain Fallback list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains
##### [Set the Local Domain Fallback list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains