# Source: https://docs.verba.ink/guides/memory-and-knowledge.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Memory and knowledge

> How context, long-term memory, training examples, and knowledge entries work together.

## Questions this guide answers

* Why does my verb forget details between messages?
* What is short-term context vs long-term memory?
* What should go into knowledge entries vs memory entries?
* How does URL scraping fill knowledge automatically?
* How do training examples and keywords influence replies?

## The four memory layers

### 1. Conversation context (short-term)

* Uses recent messages from the active conversation.
* Controlled by your `Model Context` setting.
* Higher context improves continuity but costs more tokens.

### 2. Long-term memory

* Manual memory items your verb can keep using over time.
* Best for durable facts and preferences.

### 3. Knowledge entries

* Structured lore/reference entries (title, category, content, importance).
* Best for world facts, policies, product facts, and evergreen docs.

### 4. Training examples

* Input/output examples for style and behavior shaping.
* Keyword matching can prioritize specific examples when relevant.

## Where system instructions fit

System instructions are not a memory entry type. They are the persistent
behavior policy prompt for the verb.

Where to configure:

* Dashboard -> Bot -> AI Engine -> Behavior
* Field: `systemInstructions`

Limit:

* `systemInstructions`: up to `8000` chars

Recommended split of responsibilities:

* System instructions: behavior rules, format constraints, refusal/uncertainty policy
* Knowledge entries: factual source material and documentation
* Long-term memory: durable user/world facts
* Training examples: preferred phrasing and style patterns

## Long-term memory limits

Per memory entry:

* `content`: up to `2000` chars
* `context`: up to `500` chars
* `importance`: `1..10`

Auto-memory settings:

* `autoMemoryEnabled`: on/off
* `autoMemoryInstructions`: up to `2000` chars

<Note>
  Auto-memory is selective, not guaranteed on every turn. The system saves when
  it detects durable information worth retaining.
</Note>

## Knowledge entry limits

Per entry:

* `title`: up to `100` chars
* `content`: up to `8000` chars
* `category`: up to `50` chars
* `importance`: `1..10`

Per verb:

* Maximum knowledge entries: `50`

## Training data limits

Per example:

* `input`: up to `500` chars
* `expected`: up to `2000` chars
* Optional keywords: used for relevance matching

When a user message matches example keywords, those examples are prioritized in
prompt construction.

## URL scraping into knowledge

The knowledge page can scrape a URL and generate a draft entry.

Expected result:

* `title`
* `content`
* `category`

If AI structuring fails, Verba still attempts a basic extraction fallback so you
can edit and save manually.

## Session memory by surface

| Surface           | Memory keying behavior                   |
| ----------------- | ---------------------------------------- |
| Public API v1     | Uses `session_id` per caller + character |
| Discord DM        | Scoped to user-DM context                |
| Discord server    | Scoped to server context                 |
| App group/DM chat | Scoped to group/DM conversation          |

## What to store where

### Put this in long-term memory

* Stable personal preferences
* Ongoing commitments
* Persistent roleplay relationships

### Put this in knowledge entries

* Product facts and policies
* Rulebooks
* Canon lore
* Documentation snippets you want the bot to cite reliably

### Put this in training examples

* Desired phrasing style
* Tone and boundary examples
* Repeated Q/A patterns

## Common mistakes

<AccordionGroup>
  <Accordion title="Dumping full chats into memory">
    Store compact facts, not raw transcripts. Long noisy entries reduce retrieval quality.
  </Accordion>

  <Accordion title="Using knowledge for temporary plans">
    Time-sensitive details belong in conversation context, not permanent knowledge.
  </Accordion>

  <Accordion title="No keywords in training examples">
    Add targeted keywords so examples are picked when users ask matching questions.
  </Accordion>

  <Accordion title="Oversized auto-memory instructions">
    Keep instructions strict and concise. Long broad prompts increase noisy memory writes.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="AI Engine Settings" icon="sliders" href="/guides/ai-engine">
    Tune model context, creativity, and response behavior.
  </Card>

  <Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
    Field-by-field guide for all dashboard settings and limits.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
