# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataMamba.md

---
url: /api/type-aliases/GgufMetadataMamba.md
---
# Type Alias: GgufMetadataMamba

```ts
type GgufMetadataMamba = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  ssm: {
     conv_kernel: number;
     inner_size: number;
     state_size: number;
     time_step_rank: number;
  };
  attention: {
     layer_norm_rms_epsilon: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:545](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L545)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:546](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L546)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:547](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L547)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:548](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L548)

***

### ssm

```ts
readonly ssm: {
  conv_kernel: number;
  inner_size: number;
  state_size: number;
  time_step_rank: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:549](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L549)

#### conv\_kernel

```ts
readonly conv_kernel: number;
```

#### inner\_size

```ts
readonly inner_size: number;
```

#### state\_size

```ts
readonly state_size: number;
```

#### time\_step\_rank

```ts
readonly time_step_rank: number;
```

***

### attention

```ts
readonly attention: {
  layer_norm_rms_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:555](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L555)

#### layer\_norm\_rms\_epsilon

```ts
readonly layer_norm_rms_epsilon: number;
```
