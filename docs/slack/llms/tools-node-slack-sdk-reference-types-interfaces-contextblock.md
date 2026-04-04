Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ContextBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / ContextBlock

# Interface: ContextBlock

Defined in: [block-kit/blocks.ts:121](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L121)

## Description {#description}

Displays contextual info, which can include both images and text.

## See {#see}

[Context block reference](https://docs.slack.dev/reference/block-kit/blocks/context-block).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```

Defined in: [block-kit/blocks.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L48)

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/types/interfaces/Block#block_id)

* * *

### elements {#elements}

```text
elements: ContextBlockElement[];
```

Defined in: [block-kit/blocks.ts:130](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L130)

#### Description {#description-2}

An array of [ImageElement](/tools/node-slack-sdk/reference/types/type-aliases/ImageElement), [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) or [MrkdwnElement](/tools/node-slack-sdk/reference/types/interfaces/MrkdwnElement) objects. Maximum number of items is 10.

* * *

### type {#type}

```text
type: "context";
```

Defined in: [block-kit/blocks.ts:125](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L125)

#### Description {#description-3}

The type of block. For a context block, `type` is always `context`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
