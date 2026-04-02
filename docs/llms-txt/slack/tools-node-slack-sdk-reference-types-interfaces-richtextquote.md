Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextQuote

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextQuote

# Interface: RichTextQuote

Defined in: [block-kit/block-elements.ts:1029](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1029)

## Description {#description}

A quote block within a rich text field.

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
elements: RichTextElement[];
```

Defined in: [block-kit/block-elements.ts:1037](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1037)

#### Description {#description-2}

An array of [RichTextElement](/tools/node-slack-sdk/reference/types/type-aliases/RichTextElement) comprising the quote block.

* * *

### type {#type}

```
type: "rich_text_quote";
```

Defined in: [block-kit/block-elements.ts:1033](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1033)

#### Description {#description-3}

The type of element. In this case `type` is always `rich_text_quote`.
