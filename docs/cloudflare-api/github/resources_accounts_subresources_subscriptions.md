# Subscriptions | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions

[API Reference][Accounts]
# Subscriptions

##### [List Subscriptions]
GET/accounts/{account_id}/subscriptions
##### [Create Subscription]
POST/accounts/{account_id}/subscriptions
##### [Update Subscription]
PUT/accounts/{account_id}/subscriptions/{subscription_identifier}
##### [Delete Subscription]
DELETE/accounts/{account_id}/subscriptions/{subscription_identifier}
##### ModelsExpand Collapse
SubscriptionDeleteResponse  { subscription_id } subscription_id: optional string
Subscription identifier tag.
maxLength32[][]