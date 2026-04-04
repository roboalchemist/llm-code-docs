# Source: https://node-llama-cpp.withcat.ai/api/classes/QwenChatWrapper.md

---
url: /api/classes/QwenChatWrapper.md
---
# Class: QwenChatWrapper

Defined in: [chatWrappers/QwenChatWrapper.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L12)

## Extends

* [`ChatWrapper`](ChatWrapper.md)

## Constructors

### Constructor

```ts
new QwenChatWrapper(options?: {
  keepOnlyLastThought?: boolean;
  thoughts?: "auto" | "discourage";
}): QwenChatWrapper;
```

Defined in: [chatWrappers/QwenChatWrapper.ts:21](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L21)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `keepOnlyLastThought?`: `boolean`; `thoughts?`: `"auto"` | `"discourage"`; } | - |
| `options.keepOnlyLastThought?` | `boolean` | Whether to keep only the chain of thought from the last model response. Setting this to `false` will keep all the chain of thoughts from the model responses in the context state. Defaults to `true`. |
| `options.thoughts?` | `"auto"` | `"discourage"` | Control the usage of thoughts in the model responses. Defaults to `"auto"`. |

#### Returns

`QwenChatWrapper`

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
readonly wrapperName: string = "Qwen";
```

Defined in: [chatWrappers/QwenChatWrapper.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L13)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`wrapperName`](ChatWrapper.md#wrappername)

***

### keepOnlyLastThought

```ts
readonly keepOnlyLastThought: boolean;
```

Defined in: [chatWrappers/QwenChatWrapper.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L15)

***

### thoughts

```ts
readonly thoughts: "auto" | "discourage";
```

Defined in: [chatWrappers/QwenChatWrapper.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L16)

***

### settings

```ts
readonly settings: ChatWrapperSettings;
```

Defined in: [chatWrappers/QwenChatWrapper.ts:19](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L19)

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

Defined in: [chatWrappers/QwenChatWrapper.ts:100](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L100)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateContextStateOptions`](../type-aliases/ChatWrapperGenerateContextStateOptions.md) |

#### Returns

[`ChatWrapperGeneratedContextState`](../type-aliases/ChatWrapperGeneratedContextState.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateContextState`](ChatWrapper.md#generatecontextstate)

***

### generateFunctionCallResult()

```ts
generateFunctionCallResult(
   functionName: string, 
   functionParams: any, 
   result: any): LlamaText;
```

Defined in: [chatWrappers/QwenChatWrapper.ts:214](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L214)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `functionName` | `string` |
| `functionParams` | `any` |
| `result` | `any` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateFunctionCallResult`](ChatWrapper.md#generatefunctioncallresult)

***

### generateAvailableFunctionsSystemText()

```ts
generateAvailableFunctionsSystemText(availableFunctions: ChatModelFunctions, __namedParameters: {
  documentParams?: boolean;
}): LlamaText;
```

Defined in: [chatWrappers/QwenChatWrapper.ts:221](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/QwenChatWrapper.ts#L221)

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
