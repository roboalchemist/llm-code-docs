Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextBorderable

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextBorderable

# Interface: RichTextBorderable

Defined in: [block-kit/extensions.ts:71](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L71)

For use in setting border style details on certain Rich Text elements.

## Extended by {#extended-by}

* [`RichTextList`](/tools/node-slack-sdk/reference/types/interfaces/RichTextList)
* [`RichTextQuote`](/tools/node-slack-sdk/reference/types/interfaces/RichTextQuote)
* [`RichTextPreformatted`](/tools/node-slack-sdk/reference/types/interfaces/RichTextPreformatted)

## Properties {#properties}

### border? {#border}

```
optional border: 0 | 1;
```

Defined in: [block-kit/extensions.ts:76](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L76)

#### Description {#description}

Whether to render a quote-block-like border on the inline side of the list. `0` renders no border while `1` renders a border.
