# Source: https://node-llama-cpp.withcat.ai/api/classes/Llama3_1ChatWrapper.md

---
url: /api/classes/Llama3_1ChatWrapper.md
---
# Class: Llama3\_1ChatWrapper

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L12)

## Extends

* [`ChatWrapper`](ChatWrapper.md)

## Constructors

### Constructor

```ts
new Llama3_1ChatWrapper(options?: {
  cuttingKnowledgeDate?:   | string
     | number
     | Date
     | () => Date
     | null;
  todayDate?:   | string
     | number
     | Date
     | () => Date
     | null;
  noToolInstructions?: boolean;
}): Llama3_1ChatWrapper;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:37](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L37)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `cuttingKnowledgeDate?`: | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null`; `todayDate?`: | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null`; `noToolInstructions?`: `boolean`; } | - |
| `options.cuttingKnowledgeDate?` | | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null` | Set to `null` to disable Defaults to December 2023 |
| `options.todayDate?` | | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null` | Set to `null` to disable Defaults to current date |
| `options.noToolInstructions?` | `boolean` | - |

#### Returns

`Llama3_1ChatWrapper`

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
readonly wrapperName: string = "Llama 3.1";
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L13)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`wrapperName`](ChatWrapper.md#wrappername)

***

### cuttingKnowledgeDate?

```ts
readonly optional cuttingKnowledgeDate: 
  | Date
  | () => Date
  | null;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L15)

***

### todayDate

```ts
readonly todayDate: 
  | Date
  | () => Date
  | null;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L16)

***

### noToolInstructions

```ts
readonly noToolInstructions: boolean;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L17)

***

### settings

```ts
readonly settings: ChatWrapperSettings;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:21](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L21)

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

### addAvailableFunctionsSystemMessageToHistory()

```ts
addAvailableFunctionsSystemMessageToHistory(
   history: readonly ChatHistoryItem[], 
   availableFunctions?: ChatModelFunctions, 
   __namedParameters?: {
  documentParams?: boolean;
}): readonly ChatHistoryItem[];
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:82](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L82)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `history` | readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `availableFunctions?` | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) |
| `__namedParameters?` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`addAvailableFunctionsSystemMessageToHistory`](ChatWrapper.md#addavailablefunctionssystemmessagetohistory)

***

### generateContextState()

```ts
generateContextState(__namedParameters: ChatWrapperGenerateContextStateOptions): ChatWrapperGeneratedContextState;
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:113](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L113)

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

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:236](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L236)

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

***

### prependPreambleToChatHistory()

```ts
prependPreambleToChatHistory(chatHistory: readonly ChatHistoryItem[]): readonly ChatHistoryItem[];
```

Defined in: [chatWrappers/Llama3\_1ChatWrapper.ts:279](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/Llama3_1ChatWrapper.ts#L279)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `chatHistory` | readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |

#### Returns

readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]
