# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufFileInfo.md

---
url: /api/type-aliases/GgufFileInfo.md
---
# Type Alias: GgufFileInfo

```ts
type GgufFileInfo = {
  version: 2 | 3 | number;
  tensorCount: number | bigint;
  metadata: GgufMetadata;
  metadataSize: number;
  architectureMetadata: MergeOptionalUnionTypes<Exclude<GgufMetadata[GgufArchitectureType], undefined>>;
  tensorInfo?: GgufTensorInfo[];
  tensorInfoSize?: number;
  splicedParts: number;
  totalTensorCount: number | bigint;
  totalMetadataSize: number;
  fullTensorInfo?: GgufTensorInfo[];
  totalTensorInfoSize?: number;
};
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L13)

## Properties

### version

```ts
readonly version: 2 | 3 | number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L14)

***

### tensorCount

```ts
readonly tensorCount: number | bigint;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:15](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L15)

***

### metadata

```ts
readonly metadata: GgufMetadata;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L16)

***

### metadataSize

```ts
readonly metadataSize: number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L17)

***

### architectureMetadata

```ts
readonly architectureMetadata: MergeOptionalUnionTypes<Exclude<GgufMetadata[GgufArchitectureType], undefined>>;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:20](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L20)

Same value as `metadata[metadata.general.architecture]`, but with merged types for convenience

***

### tensorInfo?

```ts
readonly optional tensorInfo: GgufTensorInfo[];
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L23)

can be null if `readTensorInfo` is set to `false`

***

### tensorInfoSize?

```ts
readonly optional tensorInfoSize: number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:26](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L26)

can be null if `readTensorInfo` is set to `false`

***

### splicedParts

```ts
readonly splicedParts: number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:34](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L34)

For spliced metadata of multiple file parts,
this will be the number of files parts read and spliced into this metadata.

Whe no splicing is done, this will be `1`.

***

### totalTensorCount

```ts
readonly totalTensorCount: number | bigint;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L41)

For spliced metadata of multiple file parts, this will be the total tensor count from all the parts

When no splicing is done, this will be the same as `tensorCount`.

***

### totalMetadataSize

```ts
readonly totalMetadataSize: number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:48](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L48)

For spliced metadata of multiple file parts, this will be the total metadata size from all the parts

When no splicing is done, this will be the same as `metadataSize`.

***

### fullTensorInfo?

```ts
readonly optional fullTensorInfo: GgufTensorInfo[];
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:56](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L56)

For spliced metadata of multiple file parts, this will be the spliced tensorInfo from all the parts.
Can be null if `readTensorInfo` is set to `false`

When no splicing is done, this will be the same as `tensorInfo`.

***

### totalTensorInfoSize?

```ts
readonly optional totalTensorInfoSize: number;
```

Defined in: [gguf/types/GgufFileInfoTypes.ts:63](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufFileInfoTypes.ts#L63)

For spliced metadata of multiple file parts, this will be the total tensor info size from all the parts

When no splicing is done, this will be the same as `tensorInfoSize`.
