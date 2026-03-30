# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LLamaChatPromptCompletionEngineOptions.md

---
url: /api/type-aliases/LLamaChatPromptCompletionEngineOptions.md
---
# Type Alias: LLamaChatPromptCompletionEngineOptions

```ts
type LLamaChatPromptCompletionEngineOptions = {
  maxPreloadTokens?: number;
  onGeneration?: void;
  maxCachedCompletions?: number;
  temperature?: LLamaChatCompletePromptOptions["temperature"];
  minP?: LLamaChatCompletePromptOptions["minP"];
  topK?: LLamaChatCompletePromptOptions["topK"];
  topP?: LLamaChatCompletePromptOptions["topP"];
  seed?: LLamaChatCompletePromptOptions["seed"];
  xtc?: LLamaChatCompletePromptOptions["xtc"];
  trimWhitespaceSuffix?: LLamaChatCompletePromptOptions["trimWhitespaceSuffix"];
  evaluationPriority?: LLamaChatCompletePromptOptions["evaluationPriority"];
  repeatPenalty?: LLamaChatCompletePromptOptions["repeatPenalty"];
  dryRepeatPenalty?: LLamaChatCompletePromptOptions["dryRepeatPenalty"];
  tokenBias?: LLamaChatCompletePromptOptions["tokenBias"];
  customStopTriggers?: LLamaChatCompletePromptOptions["customStopTriggers"];
  grammar?: LLamaChatCompletePromptOptions["grammar"];
  functions?: LLamaChatCompletePromptOptions["functions"];
  documentFunctionParams?: LLamaChatCompletePromptOptions["documentFunctionParams"];
  completeAsModel?: LLamaChatCompletePromptOptions["completeAsModel"];
};
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:8](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L8)

## Properties

### maxPreloadTokens?

```ts
optional maxPreloadTokens: number;
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L14)

Max tokens to allow for preloading a prompt and generating a completion for it.

Defaults to `256` or half of the context size, whichever is smaller.

***

### maxCachedCompletions?

```ts
optional maxCachedCompletions: number;
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L22)

Max number of completions to cache.

Defaults to `100`.

***

### temperature?

```ts
optional temperature: LLamaChatCompletePromptOptions["temperature"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:24](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L24)

***

### minP?

```ts
optional minP: LLamaChatCompletePromptOptions["minP"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L25)

***

### topK?

```ts
optional topK: LLamaChatCompletePromptOptions["topK"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:26](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L26)

***

### topP?

```ts
optional topP: LLamaChatCompletePromptOptions["topP"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:27](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L27)

***

### seed?

```ts
optional seed: LLamaChatCompletePromptOptions["seed"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:28](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L28)

***

### xtc?

```ts
optional xtc: LLamaChatCompletePromptOptions["xtc"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:29](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L29)

***

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: LLamaChatCompletePromptOptions["trimWhitespaceSuffix"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:30](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L30)

***

### evaluationPriority?

```ts
optional evaluationPriority: LLamaChatCompletePromptOptions["evaluationPriority"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L31)

***

### repeatPenalty?

```ts
optional repeatPenalty: LLamaChatCompletePromptOptions["repeatPenalty"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:32](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L32)

***

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LLamaChatCompletePromptOptions["dryRepeatPenalty"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:33](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L33)

***

### tokenBias?

```ts
optional tokenBias: LLamaChatCompletePromptOptions["tokenBias"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:34](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L34)

***

### customStopTriggers?

```ts
optional customStopTriggers: LLamaChatCompletePromptOptions["customStopTriggers"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L35)

***

### grammar?

```ts
optional grammar: LLamaChatCompletePromptOptions["grammar"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:36](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L36)

***

### functions?

```ts
optional functions: LLamaChatCompletePromptOptions["functions"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:37](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L37)

***

### documentFunctionParams?

```ts
optional documentFunctionParams: LLamaChatCompletePromptOptions["documentFunctionParams"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:38](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L38)

***

### completeAsModel?

```ts
optional completeAsModel: LLamaChatCompletePromptOptions["completeAsModel"];
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:39](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L39)

## Methods

### onGeneration()?

```ts
optional onGeneration(prompt: string, completion: string): void;
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L15)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prompt` | `string` |
| `completion` | `string` |

#### Returns

`void`
