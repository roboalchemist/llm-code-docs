Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextList

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextList

# Interface: RichTextList

Defined in: packages/types/dist/block-kit/block-elements.d.ts:891

## Description {#description}

A list block within a rich text field.

## Extends {#extends}

* [`RichTextBorderable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBorderable)

## Properties {#properties}

### border? {#border}

```text
optional border: 0 | 1;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:66

#### Description {#description-1}

Whether to render a quote-block-like border on the inline side of the list. `0` renders no border while `1` renders a border.

#### Inherited from {#inherited-from}

[`RichTextBorderable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBorderable).[`border`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBorderable#border)

* * *

### elements {#elements}

```text
elements: RichTextSection[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:899

#### Description {#description-2}

An array of [RichTextSection](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextSection) elements comprising each list item.

* * *

### indent? {#indent}

```text
optional indent: number;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:909

#### Description {#description-3}

The style of the list points. Can be a number from `0` (default) to `8`. Yields a different character or characters rendered as the list points. Also affected by the `style` property.

* * *

### style {#style}

```text
style: "bullet" | "ordered";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:904

#### Description {#description-4}

The type of list. Can be either `bullet` (the list points are all rendered the same way) or `ordered` (the list points increase numerically from 1).

* * *

### type {#type}

```text
type: "rich_text_list";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:895

#### Description {#description-5}

The type of element. In this case `type` is always `rich_text_list`.
