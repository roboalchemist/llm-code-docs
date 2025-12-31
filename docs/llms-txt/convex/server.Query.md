# Source: https://docs.convex.dev/api/interfaces/server.Query.md

# Interface: Query\<TableInfo>

[server](/api/modules/server.md).Query

The [Query](/api/interfaces/server.Query.md) interface allows functions to read values out of the database.

**If you only need to load an object by ID, use `db.get(id)` instead.**

Executing a query consists of calling

1. (Optional) [order](/api/interfaces/server.Query.md#order) to define the order
2. (Optional) [filter](/api/interfaces/server.OrderedQuery.md#filter) to refine the results
3. A *consumer* method to obtain the results

Queries are lazily evaluated. No work is done until iteration begins, so constructing and extending a query is free. The query is executed incrementally as the results are iterated over, so early terminating also reduces the cost of the query.

It is more efficient to use `filter` expression rather than executing JavaScript to filter.

|                                              |                                                                        |
| -------------------------------------------- | ---------------------------------------------------------------------- |
| **Ordering**                                 |                                                                        |
| [`order("asc")`](#order)                     | Define the order of query results.                                     |
|                                              |                                                                        |
| **Filtering**                                |                                                                        |
| [`filter(...)`](#filter)                     | Filter the query results to only the values that match some condition. |
|                                              |                                                                        |
| **Consuming**                                | Execute a query and return results in different ways.                  |
| [`[Symbol.asyncIterator]()`](#asynciterator) | The query's results can be iterated over using a `for await..of` loop. |
| [`collect()`](#collect)                      | Return all of the results as an array.                                 |
| [`take(n: number)`](#take)                   | Return the first `n` results as an array.                              |
| [`first()`](#first)                          | Return the first result.                                               |
| [`unique()`](#unique)                        | Return the only result, and throw if there is more than one result.    |

To learn more about how to write queries, see [Querying the Database](https://docs.convex.dev/using/database-queries).

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name        | Type                                                                  |
| ----------- | --------------------------------------------------------------------- |
| `TableInfo` | extends [`GenericTableInfo`](/api/modules/server.md#generictableinfo) |

## Hierarchy[​](#hierarchy "Direct link to Hierarchy")

* [`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

  ↳ **`Query`**

  ↳↳ [`QueryInitializer`](/api/interfaces/server.QueryInitializer.md)

## Methods[​](#methods "Direct link to Methods")

### \[asyncIterator][​](#asynciterator "Direct link to \[asyncIterator]")

▸ **\[asyncIterator]**(): `AsyncIterator`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, `any`, `undefined`>

#### Returns[​](#returns "Direct link to Returns")

`AsyncIterator`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>, `any`, `undefined`>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[\[asyncIterator\]](/api/interfaces/server.OrderedQuery.md#%5Basynciterator%5D)

#### Defined in[​](#defined-in "Direct link to Defined in")

../../common/temp/node\_modules/.pnpm/typescript\@5.0.4/node\_modules/typescript/lib/lib.es2018.asynciterable.d.ts:38

***

### order[​](#order "Direct link to order")

▸ **order**(`order`): [`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

Define the order of the query output.

Use `"asc"` for an ascending order and `"desc"` for a descending order. If not specified, the order defaults to ascending.

#### Parameters[​](#parameters "Direct link to Parameters")

| Name    | Type                | Description                     |
| ------- | ------------------- | ------------------------------- |
| `order` | `"asc"` \| `"desc"` | The order to return results in. |

#### Returns[​](#returns-1 "Direct link to Returns")

[`OrderedQuery`](/api/interfaces/server.OrderedQuery.md)<`TableInfo`>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/query.ts:149](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L149)

***

### filter[​](#filter "Direct link to filter")

▸ **filter**(`predicate`): [`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

Filter the query output, returning only the values for which `predicate` evaluates to true.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name        | Type                                                                                                                                                         | Description                                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `predicate` | (`q`: [`FilterBuilder`](/api/interfaces/server.FilterBuilder.md)<`TableInfo`>) => [`ExpressionOrValue`](/api/modules/server.md#expressionorvalue)<`boolean`> | An [Expression](/api/classes/server.Expression.md) constructed with the supplied [FilterBuilder](/api/interfaces/server.FilterBuilder.md) that specifies which documents to keep. |

#### Returns[​](#returns-2 "Direct link to Returns")

[`Query`](/api/interfaces/server.Query.md)<`TableInfo`>

* A new [OrderedQuery](/api/interfaces/server.OrderedQuery.md) with the given filter predicate applied.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[filter](/api/interfaces/server.OrderedQuery.md#filter)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/query.ts:165](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L165)

***

### paginate[​](#paginate "Direct link to paginate")

▸ **paginate**(`paginationOpts`): `Promise`<[`PaginationResult`](/api/interfaces/server.PaginationResult.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>>

Load a page of `n` results and obtain a [Cursor](/api/modules/server.md#cursor) for loading more.

Note: If this is called from a reactive query function the number of results may not match `paginationOpts.numItems`!

`paginationOpts.numItems` is only an initial value. After the first invocation, `paginate` will return all items in the original query range. This ensures that all pages will remain adjacent and non-overlapping.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name             | Type                                                               | Description                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `paginationOpts` | [`PaginationOptions`](/api/interfaces/server.PaginationOptions.md) | A [PaginationOptions](/api/interfaces/server.PaginationOptions.md) object containing the number of items to load and the cursor to start at. |

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<[`PaginationResult`](/api/interfaces/server.PaginationResult.md)<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>>

A [PaginationResult](/api/interfaces/server.PaginationResult.md) containing the page of results and a cursor to continue paginating.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[paginate](/api/interfaces/server.OrderedQuery.md#paginate)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/query.ts:194](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L194)

***

### collect[​](#collect "Direct link to collect")

▸ **collect**(): `Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

Execute the query and return all of the results as an array.

Note: when processing a query with a lot of results, it's often better to use the `Query` as an `AsyncIterable` instead.

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

* An array of all of the query's results.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[collect](/api/interfaces/server.OrderedQuery.md#collect)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/query.ts:206](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L206)

***

### take[​](#take "Direct link to take")

▸ **take**(`n`): `Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

Execute the query and return the first `n` results.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Name | Type     | Description                  |
| ---- | -------- | ---------------------------- |
| `n`  | `number` | The number of items to take. |

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<[`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>\[]>

* An array of the first `n` results of the query (or less if the query doesn't have `n` results).

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[take](/api/interfaces/server.OrderedQuery.md#take)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/query.ts:215](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L215)

***

### first[​](#first "Direct link to first")

▸ **first**(): `Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

Execute the query and return the first result if there is one.

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

* The first value of the query or `null` if the query returned no results.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[first](/api/interfaces/server.OrderedQuery.md#first)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/query.ts:222](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L222)

***

### unique[​](#unique "Direct link to unique")

▸ **unique**(): `Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

Execute the query and return the singular result if there is one.

**`Throws`**

Will throw an error if the query returns more than one result.

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`null` | [`DocumentByInfo`](/api/modules/server.md#documentbyinfo)<`TableInfo`>>

* The single result returned from the query or null if none exists.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[OrderedQuery](/api/interfaces/server.OrderedQuery.md).[unique](/api/interfaces/server.OrderedQuery.md#unique)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[server/query.ts:230](https://github.com/get-convex/convex-js/blob/main/src/server/query.ts#L230)
