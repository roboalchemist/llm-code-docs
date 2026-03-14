# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatWrapperGeneratedPrefixTriggersContextState.md

---
url: /api/type-aliases/ChatWrapperGeneratedPrefixTriggersContextState.md
---
# Type Alias: ChatWrapperGeneratedPrefixTriggersContextState

```ts
type ChatWrapperGeneratedPrefixTriggersContextState = {
  contextText: LlamaText;
  stopGenerationTriggers: LlamaText[];
  prefixTriggers?: (
     | {
     triggers: LlamaText[];
     type: "functionCall";
     replaceTrigger?: boolean;
     inject?: LlamaText;
   }
     | {
     triggers: LlamaText[];
     type: "segment";
     segmentType: ChatModelSegmentType;
     inject?: LlamaText;
   }
     | {
     triggers: LlamaText[];
     type: "response";
     inject?: LlamaText;
  })[];
  noPrefixTrigger?:   | {
     type: "functionCall";
     inject: LlamaText;
   }
     | {
     type: "segment";
     segmentType: ChatModelSegmentType;
     inject: LlamaText;
   }
     | {
     type: "response";
     inject: LlamaText;
   };
  rerender?: {
     triggers: LlamaText[];
     action?: "closeResponseItem";
  };
  detectFunctionCalls?: boolean;
  ignoreStartText?: never;
  functionCall?: never;
};
```

Defined in: [types.ts:144](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L144)

## Properties

### contextText

```ts
contextText: LlamaText;
```

Defined in: [types.ts:148](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L148)

The rendered chat to load into the context sequence state

***

### stopGenerationTriggers

```ts
stopGenerationTriggers: LlamaText[];
```

Defined in: [types.ts:153](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L153)

Triggers to stop the generation

***

### prefixTriggers?

```ts
optional prefixTriggers: (
  | {
  triggers: LlamaText[];
  type: "functionCall";
  replaceTrigger?: boolean;
  inject?: LlamaText;
}
  | {
  triggers: LlamaText[];
  type: "segment";
  segmentType: ChatModelSegmentType;
  inject?: LlamaText;
}
  | {
  triggers: LlamaText[];
  type: "response";
  inject?: LlamaText;
})[];
```

Defined in: [types.ts:164](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L164)

When this option is set, after evaluating the `contextText`,
it'll look for any of the triggers to be the first generated output.

When a trigger is matched, its type will determine the mode to enter to, a segment to open,
or to continue the generation as a textual output.

If all the triggers are unmatched, the `noPrefixTrigger` will take effect.

***

### noPrefixTrigger?

```ts
optional noPrefixTrigger: 
  | {
  type: "functionCall";
  inject: LlamaText;
}
  | {
  type: "segment";
  segmentType: ChatModelSegmentType;
  inject: LlamaText;
}
  | {
  type: "response";
  inject: LlamaText;
};
```

Defined in: [types.ts:226](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L226)

When no prefix triggers are matched or non are provided, after evaluating the `contextText`,
perform the action specified by this option.

#### Type Declaration

```ts
{
  type: "functionCall";
  inject: LlamaText;
}
```

#### type

```ts
type: "functionCall";
```

Enter into function calling mode.

Entering this mode will put the function calling prefix into the context sequence state
and force it to choose a function to call.

If no functions are available, this action will be ignored.

#### inject

```ts
inject: LlamaText;
```

Text to inject into the context sequence state when this action is performed.

```ts
{
  type: "segment";
  segmentType: ChatModelSegmentType;
  inject: LlamaText;
}
```

#### type

```ts
type: "segment";
```

Open a segment of the specified type.

If the budget for this segment has exceeded, this action will be ignored.

#### segmentType

```ts
segmentType: ChatModelSegmentType;
```

Type of the segment to open.

#### inject

```ts
inject: LlamaText;
```

Text to inject into the context sequence state when this action is performed.

```ts
{
  type: "response";
  inject: LlamaText;
}
```

#### type

```ts
type: "response";
```

Continue the generation as a textual output.

#### inject

```ts
inject: LlamaText;
```

Text to inject into the context sequence state when this action is performed.

***

### rerender?

```ts
optional rerender: {
  triggers: LlamaText[];
  action?: "closeResponseItem";
};
```

Defined in: [types.ts:278](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L278)

Trigger a rerender of the chat template when any of the provided triggers are matched.

When a rerender it triggered, the chat template will be rendered again and the next trigger options will come into effect again,
so if no prefix triggers are required after the rerender, make sure to not provide any.

When a rerender is triggered, the `action` will be performed.

#### triggers

```ts
triggers: LlamaText[];
```

#### action?

```ts
optional action: "closeResponseItem";
```

Action to perform when the rerender is triggered.

* **`"closeResponseItem"`**: Close the current segment or stop the textual response generation.

***

### detectFunctionCalls?

```ts
optional detectFunctionCalls: boolean;
```

Defined in: [types.ts:294](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L294)

Whether to detect the function calling prefix syntax in the current text generation to dynamically enter into function calling mode.

If it's only possible to enter function calling using a prefix trigger, then set this option to `false`.

***

### ignoreStartText?

```ts
optional ignoreStartText: never;
```

Defined in: [types.ts:296](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L296)

***

### functionCall?

```ts
optional functionCall: never;
```

Defined in: [types.ts:297](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L297)
