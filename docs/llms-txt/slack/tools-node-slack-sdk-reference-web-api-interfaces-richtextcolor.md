Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextColor

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextColor

# Interface: RichTextColor

Defined in: packages/types/dist/block-kit/block-elements.d.ts:712

## Description {#description}

A hex color element for use in a rich text message.

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

### type {#type}

```text
type: "color";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:716

#### Description {#description-7}

The type of element. In this case `type` is always `color`.

* * *

### value {#value}

```text
value: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:720

#### Description {#description-8}

The hex value for the color.
