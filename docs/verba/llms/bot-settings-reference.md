# Source: https://docs.verba.ink/guides/bot-settings-reference.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Bot settings reference

> Field-by-field guide to AI, memory, knowledge, training, voice, and Discord settings.

## Why this page exists

This is a practical reference for all major bot configuration panels in the dashboard.
Use it when you need exact ranges, limits, and behavior implications.

## AI engine settings

| Field                 | Range / Limit | Notes                                            |
| --------------------- | ------------- | ------------------------------------------------ |
| `temperature`         | `0..2`        | Creativity/randomness                            |
| `top_p`               | `0..1`        | Diversity control                                |
| `modelContext`        | plan-capped   | Number of history messages considered            |
| `replyStyle`          | preset enum   | `default`, `short`, `creative`, `crazy`, `human` |
| `webSearch`           | boolean       | Enables web-grounded answers                     |
| `multiMessageEnabled` | boolean       | Split response into multiple messages            |
| `multiMessageDelayMs` | `0..10000` ms | Delay between split parts                        |

### Plan caps

| Plan  | maxModelContext | maxTokens |
| ----- | --------------- | --------- |
| Free  | 50              | 4096      |
| Plus  | 75              | 8192      |
| Pro   | 100             | 16384     |
| Ultra | 150             | 32768     |

## Behavior settings

| Field                | Limit        | Notes                                             |
| -------------------- | ------------ | ------------------------------------------------- |
| `systemInstructions` | `8000` chars | Extra behavior control                            |
| `autonomousMode`     | boolean      | Enables autonomous behavior paths where supported |

## Training settings

Per example:

* `input`: max `500` chars
* `expected`: max `2000` chars
* `importance`: `1..10`
* `keywords[]`: optional relevance hints

Keyword matches can prioritize specific examples during generation.

## Memory settings

Per memory entry:

* `content`: max `2000` chars
* `context`: max `500` chars
* `importance`: `1..10`

Global memory toggles:

* `autoMemoryEnabled`: boolean
* `autoMemoryInstructions`: max `2000` chars

## Knowledge settings

Per knowledge entry:

* `title`: max `100` chars
* `content`: max `8000` chars
* `category`: max `50` chars
* `importance`: `1..10`

Per verb:

* max `50` knowledge entries

URL scrape helper:

* Can auto-draft title/content/category from a provided URL.

## Voice engine settings

Common fields:

* `voiceEnabled`
* `voiceResponseFrequency` (`0..100`)
* `selectedVoice`
* `voiceLanguage`
* `voiceModel`
* `voiceReferenceText`

Voice cloning:

* Up to `3` clones per verb

## Image engine settings

* `imageGeneration` toggle controls whether image commands/flows are active.
* `imageModel` selection is tier-aware.
* Non-eligible model selections can be automatically downgraded to allowed tiers.

## Discord module settings

Main controls:

* Connect/disconnect bot token
* Status/presence profile
* Slash command toggles
* AI channel management
* Server list/leave server tools

Core profile defaults include:

* Presence values: `online`, `idle`, `dnd`, `offline`
* Default status text behavior if unset

## Custom messages settings

Customizable response strings include:

* Rate limit
* Reset success/empty messages (DM + server)
* AI/processing/image errors
* Channel management messages
* Permission and server-only errors
* Voice join/leave messages

Per custom message field:

* Max length: `500` chars at schema level

<Note>
  UI may show stricter editing caps for some textareas to keep messages concise.
</Note>

## Validation and save failures

Common save rejection reasons:

* Out-of-range numeric values
* Context/model limit above plan cap
* Oversized memory/knowledge/training content
* Invalid types for structured fields

If a save fails, check browser console + response payload first, then compare against limits on this page.

<CardGroup cols={2}>
  <Card title="AI Engine Settings" icon="sliders" href="/guides/ai-engine">
    Practical tuning guidance for model behavior.
  </Card>

  <Card title="Memory and Knowledge" icon="database" href="/guides/memory-and-knowledge">
    How persistence layers interact in real usage.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
