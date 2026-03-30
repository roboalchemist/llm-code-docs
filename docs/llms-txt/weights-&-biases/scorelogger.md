# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/classes/scorelogger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Class: ScoreLogger

> TypeScript SDK reference

[weave](../) / ScoreLogger

ScoreLogger manages scoring for a single prediction.
Returned from EvaluationLogger.logPrediction().

`Example`

```ts  theme={null}
const pred = await ev.logPrediction(example, output);
await pred.logScore("accuracy", 0.95);
await pred.logScore("relevance", 0.8);
await pred.finish(); // Finalizes the prediction
```

## Table of contents

### Constructors

* [constructor](./scorelogger#constructor)

### Accessors

* [isFinishCalled](./scorelogger#isfinishcalled)

### Methods

* [finish](./scorelogger#finish)
* [logScore](./scorelogger#logscore)

## Constructors

### constructor

• **new ScoreLogger**(`evalLogger`): [`ScoreLogger`](./scorelogger)

#### Parameters

| Name         | Type                                     |
| :----------- | :--------------------------------------- |
| `evalLogger` | [`EvaluationLogger`](./evaluationlogger) |

#### Returns

[`ScoreLogger`](./scorelogger)

#### Defined in

[evaluationLogger.ts:319](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/evaluationLogger.ts#L319)

## Accessors

### isFinishCalled

• `get` **isFinishCalled**(): `boolean`

Check if finish() has been called.
Used by EvaluationLogger to detect unfinished predictions.

#### Returns

`boolean`

#### Defined in

[evaluationLogger.ts:349](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/evaluationLogger.ts#L349)

## Methods

### finish

▸ **finish**(): `Promise`\<`void`>

Finish the scoring process for the prediction.
Finalizes the predict\_and\_score call with accumulated scores.
Updates incremental aggregates and frees memory.

#### Returns

`Promise`\<`void`>

#### Defined in

[evaluationLogger.ts:451](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/evaluationLogger.ts#L451)

***

### logScore

▸ **logScore**(`scorerName`, `score`): `Promise`\<`void`>

Log a score for this prediction.
Creates a scorer call as a child of predict\_and\_score.

#### Parameters

| Name         | Type     | Description                                        |
| :----------- | :------- | :------------------------------------------------- |
| `scorerName` | `string` | Name of the scorer (e.g., "accuracy", "f1\_score") |
| `score`      | `any`    | The score value                                    |

#### Returns

`Promise`\<`void`>

#### Defined in

[evaluationLogger.ts:360](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/evaluationLogger.ts#L360)
