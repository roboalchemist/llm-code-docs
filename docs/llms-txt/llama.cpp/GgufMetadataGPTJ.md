# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataGPTJ.md

---
url: /api/type-aliases/GgufMetadataGPTJ.md
---
# Type Alias: GgufMetadataGPTJ

```ts
type GgufMetadataGPTJ = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  rope: {
     dimension_count: number;
     scale?: number;
  };
  attention: {
     head_count: number;
     layer_norm_epsilon: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:493](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L493)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:494](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L494)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:495](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L495)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:496](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L496)

***

### rope

```ts
readonly rope: {
  dimension_count: number;
  scale?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:497](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L497)

#### dimension\_count

```ts
readonly dimension_count: number;
```

#### scale?

```ts
readonly optional scale: number;
```

***

### attention

```ts
readonly attention: {
  head_count: number;
  layer_norm_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:501](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L501)

#### head\_count

```ts
readonly head_count: number;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```
