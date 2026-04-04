Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Button

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Button

# Interface: Button

Defined in: packages/types/dist/block-kit/block-elements.d.ts:9

## Description {#description}

Allows users a direct path to performing basic actions.

## See {#see}

* [Button element reference](https://docs.slack.dev/reference/block-kit/block-elements/button-element).
* [is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interactionThis).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable)

## Properties {#properties}

### accessibility_label? {#accessibility_label}

```text
optional accessibility_label: string;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:43

#### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

* * *

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:21

#### Description {#description-2}

A [Confirm](/tools/node-slack-sdk/reference/web-api/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable#confirm)

* * *

### style? {#style}

```text
optional style: ColorScheme;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:38

#### Description {#description-3}

Decorates buttons with alternative visual color schemes. Use this option with restraint. `primary` gives buttons a green outline and text, ideal for affirmation or confirmation actions. `primary` should only be used for one button within a set. `danger` gives buttons a red outline and text, and should be used when the action is destructive. Use `danger` even more sparingly than primary. If you don't include this field, the default button style will be used.

* * *

### text {#text}

```text
text: PlainTextElement;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:18

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines the button's text. `text` may truncate with ~30 characters. Maximum length for the text in this field is 75 characters.

* * *

### type {#type}

```text
type: "button";
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:13

#### Description {#description-5}

The type of element. In this case `type` is always `button`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)

* * *

### url? {#url}

```text
optional url: string;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:29

#### Description {#description-6}

A URL to load in the user's browser when the button is clicked. Maximum length for this field is 3000 characters. If you're using `url`, you'll still receive an [interaction payload](https://docs.slack.dev/interactivity/handling-user-interaction#payloads) and will need to send an [acknowledgement response](https://docs.slack.dev/interactivity/handling-user-interaction#acknowledgment_response).

* * *

### value? {#value}

```text
optional value: string;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:23

#### Description {#description-7}

The value to send along with the [interaction payload](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 2000 characters.
