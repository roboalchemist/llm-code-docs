# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponseFunctionCall.md

---
url: /api/type-aliases/LlamaChatResponseFunctionCall.md
---
# Type Alias: LlamaChatResponseFunctionCall\<Functions, FunctionCallName, Params>

```ts
type LlamaChatResponseFunctionCall<Functions, FunctionCallName, Params> = {
  functionName: FunctionCallName;
  params: Params;
  raw: LlamaTextJSON;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1074](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1074)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* [`ChatModelFunctions`](ChatModelFunctions.md) | - |
| `FunctionCallName` *extends* keyof `Functions` & `string` | `string` & keyof `Functions` |
| `Params` | `Functions`\[`FunctionCallName`]\[`"params"`] *extends* `undefined` | `null` | `void` ? `undefined` : [`GbnfJsonSchemaToType`](GbnfJsonSchemaToType.md)<`Functions`\[`FunctionCallName`]\[`"params"`]> |

## Properties

### functionName

```ts
functionName: FunctionCallName;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1081](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1081)

***

### params

```ts
params: Params;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1082](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1082)

***

### raw

```ts
raw: LlamaTextJSON;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1083](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1083)
