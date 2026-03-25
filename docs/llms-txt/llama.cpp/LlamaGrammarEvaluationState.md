# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaGrammarEvaluationState.md

---
url: /api/classes/LlamaGrammarEvaluationState.md
---
# Class: LlamaGrammarEvaluationState

Defined in: [evaluator/LlamaGrammarEvaluationState.ts:19](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammarEvaluationState.ts#L19)

Grammar evaluation state is used to track the model response to determine the next allowed characters for the model to generate.

Create a new grammar evaluation state for every response you generate with the model.

This is only needed when using the `LlamaContext` class directly, since `LlamaChatSession` already handles this for you.

## Constructors

### Constructor

```ts
new LlamaGrammarEvaluationState(options: LlamaGrammarEvaluationStateOptions): LlamaGrammarEvaluationState;
```

Defined in: [evaluator/LlamaGrammarEvaluationState.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammarEvaluationState.ts#L23)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaGrammarEvaluationStateOptions`](../type-aliases/LlamaGrammarEvaluationStateOptions.md) |

#### Returns

`LlamaGrammarEvaluationState`

### Constructor

```ts
new LlamaGrammarEvaluationState(existingState: LlamaGrammarEvaluationState): LlamaGrammarEvaluationState;
```

Defined in: [evaluator/LlamaGrammarEvaluationState.ts:24](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammarEvaluationState.ts#L24)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `existingState` | `LlamaGrammarEvaluationState` |

#### Returns

`LlamaGrammarEvaluationState`

## Methods

### clone()

```ts
clone(): LlamaGrammarEvaluationState;
```

Defined in: [evaluator/LlamaGrammarEvaluationState.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammarEvaluationState.ts#L41)

Clone the grammar evaluation state

#### Returns

`LlamaGrammarEvaluationState`
