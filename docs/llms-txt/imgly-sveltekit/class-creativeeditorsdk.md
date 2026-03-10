# Class: CreativeEditorSDK

The main entry point for the Creative Editor SDK.

This class provides a comprehensive interface for creating, configuring, and managing creative editing experiences using our ready-made editor. The SDK can be configured to serve a multitude of use cases, offering a wide range of features such as asset management, scene creation, export operations, and plugin management.

## Categories[#](#categories)

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`CreativeEditorSDK`

## Members[#](#members)

Instance members that allow access to the underlying engine, user interface, and configuration APIs.

### version[#](#version)

  

The version of the CE.SDK package.

* * *

### engine[#](#engine)

  

Access to the CreativeEngine instance that powers the editor.

* * *

### ui[#](#ui)

  

Access to the [UserInterfaceAPI](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/userinterfaceapi/) for controlling the editor’s user interface

* * *

### i18n[#](#i18n)

  

Access to the [InternationalizationAPI](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/internationalizationapi/) to control locale and translations

* * *

### feature[#](#feature)

  

Access to the [FeatureAPI](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/featureapi/) to control feature availability

* * *

### actions[#](#actions)

  

Access to the [ActionsAPI](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/actionsapi/) to control event actions

* * *

### utils[#](#utils)

  

Access to the [UtilsAPI](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/utilsapi/) for utility functions

* * *

### version[#](#version-1)

  

The version of the Creative Editor SDK

## Lifecycle Management[#](#lifecycle-management)

Methods for SDK initialization, cleanup, and resource management.

### dispose()[#](#dispose)

  

Disposes the editor and engine if no longer needed.

#### Returns[#](#returns)

`void`

#### Signature[#](#signature)

```
dispose(): void
```

* * *

### create()[#](#create)

  

Creates an editor and renders it for the given container.

This method gives you more control over the initialization process of the editor. After the returned Promise resolves, you can execute configuration commands on the CreativeEditorSDK instance. Once that is done, you can load or create an initial scene. Until then the CreativeEditorSDK will display a loading spinner

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `container` | `string` | `HTMLDivElement` |
| `config?` | `Partial` | the initial configuration to create the editor |

#### Returns[#](#returns-1)

`Promise`<`CreativeEditorSDK`\>

a promise which resolves after the engine is ready to receive further commands on the CreativeEditorSDK instance

#### Signature[#](#signature-1)

```
create(container: string | HTMLDivElement, config?: Partial): Promise<CreativeEditorSDK>
```

## Configuration[#](#configuration)

Methods for configuring SDK behavior, translations, and runtime settings.

### onReset()[#](#onreset)

  

Registers a callback function to be executed when resetEditor is called.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`cesdk`) => `void` | Function to be called with the cesdk instance when reset occurs |

#### Returns[#](#returns-2)

Function to remove the callback from the registry

```
(): void;
```

##### Returns[#](#returns-3)

`void`

#### Example[#](#example)

```
const removeCallback = cesdk.onReset((cesdk) => {  console.log('Editor is being reset');  // Custom cleanup/reinitialization logic});
// Later, to remove the callback:removeCallback();
```

#### Signature[#](#signature-2)

```
onReset(callback: (cesdk: CreativeEditorSDK) => void): () => void
```

* * *

### disableNoSceneWarning()[#](#disablenoscenewarning)

  

Disable the warning logged when no scene is available.

If no scene is available, 2 seconds after `CreativeEditorSDK.create()`, a warning is shown on the console. This method disables this warning. That can be useful in situation where you are waiting for long running async processes to finish before creating the scene.

#### Returns[#](#returns-4)

`void`

#### Signature[#](#signature-3)

```
disableNoSceneWarning(): void
```

* * *

### resetEditor()[#](#reseteditor)

  

Resets the editor to a clean state by disabling all features, clearing UI configurations, and removing asset sources.

#### Returns[#](#returns-5)

`void`

#### Example[#](#example-1)

```
// Reset the editor to clean statecesdk.resetEditor();
// Reconfigure as neededcesdk.feature.enable('ly.img.navigation.bar');cesdk.addDefaultAssetSources();
```

