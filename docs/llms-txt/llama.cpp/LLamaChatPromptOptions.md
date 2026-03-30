# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LLamaChatPromptOptions.md

---
url: /api/type-aliases/LLamaChatPromptOptions.md
---
# Type Alias: LLamaChatPromptOptions\<Functions>

```ts
type LLamaChatPromptOptions<Functions> = {
  onTextChunk?: (text: string) => void;
  onToken?: (tokens: Token[]) => void;
  onResponseChunk?: (chunk: LlamaChatResponseChunk) => void;
  signal?: AbortSignal;
  stopOnAbortSignal?: boolean;
  maxTokens?: number;
  temperature?: number;
  minP?: number;
  topK?: number;
  topP?: number;
  seed?: number;
  xtc?: {
     probability: number;
     threshold: number;
  };
  trimWhitespaceSuffix?: boolean;
  responsePrefix?: string;
  evaluationPriority?: EvaluationPriority;
  repeatPenalty?:   | false
     | LlamaChatSessionRepeatPenalty;
  dryRepeatPenalty?: LlamaChatSessionDryRepeatPenalty;
  tokenBias?:   | TokenBias
     | () => TokenBias;
  customStopTriggers?: (LlamaText | string | (string | Token)[])[];
  onFunctionCallParamsChunk?: (chunk: LlamaChatResponseFunctionCallParamsChunk) => void;
  budgets?: {
     thoughtTokens?: number;
     commentTokens?: number;
  };
} & 
  | {
  grammar?: LlamaGrammar;
  functions?: never;
  documentFunctionParams?: never;
  maxParallelFunctionCalls?: never;
  onFunctionCallParamsChunk?: never;
}
  | {
  grammar?: never;
  functions?: Functions | ChatSessionModelFunctions;
  documentFunctionParams?: boolean;
  maxParallelFunctionCalls?: number;
  onFunctionCallParamsChunk?: (chunk: LlamaChatResponseFunctionCallParamsChunk) => void;
};
```

