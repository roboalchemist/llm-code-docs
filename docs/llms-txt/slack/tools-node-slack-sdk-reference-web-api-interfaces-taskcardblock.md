Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/TaskCardBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TaskCardBlock

# Interface: TaskCardBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:305

## Description {#description}

A discrete task or tool call.

## See {#see}

[https://docs.slack.dev/reference/block-kit/blocks/task-card-block/](https://docs.slack.dev/reference/block-kit/blocks/task-card-block/)

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

### details? {#details}

```text
optional details: RichTextBlock;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:321

#### Description {#description-2}

Details of the task in the form of a single "rich\_text" entity.

* * *

### output? {#output}

```text
optional output: RichTextBlock;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:325

#### Description {#description-3}

Output of the task in the form of a single "rich\_text" entity.

* * *

### sources? {#sources}

```text
optional sources: URLSourceElement[];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:329

#### Description {#description-4}

Array of URL source elements used to generate a response.

* * *

### status {#status}

```text
status: "pending" | "in_progress" | "complete" | "error";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:333

#### Description {#description-5}

The state of a task. Can be "pending", "in\_progress", "complete", or "error".

* * *

### task_id {#task_id}

```text
task_id: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:313

#### Description {#description-6}

ID for the task.

* * *

### title {#title}

```text
title: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:317

#### Description {#description-7}

Title of the task in plain text.

* * *

### type {#type}

```text
type: "task_card";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:309

#### Description {#description-8}

The type of block. For this block, type will always be `task_card`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