#### Signature[#](#signature-4)

```
resetEditor(): void
```

* * *

### ~setTranslations()~[#](#settranslations)

  

Adds translations to be used by the editor.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `definition` | `Partial`<`Record`<`string`, `Partial`<[`Translations`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/translations/)\>>> | locale to a translation object |

#### Returns[#](#returns-6)

`void`

#### Deprecated[#](#deprecated)

Use `cesdk.i18n.setTranslations()` instead. This method will be removed in a future version.

#### Example[#](#example-2)

```
// Deprecated - do not usecesdk.setTranslations({...});
// Use this insteadcesdk.i18n.setTranslations({ en: {   presets: {     scene: ...   } }})
```

## Plugin Management[#](#plugin-management)

Methods for extending SDK functionality through plugins and custom integrations.

### addPlugin()[#](#addplugin)

  

Adds and initializes a plugin to the editor.

#### Parameters[#](#parameters-3)

| Parameter | Type |
| --- | --- |
| `plugin` | [`EditorPlugin`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/editorplugin/) |

#### Returns[#](#returns-7)

`Promise`<`void`\>

#### Signature[#](#signature-5)

```
addPlugin(plugin: EditorPlugin): Promise<void>
```

## Asset Management[#](#asset-management)

Methods for registering, managing, and refreshing asset sources including default assets, demo assets, and custom asset libraries.

### addDefaultAssetSources()[#](#adddefaultassetsources)

  

Convenience function to register a set of our default asset sources.

The sources contain our example assets. These are:

*   `'ly.img.sticker'` - Various stickers
*   `'ly.img.vectorpath'` - Shapes and arrows
*   `'ly.img.filter.lut'` - LUT effects of various kinds
*   `'ly.img.filter.duotone'` - Color effects of various kinds

These assets are parsed at `\{\{base_url\}\}/<id>/content.json`, where `baseURL` defaults to the IMG.LY CDN. Each source is created via `addLocalSource` and populated with the parsed assets. To modify the available assets, you may either exclude certain IDs via `excludeAssetSourceIds` or alter the sources after creation.

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `baseURL?`: `string`; `excludeAssetSourceIds?`: [`DefaultAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/defaultassetsourceid/)\[\]; } | Configuration options for asset sources. Contains `baseURL` (defaults to IMG.LY CDN) and `excludeAssetSourceIds` (IDs to ignore during load). |
| `options.baseURL?` | `string` | \- |
| `options.excludeAssetSourceIds?` | [`DefaultAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/defaultassetsourceid/)\[\] | \- |

#### Returns[#](#returns-8)

`Promise`<`void`\>

#### Signature[#](#signature-6)

```
addDefaultAssetSources(options?: object): Promise<void>
```

* * *

### addDemoAssetSources()[#](#adddemoassetsources)

  

Convenience function that registers a set of demo asset sources

These contain our example assets. These are not to meant to be used in your production code.

These are

*   `'ly.img.image'` - Sample images
*   `'ly.img.image.upload'` - Demo source to upload image assets
*   `'ly.img.audio'` - Sample audios
*   `'ly.img.audio.upload'` - Demo source to upload audio assets
*   `'ly.img.video'` - Sample videos
*   `'ly.img.video.upload'` - Demo source to upload video assets

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `baseURL?`: `string`; `excludeAssetSourceIds?`: [`DemoAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/demoassetsourceid/)\[\]; `sceneMode?`: `"Design"` | `"Video"`; `withUploadAssetSources?`: `boolean`; } |
| `options.baseURL?` | `string` | \- |
| `options.excludeAssetSourceIds?` | [`DemoAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/demoassetsourceid/)\[\] | \- |
| `options.sceneMode?` | `"Design"` | `"Video"` |
| `options.withUploadAssetSources?` | `boolean` | \- |

#### Returns[#](#returns-9)

`Promise`<`void`\>

#### Signature[#](#signature-7)

```
addDemoAssetSources(options?: object): Promise<void>
```

* * *

### ~refetchAssetSources()~[#](#refetchassetsources)

  

