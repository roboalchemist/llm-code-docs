Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ActionsBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ActionsBlock

# Interface: ActionsBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:36

## Description {#description}

Holds multiple interactive elements.

## See {#see}

[Actions block reference](https://docs.slack.dev/reference/block-kit/blocks/actions-block).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```
optional block_id: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#block_id)

* * *

### elements {#elements}

```
elements: ActionsBlockElement[];
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:45

#### Description {#description-2}

An array of InteractiveElements objects. There is a maximum of 25 elements in each action block.

* * *

### type {#type}

```
type: "actions";
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:40

#### Description {#description-3}

The type of block. For an actions block, `type` is always `actions`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
