Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextQuote

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextQuote

# Interface: RichTextQuote

Defined in: packages/types/dist/block-kit/block-elements.d.ts:914

## Description {#description}

A quote block within a rich text field.

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
elements: RichTextElement[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:922

#### Description {#description-2}

An array of [RichTextElement](/tools/node-slack-sdk/reference/web-api/type-aliases/RichTextElement) comprising the quote block.

* * *

### type {#type}

```text
type: "rich_text_quote";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:918

#### Description {#description-3}

The type of element. In this case `type` is always `rich_text_quote`.
