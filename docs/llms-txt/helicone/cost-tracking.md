# Source: https://docs.helicone.ai/guides/cookbooks/cost-tracking.md

# Cost Tracking & Optimization

> Monitor LLM spending, optimize costs, and understand unit economics across your AI application

Track and optimize your LLM costs across all providers. Helicone provides detailed cost analytics and optimization tools to help you manage your AI budget effectively.

## How We Calculate Costs

Helicone uses two systems for cost calculation depending on your integration method:

### AI Gateway (100% Accurate)

When using Helicone's AI Gateway, we have complete visibility into model usage and calculate costs precisely using our [Model Registry v2](https://helicone.ai/models) system.

### Best Effort (Without Gateway)

For direct provider integrations, we use our open-source cost repository with pricing for 300+ models. This provides best-effort cost estimates based on model detection and token counts.

<Note>
  **Cost not showing?** If your model costs aren't supported, [join our Discord](https://discord.com/invite/HwUbV3Q8qz) or email [help@helicone.ai](mailto:help@helicone.ai) and we'll add support quickly.
</Note>

## Understanding Unit Economics

The most critical aspect of cost tracking is understanding your unit economics - what drives costs in your application and how to optimize them.

<Frame caption="Session cost breakdown showing unit economics across different user interactions">
  <img src="https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=6d51b6313b5988e78d6f38f5033f8a81" alt="Helicone dashboard showing session-level cost breakdown with request counts and average costs per session type" data-og-width="3454" width="3454" data-og-height="1138" height="1138" data-path="images/sessions/session-metrics.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=280&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=dd5e5ceeafb9ef14c5af4f768532a965 280w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=560&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=d925d3ce970f75122615328f5541a131 560w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=840&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=45a9db2909f12463712b7a331fee335f 840w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=1100&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=ba15b6d92ead62378e581c4294caa7cf 1100w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=1650&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=dd9554f73ce11eced8edb6d51cbfec4d 1650w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/sessions/session-metrics.webp?w=2500&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=0e6324fd1a6ba41fe36447960e39ecbf 2500w" />
</Frame>

### Sessions: Your Cost Foundation

[Sessions](/features/sessions) group related requests to show the true cost of user interactions. Instead of seeing individual API calls, you see complete workflows:

```typescript  theme={null}
// Track a complete customer support interaction
const response = await client.chat.completions.create(
  { 
    model: "gpt-4o", 
    messages: [...] 
  },
  {
    headers: {
      "Helicone-Session-Id": "support-ticket-123",
      "Helicone-Session-Name": "Customer Support"
    }
  }
);
```

This reveals insights like:

* A support chat costs \$0.12 on average with 5 API calls
* Document analysis workflows cost \$0.45 with 12 API calls
* Quick queries cost \$0.02 with a single call

### Segmentation That Matters

Use [custom properties](/features/advanced-usage/custom-properties) to slice costs by the dimensions that matter to your business:

<Frame caption="Cost breakdown by user tier showing premium users generate 3x more value than cost">
  <img src="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ec8a7d26fee614033f2b382f5618fcef" alt="Dashboard showing cost segmentation by user tiers with ROI analysis" data-og-width="2564" width="2564" data-og-height="1366" height="1366" data-path="images/custom-properties/properties-page.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=280&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=68afec31a741ea76d8ef15258ac2088a 280w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=560&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=d8a09a1ee7b409d086d3fc5bac49f86f 560w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=840&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=ef162658bf9bd124ab61ee9c6d0ce2d2 840w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=1100&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=26330999b9c2425e4306be2acff41331 1100w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=1650&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=782b549eaa44c8dcfc9b0a689b9755b6 1650w, https://mintcdn.com/helicone/G4P7vGvFxEkwlqHM/images/custom-properties/properties-page.webp?w=2500&fit=max&auto=format&n=G4P7vGvFxEkwlqHM&q=85&s=f92b78ed98859e35cee6a84ff5a2508e 2500w" />
</Frame>

```typescript  theme={null}
headers: {
  "Helicone-Property-UserTier": "premium",
  "Helicone-Property-Feature": "document-analysis",
  "Helicone-Property-Environment": "production"
}
```

Now you can answer questions like:

* Do premium users justify their higher usage costs?
* Which features are cost-efficient vs. cost-intensive?
* How much are we spending on development vs. production?

## AI Gateway Cost Optimization

The [AI Gateway](/gateway/overview) doesn't just track costs - it actively optimizes them through intelligent routing.

### Automatic Model Selection

