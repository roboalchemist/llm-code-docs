# Source: https://node-llama-cpp.withcat.ai/api/functions/LlamaLogLevelGreaterThan.md

---
url: /api/functions/LlamaLogLevelGreaterThan.md
---
# Function: LlamaLogLevelGreaterThan()

```ts
function LlamaLogLevelGreaterThan(a: LlamaLogLevel, b: LlamaLogLevel): boolean;
```

Defined in: [bindings/types.ts:126](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/types.ts#L126)

Check if a log level is higher than another log level

## Parameters

| Parameter | Type |
| ------ | ------ |
| `a` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |
| `b` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |

## Returns

`boolean`

## Example

```ts
LlamaLogLevelGreaterThan(LlamaLogLevel.error, LlamaLogLevel.info); // true
```
