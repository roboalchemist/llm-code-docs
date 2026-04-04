# Source: https://docs.convex.dev/api/interfaces/server.GenericDatabaseWriter.md

# Interface: GenericDatabaseWriter\<DataModel>

[server](/api/modules/server.md).GenericDatabaseWriter

An interface to read from and write to the database within Convex mutation functions.

Convex guarantees that all writes within a single mutation are executed atomically, so you never have to worry about partial writes leaving your data in an inconsistent state. See [the Convex Guide](https://docs.convex.dev/understanding/convex-fundamentals/functions#atomicity-and-optimistic-concurrency-control) for the guarantees Convex provides your functions.

If you're using code generation, use the `DatabaseReader` type in `convex/_generated/server.d.ts` which is typed for your data model.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name        | Type                                                                  |
| ----------- | --------------------------------------------------------------------- |
| `DataModel` | extends [`GenericDataModel`](/api/modules/server.md#genericdatamodel) |

## Hierarchy[​](#hierarchy "Direct link to Hierarchy")

* [`GenericDatabaseReader`](/api/interfaces/server.GenericDatabaseReader.md)<`DataModel`>

  ↳ **`GenericDatabaseWriter`**

## Properties[​](#properties "Direct link to Properties")

### system[​](#system "Direct link to system")

• **system**: `BaseDatabaseReader`<[`SystemDataModel`](/api/interfaces/server.SystemDataModel.md)>

An interface to read from the system tables within Convex query functions

The two entry points are:

* [get](/api/interfaces/server.GenericDatabaseReader.md#get), which fetches a single document by its [GenericId](/api/modules/values.md#genericid).
* [query](/api/interfaces/server.GenericDatabaseReader.md#query), which starts building a query.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[GenericDatabaseReader](/api/interfaces/server.GenericDatabaseReader.md).[system](/api/interfaces/server.GenericDatabaseReader.md#system)

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/database.ts:128](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L128)

## Methods[​](#methods "Direct link to Methods")

### get[​](#get "Direct link to get")

▸ **get**<`TableName`>(`table`, `id`): `Promise`<`null` | [`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>>

Fetch a single document from the database by its [GenericId](/api/modules/values.md#genericid).

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters "Direct link to Parameters")

| Name    | Type                                                                     | Description                                                                                   |
| ------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `table` | `TableName`                                                              | The name of the table to fetch the document from.                                             |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`NonUnion`<`TableName`>> | The [GenericId](/api/modules/values.md#genericid) of the document to fetch from the database. |

#### Returns[​](#returns "Direct link to Returns")

`Promise`<`null` | [`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>>

* The [GenericDocument](/api/modules/server.md#genericdocument) of the document at the given [GenericId](/api/modules/values.md#genericid), or `null` if it no longer exists.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[GenericDatabaseReader](/api/interfaces/server.GenericDatabaseReader.md).[get](/api/interfaces/server.GenericDatabaseReader.md#get)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/database.ts:23](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L23)

▸ **get**<`TableName`>(`id`): `Promise`<`null` | [`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>>

Fetch a single document from the database by its [GenericId](/api/modules/values.md#genericid).

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name | Type                                                         | Description                                                                                   |
| ---- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `id` | [`GenericId`](/api/modules/values.md#genericid)<`TableName`> | The [GenericId](/api/modules/values.md#genericid) of the document to fetch from the database. |

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`null` | [`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>>

* The [GenericDocument](/api/modules/server.md#genericdocument) of the document at the given [GenericId](/api/modules/values.md#genericid), or `null` if it no longer exists.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[GenericDatabaseReader](/api/interfaces/server.GenericDatabaseReader.md).[get](/api/interfaces/server.GenericDatabaseReader.md#get)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/database.ts:34](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L34)

***

### query[​](#query "Direct link to query")

▸ **query**<`TableName`>(`tableName`): [`QueryInitializer`](/api/interfaces/server.QueryInitializer.md)<[`NamedTableInfo`](/api/modules/server.md#namedtableinfo)<`DataModel`, `TableName`>>

Begin a query for the given table name.

Queries don't execute immediately, so calling this method and extending its query are free until the results are actually used.

#### Type parameters[​](#type-parameters-3 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name        | Type        | Description                     |
| ----------- | ----------- | ------------------------------- |
| `tableName` | `TableName` | The name of the table to query. |

#### Returns[​](#returns-2 "Direct link to Returns")

[`QueryInitializer`](/api/interfaces/server.QueryInitializer.md)<[`NamedTableInfo`](/api/modules/server.md#namedtableinfo)<`DataModel`, `TableName`>>

* A [QueryInitializer](/api/interfaces/server.QueryInitializer.md) object to start building a query.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[GenericDatabaseReader](/api/interfaces/server.GenericDatabaseReader.md).[query](/api/interfaces/server.GenericDatabaseReader.md#query)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/database.ts:47](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L47)

***

### normalizeId[​](#normalizeid "Direct link to normalizeId")

▸ **normalizeId**<`TableName`>(`tableName`, `id`): `null` | [`GenericId`](/api/modules/values.md#genericid)<`TableName`>

Returns the string ID format for the ID in a given table, or null if the ID is from a different table or is not a valid ID.

This accepts the string ID format as well as the `.toString()` representation of the legacy class-based ID format.

This does not guarantee that the ID exists (i.e. `db.get(id)` may return `null`).

#### Type parameters[​](#type-parameters-4 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Name        | Type        | Description            |
| ----------- | ----------- | ---------------------- |
| `tableName` | `TableName` | The name of the table. |
| `id`        | `string`    | The ID string.         |

#### Returns[​](#returns-3 "Direct link to Returns")

`null` | [`GenericId`](/api/modules/values.md#genericid)<`TableName`>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[GenericDatabaseReader](/api/interfaces/server.GenericDatabaseReader.md).[normalizeId](/api/interfaces/server.GenericDatabaseReader.md#normalizeid)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/database.ts:63](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L63)

***

### insert[​](#insert "Direct link to insert")

▸ **insert**<`TableName`>(`table`, `value`): `Promise`<[`GenericId`](/api/modules/values.md#genericid)<`TableName`>>

Insert a new document into a table.

#### Type parameters[​](#type-parameters-5 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Name    | Type                                                                                                                                                     | Description                                                               |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `table` | `TableName`                                                                                                                                              | The name of the table to insert a new document into.                      |
| `value` | [`WithoutSystemFields`](/api/modules/server.md#withoutsystemfields)<[`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>> | The [Value](/api/modules/values.md#value) to insert into the given table. |

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`GenericId`](/api/modules/values.md#genericid)<`TableName`>>

* [GenericId](/api/modules/values.md#genericid) of the new document.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/database.ts:170](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L170)

***

### patch[​](#patch "Direct link to patch")

▸ **patch**<`TableName`>(`table`, `id`, `value`): `Promise`<`void`>

Patch an existing document, shallow merging it with the given partial document.

New fields are added. Existing fields are overwritten. Fields set to `undefined` are removed.

#### Type parameters[​](#type-parameters-6 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Name    | Type                                                                                              | Description                                                                                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `table` | `TableName`                                                                                       | The name of the table the document is in.                                                                                                                                                                               |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`NonUnion`<`TableName`>>                          | The [GenericId](/api/modules/values.md#genericid) of the document to patch.                                                                                                                                             |
| `value` | `PatchValue`<[`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>> | The partial [GenericDocument](/api/modules/server.md#genericdocument) to merge into the specified document. If this new value specifies system fields like `_id`, they must match the document's existing field values. |

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/database.ts:187](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L187)

▸ **patch**<`TableName`>(`id`, `value`): `Promise`<`void`>

Patch an existing document, shallow merging it with the given partial document.

New fields are added. Existing fields are overwritten. Fields set to `undefined` are removed.

#### Type parameters[​](#type-parameters-7 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-6 "Direct link to Parameters")

| Name    | Type                                                                                              | Description                                                                                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`TableName`>                                      | The [GenericId](/api/modules/values.md#genericid) of the document to patch.                                                                                                                                             |
| `value` | `PatchValue`<[`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>> | The partial [GenericDocument](/api/modules/server.md#genericdocument) to merge into the specified document. If this new value specifies system fields like `_id`, they must match the document's existing field values. |

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[server/database.ts:204](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L204)

***

### replace[​](#replace "Direct link to replace")

▸ **replace**<`TableName`>(`table`, `id`, `value`): `Promise`<`void`>

Replace the value of an existing document, overwriting its old value.

#### Type parameters[​](#type-parameters-8 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-7 "Direct link to Parameters")

| Name    | Type                                                                                                                                                               | Description                                                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `table` | `TableName`                                                                                                                                                        | The name of the table the document is in.                                                                                                                      |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`NonUnion`<`TableName`>>                                                                                           | The [GenericId](/api/modules/values.md#genericid) of the document to replace.                                                                                  |
| `value` | [`WithOptionalSystemFields`](/api/modules/server.md#withoptionalsystemfields)<[`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>> | The new [GenericDocument](/api/modules/server.md#genericdocument) for the document. This value can omit the system fields, and the database will fill them in. |

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[server/database.ts:217](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L217)

▸ **replace**<`TableName`>(`id`, `value`): `Promise`<`void`>

Replace the value of an existing document, overwriting its old value.

#### Type parameters[​](#type-parameters-9 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-8 "Direct link to Parameters")

| Name    | Type                                                                                                                                                               | Description                                                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`TableName`>                                                                                                       | The [GenericId](/api/modules/values.md#genericid) of the document to replace.                                                                                  |
| `value` | [`WithOptionalSystemFields`](/api/modules/server.md#withoptionalsystemfields)<[`DocumentByName`](/api/modules/server.md#documentbyname)<`DataModel`, `TableName`>> | The new [GenericDocument](/api/modules/server.md#genericdocument) for the document. This value can omit the system fields, and the database will fill them in. |

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[server/database.ts:230](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L230)

***

### delete[​](#delete "Direct link to delete")

▸ **delete**<`TableName`>(`table`, `id`): `Promise`<`void`>

Delete an existing document.

#### Type parameters[​](#type-parameters-10 "Direct link to Type parameters")

| Name        | Type             |
| ----------- | ---------------- |
| `TableName` | extends `string` |

#### Parameters[​](#parameters-9 "Direct link to Parameters")

| Name    | Type                                                                     | Description                                                                  |
| ------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `table` | `TableName`                                                              | The name of the table the document is in.                                    |
| `id`    | [`GenericId`](/api/modules/values.md#genericid)<`NonUnion`<`TableName`>> | The [GenericId](/api/modules/values.md#genericid) of the document to remove. |

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[server/database.ts:241](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L241)

▸ **delete**(`id`): `Promise`<`void`>

Delete an existing document.

#### Parameters[​](#parameters-10 "Direct link to Parameters")

| Name | Type                                                                                                                                  | Description                                                                  |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id` | [`GenericId`](/api/modules/values.md#genericid)<[`TableNamesInDataModel`](/api/modules/server.md#tablenamesindatamodel)<`DataModel`>> | The [GenericId](/api/modules/values.md#genericid) of the document to remove. |

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[server/database.ts:251](https://github.com/get-convex/convex-js/blob/main/src/server/database.ts#L251)
