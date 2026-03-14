# Source: https://node-llama-cpp.withcat.ai/api/classes/HarmonyChatWrapper.md

---
url: /api/classes/HarmonyChatWrapper.md
---
# Class: HarmonyChatWrapper

Defined in: [chatWrappers/HarmonyChatWrapper.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L15)

## Extends

* [`ChatWrapper`](ChatWrapper.md)

## Constructors

### Constructor

```ts
new HarmonyChatWrapper(options?: {
  modelIdentity?: string | null;
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
  reasoningEffort?: "medium" | "high" | "low" | null;
  requiredChannels?: {
     analysis?: boolean;
     commentary?: boolean;
     final?: boolean;
  };
  keepOnlyLastThought?: boolean;
}): HarmonyChatWrapper;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:58](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L58)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `modelIdentity?`: `string` | `null`; `cuttingKnowledgeDate?`: | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null`; `todayDate?`: | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null`; `reasoningEffort?`: `"medium"` | `"high"` | `"low"` | `null`; `requiredChannels?`: { `analysis?`: `boolean`; `commentary?`: `boolean`; `final?`: `boolean`; }; `keepOnlyLastThought?`: `boolean`; } | - |
| `options.modelIdentity?` | `string` | `null` | The model identity to use in the internal system message. Set to `null` to disable. Defaults to `"You are ChatGPT, a large language model trained by OpenAI."` |
| `options.cuttingKnowledgeDate?` | | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null` | Set to `null` to disable Defaults to `new Date("2024-06-01T00:00:00Z")` |
| `options.todayDate?` | | `string` | `number` | [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | () => [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | `null` | Set to `null` to disable Defaults to the current date |
| `options.reasoningEffort?` | `"medium"` | `"high"` | `"low"` | `null` | The amount of reasoning to instruct the model to use. Not enforced, it's up to the model to follow this instruction. Set to `null` to omit the instruction. Defaults to `"medium"`. |
| `options.requiredChannels?` | { `analysis?`: `boolean`; `commentary?`: `boolean`; `final?`: `boolean`; } | - |
| `options.requiredChannels.analysis?` | `boolean` | Defaults to `true` |
| `options.requiredChannels.commentary?` | `boolean` | Defaults to `true` |
| `options.requiredChannels.final?` | `boolean` | Defaults to `true` |
| `options.keepOnlyLastThought?` | `boolean` | Whether to keep only the chain of thought from the last model response. Setting this to `false` will keep all the chain of thoughts from the model responses in the context state. Defaults to `true`. |

#### Returns

`HarmonyChatWrapper`

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
readonly wrapperName: string = "Harmony";
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L16)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`wrapperName`](ChatWrapper.md#wrappername)

***

### modelIdentity

```ts
readonly modelIdentity: string | null;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:18](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L18)

***

### cuttingKnowledgeDate?

```ts
readonly optional cuttingKnowledgeDate: 
  | Date
  | () => Date
  | null;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:19](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L19)

***

### todayDate

```ts
readonly todayDate: 
  | Date
  | () => Date
  | null;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:20](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L20)

***

### reasoningEffort

```ts
readonly reasoningEffort: "medium" | "high" | "low" | null;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:21](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L21)

***

### requiredChannels

```ts
readonly requiredChannels: {
  analysis: boolean;
  commentary: boolean;
  final: boolean;
};
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L22)

#### analysis

```ts
analysis: boolean;
```

#### commentary

```ts
commentary: boolean;
```

#### final

```ts
final: boolean;
```

***

### keepOnlyLastThought

```ts
readonly keepOnlyLastThought: boolean;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:27](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L27)

***

### settings

```ts
readonly settings: ChatWrapperSettings;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L31)

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

Defined in: [chatWrappers/HarmonyChatWrapper.ts:164](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L164)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateContextStateOptions`](../type-aliases/ChatWrapperGenerateContextStateOptions.md) |

#### Returns

[`ChatWrapperGeneratedContextState`](../type-aliases/ChatWrapperGeneratedContextState.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateContextState`](ChatWrapper.md#generatecontextstate)

***

### generateFunctionCall()

```ts
generateFunctionCall(name: string, params: any): LlamaText;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:314](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L314)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `params` | `any` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateFunctionCall`](ChatWrapper.md#generatefunctioncall)

***

### generateFunctionCallResult()

```ts
generateFunctionCallResult(
   functionName: string, 
   functionParams: any, 
   result: any): LlamaText;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:329](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L329)

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

### generateModelResponseText()

```ts
generateModelResponseText(modelResponse: (
  | string
  | ChatModelFunctionCall
  | ChatModelSegment)[], useRawValues?: boolean): LlamaText;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:343](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L343)

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `modelResponse` | ( | `string` | [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md) | [`ChatModelSegment`](../type-aliases/ChatModelSegment.md))\[] | `undefined` |
| `useRawValues` | `boolean` | `true` |

#### Returns

[`LlamaText`](LlamaText.md)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateModelResponseText`](ChatWrapper.md#generatemodelresponsetext)

***

### generateAvailableFunctionsSystemText()

```ts
generateAvailableFunctionsSystemText(availableFunctions: ChatModelFunctions, __namedParameters: {
  documentParams?: boolean;
}): LlamaText;
```

Defined in: [chatWrappers/HarmonyChatWrapper.ts:364](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/HarmonyChatWrapper.ts#L364)

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
