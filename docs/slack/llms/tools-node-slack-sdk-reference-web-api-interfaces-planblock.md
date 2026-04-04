Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PlanBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PlanBlock

# Interface: PlanBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:339

## Description {#description}

A collection of related tasks.

## See {#see}

[https://docs.slack.dev/reference/block-kit/blocks/plan-block/](https://docs.slack.dev/reference/block-kit/blocks/plan-block/)

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

### tasks? {#tasks}

```text
optional tasks: (Record<string, unknown> | TaskCardBlock)[];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:351

#### Description {#description-2}

A sequence of task card blocks. Each task represents a single action within the plan.

* * *

### title {#title}

```text
title: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:347

#### Description {#description-3}

Title of the plan in plain text.

* * *

### type {#type}

```text
type: "plan";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:343

#### Description {#description-4}

The type of block. In this case `type` is always `plan`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
