# Source: https://node-llama-cpp.withcat.ai/api/classes/AlpacaChatWrapper.md

---
url: /api/classes/AlpacaChatWrapper.md
---
# Class: AlpacaChatWrapper

Defined in: [chatWrappers/AlpacaChatWrapper.ts:8](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L8)

This chat wrapper is not safe against chat syntax injection attacks
([learn more](https://node-llama-cpp.withcat.ai/guide/llama-text#input-safety-in-node-llama-cpp)).

## Extends

* [`GeneralChatWrapper`](GeneralChatWrapper.md)

## Constructors

### Constructor

```ts
new AlpacaChatWrapper(__namedParameters?: {
  userMessageTitle?: string;
  modelResponseTitle?: string;
  middleSystemMessageTitle?: string;
  allowSpecialTokensInTitles?: boolean;
}): AlpacaChatWrapper;
```

Defined in: [chatWrappers/AlpacaChatWrapper.ts:11](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L11)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `userMessageTitle?`: `string`; `modelResponseTitle?`: `string`; `middleSystemMessageTitle?`: `string`; `allowSpecialTokensInTitles?`: `boolean`; } |
| `__namedParameters.userMessageTitle?` | `string` |
| `__namedParameters.modelResponseTitle?` | `string` |
| `__namedParameters.middleSystemMessageTitle?` | `string` |
| `__namedParameters.allowSpecialTokensInTitles?` | `boolean` |

#### Returns

`AlpacaChatWrapper`

#### Overrides

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`constructor`](GeneralChatWrapper.md#constructor)

## Properties

### defaultSettings

```ts
static defaultSettings: ChatWrapperSettings;
```

Defined in: [ChatWrapper.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L14)

#### Inherited from

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`defaultSettings`](GeneralChatWrapper.md#defaultsettings)

***

### settings

```ts
readonly settings: ChatWrapperSettings = ChatWrapper.defaultSettings;
```

Defined in: [ChatWrapper.ts:33](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L33)

#### Inherited from

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`settings`](GeneralChatWrapper.md#settings)

***

### wrapperName

```ts
readonly wrapperName: string = "AlpacaChat";
```

Defined in: [chatWrappers/AlpacaChatWrapper.ts:9](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L9)

#### Overrides

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`wrapperName`](GeneralChatWrapper.md#wrappername)

## Accessors

### userMessageTitle

#### Get Signature

```ts
get userMessageTitle(): string;
```

Defined in: [chatWrappers/AlpacaChatWrapper.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L25)

##### Returns

`string`

#### Overrides

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`userMessageTitle`](GeneralChatWrapper.md#usermessagetitle)

***

### modelResponseTitle

#### Get Signature

```ts
get modelResponseTitle(): string;
```

Defined in: [chatWrappers/AlpacaChatWrapper.ts:29](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L29)

##### Returns

`string`

#### Overrides

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`modelResponseTitle`](GeneralChatWrapper.md#modelresponsetitle)

***

### middleSystemMessageTitle

#### Get Signature

```ts
get middleSystemMessageTitle(): string;
```

Defined in: [chatWrappers/AlpacaChatWrapper.ts:33](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/AlpacaChatWrapper.ts#L33)

##### Returns

`string`

#### Overrides

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`middleSystemMessageTitle`](GeneralChatWrapper.md#middlesystemmessagetitle)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateFunctionCallsAndResults`](GeneralChatWrapper.md#generatefunctioncallsandresults)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateFunctionCall`](GeneralChatWrapper.md#generatefunctioncall)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateFunctionCallResult`](GeneralChatWrapper.md#generatefunctioncallresult)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateModelResponseText`](GeneralChatWrapper.md#generatemodelresponsetext)

***

### generateAvailableFunctionsSystemText()

```ts
generateAvailableFunctionsSystemText(availableFunctions: ChatModelFunctions, __namedParameters: {
  documentParams?: boolean;
}): LlamaText;
```

Defined in: [ChatWrapper.ts:238](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/ChatWrapper.ts#L238)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `availableFunctions` | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) |
| `__namedParameters` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Inherited from

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateAvailableFunctionsSystemText`](GeneralChatWrapper.md#generateavailablefunctionssystemtext)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`addAvailableFunctionsSystemMessageToHistory`](GeneralChatWrapper.md#addavailablefunctionssystemmessagetohistory)

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

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateInitialChatHistory`](GeneralChatWrapper.md#generateinitialchathistory)

***

### generateContextState()

```ts
generateContextState(__namedParameters: ChatWrapperGenerateContextStateOptions): ChatWrapperGeneratedContextState;
```

Defined in: [chatWrappers/GeneralChatWrapper.ts:43](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/GeneralChatWrapper.ts#L43)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateContextStateOptions`](../type-aliases/ChatWrapperGenerateContextStateOptions.md) |

#### Returns

[`ChatWrapperGeneratedContextState`](../type-aliases/ChatWrapperGeneratedContextState.md)

#### Inherited from

[`GeneralChatWrapper`](GeneralChatWrapper.md).[`generateContextState`](GeneralChatWrapper.md#generatecontextstate)