Trigger a refetch of the asset source and update the asset library panel with the new items accordingly.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId?` | `string` | `string`\[\] |

#### Returns[#](#returns-10)

`void`

#### Deprecated[#](#deprecated-1)

Please use `cesdk.engine.asset.assetSourceContentsChanged` instead.

## Scene Creation[#](#scene-creation)

Methods for creating new scenes from scratch, including design scenes, video scenes, and scenes from existing images.

### createDesignScene()[#](#createdesignscene)

  

Create a scene with a single empty page with the given format.

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `format?` | [`PageFormatDefinition`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/pageformatdefinition/) | A `PageFormatDefinition` object specifying the page format to use. |

#### Returns[#](#returns-11)

`Promise`<`number`\>

#### Signature[#](#signature-8)

```
createDesignScene(format?: PageFormatDefinition): Promise<number>
```

* * *

### createVideoScene()[#](#createvideoscene)

  

Create a scene with a single empty page with the given format.

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `format?` | [`PageFormatDefinition`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/pageformatdefinition/) | The page format to use. Can be either a string, identifying a page format that has been configured or a `PageFormatDefinition` object. |

#### Returns[#](#returns-12)

`Promise`<`number`\>

#### Signature[#](#signature-9)

```
createVideoScene(format?: PageFormatDefinition): Promise<number>
```

* * *

### createFromImage()[#](#createfromimage)

  

Loads the given image and creates a scene with a single page showing the image.

Fetching the image may take an arbitrary amount of time, so the scene isn’t immediately available.

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The image URL. |
| `dpi?` | `number` | The scene’s DPI. Defaults to 300. |
| `pixelScaleFactor?` | `number` | The display’s pixel scale factor. Defaults to 1. |
| `sceneLayout?` | `"Free"` | `"VerticalStack"` |
| `spacing?` | `number` | Spacing between pages. Defaults to 0. |
| `spacingInScreenSpace?` | `boolean` | Whether spacing is in screen space. Defaults to false. |

#### Returns[#](#returns-13)

`Promise`<`number`\>

a promise which resolves if the scene was successfully created.

#### Signature[#](#signature-10)

```
createFromImage(url: string, dpi?: number, pixelScaleFactor?: number, sceneLayout?: "Free" | "VerticalStack" | "HorizontalStack" | "DepthStack", spacing?: number, spacingInScreenSpace?: boolean): Promise<number>
```

* * *

### createFromVideo()[#](#createfromvideo)

  

Create a scene from the provided video.

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The url of the video |

#### Returns[#](#returns-14)

`Promise`<`number`\>

a promise which resolves if the scene was successfully created.

#### Signature[#](#signature-11)

```
createFromVideo(url: string): Promise<number>
```

## Scene Loading[#](#scene-loading)

Methods for loading existing scenes from various sources including strings, URLs, and encoded scene data.

### ~load()~[#](#load)

  

Load an encoded scene from the provided string.

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `scene` | `string` | A string starting with UBQ1 and containing the encoded scene. |

#### Returns[#](#returns-15)

`Promise`<`number`\>

#### Deprecated[#](#deprecated-2)

Use `loadFromString` instead.

* * *

### loadFromString()[#](#loadfromstring)

  

Load an encoded scene from the provided string.

#### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `scene` | `string` | A string starting with UBQ1 and containing the encoded scene. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |

#### Returns[#](#returns-16)

`Promise`<`number`\>

a promise which resolves if the scene was successfully loaded.

#### Signature[#](#signature-12)

```
loadFromString(scene: string, overrideEditorConfig?: boolean): Promise<number>
```

* * *

### loadFromURL()[#](#loadfromurl)

  

Load the scene stored in the file at the given URL.

#### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The url to fetch to acquire the scene string. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |

#### Returns[#](#returns-17)

`Promise`<`number`\>

a promise which resolves if the scene was successfully loaded.

#### Signature[#](#signature-13)

```
loadFromURL(url: string, overrideEditorConfig?: boolean): Promise<number>
```

* * *

### loadFromArchiveURL()[#](#loadfromarchiveurl)

  

Load a previously archived scene from the URL to the scene file.

#### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the scene archive file. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |

#### Returns[#](#returns-18)

`Promise`<`number`\>

a promise which resolves if the scene was successfully loaded.

#### Signature[#](#signature-14)

```
loadFromArchiveURL(url: string, overrideEditorConfig?: boolean): Promise<number>
```

## Scene Saving[#](#scene-saving)

Methods for persisting and exporting scene data as strings or files.

### save()[#](#save)

  

Save and return a scene as a base64 encoded string.

#### Returns[#](#returns-19)

`Promise`<`string`\>

a promise with the scene as a string

#### Signature[#](#signature-15)

```
save(): Promise<string>
```

## Export Operations[#](#export-operations)

Methods for exporting scenes and pages as files in various formats and mimeTypes.

### export()[#](#export)

  

Exports one or multiple page(s) as an file in the given mimeType

Please note: the `onExport` callback provided in the configuration will be not called. This callback is for exports triggered by an user interaction.

#### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | [`ExportOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/exportoptions/) | options for the export |

