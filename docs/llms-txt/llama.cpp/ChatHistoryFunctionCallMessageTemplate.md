# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatHistoryFunctionCallMessageTemplate.md

---
url: /api/type-aliases/ChatHistoryFunctionCallMessageTemplate.md
---
# Type Alias: ChatHistoryFunctionCallMessageTemplate

```ts
type ChatHistoryFunctionCallMessageTemplate = {
  call: `${string}{{functionName}}${string}{{functionParams}}${string}`;
  result: `${string}{{functionCallResult}}${string}`;
};
```

Defined in: [chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts:81](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts#L81)

Template format for how functions can be called by the model and how their results are fed to the model after function calls.

Consists of an object with two properties:

1. **`call`**: The function call template.
2. **`result`**: The function call result template.

For example:

```ts
const template: ChatHistoryFunctionCallMessageTemplate = {
    call: "[[call: {{functionName}}({{functionParams}})]]",
    result: " [[result: {{functionCallResult}}]]"
};
```

It's mandatory for the call template to have text before `{{functionName}}` in order for the chat wrapper know when
to activate the function calling grammar.

## Properties

### call

```ts
call: `${string}{{functionName}}${string}{{functionParams}}${string}`;
```

Defined in: [chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts:82](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts#L82)

***

### result

```ts
result: `${string}{{functionCallResult}}${string}`;
```

Defined in: [chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts:83](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/chatHistoryFunctionCallMessageTemplate.ts#L83)
