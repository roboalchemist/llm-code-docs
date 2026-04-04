# Source: https://documentation.mailgun.com/docs/inboxready/alerts-ir.md

# Alerts

This section describes our RESTful API for alert configuration for Mailgun Optimize.

## Events & Channel

Our alerting solution is centered around two concepts: Events and Channels.

Every configured alert consists of an event type / channel pair. This level of granularity allows alerting to be configured to your exact preference.

### Events

The occurrence of an event can be configured to trigger an alert.

The current list of events that you can chose to receive alerts for are:

- `ip_listed`: A monitored IP has been added to a blocklist.
- `ip_delisted`: A monitored IP has been removed from a blocklist.
- `validation_job`: A bulk email verification job has completed.
- `validation_preview`: A bulk email verification preview job has completed.
- `domain_listed`: A monitored domain has been added to a blocklist.
- `domain_delisted`: A monitored domain has been removed from a blocklist.


### Channels

A channel describes the delivery method for an alert. The current supported delivery channels include emails and webhooks.

## Webhooks

This section covers details around consuming Mailgun Optimize deliverability alerts via webhooks. If you are familiar with Mailgun Send webhooks, there is a lot of overlapping similarity, however, there are also a few minor nuances to account for.

Securing Webhooks

[HMAC](https://en.wikipedia.org/wiki/HMAC) is used to verified to integrity as well as the authenticity of received webhooks. To verify the origin of a webhook:

1. Encode the webhook's entire POST request body with the HMAC algorithm (using your webhook signing key and SHA256 digest mode)
2. Compare the resulting hexdigest to the signature provided in the POST request's `X-Sign` header.


Below is a Ruby code example for verifying a webhook signature:


```JSON
require"json"
require"openssl"
defverify(signing\_key,webhook\_payload,signature)
data=JSON.generate(webhook\_payload)
signature==OpenSSL::HMAC.hexdigest("SHA256",signing\_key,data)
end
```

*NOTE: If you're comsuming Mailgun webhooks, please note that your Mailgun webhook signing key differs from your Optimize alerts webhook signing key. Your Optimize alerts webhook signing key is available within the Optimize UI.*

## Webhook URL Validation

When adding or updating a webhook URL for alerts, we will ensure the endpoint is reachable by sending a GET request to the provided URL. If a 200 response is not returned from your endpoint, the request will be rejected and your alert setting will not be saved. We intentionally chose to send a GET request instead of a POST when validating URLs so that your webhook endpoint does not have to account for test requests.

Additionally, when a POST request is sent to your webhook URL, if a 2xx is not returned, we will attempt retries via an exponential backoff strategy for up to ~8 hours. If the max retry count is reached, the alert will be disabled and the related alert settings record's `disabled_at` field will be populated.