Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PlanBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / PlanBlock

# Interface: PlanBlock

Defined in: [block-kit/blocks.ts:453](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L453)

## Description {#description}

A collection of related tasks.

## See {#see}

[https://docs.slack.dev/reference/block-kit/blocks/plan-block/](https://docs.slack.dev/reference/block-kit/blocks/plan-block/)

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```
optional block_id: string;
```

Defined in: [block-kit/blocks.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L48)

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/types/interfaces/Block#block_id)

* * *

### tasks? {#tasks}

```
optional tasks: (TaskCardBlock | Record<string, unknown>)[];
```

Defined in: [block-kit/blocks.ts:467](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L467)

#### Description {#description-2}

A sequence of task card blocks. Each task represents a single action within the plan.

* * *

### title {#title}

```
title: string;
```

Defined in: [block-kit/blocks.ts:462](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L462)

#### Description {#description-3}

Title of the plan in plain text.

* * *

### type {#type}

```
type: "plan";
```

Defined in: [block-kit/blocks.ts:457](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L457)

#### Description {#description-4}

The type of block. In this case `type` is always `plan`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
