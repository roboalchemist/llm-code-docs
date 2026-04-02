Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Confirm

[@slack/types](/tools/node-slack-sdk/reference/types/) / Confirm

# Interface: Confirm

Defined in: [block-kit/composition-objects.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L19)

## Deprecated {#deprecated}

Confirm aliased to [ConfirmationDialog](/tools/node-slack-sdk/reference/types/interfaces/ConfirmationDialog) in order to make the construct clearer and line up terminology with docs.slack.dev.

## Description {#description}

Defines a dialog that adds a confirmation step to interactive elements.

## See {#see}

[Confirmation dialog object reference](https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object).

## Extended by {#extended-by}

* [`ConfirmationDialog`](/tools/node-slack-sdk/reference/types/interfaces/ConfirmationDialog)

## Properties {#properties}

### confirm? {#confirm}

```text
optional confirm: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:34](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L34)

#### Description {#description-1}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) text object to define the text of the button that confirms the action. Maximum length for the `text` in this field is 30 characters.

* * *

### deny? {#deny}

```text
optional deny: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L39)

#### Description {#description-2}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) text object to define the text of the button that cancels the action. Maximum length for the `text` in this field is 30 characters.

* * *

### style? {#style}

```text
optional style: ColorScheme;
```

Defined in: [block-kit/composition-objects.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L45)

#### Description {#description-3}

Defines the color scheme applied to the `confirm` button. A value of `danger` will display the button with a red background on desktop, or red text on mobile. A value of `primary` will display the button with a green background on desktop, or blue text on mobile. If this field is not provided, the default value will be `primary`.

* * *

### text {#text}

```text
text:   | PlainTextElement  | MrkdwnElement;
```

Defined in: [block-kit/composition-objects.ts:29](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L29)

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) text object that defines the explanatory text that appears in the confirm dialog. Maximum length for the `text` in this field is 300 characters.

* * *

### title? {#title}

```text
optional title: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L24)

#### Description {#description-5}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) text object that defines the dialog's title. Maximum length for this field is 100 characters.
