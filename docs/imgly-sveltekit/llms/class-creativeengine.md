# Class: CreativeEngine

The CreativeEngine is the core processing unit of CE.SDK and handles state management, rendering, input handling, and much more. It provides APIs to directly interact with assets, blocks, scenes, and variables. These APIs can be used in a headless environment to build and manipulate designs programmatically, or in a browser to create interactive applications.

## Engine Management[#](#engine-management)

Methods for initializing, configuring, and managing the engine lifecycle.

### version[#](#version)

  

The version of the CE.SDK package.

* * *

### version[#](#version-1)

  

The SDK version

* * *

### addPlugin()[#](#addplugin)

  

Add and initialize a plugin to the engine.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `plugin` | [`EnginePlugin`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/engineplugin/) | The plugin to add and initialize. |

#### Returns[#](#returns)

`Promise`<`void`\>

#### Signature[#](#signature)

```
addPlugin(plugin: EnginePlugin): Promise<void>
```

* * *

### setWheelEventTarget()[#](#setwheeleventtarget)

  

Install the mousewheel event handler for the CreativeEngine on a different element than the canvas.

This can be useful if you are rendering HTML elements on top of the canvas and want to scroll the canvas when the mouse is over those elements.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `target` | `HTMLElement` | The HTML element to attach the wheel event handler to. |

#### Returns[#](#returns-1)

A function that removes the event handler from the target and adds it back to the canvas.

```
(): void;
```

##### Returns[#](#returns-2)

`void`

#### Signature[#](#signature-1)

```
setWheelEventTarget(target: HTMLElement): () => void
```

* * *

### element[#](#element)

  

Access the canvas element used by the CreativeEngine.

##### Returns[#](#returns-3)

[`HTMLCreativeEngineCanvasElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/htmlcreativeenginecanvaselement/)

* * *

### dispose()[#](#dispose)

  

Dispose the engine and clean up all resources.

#### Returns[#](#returns-4)

`void`

#### Signature[#](#signature-2)

```
dispose(): void
```

* * *

### init()[#](#init)

  

Initialize a CreativeEngine with an optional configuration.

#### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `C` _extends_ `Partial`<[`_EngineConfiguration`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/engineconfiguration/)\> |

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `config?` | `C` | Optional configuration object for engine initialization. |

#### Returns[#](#returns-5)

`Promise`<`CreativeEngine` & `C` _extends_ `object` ? `object` : `object`\>

A promise that resolves to an engine instance.

#### Signature[#](#signature-3)

```
init(config?: C): Promise<CreativeEngine & C extends { canvas: any } ? { element: undefined } : { element: HTMLCreativeEngineCanvasElement }>
```

* * *

### getBaseURL()[#](#getbaseurl)

  

Returns the configured base URL for the engine’s assets.

#### Returns[#](#returns-6)

`string`

The absolute base URL configured for this engine instance.

#### Example[#](#example)

```
const engine = await CreativeEngine.init({  baseURL: 'https://my-cdn.example.com/assets/'});
console.log(engine.getBaseURL()); // 'https://my-cdn.example.com/assets/'
```

#### Signature[#](#signature-4)

```
getBaseURL(): string
```

## Core APIs[#](#core-apis)

### asset[#](#asset)

  

Manage and interact with assets in the engine.

* * *

### block[#](#block)

  

Create, find, delete and modify with blocks in the engine.

* * *

### editor[#](#editor)

  

Manage the editor state, including edit modes and undo/redo operations.

* * *

### event[#](#event)

  

Subscribe to events in the engine.

* * *

### scene[#](#scene)

  

Manage scenes, including creating, modifying, and deleting scenes.

* * *

### variable[#](#variable)

  

Manage variables in the engine, allowing for dynamic data handling and manipulation.

## Asset Sources[#](#asset-sources)

Methods for adding default and demo asset sources to the engine.

### addDefaultAssetSources()[#](#adddefaultassetsources)

  

Register a set of asset sources containing default assets.

Available default asset sources:

*   `'ly.img.sticker'` - Various stickers
*   `'ly.img.vectorpath'` - Shapes and arrows
*   `'ly.img.filter.lut'` - LUT effects of various kinds
*   `'ly.img.filter.duotone'` - Color effects of various kinds

These assets are parsed at `\{\{base_url\}\}/<id>/content.json`, where `base_url` defaults to the IMG.LY CDN. Each source is created via `addLocalSource` and populated with the parsed assets. To modify the available assets, you may either exclude certain IDs via `excludeAssetSourceIds` or alter the sources after creation.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | { `baseURL?`: `string`; `excludeAssetSourceIds?`: [`DefaultAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/defaultassetsourceid/)\[\]; } | Configuration options for loading default asset sources. |
| `options.baseURL?` | `string` | The source of the asset definitions, must be absolute. Defaults to IMG.LY CDN. |
| `options.excludeAssetSourceIds?` | [`DefaultAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/defaultassetsourceid/)\[\] | A list of IDs, that will be ignored during load. |

#### Returns[#](#returns-7)

`Promise`<`void`\>

A promise that resolves when all asset sources are loaded.

#### Signature[#](#signature-5)

```
addDefaultAssetSources(options?: object): Promise<void>
```

* * *

### addDemoAssetSources()[#](#adddemoassetsources)

  

Register a set of demo asset sources containing example assets.

**Note**: These are demonstration assets not meant for production use.

Available demo asset sources:

*   `'ly.img.image'` - Sample images
*   `'ly.img.image.upload'` - Demo source to upload image assets
*   `'ly.img.audio'` - Sample audios
*   `'ly.img.audio.upload'` - Demo source to upload audio assets
*   `'ly.img.video'` - Sample videos
*   `'ly.img.video.upload'` - Demo source to upload video assets

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | { `baseURL?`: `string`; `excludeAssetSourceIds?`: [`DemoAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/demoassetsourceid/)\[\]; `sceneMode?`: `"Design"` | `"Video"`; `withUploadAssetSources?`: `boolean`; } |
| `options.baseURL?` | `string` | The source of the demo asset definitions, must be absolute. Defaults to IMG.LY CDN. |
| `options.excludeAssetSourceIds?` | [`DemoAssetSourceId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/demoassetsourceid/)\[\] | A list of IDs, that will be ignored during load |
| `options.sceneMode?` | `"Design"` | `"Video"` |
| `options.withUploadAssetSources?` | `boolean` | If ‘true’ asset sources for uploads are added (default false) |

#### Returns[#](#returns-8)

`Promise`<`void`\>

A promise that resolves when all demo asset sources are loaded.

#### Signature[#](#signature-6)

```
addDemoAssetSources(options?: object): Promise<void>
```

## Experimental Features[#](#experimental-features)

Experimental APIs that may change or be removed in future versions.

### unstable\_setVideoExportInactivityTimeout()[#](#unstable_setvideoexportinactivitytimeout)

Configure the timeout for video export inactivity detection.

Some browsers exhibit a bug where support for certain video codecs is offered, but when attempting to decode or encode in these codecs, the request will simply never return. We detect that situation using a timeout. To prevent this mechanism from triggering in situations where the export simply takes long because of a slow device, you can configure the timeout here.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `timeout` | `number` | Timeout in milliseconds. Defaults to 10 seconds. This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-9)

`void`

* * *

### unstable\_setExportInactivityTimeout()[#](#unstable_setexportinactivitytimeout)

Configure the timeout for block-exports in WebWorkers.

If exporting a block hangs because resources take too long to initialize, the export will be aborted after this many ms.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `timeout` | `number` | Timeout in milliseconds (default: 10 000) This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-10)

`void`

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/creativeeditorsdk)