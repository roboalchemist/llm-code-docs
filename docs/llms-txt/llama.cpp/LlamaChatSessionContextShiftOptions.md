# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatSessionContextShiftOptions.md

---
url: /api/type-aliases/LlamaChatSessionContextShiftOptions.md
---
# Type Alias: LlamaChatSessionContextShiftOptions

```ts
type LlamaChatSessionContextShiftOptions = {
  size?: LLamaChatContextShiftOptions["size"];
  strategy?: LLamaChatContextShiftOptions["strategy"];
};
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:53](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L53)

## Properties

### size?

```ts
optional size: LLamaChatContextShiftOptions["size"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:58](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L58)

The number of tokens to delete from the context window to make space for new ones.
Defaults to 10% of the context size.

***

### strategy?

```ts
optional strategy: LLamaChatContextShiftOptions["strategy"];
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:65](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L65)

The strategy to use when deleting tokens from the context window.

Defaults to `"eraseFirstResponseAndKeepFirstSystem"`.
