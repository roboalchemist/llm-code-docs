# Source: https://node-llama-cpp.withcat.ai/api/functions/getLlamaGpuTypes.md

---
url: /api/functions/getLlamaGpuTypes.md
---
# Function: getLlamaGpuTypes()

```ts
function getLlamaGpuTypes(include: "supported" | "allValid"): Promise<LlamaGpuType[]>;
```

Defined in: [bindings/utils/getLlamaGpuTypes.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/utils/getLlamaGpuTypes.ts#L17)

Get the list of GPU types that can be used with `getLlama` on the current machine.

When passing `"supported"`, only the GPU types that have the
necessary libraries and drivers installed on the current machine will be returned.
All of these GPU types have prebuilt binaries for the current platform and architecture.

When passing `"allValid"`, all GPU types that are compatible with the current OS and architecture will be returned.
Some of these GPU types may not have prebuilt binaries for the current platform and architecture,
as some of them are inadvisable for the current machine (like CUDA on an x64 Mac machine).

## Parameters

| Parameter | Type |
| ------ | ------ |
| `include` | `"supported"` | `"allValid"` |

## Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaGpuType`](../type-aliases/LlamaGpuType.md)\[]>
