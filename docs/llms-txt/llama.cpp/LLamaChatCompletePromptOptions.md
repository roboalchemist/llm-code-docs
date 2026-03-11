# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LLamaChatCompletePromptOptions.md

---
url: /api/type-aliases/LLamaChatCompletePromptOptions.md
---
# Type Alias: LLamaChatCompletePromptOptions

```ts
type LLamaChatCompletePromptOptions = {
  maxTokens?: LLamaChatPromptOptions["maxTokens"];
  stopOnAbortSignal?: LLamaChatPromptOptions["stopOnAbortSignal"];
  onTextChunk?: LLamaChatPromptOptions["onTextChunk"];
  onToken?: LLamaChatPromptOptions["onToken"];
  signal?: LLamaChatPromptOptions["signal"];
  temperature?: LLamaChatPromptOptions["temperature"];
  minP?: LLamaChatPromptOptions["minP"];
  topK?: LLamaChatPromptOptions["topK"];
  topP?: LLamaChatPromptOptions["topP"];
  seed?: LLamaChatPromptOptions["seed"];
  xtc?: LLamaChatPromptOptions["xtc"];
  trimWhitespaceSuffix?: LLamaChatPromptOptions["trimWhitespaceSuffix"];
  evaluationPriority?: LLamaChatPromptOptions["evaluationPriority"];
  repeatPenalty?: LLamaChatPromptOptions["repeatPenalty"];
  dryRepeatPenalty?: LLamaChatPromptOptions["dryRepeatPenalty"];
  tokenBias?: LLamaChatPromptOptions["tokenBias"];
  customStopTriggers?: LLamaChatPromptOptions["customStopTriggers"];
  grammar?: LlamaGrammar;
  functions?: ChatSessionModelFunctions;
  documentFunctionParams?: boolean;
  completeAsModel?:   | "auto"
     | boolean
     | {
     enabled?: "auto" | boolean;
     appendedMessages?: ChatHistoryItem[];
   };
};
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:291](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L291)

## Properties

### maxTokens?

```ts
optional maxTokens: LLamaChatPromptOptions["maxTokens"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:297](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L297)

Generate a completion for the given user prompt up to the given number of tokens.

Defaults to `256` or half the context size, whichever is smaller.

***

### stopOnAbortSignal?

```ts
optional stopOnAbortSignal: LLamaChatPromptOptions["stopOnAbortSignal"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:305](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L305)

When a completion already started being generated and then the given `signal` is aborted,
the generation will stop and the completion will be returned as-is instead of throwing an error.

Defaults to `false`.

***

### onTextChunk?

```ts
optional onTextChunk: LLamaChatPromptOptions["onTextChunk"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:312](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L312)

Called as the model generates a completion with the generated text chunk.

Useful for streaming the generated completion as it's being generated.

***

### onToken?

```ts
optional onToken: LLamaChatPromptOptions["onToken"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:319](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L319)

Called as the model generates a completion with the generated tokens.

Preferably, you'd want to use `onTextChunk` instead of this.

***

### signal?

```ts
optional signal: LLamaChatPromptOptions["signal"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:321](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L321)

***

### temperature?

```ts
optional temperature: LLamaChatPromptOptions["temperature"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:322](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L322)

***

### minP?

```ts
optional minP: LLamaChatPromptOptions["minP"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:323](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L323)

***

### topK?

```ts
optional topK: LLamaChatPromptOptions["topK"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:324](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L324)

***

### topP?

```ts
optional topP: LLamaChatPromptOptions["topP"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:325](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L325)

***

### seed?

```ts
optional seed: LLamaChatPromptOptions["seed"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:326](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L326)

***

### xtc?

```ts
optional xtc: LLamaChatPromptOptions["xtc"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:327](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L327)

***

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: LLamaChatPromptOptions["trimWhitespaceSuffix"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:328](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L328)

***

### evaluationPriority?

```ts
optional evaluationPriority: LLamaChatPromptOptions["evaluationPriority"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:329](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L329)

***

### repeatPenalty?

```ts
optional repeatPenalty: LLamaChatPromptOptions["repeatPenalty"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:330](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L330)

***

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LLamaChatPromptOptions["dryRepeatPenalty"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:331](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L331)

***

### tokenBias?

```ts
optional tokenBias: LLamaChatPromptOptions["tokenBias"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:332](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L332)

***

### customStopTriggers?

```ts
optional customStopTriggers: LLamaChatPromptOptions["customStopTriggers"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:333](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L333)

***

### grammar?

```ts
optional grammar: LlamaGrammar;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:335](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L335)

***

### functions?

```ts
optional functions: ChatSessionModelFunctions;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:344](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L344)

Functions are not used by the model here,
but are used for keeping the instructions given to the model about the functions in the current context state,
to avoid context shifts.

It's best to provide the same functions that were used for the previous prompt here.

***

### documentFunctionParams?

```ts
optional documentFunctionParams: boolean;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:353](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L353)

Functions are not used by the model here,
but are used for keeping the instructions given to the model about the functions in the current context state,
to avoid context shifts.

It's best to provide the same value that was used for the previous prompt here.

***

### completeAsModel?

```ts
optional completeAsModel: 
  | "auto"
  | boolean
  | {
  enabled?: "auto" | boolean;
  appendedMessages?: ChatHistoryItem[];
};
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:365](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L365)

Whether to complete the prompt as a model response.

* **`"auto"`**: Automatically determine whether to complete as a model response based on the model used.
  This is a good option to workaround some models that don't support used prompt completions.
* **`true`**: Always complete as a model response
* **`false`**: Never complete as a model response

Defaults to `"auto"`.

#### Type Declaration

`"auto"`

`boolean`

```ts
{
  enabled?: "auto" | boolean;
  appendedMessages?: ChatHistoryItem[];
}
```

#### enabled?

```ts
optional enabled: "auto" | boolean;
```

Whether to complete the prompt as a model response.

* **`"auto"`**: Automatically determine whether to complete as a model response based on the model used.
  This is a good option to workaround some models that don't support used prompt completions.
* **`true`**: Always complete as a model response
* **`false`**: Never complete as a model response

Defaults to `"auto"`.

#### appendedMessages?

```ts
optional appendedMessages: ChatHistoryItem[];
```

The messages to append to the chat history to generate a completion as a model response.

If the last message is a model message, the prompt will be pushed to it for the completion,
otherwise a new model message will be added with the prompt.

It must contain a user message or a system message before the model message.

Default to:

```ts
[
    {
        type: "system",
        text: "For your next response predict what the user may send next. " +
            "No yapping, no whitespace. Match the user's language and tone."
    },
    {type: "user", text: ""},
    {type: "model", response: [""]}
]
```
