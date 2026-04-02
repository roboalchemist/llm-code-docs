Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SectionBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SectionBlock

# Interface: SectionBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:242

## Description {#description}

Displays text, possibly alongside block elements. A section can be used as a simple text block, in combination with text fields, or side-by-side with certain [block elements](https://docs.slack.dev/reference/block-kit/block-elements).

## See {#see}

[Section block reference](https://docs.slack.dev/reference/block-kit/blocks/section-block).

## Extends {#extends}

* [`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block)

## Properties {#properties}

### accessory? {#accessory}

```text
optional accessory: SectionBlockAccessory;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:263

#### Description {#description-1}

One of the compatible element objects.

* * *

### block_id? {#block_id}

```text
optional block_id: string;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:15

#### Description {#description-2}

A string acting as a unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.

#### Inherited from {#inherited-from}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`block_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#block_id)

* * *

### expand? {#expand}

```text
optional expand: boolean;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:267

Whether or not this section block's text should always expand when rendered. If false or not provided, it may be rendered with a 'see more' option to expand and show the full text. For AI Assistant apps, this allows the app to post long messages without users needing to click 'see more' to expand the message.

* * *

### fields? {#fields}

```text
optional fields: TextObject[];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:259

#### Description {#description-3}

Required if no `text` is provided. An array of text objects. Any text objects included with `fields` will be rendered in a compact format that allows for 2 columns of side-by-side text. Maximum number of items is 10. Maximum length for the text in each item is 2000 characters. [Click here for an example](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22text%22:%22A%20message%20*with%20some%20bold%20text*%20and%20_some%20italicized%20text_.%22,%22type%22:%22mrkdwn%22%7D,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Priority*%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type*%22%7D,%7B%22type%22:%22plain_text%22,%22text%22:%22High%22%7D,%7B%22type%22:%22plain_text%22,%22text%22:%22String%22%7D%5D%7D%5D%7D).

* * *

### text? {#text}

```text
optional text: TextObject;
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:252

#### Description {#description-4}

The text for the block, in the form of a [TextObject](/tools/node-slack-sdk/reference/web-api/type-aliases/TextObject). Minimum length for the `text` in this field is 1 and maximum length is 3000 characters. This field is not required if a valid array of `fields` objects is provided instead.

* * *

### type {#type}

```text
type: "section";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:246

#### Description {#description-5}

The type of block. For a section block, `type` is always `section`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
