Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/TableBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / TableBlock

# Interface: TableBlock

Defined in: [block-kit/blocks.ts:378](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L378)

## Description {#description}

Displays structured information in a table.

## See {#see}

[Table block reference](https://docs.slack.dev/reference/block-kit/blocks/table-block).

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

### column_settings? {#column_settings}

```
optional column_settings: TableBlockColumnSettings[];
```

Defined in: [block-kit/blocks.ts:390](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L390)

#### Description {#description-2}

An array describing column behavior. If there are fewer items in the column\_settings array than there are columns in the table, then the items in the the column\_settings array will describe the same number of columns in the table as there are in the array itself. Any additional columns will have the default behavior. Maximum 20 items.

* * *

### rows {#rows}

```
rows: (  | RichTextBlock  | RawTextElement)[][];
```

Defined in: [block-kit/blocks.ts:386](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L386)

#### Description {#description-3}

An array consisting of table rows. Maximum 100 rows. Each row object is an array with a max of 20 table cells. Table cells can have a type of raw\_text or rich\_text.

* * *

### type {#type}

```
type: "table";
```

Defined in: [block-kit/blocks.ts:382](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L382)

#### Description {#description-4}

The type of block. For a table block, `type` is always `table`.

#### Overrides {#overrides}

[`Block`](/tools/node-slack-sdk/reference/types/interfaces/Block).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Block#type)
