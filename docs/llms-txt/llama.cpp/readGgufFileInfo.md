# Source: https://node-llama-cpp.withcat.ai/api/functions/readGgufFileInfo.md

---
url: /api/functions/readGgufFileInfo.md
---
# Function: readGgufFileInfo()

```ts
function readGgufFileInfo(pathOrUri: string, options?: {
  readTensorInfo?: boolean;
  sourceType?: "network" | "filesystem";
  ignoreKeys?: string[];
  logWarnings?: boolean;
  fetchRetryOptions?: Options<unknown>;
  fetchHeaders?: Record<string, string>;
  spliceSplitFiles?: boolean;
  signal?: AbortSignal;
  tokens?: ModelFileAccessTokens;
  endpoints?: ModelDownloadEndpoints;
}): Promise<GgufFileInfo>;
```

Defined in: [gguf/readGgufFileInfo.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/readGgufFileInfo.ts#L23)

Read a GGUF file and return its metadata and tensor info (unless `readTensorInfo` is set to `false`).
Only the parts of the file required for the metadata and tensor info are read.

## Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `pathOrUri` | `string` | - |
| `options` | { `readTensorInfo?`: `boolean`; `sourceType?`: `"network"` | `"filesystem"`; `ignoreKeys?`: `string`\[]; `logWarnings?`: `boolean`; `fetchRetryOptions?`: `Options`<`unknown`>; `fetchHeaders?`: [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`string`, `string`>; `spliceSplitFiles?`: `boolean`; `signal?`: `AbortSignal`; `tokens?`: [`ModelFileAccessTokens`](../type-aliases/ModelFileAccessTokens.md); `endpoints?`: `ModelDownloadEndpoints`; } | - |
| `options.readTensorInfo?` | `boolean` | Whether to read the tensor info from the file's header. Defaults to `true`. |
| `options.sourceType?` | `"network"` | `"filesystem"` | Set to a specific value to force it to only use that source type. By default, it detects whether the path is a network URL or a filesystem path and uses the appropriate reader accordingly. |
| `options.ignoreKeys?` | `string`\[] | Metadata keys to ignore when parsing the metadata. For example, `["tokenizer.ggml.tokens"]` |
| `options.logWarnings?` | `boolean` | Whether to log warnings Defaults to `true`. |
| `options.fetchRetryOptions?` | `Options`<`unknown`> | Relevant only when fetching from a network |
| `options.fetchHeaders?` | [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`string`, `string`> | Relevant only when fetching from a network |
| `options.spliceSplitFiles?` | `boolean` | When split files are detected, read the metadata of the first file and splice the tensor info from all the parts. Defaults to `true`. |
| `options.signal?` | `AbortSignal` | - |
| `options.tokens?` | [`ModelFileAccessTokens`](../type-aliases/ModelFileAccessTokens.md) | Tokens to use to access the remote model file. |
| `options.endpoints?` | `ModelDownloadEndpoints` | Configure the URLs used for resolving model URIs. **See** [Model URIs](https://node-llama-cpp.withcat.ai/guide/downloading-models#model-uris) |

## Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`GgufFileInfo`](../type-aliases/GgufFileInfo.md)>
