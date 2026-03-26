# Source: https://www.zuplo.com/docs/policies/stripe-webhook-verification-inbound.md

# Stripe Webhook Auth Policy

The Stripe Webhook policy secures your incoming webhooks by validating that the
request was sent by Stripe.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-stripe-webhook-verification-inbound-policy",
  "policyType": "stripe-webhook-verification-inbound",
  "handler": {
    "export": "StripeWebhookVerificationInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "tolerance": 300
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `stripe-webhook-verification-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `StripeWebhookVerificationInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `signingSecret` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The signing secret for the webhook.
- `tolerance` <code className="text-green-600">&lt;number&gt;</code> - The allowed clock skew in seconds between the time the webhook signature was crated and the current time. Defaults to `300`.

## Using the Policy

Read more about [how policies work](/articles/policies)
