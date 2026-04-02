Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/FeedbackButtons

[@slack/types](/tools/node-slack-sdk/reference/types/) / FeedbackButtons

# Interface: FeedbackButtons

Defined in: [block-kit/block-elements.ts:144](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L144)

## Description {#description}

Buttons to indicate positive or negative feedback.

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#action_id)

* * *

### negative_button {#negative_button}

```text
negative_button: object;
```

Defined in: [block-kit/block-elements.ts:173](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L173)

#### accessibility_label? {#accessibility_label}

```text
optional accessibility_label: string;
```

##### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

#### text {#text}

```text
text: PlainTextElement;
```

##### Description {#description-2}

Defines an object containing some text.

##### See {#see}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

#### value {#value}

```text
value: string;
```

##### Description {#description-3}

The negative feedback button value.

#### Description {#description-4}

A button to indicate negative feedback.

#### See {#see-1}

[Feedback buttons object fields reference](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element/#button-object-fields).

* * *

### positive_button {#positive_button}

```text
positive_button: object;
```

Defined in: [block-kit/block-elements.ts:154](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L154)

#### accessibility_label? {#accessibility_label-1}

```text
optional accessibility_label: string;
```

##### Description {#description-5}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

#### text {#text-1}

```text
text: PlainTextElement;
```

##### Description {#description-6}

Defines an object containing some text.

##### See {#see-2}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

#### value {#value-1}

```text
value: string;
```

##### Description {#description-7}

The positive feedback button value.

#### Description {#description-8}

A button to indicate positive feedback.

#### See {#see-3}

[Feedback buttons object fields reference](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element/#button-object-fields).

* * *

### type {#type}

```text
type: "feedback_buttons";
```

Defined in: [block-kit/block-elements.ts:149](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L149)

#### Description {#description-9}

The type of block. For a feedback buttons block, `type` is always `feedback_buttons`.

#### See {#see-4}

[Feedback buttons element reference](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element).

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
