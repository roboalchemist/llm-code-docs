# Source: https://docs.convex.dev/api/interfaces/server.GenericQueryCtx.md

# Interface: GenericQueryCtx\<DataModel>

[server](/api/modules/server.md).GenericQueryCtx

A set of services for use within Convex query functions.

The query context is passed as the first argument to any Convex query function run on the server.

This differs from the MutationCtx because all of the services are read-only.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name        | Type                                                                  |
| ----------- | --------------------------------------------------------------------- |
| `DataModel` | extends [`GenericDataModel`](/api/modules/server.md#genericdatamodel) |

## Properties[​](#properties "Direct link to Properties")

### db[​](#db "Direct link to db")

• **db**: [`GenericDatabaseReader`](/api/interfaces/server.GenericDatabaseReader.md)<`DataModel`>

A utility for reading data in the database.

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/registration.ts:130](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L130)

***

### auth[​](#auth "Direct link to auth")

• **auth**: [`Auth`](/api/interfaces/server.Auth.md)

Information about the currently authenticated user.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/registration.ts:135](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L135)

***

### storage[​](#storage "Direct link to storage")

• **storage**: [`StorageReader`](/api/interfaces/server.StorageReader.md)

A utility for reading files in storage.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/registration.ts:140](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L140)

***

### runQuery[​](#runquery "Direct link to runQuery")

• **runQuery**: \<Query>(`query`: `Query`, ...`args`: [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`Query`>) => `Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Query`>>

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

▸ <`Query`>(`query`, `...args`): `Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Query`>>

Call a query function within the same transaction.

NOTE: often you can call the query's function directly instead of using this. `runQuery` incurs overhead of running argument and return value validation, and creating a new isolated JS context.

##### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name    | Type                                                                                                           |
| ------- | -------------------------------------------------------------------------------------------------------------- |
| `Query` | extends [`FunctionReference`](/api/modules/server.md#functionreference)<`"query"`, `"public"` \| `"internal"`> |

##### Parameters[​](#parameters "Direct link to Parameters")

| Name      | Type                                                                   |
| --------- | ---------------------------------------------------------------------- |
| `query`   | `Query`                                                                |
| `...args` | [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`Query`> |

##### Returns[​](#returns "Direct link to Returns")

`Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Query`>>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/registration.ts:149](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L149)
