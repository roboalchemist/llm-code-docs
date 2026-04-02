Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RichTextStyleable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RichTextStyleable

# Interface: RichTextStyleable

Defined in: packages/types/dist/block-kit/extensions.d.ts:71

## Description {#description}

For use styling Rich Text sub-elements.

## Extended by {#extended-by}

* [`RichTextBroadcastMention`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextBroadcastMention)
* [`RichTextColor`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextColor)
* [`RichTextChannelMention`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextChannelMention)
* [`RichTextDate`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextDate)
* [`RichTextEmoji`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextEmoji)
* [`RichTextLink`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextLink)
* [`RichTextTeamMention`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextTeamMention)
* [`RichTextText`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextText)
* [`RichTextUserMention`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextUserMention)
* [`RichTextUsergroupMention`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextUsergroupMention)

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
