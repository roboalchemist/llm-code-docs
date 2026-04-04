Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/HeaderBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / HeaderBlock

# Interface: HeaderBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:122

## Description {#description}

Displays a larger-sized text block. A `header` is a plain-text block that displays in a larger, bold font. Use it to delineate between different groups of content in your app's surfaces.

## See {#see}

[Header block reference](https://docs.slack.dev/reference/block-kit/blocks/header-block).

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
text: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:131

#### Description {#description-2}

The text for the block, in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement). Maximum length for the text in this field is 150 characters.

* * *

### type {#type}

```text
type: "header";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:126

#### Description {#description-3}

The type of block. For a header block, `type` is always `header`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
