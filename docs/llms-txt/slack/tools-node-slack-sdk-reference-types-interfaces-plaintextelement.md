Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement

[@slack/types](/tools/node-slack-sdk/reference/types/) / PlainTextElement

# Interface: PlainTextElement

Defined in: [block-kit/composition-objects.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L138)

## Description {#description}

Defines an object containing some text.

## See {#see}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

## Properties {#properties}

### emoji? {#emoji}

```
optional emoji: boolean;
```

Defined in: [block-kit/composition-objects.ts:150](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L150)

#### Description {#description-1}

Indicates whether emojis in a text field should be escaped into the colon emoji format.

* * *

### text {#text}

```
text: string;
```

Defined in: [block-kit/composition-objects.ts:146](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L146)

#### Description {#description-2}

The text for the block. The minimum length is 1 and maximum length is 3000 characters.

* * *

### type {#type}

```
type: "plain_text";
```

Defined in: [block-kit/composition-objects.ts:142](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L142)

#### Description {#description-3}

The formatting to use for this text object.
