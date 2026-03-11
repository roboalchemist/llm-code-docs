# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaCompletionGenerationOptions.md

---
url: /api/type-aliases/LlamaCompletionGenerationOptions.md
---
# Type Alias: LlamaCompletionGenerationOptions

```ts
type LlamaCompletionGenerationOptions = {
  onTextChunk?: (text: string) => void;
  onToken?: (tokens: Token[]) => void;
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
  repeatPenalty?:   | false
     | LLamaContextualRepeatPenalty;
  dryRepeatPenalty?: LLamaContextualDryRepeatPenalty;
  tokenBias?:   | TokenBias
     | () => TokenBias;
  evaluationPriority?: EvaluationPriority;
  grammar?: LlamaGrammar;
  customStopTriggers?: readonly (LlamaText | string | readonly (string | Token)[])[];
  contextShiftSize?:   | number
     | (sequence: LlamaContextSequence) => 
     | number
     | Promise<number>;
  disableContextShift?: boolean;
};
```

Defined in: [evaluator/LlamaCompletion.ts:33](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L33)

## Properties

### onTextChunk()?

```ts
optional onTextChunk: (text: string) => void;
```

Defined in: [evaluator/LlamaCompletion.ts:39](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L39)

Called as the model generates a completion with the generated text chunk.

Useful for streaming the generated completion as it's being generated.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `text` | `string` |

#### Returns

`void`

***

### onToken()?

```ts
optional onToken: (tokens: Token[]) => void;
```

Defined in: [evaluator/LlamaCompletion.ts:46](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L46)

Called as the model generates a completion with the generated tokens.

Preferably, you'd want to use `onTextChunk` instead of this.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](Token.md)\[] |

#### Returns

`void`

***

### signal?

```ts
optional signal: AbortSignal;
```

Defined in: [evaluator/LlamaCompletion.ts:55](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L55)

An AbortSignal to later abort the generation.

When the signal is aborted, the generation will stop and throw `signal.reason` as the error.

> To stop an ongoing generation without throwing an error, also set `stopOnAbortSignal` to `true`.

***

### stopOnAbortSignal?

```ts
optional stopOnAbortSignal: boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:63](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L63)

When a completion already started being generated and then the signal is aborted,
the generation will stop and the completion will be returned as is instead of throwing an error.

Defaults to `false`.

***

### maxTokens?

```ts
optional maxTokens: number;
```

Defined in: [evaluator/LlamaCompletion.ts:66](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L66)

Maximum number of tokens to generate

***

### temperature?

```ts
optional temperature: number;
```

Defined in: [evaluator/LlamaCompletion.ts:82](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L82)

Temperature is a hyperparameter that controls the randomness of the generated text.
It affects the probability distribution of the model's output tokens.

A higher temperature (e.g., 1.5) makes the output more random and creative,
while a lower temperature (e.g., 0.5) makes the output more focused, deterministic, and conservative.

The suggested temperature is 0.8, which provides a balance between randomness and determinism.

At the extreme, a temperature of 0 will always pick the most likely next token, leading to identical outputs in each run.

Set to `0` to disable.
Disabled by default (set to `0`).

***

### minP?

```ts
optional minP: number;
```

Defined in: [evaluator/LlamaCompletion.ts:93](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L93)

From the next token candidates, discard the percentage of tokens with the lowest probability.
For example, if set to `0.05`, 5% of the lowest probability tokens will be discarded.
This is useful for generating more high-quality results when using a high temperature.
Set to a value between `0` and `1` to enable.

Only relevant when `temperature` is set to a value greater than `0`.
Disabled by default.

***

### topK?

```ts
optional topK: number;
```

Defined in: [evaluator/LlamaCompletion.ts:102](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L102)

Limits the model to consider only the K most likely next tokens for sampling at each step of sequence generation.
An integer number between `1` and the size of the vocabulary.
Set to `0` to disable (which uses the full vocabulary).

Only relevant when `temperature` is set to a value greater than 0.

***

### topP?

```ts
optional topP: number;
```

Defined in: [evaluator/LlamaCompletion.ts:112](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L112)

Dynamically selects the smallest set of tokens whose cumulative probability exceeds the threshold P,
and samples the next token only from this set.
A float number between `0` and `1`.
Set to `1` to disable.

Only relevant when `temperature` is set to a value greater than `0`.

***

### seed?

```ts
optional seed: number;
```

Defined in: [evaluator/LlamaCompletion.ts:121](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L121)

Used to control the randomness of the generated text.

Change the seed to get different results.

Only relevant when using `temperature`.

***

### xtc?

```ts
optional xtc: {
  probability: number;
  threshold: number;
};
```

Defined in: [evaluator/LlamaCompletion.ts:134](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L134)

Exclude Top Choices (XTC) removes the top tokens from consideration and avoids more obvious and repetitive generations.
Using it leads to more creative responses, but also to increased hallucinations.

The `probability` value controls the chance that the top tokens will be removed in the next token generation step.
The `threshold` value control the minimum probability of a token for it to be removed.

Start with `{probability: 0.5, threshold: 0.1}` and adjust from there.

Disabled by default.

#### probability

```ts
probability: number;
```

A number between `0` and `1` representing the probability of applying Exclude Top Choices (XTC) at each token generation step.

#### threshold

```ts
threshold: number;
```

A number between `0` and `1` representing the minimum probability
of a token for it to be removed when applying Exclude Top Choices (XTC).

***

### trimWhitespaceSuffix?

```ts
optional trimWhitespaceSuffix: boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:151](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L151)

