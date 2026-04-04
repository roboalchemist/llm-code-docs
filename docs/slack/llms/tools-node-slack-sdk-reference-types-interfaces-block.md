Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Block

[@slack/types](/tools/node-slack-sdk/reference/types/) / Block

# Interface: Block

Defined in: [block-kit/blocks.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L36)

## Extended by {#extended-by}

* [`ActionsBlock`](/tools/node-slack-sdk/reference/types/interfaces/ActionsBlock)
* [`ContextBlock`](/tools/node-slack-sdk/reference/types/interfaces/ContextBlock)
* [`ContextActionsBlock`](/tools/node-slack-sdk/reference/types/interfaces/ContextActionsBlock)
* [`DividerBlock`](/tools/node-slack-sdk/reference/types/interfaces/DividerBlock)
* [`FileBlock`](/tools/node-slack-sdk/reference/types/interfaces/FileBlock)
* [`HeaderBlock`](/tools/node-slack-sdk/reference/types/interfaces/HeaderBlock)
* [`InputBlock`](/tools/node-slack-sdk/reference/types/interfaces/InputBlock)
* [`MarkdownBlock`](/tools/node-slack-sdk/reference/types/interfaces/MarkdownBlock)
* [`RichTextBlock`](/tools/node-slack-sdk/reference/types/interfaces/RichTextBlock)
* [`SectionBlock`](/tools/node-slack-sdk/reference/types/interfaces/SectionBlock)
* [`TableBlock`](/tools/node-slack-sdk/reference/types/interfaces/TableBlock)
* [`TaskCardBlock`](/tools/node-slack-sdk/reference/types/interfaces/TaskCardBlock)
* [`PlanBlock`](/tools/node-slack-sdk/reference/types/interfaces/PlanBlock)
* [`VideoBlock`](/tools/node-slack-sdk/reference/types/interfaces/VideoBlock)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```

Defined in: [block-kit/blocks.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L48)

#### Description {#description}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

* * *

### type {#type}

```text
type: string;
```

Defined in: [block-kit/blocks.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L40)

#### Description {#description-1}

The type of block.
