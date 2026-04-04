# Source: https://docs.convex.dev/api/interfaces/server.Scheduler.md

# Interface: Scheduler

[server](/api/modules/server.md).Scheduler

An interface to schedule Convex functions.

You can schedule either mutations or actions. Mutations are guaranteed to execute exactly once - they are automatically retried on transient errors and either execute successfully or fail deterministically due to developer error in defining the function. Actions execute at most once - they are not retried and might fail due to transient errors.

Consider using an internalMutation or internalAction to enforce that these functions cannot be called directly from a Convex client.

## Methods[​](#methods "Direct link to Methods")

### runAfter[​](#runafter "Direct link to runAfter")

▸ **runAfter**<`FuncRef`>(`delayMs`, `functionReference`, `...args`): `Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_scheduled_functions"`>>

Schedule a function to execute after a delay.

#### Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name      | Type                                                                                          |
| --------- | --------------------------------------------------------------------------------------------- |
| `FuncRef` | extends [`SchedulableFunctionReference`](/api/modules/server.md#schedulablefunctionreference) |

#### Parameters[​](#parameters "Direct link to Parameters")

| Name                | Type                                                                     | Description                                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `delayMs`           | `number`                                                                 | Delay in milliseconds. Must be non-negative. If the delay is zero, the scheduled function will be due to execute immediately after the scheduling one completes. |
| `functionReference` | `FuncRef`                                                                | A [FunctionReference](/api/modules/server.md#functionreference) for the function to schedule.                                                                    |
| `...args`           | [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`FuncRef`> | Arguments to call the scheduled functions with.                                                                                                                  |

#### Returns[​](#returns "Direct link to Returns")

`Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_scheduled_functions"`>>

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/scheduler.ts:41](https://github.com/get-convex/convex-js/blob/main/src/server/scheduler.ts#L41)

***

### runAt[​](#runat "Direct link to runAt")

▸ **runAt**<`FuncRef`>(`timestamp`, `functionReference`, `...args`): `Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_scheduled_functions"`>>

Schedule a function to execute at a given timestamp.

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name      | Type                                                                                          |
| --------- | --------------------------------------------------------------------------------------------- |
| `FuncRef` | extends [`SchedulableFunctionReference`](/api/modules/server.md#schedulablefunctionreference) |

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name                | Type                                                                     | Description                                                                                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp`         | `number` \| `Date`                                                       | A Date or a timestamp (milliseconds since the epoch). If the timestamp is in the past, the scheduled function will be due to execute immediately after the scheduling one completes. The timestamp can't be more than five years in the past or more than five years in the future. |
| `functionReference` | `FuncRef`                                                                | A [FunctionReference](/api/modules/server.md#functionreference) for the function to schedule.                                                                                                                                                                                       |
| `...args`           | [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`FuncRef`> | arguments to call the scheduled functions with.                                                                                                                                                                                                                                     |

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_scheduled_functions"`>>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/scheduler.ts:58](https://github.com/get-convex/convex-js/blob/main/src/server/scheduler.ts#L58)

***

### cancel[​](#cancel "Direct link to cancel")

▸ **cancel**(`id`): `Promise`<`void`>

Cancels a previously scheduled function if it has not started yet. If the scheduled function is already in progress, it will continue running but any new functions that it tries to schedule will be canceled.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name | Type                                                                      |
| ---- | ------------------------------------------------------------------------- |
| `id` | [`GenericId`](/api/modules/values.md#genericid)<`"_scheduled_functions"`> |

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/scheduler.ts:71](https://github.com/get-convex/convex-js/blob/main/src/server/scheduler.ts#L71)
