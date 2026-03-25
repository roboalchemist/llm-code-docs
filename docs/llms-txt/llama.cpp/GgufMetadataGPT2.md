# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataGPT2.md

---
url: /api/type-aliases/GgufMetadataGPT2.md
---
# Type Alias: GgufMetadataGPT2

```ts
type GgufMetadataGPT2 = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  attention: {
     head_count: number;
     layer_norm_epsilon: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:508](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L508)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:509](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L509)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:510](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L510)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:511](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L511)

***

### attention

```ts
readonly attention: {
  head_count: number;
  layer_norm_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:512](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L512)

#### head\_count

```ts
readonly head_count: number;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```
