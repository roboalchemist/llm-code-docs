# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/CustomBatchingDispatchSchedule.md

---
url: /api/type-aliases/CustomBatchingDispatchSchedule.md
---
# Type Alias: CustomBatchingDispatchSchedule()

```ts
type CustomBatchingDispatchSchedule = (dispatch: () => void) => void;
```

Defined in: [evaluator/LlamaContext/types.ts:321](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L321)

A function that schedules the dispatch of the batch items.
Call the `dispatch` function to dispatch the items.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `dispatch` | () => `void` |

## Returns

`void`
