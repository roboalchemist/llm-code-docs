# Subscriptions | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/user/subresources/subscriptions

[API Reference][User]
# Subscriptions

##### [Get User Subscriptions]
GET/user/subscriptions
##### [Update User Subscription]
PUT/user/subscriptions/{identifier}
##### [Delete User Subscription]
DELETE/user/subscriptions/{identifier}
##### ModelsExpand Collapse
SubscriptionUpdateResponse = unknown or stringOne of the following:unknown[]string[][]SubscriptionDeleteResponse  { subscription_id } subscription_id: optional string
Subscription identifier tag.
maxLength32[][]