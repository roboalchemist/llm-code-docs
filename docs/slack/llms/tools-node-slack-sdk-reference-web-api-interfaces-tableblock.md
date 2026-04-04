Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/TableBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TableBlock

# Interface: TableBlock

Defined in: packages/types/dist/block-kit/blocks.d.ts:273

## Description {#description}

Displays structured information in a table.

## See {#see}

[Table block reference](https://docs.slack.dev/reference/block-kit/blocks/table-block).

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

### column_settings? {#column_settings}

```text
optional column_settings: TableBlockColumnSettings[];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:285

#### Description {#description-2}

An array describing column behavior. If there are fewer items in the column\_settings array than there are columns in the table, then the items in the the column\_settings array will describe the same number of columns in the table as there are in the array itself. Any additional columns will have the default behavior. Maximum 20 items.

* * *

### rows {#rows}

```text
rows: (  | RichTextBlock  | RawTextElement)[][];
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:281

#### Description {#description-3}

An array consisting of table rows. Maximum 100 rows. Each row object is an array with a max of 20 table cells. Table cells can have a type of raw\_text or rich\_text.

* * *

### type {#type}

```text
type: "table";
```text

Defined in: packages/types/dist/block-kit/blocks.d.ts:277

#### Description {#description-4}

The type of block. For a table block, `type` is always `table`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/web-api/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Block#type)
