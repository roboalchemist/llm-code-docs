Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextEmoji

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextEmoji

# Interface: RichTextEmoji

Defined in: [block-kit/block-elements.ts:879](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L879)

## Description {#description}

An emoji element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable)

## Properties {#properties}

### name {#name}

```
name: string;
```

Defined in: [block-kit/block-elements.ts:887](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L887)

#### Description {#description-1}

Name of emoji, without colons or skin tones, e.g. `wave`

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
type: "emoji";
```

Defined in: [block-kit/block-elements.ts:883](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L883)

#### Description {#description-8}

The type of element. In this case `type` is always `emoji`.

* * *

### unicode? {#unicode}

```
optional unicode: string;
```

Defined in: [block-kit/block-elements.ts:891](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L891)

#### Description {#description-9}

Lowercase hexadecimal Unicode representation of a standard emoji (not for use with custom emoji).

* * *

### url? {#url}

```
optional url: string;
```

Defined in: [block-kit/block-elements.ts:895](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L895)

#### Description {#description-10}

URL of emoji asset. Only used when sharing custom emoji across workspaces.
