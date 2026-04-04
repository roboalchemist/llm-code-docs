# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataDefaultArchitectureType.md

---
url: /api/type-aliases/GgufMetadataDefaultArchitectureType.md
---
# Type Alias: GgufMetadataDefaultArchitectureType

```ts
type GgufMetadataDefaultArchitectureType = {
  vocab_size?: number;
  context_length?: number;
  embedding_length?: number;
  block_count?: number;
  feed_forward_length?: number;
  use_parallel_residual?: boolean;
  tensor_data_layout?: string;
  expert_count?: number;
  expert_used_count?: number;
  pooling_type?: GgufMetadataArchitecturePoolingType;
  logit_scale?: number;
  token_shift_count?: number;
  attention?: {
     head_count?: number;
     head_count_kv?: number | number[];
     max_alibi_bias?: number;
     clamp_kqv?: number;
     layer_norm_epsilon?: number;
     layer_norm_rms_epsilon?: number;
     key_length?: number;
     value_length?: number;
     sliding_window?: number;
     causal?: boolean;
  };
  rope?: {
     dimension_count?: number;
     freq_base?: number;
     scale_linear?: number;
     scaling?: {
        type?: "none" | "linear" | "yarn" | string;
        factor?: number;
        original_context_length?: number;
        finetuned?: boolean;
     };
  };
  ssm?: {
     conv_kernel?: number;
     inner_size?: number;
     state_size?: number;
     time_step_rank?: number;
  };
  wkv?: {
     head_size?: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:350](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L350)

## Properties

### vocab\_size?

```ts
readonly optional vocab_size: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:351](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L351)

***

### context\_length?

```ts
readonly optional context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:352](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L352)

***

### embedding\_length?

```ts
readonly optional embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:353](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L353)

***

### block\_count?

```ts
readonly optional block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:354](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L354)

***

### feed\_forward\_length?

```ts
readonly optional feed_forward_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:355](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L355)

***

### use\_parallel\_residual?

```ts
readonly optional use_parallel_residual: boolean;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:356](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L356)

***

### tensor\_data\_layout?

```ts
readonly optional tensor_data_layout: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:357](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L357)

***

### expert\_count?

```ts
readonly optional expert_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:358](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L358)

***

### expert\_used\_count?

```ts
readonly optional expert_used_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:359](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L359)

***

### pooling\_type?

```ts
readonly optional pooling_type: GgufMetadataArchitecturePoolingType;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:360](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L360)

***

### logit\_scale?

```ts
readonly optional logit_scale: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:361](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L361)

***

### token\_shift\_count?

```ts
readonly optional token_shift_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:362](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L362)

***

### attention?

```ts
readonly optional attention: {
  head_count?: number;
  head_count_kv?: number | number[];
  max_alibi_bias?: number;
  clamp_kqv?: number;
  layer_norm_epsilon?: number;
  layer_norm_rms_epsilon?: number;
  key_length?: number;
  value_length?: number;
  sliding_window?: number;
  causal?: boolean;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:364](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L364)

#### head\_count?

```ts
readonly optional head_count: number;
```

#### head\_count\_kv?

```ts
readonly optional head_count_kv: number | number[];
```

#### max\_alibi\_bias?

```ts
readonly optional max_alibi_bias: number;
```

#### clamp\_kqv?

```ts
readonly optional clamp_kqv: number;
```

#### layer\_norm\_epsilon?

```ts
readonly optional layer_norm_epsilon: number;
```

#### layer\_norm\_rms\_epsilon?

```ts
readonly optional layer_norm_rms_epsilon: number;
```

#### key\_length?

```ts
readonly optional key_length: number;
```

#### value\_length?

```ts
readonly optional value_length: number;
```

#### sliding\_window?

```ts
readonly optional sliding_window: number;
```

#### causal?

```ts
readonly optional causal: boolean;
```

***

### rope?

```ts
readonly optional rope: {
  dimension_count?: number;
  freq_base?: number;
  scale_linear?: number;
  scaling?: {
     type?: "none" | "linear" | "yarn" | string;
     factor?: number;
     original_context_length?: number;
     finetuned?: boolean;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:377](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L377)

#### dimension\_count?

```ts
readonly optional dimension_count: number;
```

#### freq\_base?

```ts
readonly optional freq_base: number;
```

#### scale\_linear?

```ts
readonly optional scale_linear: number;
```

#### scaling?

```ts
readonly optional scaling: {
  type?: "none" | "linear" | "yarn" | string;
  factor?: number;
  original_context_length?: number;
  finetuned?: boolean;
};
```

##### scaling.type?

```ts
readonly optional type: "none" | "linear" | "yarn" | string;
```

##### scaling.factor?

```ts
readonly optional factor: number;
```

##### scaling.original\_context\_length?

```ts
readonly optional original_context_length: number;
```

##### scaling.finetuned?

```ts
readonly optional finetuned: boolean;
```

***

### ssm?

```ts
readonly optional ssm: {
  conv_kernel?: number;
  inner_size?: number;
  state_size?: number;
  time_step_rank?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:389](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L389)

#### conv\_kernel?

```ts
readonly optional conv_kernel: number;
```

#### inner\_size?

```ts
readonly optional inner_size: number;
```

#### state\_size?

```ts
readonly optional state_size: number;
```

#### time\_step\_rank?

```ts
readonly optional time_step_rank: number;
```

***

### wkv?

```ts
readonly optional wkv: {
  head_size?: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:396](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L396)

#### head\_size?

```ts
readonly optional head_size: number;
```
