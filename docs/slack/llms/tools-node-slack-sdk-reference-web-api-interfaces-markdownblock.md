Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MarkdownBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MarkdownBlock

# Interface: MarkdownBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:200

## Description {#description}

This block can be used with AI apps when you expect a markdown response from an LLM that can get lost in translation rendering in Slack. Providing it in a markdown block leaves the translating to Slack to ensure your message appears as intended. Note that passing a single block may result in multiple blocks after translation.

## See {#see}

[Markdown block reference](https://api.slack.com/reference/block-kit/blocks#markdown).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#block_id)

* * *

### text {#text}

```text
text: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:208

#### Description {#description-2}

The standard markdown-formatted text. Limit 12,000 characters max.

* * *

### type {#type}

```text
type: "markdown";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:204

#### Description {#description-3}

The type of block. For a markdown block, `type` is always `markdown`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
