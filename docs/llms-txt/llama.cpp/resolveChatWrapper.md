# Source: https://node-llama-cpp.withcat.ai/api/functions/resolveChatWrapper.md

---
url: /api/functions/resolveChatWrapper.md
---
# Function: resolveChatWrapper()

## Call Signature

```ts
function resolveChatWrapper(model: LlamaModel, options?: ResolveChatWrapperWithModelOptions): BuiltInChatWrapperType;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:188](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L188)

Resolve to a chat wrapper instance based on the provided information.
The more information provided, the better the resolution will be (except for `type`).

It's recommended to not set `type` to a specific chat wrapper in order for the resolution to be more flexible, but it is useful for when
you need to provide the ability to force a specific chat wrapper type.
Note that when setting `type` to a generic chat wrapper type (such as `"template"` or `"jinjaTemplate"`), the `customWrapperSettings`
must contain the necessary settings for that chat wrapper to be created.

When loading a Jinja chat template from either `fileInfo` or `customWrapperSettings.jinjaTemplate.template`,
if the chat template format is invalid, it fallbacks to resolve other chat wrappers,
unless `fallbackToOtherWrappersOnJinjaError` is set to `false` (in which case, it will throw an error).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `model` | [`LlamaModel`](../classes/LlamaModel.md) |
| `options?` | [`ResolveChatWrapperWithModelOptions`](../type-aliases/ResolveChatWrapperWithModelOptions.md) |

### Returns

[`BuiltInChatWrapperType`](../type-aliases/BuiltInChatWrapperType.md)

### Examples

```typescript
import {getLlama, resolveChatWrapper, GeneralChatWrapper} from "node-llama-cpp";

const llama = await getLlama();
const model = await llama.loadModel({modelPath: "path/to/model.gguf"});

const chatWrapper = resolveChatWrapper(model, {
    customWrapperSettings: {
        "llama3.1": {
            cuttingKnowledgeDate: new Date("2025-01-01T00:00:00Z")
        }
    }
}) ?? new GeneralChatWrapper()
```

```typescript
import {getLlama, resolveChatWrapper, GeneralChatWrapper} from "node-llama-cpp";

const llama = await getLlama();
const model = await llama.loadModel({modelPath: "path/to/model.gguf"});

const chatWrapper = resolveChatWrapper({
    bosString: model.tokens.bosString,
    filename: model.filename,
    fileInfo: model.fileInfo,
    tokenizer: model.tokenizer
}) ?? new GeneralChatWrapper()
```

## Call Signature

```ts
function resolveChatWrapper(options: ResolveChatWrapperOptions): 
  | BuiltInChatWrapperType
  | null;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:189](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L189)

Resolve to a chat wrapper instance based on the provided information.
The more information provided, the better the resolution will be (except for `type`).

It's recommended to not set `type` to a specific chat wrapper in order for the resolution to be more flexible, but it is useful for when
you need to provide the ability to force a specific chat wrapper type.
Note that when setting `type` to a generic chat wrapper type (such as `"template"` or `"jinjaTemplate"`), the `customWrapperSettings`
must contain the necessary settings for that chat wrapper to be created.

When loading a Jinja chat template from either `fileInfo` or `customWrapperSettings.jinjaTemplate.template`,
if the chat template format is invalid, it fallbacks to resolve other chat wrappers,
unless `fallbackToOtherWrappersOnJinjaError` is set to `false` (in which case, it will throw an error).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`ResolveChatWrapperOptions`](../type-aliases/ResolveChatWrapperOptions.md) |

### Returns

| [`BuiltInChatWrapperType`](../type-aliases/BuiltInChatWrapperType.md)
| `null`

### Examples

```typescript
import {getLlama, resolveChatWrapper, GeneralChatWrapper} from "node-llama-cpp";

const llama = await getLlama();
const model = await llama.loadModel({modelPath: "path/to/model.gguf"});

const chatWrapper = resolveChatWrapper(model, {
    customWrapperSettings: {
        "llama3.1": {
            cuttingKnowledgeDate: new Date("2025-01-01T00:00:00Z")
        }
    }
}) ?? new GeneralChatWrapper()
```

```typescript
import {getLlama, resolveChatWrapper, GeneralChatWrapper} from "node-llama-cpp";

const llama = await getLlama();
const model = await llama.loadModel({modelPath: "path/to/model.gguf"});

const chatWrapper = resolveChatWrapper({
    bosString: model.tokens.bosString,
    filename: model.filename,
    fileInfo: model.fileInfo,
    tokenizer: model.tokenizer
}) ?? new GeneralChatWrapper()
```
