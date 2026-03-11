# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataMPT.md

---
url: /api/type-aliases/GgufMetadataMPT.md
---
# Type Alias: GgufMetadataMPT

```ts
type GgufMetadataMPT = {
  context_length: number;
  embedding_length: number;
  block_count: number;
  attention: {
     head_count: number;
     alibi_bias_max: number;
     clip_kqv: number;
     layer_norm_epsilon: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:463](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L463)

## Properties

### context\_length

```ts
readonly context_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:464](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L464)

***

### embedding\_length

```ts
readonly embedding_length: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:465](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L465)

***

### block\_count

```ts
readonly block_count: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:466](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L466)

***

### attention

```ts
readonly attention: {
  head_count: number;
  alibi_bias_max: number;
  clip_kqv: number;
  layer_norm_epsilon: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:467](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L467)

#### head\_count

```ts
readonly head_count: number;
```

#### alibi\_bias\_max

```ts
readonly alibi_bias_max: number;
```

#### clip\_kqv

```ts
readonly clip_kqv: number;
```

#### layer\_norm\_epsilon

```ts
readonly layer_norm_epsilon: number;
```
