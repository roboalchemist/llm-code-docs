# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GgufMetadata.md

---
url: /api/type-aliases/GgufMetadata.md
---
# Type Alias: GgufMetadata\<A>

```ts
type GgufMetadata<A> = {
  general: GgufMetadataGeneral<A>;
  tokenizer: GgufMetadataTokenizer;
} & GgufArchitectureType extends A ? { readonly [key in GgufArchitectureType]?: key extends keyof GgufMetadataLlmToType ? GgufMetadataLlmToType[key] : GgufMetadataDefaultArchitectureType } : { readonly [key in A]: key extends keyof GgufMetadataLlmToType ? GgufMetadataLlmToType[key] : GgufMetadataDefaultArchitectureType };
```

Defined in: [gguf/types/GgufMetadataTypes.ts:123](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L123)

## Type Declaration

### general

```ts
readonly general: GgufMetadataGeneral<A>;
```

### tokenizer

```ts
readonly tokenizer: GgufMetadataTokenizer;
```

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `A` *extends* [`GgufArchitectureType`](../enumerations/GgufArchitectureType.md) | [`GgufArchitectureType`](../enumerations/GgufArchitectureType.md) |
