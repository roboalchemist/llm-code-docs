# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaChatSessionPromptCompletionEngine.md

---
url: /api/classes/LlamaChatSessionPromptCompletionEngine.md
---
# Class: LlamaChatSessionPromptCompletionEngine

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:58](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L58)

## Methods

### dispose()

```ts
dispose(): void;
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:93](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L93)

#### Returns

`void`

***

### complete()

```ts
complete(prompt: string): string;
```

Defined in: [evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts:106](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/LlamaChatSessionPromptCompletionEngine.ts#L106)

Get completion for the prompt from the cache,
and begin preloading this prompt into the context sequence and completing it.

On completion progress, `onGeneration` (configured for this engine instance) will be called.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prompt` | `string` |

#### Returns

`string`
