# Class: SceneAPI

Create, load, save, and manipulate scenes.

Scenes are the root element of every design hierarchy. Their children, stacks of pages, individual pages or other blocks, define the content of the design. Scenes can be created from scratch, loaded from a file or URL, or created from an image or video. After manipulation, they can be saved to a string or an archive. This allows further processing in another editor instance, automated processing in scripts or sharing with other users.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`SceneAPI`

## Scene Creation[#](#scene-creation)

Create new scenes from scratch or from media files.

### create()[#](#create)

  

Create a new design scene, along with its own camera.

```
const scene = engine.scene.create(layout);
```

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `sceneLayout?` | `"Free"` | `"VerticalStack"` |
| `options?` | [`CreateSceneOptions`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/createsceneoptions/) | Optional parameters for the scene. Properties: - `page` - Page options. Properties: - `size` - The size of the page. - `color` - Optional background color of the page. |

#### Returns[#](#returns)

`number`

The scene’s handle.

#### Signature[#](#signature)

```
create(sceneLayout?: "Free" | "VerticalStack" | "HorizontalStack" | "DepthStack", options?: CreateSceneOptions): number
```

* * *

### createVideo()[#](#createvideo)

  

Create a new scene in video mode, along with its own camera.

```
const scene = engine.scene.createVideo();
```

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | [`CreateSceneOptions`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/createsceneoptions/) | Optional parameters for the scene. Properties: - `page` - Page options. Properties: - `size` - The size of the page. - `color` - Optional background color of the page. |

#### Returns[#](#returns-1)

`number`

The scene’s handle.

#### Signature[#](#signature-1)

```
createVideo(options?: CreateSceneOptions): number
```

* * *

### createFromImage()[#](#createfromimage)

  

Loads the given image and creates a scene with a single page showing the image.

Fetching the image may take an arbitrary amount of time, so the scene isn’t immediately available.

```
const scene = await engine.scene.createFromImage('https://img.ly/static/ubq_samples/sample_4.jpg');
```

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The image URL. |
| `dpi?` | `number` | The scene’s DPI. |
| `pixelScaleFactor?` | `number` | The display’s pixel scale factor. |
| `sceneLayout?` | `"Free"` | `"VerticalStack"` |
| `spacing?` | `number` | \- |
| `spacingInScreenSpace?` | `boolean` | \- |

#### Returns[#](#returns-2)

`Promise`<`number`\>

A promise that resolves with the scene ID on success or rejected with an error otherwise.

#### Signature[#](#signature-2)

```
createFromImage(url: string, dpi?: number, pixelScaleFactor?: number, sceneLayout?: "Free" | "VerticalStack" | "HorizontalStack" | "DepthStack", spacing?: number, spacingInScreenSpace?: boolean): Promise<number>
```

* * *

### createFromVideo()[#](#createfromvideo)

  

Loads the given video and creates a scene with a single page showing the video.

Fetching the video may take an arbitrary amount of time, so the scene isn’t immediately available.

```
const scene = await engine.scene.createFromVideo('https://img.ly/static/ubq_video_samples/bbb.mp4');
```

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The video URL. |

#### Returns[#](#returns-3)

`Promise`<`number`\>

A promise that resolves with the scene ID on success or rejected with an error otherwise.

#### Signature[#](#signature-3)

```
createFromVideo(url: string): Promise<number>
```

## Scene Loading[#](#scene-loading)

Load scenes from various sources including strings, URLs, and archives.

### loadFromString()[#](#loadfromstring)

  

Load the contents of a scene file.

The string must be the binary contents of a scene file and is directly imported as blocks. Any existing scene is replaced by the new one. This is useful for loading scenes that were saved with `saveToString` or scenes that were created in another editor instance.

```
const sceneContent = await creativeEngine.scene.saveToString();creativeEngine.scene.loadFromString(sceneContent);
```

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `sceneContent` | `string` | The scene file contents, a base64 string. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |
| `waitForResources?` | `boolean` | Whether to wait for all resources to finish loading before resolving. Defaults to false. |

#### Returns[#](#returns-4)

`Promise`<`number`\>

A handle to the loaded scene.

#### Signature[#](#signature-4)

```
loadFromString(sceneContent: string, overrideEditorConfig?: boolean, waitForResources?: boolean): Promise<number>
```

* * *

### loadFromURL()[#](#loadfromurl)

  

Load a scene from the URL to the scene file.

The scene file will be fetched asynchronously by the engine and loaded into the engine once it is available. Any existing scene is replaced by the new one.

