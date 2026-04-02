Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/InputBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / InputBlock

# Interface: InputBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:164

## Description {#description}

Collects information from users via block elements.

## See {#see}

* [Input block reference](https://docs.slack.dev/reference/block-kit/blocks/input-block).
* [Collecting input in modals guide](https://docs.slack.dev/surfaces/modals#gathering_input).
* [Collecting input in Home tabs guide](https://docs.slack.dev/surfaces/app-home).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block)

## Properties {#properties}

### block_id? {#block_id}

```text
optional block_id: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description-1}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#block_id)

* * *

### dispatch_action? {#dispatch_action}

```text
optional dispatch_action: boolean;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:192

#### Description {#description-2}

A boolean that indicates whether or not the use of elements in this block should dispatch a [block\_actions payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload). Defaults to `false`.

* * *

### element {#element}

```text
element: InputBlockElement;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:187

#### Description {#description-3}

A block element.

* * *

### hint? {#hint}

```text
optional hint: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:178

#### Description {#description-4}

An optional hint that appears below an input element in a lighter grey. It must be a [object](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement). Maximum length for the `text` in this field is 2000 characters.

* * *

### label {#label}

```text
label: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:173

#### Description {#description-5}

A label that appears above an input element in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object. Maximum length for the text in this field is 2000 characters.

* * *

### optional? {#optional}

```text
optional optional: boolean;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:183

#### Description {#description-6}

A boolean that indicates whether the input element may be empty when a user submits the modal. Defaults to `false`.

* * *

### type {#type}

```text
type: "input";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:168

#### Description {#description-7}

The type of block. For an input block, `type` is always `input`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
