# Source: https://docs.convex.dev/api/interfaces/server.PaginationOptions.md

# Interface: PaginationOptions

[server](/api/modules/server.md).PaginationOptions

The options passed to [paginate](/api/interfaces/server.OrderedQuery.md#paginate).

To use this type in [argument validation](https://docs.convex.dev/functions/validation), use the [paginationOptsValidator](/api/modules/server.md#paginationoptsvalidator).

## Properties[​](#properties "Direct link to Properties")

### numItems[​](#numitems "Direct link to numItems")

• **numItems**: `number`

Number of items to load in this page of results.

Note: This is only an initial value!

If you are running this paginated query in a reactive query function, you may receive more or less items than this if items were added to or removed from the query range.

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/pagination.ts:78](https://github.com/get-convex/convex-js/blob/main/src/server/pagination.ts#L78)

***

### cursor[​](#cursor "Direct link to cursor")

• **cursor**: `null` | `string`

A [Cursor](/api/modules/server.md#cursor) representing the start of this page or `null` to start at the beginning of the query results.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/pagination.ts:84](https://github.com/get-convex/convex-js/blob/main/src/server/pagination.ts#L84)
