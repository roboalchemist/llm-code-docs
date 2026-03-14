# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataBloom.md

---
url: /api/type-aliases/GgufMetadataBloom.md
---
# Type Alias: GgufMetadataBloom

```ts
type GgufMetadataBloom = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  feed_forward_length: number;
  attention: {
     head_count: number;
     layer_norm_epsilon: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:519](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L519)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:520](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L520)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:521](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L521)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:522](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L522)

***

### feed\_forward\_length

```ts
readonly feed_forward_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:523](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L523)

***

### attention

```ts
readonly attention: {
  head_count: number;
  layer_norm_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:524](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L524)

#### head\_count

```ts
readonly head_count: number;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```
