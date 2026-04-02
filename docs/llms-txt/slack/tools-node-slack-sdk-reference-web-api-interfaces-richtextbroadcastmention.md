Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBroadcastMention

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextBroadcastMention

# Interface: RichTextBroadcastMention

Defined in: packages/types/dist/block-kit/block-elements.d.ts:699

## Description {#description}

A broadcast mention element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable)

## Properties {#properties}

### range {#range}

```text
range: "channel" | "here" | "everyone";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:707

#### Description {#description-1}

The range of the broadcast; can be one of `here`, `channel` and `everyone`.

* * *

### style? {#style}

```text
optional style: object;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:75

#### bold? {#bold}

```text
optional bold: boolean;
```text

##### Description {#description-2}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```text
optional code: boolean;
```text

##### Description {#description-3}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```text
optional italic: boolean;
```text

##### Description {#description-4}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```text
optional strike: boolean;
```text

##### Description {#description-5}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```text
optional underline: boolean;
```text

##### Description {#description-6}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-7}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable#style)

* * *

### type {#type}

```text
type: "broadcast";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:703

#### Description {#description-8}

The type of element. In this case `type` is always `broadcast`.
