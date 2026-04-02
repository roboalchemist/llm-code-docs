Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/URLSourceElement

[@slack/types](/tools/node-slack-sdk/reference/types/) / URLSourceElement

# Interface: URLSourceElement

Defined in: [block-kit/block-elements.ts:710](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L710)

## Description {#description}

A URL source element that displays a URL source for referencing within a task card block.

## See {#see}

[https://docs.slack.dev/reference/block-kit/block-elements/url-source-element](https://docs.slack.dev/reference/block-kit/block-elements/url-source-element)

## Properties {#properties}

### text {#text}

```
text: string;
```

Defined in: [block-kit/block-elements.ts:724](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L724)

#### Description {#description-1}

Display text for the URL.

* * *

### type {#type}

```
type: "url";
```

Defined in: [block-kit/block-elements.ts:714](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L714)

#### Description {#description-2}

The type of element. In this case `type` is always `url`.

* * *

### url {#url}

```
url: string;
```

Defined in: [block-kit/block-elements.ts:719](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L719)

#### Description {#description-3}

The URL type source.
