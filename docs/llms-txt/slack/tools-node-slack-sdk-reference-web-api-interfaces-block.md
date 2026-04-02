Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Block

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Block

# Interface: Block

Defined in: packages/types/dist/block-kit/blocks.d.ts:3

## Extended by {#extended-by}

* [`ActionsBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/ActionsBlock)
* [`ContextBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/ContextBlock)
* [`ContextActionsBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/ContextActionsBlock)
* [`DividerBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/DividerBlock)
* [`FileBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/FileBlock)
* [`HeaderBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/HeaderBlock)
* [`InputBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/InputBlock)
* [`MarkdownBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/MarkdownBlock)
* [`RichTextBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBlock)
* [`SectionBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/SectionBlock)
* [`TableBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/TableBlock)
* [`TaskCardBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/TaskCardBlock)
* [`PlanBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/PlanBlock)
* [`VideoBlock`](/tools/node-slack-sdk/reference/web-api/interfaces/VideoBlock)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

* * *

### type {#type}

```text
type: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:7

#### Description {#description-1}

The type of block.
