# Source: https://docs.convex.dev/api/classes/server.TableDefinition.md

# Class: TableDefinition\<DocumentType, Indexes, SearchIndexes, VectorIndexes>

[server](/api/modules/server.md).TableDefinition

The definition of a table within a schema.

This should be produced by using [defineTable](/api/modules/server.md#definetable).

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name            | Type                                                                                                                                                |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DocumentType`  | extends [`Validator`](/api/modules/values.md#validator)<`any`, `any`, `any`> = [`Validator`](/api/modules/values.md#validator)<`any`, `any`, `any`> |
| `Indexes`       | extends [`GenericTableIndexes`](/api/modules/server.md#generictableindexes) =                                                                       |
| `SearchIndexes` | extends [`GenericTableSearchIndexes`](/api/modules/server.md#generictablesearchindexes) =                                                           |
| `VectorIndexes` | extends [`GenericTableVectorIndexes`](/api/modules/server.md#generictablevectorindexes) =                                                           |

## Properties[​](#properties "Direct link to Properties")

### validator[​](#validator "Direct link to validator")

• **validator**: `DocumentType`

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/schema.ts:199](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L199)

## Methods[​](#methods "Direct link to Methods")

### indexes[​](#indexes "Direct link to indexes")

▸ \*\* indexes\*\*(): { `indexDescriptor`: `string` ; `fields`: `string`\[] }\[]

This API is experimental: it may change or disappear.

Returns indexes defined on this table. Intended for the advanced use cases of dynamically deciding which index to use for a query. If you think you need this, please chime in on ths issue in the Convex JS GitHub repo. <https://github.com/get-convex/convex-js/issues/49>

#### Returns[​](#returns "Direct link to Returns")

{ `indexDescriptor`: `string` ; `fields`: `string`\[] }\[]

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/schema.ts:222](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L222)

***

### index[​](#index "Direct link to index")

▸ **index**<`IndexName`, `FirstFieldPath`, `RestFieldPaths`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, [`Expand`](/api/modules/server.md#expand)<`Indexes` & `Record`<`IndexName`, \[`FirstFieldPath`, ...RestFieldPaths\[], `"_creationTime"`]>>, `SearchIndexes`, `VectorIndexes`>

Define an index on this table.

To learn about indexes, see [Defining Indexes](https://docs.convex.dev/using/indexes).

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name             | Type                                           |
| ---------------- | ---------------------------------------------- |
| `IndexName`      | extends `string`                               |
| `FirstFieldPath` | extends `any`                                  |
| `RestFieldPaths` | extends `ExtractFieldPaths`<`DocumentType`>\[] |

#### Parameters[​](#parameters "Direct link to Parameters")

| Name                  | Type                                      | Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                | `IndexName`                               | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`         | `Object`                                  | The index configuration object.                                                                                                                                                                                                                                                                                                                               |
| `indexConfig.fields`  | \[`FirstFieldPath`, ...RestFieldPaths\[]] | The fields to index, in order. Must specify at least one field.                                                                                                                                                                                                                                                                                               |
| `indexConfig.staged?` | `false`                                   | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-1 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, [`Expand`](/api/modules/server.md#expand)<`Indexes` & `Record`<`IndexName`, \[`FirstFieldPath`, ...RestFieldPaths\[], `"_creationTime"`]>>, `SearchIndexes`, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this index included.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/schema.ts:235](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L235)

▸ **index**<`IndexName`, `FirstFieldPath`, `RestFieldPaths`>(`name`, `fields`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, [`Expand`](/api/modules/server.md#expand)<`Indexes` & `Record`<`IndexName`, \[`FirstFieldPath`, ...RestFieldPaths\[], `"_creationTime"`]>>, `SearchIndexes`, `VectorIndexes`>

Define an index on this table.

To learn about indexes, see [Defining Indexes](https://docs.convex.dev/using/indexes).

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

| Name             | Type                                           |
| ---------------- | ---------------------------------------------- |
| `IndexName`      | extends `string`                               |
| `FirstFieldPath` | extends `any`                                  |
| `RestFieldPaths` | extends `ExtractFieldPaths`<`DocumentType`>\[] |

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name     | Type                                      | Description                                                     |
| -------- | ----------------------------------------- | --------------------------------------------------------------- |
| `name`   | `IndexName`                               | The name of the index.                                          |
| `fields` | \[`FirstFieldPath`, ...RestFieldPaths\[]] | The fields to index, in order. Must specify at least one field. |

#### Returns[​](#returns-2 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, [`Expand`](/api/modules/server.md#expand)<`Indexes` & `Record`<`IndexName`, \[`FirstFieldPath`, ...RestFieldPaths\[], `"_creationTime"`]>>, `SearchIndexes`, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this index included.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/schema.ts:268](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L268)

▸ **index**<`IndexName`, `FirstFieldPath`, `RestFieldPaths`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

Define a staged index on this table.

For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later.

If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries.

To learn about indexes, see [Defining Indexes](https://docs.convex.dev/using/indexes).

#### Type parameters[​](#type-parameters-3 "Direct link to Type parameters")

| Name             | Type                                           |
| ---------------- | ---------------------------------------------- |
| `IndexName`      | extends `string`                               |
| `FirstFieldPath` | extends `any`                                  |
| `RestFieldPaths` | extends `ExtractFieldPaths`<`DocumentType`>\[] |

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name                 | Type                                      | Description                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`               | `IndexName`                               | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`        | `Object`                                  | The index configuration object.                                                                                                                                                                                                                                                                                                                               |
| `indexConfig.fields` | \[`FirstFieldPath`, ...RestFieldPaths\[]] | The fields to index, in order. Must specify at least one field.                                                                                                                                                                                                                                                                                               |
| `indexConfig.staged` | `true`                                    | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-3 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this index included.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/schema.ts:304](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L304)

***

### searchIndex[​](#searchindex "Direct link to searchIndex")

▸ **searchIndex**<`IndexName`, `SearchField`, `FilterFields`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, [`Expand`](/api/modules/server.md#expand)<`SearchIndexes` & `Record`<`IndexName`, { `searchField`: `SearchField` ; `filterFields`: `FilterFields` }>>, `VectorIndexes`>

Define a search index on this table.

To learn about search indexes, see [Search](https://docs.convex.dev/text-search).

#### Type parameters[​](#type-parameters-4 "Direct link to Type parameters")

| Name           | Type                    |
| -------------- | ----------------------- |
| `IndexName`    | extends `string`        |
| `SearchField`  | extends `any`           |
| `FilterFields` | extends `any` = `never` |

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Name                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                      | `IndexName`       | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`               | `Object`          | The search index configuration object.                                                                                                                                                                                                                                                                                                                        |
| `indexConfig.searchField`   | `SearchField`     | The field to index for full text search. This must be a field of type `string`.                                                                                                                                                                                                                                                                               |
| `indexConfig.filterFields?` | `FilterFields`\[] | Additional fields to index for fast filtering when running search queries.                                                                                                                                                                                                                                                                                    |
| `indexConfig.staged?`       | `false`           | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-4 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, [`Expand`](/api/modules/server.md#expand)<`SearchIndexes` & `Record`<`IndexName`, { `searchField`: `SearchField` ; `filterFields`: `FilterFields` }>>, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this search index included.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/schema.ts:357](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L357)

▸ **searchIndex**<`IndexName`, `SearchField`, `FilterFields`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

Define a staged search index on this table.

For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later.

If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries.

To learn about search indexes, see [Search](https://docs.convex.dev/text-search).

#### Type parameters[​](#type-parameters-5 "Direct link to Type parameters")

| Name           | Type                    |
| -------------- | ----------------------- |
| `IndexName`    | extends `string`        |
| `SearchField`  | extends `any`           |
| `FilterFields` | extends `any` = `never` |

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Name                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                      | `IndexName`       | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`               | `Object`          | The search index configuration object.                                                                                                                                                                                                                                                                                                                        |
| `indexConfig.searchField`   | `SearchField`     | The field to index for full text search. This must be a field of type `string`.                                                                                                                                                                                                                                                                               |
| `indexConfig.filterFields?` | `FilterFields`\[] | Additional fields to index for fast filtering when running search queries.                                                                                                                                                                                                                                                                                    |
| `indexConfig.staged`        | `true`            | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-5 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this search index included.

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/schema.ts:401](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L401)

***

### vectorIndex[​](#vectorindex "Direct link to vectorIndex")

▸ **vectorIndex**<`IndexName`, `VectorField`, `FilterFields`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, [`Expand`](/api/modules/server.md#expand)<`VectorIndexes` & `Record`<`IndexName`, { `vectorField`: `VectorField` ; `dimensions`: `number` ; `filterFields`: `FilterFields` }>>>

Define a vector index on this table.

To learn about vector indexes, see [Vector Search](https://docs.convex.dev/vector-search).

#### Type parameters[​](#type-parameters-6 "Direct link to Type parameters")

| Name           | Type                    |
| -------------- | ----------------------- |
| `IndexName`    | extends `string`        |
| `VectorField`  | extends `any`           |
| `FilterFields` | extends `any` = `never` |

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Name                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                      | `IndexName`       | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`               | `Object`          | The vector index configuration object.                                                                                                                                                                                                                                                                                                                        |
| `indexConfig.vectorField`   | `VectorField`     | The field to index for vector search. This must be a field of type `v.array(v.float64())` (or a union)                                                                                                                                                                                                                                                        |
| `indexConfig.dimensions`    | `number`          | The length of the vectors indexed. This must be between 2 and 2048 inclusive.                                                                                                                                                                                                                                                                                 |
| `indexConfig.filterFields?` | `FilterFields`\[] | Additional fields to index for fast filtering when running vector searches.                                                                                                                                                                                                                                                                                   |
| `indexConfig.staged?`       | `false`           | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-6 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, [`Expand`](/api/modules/server.md#expand)<`VectorIndexes` & `Record`<`IndexName`, { `vectorField`: `VectorField` ; `dimensions`: `number` ; `filterFields`: `FilterFields` }>>>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this vector index included.

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[server/schema.ts:448](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L448)

▸ **vectorIndex**<`IndexName`, `VectorField`, `FilterFields`>(`name`, `indexConfig`): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

Define a staged vector index on this table.

For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later.

If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries.

To learn about vector indexes, see [Vector Search](https://docs.convex.dev/vector-search).

#### Type parameters[​](#type-parameters-7 "Direct link to Type parameters")

| Name           | Type                    |
| -------------- | ----------------------- |
| `IndexName`    | extends `string`        |
| `VectorField`  | extends `any`           |
| `FilterFields` | extends `any` = `never` |

#### Parameters[​](#parameters-6 "Direct link to Parameters")

| Name                        | Type              | Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                      | `IndexName`       | The name of the index.                                                                                                                                                                                                                                                                                                                                        |
| `indexConfig`               | `Object`          | The vector index configuration object.                                                                                                                                                                                                                                                                                                                        |
| `indexConfig.vectorField`   | `VectorField`     | The field to index for vector search. This must be a field of type `v.array(v.float64())` (or a union)                                                                                                                                                                                                                                                        |
| `indexConfig.dimensions`    | `number`          | The length of the vectors indexed. This must be between 2 and 2048 inclusive.                                                                                                                                                                                                                                                                                 |
| `indexConfig.filterFields?` | `FilterFields`\[] | Additional fields to index for fast filtering when running vector searches.                                                                                                                                                                                                                                                                                   |
| `indexConfig.staged`        | `true`            | Whether the index should be staged. For large tables, index backfill can be slow. Staging an index allows you to push the schema and enable the index later. If `staged` is `true`, the index will be staged and will not be enabled until the staged flag is removed. Staged indexes do not block push completion. Staged indexes cannot be used in queries. |

#### Returns[​](#returns-7 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

A [TableDefinition](/api/classes/server.TableDefinition.md) with this vector index included.

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[server/schema.ts:491](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L491)

***

### self[​](#self "Direct link to self")

▸ `Protected` **self**(): [`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

Work around for <https://github.com/microsoft/TypeScript/issues/57035>

#### Returns[​](#returns-8 "Direct link to Returns")

[`TableDefinition`](/api/classes/server.TableDefinition.md)<`DocumentType`, `Indexes`, `SearchIndexes`, `VectorIndexes`>

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[server/schema.ts:534](https://github.com/get-convex/convex-js/blob/main/src/server/schema.ts#L534)
