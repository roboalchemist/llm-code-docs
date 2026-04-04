Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ActionsBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / ActionsBlock

# Interface: ActionsBlock

Defined in: [block-kit/blocks.ts:99](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L99)

## Description {#description}

Holds multiple interactive elements.

## See {#see}

[Actions block reference](https://docs.slack.dev/reference/block-kit/blocks/actions-block).

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
elements: ActionsBlockElement[];
```

Defined in: [block-kit/blocks.ts:108](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L108)

#### Description {#description-2}

An array of InteractiveElements objects. There is a maximum of 25 elements in each action block.

* * *

### type {#type}

```text
type: "actions";
```

Defined in: [block-kit/blocks.ts:103](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L103)

#### Description {#description-3}

The type of block. For an actions block, `type` is always `actions`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
