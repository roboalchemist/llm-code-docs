# Source: https://node-llama-cpp.withcat.ai/api/functions/isChatModelResponseFunctionCall.md

---
url: /api/functions/isChatModelResponseFunctionCall.md
---
# Function: isChatModelResponseFunctionCall()

```ts
function isChatModelResponseFunctionCall(item: 
  | string
  | ChatModelFunctionCall
  | ChatModelSegment
  | undefined): item is ChatModelFunctionCall;
```

Defined in: [types.ts:379](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L379)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `item` | | `string` | [`ChatModelFunctionCall`](../type-aliases/ChatModelFunctionCall.md) | [`ChatModelSegment`](../type-aliases/ChatModelSegment.md) | `undefined` |

## Returns

`item is ChatModelFunctionCall`
