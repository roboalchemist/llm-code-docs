# Source: https://docs.verba.ink/guides/ai-engine.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# AI engine settings

> Tune model behavior, response length, context, and search.

## Questions this guide answers

* Which settings affect creativity vs consistency?
* Why are responses short or long?
* How much context and max tokens can my plan use?
* What does web search actually do?

## Core controls

| Setting       | Range          | What it changes                    |
| ------------- | -------------- | ---------------------------------- |
| Temperature   | `0..2`         | Randomness and creativity          |
| Top-p         | `0..1`         | Diversity of token selection       |
| Model Context | plan-limited   | Number of recent messages included |
| Reply Style   | preset         | Voice/format tendency              |
| Multi-message | on/off + delay | Sends split follow-up replies      |
| Web search    | on/off         | Allows live web-grounded replies   |

## System instructions (behavior prompt)

System instructions are your verb's persistent behavior rules.

Where to set:

* Dashboard -> Bot -> AI Engine -> Behavior
* Field name: `systemInstructions`

Limit:

* Up to `8000` characters

How they interact with other layers:

* `systemInstructions`: behavior/rules/tone constraints
* Training examples: style shaping and response pattern hints
* Long-term memory: durable facts/preferences
* Knowledge entries: factual/reference content
* Conversation context: recent turns in current chat/thread/session

Practical rule:

* Put "how to behave" in system instructions.
* Put "facts to remember" in knowledge/memory.
* Put "how to phrase outputs" in training examples.

## Plan-based limits

Current default limits:

| Plan  | Max model context | Max response tokens |
| ----- | ----------------- | ------------------- |
| Free  | `50`              | `4096`              |
| Plus  | `75`              | `8192`              |
| Pro   | `100`             | `16384`             |
| Ultra | `150`             | `32768`             |

<Note>
  If you request settings above your tier limits, they are clamped or rejected
  depending on the endpoint.
</Note>

## Recommended presets

<CardGroup cols={2}>
  <Card title="Reliable support" icon="shield">
    Temperature `0.4-0.7`, top-p `0.7-0.9`, moderate context.
  </Card>

  <Card title="Creative roleplay" icon="sparkles">
    Temperature `0.8-1.1`, top-p `0.9-1.0`, higher context.
  </Card>

  <Card title="Cost-aware" icon="wallet">
    Lower context, web search off, shorter reply style.
  </Card>

  <Card title="Fast troubleshooting" icon="bolt">
    Lower context + deterministic settings to reduce latency variance.
  </Card>
</CardGroup>

## Multi-message behavior

When enabled:

* Verba can split a response into multiple shorter messages.
* Delay between parts is configurable (`0..10000ms`).

Use this for natural chat pacing; disable if you want one compact answer.

## Web search behavior

When enabled, Verba may perform model-driven search planning before the final answer.
This improves freshness, but can increase:

* Latency
* Token usage
* Cost

Use web search for:

* News
* Live pricing
* Fast-changing product details

Keep it off for:

* Roleplay
* Stable canon/lore
* Deterministic support flows

## System instructions best practices

* Keep instructions concrete and scoped.
* Avoid contradictory rules.
* Prefer short imperative bullets over long prose.
* Include failure policy (what to do when unknown).
* Specify output format explicitly (headings, bullets, steps, code blocks).

## Quick diagnostics

<AccordionGroup>
  <Accordion title="Replies are too generic">
    Lower temperature, tighten system instructions, and add targeted training examples.
  </Accordion>

  <Accordion title="Bot forgets recent details">
    Increase model context (within your plan limit).
  </Accordion>

  <Accordion title="Replies are too short">
    Increase max tokens and use a fuller reply style.
  </Accordion>

  <Accordion title="Replies are too slow">
    Reduce context and disable web search unless needed.
  </Accordion>
</AccordionGroup>

<Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
  See all AI-related fields and limits in one place.
</Card>

Built with [Mintlify](https://mintlify.com).
