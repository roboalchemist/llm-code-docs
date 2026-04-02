Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextBlock

# Interface: RichTextBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:224

## Description {#description}

Displays formatted, structured representation of text. It is also the output of the Slack client's WYSIWYG message composer, so all messages sent by end-users will have this format. Use this block to include user-defined formatted text in your Block Kit payload. While it is possible to format text with `mrkdwn`, `rich_text` is strongly preferred and allows greater flexibility. You might encounter a `rich_text` block in a message payload, as a built-in type in workflow apps, or as output of the [RichTextInput](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextInput).

## See {#see}

[Rich text block reference](https://docs.slack.dev/reference/block-kit/blocks/rich-text-block).

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

### elements {#elements}

```text
elements: RichTextBlockElement[];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:229

* * *

### type {#type}

```text
type: "rich_text";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:228

#### Description {#description-2}

The type of block. For a rich text block, `type` is always `rich_text`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
