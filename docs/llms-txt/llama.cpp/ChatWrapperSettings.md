# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatWrapperSettings.md

---
url: /api/type-aliases/ChatWrapperSettings.md
---
# Type Alias: ChatWrapperSettings

```ts
type ChatWrapperSettings = {
  supportsSystemMessages: boolean;
  functions: {
     call: {
        optionalPrefixSpace: boolean;
        prefix: string | LlamaText;
        paramsPrefix: string | LlamaText;
        suffix: string | LlamaText;
        emptyCallParamsPlaceholder?: object | string | number | boolean | null;
     };
     result: {
        prefix: string | LlamaText;
        suffix: string | LlamaText;
     };
     parallelism?: {
        call: {
           sectionPrefix: string | LlamaText;
           sectionPrefixAlternateMatches?: (string | LlamaText)[];
           betweenCalls?: string | LlamaText;
           sectionSuffix?: string | LlamaText;
        };
        result?: {
           sectionPrefix?: string | LlamaText;
           betweenResults?: string | LlamaText;
           sectionSuffix?: string | LlamaText;
        };
     };
  };
  segments?: {
     closeAllSegments?: string | LlamaText;
     reiterateStackAfterFunctionCalls?: boolean;
     thought?: ChatWrapperSettingsSegment & {
        reopenAfterFunctionCalls?: boolean;
     };
     comment?: ChatWrapperSettingsSegment;
  };
};
```

Defined in: [types.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L22)

## Properties

### supportsSystemMessages

```ts
readonly supportsSystemMessages: boolean;
```

Defined in: [types.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L23)

***

### functions

```ts
readonly functions: {
  call: {
     optionalPrefixSpace: boolean;
     prefix: string | LlamaText;
     paramsPrefix: string | LlamaText;
     suffix: string | LlamaText;
     emptyCallParamsPlaceholder?: object | string | number | boolean | null;
  };
  result: {
     prefix: string | LlamaText;
     suffix: string | LlamaText;
  };
  parallelism?: {
     call: {
        sectionPrefix: string | LlamaText;
        sectionPrefixAlternateMatches?: (string | LlamaText)[];
        betweenCalls?: string | LlamaText;
        sectionSuffix?: string | LlamaText;
     };
     result?: {
        sectionPrefix?: string | LlamaText;
        betweenResults?: string | LlamaText;
        sectionSuffix?: string | LlamaText;
     };
  };
};
```

Defined in: [types.ts:24](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L24)

#### call

```ts
readonly call: {
  optionalPrefixSpace: boolean;
  prefix: string | LlamaText;
  paramsPrefix: string | LlamaText;
  suffix: string | LlamaText;
  emptyCallParamsPlaceholder?: object | string | number | boolean | null;
};
```

##### call.optionalPrefixSpace

```ts
readonly optionalPrefixSpace: boolean;
```

##### call.prefix

```ts
readonly prefix: string | LlamaText;
```

##### call.paramsPrefix

```ts
readonly paramsPrefix: string | LlamaText;
```

##### call.suffix

```ts
readonly suffix: string | LlamaText;
```

##### call.emptyCallParamsPlaceholder?

```ts
readonly optional emptyCallParamsPlaceholder: object | string | number | boolean | null;
```

The value to use when the function has no arguments.

Will be stringified using `jsonDumps`.

Defaults to `""`.

#### result

```ts
readonly result: {
  prefix: string | LlamaText;
  suffix: string | LlamaText;
};
```

##### result.prefix

```ts
readonly prefix: string | LlamaText;
```

Supported template parameters:

* `{{functionName}}`
* `{{functionParams}}`

Template parameters can only appear in a string or a string in a `LlamaText`.

Template parameters inside a `SpecialTokensText` inside a `LlamaText` won't be replaced.

Example of supported values:

* `"text{{functionName}}text"`
* `LlamaText(["text{{functionName}}text"])`

Example of unsupported values:

* `LlamaText([new SpecialTokensText("text{{functionName}}text")])`

##### result.suffix

```ts
readonly suffix: string | LlamaText;
```

Supported template parameters:

* `{{functionName}}`
* `{{functionParams}}`

Template parameters can only appear in a string or a string in a `LlamaText`.

Template parameters inside a `SpecialTokensText` inside a `LlamaText` won't be replaced.

Example of **supported** values:

* `"text{{functionName}}text"`
* `LlamaText(["text{{functionName}}text"])`

Example of **unsupported** values:

* `LlamaText([new SpecialTokensText("text{{functionName}}text")])`

#### parallelism?

```ts
readonly optional parallelism: {
  call: {
     sectionPrefix: string | LlamaText;
     sectionPrefixAlternateMatches?: (string | LlamaText)[];
     betweenCalls?: string | LlamaText;
     sectionSuffix?: string | LlamaText;
  };
  result?: {
     sectionPrefix?: string | LlamaText;
     betweenResults?: string | LlamaText;
     sectionSuffix?: string | LlamaText;
  };
};
```

If this field is present, parallel function calling is supported

##### parallelism.call

```ts
readonly call: {
  sectionPrefix: string | LlamaText;
  sectionPrefixAlternateMatches?: (string | LlamaText)[];
  betweenCalls?: string | LlamaText;
  sectionSuffix?: string | LlamaText;
};
```

##### parallelism.call.sectionPrefix

```ts
readonly sectionPrefix: string | LlamaText;
```

##### parallelism.call.sectionPrefixAlternateMatches?

```ts
readonly optional sectionPrefixAlternateMatches: (string | LlamaText)[];
```

Alternate section prefixes that can be used to detect a function call section,
but won't be used to construct the context when building it from scratch.

##### parallelism.call.betweenCalls?

```ts
readonly optional betweenCalls: string | LlamaText;
```

##### parallelism.call.sectionSuffix?

```ts
readonly optional sectionSuffix: string | LlamaText;
```

##### parallelism.result?

```ts
readonly optional result: {
  sectionPrefix?: string | LlamaText;
  betweenResults?: string | LlamaText;
  sectionSuffix?: string | LlamaText;
};
```

##### parallelism.result.sectionPrefix?

```ts
readonly optional sectionPrefix: string | LlamaText;
```

##### parallelism.result.betweenResults?

```ts
readonly optional betweenResults: string | LlamaText;
```

##### parallelism.result.sectionSuffix?

```ts
readonly optional sectionSuffix: string | LlamaText;
```

***

### segments?

```ts
readonly optional segments: {
  closeAllSegments?: string | LlamaText;
  reiterateStackAfterFunctionCalls?: boolean;
  thought?: ChatWrapperSettingsSegment & {
     reopenAfterFunctionCalls?: boolean;
  };
  comment?: ChatWrapperSettingsSegment;
};
```

Defined in: [types.ts:101](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L101)

#### closeAllSegments?

```ts
readonly optional closeAllSegments: string | LlamaText;
```

Consider all active segments to be closed when this text is detected

#### reiterateStackAfterFunctionCalls?

```ts
readonly optional reiterateStackAfterFunctionCalls: boolean;
```

After function calls, reiterate the stack of the active segments to remind the model of the context.

Defaults to `false`.

#### thought?

```ts
readonly optional thought: ChatWrapperSettingsSegment & {
  reopenAfterFunctionCalls?: boolean;
};
```

Chain of Thought text segment

##### Type Declaration

###### reopenAfterFunctionCalls?

```ts
optional reopenAfterFunctionCalls: boolean;
```

#### comment?

```ts
readonly optional comment: ChatWrapperSettingsSegment;
```

Comment segment.

Used by models such as gpt-oss.
