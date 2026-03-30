# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ControlledEvaluateIndexOutput.md

---
url: /api/type-aliases/ControlledEvaluateIndexOutput.md
---
# Type Alias: ControlledEvaluateIndexOutput

```ts
type ControlledEvaluateIndexOutput = {
  next: {
     token?: Token | null;
     confidence?: number;
     probabilities?: Map<Token, number>;
  };
};
```

Defined in: [evaluator/LlamaContext/types.ts:592](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L592)

## Properties

### next

```ts
next: {
  token?: Token | null;
  confidence?: number;
  probabilities?: Map<Token, number>;
};
```

Defined in: [evaluator/LlamaContext/types.ts:593](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L593)

#### token?

```ts
optional token: Token | null;
```

#### confidence?

```ts
optional confidence: number;
```

The confidence (probability) of the selected token (the `token` field in this object).

Same as `next.probabilities.get(next.token)`.

If you need only this value, you can skip getting the full probabilities list to improve performance.

This value might be slightly different when evaluated on different GPUs and configurations.

#### probabilities?

```ts
optional probabilities: Map<Token, number>;
```

The probabilities of the tokens from the vocabulary to be the next token.

A probability is a number from `0` to `1`.

The probabilities might be slightly different when evaluated on different GPUs and configurations.

The map is sorted by the probability of the tokens from the highest to the lowest,
and is reflected in the order of the entries when iterating over the map.
Use `.entries().next().value` to get the top probability pair
([learn more](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)).
