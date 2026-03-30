# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataLlmLLaMA.md

---
url: /api/type-aliases/GgufMetadataLlmLLaMA.md
---
# Type Alias: GgufMetadataLlmLLaMA

```ts
type GgufMetadataLlmLLaMA = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  feed_forward_length: number;
  attention: {
     head_count: number;
     layer_norm_rms_epsilon: number;
     head_count_kv?: number;
  };
  rope: {
     dimension_count: number;
     scale?: number;
  };
  expert_count?: number;
  expert_used_count?: number;
  tensor_data_layout?: string;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:443](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L443)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:444](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L444)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:445](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L445)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:446](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L446)

***

### feed\_forward\_length

```ts
readonly feed_forward_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:447](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L447)

***

### attention

```ts
readonly attention: {
  head_count: number;
  layer_norm_rms_epsilon: number;
  head_count_kv?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:448](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L448)

#### head\_count

```ts
readonly head_count: number;
```

#### layer\_norm\_rms\_epsilon

```ts
readonly layer_norm_rms_epsilon: number;
```

#### head\_count\_kv?

```ts
readonly optional head_count_kv: number;
```

***

### rope

```ts
readonly rope: {
  dimension_count: number;
  scale?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:453](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L453)

#### dimension\_count

```ts
readonly dimension_count: number;
```

#### scale?

```ts
readonly optional scale: number;
```

***

### expert\_count?

```ts
readonly optional expert_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:457](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L457)

***

### expert\_used\_count?

```ts
readonly optional expert_used_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:458](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L458)

***

### tensor\_data\_layout?

```ts
readonly optional tensor_data_layout: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:459](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L459)
