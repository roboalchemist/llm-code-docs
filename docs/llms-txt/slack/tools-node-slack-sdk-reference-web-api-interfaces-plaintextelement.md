Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PlainTextElement

# Interface: PlainTextElement

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:125

## Description {#description}

Defines an object containing some text.

## See {#see}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

## Properties {#properties}

### emoji? {#emoji}

```text
optional emoji: boolean;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:137

#### Description {#description-1}

Indicates whether emojis in a text field should be escaped into the colon emoji format.

* * *

### text {#text}

```text
text: string;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:133

#### Description {#description-2}

The text for the block. The minimum length is 1 and maximum length is 3000 characters.

* * *

### type {#type}

```text
type: "plain_text";
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:129

#### Description {#description-3}

The formatting to use for this text object.
