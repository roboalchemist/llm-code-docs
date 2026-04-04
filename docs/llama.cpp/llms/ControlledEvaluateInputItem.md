# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ControlledEvaluateInputItem.md

---
url: /api/type-aliases/ControlledEvaluateInputItem.md
---
# Type Alias: ControlledEvaluateInputItem

```ts
type ControlledEvaluateInputItem = 
  | Token
  | [Token, {
  generateNext?: {
     probabilities?: boolean;
     confidence?: boolean;
     token?: boolean;
     options?: {
        temperature?: number;
        minP?: number;
        topK?: number;
        topP?: number;
        seed?: number;
        xtc?: {
           probability: number;
           threshold: number;
        };
        repeatPenalty?: LlamaContextSequenceRepeatPenalty;
        dryRepeatPenalty?: LlamaContextSequenceDryRepeatPenalty;
        tokenBias?:   | TokenBias
           | () => TokenBias;
     };
  };
}];
```

Defined in: [evaluator/LlamaContext/types.ts:500](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L500)
