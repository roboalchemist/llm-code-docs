Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ContextActionsBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ContextActionsBlock

# Interface: ContextActionsBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:75

## Description {#description}

Displays actions as contextual info, which can include both feedback buttons and icon buttons.

## See {#see}

[Context actions block reference](https://docs.slack.dev/reference/block-kit/blocks/context-actions-block).

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
elements: ContextActionsBlockElement[];
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:83

#### Description {#description-2}

An array of [FeedbackButtons](/tools/node-slack-sdk/reference/web-api/interfaces/FeedbackButtons) or [IconButton](/tools/node-slack-sdk/reference/web-api/interfaces/IconButton) block elements. Maximum number of items is 5.

* * *

### type {#type}

```text
type: "context_actions";
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:79

#### Description {#description-3}

The type of block. For a context actions block, `type` is always `context_actions`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
