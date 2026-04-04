# Source: https://node-llama-cpp.withcat.ai/api/functions/jsonDumps.md

---
url: /api/functions/jsonDumps.md
---
# Function: jsonDumps()

```ts
function jsonDumps(value: any): string;
```

Defined in: [chatWrappers/utils/jsonDumps.ts:7](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/jsonDumps.ts#L7)

Like `JSON.stringify` but results in a value formatted in the format that Python produces when using `json.dumps(value)`.

We need to format results this way since this is what many models use in their training data,
so this is what many models expect to have in their context state.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | `any` |

## Returns

`string`
