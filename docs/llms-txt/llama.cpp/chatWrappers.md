# Source: https://node-llama-cpp.withcat.ai/api/variables/chatWrappers.md

---
url: /api/variables/chatWrappers.md
---
# Variable: chatWrappers

```ts
const chatWrappers: Readonly<{
  general: typeof GeneralChatWrapper;
  deepSeek: typeof DeepSeekChatWrapper;
  qwen: typeof QwenChatWrapper;
  llama3.1: typeof Llama3_1ChatWrapper;
  llama3.2-lightweight: typeof Llama3_2LightweightChatWrapper;
  llama3: typeof Llama3ChatWrapper;
  llama2Chat: typeof Llama2ChatWrapper;
  mistral: typeof MistralChatWrapper;
  alpacaChat: typeof AlpacaChatWrapper;
  functionary: typeof FunctionaryChatWrapper;
  chatML: typeof ChatMLChatWrapper;
  falconChat: typeof FalconChatWrapper;
  gemma: typeof GemmaChatWrapper;
  harmony: typeof HarmonyChatWrapper;
  seed: typeof SeedChatWrapper;
  template: typeof TemplateChatWrapper;
  jinjaTemplate: typeof JinjaTemplateChatWrapper;
}>;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:46](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L46)
