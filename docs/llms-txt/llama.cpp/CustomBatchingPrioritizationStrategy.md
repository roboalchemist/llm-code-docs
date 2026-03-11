# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/CustomBatchingPrioritizationStrategy.md

---
url: /api/type-aliases/CustomBatchingPrioritizationStrategy.md
---
# Type Alias: CustomBatchingPrioritizationStrategy()

```ts
type CustomBatchingPrioritizationStrategy = (options: {
  items: readonly BatchItem[];
  size: number;
}) => PrioritizedBatchItem[];
```

Defined in: [evaluator/LlamaContext/types.ts:331](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L331)

A function that prioritizes the batch items to be processed.
The function receives an array of `items` and the `size` of how many tokens can be processed in this batch.

The function should return an array of prioritized items,
where the sum of `processAmount` of all the items is less or equal to the given `size` that the function received,
and where the `item` of each prioritized item is the same reference to an original item in the `items` array.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | { `items`: readonly [`BatchItem`](BatchItem.md)\[]; `size`: `number`; } |
| `options.items` | readonly [`BatchItem`](BatchItem.md)\[] |
| `options.size` | `number` |

## Returns

[`PrioritizedBatchItem`](PrioritizedBatchItem.md)\[]
