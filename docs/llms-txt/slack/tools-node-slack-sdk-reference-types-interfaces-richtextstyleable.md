Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextStyleable

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextStyleable

# Interface: RichTextStyleable

Defined in: [block-kit/extensions.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L82)

## Description {#description}

For use styling Rich Text sub-elements.

## Extended by {#extended-by}

* [`RichTextBroadcastMention`](/tools/node-slack-sdk/reference/types/interfaces/RichTextBroadcastMention)
* [`RichTextColor`](/tools/node-slack-sdk/reference/types/interfaces/RichTextColor)
* [`RichTextChannelMention`](/tools/node-slack-sdk/reference/types/interfaces/RichTextChannelMention)
* [`RichTextDate`](/tools/node-slack-sdk/reference/types/interfaces/RichTextDate)
* [`RichTextEmoji`](/tools/node-slack-sdk/reference/types/interfaces/RichTextEmoji)
* [`RichTextLink`](/tools/node-slack-sdk/reference/types/interfaces/RichTextLink)
* [`RichTextTeamMention`](/tools/node-slack-sdk/reference/types/interfaces/RichTextTeamMention)
* [`RichTextText`](/tools/node-slack-sdk/reference/types/interfaces/RichTextText)
* [`RichTextUserMention`](/tools/node-slack-sdk/reference/types/interfaces/RichTextUserMention)
* [`RichTextUsergroupMention`](/tools/node-slack-sdk/reference/types/interfaces/RichTextUsergroupMention)

## Properties {#properties}

### style? {#style}

```
optional style: object;
```

Defined in: [block-kit/extensions.ts:86](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L86)

#### bold? {#bold}

```
optional bold: boolean;
```

##### Description {#description-1}

When `true`, boldens the text in this element. Defaults to `false`.

#### code? {#code}

```
optional code: boolean;
```

##### Description {#description-2}

When `true`, the text is preformatted in an inline code style. Defaults to \`false.

#### italic? {#italic}

```
optional italic: boolean;
```

##### Description {#description-3}

When `true`, italicizes the text in this element. Defaults to `false`.

#### strike? {#strike}

```
optional strike: boolean;
```

##### Description {#description-4}

When `true`, strikes through the text in this element. Defaults to `false`.

#### underline? {#underline}

```
optional underline: boolean;
```

##### Description {#description-5}

When `true`, underlines the text in this element. Defaults to `false`.

#### Description {#description-6}

A limited style object for styling rich text `text` elements.
