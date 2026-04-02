Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/TaskCardBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / TaskCardBlock

# Interface: TaskCardBlock

Defined in: [block-kit/blocks.ts:412](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L412)

## Description {#description}

A discrete task or tool call.

## See {#see}

[https://docs.slack.dev/reference/block-kit/blocks/task-card-block/](https://docs.slack.dev/reference/block-kit/blocks/task-card-block/)

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

### details? {#details}

```
optional details: RichTextBlock;
```

Defined in: [block-kit/blocks.ts:431](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L431)

#### Description {#description-2}

Details of the task in the form of a single "rich\_text" entity.

* * *

### output? {#output}

```
optional output: RichTextBlock;
```

Defined in: [block-kit/blocks.ts:436](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L436)

#### Description {#description-3}

Output of the task in the form of a single "rich\_text" entity.

* * *

### sources? {#sources}

```
optional sources: URLSourceElement[];
```

Defined in: [block-kit/blocks.ts:441](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L441)

#### Description {#description-4}

Array of URL source elements used to generate a response.

* * *

### status {#status}

```
status: "pending" | "in_progress" | "complete" | "error";
```

Defined in: [block-kit/blocks.ts:446](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L446)

#### Description {#description-5}

The state of a task. Can be "pending", "in\_progress", "complete", or "error".

* * *

### task_id {#task_id}

```
task_id: string;
```

Defined in: [block-kit/blocks.ts:421](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L421)

#### Description {#description-6}

ID for the task.

* * *

### title {#title}

```
title: string;
```

Defined in: [block-kit/blocks.ts:426](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L426)

#### Description {#description-7}

Title of the task in plain text.

* * *

### type {#type}

```
type: "task_card";
```

Defined in: [block-kit/blocks.ts:416](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L416)

#### Description {#description-8}

The type of block. For this block, type will always be `task_card`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
