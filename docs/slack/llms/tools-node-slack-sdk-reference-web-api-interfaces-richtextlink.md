Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextLink

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextLink

# Interface: RichTextLink

Defined in: packages/types/dist/block-kit/block-elements.d.ts:804

## Description {#description}

A link element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable)

## Properties {#properties}

### style? {#style}

```text
optional style: object;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:75

#### bold? {#bold}

```text
optional bold: boolean;
```text

##### Description {#description-1}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```text
optional code: boolean;
```text

##### Description {#description-2}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```text
optional italic: boolean;
```text

##### Description {#description-3}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```text
optional strike: boolean;
```text

##### Description {#description-4}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```text
optional underline: boolean;
```text

##### Description {#description-5}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-6}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable#style)

* * *

### text? {#text}

```text
optional text: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:812

#### Description {#description-7}

The text to link.

* * *

### type {#type}

```text
type: "link";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:808

#### Description {#description-8}

The type of element. In this case `type` is always `link`.

* * *

### unsafe? {#unsafe}

```text
optional unsafe: boolean;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:816

#### Description {#description-9}

TODO: ?

* * *

### url {#url}

```text
url: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:820

#### Description {#description-10}

URL to link to.