```
const sceneURL = 'https://example.com/my-scene.json';creativeEngine.scene.loadFromURL(sceneURL);
```

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the scene file. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |
| `waitForResources?` | `boolean` | Whether to wait for all resources to finish loading before resolving. Defaults to false. |

#### Returns[#](#returns-5)

`Promise`<`number`\>

scene A promise that resolves once the scene was loaded or rejects with an error otherwise.

#### Signature[#](#signature-5)

```
loadFromURL(url: string, overrideEditorConfig?: boolean, waitForResources?: boolean): Promise<number>
```

* * *

### loadFromArchiveURL()[#](#loadfromarchiveurl)

  

Load a previously archived scene from the URL to the scene file.

The scene file will be fetched asynchronously by the engine. This requires continuous `render` calls on this engines instance.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the scene archive file. |
| `overrideEditorConfig?` | `boolean` | Whether to override editor configuration with settings and data from the scene file. Defaults to false. |
| `waitForResources?` | `boolean` | Whether to wait for all resources to finish loading before resolving. Defaults to false. |

#### Returns[#](#returns-6)

`Promise`<`number`\>

scene A promise that resolves once the scene was loaded or rejects with an error otherwise.

#### Signature[#](#signature-6)

```
loadFromArchiveURL(url: string, overrideEditorConfig?: boolean, waitForResources?: boolean): Promise<number>
```

## Scene Saving[#](#scene-saving)

Save and export scenes to different formats.

### saveToString()[#](#savetostring)

  

Serializes the current scene into a string. Selection is discarded.

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `allowedResourceSchemes?` | `string`\[\] | The resource schemes to allow in the saved string. Defaults to \[‘blob’, ‘bundle’, ‘file’, ‘http’, ‘https’, ‘opfs’\]. |
| `onDisallowedResourceScheme?` | (`url`, `dataHash`) => `Promise`<`string`\> | An optional callback that is called for each resource URL that has a scheme absent from `resourceSchemesAllowed`. The `url` parameter is the resource URL and the `dataHash` parameter is the hash of the resource’s data. The callback should return a new URL for the resource, which will be used in the serialized scene. The callback is expected to return the original URL if no persistence is needed. |

#### Returns[#](#returns-7)

`Promise`<`string`\>

A promise that resolves with a string on success or an error on failure.

#### Signature[#](#signature-7)

```
saveToString(allowedResourceSchemes?: string[], onDisallowedResourceScheme?: (url: string, dataHash: string) => Promise<string>): Promise<string>
```

* * *

### saveToArchive()[#](#savetoarchive)

  

Saves the current scene and all of its referenced assets into an archive.

The archive contains all assets, that were accessible when this function was called. Blocks in the archived scene reference assets relative from to the location of the scene file. These references are resolved when loading such a scene via `loadSceneFromURL`.

#### Returns[#](#returns-8)

`Promise`<`Blob`\>

A promise that resolves with a Blob on success or an error on failure.

#### Signature[#](#signature-8)

```
saveToArchive(): Promise<Blob>
```

## Page Management[#](#page-management)

Manage pages within scenes and find elements.

### getPages()[#](#getpages)

  

Get the sorted list of pages in the scene.

```
const pages = engine.scene.getPages();
```

#### Returns[#](#returns-9)

`number`\[\]

The sorted list of pages in the scene.

#### Signature[#](#signature-9)

```
getPages(): number[]
```

* * *

### getCurrentPage()[#](#getcurrentpage)

  

Get the current page, i.e., the page of the first selected element if this page is at least 25% visible or, otherwise, the page nearest to the viewport center.

```
const currentPage = engine.scene.getCurrentPage();
```

#### Returns[#](#returns-10)

`number`

The current page in the scene or null.

#### Signature[#](#signature-10)

```
getCurrentPage(): number
```

* * *

### findNearestToViewPortCenterByType()[#](#findnearesttoviewportcenterbytype)

  

Find all blocks with the given type sorted by the distance to viewport center.

```
// Use longhand block type ID to find nearest pages.let nearestPageByType = engine.scene.findNearestToViewPortCenterByType('//ly.img.ubq/page')[0];// Or use shorthand block type ID.nearestPageByType = engine.scene.findNearestToViewPortCenterByType('page')[0];
```

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`DesignBlockType`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/designblocktype/) | The type to search for. |

#### Returns[#](#returns-11)

`number`\[\]

A list of block ids sorted by distance to viewport center.

#### Signature[#](#signature-11)

