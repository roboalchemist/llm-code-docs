Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/HeaderBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / HeaderBlock

# Interface: HeaderBlock

Defined in: [block-kit/blocks.ts:192](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L192)

## Description {#description}

Displays a larger-sized text block. A `header` is a plain-text block that displays in a larger, bold font. Use it to delineate between different groups of content in your app's surfaces.

## See {#see}

[Header block reference](https://docs.slack.dev/reference/block-kit/blocks/header-block).

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

### text {#text}

```
text: PlainTextElement;
```

Defined in: [block-kit/blocks.ts:201](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L201)

#### Description {#description-2}

The text for the block, in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement). Maximum length for the text in this field is 150 characters.

* * *

### type {#type}

```
type: "header";
```

Defined in: [block-kit/blocks.ts:196](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L196)

#### Description {#description-3}

The type of block. For a header block, `type` is always `header`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
