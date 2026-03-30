# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatWrapperGenerateContextStateOptions.md

---
url: /api/type-aliases/ChatWrapperGenerateContextStateOptions.md
---
# Type Alias: ChatWrapperGenerateContextStateOptions

```ts
type ChatWrapperGenerateContextStateOptions = {
  chatHistory: readonly ChatHistoryItem[];
  availableFunctions?: ChatModelFunctions;
  documentFunctionParams?: boolean;
};
```

Defined in: [types.ts:130](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L130)

## Properties

### chatHistory

```ts
chatHistory: readonly ChatHistoryItem[];
```

Defined in: [types.ts:131](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L131)

***

### availableFunctions?

```ts
optional availableFunctions: ChatModelFunctions;
```

Defined in: [types.ts:132](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L132)

***

### documentFunctionParams?

```ts
optional documentFunctionParams: boolean;
```

Defined in: [types.ts:133](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L133)
