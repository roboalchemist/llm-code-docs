# Source: https://node-llama-cpp.withcat.ai/api/functions/appendUserMessageToChatHistory.md

---
url: /api/functions/appendUserMessageToChatHistory.md
---
# Function: appendUserMessageToChatHistory()

```ts
function appendUserMessageToChatHistory(chatHistory: readonly ChatHistoryItem[], message: string): ChatHistoryItem[];
```

Defined in: [utils/appendUserMessageToChatHistory.ts:7](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/appendUserMessageToChatHistory.ts#L7)

Appends a user message to the chat history.
If the last message in the chat history is also a user message, the new message will be appended to it.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `chatHistory` | readonly [`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[] |
| `message` | `string` |

## Returns

[`ChatHistoryItem`](../type-aliases/ChatHistoryItem.md)\[]
