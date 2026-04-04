Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBorderable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextBorderable

# Interface: RichTextBorderable

Defined in: packages/types/dist/block-kit/extensions.d.ts:61

For use in setting border style details on certain Rich Text elements.

## Extended by {#extended-by}

* [`RichTextList`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextList)
* [`RichTextQuote`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextQuote)
* [`RichTextPreformatted`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextPreformatted)

## Properties {#properties}

### border? {#border}

```text
optional border: 0 | 1;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:66

#### Description {#description}

Whether to render a quote-block-like border on the inline side of the list. `0` renders no border while `1` renders a border.