Trim whitespace from the end of the generated text
Disabled by default.

***

### repeatPenalty?

```ts
optional repeatPenalty: 
  | false
  | LLamaContextualRepeatPenalty;
```

Defined in: [evaluator/LlamaCompletion.ts:153](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L153)

***

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LLamaContextualDryRepeatPenalty;
```

Defined in: [evaluator/LlamaCompletion.ts:165](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L165)

DRY (Don't Repeat Yourself) penalty is a technique to reduce repetitions in the generated text
by penalizing tokens based on recent token usage patterns.

With the right parameters choice, it makes it impossible for the model to
repeat itself verbatim with the same tokens in the same order (the model can still repeat itself by
using different tokens or by paraphrasing, but that is far less of an issue than a broken-record looping).

Disabled by default.

***

### tokenBias?

```ts
optional tokenBias: 
  | TokenBias
  | () => TokenBias;
```

Defined in: [evaluator/LlamaCompletion.ts:172](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L172)

Adjust the probability of tokens being generated.
Can be used to bias the model to generate tokens that you want it to lean towards,
or to avoid generating tokens that you want it to avoid.

***

### evaluationPriority?

```ts
optional evaluationPriority: EvaluationPriority;
```

Defined in: [evaluator/LlamaCompletion.ts:177](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L177)

See the parameter `evaluationPriority` on the `LlamaContextSequence.evaluate()` function for more information.

***

### grammar?

```ts
optional grammar: LlamaGrammar;
```

Defined in: [evaluator/LlamaCompletion.ts:179](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L179)

***

### customStopTriggers?

```ts
optional customStopTriggers: readonly (LlamaText | string | readonly (string | Token)[])[];
```

Defined in: [evaluator/LlamaCompletion.ts:184](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L184)

Custom stop triggers to stop the completion when any of the provided triggers are found.

***

### contextShiftSize?

```ts
optional contextShiftSize: 
  | number
  | (sequence: LlamaContextSequence) => 
  | number
  | Promise<number>;
```

Defined in: [evaluator/LlamaCompletion.ts:190](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L190)

The number of tokens to delete from the context window to make space for new ones.
Defaults to 10% of the context size.

***

### disableContextShift?

```ts
optional disableContextShift: boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:201](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L201)

Context shift reconstructs the context with partial relevant data to continue generation when the context fills up.
This flag disables this behavior.
This flag will cause the generation to stop when the context fills up
by setting an appropriate `maxTokens` value or lowering the given `maxTokens` value when needed.
This flag will cause the generation to fail if there's no space for generating new tokens at all with the given inputs.

Disabled by default. Not recommended unless you know what you're doing.
