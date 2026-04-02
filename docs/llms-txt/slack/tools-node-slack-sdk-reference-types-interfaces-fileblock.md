Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/FileBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / FileBlock

# Interface: FileBlock

Defined in: [block-kit/blocks.ts:172](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L172)

## Description {#description}

Displays a [remote file](https://docs.slack.dev/messaging/working-with-files#remote). You can't add this block to app surfaces directly, but it will show up when [retrieving messages](https://docs.slack.dev/messaging/retrieving-messages) that contain remote files. If you want to add remote files to messages, [follow our guide](https://docs.slack.dev/messaging/working-with-files#remote).

## See {#see}

[File block reference](https://docs.slack.dev/reference/block-kit/blocks/file-block).

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

### external_id {#external_id}

```text
external_id: string;
```

Defined in: [block-kit/blocks.ts:184](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L184)

#### Description {#description-2}

The external unique ID for this file.

* * *

### source {#source}

```text
source: string;
```

Defined in: [block-kit/blocks.ts:180](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L180)

#### Description {#description-3}

At the moment, source will always be `remote` for a remote file.

* * *

### type {#type}

```text
type: "file";
```

Defined in: [block-kit/blocks.ts:176](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L176)

#### Description {#description-4}

The type of block. For a file block, `type` is always `file`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
