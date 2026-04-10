# Source: https://docs.convex.dev/api/interfaces/react.MutationOptions.md

# Interface: MutationOptions\<Args>

[react](/api/modules/react.md).MutationOptions

Options for [mutation](/api/classes/react.ConvexReactClient.md#mutation).

## Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name   | Type                                                                |
| ------ | ------------------------------------------------------------------- |
| `Args` | extends `Record`<`string`, [`Value`](/api/modules/values.md#value)> |

## Properties[​](#properties "Direct link to Properties")

### optimisticUpdate[​](#optimisticupdate "Direct link to optimisticUpdate")

• `Optional` **optimisticUpdate**: [`OptimisticUpdate`](/api/modules/browser.md#optimisticupdate)<`Args`>

An optimistic update to apply along with this mutation.

An optimistic update locally updates queries while a mutation is pending. Once the mutation completes, the update will be rolled back.

#### Defined in[​](#defined-in "Direct link to Defined in")

[react/client.ts:282](https://github.com/get-convex/convex-js/blob/main/src/react/client.ts#L282)
