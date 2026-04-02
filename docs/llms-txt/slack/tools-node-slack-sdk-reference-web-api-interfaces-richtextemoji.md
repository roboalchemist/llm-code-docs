Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextEmoji

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextEmoji

# Interface: RichTextEmoji

Defined in: packages/types/dist/block-kit/block-elements.d.ts:783

## Description {#description}

An emoji element for use in a rich text message.

## Extends {#extends}

* [`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable)

## Properties {#properties}

### name {#name}

```text
name: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:791

#### Description {#description-1}

Name of emoji, without colons or skin tones, e.g. `wave`

* * *

### style? {#style}

```text
optional style: object;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:75

#### bold? {#bold}

```text
optional bold: boolean;
```text

##### Description {#description-2}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```text
optional code: boolean;
```text

##### Description {#description-3}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```text
optional italic: boolean;
```text

##### Description {#description-4}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```text
optional strike: boolean;
```text

##### Description {#description-5}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```text
optional underline: boolean;
```text

##### Description {#description-6}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-7}

A limited style object for styling rich text `text` elements.

#### Inherited from {#inherited-from}

[`RichTextStyleable`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable).[`style`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable#style)

* * *

### type {#type}

```text
type: "emoji";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:787

#### Description {#description-8}

The type of element. In this case `type` is always `emoji`.

* * *

### unicode? {#unicode}

```text
optional unicode: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:795

#### Description {#description-9}

Lowercase hexadecimal Unicode representation of a standard emoji (not for use with custom emoji).

* * *

### url? {#url}

```text
optional url: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:799

#### Description {#description-10}

URL of emoji asset. Only used when sharing custom emoji across workspaces.
