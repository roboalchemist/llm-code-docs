Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MrkdwnElement

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MrkdwnElement

# Interface: MrkdwnElement

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:143

## Description {#description}

Defines an object containing some text.

## See {#see}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

## Properties {#properties}

### text {#text}

```text
text: string;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:152

#### Description {#description-1}

The text for the block. This field accepts any of the standard text formatting markup. The minimum length is 1 and maximum length is 3000 characters.

* * *

### type {#type}

```text
type: "mrkdwn";
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:147

#### Description {#description-2}

The formatting to use for this text object.

* * *

### verbatim? {#verbatim}

```text
optional verbatim: boolean;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:159

#### Description {#description-3}

When set to `false` (as is default) URLs will be auto-converted into links, conversation names will be link-ified, and certain mentions will be [automatically parsed](https://docs.slack.dev/messaging/formatting-message-text). Using a value of `true` will skip any preprocessing of this nature, although you can still include [manual parsing strings](https://docs.slack.dev/messaging/formatting-message-text).
