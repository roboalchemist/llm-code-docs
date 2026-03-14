# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaCompletionResponse.md

---
url: /api/type-aliases/LlamaCompletionResponse.md
---
# Type Alias: LlamaCompletionResponse

```ts
type LlamaCompletionResponse = {
  response: string;
  metadata:   | {
     remainingGenerationAfterStop?: string | Token[];
     stopReason: "eogToken" | "stopGenerationTrigger" | "maxTokens" | "abort";
   }
     | {
     remainingGenerationAfterStop?: string | Token[];
     stopReason: "customStopTrigger";
     customStopTrigger: (string | Token)[];
   };
};
```

Defined in: [evaluator/LlamaCompletion.ts:212](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L212)

## Properties

### response

```ts
response: string;
```

Defined in: [evaluator/LlamaCompletion.ts:213](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L213)

***

### metadata

```ts
metadata: 
  | {
  remainingGenerationAfterStop?: string | Token[];
  stopReason: "eogToken" | "stopGenerationTrigger" | "maxTokens" | "abort";
}
  | {
  remainingGenerationAfterStop?: string | Token[];
  stopReason: "customStopTrigger";
  customStopTrigger: (string | Token)[];
};
```

Defined in: [evaluator/LlamaCompletion.ts:214](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L214)
