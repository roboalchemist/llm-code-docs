Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DividerBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DividerBlock

# Interface: DividerBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:90

## Description {#description}

Visually separates pieces of info inside of a message. A content divider, like an `<hr>`, to split up different blocks inside of a message. The divider block is nice and neat, requiring only a `type`.

## See {#see}

[Divider block reference](https://docs.slack.dev/reference/block-kit/blocks/divider-block).

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

### type {#type}

```text
type: "divider";
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:94

#### Description {#description-2}

The type of block. For a divider block, `type` is always `divider`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
