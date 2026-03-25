# Source: https://node-llama-cpp.withcat.ai/api/classes/JinjaTemplateChatWrapper.md

---
url: /api/classes/JinjaTemplateChatWrapper.md
---
# Class: JinjaTemplateChatWrapper

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:147](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L147)

A chat wrapper based on a Jinja template.
Useful for using the original model's Jinja template as-is without any additional conversion work to chat with a model.

If you want to create a new chat wrapper from scratch, using this chat wrapper is not recommended, and instead you better inherit
from the `ChatWrapper` class and implement a custom chat wrapper of your own in TypeScript.

For a simpler way to create a chat wrapper, see the `TemplateChatWrapper` class.

## Example

```ts
import {JinjaTemplateChatWrapper} from "node-llama-cpp";

const chatWrapper = new JinjaTemplateChatWrapper({
    template: "<Jinja template here>",
    // functionCallMessageTemplate: { // optional
    //     call: "[[call: {{functionName}}({{functionParams}})]]",
    //     result: " [[result: {{functionCallResult}}]]"
    // },
    // segments: {
    //     thoughtTemplate: "<think>{{content}}</think>",
    //     reopenThoughtAfterFunctionCalls: true
    // }
});
```

## Extends

* [`ChatWrapper`](ChatWrapper.md)

## Constructors

### Constructor

```ts
new JinjaTemplateChatWrapper(options: JinjaTemplateChatWrapperOptions): JinjaTemplateChatWrapper;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:170](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L170)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | [`JinjaTemplateChatWrapperOptions`](../type-aliases/JinjaTemplateChatWrapperOptions.md) | - |

#### Returns

`JinjaTemplateChatWrapper`

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
readonly wrapperName: "JinjaTemplate" = "JinjaTemplate";
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:148](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L148)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`wrapperName`](ChatWrapper.md#wrappername)

***

### settings

```ts
readonly settings: ChatWrapperSettings;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:149](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L149)

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`settings`](ChatWrapper.md#settings)

***

### template

```ts
readonly template: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:151](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L151)

***

### modelRoleName

```ts
readonly modelRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:152](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L152)

***

### userRoleName

```ts
readonly userRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:153](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L153)

***

### systemRoleName

```ts
readonly systemRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:154](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L154)

***

### convertUnsupportedSystemMessagesToUserMessages?

```ts
readonly optional convertUnsupportedSystemMessagesToUserMessages: JinjaTemplateChatWrapperOptionsConvertMessageFormat;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:155](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L155)

***

### joinAdjacentMessagesOfTheSameType

```ts
readonly joinAdjacentMessagesOfTheSameType: boolean;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:156](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L156)

***

### trimLeadingWhitespaceInResponses

```ts
readonly trimLeadingWhitespaceInResponses: boolean;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:157](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L157)

***

### additionalRenderParameters?

```ts
readonly optional additionalRenderParameters: Record<string, any>;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:158](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L158)

## Accessors

### usingJinjaFunctionCallTemplate

#### Get Signature

```ts
get usingJinjaFunctionCallTemplate(): boolean;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:364](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L364)

Whether the function call syntax settings were extracted from the given Jinja template.

The function call syntax settings can be accessed using the `.settings.functions` property.

##### Returns

`boolean`

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

[`ChatWrapper`](ChatWrapper.md).[`generateAvailableFunctionsSystemText`](ChatWrapper.md#generateavailablefunctionssystemtext)

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
generateContextState(__namedParameters: ChatWrapperGenerateContextStateOptions): ChatWrapperGeneratedContextState & {
  transformedSystemMessagesToUserMessages: boolean;
};
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:368](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L368)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`ChatWrapperGenerateContextStateOptions`](../type-aliases/ChatWrapperGenerateContextStateOptions.md) |

#### Returns

[`ChatWrapperGeneratedContextState`](../type-aliases/ChatWrapperGeneratedContextState.md) & {
`transformedSystemMessagesToUserMessages`: `boolean`;
}

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`generateContextState`](ChatWrapper.md#generatecontextstate)

***

### addAvailableFunctionsSystemMessageToHistory()

```ts
addAvailableFunctionsSystemMessageToHistory(
   history: readonly ChatHistoryItem[], 
   availableFunctions?: ChatModelFunctions, 
   options?: {
  documentParams?: boolean;
}): readonly ChatHistoryItem[];
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:383](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L383)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `history` | readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `availableFunctions?` | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) |
| `options?` | { `documentParams?`: `boolean`; } |
| `options.documentParams?` | `boolean` |

#### Returns

readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]

#### Overrides

[`ChatWrapper`](ChatWrapper.md).[`addAvailableFunctionsSystemMessageToHistory`](ChatWrapper.md#addavailablefunctionssystemmessagetohistory)

***

### generateFunctionCall()

```ts
generateFunctionCall(name: string, params: any): LlamaText;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:394](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L394)

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

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:414](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L414)

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
