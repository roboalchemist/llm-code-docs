# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatSessionOptions.md

---
url: /api/type-aliases/LlamaChatSessionOptions.md
---
# Type Alias: LlamaChatSessionOptions

```ts
type LlamaChatSessionOptions = {
  contextSequence: LlamaContextSequence;
  chatWrapper?: "auto" | ChatWrapper;
  systemPrompt?: string;
  forceAddSystemPrompt?: boolean;
  autoDisposeSequence?: boolean;
  contextShift?: LlamaChatSessionContextShiftOptions;
};
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L25)

## Properties

### contextSequence

```ts
contextSequence: LlamaContextSequence;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:26](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L26)

***

### chatWrapper?

```ts
optional chatWrapper: "auto" | ChatWrapper;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:29](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L29)

`"auto"` is used by default

***

### systemPrompt?

```ts
optional systemPrompt: string;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L31)

***

### forceAddSystemPrompt?

```ts
optional forceAddSystemPrompt: boolean;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L41)

Add the system prompt even on models that don't support a system prompt.

Each chat wrapper has its own workaround for adding a system prompt to a model that doesn't support it,
but forcing the system prompt on unsupported models may not always work as expected.

Use with caution.

***

### autoDisposeSequence?

```ts
optional autoDisposeSequence: boolean;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:48](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L48)

Automatically dispose the sequence when the session is disposed.

Defaults to `false`.

***

### contextShift?

```ts
optional contextShift: LlamaChatSessionContextShiftOptions;
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:50](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L50)
