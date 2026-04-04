# Type Alias: UploadAction

```
type UploadAction = (file, onProgress, context?) => Promise<AssetDefinition>;
```

Action function for uploading files to asset sources.

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `File` | The file to upload |
| `onProgress` | (`progress`) => `void` | Progress action that receives upload progress (0-100) |
| `context?` | [`UploadCallbackContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uploadcallbackcontext/) | Optional context information for the upload operation |

## Returns[#](#returns)

`Promise`<[`AssetDefinition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetdefinition/)\>

A promise that resolves with the uploaded asset definition

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/unknowntranslations)