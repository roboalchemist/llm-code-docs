# Type Alias: Callbacks

```
type Callbacks = object;
```

Represents the callback functions for various events in the Creative Editor SDK. This interface defines functions for handling back, close, share, save, load, load archive, download, export, upload, and unsupported browser events.

## Deprecated[#](#deprecated)

Use the `cesdk.actions` API and the Order API instead.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`onBack?`~ | () => `void` | `Promise`<`void`\> |
| ~`onClose?`~ | () => `void` | `Promise`<`void`\> |
| ~`onShare?`~ | (`s`) => `void` | `Promise`<`void`\> |
| ~`onSave?`~ | (`s`) => `void` | `Promise`<`void`\> |
| ~`onLoad?`~ | () => `Promise`<`string`\> | `"upload"` |
| ~`onLoadArchive?`~ | () => `Promise`<`string`\> | `"uploadArchive"` |
| ~`onDownload?`~ | (`s`) => `void` | `Promise`<`void`\> |
| ~`onExport?`~ | (`blobs`, `options`) => `void` | `Promise`<`void`\> |
| ~`onUpload?`~ |  | [`OnUploadCallback`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/onuploadcallback/) |
| ~`onUnsupportedBrowser?`~ | () => `void` | **Deprecated** Use the `cesdk.actions.register('onUnsupportedBrowser', action)` instead. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/a11y)