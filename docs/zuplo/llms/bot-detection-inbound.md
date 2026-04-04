# Source: https://www.zuplo.com/docs/policies/bot-detection-inbound.md

# Bot Detection Policy

The bot detection inbound policy provides a bot score for every request that can
be used to determine the likelihood the request came from a bot. The policy can
be configured to automatically block traffic with a set score or simply pass
along the score for you to respond in other policies or handlers.

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-bot-detection-inbound-policy",
  "policyType": "bot-detection-inbound",
  "handler": {
    "export": "BotDetectionInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "blockScoresBelow": 80
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `bot-detection-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `BotDetectionInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `blockScoresBelow` **(required)** <code className="text-green-600">&lt;number&gt;</code> - The threshold at which bots are automatically blocked.

## Using the Policy

Read more about [how policies work](/articles/policies)
