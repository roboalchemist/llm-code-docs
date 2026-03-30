# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/SequenceEvaluateOptions.md

---
url: /api/type-aliases/SequenceEvaluateOptions.md
---
# Type Alias: SequenceEvaluateOptions

```ts
type SequenceEvaluateOptions = {
  temperature?: number;
  minP?: number;
  topK?: number;
  topP?: number;
  seed?: number;
  xtc?: {
     probability: number;
     threshold: number;
  };
  grammarEvaluationState?:   | LlamaGrammarEvaluationState
     | () => 
     | LlamaGrammarEvaluationState
     | undefined;
  repeatPenalty?: LlamaContextSequenceRepeatPenalty;
  dryRepeatPenalty?: LlamaContextSequenceDryRepeatPenalty;
  tokenBias?:   | TokenBias
     | () => TokenBias;
  evaluationPriority?: EvaluationPriority;
  contextShift?: ContextShiftOptions;
  yieldEogToken?: boolean;
};
```

Defined in: [evaluator/LlamaContext/types.ts:349](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L349)

## Properties

### temperature?

```ts
optional temperature: number;
```

Defined in: [evaluator/LlamaContext/types.ts:350](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L350)

***

### minP?

```ts
optional minP: number;
```

Defined in: [evaluator/LlamaContext/types.ts:350](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L350)

***

### topK?

```ts
optional topK: number;
```

Defined in: [evaluator/LlamaContext/types.ts:350](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L350)

***

### topP?

```ts
optional topP: number;
```

Defined in: [evaluator/LlamaContext/types.ts:350](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L350)

***

### seed?

```ts
optional seed: number;
```

Defined in: [evaluator/LlamaContext/types.ts:361](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L361)

Used to control the randomness of the generated text.

Change the seed to get different results.

Defaults to the current epoch time.

Only relevant when using `temperature`.

***

### xtc?

```ts
optional xtc: {
  probability: number;
  threshold: number;
};
```

Defined in: [evaluator/LlamaContext/types.ts:374](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L374)

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

### grammarEvaluationState?

```ts
optional grammarEvaluationState: 
  | LlamaGrammarEvaluationState
  | () => 
  | LlamaGrammarEvaluationState
  | undefined;
```

Defined in: [evaluator/LlamaContext/types.ts:387](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L387)

***

### repeatPenalty?

```ts
optional repeatPenalty: LlamaContextSequenceRepeatPenalty;
```

Defined in: [evaluator/LlamaContext/types.ts:388](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L388)

***

### dryRepeatPenalty?

```ts
optional dryRepeatPenalty: LlamaContextSequenceDryRepeatPenalty;
```

Defined in: [evaluator/LlamaContext/types.ts:400](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L400)

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

Defined in: [evaluator/LlamaContext/types.ts:407](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L407)

Adjust the probability of tokens being generated.
Can be used to bias the model to generate tokens that you want it to lean towards,
or to avoid generating tokens that you want it to avoid.

***

### evaluationPriority?

```ts
optional evaluationPriority: EvaluationPriority;
```

Defined in: [evaluator/LlamaContext/types.ts:418](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L418)

When a lot of tokens are queued for the next batch, more than the configured `batchSize`, the tokens for each sequence will be
evaluated based on the strategy chosen for the context.
By default, the `"maximumParallelism"` strategy is used, which will try to evaluate as many sequences in parallel as possible,
but at some point, it'll have to choose which sequences to evaluate more tokens of, so it'll prioritize the sequences with the
highest evaluation priority.
Also, a custom strategy can be used to prioritize the sequences differently, but generally, the higher the evaluation priority
is, the more likely and more tokens will be evaluated for that sequence in the next queued batch.

***

### contextShift?

```ts
optional contextShift: ContextShiftOptions;
```

Defined in: [evaluator/LlamaContext/types.ts:425](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L425)

Override the sequence context shift options for this evaluation

See [ContextShiftOptions](ContextShiftOptions.md) for more information.

***

### yieldEogToken?

```ts
optional yieldEogToken: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:432](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L432)

Yield an EOG (End Of Generation) token (like EOS and EOT) when it's generated.
When `false` the generation will stop when an EOG token is generated and the token won't be yielded.
Defaults to `false`.
