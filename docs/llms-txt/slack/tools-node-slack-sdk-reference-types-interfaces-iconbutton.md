Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/IconButton

[@slack/types](/tools/node-slack-sdk/reference/types/) / IconButton

# Interface: IconButton

Defined in: [block-kit/block-elements.ts:217](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L217)

## Description {#description}

An icon button to perform actions.

## See {#see}

[Icon button element reference](https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable)

## Properties {#properties}

### accessibility_label? {#accessibility_label}

```
optional accessibility_label: string;
```

Defined in: [block-kit/block-elements.ts:235](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L235)

#### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

* * *

### action_id? {#action_id}

```
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```
optional confirm: ConfirmationDialog;
```

Defined in: [block-kit/extensions.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L25)

#### Description {#description-2}

A [Confirm](/tools/node-slack-sdk/reference/types/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable#confirm)

* * *

### icon {#icon}

```
icon: string;
```

Defined in: [block-kit/block-elements.ts:226](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L226)

#### Description {#description-3}

The icon to show.

#### Example {#example}

```
trash
```

* * *

### text {#text}

```
text: PlainTextElement;
```

Defined in: [block-kit/block-elements.ts:231](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L231)

#### Description {#description-4}

Defines an object containing some text.

#### See {#see-1}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

* * *

### type {#type}

```
type: "icon_button";
```

Defined in: [block-kit/block-elements.ts:221](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L221)

#### Description {#description-5}

The type of element. In this case `type` is always `icon_button`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)

* * *

### value? {#value}

```
optional value: string;
```

Defined in: [block-kit/block-elements.ts:239](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L239)

#### Description {#description-6}

The button value.

* * *

### visible_to_user_ids? {#visible_to_user_ids}

```
optional visible_to_user_ids: string[];
```

Defined in: [block-kit/block-elements.ts:243](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L243)

#### Description {#description-7}

User IDs for which the icon appears.
