# Source: https://node-llama-cpp.withcat.ai/api/classes/CombinedModelDownloader.md

---
url: /api/classes/CombinedModelDownloader.md
---
# Class: CombinedModelDownloader

Defined in: [utils/createModelDownloader.ts:538](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L538)

## Accessors

### modelDownloaders

#### Get Signature

```ts
get modelDownloaders(): readonly ModelDownloader[];
```

Defined in: [utils/createModelDownloader.ts:623](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L623)

##### Returns

readonly [`ModelDownloader`](ModelDownloader.md)\[]

***

### entrypointFilenames

#### Get Signature

```ts
get entrypointFilenames(): string[];
```

Defined in: [utils/createModelDownloader.ts:630](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L630)

The filename of the entrypoint files that should be used to load the models.

##### Returns

`string`\[]

***

### entrypointFilePaths

#### Get Signature

```ts
get entrypointFilePaths(): string[];
```

Defined in: [utils/createModelDownloader.ts:637](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L637)

The full paths to the entrypoint files that should be used to load the models.

##### Returns

`string`\[]

***

### totalFiles

#### Get Signature

```ts
get totalFiles(): number;
```

Defined in: [utils/createModelDownloader.ts:644](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L644)

The accumulation of `totalFiles` of all the model downloaders

##### Returns

`number`

***

### totalSize

#### Get Signature

```ts
get totalSize(): number;
```

Defined in: [utils/createModelDownloader.ts:650](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L650)

##### Returns

`number`

***

### downloadedSize

#### Get Signature

```ts
get downloadedSize(): number;
```

Defined in: [utils/createModelDownloader.ts:656](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L656)

##### Returns

`number`

## Methods

### cancel()

```ts
cancel(): Promise<void>;
```

Defined in: [utils/createModelDownloader.ts:569](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L569)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### download()

```ts
download(__namedParameters?: {
  signal?: AbortSignal;
}): Promise<string[]>;
```

Defined in: [utils/createModelDownloader.ts:586](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L586)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `signal?`: `AbortSignal`; } |
| `__namedParameters.signal?` | `AbortSignal` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`\[]>

The paths to the entrypoint files that should be used to load the models
