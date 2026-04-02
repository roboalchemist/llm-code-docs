Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextBroadcastMention

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextBroadcastMention

# Interface: RichTextBroadcastMention

Defined in: [block-kit/block-elements.ts:791](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L791)

## Description {#description}

A broadcast mention element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable)

## Properties {#properties}

### range {#range}

```
range: "here" | "channel" | "everyone";
```

Defined in: [block-kit/block-elements.ts:799](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L799)

#### Description {#description-1}

The range of the broadcast; can be one of `here`, `channel` and `everyone`.

* * *

### style? {#style}

```
optional style: object;
```

Defined in: [block-kit/extensions.ts:86](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L86)

#### bold? {#bold}

```
optional bold: boolean;
```

##### Description {#description-2}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```
optional code: boolean;
```

##### Description {#description-3}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```
optional italic: boolean;
```

##### Description {#description-4}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```
optional strike: boolean;
```

##### Description {#description-5}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```
optional underline: boolean;
```

##### Description {#description-6}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-7}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable#style)

* * *

### type {#type}

```
type: "broadcast";
```

Defined in: [block-kit/block-elements.ts:795](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L795)

#### Description {#description-8}

The type of element. In this case `type` is always `broadcast`.