Defined in: [evaluator/LlamaChatSession/LlamaChatSession.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/LlamaChatSession.ts#L68)

## Type Declaration

### onTextChunk()?

```ts
optional onTextChunk: (text: string) => void;
```

Called as the model generates the main response with the generated text chunk.

Useful for streaming the generated response as it's being generated.

Includes only the main response without any text segments (like thoughts).
For streaming the response with segments, use \`onResponseChunk\`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `text` | `string` |

#### Returns

`void`

### onToken()?

```ts
optional onToken: (tokens: Token[]) => void;
```

Called as the model generates the main response with the generated tokens.

Preferably, you'd want to use \`onTextChunk\` instead of this.

Includes only the main response without any segments (like thoughts).
For streaming the response with segments, use \`onResponseChunk\`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](Token.md)\[] |

#### Returns

`void`

### onResponseChunk()?

```ts
optional onResponseChunk: (chunk: LlamaChatResponseChunk) => void;
```

Called as the model generates a response with the generated text and tokens,
including segment information (when the generated output is part of a segment).

Useful for streaming the generated response as it's being generated, including the main response and all segments.

Only use this function when you need the segmented texts, like thought segments (chain of thought text).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `chunk` | [`LlamaChatResponseChunk`](LlamaChatResponseChunk.md) |

#### Returns

`void`

### signal?

```ts
optional signal: AbortSignal;
```

An AbortSignal to later abort the generation.

When the signal is aborted, the generation will stop and throw `signal.reason` as the error.

> To stop an ongoing generation without throwing an error, also set `stopOnAbortSignal` to `true`.

### stopOnAbortSignal?

```ts
optional stopOnAbortSignal: boolean;
```

When a response already started being generated and then the signal is aborted,
the generation will stop and the response will be returned as is instead of throwing an error.

Defaults to `false`.

### maxTokens?

```ts
optional maxTokens: number;
```

Maximum number of tokens to generate

### temperature?

```ts
optional temperature: number;
```

Temperature is a hyperparameter that controls the randomness of the generated text.
It affects the probability distribution of the model's output tokens.

A higher temperature (e.g., 1.5) makes the output more random and creative,
while a lower temperature (e.g., 0.5) makes the output more focused, deterministic, and conservative.

The suggested temperature is 0.8, which provides a balance between randomness and determinism.

At the extreme, a temperature of 0 will always pick the most likely next token, leading to identical outputs in each run.

Set to `0` to disable.
Disabled by default (set to `0`).

### minP?

```ts
optional minP: number;
```

From the next token candidates, discard the percentage of tokens with the lowest probability.
For example, if set to `0.05`, 5% of the lowest probability tokens will be discarded.
This is useful for generating more high-quality results when using a high temperature.
Set to a value between `0` and `1` to enable.

Only relevant when `temperature` is set to a value greater than `0`.
Disabled by default.

### topK?

```ts
optional topK: number;
```

Limits the model to consider only the K most likely next tokens for sampling at each step of sequence generation.
An integer number between `1` and the size of the vocabulary.
Set to `0` to disable (which uses the full vocabulary).

Only relevant when `temperature` is set to a value greater than 0.

### topP?

```ts
optional topP: number;
```

Dynamically selects the smallest set of tokens whose cumulative probability exceeds the threshold P,
and samples the next token only from this set.
A float number between `0` and `1`.
Set to `1` to disable.

Only relevant when `temperature` is set to a value greater than `0`.

### seed?

```ts
optional seed: number;
```

Used to control the randomness of the generated text.

Change the seed to get different results.

Only relevant when using `temperature`.

### xtc?

```ts
optional xtc: {
  probability: number;
  threshold: number;
};
```

Exclude Top Choices (XTC) removes the top tokens from consideration and avoids more obvious and repetitive generations.
Using it leads to more creative responses, but also to increased hallucinations.

The `probability` value controls the chance that the top tokens will be removed in the next token generation step.
The `threshold` value control the minimum probability of a token for it to be removed.

Start with `{probability: 0.5, threshold: 0.1}` and adjust from there.

Disabled by default.

#### xtc.probability

```ts
probability: number;
```

A number between `0` and `1` representing the probability of applying Exclude Top Choices (XTC) at each token generation step.

#### xtc.threshold

```ts
threshold: number;
```

A number between `0` and `1` representing the minimum probability
of a token for it to be removed when applying Exclude Top Choices (XTC).

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: boolean;
```

Trim whitespace from the end of the generated text
Disabled by default.

### responsePrefix?

```ts
optional responsePrefix: string;
```

Force a given text prefix to be the start of the model response, to make the model follow a certain direction.

May cause some models to not use the given functions in some scenarios where they would have been used otherwise,
so avoid using it together with function calling if you notice unexpected behavior.

### evaluationPriority?

```ts
optional evaluationPriority: EvaluationPriority;
```

See the parameter `evaluationPriority` on the `LlamaContextSequence.evaluate()` function for more information.

### repeatPenalty?

```ts
optional repeatPenalty: 
  | false
  | LlamaChatSessionRepeatPenalty;
```

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LlamaChatSessionDryRepeatPenalty;
```

DRY (Don't Repeat Yourself) penalty is a technique to reduce repetitions in the generated text
by penalizing tokens based on recent token usage patterns.

With the right parameters choice, it makes it impossible for the model to
repeat itself verbatim with the same tokens in the same order (the model can still repeat itself by
using different tokens or by paraphrasing, but that is far less of an issue than a broken-record looping).

Disabled by default.

### tokenBias?

```ts
optional tokenBias: 
  | TokenBias
  | () => TokenBias;
```

Adjust the probability of tokens being generated.
Can be used to bias the model to generate tokens that you want it to lean towards,
or to avoid generating tokens that you want it to avoid.

### customStopTriggers?

```ts
optional customStopTriggers: (LlamaText | string | (string | Token)[])[];
```

Custom stop triggers to stop the generation of the response when any of the provided triggers are found.

### onFunctionCallParamsChunk()?

```ts
optional onFunctionCallParamsChunk: (chunk: LlamaChatResponseFunctionCallParamsChunk) => void;
```

Called as the model generates function calls with the generated parameters chunk for each function call.

Useful for streaming the generated function call parameters as they're being generated.
Only useful in specific use cases,
such as showing the generated textual file content as it's being generated (note that doing this requires parsing incomplete JSON).

The constructed text from all the params chunks of a given function call can be parsed as a JSON object,
according to the function parameters schema.

Each function call has its own `callIndex` you can use to distinguish between them.

Only relevant when using function calling (via passing the `functions` option).

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `chunk` | [`LlamaChatResponseFunctionCallParamsChunk`](LlamaChatResponseFunctionCallParamsChunk.md) |

#### Returns

`void`

### budgets?

```ts
optional budgets: {
  thoughtTokens?: number;
  commentTokens?: number;
};
```

Set the maximum number of tokens that the model is allowed to spend on various segmented responses.

#### budgets.thoughtTokens?

```ts
optional thoughtTokens: number;
```

Budget for thought tokens.

Defaults to `Infinity`.

#### budgets.commentTokens?

```ts
optional commentTokens: number;
```

Budget for comment tokens.

Defaults to `Infinity`.

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Functions` *extends* [`ChatSessionModelFunctions`](ChatSessionModelFunctions.md) | `undefined` | [`ChatSessionModelFunctions`](ChatSessionModelFunctions.md) | `undefined` |
