# Source: https://node-llama-cpp.withcat.ai/api/classes/ModelDownloader.md

---
url: /api/classes/ModelDownloader.md
---
# Class: ModelDownloader

Defined in: [utils/createModelDownloader.ts:211](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L211)

## Accessors

### entrypointFilename

#### Get Signature

```ts
get entrypointFilename(): string;
```

Defined in: [utils/createModelDownloader.ts:258](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L258)

The filename of the entrypoint file that should be used to load the model.

##### Returns

`string`

***

### entrypointFilePath

#### Get Signature

```ts
get entrypointFilePath(): string;
```

Defined in: [utils/createModelDownloader.ts:265](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L265)

The full path to the entrypoint file that should be used to load the model.

##### Returns

`string`

***

### splitBinaryParts

#### Get Signature

```ts
get splitBinaryParts(): number | undefined;
```

Defined in: [utils/createModelDownloader.ts:272](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L272)

If the model is binary spliced from multiple parts, this will return the number of those binary parts.

##### Returns

`number` | `undefined`

***

### totalFiles

#### Get Signature

```ts
get totalFiles(): number;
```

Defined in: [utils/createModelDownloader.ts:281](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L281)

The total number of files that will be saved to the directory.
For split files, this will be the number of split parts, as multiple files will be saved.
For binary-split files, this will be 1, as the parts will be spliced into a single file.

##### Returns

`number`

***

### totalSize

#### Get Signature

```ts
get totalSize(): number;
```

Defined in: [utils/createModelDownloader.ts:285](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L285)

##### Returns

`number`

***

### downloadedSize

#### Get Signature

```ts
get downloadedSize(): number;
```

Defined in: [utils/createModelDownloader.ts:291](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L291)

##### Returns

`number`

## Methods

### download()

```ts
download(__namedParameters?: {
  signal?: AbortSignal;
}): Promise<string>;
```

Defined in: [utils/createModelDownloader.ts:300](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L300)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `signal?`: `AbortSignal`; } |
| `__namedParameters.signal?` | `AbortSignal` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`>

The path to the entrypoint file that should be used to load the model

***

### cancel()

```ts
cancel(__namedParameters?: {
  deleteTempFile?: boolean;
}): Promise<void>;
```

Defined in: [utils/createModelDownloader.ts:337](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L337)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `__namedParameters` | { `deleteTempFile?`: `boolean`; } | - |
| `__namedParameters.deleteTempFile?` | `boolean` | Delete the temporary file that was created during the download. Defaults to the value of `deleteTempFileOnCancel` in the constructor. |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>
