# Source: https://node-llama-cpp.withcat.ai/api/functions/LlamaLogLevelGreaterThanOrEqual.md

---
url: /api/functions/LlamaLogLevelGreaterThanOrEqual.md
---
# Function: LlamaLogLevelGreaterThanOrEqual()

```ts
function LlamaLogLevelGreaterThanOrEqual(a: LlamaLogLevel, b: LlamaLogLevel): boolean;
```

Defined in: [bindings/types.ts:138](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/types.ts#L138)

Check if a log level is higher than or equal to another log level

## Parameters

| Parameter | Type |
| ------ | ------ |
| `a` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |
| `b` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |

## Returns

`boolean`

## Example

```ts
LlamaLogLevelGreaterThanOrEqual(LlamaLogLevel.error, LlamaLogLevel.info); // true
LlamaLogLevelGreaterThanOrEqual(LlamaLogLevel.error, LlamaLogLevel.error); // true
```
