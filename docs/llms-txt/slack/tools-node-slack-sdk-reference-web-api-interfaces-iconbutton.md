Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/IconButton

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / IconButton

# Interface: IconButton

Defined in: packages/types/dist/block-kit/block-elements.d.ts:190

## Description {#description}

An icon button to perform actions.

## See {#see}

[Icon button element reference](https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable)

## Properties {#properties}

### accessibility_label? {#accessibility_label}

```text
optional accessibility_label: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:208

#### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

* * *

### action_id? {#action_id}

```text
optional action_id: string;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:21

#### Description {#description-2}

A [Confirm](/tools/node-slack-sdk/reference/web-api/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable#confirm)

* * *

### icon {#icon}

```text
icon: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:199

#### Description {#description-3}

The icon to show.

#### Example {#example}

```text
trash
```text

* * *

### text {#text}

```text
text: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:204

#### Description {#description-4}

Defines an object containing some text.

#### See {#see-1}

[Text object reference](https://docs.slack.dev/reference/block-kit/composition-objects/text-object).

* * *

### type {#type}

```text
type: "icon_button";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:194

#### Description {#description-5}

The type of element. In this case `type` is always `icon_button`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)

* * *

### value? {#value}

```text
optional value: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:212

#### Description {#description-6}

The button value.

* * *

### visible_to_user_ids? {#visible_to_user_ids}

```text
optional visible_to_user_ids: string[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:216

#### Description {#description-7}

User IDs for which the icon appears.
