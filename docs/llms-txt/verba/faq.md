# Source: https://docs.verba.ink/guides/faq.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ

> High-frequency questions across API, Discord, memory, billing, and account settings.

## Top support answers

* How does the API work: create API key -> call `POST /v1/response` with `character` + `messages` -> reuse `session_id`.
* Where to set system instructions: Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`, max `8000` chars).
* Plan limits: Free `50/4096`, Plus `75/8192`, Pro `100/16384`, Ultra `150/32768` (context/max tokens).
* Full tier matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.

## Product basics

<AccordionGroup>
  <Accordion title="Can I keep a verb private?">
    Yes. Private verbs are only accessible by the owner. Public verbs can be discovered and used by others.
  </Accordion>

  <Accordion title="Why do replies consume credits?">
    Credits cover model inference and processing. Longer context and larger outputs consume more.
  </Accordion>

  <Accordion title="Can I use Verba outside Discord?">
    Yes. Use the public API at `api.verba.ink` with your API key.
  </Accordion>

  <Accordion title="Do I need a paid plan to use the API?">
    API access is available on all plans. Limits and model availability vary by tier.
  </Accordion>
</AccordionGroup>

## Discord FAQ

<AccordionGroup>
  <Accordion title="Why does the bot not answer unless pinged?">
    In server channels, the bot replies when mentioned, when channel is marked AI-enabled, or when a training keyword rule triggers.
  </Accordion>

  <Accordion title="How do I make it answer without mention in one channel?">
    Use `/activate-channel` in that channel.
  </Accordion>

  <Accordion title="How do I stop auto replies in a channel?">
    Use `/remove-channel`.
  </Accordion>

  <Accordion title="Why does /reset fail in server?">
    Server reset requires admin/server-owner/bot-owner permission.
  </Accordion>
</AccordionGroup>

## Memory and knowledge FAQ

<AccordionGroup>
  <Accordion title="What is the difference between memory and knowledge?">
    Memory is compact persistent facts; knowledge entries are richer structured references/lore.
  </Accordion>

  <Accordion title="How many knowledge entries can one verb store?">
    Up to `50` entries.
  </Accordion>

  <Accordion title="Can Verba auto-save memory from chats?">
    Yes, with Auto Memory enabled and instructions configured.
  </Accordion>

  <Accordion title="Why is it not using my docs correctly?">
    Improve knowledge entry quality (clear title/category/content), reduce ambiguity, and add training examples for recurring question patterns.
  </Accordion>
</AccordionGroup>

## API FAQ

<AccordionGroup>
  <Accordion title="How does the API work?">
    Create an API key, call `POST /v1/response` for text (or `POST /v1/image` for images), and reuse `session_id` for follow-up context.
  </Accordion>

  <Accordion title="How do I authenticate API requests?">
    Use `Authorization: Bearer vka_...` or `x-api-key`.
  </Accordion>

  <Accordion title="How does session memory work in API calls?">
    Reuse `session_id` to preserve context for the same caller + character.
  </Accordion>

  <Accordion title="Can I stream responses?">
    Yes with `stream: true` on `/v1/response` (tier restrictions apply).
  </Accordion>

  <Accordion title="Can I pass system messages directly in /v1/response?">
    No. Character system/personality is applied automatically.
  </Accordion>

  <Accordion title="What are the main /v1/response limits?">
    Max `60` messages, max `4000` chars per message, max `20000` total chars, max `4` image URLs, and max `128` chars for `session_id`.
  </Accordion>

  <Accordion title="How many API keys can I keep active?">
    Up to `3` active API keys per account.
  </Accordion>
</AccordionGroup>

## Plans and premium FAQ

<AccordionGroup>
  <Accordion title="Which plans support streaming on /v1/response?">
    Streaming is available on Plus, Pro, and Ultra. Free plan streaming requests are rejected.
  </Accordion>

  <Accordion title="How many verbs can I create per plan?">
    Free: 5, Plus: 10, Pro: 20, Ultra: 40.
  </Accordion>

  <Accordion title="Do plans affect context and token limits?">
    Yes. Plan tier sets max model context and max response tokens.
  </Accordion>

  <Accordion title="Where can I see the full plan matrix?">
    See the Plans and limits guide for complete tier-by-tier details.
  </Accordion>
</AccordionGroup>

## Account and security FAQ

<AccordionGroup>
  <Accordion title="How many API keys can I keep active?">
    Up to `3` active keys per account by default.
  </Accordion>

  <Accordion title="How long is a magic-link login valid?">
    Magic links expire after `20` minutes.
  </Accordion>

  <Accordion title="Can I disable 2FA later?">
    Yes. You can disable it from settings after verification.
  </Accordion>

  <Accordion title="Can I disconnect Patreon anytime?">
    Not while an active paid Patreon subscription is still linked.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fix connection, timeout, and no-response issues.
  </Card>

  <Card title="Question Bank" icon="book-open" href="/guides/question-bank">
    Larger question-driven reference generated from backend/frontend behavior.
  </Card>
</CardGroup>

<Card title="Plans and limits" icon="gauge" href="/guides/plans-and-limits">
  Premium tiers, usage limits, streaming, and allowances.
</Card>

Built with [Mintlify](https://mintlify.com).
