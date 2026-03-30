# transaction

> The main mutation method, covers most of the modifications that can be done to the schema with three different transaction types: create, update and delete.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Transaction Type

Arguments

Type

Description

Create

`parentId`

`string`

The block ID to target, where the data will be injected

`data`

`Object`

The block values to be inserted, `type` is mandatory and will constraint the object type to the specific block schema

`type`

`”create”`

The transaction type

Delete

`id`

`string`

The block ID to delete

`type`

`”delete”`

The transaction type

Update

`data`

`Object`

Very similar to `create` data, but has an extra mandatory field `id` that maps to the existing block that will be updated

`type`

`”update”`

The transaction type

## Example

Check out our Mutation API Playground for full examples.

*   [Playground](https://mutation-api-playground.vercel.app/).
    
*   [Source](https://github.com/basehub-ai/mutations-api-example).
    
*   [Content](https://basehub.com/basehub/mutation-api-playground/explore).
    

## Create

When running the create transaction, you will need to pass two additional parameters: `parentId` and `data`.

The `parentId` is the ID from the block where the creation will be done, could be any block, but that will affect which data structures are valid. In the example above, using that specific `parentId` we cannot insert anything apart from instances, because collection children are always instances (or a component that works as template).

The `data` field is the new block schema and values, including all its children.

## Bulk Insert (Multiple Creations)

When using the `create` transaction type, the `data` field can accept either a single object or an array of objects. This allows you to create multiple instances inside the same parent block in a single transaction call.

## Automatic Commit

The `autoCommit` is an optional field that accepts any `string` as the commit message that will be injected into the repository history. If not provided, the mutation updates will stay as work in progress (you will see them listed in your  Changes Tab).

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Transaction Type

Arguments

Type

Description

Create

`parentId`

`string`

The block ID to target, where the data will be injected

`data`

`Object`

The block values to be inserted, `type` is mandatory and will constraint the object type to the specific block schema

`type`

`”create”`

The transaction type

Delete

`id`

`string`

The block ID to delete

`type`

`”delete”`

The transaction type

Update

`data`

`Object`

Very similar to `create` data, but has an extra mandatory field `id` that maps to the existing block that will be updated

`type`

`”update”`

The transaction type

## Example

Check out our Mutation API Playground for full examples.

*   [Playground](https://mutation-api-playground.vercel.app/).
    
*   [Source](https://github.com/basehub-ai/mutations-api-example).
    
*   [Content](https://basehub.com/basehub/mutation-api-playground/explore).
    

## Create

When running the create transaction, you will need to pass two additional parameters: `parentId` and `data`.

The `parentId` is the ID from the block where the creation will be done, could be any block, but that will affect which data structures are valid. In the example above, using that specific `parentId` we cannot insert anything apart from instances, because collection children are always instances (or a component that works as template).

The `data` field is the new block schema and values, including all its children.