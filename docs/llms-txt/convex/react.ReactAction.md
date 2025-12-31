# Source: https://docs.convex.dev/api/interfaces/react.ReactAction.md

# Interface: ReactAction\<Action>

[react](/api/modules/react.md).ReactAction

An interface to execute a Convex action on the server.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name     | Type                                                                                |
| -------- | ----------------------------------------------------------------------------------- |
| `Action` | extends [`FunctionReference`](/api/modules/server.md#functionreference)<`"action"`> |

## Callable[​](#callable "Direct link to Callable")

### ReactAction[​](#reactaction "Direct link to ReactAction")

▸ **ReactAction**(`...args`): `Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Action`>>

Execute the function on the server, returning a `Promise` of its return value.

#### Parameters[​](#parameters "Direct link to Parameters")

| Name      | Type                                                                    | Description                                          |
| --------- | ----------------------------------------------------------------------- | ---------------------------------------------------- |
| `...args` | [`OptionalRestArgs`](/api/modules/server.md#optionalrestargs)<`Action`> | Arguments for the function to pass up to the server. |

#### Returns[​](#returns "Direct link to Returns")

`Promise`<[`FunctionReturnType`](/api/modules/server.md#functionreturntype)<`Action`>>

The return value of the server-side function call.

#### Defined in[​](#defined-in "Direct link to Defined in")

[react/client.ts:136](https://github.com/get-convex/convex-js/blob/main/src/react/client.ts#L136)
