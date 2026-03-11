# Source: https://node-llama-cpp.withcat.ai/api/functions/combineModelDownloaders.md

---
url: /api/functions/combineModelDownloaders.md
---
# Function: combineModelDownloaders()

```ts
function combineModelDownloaders(downloaders: (
  | ModelDownloader
  | Promise<ModelDownloader>)[], options?: CombinedModelDownloaderOptions): Promise<CombinedModelDownloader>;
```

Defined in: [utils/createModelDownloader.ts:202](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/createModelDownloader.ts#L202)

Combine multiple models downloaders to a single downloader to download everything using as much parallelism as possible.

You can check each individual model downloader for its download progress,
but only the `onProgress` passed to the combined downloader will be called during the download.

When combining `ModelDownloader` instances, the following options on each individual `ModelDownloader` are ignored:

* `showCliProgress`
* `onProgress`
* `parallelDownloads`

To set any of those options for the combined downloader, you have to pass them to the combined downloader instance.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `downloaders` | ( | [`ModelDownloader`](../classes/ModelDownloader.md) | [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`ModelDownloader`](../classes/ModelDownloader.md)>)\[] |
| `options?` | [`CombinedModelDownloaderOptions`](../type-aliases/CombinedModelDownloaderOptions.md) |

## Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`CombinedModelDownloader`](../classes/CombinedModelDownloader.md)>

## Example

```typescript
import {fileURLToPath} from "url";
import path from "path";
import {createModelDownloader, combineModelDownloaders, getLlama} from "node-llama-cpp";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const downloaders = [
    createModelDownloader({
        modelUri: "https://example.com/model1.gguf",
        dirPath: path.join(__dirname, "models")
    }),
    createModelDownloader({
        modelUri: "hf:user/model2:quant",
        dirPath: path.join(__dirname, "models")
    }),
    createModelDownloader({
        modelUri: "hf:user/model/model3.gguf",
        dirPath: path.join(__dirname, "models")
    })
];
const combinedDownloader = await combineModelDownloaders(downloaders, {
    showCliProgress: true // show download progress in the CLI
});
const [
    model1Path,
    model2Path,
    model3Path
] = await combinedDownloader.download();

const llama = await getLlama();
const model1 = await llama.loadModel({
    modelPath: model1Path!
});
const model2 = await llama.loadModel({
    modelPath: model2Path!
});
const model3 = await llama.loadModel({
    modelPath: model3Path!
});
```
