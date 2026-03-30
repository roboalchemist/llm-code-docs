# Type Alias: OnUploadCallback

```
type OnUploadCallback = (file, onProgress, context?) => Promise<AssetDefinition>;
```

Represents the upload callback function for the Creative Editor SDK. This type defines a function that handles file uploads, including progress updates and context.

## Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `file` | `File` |
| `onProgress` | (`progress`) => `void` |
| `context?` | [`UploadCallbackContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uploadcallbackcontext/) |

## Returns[#](#returns)

`Promise`<[`AssetDefinition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetdefinition/)\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/i18n)