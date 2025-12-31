# Source: https://docs.convex.dev/api/interfaces/server.QueryInitializer.md

# Interface: QueryInitializer\<TableInfo>

[server](/api/modules/server.md).QueryInitializer

The [QueryInitializer](/api/interfaces/server.QueryInitializer.md) interface is the entry point for building a [Query](/api/interfaces/server.Query.md) over a Convex database table.

There are two types of queries:

1. Full table scans: Queries created with [fullTableScan](/api/interfaces/server.QueryInitializer.md#fulltablescan) which iterate over all of the documents in the table in insertion order.
2. Indexed Queries: Queries created with [withIndex](/api/interfaces/server.QueryInitializer.md#withindex) which iterate over an index range in index order.

For convenience, [QueryInitializer](/api/interfaces/server.QueryInitializer.md) extends the [Query](/api/interfaces/server.Query.md) interface, implicitly starting a full table scan.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name        | Type                                                                  |
| ----------- | --------------------------------------------------------------------- |
| `TableInfo` | extends [`GenericTableInfo`](/api/modules/server.md#generictableinfo) |

## Hierarchy[​](#hierarchy "Direct link to Hierarchy")

* [`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

  ↳ **`QueryInitializer`**

## Methods[​](#methods "Direct link to Methods")

### \[asyncIterator][​](#asynciterator "Direct link to \[asyncIterator]")

▸ **\[asyncIterator]**(): `AsyncIterator`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, `any`, `undefined`>

#### Returns[​](#returns "Direct link to Returns")

`AsyncIterator`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, `any`, `undefined`>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[\[asyncIterator\]](/api/interfaces/server.Query.md#%5Basynciterator%5D)

#### Defined in[​](#defined-in "Direct link to Defined in")

../../common/temp/node\_modules/.pnpm/typescript\@5.0.4/node\_modules/typescript/lib/lib.es2018.asynciterable.d.ts:38

***

### fullTableScan[​](#fulltablescan "Direct link to fullTableScan")

▸ **fullTableScan**(): [`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

Query by reading all of the values out of this table.

This query's cost is relative to the size of the entire table, so this should only be used on tables that will stay very small (say between a few hundred and a few thousand documents) and are updated infrequently.

#### Returns[​](#returns-1 "Direct link to Returns")

[`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

* The [Query](/api/interfaces/server.Query.md) that iterates over every document of the table.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/query.ts:40](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L40)

***

### withIndex[​](#withindex "Direct link to withIndex")

▸ **withIndex**<`IndexName`>(`indexName`, `indexRange?`): [`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

Query by reading documents from an index on this table.

This query's cost is relative to the number of documents that match the index range expression.

Results will be returned in index order.

To learn about indexes, see [Indexes](https://docs.convex.dev/using/indexes).

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name        | Type                                     |
| ----------- | ---------------------------------------- |
| `IndexName` | extends `string` \| `number` \| `symbol` |

#### Parameters[​](#parameters "Direct link to Parameters")

| Name          | Type                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                 |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `indexName`   | `IndexName`                                                                                                                                                                                                                                                                              | The name of the index to query.                                                                                                                                                                                                                                                                             |
| `indexRange?` | (`q`: [`IndexRangeBuilder`](/api/interfaces/server.IndexRangeBuilder.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, [`NamedIndex`](/api/modules/server.md#namedindex)<`TableInfo`, `IndexName`>, `0`>) => [`IndexRange`](/api/classes/server.IndexRange.md) | An optional index range constructed with the supplied [IndexRangeBuilder](/api/interfaces/server.IndexRangeBuilder.md). An index range is a description of which documents Convex should consider when running the query. If no index range is present, the query will consider all documents in the index. |

#### Returns[​](#returns-2 "Direct link to Returns")

[`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

* The query that yields documents in the index.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/query.ts:59](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L59)

***

### withSearchIndex[​](#withsearchindex "Direct link to withSearchIndex")

▸ **withSearchIndex**<`IndexName`>(`indexName`, `searchFilter`): [`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

Query by running a full text search against a search index.

Search queries must always search for some text within the index's `searchField`. This query can optionally add equality filters for any `filterFields` specified in the index.

Documents will be returned in relevance order based on how well they match the search text.

To learn about full text search, see [Indexes](https://docs.convex.dev/text-search).

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

| Name        | Type                                     |
| ----------- | ---------------------------------------- |
| `IndexName` | extends `string` \| `number` \| `symbol` |

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name           | Type                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `indexName`    | `IndexName`                                                                                                                                                                                                                                                                                             | The name of the search index to query.                                                                                                                                                                                                |
| `searchFilter` | (`q`: [`SearchFilterBuilder`](/api/interfaces/server.SearchFilterBuilder.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, [`NamedSearchIndex`](/api/modules/server.md#namedsearchindex)<`TableInfo`, `IndexName`>>) => [`SearchFilter`](/api/classes/server.SearchFilter.md) | A search filter expression constructed with the supplied [SearchFilterBuilder](/api/interfaces/server.SearchFilterBuilder.md). This defines the full text search to run along with equality filtering to run within the search index. |

#### Returns[​](#returns-3 "Direct link to Returns")

[`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

* A query that searches for matching documents, returning them in relevancy order.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/query.ts:88](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L88)

***

### order[​](#order "Direct link to order")

▸ **order**(`order`): [`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

Define the order of the query output.

Use `"asc"` for an ascending order and `"desc"` for a descending order. If not specified, the order defaults to ascending.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name    | Type                | Description                     |
| ------- | ------------------- | ------------------------------- |
| `order` | `"asc"` \| `"desc"` | The order to return results in. |

#### Returns[​](#returns-4 "Direct link to Returns")

[`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[order](/api/interfaces/server.Query.md#order)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/query.ts:149](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L149)

***

### filter[​](#filter "Direct link to filter")

▸ **filter**(`predicate`): [`QueryInitializer`](/api/interfaces/server.QueryInitializer.md)<`TableInfo`>

Filter the query output, returning only the values for which `predicate` evaluates to true.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Name        | Type                                                                                                                                                         | Description                                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `predicate` | (`q`: [`FilterBuilder`](/api/interfaces/server.FilterBuilder.md)<`TableInfo`>) => [`ExpressionOrValue`](/api/modules/server.md#expressionorvalue)<`boolean`> | An [Expression](/api/classes/server.Expression.md) constructed with the supplied [FilterBuilder](/api/interfaces/server.FilterBuilder.md) that specifies which documents to keep. |

#### Returns[​](#returns-5 "Direct link to Returns")

[`QueryInitializer`](/api/interfaces/server.QueryInitializer.md)<`TableInfo`>

* A new [OrderedQuery](/api/interfaces/server.OrderedQuery.md) with the given filter predicate applied.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[filter](/api/interfaces/server.Query.md#filter)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/query.ts:165](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L165)

***

### paginate[​](#paginate "Direct link to paginate")

▸ **paginate**(`paginationOpts`): `Promise`<[`PaginationResult`](/api/interfaces/server.PaginationResult.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>>

Load a page of `n` results and obtain a [Cursor](/api/modules/server.md#cursor) for loading more.

Note: If this is called from a reactive query function the number of results may not match `paginationOpts.numItems`!

`paginationOpts.numItems` is only an initial value. After the first invocation, `paginate` will return all items in the original query range. This ensures that all pages will remain adjacent and non-overlapping.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Name             | Type                                                               | Description                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `paginationOpts` | [`PaginationOptions`](/api/interfaces/server.PaginationOptions.md) | A [PaginationOptions](/api/interfaces/server.PaginationOptions.md) object containing the number of items to load and the cursor to start at. |

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`PaginationResult`](/api/interfaces/server.PaginationResult.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>>

A [PaginationResult](/api/interfaces/server.PaginationResult.md) containing the page of results and a cursor to continue paginating.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[paginate](/api/interfaces/server.Query.md#paginate)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/query.ts:194](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L194)

***

### collect[​](#collect "Direct link to collect")

▸ **collect**(): `Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

Execute the query and return all of the results as an array.

Note: when processing a query with a lot of results, it's often better to use the `Query` as an `AsyncIterable` instead.

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

* An array of all of the query's results.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[collect](/api/interfaces/server.Query.md#collect)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[server/query.ts:206](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L206)

***

### take[​](#take "Direct link to take")

▸ **take**(`n`): `Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

Execute the query and return the first `n` results.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Name | Type     | Description                  |
| ---- | -------- | ---------------------------- |
| `n`  | `number` | The number of items to take. |

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

* An array of the first `n` results of the query (or less if the query doesn't have `n` results).

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[take](/api/interfaces/server.Query.md#take)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[server/query.ts:215](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L215)

***

### first[​](#first "Direct link to first")

▸ **first**(): `Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

Execute the query and return the first result if there is one.

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

* The first value of the query or `null` if the query returned no results.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[first](/api/interfaces/server.Query.md#first)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[server/query.ts:222](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L222)

***

### unique[​](#unique "Direct link to unique")

▸ **unique**(): `Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

Execute the query and return the singular result if there is one.

**`Throws`**

Will throw an error if the query returns more than one result.

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

* The single result returned from the query or null if none exists.

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[Query](/api/interfaces/server.Query.md).[unique](/api/interfaces/server.Query.md#unique)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[server/query.ts:230](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L230)
