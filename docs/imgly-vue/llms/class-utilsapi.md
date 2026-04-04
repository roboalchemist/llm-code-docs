# Class: UtilsAPI

UtilsAPI provides utility functions for common operations in the Creative Engine SDK.

This API includes utilities for:

*   Creating and managing loading dialogs
*   Exporting content (images, PDFs, videos)
*   Loading and downloading files
*   Local file uploads

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`UtilsAPI`

## Methods[#](#methods)

### generateBlockName()[#](#generateblockname)

  

Generates the automatic, localized fallback name for a design block. When the block does not have an explicit name set, this mirrors the naming shown in the UI panels.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockId` | `number` | The block ID to generate a fallback name for |

#### Returns[#](#returns)

`string`

The localized fallback name for the block

#### Signature[#](#signature)

```
generateBlockName(blockId: number): string
```

* * *

### showLoadingDialog()[#](#showloadingdialog)

  

Shows and manages a loading dialog with progress tracking

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `title?`: `string`; `message?`: `string` | `string`\[\]; `cancelLabel?`: `string`; `abortLabel?`: `string`; `abortTitle?`: `string`; `abortMessage?`: `string` |
| `options.title?` | `string` | \- |
| `options.message?` | `string` | `string`\[\] |
| `options.cancelLabel?` | `string` | \- |
| `options.abortLabel?` | `string` | \- |
| `options.abortTitle?` | `string` | \- |
| `options.abortMessage?` | `string` | `string`\[\] |
| `options.size?` | `"large"` | `"regular"` |
| `options.clickOutsideToClose?` | `boolean` | \- |
| `options.progress?` | [`DialogProgress`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogprogress/) | \- |
| `options.onDone?` | () => `void` | \- |
| `options.onAbort?` | () => `void` | \- |

#### Returns[#](#returns-1)

`object`

A controller object for managing the dialog

| Name | Type |
| --- | --- |
| `dialogId` | `string` |
| `updateProgress()` | (`progress`) => `void` |
| `showSuccess()` | (`options`) => `void` |
| `showError()` | (`options`) => `void` |
| `close()` | () => `void` |

#### Example[#](#example)

```
const controller = cesdk.utils.showLoadingDialog({  title: 'Exporting',  message: 'Please wait...',  onAbort: () => console.log('Aborted')});
// Update progresscontroller.updateProgress({ value: 50, max: 100 });
// Show successcontroller.showSuccess({  title: 'Success',  message: 'Export completed!'});
```

#### Signature[#](#signature-1)

```
showLoadingDialog(options?: object): object
```

* * *

### export()[#](#export)

  

Exports content with a loading dialog and progress tracking. Automatically handles both static exports (images, PDFs) and video exports based on MIME type.

#### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` _extends_ |

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | `T` | Export options. Type inference based on mimeType. |

#### Returns[#](#returns-2)

