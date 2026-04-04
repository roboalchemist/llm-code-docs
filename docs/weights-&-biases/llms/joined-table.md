# Source: https://docs.wandb.ai/models/ref/query-panel/joined-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# joined-table

## Chainable Ops

### <a id="asset-file" />`asset-file`

Returns the *file* of the asset

| Argument | Description |
| :------- | :---------- |
| `asset`  | The asset   |

#### Return Value

The *file* of the asset

### <a id="joinedtable-file" />`joinedtable-file`

Returns the *file* of a *joined-table*

| Argument      | Description        |
| :------------ | :----------------- |
| `joinedTable` | The *joined-table* |

#### Return Value

The  *file* of a *joined-table*

### <a id="joinedtable-rows" />`joinedtable-rows`

Returns the rows of a *joined-table*

| Argument      | Description                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------- |
| `joinedTable` | The *joined-table*                                                                             |
| `leftOuter`   | Whether to include rows from the left table that do not have a matching row in the right table |
| `rightOuter`  | Whether to include rows from the right table that do not have a matching row in the left table |

#### Return Value

The rows of the *joined-table*

## List Ops

### <a id="asset-file" />`asset-file`

Returns the *file* of the asset

| Argument | Description |
| :------- | :---------- |
| `asset`  | The asset   |

#### Return Value

The *file* of the asset
