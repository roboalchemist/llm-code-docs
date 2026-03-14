# Source: https://node-llama-cpp.withcat.ai/api/functions/isGgufMetadataOfArchitectureType.md

---
url: /api/functions/isGgufMetadataOfArchitectureType.md
---
# Function: isGgufMetadataOfArchitectureType()

```ts
function isGgufMetadataOfArchitectureType<A>(metadata: GgufMetadata, type: A): metadata is GgufMetadata<A>;
```

Defined in: [gguf/types/GgufMetadataTypes.ts:560](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/types/GgufMetadataTypes.ts#L560)

## Type Parameters

| Type Parameter |
| ------ |
| `A` *extends* [`GgufArchitectureType`](../enumerations/GgufArchitectureType.md) |

## Parameters

| Parameter | Type |
| ------ | ------ |
| `metadata` | [`GgufMetadata`](../type-aliases/GgufMetadata.md) |
| `type` | `A` |

## Returns

`metadata is GgufMetadata<A>`
