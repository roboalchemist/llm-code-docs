Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextList

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextList

# Interface: RichTextList

Defined in: [block-kit/block-elements.ts:1005](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1005)

## Description {#description}

A list block within a rich text field.

## Extends {#extends}

* [`RichTextBorderable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextBorderable)

## Properties {#properties}

### border? {#border}

```
optional border: 0 | 1;
```

Defined in: [block-kit/extensions.ts:76](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L76)

#### Description {#description-1}

Whether to render a quote-block-like border on the inline side of the list. `0` renders no border while `1` renders a border.

#### Inherited from {#inherited-from}

[`RichTextBorderable`](/tools/node-slack-sdk/reference/types/interfaces/RichTextBorderable).[`border`](/tools/node-slack-sdk/reference/types/interfaces/RichTextBorderable#border)

* * *

### elements {#elements}

```
elements: RichTextSection[];
```

Defined in: [block-kit/block-elements.ts:1013](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1013)

#### Description {#description-2}

An array of [RichTextSection](/tools/node-slack-sdk/reference/types/interfaces/RichTextSection) elements comprising each list item.

* * *

### indent? {#indent}

```
optional indent: number;
```

Defined in: [block-kit/block-elements.ts:1023](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1023)

#### Description {#description-3}

The style of the list points. Can be a number from `0` (default) to `8`. Yields a different character or characters rendered as the list points. Also affected by the `style` property.

* * *

### style {#style}

```
style: "bullet" | "ordered";
```

Defined in: [block-kit/block-elements.ts:1018](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1018)

#### Description {#description-4}

The type of list. Can be either `bullet` (the list points are all rendered the same way) or `ordered` (the list points increase numerically from 1).

* * *

### type {#type}

```
type: "rich_text_list";
```

Defined in: [block-kit/block-elements.ts:1009](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1009)

#### Description {#description-5}

The type of element. In this case `type` is always `rich_text_list`.
