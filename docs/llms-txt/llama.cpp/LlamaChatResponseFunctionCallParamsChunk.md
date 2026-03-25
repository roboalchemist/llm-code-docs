# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponseFunctionCallParamsChunk.md

---
url: /api/type-aliases/LlamaChatResponseFunctionCallParamsChunk.md
---
# Type Alias: LlamaChatResponseFunctionCallParamsChunk

```ts
type LlamaChatResponseFunctionCallParamsChunk = {
  callIndex: number;
  functionName: string;
  paramsChunk: string;
  done: boolean;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:110](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L110)

## Properties

### callIndex

```ts
callIndex: number;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:118](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L118)

Each different function call has a different `callIndex`.

When the previous function call has finished being generated, the `callIndex` of the next one will increment.

Use this value to distinguish between different function calls.

***

### functionName

```ts
functionName: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:123](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L123)

The name of the function being called

***

### paramsChunk

```ts
paramsChunk: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:133](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L133)

A chunk of the generated text used for the function call parameters.

Collect all the chunks together to construct the full function call parameters.

After the function call is finished, the entire constructed params text can be parsed as a JSON object,
according to the function parameters schema.

***

### done

```ts
done: boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:138](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L138)

When this is `true`, the current chunk is the last chunk in the generation of the current function call parameters.
