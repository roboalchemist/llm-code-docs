# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatLoadAndCompleteUserResponse.md

---
url: /api/type-aliases/LlamaChatLoadAndCompleteUserResponse.md
---
# Type Alias: LlamaChatLoadAndCompleteUserResponse

```ts
type LlamaChatLoadAndCompleteUserResponse = {
  completion: string;
  lastEvaluation: {
     contextWindow: ChatHistoryItem[];
     contextShiftMetadata: any;
  };
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

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1096](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1096)

## Properties

### completion

```ts
completion: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1097](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1097)

***

### lastEvaluation

```ts
lastEvaluation: {
  contextWindow: ChatHistoryItem[];
  contextShiftMetadata: any;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1098](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1098)

#### contextWindow

```ts
contextWindow: ChatHistoryItem[];
```

The completion and initial user prompt are not added to this context window result,
but are loaded to the current context sequence state as tokens

#### contextShiftMetadata

```ts
contextShiftMetadata: any;
```

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

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1106](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1106)
