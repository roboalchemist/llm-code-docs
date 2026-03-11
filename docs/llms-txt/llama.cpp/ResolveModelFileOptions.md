# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ResolveModelFileOptions.md

---
url: /api/type-aliases/ResolveModelFileOptions.md
---
# Type Alias: ResolveModelFileOptions

```ts
type ResolveModelFileOptions = {
  directory?: string;
  download?: "auto" | false;
  verify?: boolean;
  fileName?: string;
  headers?: Record<string, string>;
  cli?: boolean;
  onProgress?: (status: {
     totalSize: number;
     downloadedSize: number;
  }) => void;
  deleteTempFileOnCancel?: boolean;
  parallel?: number;
  tokens?: ModelFileAccessTokens;
  endpoints?: ModelDownloadEndpoints;
  signal?: AbortSignal;
};
```

Defined in: [utils/resolveModelFile.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L16)

## Properties

### directory?

```ts
optional directory: string;
```

Defined in: [utils/resolveModelFile.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L22)

The directory to resolve models from, and download models to.

Default to `node-llama-cpp`'s default global models directory (`~/.node-llama-cpp/models`).

***

### download?

```ts
optional download: "auto" | false;
```

Defined in: [utils/resolveModelFile.ts:32](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L32)

When downloading a model file, whether to download the file if it doesn't exist.

* `"auto"`: Download the file if it doesn't exist
* `false`: Don't download the file if it doesn't exist. Implies `verify: false` even if `verify` is set to `true`.

Defaults to `"auto"`.

***

### verify?

```ts
optional verify: boolean;
```

Defined in: [utils/resolveModelFile.ts:40](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L40)

When an existing model file that corresponds to the URI is found,
verify that it matches the expected size of the remote file.

Defaults to `false`.

***

### fileName?

```ts
optional fileName: string;
```

Defined in: [utils/resolveModelFile.ts:49](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L49)

The name of the file to be resolved.

If provided and existing file is found with the same name, it will be returned.

If provided and no existing file is found with the same name, the file will be downloaded with the provided name.

***

### headers?

```ts
optional headers: Record<string, string>;
```

Defined in: [utils/resolveModelFile.ts:54](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L54)

Additional headers to use when downloading a model file.

***

### cli?

```ts
optional cli: boolean;
```

Defined in: [utils/resolveModelFile.ts:61](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L61)

When downloading a model file, show the download progress.

Defaults to `true`.

***

### onProgress()?

```ts
optional onProgress: (status: {
  totalSize: number;
  downloadedSize: number;
}) => void;
```

Defined in: [utils/resolveModelFile.ts:66](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L66)

When downloading a model file, called on download progress

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `status` | { `totalSize`: `number`; `downloadedSize`: `number`; } |
| `status.totalSize` | `number` |
| `status.downloadedSize` | `number` |

#### Returns

`void`

***

### deleteTempFileOnCancel?

```ts
optional deleteTempFileOnCancel: boolean;
```

Defined in: [utils/resolveModelFile.ts:73](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L73)

If true, the temporary file will be deleted if the download is canceled.

Defaults to `true`.

***

### parallel?

```ts
optional parallel: number;
```

Defined in: [utils/resolveModelFile.ts:80](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L80)

The number of parallel downloads to use when downloading split files.

Defaults to `4`.

***

### tokens?

```ts
optional tokens: ModelFileAccessTokens;
```

Defined in: [utils/resolveModelFile.ts:85](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L85)

Tokens to use to access the remote model file when downloading.

***

### endpoints?

```ts
optional endpoints: ModelDownloadEndpoints;
```

Defined in: [utils/resolveModelFile.ts:91](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L91)

Configure the URLs used for resolving model URIs.

#### See

[Model URIs](https://node-llama-cpp.withcat.ai/guide/downloading-models#model-uris)

***

### signal?

```ts
optional signal: AbortSignal;
```

Defined in: [utils/resolveModelFile.ts:96](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/resolveModelFile.ts#L96)

The signal to use to cancel a download.