The [Model Registry](https://helicone.ai/models) shows all supported models with real-time pricing across providers. The AI Gateway automatically sorts by cost to find the cheapest option:

<Frame caption="Model Registry showing price comparison across providers">
  <img src="https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=8a6c4679725ba09df63121df10be2de7" alt="Helicone Model Registry interface showing models sorted by price across different providers" data-og-width="2302" width="2302" data-og-height="908" height="908" data-path="images/model-selection.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=280&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=3367c2307c621c0a17ce661248ae2b37 280w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=560&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=4ab9db26db48dada785b07962ff863ab 560w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=840&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=a227e4abff0ed55a81c4f828915ddbbe 840w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=1100&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=c5fb6d8e557873112830f3f59ecb5536 1100w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=1650&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=0ad77f7d19fa071e8a751fb1e5f3ed0d 1650w, https://mintcdn.com/helicone/K0iTieGnNg2WsNq1/images/model-selection.webp?w=2500&fit=max&auto=format&n=K0iTieGnNg2WsNq1&q=85&s=2ebe0feed4469cfcf43811f4f21eb846 2500w" />
</Frame>

### How Automatic Optimization Works

1. **[BYOK Priority](/gateway/provider-routing#option-2-your-own-keys-byok)** - Uses your existing credits first (AWS, Azure, etc.)
2. **[Cost-Based Routing](/gateway/provider-routing#smart-routing-algorithm)** - Automatically selects the cheapest available provider
3. **[Smart Fallbacks](/gateway/provider-routing#failover-triggers)** - If one provider fails, routes to the next cheapest option

```typescript  theme={null}
// One request, multiple potential providers
await gateway.chat.completions.create({
  model: "claude-3.5-sonnet",
  messages: [...]
});

// Gateway automatically routes to cheapest available:
// 1. Your AWS Bedrock key ($3/1M tokens)
// 2. Your Anthropic key ($3/1M tokens)
// 3. Next cheapest provider...
```

## Cost Prevention & Alerts

<Frame caption="Cost alert configuration with spending thresholds and real-time notifications">
  <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=a4fbd06770b64b9d0970caa0daa80616" alt="Alert configuration interface showing daily and monthly spending limits" data-og-width="2536" width="2536" data-og-height="1024" height="1024" data-path="images/alerts/alert-triggered.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=57fc921e8eb5dd84a16d95d5855889ba 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=a3bfd0859e9bbff27ce23abde2ba833f 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=c01fe0c492bb65a9191397cc72c5d169 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=76f96d49fdaa1ade5f7441bda8014d3c 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=85f784d9255c2a90ff8a4dfb012a3fe9 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/alerts/alert-triggered.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=051bad70f38653d842d7e6588901e045 2500w" />
</Frame>

### Setting Smart Alerts

Configure [cost alerts](/features/alerts) to catch spending issues before they become problems. Set graduated thresholds (50%, 80%, 95% of budget) and use different limits for development vs. production environments.

The key is understanding your baseline spending patterns and setting alerts that give you time to react without causing alert fatigue.

<Note>
  Cost alerts rely on accurate cost data. See [How We Calculate Costs](#how-we-calculate-costs) above. If you see "cost not supported" for your model, [contact us](https://discord.com/invite/HwUbV3Q8qz) to add support.
</Note>

### Caching for Cost Reduction

Enable [caching](/features/advanced-usage/caching) to eliminate redundant API calls entirely:

<Frame caption="Cache performance showing 73% hit rate saving $1,247 this month">
  <img src="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=1a3a46805f953e48ab3267917c455c83" alt="Dashboard showing cache hit rates and associated cost savings" data-og-width="1180" width="1180" data-og-height="772" height="772" data-path="images/caching.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=280&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=f24c59826a4ba96fefa38f7ba371ea1f 280w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=560&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=2f44055ab72d902657e4e38701146afb 560w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=840&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=dea6376f9dee9827848d5420bdf3bf9a 840w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=1100&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=b63ce405984fe3d3141b0cdb1bd763f6 1100w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=1650&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=971bcb02d30592e1a982cd211047de71 1650w, https://mintcdn.com/helicone/mei53w0pDEM5bxFI/images/caching.webp?w=2500&fit=max&auto=format&n=mei53w0pDEM5bxFI&q=85&s=dc1b8951709df03b24d8078dc3f9a91f 2500w" />
</Frame>

```typescript  theme={null}
headers: {
  "Helicone-Cache-Enabled": "true",
  "Cache-Control": "max-age=3600"  // 1 hour cache
}
```

Best caching opportunities:

* FAQ responses in support bots
* Static content generation
* Development and testing environments

## Automated Reports

Get regular cost summaries delivered to your inbox or Slack channels. Reports provide insights into spending trends, model usage, and optimization opportunities.

### What Reports Include

* Weekly spending summaries and trends
* Model usage breakdown by cost
* Top cost drivers and expensive requests
* Week-over-week comparisons
* Optimization recommendations

### Setting Up Reports

Configure automated reports in **Settings → Reports** to receive them via:

* **Email** - Weekly digests to any email address
* **Slack** - Post to your team channels

<Note>
  Reports help you stay on top of costs without checking the dashboard daily. Perfect for finance teams and engineering managers tracking AI spend.
</Note>

## Next Steps

<CardGroup cols={2}>
  <Card title="Set Up Alerts" icon="bell" href="/features/alerts">
    Configure spending thresholds before they become problems
  </Card>

  <Card title="Enable Caching" icon="database" href="/features/advanced-usage/caching">
    Start saving immediately on repetitive requests
  </Card>

  <Card title="Configure Gateway" icon="route" href="/gateway/overview">
    Let automatic routing optimize your costs
  </Card>

  <Card title="Track Sessions" icon="layer-group" href="/features/sessions">
    Understand your true unit economics
  </Card>
</CardGroup>
