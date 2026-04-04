# Source: https://docs.fireworks.ai/guides/quotas_usage/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits & Quotas

> Understand and manage your rate limits, spend limits and quotas

## Check your current limits

View your account's current quotas and limits:

```bash  theme={null}
firectl quota list
```

This shows your rate limits, GPU quotas, spend limits, and usage across serverless and on-demand deployments.

## Spending tiers

Your account tier determines the maximum budget you can set:

| Tier      | Criteria                                              | Max Monthly Budget |
| --------- | ----------------------------------------------------- | ------------------ |
| Tier 1    | [Valid payment method](https://fireworks.ai/billing)  | \$50               |
| Tier 2    | Spend or add \$50 in credits                          | \$500              |
| Tier 3    | Spend or add \$500 in credits                         | \$5,000            |
| Tier 4    | Spend or add \$5,000 in credits                       | \$50,000           |
| Unlimited | [Contact us](https://fireworks.ai/company/contact-us) | Unlimited          |

<Tip>
  Add prepaid credits to unlock a higher tier. For example, adding \$100 moves you from Tier 1 to Tier 2. Your new tier activates within minutes.
</Tip>

## Manage your quotas

### Budget control

Control your monthly spending with flexible budget limits. Set a limit that fits your needs and adjust it anytime.

### View and adjust your spend limit

Check your current spend limit:

```bash  theme={null}
firectl quota list
```

Set a custom monthly budget:

```bash  theme={null}
firectl quota update monthly-spend-usd --value <AMOUNT>
```

For example, to set a \$200 monthly budget:

```bash  theme={null}
firectl quota update monthly-spend-usd --value 200
```

### When you reach your budget

When you reach your spending limit, all API requests pause automatically across serverless inference, deployments, and fine-tuning. To resume, [add credits](https://fireworks.ai/billing) to increase your tier and set a higher budget.

### On-demand deployment quotas

On-demand deployments have GPU quotas instead of rate limits:

| GPU Type          | Default Quota |
| ----------------- | ------------- |
| Nvidia A100       | 16 GPUs       |
| Nvidia H100       | 16 GPUs       |
| Nvidia H200       | 16 GPUs       |
| Nvidia B200       | 16 GPUs       |
| GPU hours/month   | 2,000         |
| LoRAs (on-demand) | 100           |

<Tip>
  Need more GPUs? [Contact us](https://fireworks.ai/company/contact-us) to request a quota increase.
</Tip>

### Serverless rate limits

### Default limits

All accounts with a payment method get these limits:

| Limit                                       | Value                         |
| ------------------------------------------- | ----------------------------- |
| Requests per minute (RPM, spike arrest max) | Up to 6,000 (dynamic ceiling) |
| Audio min per minute, Whisper-v3-large      | 200                           |
| Audio min per minute, Whisper-v3-turbo      | 400                           |
| Concurrent connections, streaming speech    | 10                            |
| LoRAs (on-demand)                           | 100                           |

<Tip>
  Make sure to add a [payment method](https://fireworks.ai/billing) to access higher rate limits up to the 6,000 RPM spike arrest ceiling. Without a payment method, you're limited to 10 RPM. Your rate limits will increase automatically once the payment method is added.
</Tip>

<Tip>
  During periods of high load, RPM limit may be lower.
</Tip>

<Callout type="warning">
  **Spike arrest policy**: 6,000 RPM is the maximum ceiling under our spike arrest policy, not a guaranteed fixed rate. Your effective RPM limit adjusts dynamically based on sustained usage and system load, so short spikes may see a lower cap to protect other tenants.
</Callout>

### How rate limiting works

Dynamic rate limits support high RPM limits in a fair manner, while limiting spiky traffic from impacting other users:

* **Gradual scaling**: Your minimum limits increase as you sustain consistent high usage
* **Typical scale-up**: Traffic can typically double within an hour without issues
* **Burst handling**: Short traffic spikes are accommodated during autoscaling

**Monitoring your limits:**

* Check response headers to see your current limits and remaining capacity
* `x-ratelimit-limit-requests`: Your current minimum limit
* `x-ratelimit-remaining-requests`: Remaining capacity
* `x-ratelimit-over-limit: yes`: Your request was processed but you're near capacity

<Tip>
  For production workloads requiring consistent performance and higher limits, use [on-demand deployments](/guides/ondemand-deployments). They provide dedicated GPUs with no rate limits and SLA guarantees.
</Tip>

### Account recovery

If your account is suspended due to failed payment:

1. Go to [Billing → Invoices](https://fireworks.ai/billing)
2. Pay any outstanding invoices
3. Your account reactivates automatically within an hour

<Tip>
  Still suspended after resolving payment issues? Contact support via [Discord](https://discord.gg/fireworks-ai) or email [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
</Tip>
