# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ResolveChatWrapperWithModelOptions.md

---
url: /api/type-aliases/ResolveChatWrapperWithModelOptions.md
---
# Type Alias: ResolveChatWrapperWithModelOptions

```ts
type ResolveChatWrapperWithModelOptions = {
  type?:   | "auto"
     | SpecializedChatWrapperTypeName
     | TemplateChatWrapperTypeName;
  customWrapperSettings?: { [wrapper in keyof typeof chatWrappers]?: typeof JinjaTemplateChatWrapper extends typeof chatWrappers[wrapper] ? Partial<ConstructorParameters<typeof chatWrappers[wrapper]>[0]> : ConstructorParameters<typeof chatWrappers[wrapper]>[0] };
  warningLogs?: boolean;
  fallbackToOtherWrappersOnJinjaError?: boolean;
  noJinja?: boolean;
};
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:113](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L113)

## Properties

### type?

```ts
optional type: 
  | "auto"
  | SpecializedChatWrapperTypeName
  | TemplateChatWrapperTypeName;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:120](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L120)

Resolve to a specific chat wrapper type.
You better not set this option unless you need to force a specific chat wrapper type.

Defaults to `"auto"`.

***

### customWrapperSettings?

```ts
optional customWrapperSettings: { [wrapper in keyof typeof chatWrappers]?: typeof JinjaTemplateChatWrapper extends typeof chatWrappers[wrapper] ? Partial<ConstructorParameters<typeof chatWrappers[wrapper]>[0]> : ConstructorParameters<typeof chatWrappers[wrapper]>[0] };
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:122](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L122)

***

### warningLogs?

```ts
optional warningLogs: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:131](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L131)

Defaults to `true`.

***

### fallbackToOtherWrappersOnJinjaError?

```ts
optional fallbackToOtherWrappersOnJinjaError: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:136](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L136)

Defaults to `true`.

***

### noJinja?

```ts
optional noJinja: boolean;
```

Defined in: [chatWrappers/utils/resolveChatWrapper.ts:143](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/resolveChatWrapper.ts#L143)

Don't resolve to a Jinja chat wrapper unless `type` is set to a Jinja chat wrapper type.

Defaults to `false`.
