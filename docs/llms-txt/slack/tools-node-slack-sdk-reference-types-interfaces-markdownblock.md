Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MarkdownBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / MarkdownBlock

# Interface: MarkdownBlock

Defined in: [block-kit/blocks.ts:288](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L288)

## Description {#description}

This block can be used with AI apps when you expect a markdown response from an LLM that can get lost in translation rendering in Slack. Providing it in a markdown block leaves the translating to Slack to ensure your message appears as intended. Note that passing a single block may result in multiple blocks after translation.

## See {#see}

[Markdown block reference](https://api.slack.com/reference/block-kit/blocks#markdown).

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
text: string;
```

Defined in: [block-kit/blocks.ts:296](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L296)

#### Description {#description-2}

The standard markdown-formatted text. Limit 12,000 characters max.

* * *

### type {#type}

```
type: "markdown";
```

Defined in: [block-kit/blocks.ts:292](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L292)

#### Description {#description-3}

The type of block. For a markdown block, `type` is always `markdown`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