`Promise`<{ `blobs`: `Blob`\[\]; `options`: `T` _extends_ [`VideoExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videoexportoptions/) ? [`OnExportVideoOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onexportvideooptions/) : [`OnExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onexportoptions/); }>

Export result - either blobs array for static or single blob for video

#### Example[#](#example-1)

```
// Image exportconst imageResult = await cesdk.utils.export({  mimeType: 'image/png',  pngCompressionLevel: 7});
// Video exportconst videoResult = await cesdk.utils.export({  mimeType: 'video/mp4',  onProgress: (rendered, encoded, total) => console.log(`${rendered}/${total}`)});
```

#### Signature[#](#signature-2)

```
export(options?: T): Promise<object>
```

* * *

### loadFile()[#](#loadfile)

  

Opens a file picker dialog for the user to select a file

#### Type Parameters[#](#type-parameters-1)

| Type Parameter |
| --- |
| `T` _extends_ `"text"` |

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | { `accept`: `string`; `returnType?`: `T`; } | Options for the file load operation |
| `options.accept` | `string` | \- |
| `options.returnType?` | `T` | \- |

#### Returns[#](#returns-3)

`Promise`<`T` _extends_ `"dataURL"` ? `string` : `T` _extends_ `"text"` ? `string` : `T` _extends_ `"blob"` ? `Blob` : `T` _extends_ `"arrayBuffer"` ? `ArrayBuffer` : `T` _extends_ `"objectURL"` ? `string` : `File`\>

The loaded file content in the requested format. For dataURL return type, if the file is eligible for OPFS storage and the feature is enabled, returns the OPFS URL (opfs://…) instead of a data URL.

#### Example[#](#example-2)

```
// Load a text fileconst text = await cesdk.utils.loadFile({  accept: '.txt',  returnType: 'text'});
// Load an image as blobconst blob = await cesdk.utils.loadFile({  accept: 'image/*',  returnType: 'blob'});
// Load a file with OPFS support (returns opfs:// URL for eligible files)const url = await cesdk.utils.loadFile({  accept: 'video/*',  returnType: 'dataURL'});// For eligible files: "opfs://cesdk-1234567890-video.mp4"// For non-eligible files: "data:video/mp4;base64,..."// Load a file as object URL (blob URL)const objectURL = await cesdk.utils.loadFile({  accept: '.zip',  returnType: 'objectURL'});// Remember to revoke the object URL when doneURL.revokeObjectURL(objectURL);
```

#### Signature[#](#signature-3)

```
loadFile(options: object): Promise<T extends "dataURL" ? string : T extends "text" ? string : T extends "blob" ? Blob : T extends "arrayBuffer" ? ArrayBuffer : T extends "objectURL" ? string : File>
```

* * *

### downloadFile()[#](#downloadfile)

  

Downloads a blob, string, or OPFS path as a file to the user’s device

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `string` | `Blob` |
| `mimeType?` | [`FileMimeType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filemimetype/) | The MIME type of the content |

#### Returns[#](#returns-4)

`Promise`<`void`\>

#### Example[#](#example-3)

```
// Download a text fileawait cesdk.utils.downloadFile('Hello World', 'text/plain');
// Download a blobconst blob = new Blob(['content'], { type: 'text/plain' });await cesdk.utils.downloadFile(blob, 'text/plain');
// Download from OPFS pathawait cesdk.utils.downloadFile('opfs://cesdk/buffer/file.mp4', 'video/mp4');
```

#### Signature[#](#signature-4)

```
downloadFile(file: string | Blob, mimeType?: FileMimeType): Promise<void>
```

* * *

### localUpload()[#](#localupload)

  

Performs a local upload of a file (development only)

Note: This is meant for development testing only. In production, you should implement a proper upload handler using the callbacks API.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `File` | The file to upload |
| `context?` | [`UploadCallbackContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/interfaces/uploadcallbackcontext/) | Optional context information for the upload operation |

#### Returns[#](#returns-5)

`Promise`<[`AssetDefinition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetdefinition/)\>

The asset definition for the uploaded file

#### Example[#](#example-4)

```
const file = new File(['content'], 'test.txt');const asset = await cesdk.utils.localUpload(file, {  context: { source: 'user-upload' }});
```

#### Signature[#](#signature-5)

```
localUpload(file: File, context?: UploadCallbackContext): Promise<AssetDefinition>
```

* * *

### calculateViewportPadding()[#](#calculateviewportpadding)

  

Calculates the recommended viewport padding based on current viewport size and settings. This utility matches the internal padding used by the SDK for zoom operations. The calculation accounts for safe area insets to ensure content remains visible in UI-safe regions (avoiding notches, rounded corners, system overlays, etc.).

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `width?` | `number` | Optional viewport width to use instead of current camera width |
| `height?` | `number` | Optional viewport height to use instead of current camera height |

#### Returns[#](#returns-6)

`object`

An object containing paddingX and paddingY values

| Name | Type |
| --- | --- |
| `paddingX` | `number` |
| `paddingY` | `number` |

#### Example[#](#example-5)

```
const padding = cesdk.utils.calculateViewportPadding();console.log(`Padding: ${padding.paddingX}x${padding.paddingY}`);
// Use with custom zoomawait cesdk.engine.scene.zoomToBlock(  pageId,  padding.paddingX,  padding.paddingY,  padding.paddingX,  padding.paddingY);
```

#### Signature[#](#signature-6)

```
calculateViewportPadding(width?: number, height?: number): object
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/classes/userinterfaceapi)