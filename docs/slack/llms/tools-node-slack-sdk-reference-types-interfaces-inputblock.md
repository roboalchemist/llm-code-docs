Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/InputBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / InputBlock

# Interface: InputBlock

Defined in: [block-kit/blocks.ts:251](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L251)

## Description {#description}

Collects information from users via block elements.

## See {#see}

* [Input block reference](https://docs.slack.dev/reference/block-kit/blocks/input-block).
* [Collecting input in modals guide](https://docs.slack.dev/surfaces/modals#gathering_input).
* [Collecting input in Home tabs guide](https://docs.slack.dev/surfaces/app-home).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```
optional block_id: string;
```

Defined in: [block-kit/blocks.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L48)

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/types/interfaces/Block#block_id)

* * *

### dispatch_action? {#dispatch_action}

```
optional dispatch_action: boolean;
```

Defined in: [block-kit/blocks.ts:279](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L279)

#### Description {#description-2}

A boolean that indicates whether or not the use of elements in this block should dispatch a [block\_actions payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload). Defaults to `false`.

* * *

### element {#element}

```
element: InputBlockElement;
```

Defined in: [block-kit/blocks.ts:274](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L274)

#### Description {#description-3}

A block element.

* * *

### hint? {#hint}

```
optional hint: PlainTextElement;
```

Defined in: [block-kit/blocks.ts:265](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L265)

#### Description {#description-4}

An optional hint that appears below an input element in a lighter grey. It must be a [object](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement). Maximum length for the `text` in this field is 2000 characters.

* * *

### label {#label}

```
label: PlainTextElement;
```

Defined in: [block-kit/blocks.ts:260](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L260)

#### Description {#description-5}

A label that appears above an input element in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object. Maximum length for the text in this field is 2000 characters.

* * *

### optional? {#optional}

```
optional optional: boolean;
```

Defined in: [block-kit/blocks.ts:270](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L270)

#### Description {#description-6}

A boolean that indicates whether the input element may be empty when a user submits the modal. Defaults to `false`.

* * *

### type {#type}

```
type: "input";
```

Defined in: [block-kit/blocks.ts:255](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L255)

#### Description {#description-7}

The type of block. For an input block, `type` is always `input`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
