Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextPreformatted

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextPreformatted

# Interface: RichTextPreformatted

Defined in: [block-kit/block-elements.ts:1043](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1043)

## Description {#description}

A block of preformatted text within a rich text field.

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
elements: (RichTextLink | RichTextText)[];
```

Defined in: [block-kit/block-elements.ts:1051](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1051)

#### Description {#description-2}

An array of either [RichTextLink](/tools/node-slack-sdk/reference/types/interfaces/RichTextLink) or [RichTextText](/tools/node-slack-sdk/reference/types/interfaces/RichTextText) comprising the preformatted text.

* * *

### type {#type}

```
type: "rich_text_preformatted";
```

Defined in: [block-kit/block-elements.ts:1047](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1047)

#### Description {#description-3}

The type of element. In this case `type` is always `rich_text_preformatted`.
