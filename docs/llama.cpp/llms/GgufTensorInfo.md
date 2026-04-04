# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufTensorInfo.md

---
url: /api/type-aliases/GgufTensorInfo.md
---
# Type Alias: GgufTensorInfo

```ts
type GgufTensorInfo = {
  name: string;
  dimensions: readonly (number | bigint)[];
  ggmlType: GgmlType;
  offset: number | bigint;
  fileOffset: number | bigint;
  filePart: number;
};
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:1](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L1)

## Properties

### name

```ts
readonly name: string;
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:2](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L2)

***

### dimensions

```ts
readonly dimensions: readonly (number | bigint)[];
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:3](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L3)

***

### ggmlType

```ts
readonly ggmlType: GgmlType;
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:4](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L4)

***

### offset

```ts
readonly offset: number | bigint;
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:5](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L5)

***

### fileOffset

```ts
readonly fileOffset: number | bigint;
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L12)

Adjusted offset relative to the file.

Added by the GGUF parser - not part of the file's metadata.

***

### filePart

```ts
readonly filePart: number;
```

Defined in: [gguf/types/GgufTensorInfoTypes.ts:20](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufTensorInfoTypes.ts#L20)

For spliced metadata of multiple file parts, this will be the file part number.
Starts from `1`.

Added by the GGUF parser - not part of the file's metadata.
