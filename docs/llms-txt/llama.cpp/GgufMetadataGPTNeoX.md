# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataGPTNeoX.md

---
url: /api/type-aliases/GgufMetadataGPTNeoX.md
---
# Type Alias: GgufMetadataGPTNeoX

```ts
type GgufMetadataGPTNeoX = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  use_parallel_residual: boolean;
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

Defined in: [gguf/types/GgufMetadataTypes.ts:476](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L476)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:477](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L477)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:478](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L478)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:479](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L479)

***

### use\_parallel\_residual

```ts
readonly use_parallel_residual: boolean;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:480](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L480)

***

### rope

```ts
readonly rope: {
  dimension_count: number;
  scale?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:481](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L481)

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

Defined in: [gguf/types/GgufMetadataTypes.ts:486](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L486)

#### head\_count

```ts
readonly head_count: number;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```