```
findNearestToViewPortCenterByType(type: DesignBlockType): number[]
```

* * *

### findNearestToViewPortCenterByKind()[#](#findnearesttoviewportcenterbykind)

  

Find all blocks with the given kind sorted by the distance to viewport center.

```
let nearestImageByKind = engine.scene.findNearestToViewPortCenterByKind('image')[0];
```

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `string` | The kind to search for. |

#### Returns[#](#returns-12)

`number`\[\]

A list of block ids sorted by distance to viewport center.

#### Signature[#](#signature-12)

```
findNearestToViewPortCenterByKind(kind: string): number[]
```

## Event Subscriptions[#](#event-subscriptions)

Subscribe to scene-related events and changes.

### onZoomLevelChanged()[#](#onzoomlevelchanged)

  

Subscribe to changes to the zoom level.

```
const unsubscribeZoomLevelChanged = engine.scene.onZoomLevelChanged(() => {  const zoomLevel = engine.scene.getZoomLevel();  console.log('Zoom level is now: ', zoomLevel);});
```

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | This function is called at the end of the engine update, if the zoom level has changed. |

#### Returns[#](#returns-13)

A method to unsubscribe.

```
(): void;
```

##### Returns[#](#returns-14)

`void`

* * *

### onActiveChanged()[#](#onactivechanged)

  

Subscribe to changes to the active scene rendered by the engine.

```
const unsubscribe = engine.scene.onActiveChanged(() => {  const newActiveScene = engine.scene.get();});
```

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | This function is called at the end of the engine update, if the active scene has changed. |

#### Returns[#](#returns-15)

A method to unsubscribe.

```
(): void;
```

##### Returns[#](#returns-16)

`void`

## Experimental Features[#](#experimental-features)

Experimental features that may change or be removed in future versions.

### unstable\_enableCameraPositionClamping()[#](#unstable_enablecamerapositionclamping)

Continually ensures the camera position to be within the width and height of the blocks axis-aligned bounding box. Disables any previously set camera position clamping in the scene and also takes priority over clamp camera commands.

```
// Keep the scene with padding of 10px within the cameraengine.scene.unstable_enableCameraPositionClamping([scene], 10.0, 10.0, 10.0, 10.0, 0.0, 0.0, 0.0, 0.0);
```

Without padding, this results in a tight clamp on the block. With padding, the padded part of the blocks is ensured to be visible.

#### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The blocks to which the camera position is adjusted to, usually, the scene or a page. |
| `paddingLeft?` | `number` | Optional padding in screen pixels to the left of the block. |
| `paddingTop?` | `number` | Optional padding in screen pixels to the top of the block. |
| `paddingRight?` | `number` | Optional padding in screen pixels to the right of the block. |
| `paddingBottom?` | `number` | Optional padding in screen pixels to the bottom of the block. |
| `scaledPaddingLeft?` | `number` | Optional padding in screen pixels to the left of the block that scales with the zoom level until five times the initial value. |
| `scaledPaddingTop?` | `number` | Optional padding in screen pixels to the top of the block that scales with the zoom level until five times the initial value. |
| `scaledPaddingRight?` | `number` | Optional padding in screen pixels to the right of the block that scales with the zoom level until five times the initial value. |
| `scaledPaddingBottom?` | `number` | Optional padding in screen pixels to the bottom of the block that scales with the zoom level until five times the initial value. This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-17)

`void`

* * *

### unstable\_disableCameraPositionClamping()[#](#unstable_disablecamerapositionclamping)

Disables any previously set position clamping for the current scene.

```
engine.scene.unstable_disableCameraPositionClamping();
```

#### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene?` | `number` | Optionally, the scene or a block in the scene for which to query the position clamping. This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-18)

`void`

* * *

### unstable\_isCameraPositionClampingEnabled()[#](#unstable_iscamerapositionclampingenabled)

Queries whether position clamping is enabled.

```
engine.scene.unstable_isCameraPositionClampingEnabled();
```

#### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene?` | `number` | Optionally, the scene or a block in the scene for which to query the position clamping. |

#### Returns[#](#returns-19)

`boolean`

True if the given block has position clamping set or the scene contains a block for which position clamping is set, false otherwise. This API is experimental and may change or be removed in future versions.

* * *

### unstable\_enableCameraZoomClamping()[#](#unstable_enablecamerazoomclamping)

Continually ensures the zoom level of the camera in the active scene to be in the given range.

```
// Allow zooming from 12.5% to 800% relative to the size of a pageengine.scene.unstable_enableCameraZoomClamping([page], 0.125, 8.0, 0.0, 0.0, 0.0, 0.0);
```

#### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The blocks to which the camera zoom limits are adjusted to, usually, the scene or a page. |
| `minZoomLimit?` | `number` | The minimum zoom level limit when zooming out, unlimited when negative. |
| `maxZoomLimit?` | `number` | The maximum zoom level limit when zooming in, unlimited when negative. |
| `paddingLeft?` | `number` | Optional padding in screen pixels to the left of the block. Only applied when the block is not a camera. |
| `paddingTop?` | `number` | Optional padding in screen pixels to the top of the block. Only applied when the block is not a camera. |
| `paddingRight?` | `number` | Optional padding in screen pixels to the right of the block. Only applied when the block is not a camera. |
| `paddingBottom?` | `number` | Optional padding in screen pixels to the bottom of the block. Only applied when the block is not a camera. This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-20)

`void`

* * *

### unstable\_disableCameraZoomClamping()[#](#unstable_disablecamerazoomclamping)

Disables any previously set zoom clamping for the current scene.

```
engine.scene.unstable_disableCameraZoomClamping();
```

#### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene?` | `number` | Optionally, the scene or a block for which to query the zoom clamping. This API is experimental and may change or be removed in future versions. |

#### Returns[#](#returns-21)

`void`

* * *

### unstable\_isCameraZoomClampingEnabled()[#](#unstable_iscamerazoomclampingenabled)

Queries whether zoom clamping is enabled.

```
engine.scene.unstable_isCameraZoomClampingEnabled();
```

#### Parameters[#](#parameters-17)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene?` | `number` | Optionally, the scene or a block for which to query the zoom clamping. |

#### Returns[#](#returns-22)

`boolean`

True if the given block has zoom clamping set or the scene contains a block for which zoom clamping is set, false otherwise. This API is experimental and may change or be removed in future versions.

## Scene Properties[#](#scene-properties)

Get and set scene properties like design units and mode.

### get()[#](#get)

  

Return the currently active scene.

```
const scene = engine.scene.get();
```

#### Returns[#](#returns-23)

`number`

The scene or null, if none was created yet.

#### Signature[#](#signature-13)

```
get(): number
```

* * *

### getMode()[#](#getmode)

  

Get the current scene mode.

```
const mode = scene.getMode();
```

#### Returns[#](#returns-24)

`"Design"` | `"Video"`

The current mode of the scene.

#### Signature[#](#signature-14)

```
getMode(): "Design" | "Video"
```

* * *

### setDesignUnit()[#](#setdesignunit)

  

Converts all values of the current scene into the given design unit.

```
engine.scene.setDesignUnit('Pixel');
```

#### Parameters[#](#parameters-18)

| Parameter | Type | Description |
| --- | --- | --- |
| `designUnit` | `"Pixel"` | `"Millimeter"` |

#### Returns[#](#returns-25)

`void`

#### Signature[#](#signature-15)

```
setDesignUnit(designUnit: "Pixel" | "Millimeter" | "Inch"): void
```

* * *

### getDesignUnit()[#](#getdesignunit)

  

Returns the design unit of the current scene.

```
engine.scene.getDesignUnit();
```

#### Returns[#](#returns-26)

`"Pixel"` | `"Millimeter"` | `"Inch"`

The current design unit.

#### Signature[#](#signature-16)

```
getDesignUnit(): "Pixel" | "Millimeter" | "Inch"
```

* * *

### getLayout()[#](#getlayout)

  

Get the layout of the current scene.

```
const layout = engine.scene.getLayout();
```

#### Returns[#](#returns-27)

`"Free"` | `"VerticalStack"` | `"HorizontalStack"` | `"DepthStack"`

The current layout of the scene.

#### Signature[#](#signature-17)

```
getLayout(): "Free" | "VerticalStack" | "HorizontalStack" | "DepthStack"
```

* * *

### setLayout()[#](#setlayout)

  

Set the layout of the current scene. This will handle all necessary conversions including creating or destroying stack blocks and reparenting pages as needed.

When transitioning from stack layouts (VerticalStack, HorizontalStack, DepthStack) to Free layout, the global positions of pages are preserved to maintain their visual appearance in the scene.

```
engine.scene.setLayout('VerticalStack');
```

#### Parameters[#](#parameters-19)

| Parameter | Type | Description |
| --- | --- | --- |
| `layout` | `"Free"` | `"VerticalStack"` |

#### Returns[#](#returns-28)

`void`

