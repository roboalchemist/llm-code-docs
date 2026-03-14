# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/TemplateChatWrapperSegmentsOptions.md

---
url: /api/type-aliases/TemplateChatWrapperSegmentsOptions.md
---
# Type Alias: TemplateChatWrapperSegmentsOptions

```ts
type TemplateChatWrapperSegmentsOptions = {
  thoughtTemplate?: `${string}{{content}}${string}`;
  reopenThoughtAfterFunctionCalls?: boolean;
  closeAllSegmentsTemplate?: string;
  reiterateStackAfterFunctionCalls?: boolean;
};
```

Defined in: [chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts:39](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts#L39)

## Properties

### thoughtTemplate?

```ts
optional thoughtTemplate: `${string}{{content}}${string}`;
```

Defined in: [chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts#L41)

Template for a thought segment

***

### reopenThoughtAfterFunctionCalls?

```ts
optional reopenThoughtAfterFunctionCalls: boolean;
```

Defined in: [chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts:50](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts#L50)

Automatically reopen a thought segment after function calls.

Useful for aligning the output of models that assume that a thought segment is already open after function calls.

Defaults to `false`.

***

### closeAllSegmentsTemplate?

```ts
optional closeAllSegmentsTemplate: string;
```

Defined in: [chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts:53](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts#L53)

Consider all segments to be closed when this text is detected

***

### reiterateStackAfterFunctionCalls?

```ts
optional reiterateStackAfterFunctionCalls: boolean;
```

Defined in: [chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts:60](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/generic/utils/templateSegmentOptionsToChatWrapperSettings.ts#L60)

After function calls, reiterate the stack of the active segments to remind the model of the context.

Defaults to `false`.
