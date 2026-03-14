# Source: https://docs.verba.ink/guides/credits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Credits and billing

> Understand how credits work and plan usage.

## Credits in plain language

Credits are used for text, image, and voice generation. Bigger models, longer
outputs, and search-enabled workflows typically consume more.

## Plan-aware limits that affect credit usage

| Plan  | Monthly included allowance | Max context | Max tokens |
| ----- | -------------------------- | ----------- | ---------- |
| Free  | `0`                        | `50`        | `4096`     |
| Plus  | `2.5`                      | `75`        | `8192`     |
| Pro   | `5`                        | `100`       | `16384`    |
| Ultra | `10`                       | `150`       | `32768`    |

<Note>
  Included monthly allowance comes from your active tier. You can still top up
  credits separately.
</Note>

## Usage strategy

* Keep web search off for stable topics.
* Use smaller context for routine support replies.
* Reserve larger token limits for long-form answers.
* Use deterministic settings for troubleshooting to reduce retries.

## Common billing questions

<AccordionGroup>
  <Accordion title="Why did usage spike?">
    Typical causes are higher context, longer max tokens, web search, or a more expensive model selection.
  </Accordion>

  <Accordion title="Why does a model disappear?">
    Model access is tier-based. If tier or mapping changed, unavailable models are removed or remapped.
  </Accordion>

  <Accordion title="Do I lose access if Patreon is disconnected?">
    Active premium subscriptions can block Patreon disconnect until status is consistent.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="Billing" icon="credit-card" href="https://verba.ink/billing">
    Buy credits and review purchase history.
  </Card>

  <Card title="Pricing" icon="tag" href="https://verba.ink/pricing">
    Compare plans and pricing.
  </Card>
</CardGroup>

<Info>
  If a model is unavailable, your current tier may not include it.
</Info>

<Card title="Billing and refunds" icon="receipt" href="/guides/billing-and-refunds">
  What to do if something looks off.
</Card>

<Card title="Plans and limits" icon="gauge" href="/guides/plans-and-limits">
  Full premium matrix: verbs, limits, streaming, and allowances.
</Card>

Built with [Mintlify](https://mintlify.com).
