# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/functions/withattributes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# withAttributes

> TypeScript SDK reference

# withAttributes

▸ **withAttributes**\<`T`>(`attrs`, `fn`): `Promise`\<`T`> | `T`

Attach attributes to the current execution context so that any calls created
inside `fn` automatically inherit them. Attributes are written to the call
record on the trace server and surface in the Weave UI/filtering, so they’re
ideal for tagging runs with request IDs, tenants, experiments, etc.

Example:

```ts  theme={null}
await withAttributes({requestId: 'abc'}, async () => {
  await myOp();
});
```

#### Type parameters

| Name |
| :--- |
| `T`  |

#### Parameters

| Name    | Type                         |
| :------ | :--------------------------- |
| `attrs` | `Record`\<`string`, `any`>   |
| `fn`    | () => `T` \| `Promise`\<`T`> |

#### Returns

`Promise`\<`T`> | `T`

#### Defined in

[clientApi.ts:193](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/clientApi.ts#L193)

***
