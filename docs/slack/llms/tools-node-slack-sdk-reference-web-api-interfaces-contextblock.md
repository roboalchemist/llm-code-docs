Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ContextBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ContextBlock

# Interface: ContextBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:56

## Description {#description}

Displays contextual info, which can include both images and text.

## See {#see}

[Context block reference](https://docs.slack.dev/reference/block-kit/blocks/context-block).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#block_id)

* * *

### elements {#elements}

```text
elements: ContextBlockElement[];
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:65

#### Description {#description-2}

An array of [ImageElement](/tools/node-slack-sdk/reference/web-api/type-aliases/ImageElement), [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) or [MrkdwnElement](/tools/node-slack-sdk/reference/web-api/interfaces/MrkdwnElement) objects. Maximum number of items is 10.

* * *

### type {#type}

```text
type: "context";
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:60

#### Description {#description-3}

The type of block. For a context block, `type` is always `context`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
