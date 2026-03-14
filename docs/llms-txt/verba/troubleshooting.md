# Source: https://docs.verba.ink/guides/troubleshooting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Fix common Verba issues fast with concrete checks and recovery steps.

## Fast triage checklist

1. Confirm you are logged into the correct account/workspace.
2. Hard refresh the page and retry once.
3. Check plan limits (context, tokens, credits, model availability).
4. Confirm your verb settings were actually saved.
5. Test with a minimal prompt in a clean chat/thread.

## Discord issues

<AccordionGroup>
  <Accordion title="Connection failed while linking Discord token">
    Verify token format, ensure the token is not already linked to another verb, and retry after a short delay if Discord is rate limiting requests.
  </Accordion>

  <Accordion title="The application did not respond">
    This usually means command timeout, missing channel permission, or a disabled slash command. Check command toggles and bot permissions in that server/channel.
  </Accordion>

  <Accordion title="Bot only responds sometimes">
    In servers, bot response depends on routing: mention, AI channel, or keyword match. If none of those apply, no response is expected.
  </Accordion>

  <Accordion title="Bot replies in wrong places or too often">
    Remove AI channels with `/remove-channel` and keep mention-only behavior in shared channels.
  </Accordion>

  <Accordion title="/reset fails in server but works in DM">
    Server reset requires admin/server-owner/bot-owner level permission. DM reset is user scoped.
  </Accordion>
</AccordionGroup>

## Response quality issues

<AccordionGroup>
  <Accordion title="Replies are too short">
    Increase max tokens and use a fuller reply style. Also check whether your current plan caps output lower than expected.
  </Accordion>

  <Accordion title="Replies are too generic">
    Tighten system instructions, add focused training examples, and lower temperature.
  </Accordion>

  <Accordion title="Bot forgets earlier messages">
    Increase model context (within plan cap) and avoid splitting related topics across many disconnected chats.
  </Accordion>

  <Accordion title="Bot misses known docs/knowledge">
    Add or refine knowledge entries, improve titles/categories, and verify entries are active. For URL imports, scrape again and clean the generated draft.
  </Accordion>

  <Accordion title="Web search feels noisy or irrelevant">
    Disable web search for stable topics. Keep it for fresh/live data only.
  </Accordion>
</AccordionGroup>

## Performance and timeout issues

<AccordionGroup>
  <Accordion title="Responses are slow">
    Reduce context, disable web search, and test a lighter model. Long prompts + web search + high max tokens significantly increase latency.
  </Accordion>

  <Accordion title="Intermittent provider failures">
    Retries/backoff are built into the call path, but upstream outages still happen. Retry shortly and keep fallback models available in your plan tier.
  </Accordion>

  <Accordion title="Image generation fails randomly">
    Provider capacity spikes can cause temporary errors. Retry with a shorter prompt and no reference image first.
  </Accordion>
</AccordionGroup>

## Account and billing issues

<AccordionGroup>
  <Accordion title="Insufficient credits error">
    Top up credits or switch to a lower-cost model. Credits are charged to the account tied to the request/verb owner depending on surface.
  </Accordion>

  <Accordion title="Model not selectable">
    Your plan may not include that model tier. Choose an available model or upgrade.
  </Accordion>

  <Accordion title="API key works in dashboard but fails in API calls">
    Check header format (`Authorization: Bearer vka_...` or `x-api-key`), key revocation status, and whether you exceeded active key limits.
  </Accordion>
</AccordionGroup>

## Chat and group issues

<AccordionGroup>
  <Accordion title="Message send blocked">
    Anti-spam protections can block mention floods and invisible-character abuse. Remove unusual hidden characters and retry.
  </Accordion>

  <Accordion title="Uploads fail">
    Ensure the file is an image and under limit for that surface (for chat message uploads, 5MB max).
  </Accordion>

  <Accordion title="Group invite problems">
    Verify invite code freshness and that owner has not regenerated it recently.
  </Accordion>
</AccordionGroup>

## When to contact support

Contact support with:

* Exact timestamp (with timezone)
* Verb ID/vanity URL
* Surface (`Discord`, `chat`, `API`)
* Error text + screenshot
* Repro steps from clean session

<CardGroup cols={2}>
  <Card title="Contact Support" icon="envelope" href="https://verba.ink/contact">
    Share reproducible steps and timestamps for fastest resolution.
  </Card>

  <Card title="Community" icon="users" href="https://discord.gg/verba">
    Ask in community channels for quick operational help.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
