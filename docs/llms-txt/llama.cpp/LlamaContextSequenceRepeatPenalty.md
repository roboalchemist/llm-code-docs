# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaContextSequenceRepeatPenalty.md

---
url: /api/type-aliases/LlamaContextSequenceRepeatPenalty.md
---
# Type Alias: LlamaContextSequenceRepeatPenalty

```ts
type LlamaContextSequenceRepeatPenalty = {
  punishTokens: Token[] | () => Token[];
  maxPunishTokens?: number;
  penalty?: number;
  frequencyPenalty?: number;
  presencePenalty?: number;
};
```

Defined in: [evaluator/LlamaContext/types.ts:205](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L205)

## Properties

### punishTokens

```ts
punishTokens: Token[] | () => Token[];
```

Defined in: [evaluator/LlamaContext/types.ts:207](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L207)

Tokens to lower the predication probability of to be the next predicted token

***

### maxPunishTokens?

```ts
optional maxPunishTokens: number;
```

Defined in: [evaluator/LlamaContext/types.ts:218](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L218)

The maximum number of tokens that will be provided in the `punishTokens` array.

This is used as a hint for a performance optimization for avoiding frequent memory deallocation and reallocation.

Don't set this value too high, as it can allocate too much memory.

Defaults to `64`.

***

### penalty?

```ts
optional penalty: number;
```

Defined in: [evaluator/LlamaContext/types.ts:226](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L226)

The relative amount to lower the probability of the tokens in `punishTokens` by.

Defaults to `1.1`.
Set to `1` to disable.

***

### frequencyPenalty?

```ts
optional frequencyPenalty: number;
```

Defined in: [evaluator/LlamaContext/types.ts:234](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L234)

For n time a token is in the `punishTokens` array, lower its probability by `n * frequencyPenalty`.

Disabled by default (`0`).
Set to a value between `0` and `1` to enable.

***

### presencePenalty?

```ts
optional presencePenalty: number;
```

Defined in: [evaluator/LlamaContext/types.ts:242](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L242)

Lower the probability of all the tokens in the `punishTokens` array by `presencePenalty`.

Disabled by default (`0`).
Set to a value between `0` and `1` to enable.
