# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadataGeneral.md

---
url: /api/type-aliases/GgufMetadataGeneral.md
---
# Type Alias: GgufMetadataGeneral\<A>

```ts
type GgufMetadataGeneral<A> = {
  architecture: A;
  quantization_version: string;
  alignment?: number;
  name?: string;
  basename?: string;
  size_label?: string;
  author?: string;
  url?: string;
  description?: string;
  license?: string;
  license.name?: string;
  license.link?: string;
  source?: {
     url?: string;
     huggingface?: {
        repository?: string;
     };
  };
  file_type?: GgufFileType;
  base_model?: {
   [key: `${bigint}`]: {
     name?: string;
     author?: string;
     version?: string;
     organization?: string;
     url?: string;
     doi?: string;
     uuid?: string;
     repo_url?: string;
   };
     count: number;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:196](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L196)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `A` *extends* [`GgufArchitectureType`](../enumerations/GgufArchitectureType.md) | [`GgufArchitectureType`](../enumerations/GgufArchitectureType.md) |

## Properties

### architecture

```ts
readonly architecture: A;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:197](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L197)

***

### quantization\_version

```ts
readonly quantization_version: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:207](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L207)

The version of the quantization format. Not required if the model is not
quantized (i.e. no tensors are quantized). If any tensors are quantized,
this must be present. This is separate to the quantization scheme of the
tensors itself; the quantization version may change without changing the
scheme's name (e.g. the quantization scheme is Q5\_K, and the quantization
version is 4).

***

### alignment?

```ts
readonly optional alignment: number;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:215](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L215)

the global alignment to use, as described above. This can vary to allow
for different alignment schemes, but it must be a multiple of 8. Some
writers may not write the alignment. If the alignment is not specified,
assume it is `32`.

***

### name?

```ts
readonly optional name: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:222](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L222)

The name of the model. This should be a human-readable name that can be
used to identify the model. It should be unique within the community
that the model is defined in.

***

### basename?

```ts
readonly optional basename: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:223](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L223)

***

### size\_label?

```ts
readonly optional size_label: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:224](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L224)

***

### author?

```ts
readonly optional author: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:225](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L225)

***

### url?

```ts
readonly optional url: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:230](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L230)

URL to the model's homepage. This can be a GitHub repo, a paper, etc.

***

### description?

```ts
readonly optional description: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:236](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L236)

free-form description of the model including anything that isn't
covered by the other fields

***

### license?

```ts
readonly optional license: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:243](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L243)

License of the model, expressed as a SPDX license expression
(e.g. `MIT OR Apache-2.0`). *Should not* include any other information,
such as the license text or the URL to the license.

***

### license.name?

```ts
readonly optional license.name: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:244](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L244)

***

### license.link?

```ts
readonly optional license.link: string;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:245](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L245)

***

### source?

```ts
readonly optional source: {
  url?: string;
  huggingface?: {
     repository?: string;
  };
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:253](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L253)

Information about where this model came from. This is useful for tracking
the provenance of the model, and for finding the original source if the
model is modified. For a model that was converted from GGML, for
example, these keys would point to the model that was converted from.

#### url?

```ts
readonly optional url: string;
```

URL to the source of the model. Can be a GitHub repo, a paper, etc.

#### huggingface?

```ts
readonly optional huggingface: {
  repository?: string;
};
```

##### huggingface.repository?

```ts
readonly optional repository: string;
```

***

### file\_type?

```ts
readonly optional file_type: GgufFileType;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:267](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L267)

An enumerated value describing the type of the majority of the tensors
in the file. Optional; can be inferred from the tensor types.

***

### base\_model?

```ts
readonly optional base_model: {
[key: `${bigint}`]: {
  name?: string;
  author?: string;
  version?: string;
  organization?: string;
  url?: string;
  doi?: string;
  uuid?: string;
  repo_url?: string;
};
  count: number;
};
```

Defined in: [gguf/types/GgufMetadataTypes.ts:269](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L269)

#### Index Signature

```ts
[key: `${bigint}`]: {
  name?: string;
  author?: string;
  version?: string;
  organization?: string;
  url?: string;
  doi?: string;
  uuid?: string;
  repo_url?: string;
}
```

#### count

```ts
readonly count: number;
```