#### Returns[#](#returns-20)

`Promise`<{ `blobs`: `Blob`\[\]; `options`: [`ExportOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/exportoptions/); }>

a promise with an object holding `blobs` of the export pages and the provided `options`.

#### Signature[#](#signature-16)

```
export(options: ExportOptions): Promise<object>
```

## Upload Operations[#](#upload-operations)

Methods for handling file uploads and asset creation from user-provided files.

### ~unstable\_upload()~[#](#unstable_upload)

Uses the configured upload handler to upload the given file.

#### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `File` | The file to upload |
| `onProgress` | (`progress`) => `void` | A callback to track the progress of the upload This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-21)

`Promise`<[`AssetDefinition`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/assetdefinition/)\>

#### Deprecated[#](#deprecated-3)

This API will be removed in future versions. Please use the `uploadFile` action instead.

## Other[#](#other)

### getBaseURL()[#](#getbaseurl)

  

Returns the baseURL that was provided in the configuration during editor initialization.

#### Returns[#](#returns-22)

`string`

The original baseURL from the top-level configuration

#### Example[#](#example-3)

```
const cesdk = await CreativeEditorSDK.create('#editor', {  baseURL: 'https://my-cdn.example.com/assets/'});
console.log(cesdk.getBaseURL()); // 'https://my-cdn.example.com/assets/'
```

#### Signature[#](#signature-17)

```
getBaseURL(): string
```

## Page Management[#](#page-management)

This API is experimental and may change or be removed in future versions.

### unstable\_switchPage()[#](#unstable_switchpage)

#### Parameters[#](#parameters-17)

| Parameter | Type |
| --- | --- |
| `pageId` | `number` |

#### Returns[#](#returns-23)

`Promise`<`void`\>

* * *

### unstable\_getPages()[#](#unstable_getpages)

#### Returns[#](#returns-24)

`Promise`<`number`\[\]>

* * *

### unstable\_onActivePageChanged()[#](#unstable_onactivepagechanged)

#### Parameters[#](#parameters-18)

| Parameter | Type |
| --- | --- |
| `callback` | (`id`) => `void` |

#### Returns[#](#returns-25)

```
(): void;
```

##### Returns[#](#returns-26)

`void`

* * *

### unstable\_focusPage()[#](#unstable_focuspage)

Focus on a specific page and zoom to fit it in the viewport.

#### Parameters[#](#parameters-19)

| Parameter | Type | Description |
| --- | --- | --- |
| `pageId` | `number` | The ID of the page to focus on |

#### Returns[#](#returns-27)

`Promise`<`void`\>

A promise that resolves when the focus operation is complete

## Upload Operations[#](#upload-operations-1)

This API is experimental and may change or be removed in future versions.

### ~unstable\_supportsUpload()~[#](#unstable_supportsupload)

Returns true if a upload handler was configured. If mime types are given as an argument, it will return true if the upload handler supports all of the given mime types.

#### Parameters[#](#parameters-20)

| Parameter | Type |
| --- | --- |
| `mimeTypes?` | `string` |

#### Returns[#](#returns-28)

`boolean`

#### Deprecated[#](#deprecated-4)

This API will be removed in future versions. Please use the `engine.editor.getSetting('upload/supportedMimeTypes')` to check for supported mime types instead.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/blockapi)