# Source: https://node-llama-cpp.withcat.ai/api/functions/isChatModelResponseSegment.md

---
url: /api/functions/isChatModelResponseSegment.md
---
# Function: isChatModelResponseSegment()

```ts
function isChatModelResponseSegment(item: 
  | string
  | ChatModelFunctionCall
  | ChatModelSegment
  | undefined): item is ChatModelSegment;
```

Defined in: [types.ts:386](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L386)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `item` | | `string` | [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md) | [`ChatModelSegment`](../type-aliases/ChatModelSegment.md) | `undefined` |

## Returns

`item is ChatModelSegment`
