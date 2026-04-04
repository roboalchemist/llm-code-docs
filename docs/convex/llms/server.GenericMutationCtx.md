# Source: https://docs.convex.dev/api/interfaces/server.GenericMutationCtx.md

# Interface: GenericMutationCtx\<DataModel>

[server](/api/modules/server.md).GenericMutationCtx

A set of services for use within Convex mutation functions.

The mutation context is passed as the first argument to any Convex mutation function run on the server.

If you're using code generation, use the `MutationCtx` type in `convex/_generated/server.d.ts` which is typed for your data model.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name        | Type                                                                  |
| ----------- | --------------------------------------------------------------------- |
| `DataModel` | extends [`GenericDataModel`](/api/modules/server.md#genericdatamodel) |

## Properties[​](#properties "Direct link to Properties")

### db[​](#db "Direct link to db")

• **db**: [`GenericDatabaseWriter`](/api/interfaces/server.GenericDatabaseWriter.md)<`DataModel`>

A utility for reading and writing data in the database.

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/registration.ts:50](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L50)

***

### auth[​](#auth "Direct link to auth")

• **auth**: [`Auth`](/api/interfaces/server.Auth.md)

Information about the currently authenticated user.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/registration.ts:55](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L55)

***

### storage[​](#storage "Direct link to storage")

• **storage**: [`StorageWriter`](/api/interfaces/server.StorageWriter.md)

A utility for reading and writing files in storage.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/registration.ts:60](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L60)

***

### scheduler[​](#scheduler "Direct link to scheduler")

• **scheduler**: [`Scheduler`](/api/interfaces/server.Scheduler.md)

A utility for scheduling Convex functions to run in the future.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/registration.ts:65](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L65)

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

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/registration.ts:74](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L74)

***

### runMutation[​](#runmutation "Direct link to runMutation")

• **runMutation**: \<Mutation>(`mutation`: `Mutation`, ...`args`: [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`Mutation`>) => `Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Mutation`>>

#### Type declaration[​](#type-declaration-1 "Direct link to Type declaration")

▸ <`Mutation`>(`mutation`, `...args`): `Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Mutation`>>

Call a mutation function within the same transaction.

NOTE: often you can call the mutation's function directly instead of using this. `runMutation` incurs overhead of running argument and return value validation, and creating a new isolated JS context.

The mutation runs in a sub-transaction, so if the mutation throws an error, all of its writes will be rolled back. Additionally, a successful mutation's writes will be serializable with other writes in the transaction.

##### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

| Name       | Type                                                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------------- |
| `Mutation` | extends [`FunctionReference`](/api/modules/server.md#functionreference)<`"mutation"`, `"public"` \| `"internal"`> |

##### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name       | Type                                                                      |
| ---------- | ------------------------------------------------------------------------- |
| `mutation` | `Mutation`                                                                |
| `...args`  | [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`Mutation`> |

##### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Mutation`>>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/registration.ts:90](https://github.com/get-convex/convex-js/blob/main/src/server/registration.ts#L90)
