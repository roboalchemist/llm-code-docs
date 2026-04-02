Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextPreformatted

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextPreformatted

# Interface: RichTextPreformatted

Defined in: packages/types/dist/block-kit/block-elements.d.ts:927

## Description {#description}

A block of preformatted text within a rich text field.

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
elements: (RichTextLink | RichTextText)[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:935

#### Description {#description-2}

An array of either [RichTextLink](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextLink) or [RichTextText](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextText) comprising the preformatted text.

* * *

### type {#type}

```text
type: "rich_text_preformatted";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:931

#### Description {#description-3}

The type of element. In this case `type` is always `rich_text_preformatted`.
