# Source: https://node-llama-cpp.withcat.ai/api/classes/DeepSeekChatWrapper.md

---
url: /api/classes/DeepSeekChatWrapper.md
---
# Class: DeepSeekChatWrapper

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:11](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L11)

## Extends

* [`ChatWrapper`](ChatWrapper.md)

## Constructors

### Constructor

```ts
new DeepSeekChatWrapper(options?: {
  keepOnlyLastThought?: boolean;
  functionCallingSyntax?: "r1-workaround" | "simplified" | "original";
  parallelFunctionCalling?: boolean;
}): DeepSeekChatWrapper;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:20](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L20)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `keepOnlyLastThought?`: `boolean`; `functionCallingSyntax?`: `"r1-workaround"` | `"simplified"` | `"original"`; `parallelFunctionCalling?`: `boolean`; } | - |
| `options.keepOnlyLastThought?` | `boolean` | Whether to keep only the chain of thought from the last model response. Setting this to `false` will keep all the chain of thoughts from the model responses in the context state. Defaults to `true`. |
| `options.functionCallingSyntax?` | `"r1-workaround"` | `"simplified"` | `"original"` | Use a different variation function calling syntax to improve syntax compliance. Defaults to `"r1-workaround"`. |
| `options.parallelFunctionCalling?` | `boolean` | Support parallel function calling. May not work well with all distill model variations, as some distillation models make unnecessary additional calls in parallel. Defaults to `false`. |

#### Returns

`DeepSeekChatWrapper`

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`constructor`](ChatWrapper.md#constructor)

## Properties

### defaultSettings

```ts
static defaultSettings: ChatWrapperSettings;
```

Defined in: [ChatWrapper.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L14)

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`defaultSettings`](ChatWrapper.md#defaultsettings)

***

### wrapperName

```ts
readonly wrapperName: string = "DeepSeek";
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L12)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`wrapperName`](ChatWrapper.md#wrappername)

***

### keepOnlyLastThought

```ts
readonly keepOnlyLastThought: boolean;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L14)

***

### functionCallingSyntax

```ts
readonly functionCallingSyntax: "r1-workaround" | "simplified" | "original";
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L15)

***

### parallelFunctionCalling

```ts
readonly parallelFunctionCalling: boolean;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L16)

***

### settings

```ts
readonly settings: ChatWrapperSettings;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:18](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L18)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`settings`](ChatWrapper.md#settings)

## Methods

### generateFunctionCallsAndResults()

```ts
generateFunctionCallsAndResults(functionCalls: ChatModelFunctionCall[], useRawCall?: boolean): LlamaText;
```

Defined in: [ChatWrapper.ts:60](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L60)

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `functionCalls` | [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md)\[] | `undefined` |
| `useRawCall` | `boolean` | `true` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`generateFunctionCallsAndResults`](ChatWrapper.md#generatefunctioncallsandresults)

***

### generateFunctionCall()

```ts
generateFunctionCall(name: string, params: any): LlamaText;
```

Defined in: [ChatWrapper.ts:107](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L107)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `params` | `any` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`generateFunctionCall`](ChatWrapper.md#generatefunctioncall)

***

### generateFunctionCallResult()

```ts
generateFunctionCallResult(
   functionName: string, 
   functionParams: any, 
   result: any): LlamaText;
```

Defined in: [ChatWrapper.ts:124](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L124)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `functionName` | `string` |
| `functionParams` | `any` |
| `result` | `any` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`generateFunctionCallResult`](ChatWrapper.md#generatefunctioncallresult)

***

### generateModelResponseText()

```ts
generateModelResponseText(modelResponse: (
  | string
  | ChatModelFunctionCall
  | ChatModelSegment)[], useRawValues?: boolean): LlamaText;
```

Defined in: [ChatWrapper.ts:155](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L155)

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `modelResponse` | ( | `string` | [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md) | [`ChatModelSegment`](../type-aliases/ChatModelSegment.md))\[] | `undefined` |
| `useRawValues` | `boolean` | `true` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`generateModelResponseText`](ChatWrapper.md#generatemodelresponsetext)

***

### addAvailableFunctionsSystemMessageToHistory()

```ts
addAvailableFunctionsSystemMessageToHistory(
   history: readonly ChatHistoryItem[], 
   availableFunctions?: ChatModelFunctions, 
   __namedParameters?: {
  documentParams?: boolean;
}): readonly ChatHistoryItem[];
```

Defined in: [ChatWrapper.ts:264](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L264)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `history` | readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `availableFunctions?` | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) |
| `__namedParameters?` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`addAvailableFunctionsSystemMessageToHistory`](ChatWrapper.md#addavailablefunctionssystemmessagetohistory)

***

### generateInitialChatHistory()

```ts
generateInitialChatHistory(__namedParameters?: ChatWrapperGenerateInitialHistoryOptions): ChatHistoryItem[];
```

Defined in: [ChatWrapper.ts:285](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L285)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateInitialHistoryOptions`](../type-aliases/ChatWrapperGenerateInitialHistoryOptions.md) |

#### Returns

[`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]

#### Inherited from

[`ChatWrapper`](ChatWrapper.md).[`generateInitialChatHistory`](ChatWrapper.md#generateinitialchathistory)

***

### generateContextState()

```ts
generateContextState(__namedParameters: ChatWrapperGenerateContextStateOptions): ChatWrapperGeneratedContextState;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:173](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L173)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateContextStateOptions`](../type-aliases/ChatWrapperGenerateContextStateOptions.md) |

#### Returns

[`ChatWrapperGeneratedContextState`](../type-aliases/ChatWrapperGeneratedContextState.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateContextState`](ChatWrapper.md#generatecontextstate)

***

### generateAvailableFunctionsSystemText()

```ts
generateAvailableFunctionsSystemText(availableFunctions: ChatModelFunctions, __namedParameters: {
  documentParams?: boolean;
}): LlamaText;
```

Defined in: [chatWrappers/DeepSeekChatWrapper.ts:230](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/DeepSeekChatWrapper.ts#L230)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `availableFunctions` | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) |
| `__namedParameters` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateAvailableFunctionsSystemText`](ChatWrapper.md#generateavailablefunctionssystemtext)
