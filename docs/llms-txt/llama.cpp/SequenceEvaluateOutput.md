# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/SequenceEvaluateOutput.md

---
url: /api/type-aliases/SequenceEvaluateOutput.md
---
# Type Alias: SequenceEvaluateOutput\<Options>

```ts
type SequenceEvaluateOutput<Options> = PickOptions<{
  token: Token;
  confidence: number;
  probabilities: Map<Token, number>;
}, Options & {
  token: true;
}>;
```

Defined in: [evaluator/LlamaContext/types.ts:460](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L460)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Options` *extends* { `confidence?`: `boolean`; `probabilities?`: `boolean`; } | { `confidence`: `true`; `probabilities`: `true`; } |