#### Signature[#](#signature-18)

```
setLayout(layout: "Free" | "VerticalStack" | "HorizontalStack" | "DepthStack"): void
```

## Template Operations[#](#template-operations)

Apply templates to existing scenes.

### applyTemplateFromString()[#](#applytemplatefromstring)

  

Applies the contents of the given template scene to the currently loaded scene.

This loads the template scene while keeping the design unit and page dimensions of the current scene. The content of the pages is automatically adjusted to fit the new dimensions.

```
engine.scene.applyTemplateFromString("UBQ1ewoiZm9ybWF0Ij...");
```

#### Parameters[#](#parameters-20)

| Parameter | Type | Description |
| --- | --- | --- |
| `content` | `string` | The template scene file contents, a base64 string. |

#### Returns[#](#returns-29)

`Promise`<`void`\>

A Promise that resolves once the template was applied or rejects if there was an error.

#### Signature[#](#signature-19)

```
applyTemplateFromString(content: string): Promise<void>
```

* * *

### applyTemplateFromURL()[#](#applytemplatefromurl)

  

Applies the contents of the given template scene to the currently loaded scene.

This loads the template scene while keeping the design unit and page dimensions of the current scene. The content of the pages is automatically adjusted to fit the new dimensions.

```
engine.scene.applyTemplateFromURL('https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene');
```

#### Parameters[#](#parameters-21)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The url to the template scene file. |

#### Returns[#](#returns-30)

`Promise`<`void`\>

A Promise that resolves once the template was applied or rejects if there was an error.

#### Signature[#](#signature-20)

```
applyTemplateFromURL(url: string): Promise<void>
```

## Camera & Zoom[#](#camera--zoom)

Control camera position, zoom levels, and auto-fit behavior.

### setZoomLevel()[#](#setzoomlevel)

  

Set the zoom level of the scene, e.g., for headless versions.

This only shows an effect if the zoom level is not handled/overwritten by the UI. Setting a zoom level of 2.0f results in one dot in the design to be two pixels on the screen.

```
// Zoom to 100%engine.scene.setZoomLevel(1.0);
// Zoom to 50%engine.scene.setZoomLevel(0.5 * engine.scene.getZoomLevel());
```

#### Parameters[#](#parameters-22)

| Parameter | Type | Description |
| --- | --- | --- |
| `zoomLevel?` | `number` | The new zoom level. |

#### Returns[#](#returns-31)

`void`

#### Signature[#](#signature-21)

```
setZoomLevel(zoomLevel?: number): void
```

* * *

### getZoomLevel()[#](#getzoomlevel)

  

Get the zoom level of the scene or for a camera in the scene in unit `dpx/dot`. A zoom level of 2.0 results in one pixel in the design to be two pixels on the screen.

```
const zoomLevel = engine.scene.getZoomLevel();
```

#### Returns[#](#returns-32)

`number`

The zoom level of the block’s camera.

#### Signature[#](#signature-22)

```
getZoomLevel(): number
```

* * *

### zoomToBlock()[#](#zoomtoblock)

  

Sets the zoom and focus to show a block, optionally with animation. This only shows an effect if the zoom level is not handled/overwritten by the UI. Without padding, this results in a tight view on the block.

##### Parameters[#](#parameters-23)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block that should be focused on. |
| `options?` | [`ZoomOptions`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/zoomoptions/) | Configuration for padding and animation. |

##### Returns[#](#returns-33)

`Promise`<`void`\>

A promise that resolves once the zoom was set or rejects with an error otherwise.

#### Call Signature[#](#call-signature)

```
zoomToBlock(   id,   paddingLeft?,   paddingTop?,   paddingRight?,paddingBottom?): Promise<void>;
```

Sets the zoom and focus to show a block.

This only shows an effect if the zoom level is not handled/overwritten by the UI. Without padding, this results in a tight view on the block.

```
// Bring entire scene in view with padding of 20px in all directionsengine.scene.zoomToBlock(scene, 20.0, 20.0, 20.0, 20.0);
```

##### Parameters[#](#parameters-24)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block that should be focused on. |
| `paddingLeft?` | `number` | Optional padding in screen pixels to the left of the block. |
| `paddingTop?` | `number` | Optional padding in screen pixels to the top of the block. |
| `paddingRight?` | `number` | Optional padding in screen pixels to the right of the block. |
| `paddingBottom?` | `number` | Optional padding in screen pixels to the bottom of the block. |

##### Returns[#](#returns-34)

`Promise`<`void`\>

