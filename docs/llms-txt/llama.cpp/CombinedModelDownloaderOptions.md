# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/CombinedModelDownloaderOptions.md

---
url: /api/type-aliases/CombinedModelDownloaderOptions.md
---
# Type Alias: CombinedModelDownloaderOptions

```ts
type CombinedModelDownloaderOptions = {
  showCliProgress?: boolean;
  onProgress?: (status: {
     totalSize: number;
     downloadedSize: number;
  }) => void;
  parallelDownloads?: number;
};
```

Defined in: [utils/createModelDownloader.ts:522](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L522)

## Properties

### showCliProgress?

```ts
optional showCliProgress: boolean;
```

Defined in: [utils/createModelDownloader.ts:526](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L526)

Defaults to `false`.

***

### onProgress()?

```ts
optional onProgress: (status: {
  totalSize: number;
  downloadedSize: number;
}) => void;
```

Defined in: [utils/createModelDownloader.ts:528](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L528)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `status` | { `totalSize`: `number`; `downloadedSize`: `number`; } |
| `status.totalSize` | `number` |
| `status.downloadedSize` | `number` |

#### Returns

`void`

***

### parallelDownloads?

```ts
optional parallelDownloads: number;
```

Defined in: [utils/createModelDownloader.ts:535](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L535)

The number of parallel downloads to use fo files.

Defaults to `4`.
