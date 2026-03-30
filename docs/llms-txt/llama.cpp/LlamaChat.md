# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaChat.md

---
url: /api/classes/LlamaChat.md
---
# Class: LlamaChat

Defined in: [evaluator/LlamaChat/LlamaChat.ts:515](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L515)

## Constructors

### Constructor

```ts
new LlamaChat(__namedParameters: LlamaChatOptions): LlamaChat;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:523](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L523)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`LlamaChatOptions`](../type-aliases/LlamaChatOptions.md) |

#### Returns

`LlamaChat`

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:521](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L521)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:566](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L566)

##### Returns

`boolean`

***

### chatWrapper

#### Get Signature

```ts
get chatWrapper(): ChatWrapper;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:570](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L570)

##### Returns

[`ChatWrapper`](ChatWrapper.md)

***

### sequence

#### Get Signature

```ts
get sequence(): LlamaContextSequence;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:577](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L577)

##### Returns

[`LlamaContextSequence`](LlamaContextSequence.md)

***

### context

#### Get Signature

```ts
get context(): LlamaContext;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:584](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L584)

##### Returns

[`LlamaContext`](LlamaContext.md)

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:588](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L588)

##### Returns

[`LlamaModel`](LlamaModel.md)

## Methods

### dispose()

```ts
dispose(__namedParameters?: {
  disposeSequence?: boolean;
}): void;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:549](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L549)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `disposeSequence?`: `boolean`; } |
| `__namedParameters.disposeSequence?` | `boolean` |

#### Returns

`void`

***

### generateResponse()

```ts
generateResponse<Functions>(history: ChatHistoryItem[], options?: LLamaChatGenerateResponseOptions<Functions>): Promise<LlamaChatResponse<Functions>>;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:592](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L592)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) | `undefined` | `undefined` |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `history` | [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `options` | [`LLamaChatGenerateResponseOptions`](../type-aliases/LLamaChatGenerateResponseOptions.md)<`Functions`> |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaChatResponse`](../type-aliases/LlamaChatResponse.md)<`Functions`>>

***

### loadChatAndCompleteUserMessage()

```ts
loadChatAndCompleteUserMessage<Functions>(history: ChatHistoryItem[], options?: LLamaChatLoadAndCompleteUserMessageOptions<Functions>): Promise<LlamaChatLoadAndCompleteUserResponse>;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:799](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L799)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) | `undefined` | `undefined` |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `history` | [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `options` | [`LLamaChatLoadAndCompleteUserMessageOptions`](../type-aliases/LLamaChatLoadAndCompleteUserMessageOptions.md)<`Functions`> |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaChatLoadAndCompleteUserResponse`](../type-aliases/LlamaChatLoadAndCompleteUserResponse.md)>
