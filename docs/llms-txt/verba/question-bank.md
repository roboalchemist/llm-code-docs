# Source: https://docs.verba.ink/guides/question-bank.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Question bank

> Large question-driven reference generated from backend routes and frontend settings flows.

## About this page

This page is a high-volume Q\&A index built from real product behavior in the
backend and frontend codepaths.

Use it when users ask operational questions and you need fast, practical
answers.

## Quick high-signal answers

* API flow: create API key -> call `POST /v1/response` -> reuse returned `session_id` for follow-ups.
* System instructions: set in Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`, max `8000` chars).
* `/v1/response` auth: `Authorization: Bearer vka_...` or `x-api-key: vka_...`.
* Session memory: reuse `session_id` for follow-up calls.
* Plan limits (context/tokens): Free `50/4096`, Plus `75/8192`, Pro `100/16384`, Ultra `150/32768`.
* Plan full matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.

## API questions

<AccordionGroup>
  <Accordion title="How does the API work?">
    Create an API key, call `POST /v1/response` with `character` + `messages`, then reuse the returned `session_id` to keep conversation memory. Use `stream: true` for SSE on Plus/Pro/Ultra.
  </Accordion>

  <Accordion title="How do I authenticate requests to api.verba.ink?">
    Send `Authorization: Bearer vka_...` or `x-api-key: vka_...`.
  </Accordion>

  <Accordion title="How do I call the text endpoint?">
    Use `POST /v1/response` with `character` and `messages`.
  </Accordion>

  <Accordion title="How do I call /v1/response with API key auth and session memory?">
    Use `Authorization: Bearer vka_...` (or `x-api-key`), send `character` + `messages`, and reuse `session_id` across calls. If omitted on first call, API returns a generated `session_id` you can keep using.
  </Accordion>

  <Accordion title="How do I generate images through API?">
    Use `POST /v1/image` with `character` and `prompt`.
  </Accordion>

  <Accordion title="What value goes in character?">
    A vanity slug/path/URL (for example `/v/my_slug`).
  </Accordion>

  <Accordion title="Does API support streaming?">
    Yes, `/v1/response` supports SSE when `stream: true`.
  </Accordion>

  <Accordion title="Why does streaming return forbidden?">
    Streaming is plan-gated; free tier requests can return upgrade-required errors.
  </Accordion>

  <Accordion title="Does API keep session memory?">
    Yes, reuse `session_id` to continue context.
  </Accordion>

  <Accordion title="Can I pass system role messages?">
    No, system role is blocked on `/v1/response`.
  </Accordion>

  <Accordion title="Can I send images in /v1/response?">
    Yes, via `messages[].content` image parts or top-level `image_urls`.
  </Accordion>

  <Accordion title="How many image URLs can I attach?">
    Up to 4 combined per request.
  </Accordion>

  <Accordion title="Can I use tools/function calls?">
    Yes, request-scoped HTTP tools are supported with validation and limits.
  </Accordion>

  <Accordion title="What are /v1/response hard payload limits?">
    `messages`: max `60`; each message text max `4000` chars; total text max `20000` chars; combined `image_urls` max `4`; `session_id` max `128` chars; tools max `8` definitions and `2` executed calls per request.
  </Accordion>

  <Accordion title="How many API keys can I keep active?">
    Up to `3` active API keys per account.
  </Accordion>

  <Accordion title="Why do I get payload too large errors?">
    Request bodies have size guards; oversized JSON payloads are rejected.
  </Accordion>
</AccordionGroup>

## Plans and limits questions

<AccordionGroup>
  <Accordion title="What are Free/Plus/Pro/Ultra limits for context, max tokens, verbs, and message rate?">
    Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768` (format: verbs/msg-min/context/max-tokens).
  </Accordion>

  <Accordion title="What are max model context and max response tokens by plan?">
    Free: `50` context, `4096` max tokens. Plus: `75`, `8192`. Pro: `100`, `16384`. Ultra: `150`, `32768`.
  </Accordion>

  <Accordion title="Which plans support streaming on /v1/response?">
    Plus, Pro, and Ultra support `stream: true`. Free does not.
  </Accordion>

  <Accordion title="How many verbs can I create per plan?">
    Free `5`, Plus `10`, Pro `20`, Ultra `40`.
  </Accordion>
</AccordionGroup>

## Discord questions

