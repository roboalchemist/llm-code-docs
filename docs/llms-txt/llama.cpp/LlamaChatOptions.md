# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatOptions.md

---
url: /api/type-aliases/LlamaChatOptions.md
---
# Type Alias: LlamaChatOptions

```ts
type LlamaChatOptions = {
  contextSequence: LlamaContextSequence;
  chatWrapper?: "auto" | ChatWrapper;
  autoDisposeSequence?: boolean;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L35)

## Properties

### contextSequence

```ts
contextSequence: LlamaContextSequence;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:36](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L36)

***

### chatWrapper?

```ts
optional chatWrapper: "auto" | ChatWrapper;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:39](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L39)

`"auto"` is used by default

***

### autoDisposeSequence?

```ts
optional autoDisposeSequence: boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:46](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L46)

Automatically dispose the sequence when the session is disposed

Defaults to `false`.
