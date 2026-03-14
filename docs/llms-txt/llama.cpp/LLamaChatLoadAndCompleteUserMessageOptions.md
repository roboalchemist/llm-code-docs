# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LLamaChatLoadAndCompleteUserMessageOptions.md

---
url: /api/type-aliases/LLamaChatLoadAndCompleteUserMessageOptions.md
---
# Type Alias: LLamaChatLoadAndCompleteUserMessageOptions\<Functions>

```ts
type LLamaChatLoadAndCompleteUserMessageOptions<Functions> = {
  initialUserPrompt?: string;
  stopOnAbortSignal?: boolean;
  onTextChunk?: LLamaChatGenerateResponseOptions<Functions>["onTextChunk"];
  onToken?: LLamaChatGenerateResponseOptions<Functions>["onToken"];
  signal?: LLamaChatGenerateResponseOptions<Functions>["signal"];
  maxTokens?: LLamaChatGenerateResponseOptions<Functions>["maxTokens"];
  temperature?: LLamaChatGenerateResponseOptions<Functions>["temperature"];
  minP?: LLamaChatGenerateResponseOptions<Functions>["minP"];
  topK?: LLamaChatGenerateResponseOptions<Functions>["topK"];
  topP?: LLamaChatGenerateResponseOptions<Functions>["topP"];
  seed?: LLamaChatGenerateResponseOptions<Functions>["seed"];
  xtc?: LLamaChatGenerateResponseOptions<Functions>["xtc"];
  trimWhitespaceSuffix?: LLamaChatGenerateResponseOptions<Functions>["trimWhitespaceSuffix"];
  repeatPenalty?: LLamaChatGenerateResponseOptions<Functions>["repeatPenalty"];
  dryRepeatPenalty?: LLamaChatGenerateResponseOptions<Functions>["dryRepeatPenalty"];
  tokenBias?: LLamaChatGenerateResponseOptions<Functions>["tokenBias"];
  evaluationPriority?: LLamaChatGenerateResponseOptions<Functions>["evaluationPriority"];
  contextShift?: LLamaChatGenerateResponseOptions<Functions>["contextShift"];
  customStopTriggers?: LLamaChatGenerateResponseOptions<Functions>["customStopTriggers"];
  lastEvaluationContextWindow?: LLamaChatGenerateResponseOptions<Functions>["lastEvaluationContextWindow"];
  grammar?: LlamaGrammar;
  functions?: Functions | ChatModelFunctions;
  documentFunctionParams?: boolean;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:397](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L397)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* [`ChatModelFunctions`](ChatModelFunctions.md) | `undefined` | `undefined` |

## Properties

### initialUserPrompt?

```ts
optional initialUserPrompt: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:401](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L401)

Complete the given user prompt without adding it or the completion to the returned context window.

***

### stopOnAbortSignal?

```ts
optional stopOnAbortSignal: boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:409](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L409)

When a completion already started being generated and then the signal is aborted,
the generation will stop and the completion will be returned as is instead of throwing an error.

Defaults to `false`.

***

### onTextChunk?

```ts
optional onTextChunk: LLamaChatGenerateResponseOptions<Functions>["onTextChunk"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:416](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L416)

Called as the model generates a completion with the generated text chunk.

Useful for streaming the generated completion as it's being generated.

***

### onToken?

```ts
optional onToken: LLamaChatGenerateResponseOptions<Functions>["onToken"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:423](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L423)

Called as the model generates a completion with the generated tokens.

Preferably, you'd want to use `onTextChunk` instead of this.

***

### signal?

```ts
optional signal: LLamaChatGenerateResponseOptions<Functions>["signal"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:425](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L425)

***

### maxTokens?

```ts
optional maxTokens: LLamaChatGenerateResponseOptions<Functions>["maxTokens"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:426](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L426)

***

### temperature?

```ts
optional temperature: LLamaChatGenerateResponseOptions<Functions>["temperature"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:427](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L427)

***

### minP?

```ts
optional minP: LLamaChatGenerateResponseOptions<Functions>["minP"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:428](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L428)

***

### topK?

```ts
optional topK: LLamaChatGenerateResponseOptions<Functions>["topK"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:429](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L429)

***

### topP?

```ts
optional topP: LLamaChatGenerateResponseOptions<Functions>["topP"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:430](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L430)

***

### seed?

```ts
optional seed: LLamaChatGenerateResponseOptions<Functions>["seed"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:431](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L431)

***

### xtc?

```ts
optional xtc: LLamaChatGenerateResponseOptions<Functions>["xtc"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:432](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L432)

***

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: LLamaChatGenerateResponseOptions<Functions>["trimWhitespaceSuffix"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:433](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L433)

***

### repeatPenalty?

```ts
optional repeatPenalty: LLamaChatGenerateResponseOptions<Functions>["repeatPenalty"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:434](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L434)

***

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LLamaChatGenerateResponseOptions<Functions>["dryRepeatPenalty"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:435](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L435)

***

### tokenBias?

```ts
optional tokenBias: LLamaChatGenerateResponseOptions<Functions>["tokenBias"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:436](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L436)

***

### evaluationPriority?

```ts
optional evaluationPriority: LLamaChatGenerateResponseOptions<Functions>["evaluationPriority"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:437](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L437)

***

### contextShift?

```ts
optional contextShift: LLamaChatGenerateResponseOptions<Functions>["contextShift"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:438](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L438)

***

### customStopTriggers?

```ts
optional customStopTriggers: LLamaChatGenerateResponseOptions<Functions>["customStopTriggers"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:439](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L439)

***

### lastEvaluationContextWindow?

```ts
optional lastEvaluationContextWindow: LLamaChatGenerateResponseOptions<Functions>["lastEvaluationContextWindow"];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:440](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L440)

***

### grammar?

```ts
optional grammar: LlamaGrammar;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:442](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L442)

***

### functions?

```ts
optional functions: Functions | ChatModelFunctions;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:451](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L451)

Functions are not used by the model here,
but are used for keeping the instructions given to the model about the functions in the current context state,
to avoid context shifts.

It's best to provide the same functions that were used for the previous prompt here.

***

### documentFunctionParams?

```ts
optional documentFunctionParams: boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:460](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L460)

Functions are not used by the model here,
but are used for keeping the instructions given to the model about the functions in the current context state,
to avoid context shifts.

It's best to provide the same value that was used for the previous prompt here.
