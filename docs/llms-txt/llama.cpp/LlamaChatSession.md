# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaChatSession.md

---
url: /api/classes/LlamaChatSession.md
---
# Class: LlamaChatSession

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:513](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L513)

## See

[Using `LlamaChatSession`](https://node-llama-cpp.withcat.ai/guide/chat-session) tutorial

## Constructors

### Constructor

```ts
new LlamaChatSession(options: LlamaChatSessionOptions): LlamaChatSession;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:529](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L529)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaChatSessionOptions`](../type-aliases/LlamaChatSessionOptions.md) |

#### Returns

`LlamaChatSession`

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:527](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L527)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:586](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L586)

##### Returns

`boolean`

***

### chatWrapper

#### Get Signature

```ts
get chatWrapper(): ChatWrapper;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:590](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L590)

##### Returns

[`ChatWrapper`](ChatWrapper.md)

***

### sequence

#### Get Signature

```ts
get sequence(): LlamaContextSequence;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:597](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L597)

##### Returns

[`LlamaContextSequence`](LlamaContextSequence.md)

***

### context

#### Get Signature

```ts
get context(): LlamaContext;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:604](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L604)

##### Returns

[`LlamaContext`](LlamaContext.md)

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:608](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L608)

##### Returns

[`LlamaModel`](LlamaModel.md)

## Methods

### dispose()

```ts
dispose(__namedParameters?: {
  disposeSequence?: boolean;
}): void;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:571](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L571)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `disposeSequence?`: `boolean`; } |
| `__namedParameters.disposeSequence?` | `boolean` |

#### Returns

`void`

***

### prompt()

```ts
prompt<Functions>(prompt: string, options?: LLamaChatPromptOptions<Functions>): Promise<string>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:612](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L612)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* | [`ChatSessionModelFunctions`](../type-aliases/ChatSessionModelFunctions.md) | `undefined` | `undefined` |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prompt` | `string` |
| `options` | [`LLamaChatPromptOptions`](../type-aliases/LLamaChatPromptOptions.md)<`Functions`> |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`>

***

### promptWithMeta()

```ts
promptWithMeta<Functions>(prompt: string, options?: LLamaChatPromptOptions<Functions>): Promise<
  | {
  response: (
     | string
     | ChatModelFunctionCall
    | ChatModelSegment)[];
  responseText: string;
  stopReason: "customStopTrigger";
  customStopTrigger: (string | Token)[];
  remainingGenerationAfterStop: string | Token[] | undefined;
}
  | {
  customStopTrigger?: undefined;
  response: (
     | string
     | ChatModelFunctionCall
    | ChatModelSegment)[];
  responseText: string;
  stopReason:   | "abort"
     | "maxTokens"
     | "eogToken"
     | "stopGenerationTrigger"
     | "functionCalls";
  remainingGenerationAfterStop: string | Token[] | undefined;
}>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:663](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L663)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* | [`ChatSessionModelFunctions`](../type-aliases/ChatSessionModelFunctions.md) | `undefined` | `undefined` |

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `prompt` | `string` | - |
| `options?` | [`LLamaChatPromptOptions`](../type-aliases/LLamaChatPromptOptions.md)<`Functions`> | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<
| {
`response`: (
| `string`
| [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md)
| [`ChatModelSegment`](../type-aliases/ChatModelSegment.md))\[];
`responseText`: `string`;
`stopReason`: `"customStopTrigger"`;
`customStopTrigger`: (`string` | [`Token`](../type-aliases/Token.md))\[];
`remainingGenerationAfterStop`: `string` | [`Token`](../type-aliases/Token.md)\[] | `undefined`;
}
| {
`customStopTrigger?`: `undefined`;
`response`: (
| `string`
| [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md)
| [`ChatModelSegment`](../type-aliases/ChatModelSegment.md))\[];
`responseText`: `string`;
`stopReason`:   | `"abort"`
| `"maxTokens"`
| `"eogToken"`
| `"stopGenerationTrigger"`
| `"functionCalls"`;
`remainingGenerationAfterStop`: `string` | [`Token`](../type-aliases/Token.md)\[] | `undefined`;
}>

