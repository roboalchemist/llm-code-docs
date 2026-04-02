Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FileBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FileBlock

# Interface: FileBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:103

## Description {#description}

Displays a [remote file](https://docs.slack.dev/messaging/working-with-files#remote). You can't add this block to app surfaces directly, but it will show up when [retrieving messages](https://docs.slack.dev/messaging/retrieving-messages) that contain remote files. If you want to add remote files to messages, [follow our guide](https://docs.slack.dev/messaging/working-with-files#remote).

## See {#see}

[File block reference](https://docs.slack.dev/reference/block-kit/blocks/file-block).

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

### external_id {#external_id}

```text
external_id: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:115

#### Description {#description-2}

The external unique ID for this file.

* * *

### source {#source}

```text
source: string;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:111

#### Description {#description-3}

At the moment, source will always be `remote` for a remote file.

* * *

### type {#type}

```text
type: "file";
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:107

#### Description {#description-4}

The type of block. For a file block, `type` is always `file`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
