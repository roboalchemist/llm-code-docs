# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataFalcon.md

---
url: /api/type-aliases/GgufMetadataFalcon.md
---
# Type Alias: GgufMetadataFalcon

```ts
type GgufMetadataFalcon = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  attention: {
     head_count: number;
     head_count_kv: number;
     use_norm: boolean;
     layer_norm_epsilon: number;
  };
  tensor_data_layout?: string;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:531](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L531)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:532](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L532)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:533](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L533)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:534](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L534)

***

### attention

```ts
readonly attention: {
  head_count: number;
  head_count_kv: number;
  use_norm: boolean;
  layer_norm_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:535](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L535)

#### head\_count

```ts
readonly head_count: number;
```

#### head\_count\_kv

```ts
readonly head_count_kv: number;
```

#### use\_norm

```ts
readonly use_norm: boolean;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```

***

### tensor\_data\_layout?

```ts
readonly optional tensor_data_layout: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:541](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L541)
