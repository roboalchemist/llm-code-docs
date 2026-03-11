# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatWrapperGeneratedInitiallyEngagedFunctionsContextState.md

---
url: /api/type-aliases/ChatWrapperGeneratedInitiallyEngagedFunctionsContextState.md
---
# Type Alias: ChatWrapperGeneratedInitiallyEngagedFunctionsContextState

```ts
type ChatWrapperGeneratedInitiallyEngagedFunctionsContextState = {
  contextText: LlamaText;
  stopGenerationTriggers: LlamaText[];
  ignoreStartText?: LlamaText[];
  functionCall?: {
     initiallyEngaged: boolean;
     disengageInitiallyEngaged: LlamaText[];
  };
  detectFunctionCalls?: never;
  prefixTriggers?: never;
  noPrefixTrigger?: never;
  rerender?: never;
};
```

Defined in: [types.ts:299](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L299)

## Properties

### contextText

```ts
contextText: LlamaText;
```

Defined in: [types.ts:300](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L300)

***

### stopGenerationTriggers

```ts
stopGenerationTriggers: LlamaText[];
```

Defined in: [types.ts:301](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L301)

***

### ignoreStartText?

```ts
optional ignoreStartText: LlamaText[];
```

Defined in: [types.ts:302](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L302)

***

### functionCall?

```ts
optional functionCall: {
  initiallyEngaged: boolean;
  disengageInitiallyEngaged: LlamaText[];
};
```

Defined in: [types.ts:303](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L303)

#### initiallyEngaged

```ts
initiallyEngaged: boolean;
```

#### disengageInitiallyEngaged

```ts
disengageInitiallyEngaged: LlamaText[];
```

***

### detectFunctionCalls?

```ts
optional detectFunctionCalls: never;
```

Defined in: [types.ts:308](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L308)

***

### prefixTriggers?

```ts
optional prefixTriggers: never;
```

Defined in: [types.ts:309](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L309)

***

### noPrefixTrigger?

```ts
optional noPrefixTrigger: never;
```

Defined in: [types.ts:310](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L310)

***

### rerender?

```ts
optional rerender: never;
```

Defined in: [types.ts:311](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L311)
