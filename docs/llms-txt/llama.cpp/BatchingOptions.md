# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/BatchingOptions.md

---
url: /api/type-aliases/BatchingOptions.md
---
# Type Alias: BatchingOptions

```ts
type BatchingOptions = {
  dispatchSchedule?:   | "nextCycle"
     | CustomBatchingDispatchSchedule;
  itemPrioritizationStrategy?:   | "maximumParallelism"
     | "firstInFirstOut"
     | CustomBatchingPrioritizationStrategy;
};
```

Defined in: [evaluator/LlamaContext/types.ts:295](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L295)

## Properties

### dispatchSchedule?

```ts
optional dispatchSchedule: 
  | "nextCycle"
  | CustomBatchingDispatchSchedule;
```

Defined in: [evaluator/LlamaContext/types.ts:303](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L303)

The strategy used to dispatch items to be processed when there are items pending to be processed.

* **`"nextCycle"`** - dispatch the items on the next event loop cycle.
  You can provide a custom function to define a custom dispatch schedule.

Defaults to `"nextCycle"`.

***

### itemPrioritizationStrategy?

```ts
optional itemPrioritizationStrategy: 
  | "maximumParallelism"
  | "firstInFirstOut"
  | CustomBatchingPrioritizationStrategy;
```

Defined in: [evaluator/LlamaContext/types.ts:314](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L314)

The strategy used to prioritize pending items to be processed.

* **`"maximumParallelism"`** - process as many different sequences in parallel as possible.
* **`"firstInFirstOut"`** - process items in the order they were added.
* **Custom prioritization function** - a custom function that prioritizes the items to be processed.
  See the [CustomBatchingPrioritizationStrategy](CustomBatchingPrioritizationStrategy.md) type for more information.

Defaults to `"maximumParallelism"`.
