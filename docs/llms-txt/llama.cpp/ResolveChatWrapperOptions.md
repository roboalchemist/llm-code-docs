# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ResolveChatWrapperOptions.md

---
url: /api/type-aliases/ResolveChatWrapperOptions.md
---
# Type Alias: ResolveChatWrapperOptions

```ts
type ResolveChatWrapperOptions = {
  type?:   | "auto"
     | SpecializedChatWrapperTypeName
     | TemplateChatWrapperTypeName;
  bosString?: string | null;
  filename?: string;
  fileInfo?: GgufFileInfo;
  tokenizer?: Tokenizer;
  customWrapperSettings?: { [wrapper in keyof typeof chatWrappers]?: ConstructorParameters<typeof chatWrappers[wrapper]>[0] };
  warningLogs?: boolean;
  fallbackToOtherWrappersOnJinjaError?: boolean;
  noJinja?: boolean;
};
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:78](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L78)

## Properties

### type?

```ts
optional type: 
  | "auto"
  | SpecializedChatWrapperTypeName
  | TemplateChatWrapperTypeName;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:85](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L85)

Resolve to a specific chat wrapper type.
You better not set this option unless you need to force a specific chat wrapper type.

Defaults to `"auto"`.

***

### bosString?

```ts
optional bosString: string | null;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:87](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L87)

***

### filename?

```ts
optional filename: string;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:88](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L88)

***

### fileInfo?

```ts
optional fileInfo: GgufFileInfo;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:89](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L89)

***

### tokenizer?

```ts
optional tokenizer: Tokenizer;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:90](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L90)

***

### customWrapperSettings?

```ts
optional customWrapperSettings: { [wrapper in keyof typeof chatWrappers]?: ConstructorParameters<typeof chatWrappers[wrapper]>[0] };
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:91](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L91)

***

### warningLogs?

```ts
optional warningLogs: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:98](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L98)

Defaults to `true`.

***

### fallbackToOtherWrappersOnJinjaError?

```ts
optional fallbackToOtherWrappersOnJinjaError: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:103](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L103)

Defaults to `true`.

***

### noJinja?

```ts
optional noJinja: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:110](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L110)

Don't resolve to a Jinja chat wrapper unless `type` is set to a Jinja chat wrapper type.

Defaults to `false`.
