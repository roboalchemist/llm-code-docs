# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/JinjaTemplateChatWrapperOptions.md

---
url: /api/type-aliases/JinjaTemplateChatWrapperOptions.md
---
# Type Alias: JinjaTemplateChatWrapperOptions

```ts
type JinjaTemplateChatWrapperOptions = {
  template: string;
  modelRoleName?: string;
  userRoleName?: string;
  systemRoleName?: string;
  convertUnsupportedSystemMessagesToUserMessages?:   | "auto"
     | boolean
     | JinjaTemplateChatWrapperOptionsConvertMessageFormat;
  functionCallMessageTemplate?:   | "auto"
     | "noJinja"
     | ChatHistoryFunctionCallMessageTemplate;
  joinAdjacentMessagesOfTheSameType?: boolean;
  trimLeadingWhitespaceInResponses?: boolean;
  additionalRenderParameters?: Record<string, any>;
  segments?: TemplateChatWrapperSegmentsOptions;
  tokenizer?: Tokenizer;
};
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L25)

## Properties

### template

```ts
template: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:26](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L26)

***

### modelRoleName?

```ts
optional modelRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L31)

Defaults to `"assistant"`.

***

### userRoleName?

```ts
optional userRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:36](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L36)

Defaults to `"user"`.

***

### systemRoleName?

```ts
optional systemRoleName: string;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L41)

Defaults to `"system"`.

***

### convertUnsupportedSystemMessagesToUserMessages?

```ts
optional convertUnsupportedSystemMessagesToUserMessages: 
  | "auto"
  | boolean
  | JinjaTemplateChatWrapperOptionsConvertMessageFormat;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:58](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L58)

Some Jinja templates may not support system messages, and in such cases,
it'll be detected and system messages can be converted to user messages.

You can specify the format of the converted user message.

* **"auto"**: Convert system messages to user messages only if the template does not support system messages.
* **`true`**: Always convert system messages to user messages.
* **`false`**: Never convert system messages to user messages.
  May throw an error if some system messages don't appear in the template.
* **`{use: "ifNeeded", format: "..."}`**: Convert system messages to user messages only if the template does not support system
  messages with the specified format.
* **`{use: "always", format: "..."}`**: Always convert system messages to user messages with the specified format.

Defaults to `"auto"`.

***

### functionCallMessageTemplate?

```ts
optional functionCallMessageTemplate: 
  | "auto"
  | "noJinja"
  | ChatHistoryFunctionCallMessageTemplate;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:71](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L71)

Template format for how functions can be called by the model and how their results are fed to the model after function calls.

* **`"auto"`**: Extract the function call message template from the Jinja template.
  Fallback to the default template if not found.
* **`"noJinja"`**: Use the default template.
* **Custom template**: Use the specified [template](ChatHistoryFunctionCallMessageTemplate.md).
  See [\`ChatHistoryFunctionCallMessageTemplate\`](ChatHistoryFunctionCallMessageTemplate.md) for more details.

Defaults to `"auto"`.

***

### joinAdjacentMessagesOfTheSameType?

```ts
optional joinAdjacentMessagesOfTheSameType: boolean;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:79](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L79)

Whether to join adjacent messages of the same type.
Some Jinja templates may throw an error if this is not set to `true`.

Defaults to `true`.

***

### trimLeadingWhitespaceInResponses?

```ts
optional trimLeadingWhitespaceInResponses: boolean;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:86](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L86)

Whether to trim leading whitespace in responses.

Defaults to `true`.

***

### additionalRenderParameters?

```ts
optional additionalRenderParameters: Record<string, any>;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:91](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L91)

Additional parameters to use for rendering the Jinja template.

***

### segments?

```ts
optional segments: TemplateChatWrapperSegmentsOptions;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:96](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L96)

Format of the segments generated by the model (like thought segments)

***

### tokenizer?

```ts
optional tokenizer: Tokenizer;
```

Defined in: [chatWrappers/generic/JinjaTemplateChatWrapper.ts:103](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/JinjaTemplateChatWrapper.ts#L103)

Pass a model's tokenizer to attempt to detect common tokens used for chat formatting from it.

Currently only used for detecting support for `<think>` tags for thought segments.
