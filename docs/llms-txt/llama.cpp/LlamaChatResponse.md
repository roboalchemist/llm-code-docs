# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponse.md

---
url: /api/type-aliases/LlamaChatResponse.md
---
# Type Alias: LlamaChatResponse\<Functions>

```ts
type LlamaChatResponse<Functions> = {
  response: string;
  fullResponse: (string | LlamaChatResponseSegment)[];
  functionCalls?: Functions extends ChatModelFunctions ? LlamaChatResponseFunctionCall<Functions>[] : never;
  lastEvaluation: {
     cleanHistory: ChatHistoryItem[];
     contextWindow: ChatHistoryItem[];
     contextShiftMetadata: any;
  };
  metadata:   | {
     remainingGenerationAfterStop?: string | Token[];
     stopReason:   | "eogToken"
        | "stopGenerationTrigger"
        | "functionCalls"
        | "maxTokens"
        | "abort";
   }
     | {
     remainingGenerationAfterStop?: string | Token[];
     stopReason: "customStopTrigger";
     customStopTrigger: (string | Token)[];
   };
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1046](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1046)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* [`ChatModelFunctions`](ChatModelFunctions.md) | `undefined` | `undefined` |

## Properties

### response

```ts
response: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1050](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1050)

The response text only, *without* any text segments (like thoughts).

***

### fullResponse

```ts
fullResponse: (string | LlamaChatResponseSegment)[];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1055](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1055)

The full response, including all text and text segments (like thoughts).

***

### functionCalls?

```ts
optional functionCalls: Functions extends ChatModelFunctions ? LlamaChatResponseFunctionCall<Functions>[] : never;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1056](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1056)

***

### lastEvaluation

```ts
lastEvaluation: {
  cleanHistory: ChatHistoryItem[];
  contextWindow: ChatHistoryItem[];
  contextShiftMetadata: any;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1059](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1059)

#### cleanHistory

```ts
cleanHistory: ChatHistoryItem[];
```

#### contextWindow

```ts
contextWindow: ChatHistoryItem[];
```

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
  stopReason:   | "eogToken"
     | "stopGenerationTrigger"
     | "functionCalls"
     | "maxTokens"
     | "abort";
}
  | {
  remainingGenerationAfterStop?: string | Token[];
  stopReason: "customStopTrigger";
  customStopTrigger: (string | Token)[];
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1064](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1064)