A promise that resolves once the zoom was set or rejects with an error otherwise.

##### Deprecated[#](#deprecated)

Use zoomToBlock with options object instead

#### Signatures[#](#signatures)

```
zoomToBlock(id: number, options?: ZoomOptions): Promise<void>
```

```
zoomToBlock(id: number, paddingLeft?: number, paddingTop?: number, paddingRight?: number, paddingBottom?: number): Promise<void>
```

* * *

### enableZoomAutoFit()[#](#enablezoomautofit)

  

Continually adjusts the zoom level to fit the width or height of a block’s axis-aligned bounding box.

This only shows an effect if the zoom level is not handled/overwritten by the UI. Without padding, this results in a tight view on the block. No more than one block per scene can have zoom auto-fit enabled. Calling `setZoomLevel` or `zoomToBlock` disables the continuous adjustment.

```
// Follow page with padding of 20px horizontally before and after the blockengine.scene.enableZoomAutoFit(page, 'Horizontal', 20, 20)
```

##### Parameters[#](#parameters-25)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block for which the zoom is adjusted. |
| `axis` | `"Horizontal"` | `"Vertical"` |
| `paddingBefore?` | `number` | Optional padding in screen pixels before the block. |
| `paddingAfter?` | `number` | Optional padding in screen pixels after the block. |

##### Returns[#](#returns-35)

`void`

#### Call Signature[#](#call-signature-1)

```
enableZoomAutoFit(   id,   axis,   paddingLeft?,   paddingTop?,   paddingRight?,   paddingBottom?): void;
```

Continually adjusts the zoom level to fit the width or height of a block’s axis-aligned bounding box.

This only shows an effect if the zoom level is not handled/overwritten by the UI. Without padding, this results in a tight view on the block. Calling `setZoomLevel` or `zoomToBlock` disables the continuous adjustment.

```
// Follow page with padding of 20px in both directionsengine.scene.enableZoomAutoFit(page, 'Both', 20.0, 20.0, 20.0, 20.0);
```

##### Parameters[#](#parameters-26)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block for which the zoom is adjusted. |
| `axis` | `"Both"` | The block axis for which the zoom is adjusted. |
| `paddingLeft?` | `number` | Optional padding in screen pixels to the left of the block. |
| `paddingTop?` | `number` | Optional padding in screen pixels to the top of the block. |
| `paddingRight?` | `number` | Optional padding in screen pixels to the right of the block. |
| `paddingBottom?` | `number` | Optional padding in screen pixels to the bottom of the block. |

##### Returns[#](#returns-36)

`void`

#### Signatures[#](#signatures-1)

```
enableZoomAutoFit(id: number, axis: "Horizontal" | "Vertical", paddingBefore?: number, paddingAfter?: number): void
```

```
enableZoomAutoFit(id: number, axis: "Both", paddingLeft?: number, paddingTop?: number, paddingRight?: number, paddingBottom?: number): void
```

* * *

### disableZoomAutoFit()[#](#disablezoomautofit)

  

Disables any previously set zoom auto-fit.

```
engine.scene.disableZoomAutoFit(scene);
```

#### Parameters[#](#parameters-27)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene` | `number` | The scene or a block in the scene for which to disable zoom auto-fit. |

#### Returns[#](#returns-37)

`void`

#### Signature[#](#signature-23)

```
disableZoomAutoFit(blockOrScene: number): void
```

* * *

### isZoomAutoFitEnabled()[#](#iszoomautofitenabled)

  

Queries whether zoom auto-fit is enabled for the given block.

```
engine.scene.isZoomAutoFitEnabled(scene);
```

#### Parameters[#](#parameters-28)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockOrScene` | `number` | The scene or a block in the scene for which to query the zoom auto-fit. |

#### Returns[#](#returns-38)

`boolean`

True if the given block has auto-fit set or the scene contains a block for which auto-fit is set, false otherwise.

#### Signature[#](#signature-24)

```
isZoomAutoFitEnabled(blockOrScene: number): boolean
```

## Other[#](#other)

### setPlaying()[#](#setplaying)

  

Starts or stops playback of the current scene. Only works in Video mode, not in Design mode.

#### Parameters[#](#parameters-29)

| Parameter | Type | Description |
| --- | --- | --- |
| `play` | `boolean` | True to start playback, false to stop |

#### Returns[#](#returns-39)

`void`

#### Throws[#](#throws)

Error if no page is available for playback

#### Signature[#](#signature-25)

```
setPlaying(play: boolean): void
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/classes/eventapi)