***

### preloadPrompt()

```ts
preloadPrompt(prompt: string, options?: LLamaChatPreloadPromptOptions): Promise<void>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:957](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L957)

Preload a user prompt into the current context sequence state to make later inference of the model response begin sooner
and feel faster.

> **Note:** Preloading a long user prompt can incur context shifts, so consider limiting the length of prompts you preload

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `prompt` | `string` | the prompt to preload |
| `options?` | [`LLamaChatPreloadPromptOptions`](../type-aliases/LLamaChatPreloadPromptOptions.md) | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### completePrompt()

```ts
completePrompt(prompt: string, options?: LLamaChatCompletePromptOptions): Promise<string>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:975](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L975)

Preload a user prompt into the current context sequence state and generate a completion for it.

> **Note:** Preloading a long user prompt and completing a user prompt with a high number of `maxTokens` can incur context shifts,
> so consider limiting the length of prompts you preload.
>
> Also, it's recommended to limit the number of tokens generated to a reasonable amount by configuring `maxTokens`.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `prompt` | `string` | the prompt to preload |
| `options?` | [`LLamaChatCompletePromptOptions`](../type-aliases/LLamaChatCompletePromptOptions.md) | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`>

***

### createPromptCompletionEngine()

```ts
createPromptCompletionEngine(options?: LLamaChatPromptCompletionEngineOptions): LlamaChatSessionPromptCompletionEngine;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:988](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L988)

Create a smart completion engine that caches the prompt completions
and reuses them when the user prompt matches the beginning of the cached prompt or completion.

All completions are made and cache is used only for the current chat session state.
You can create a single completion engine for an entire chat session.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options?` | [`LLamaChatPromptCompletionEngineOptions`](../type-aliases/LLamaChatPromptCompletionEngineOptions.md) |

#### Returns

[`LlamaChatSessionPromptCompletionEngine`](LlamaChatSessionPromptCompletionEngine.md)

***

### completePromptWithMeta()

```ts
completePromptWithMeta(prompt: string, options?: LLamaChatCompletePromptOptions): Promise<
  | {
  completion: string;
  stopReason: "customStopTrigger";
  customStopTrigger: (string | Token)[];
  remainingGenerationAfterStop: string | Token[] | undefined;
}
  | {
  customStopTrigger?: undefined;
  completion: string;
  stopReason:   | "abort"
     | "maxTokens"
     | "eogToken"
     | "stopGenerationTrigger"
     | "functionCalls";
  remainingGenerationAfterStop: string | Token[] | undefined;
}>;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:997](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L997)

See `completePrompt` for more information.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `prompt` | `string` | - |
| `options?` | [`LLamaChatCompletePromptOptions`](../type-aliases/LLamaChatCompletePromptOptions.md) | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<
| {
`completion`: `string`;
`stopReason`: `"customStopTrigger"`;
`customStopTrigger`: (`string` | [`Token`](../type-aliases/Token.md))\[];
`remainingGenerationAfterStop`: `string` | [`Token`](../type-aliases/Token.md)\[] | `undefined`;
}
| {
`customStopTrigger?`: `undefined`;
`completion`: `string`;
`stopReason`:   | `"abort"`
| `"maxTokens"`
| `"eogToken"`
| `"stopGenerationTrigger"`
| `"functionCalls"`;
`remainingGenerationAfterStop`: `string` | [`Token`](../type-aliases/Token.md)\[] | `undefined`;
}>

***

### getChatHistory()

```ts
getChatHistory(): ChatHistoryItem[];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:1231](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L1231)

#### Returns

[`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]

***

### getLastEvaluationContextWindow()

```ts
getLastEvaluationContextWindow(): ChatHistoryItem[] | null;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:1235](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L1235)

#### Returns

[`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] | `null`

***

### setChatHistory()

```ts
setChatHistory(chatHistory: ChatHistoryItem[]): void;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:1242](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L1242)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `chatHistory` | [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |

#### Returns

`void`

***

### resetChatHistory()

```ts
resetChatHistory(): void;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:1250](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L1250)

Clear the chat history and reset it to the initial state.

#### Returns

`void`