<AccordionGroup>
  <Accordion title="Why does my bot connect but not respond?">
    Most often missing intents, wrong routing mode, or command/channel permission issues.
  </Accordion>

  <Accordion title="How do I make it respond without pinging in one channel?">
    Use `/activate-channel` there.
  </Accordion>

  <Accordion title="How do I stop auto-replies in that channel?">
    Use `/remove-channel`.
  </Accordion>

  <Accordion title="Can the bot reply to other bots?">
    Default behavior ignores bot-authored messages.
  </Accordion>

  <Accordion title="Why does /reset fail for regular members in a server?">
    Server reset requires elevated permissions.
  </Accordion>

  <Accordion title="Does /reset work in DMs?">
    Yes, DM reset is user-scoped.
  </Accordion>

  <Accordion title="Why does /generate fail?">
    Image generation may be disabled, prompt invalid, or provider temporarily unavailable.
  </Accordion>

  <Accordion title="Why does 'The application did not respond' appear?">
    Usually command timeout or permission/runtime failure.
  </Accordion>

  <Accordion title="Can I hide/disable specific slash commands?">
    Yes, via command toggles in Discord module settings.
  </Accordion>

  <Accordion title="Can I update bot status/presence from dashboard?">
    Yes, status type/text/presence are configurable.
  </Accordion>

  <Accordion title="How do I remove bot from a specific server?">
    Use the server list in Discord module and leave server action.
  </Accordion>

  <Accordion title="Why do only some pings get a reply when many bots are tagged?">
    Multi-bot mention handling intentionally limits responding bots for stability.
  </Accordion>
</AccordionGroup>

## Memory, knowledge, and training questions

<AccordionGroup>
  <Accordion title="How do system instructions work?">
    System instructions are persistent behavior rules for the verb. They define response policy and format, while knowledge/memory provide facts and training examples shape style.
  </Accordion>

  <Accordion title="Where do I set system instructions and what is the limit?">
    Set them in Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`). Max length is `8000` characters.
  </Accordion>

  <Accordion title="How many knowledge entries can I store?">
    Up to 50 per verb.
  </Accordion>

  <Accordion title="How do I add docs quickly from a URL?">
    Use knowledge URL scrape to draft title/content/category.
  </Accordion>

  <Accordion title="What if URL scrape gives poor output?">
    Manually edit the draft entry and tighten structure before saving.
  </Accordion>

  <Accordion title="What is auto memory?">
    Optional automatic saving of durable facts from conversation history.
  </Accordion>

  <Accordion title="What should auto-memory instructions include?">
    Durable facts to keep; explicit exclusions for temporary/noisy details.
  </Accordion>

  <Accordion title="Why does my bot ignore training examples?">
    Add keywords and ensure examples match real user phrasing.
  </Accordion>

  <Accordion title="Can knowledge and memory conflict?">
    Yes. Keep one canonical source and remove outdated entries.
  </Accordion>

  <Accordion title="How does context size affect memory quality?">
    Larger context keeps recent flow better but costs more and can add noise.
  </Accordion>

  <Accordion title="Do memory entries have importance levels?">
    Yes, entries use importance scoring.
  </Accordion>

  <Accordion title="Should I store full transcripts in memory?">
    No. Store compact facts and reusable rules.
  </Accordion>
</AccordionGroup>

## Chat, groups, and realtime questions

<AccordionGroup>
  <Accordion title="How many groups can one user own?">
    Up to 15 owned groups.
  </Accordion>

  <Accordion title="Why did my message get blocked in group chat?">
    Anti-spam filters can block mention floods and invisible-character abuse.
  </Accordion>

  <Accordion title="What is the message history page size?">
    Default 50, capped at 200 per request.
  </Accordion>

  <Accordion title="Can I DM a private verb I do not own?">
    No, private verbs are owner-only.
  </Accordion>

  <Accordion title="Why are updates instant across tabs?">
    WebSocket subscriptions broadcast message/typing/update events in real time.
  </Accordion>

  <Accordion title="Can owner leave their own group?">
    No, owner must transfer ownership or delete the group.
  </Accordion>

  <Accordion title="Who can add/remove verbs in groups?">
    Group owner only.
  </Accordion>

  <Accordion title="Are message image uploads limited?">
    Yes, chat message image upload path is capped to small file sizes (5MB class limits).
  </Accordion>
</AccordionGroup>

## Account, billing, and security questions

<AccordionGroup>
  <Accordion title="How many active API keys can I keep?">
    Up to 3 active keys.
  </Accordion>

  <Accordion title="Do revoked API keys keep working?">
    No, revocation is immediate.
  </Accordion>

  <Accordion title="How long does a magic link stay valid?">
    20 minutes.
  </Accordion>

  <Accordion title="Can I sign in with backup code for 2FA?">
    Yes. Backup codes are one-time use.
  </Accordion>

  <Accordion title="Can I disconnect Patreon anytime?">
    Active paid subscription linkage can block disconnect.
  </Accordion>

  <Accordion title="Why is a model missing in settings?">
    Tier gating: available model set depends on plan.
  </Accordion>

  <Accordion title="Why do requests fail with insufficient credits?">
    Credits are exhausted for the account/owner being billed for that request.
  </Accordion>

  <Accordion title="What happens when I delete my account?">
    Related entities and associations are cleaned up; some owned resources may transfer or be removed.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
    Full limits and field behavior for dashboard configuration.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Operational fix guide for the most common failures.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
