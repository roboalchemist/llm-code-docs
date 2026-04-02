Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextLink

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextLink

# Interface: RichTextLink

Defined in: [block-kit/block-elements.ts:901](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L901)

## Description {#description}

A link element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable)

## Properties {#properties}

### style? {#style}

```
optional style: object;
```

Defined in: [block-kit/extensions.ts:86](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L86)

#### bold? {#bold}

```
optional bold: boolean;
```

##### Description {#description-1}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```
optional code: boolean;
```

##### Description {#description-2}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```
optional italic: boolean;
```

##### Description {#description-3}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```
optional strike: boolean;
```

##### Description {#description-4}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```
optional underline: boolean;
```

##### Description {#description-5}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-6}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable#style)

* * *

### text? {#text}

```
optional text: string;
```

Defined in: [block-kit/block-elements.ts:909](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L909)

#### Description {#description-7}

The text to link.

* * *

### type {#type}

```
type: "link";
```

Defined in: [block-kit/block-elements.ts:905](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L905)

#### Description {#description-8}

The type of element. In this case `type` is always `link`.

* * *

### unsafe? {#unsafe}

```
optional unsafe: boolean;
```

Defined in: [block-kit/block-elements.ts:913](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L913)

#### Description {#description-9}

TODO: ?

* * *

### url {#url}

```
url: string;
```

Defined in: [block-kit/block-elements.ts:917](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L917)

#### Description {#description-10}

URL to link to.
