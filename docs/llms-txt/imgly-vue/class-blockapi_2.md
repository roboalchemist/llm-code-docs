# Class: BlockAPI

Create, manipulate, and query the building blocks of your design.

This is the primary interface for all block-level operations. Use it to manage the entire lifecycle of blocks from creation and serialization to destruction. You can precisely control a block’s appearance by modifying its fills, strokes, and effects, or transform its position, size, and rotation. The API also includes powerful features for managing complex content like text and video, organizing blocks into groups and hierarchies, and exporting final designs to various formats.

## Block Lifecycle[#](#block-lifecycle)

Manage the complete lifecycle: create, find, duplicate, destroy, and serialize blocks.

### loadFromString()[#](#loadfromstring)

  

Loads blocks from a serialized string.

The blocks are not attached by default and won’t be visible until attached to a page or the scene. The UUID of the loaded blocks is replaced with a new one.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `content` | `string` | A string representing the given blocks. |

#### Returns[#](#returns)

`Promise`<`number`\[\]>

A promise that resolves with a list of handles representing the found blocks or an error.

#### Example[#](#example)

```
const serializedBlocks = await engine.block.saveToString([pageBlockId]);// Later, load those blocksconst loadedBlocks = await engine.block.loadFromString(serializedBlocks);// Attach the first loaded block to the sceneengine.block.appendChild(sceneBlockId, loadedBlocks[0]);
```

#### Signature[#](#signature)

```
loadFromString(content: string): Promise<number[]>
```

* * *

### loadFromArchiveURL()[#](#loadfromarchiveurl)

  

Loads blocks from a remote archive URL.

The URL should be that of a file previously saved with `block.saveToArchive`. The blocks are not attached by default and won’t be visible until attached to a page or the scene. The UUID of the loaded blocks is replaced with a new one.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL of the blocks archive file. |

#### Returns[#](#returns-1)

`Promise`<`number`\[\]>

A promise that resolves with a list of handles representing the found blocks or an error.

#### Example[#](#example-1)

```
// Load blocks from a remote archiveconst loadedBlocks = await engine.block.loadFromArchiveURL('https://example.com/blocks.zip');// Attach the first loaded block to the sceneengine.block.appendChild(sceneBlockId, loadedBlocks[0]);
```

#### Signature[#](#signature-1)

```
loadFromArchiveURL(url: string): Promise<number[]>
```

* * *

### loadFromURL()[#](#loadfromurl)

  

Loads blocks from a URL.

The URL should point to a blocks file within an unzipped archive directory previously saved with `block.saveToArchive`. The blocks are not attached by default and won’t be visible until attached to a page or the scene. The UUID of the loaded blocks is replaced with a new one.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | The URL to the blocks file |

#### Returns[#](#returns-2)

`Promise`<`number`\[\]>

A promise that resolves with a list of block handles

#### Example[#](#example-2)

```
// Load blocks from a URLconst loadedBlocks = await engine.block.loadFromURL('https://example.com/blocks.blocks');// Attach the first loaded block to the sceneengine.block.appendChild(sceneBlockId, loadedBlocks[0]);
```

#### Signature[#](#signature-2)

```
loadFromURL(url: string): Promise<number[]>
```

* * *

### saveToString()[#](#savetostring)

  

Saves the given blocks to a serialized string.

If a page with multiple children is given, the entire hierarchy is saved.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `blocks` | `number`\[\] | The blocks to save. |
| `allowedResourceSchemes` | `string`\[\] | The resource schemes to allow in the saved string. Defaults to \[‘buffer’, ‘http’, ‘https’\]. |
| `onDisallowedResourceScheme?` | (`url`, `dataHash`) => `Promise`<`string`\> | An optional callback that is called for each resource URL that has a scheme absent from `resourceSchemesAllowed`. The `url` parameter is the resource URL and the `dataHash` parameter is the hash of the resource’s data. The callback should return a new URL for the resource, which will be used in the serialized scene. The callback is expected to return the original URL if no persistence is needed. |

#### Returns[#](#returns-3)

`Promise`<`string`\>

A promise that resolves to a string representing the blocks or an error.

#### Example[#](#example-3)

```
// Create a page with a text elementconst page = engine.block.create('page');const text = engine.block.create('text');engine.block.appendChild(page, text);
// Save the whole page hierarchy to a stringconst serialized = await engine.block.saveToString([page]);
```

#### Signature[#](#signature-3)

```
saveToString(blocks: number[], allowedResourceSchemes?: string[], onDisallowedResourceScheme?: (url: string, dataHash: string) => Promise<string>): Promise<string>
```

* * *

### saveToArchive()[#](#savetoarchive)

  

Saves the given blocks and their assets to a zip archive.

The archive contains all assets that were accessible when this function was called. Blocks in the archived scene reference assets relative to the location of the scene file.

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `blocks` | `number`\[\] | The blocks to save. |

#### Returns[#](#returns-4)

`Promise`<`Blob`\>

A promise that resolves with a Blob on success or an error on failure.

#### Signature[#](#signature-4)

```
saveToArchive(blocks: number[]): Promise<Blob>
```

* * *

### create()[#](#create)

  

Creates a new block of a given type.

```
// Create a new text blockconst text = engine.block.create('text');const page = engine.scene.getCurrentPage();engine.block.appendChild(page, text);
// Create a new image blockconst image = engine.block.create('graphic');engine.block.setShape(image, engine.block.createShape('rect'));const imageFill = engine.block.createFill('image');engine.block.setFill(image, imageFill);engine.block.setString(imageFill, 'fill/image/imageFileURI', 'https://img.ly/static/ubq_samples/sample_1.jpg');engine.block.appendChild(page, image);
// Create a new video blockconst video = engine.block.create('graphic');engine.block.setShape(video, engine.block.createShape('rect'));const videoFill = engine.block.createFill('video');engine.block.setString(videoFill, 'fill/video/fileURI', 'https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4');engine.block.setFill(video, videoFill);engine.block.appendChild(page, video);
```

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`DesignBlockType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblocktype/) | The type of the block that shall be created. |

#### Returns[#](#returns-5)

`number`

The created block’s handle.

#### Signature[#](#signature-5)

```
create(type: DesignBlockType): number
```

* * *

### duplicate()[#](#duplicate)

  

Duplicates a block and its children.

#### Parameters[#](#parameters-6)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block to duplicate. |
| `attachToParent` | `boolean` | `true` | Whether the duplicated block should be attached to the original’s parent. Defaults to true. |

#### Returns[#](#returns-6)

`number`

The handle of the duplicate.

#### Signature[#](#signature-6)

```
duplicate(id: number, attachToParent?: boolean): number
```

* * *

### destroy()[#](#destroy)

  

Destroys a block and its children.

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to destroy. |

#### Returns[#](#returns-7)

`void`

#### Signature[#](#signature-7)

```
destroy(id: number): void
```

* * *

### forceLoadResources()[#](#forceloadresources)

  

Forces the loading of resources for a set of blocks and their children.

This is useful for preloading resources. If a resource failed to load previously, it will be reloaded.

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The blocks whose resources should be loaded. |

#### Returns[#](#returns-8)

`Promise`<`void`\>

A Promise that resolves once all resources have finished loading.

#### Signature[#](#signature-8)

```
forceLoadResources(ids: number[]): Promise<void>
```

## Block Exploration[#](#block-exploration)

Find blocks by properties like name, type, or kind.

### findByName()[#](#findbyname)

  

Finds all blocks with a given name.

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name to search for. |

#### Returns[#](#returns-9)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-9)

```
findByName(name: string): number[]
```

* * *

### findByType()[#](#findbytype)

  

Finds all blocks with a given type.

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`ObjectType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttype/) | The type to search for. |

#### Returns[#](#returns-10)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-10)

```
findByType(type: ObjectType): number[]
```

* * *

### findByKind()[#](#findbykind)

  

Finds all blocks with a given kind.

```
const allTitles = engine.block.findByKind('title');
```

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `string` | The kind to search for. |

#### Returns[#](#returns-11)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-11)

```
findByKind(kind: string): number[]
```

* * *

### findAll()[#](#findall)

  

Finds all blocks known to the engine.

#### Returns[#](#returns-12)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-12)

```
findAll(): number[]
```

* * *

### findAllPlaceholders()[#](#findallplaceholders)

  

Finds all placeholder blocks in the current scene.

#### Returns[#](#returns-13)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-13)

```
findAllPlaceholders(): number[]
```

## Block Export[#](#block-export)

Export blocks to various formats like images, videos, and audio.

### export()[#](#export)

  

Exports a design block to a Blob.

Performs an internal update to resolve the final layout for the blocks.

##### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. |
| `options?` | [`EngineExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineexportoptions/) | The options for exporting the block type, including mime type and export settings. |

##### Returns[#](#returns-14)

`Promise`<`Blob`\>

A promise that resolves with the exported image or is rejected with an error.

#### Call Signature[#](#call-signature)

```
export(   handle,   mimeType?,options?): Promise<Blob>;
```

Exports a design block to a Blob.

Performs an internal update to resolve the final layout for the blocks.

##### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. |
| `mimeType?` |  | `"application/octet-stream"` |
| `options?` | `Omit`<[`EngineExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineexportoptions/), `"mimeType"`\> | The options for exporting the block type |

##### Returns[#](#returns-15)

`Promise`<`Blob`\>

A promise that resolves with the exported image or is rejected with an error.

##### Deprecated[#](#deprecated)

Use the new `export` signature instead

##### Example[#](#example-4)

```
// Before migrationconst blob = await cesdk.block.export(blockId, MimeType.Png, { pngCompressionLevel: 5 })// After migrationconst blob = await cesdk.block.export(blockId, { mimeType: 'image/png', pngCompressionLevel: 5 })
```

#### Signatures[#](#signatures)

```
export(handle: number, options?: ExportOptions): Promise<Blob>
```

```
export(handle: number, mimeType?: "application/octet-stream" | "application/pdf" | ImageMimeType, options?: Omit<ExportOptions, "mimeType">): Promise<Blob>
```

* * *

### exportWithColorMask()[#](#exportwithcolormask)

  

Exports a design block and a color mask to two separate Blobs.

Performs an internal update to resolve the final layout for the blocks.

##### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. |
| `maskColorR` | `number` | The red component of the special color mask color. |
| `maskColorG` | `number` | The green component of the special color mask color. |
| `maskColorB` | `number` | The blue component of the special color mask color. |
| `options?` | [`EngineExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineexportoptions/) | The options for exporting the block type |

##### Returns[#](#returns-16)

`Promise`<`Blob`\[\]>

A promise that resolves with an array of the exported image and mask or is rejected with an error.

#### Call Signature[#](#call-signature-1)

```
exportWithColorMask(   handle,   mimeType,   maskColorR,   maskColorG,   maskColorB,options?): Promise<Blob[]>;
```

Exports a design block and a color mask to two separate Blobs.

Performs an internal update to resolve the final layout for the blocks. Removes all pixels that exactly match the given RGB color and replaces them with transparency. The output includes two files: the masked image and the mask itself.

##### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. |
| `mimeType` |  | `"application/octet-stream"` |
| `maskColorR` | `number` | The red component of the special color mask color. |
| `maskColorG` | `number` | The green component of the special color mask color. |
| `maskColorB` | `number` | The blue component of the special color mask color. |
| `options?` | `Omit`<[`EngineExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/engineexportoptions/), `"mimeType"`\> | The options for exporting the block type |

##### Returns[#](#returns-17)

`Promise`<`Blob`\[\]>

A promise that resolves with an array of the exported image and mask or is rejected with an error.

##### Deprecated[#](#deprecated-1)

Use the new `exportWithColorMask` signature instead

##### Example[#](#example-5)

```
// Before migrationconst blob = await cesdk.block.exportWithColorMask(   blockId,   MimeType.Png,   0.5,   0,   0,   {     pngCompressionLevel: 5   });// After migrationconst blob = await cesdk.block.exportWithColorMask(   blockId,   0.5,   0,   0,   {     mimeType: 'image/png',     pngCompressionLevel: 5   });
```

#### Signatures[#](#signatures-1)

```
exportWithColorMask(handle: number, maskColorR: number, maskColorG: number, maskColorB: number, options?: ExportOptions): Promise<Blob[]>
```

```
exportWithColorMask(handle: number, mimeType: "application/octet-stream" | "application/pdf" | ImageMimeType, maskColorR: number, maskColorG: number, maskColorB: number, options?: Omit<ExportOptions, "mimeType">): Promise<Blob[]>
```

* * *

### exportVideo()[#](#exportvideo)

  

Exports a design block as a video file.

Note: The export will run across multiple iterations of the update loop. In each iteration a frame is scheduled for encoding.

##### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. Currently, only page blocks are supported. |
| `options?` | [`VideoExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videoexportoptions/) | The options for exporting the video, including mime type, h264 profile, level, bitrate, time offset, duration, framerate, target width and height. |

##### Returns[#](#returns-18)

`Promise`<`Blob`\>

A promise that resolves with a video blob or is rejected with an error.

##### Example[#](#example-6)

```
const page = engine.block.create('page');// Set up a progress tracking functionconst progressTracker = (renderedFrames, encodedFrames, totalFrames) => {  console.log(`Progress: ${Math.round((encodedFrames / totalFrames) * 100)}%`);};const videoOptions = { framerate: 30, duration: 5 };const videoBlob = await engine.block.exportVideo(page, MimeType.Mp4, progressTracker, videoOptions);
```

#### Call Signature[#](#call-signature-2)

```
exportVideo(   handle,   mimeType?,   progressCallback?,options?): Promise<Blob>;
```

Exports a design block as a video file.

Note: The export will run across multiple iterations of the update loop. In each iteration a frame is scheduled for encoding.

##### Parameters[#](#parameters-17)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. Currently, only page blocks are supported. |
| `mimeType?` | [`VideoMimeType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videomimetype/) | The MIME type of the output video file. |
| `progressCallback?` | (`numberOfRenderedFrames`, `numberOfEncodedFrames`, `totalNumberOfFrames`) => `void` | A callback which reports on the progress of the export. |
| `options?` | `Omit`<[`VideoExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videoexportoptions/), `"mimeType"` | `"onProgress"`\> |

##### Returns[#](#returns-19)

`Promise`<`Blob`\>

A promise that resolves with a video blob or is rejected with an error.

##### Deprecated[#](#deprecated-2)

Use the new `exportVideo` signature instead

##### Example[#](#example-7)

```
// Before migrationconst blob = await cesdk.block.exportVideo(blockId, 'video/mp4', handleProgress, {  targetWidth: 1920,  targetHeight: 1080,})// After migrationconst blob = await cesdk.block.exportVideo(blockId, {  mimeType: 'video/mp4',  progressCallback: handleProgress,  targetWidth: 1920,  targetHeight: 1080,})
```

#### Signatures[#](#signatures-2)

```
exportVideo(handle: number, options?: VideoExportOptions): Promise<Blob>
```

```
exportVideo(handle: number, mimeType?: VideoMimeType, progressCallback?: (numberOfRenderedFrames: number, numberOfEncodedFrames: number, totalNumberOfFrames: number) => void, options?: Omit<VideoExportOptions, "mimeType" | "onProgress">): Promise<Blob>
```

* * *

### exportAudio()[#](#exportaudio)

Exports a design block as an audio file.

#### Parameters[#](#parameters-18)

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `number` | The design block element to export. Currently, only audio blocks are supported. |
| `options` | [`AudioExportOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/audioexportoptions/) | The options for exporting the audio, including mime type, progress callback, and export settings. |

#### Returns[#](#returns-20)

`Promise`<`Blob`\>

A promise that resolves with an audio blob or is rejected with an error. This API is experimental and may change or be removed in future versions.

#### Example[#](#example-8)

```
const audioBlock = engine.block.create('audio');// Set up a progress tracking functionconst progressTracker = (renderedFrames, encodedFrames, totalFrames) => {  console.log(`Audio export progress: ${Math.round((encodedFrames / totalFrames) * 100)}%`);};const audioOptions = { duration: 10 };const audioBlob = await engine.block.exportAudio(audioBlock, MimeType.Wav, progressTracker, audioOptions);
```

#### Signature[#](#signature-14)

```
exportAudio(handle: number, options?: AudioExportOptions): Promise<Blob>
```

## Block Hierarchies[#](#block-hierarchies)

Manage parent-child relationships and the scene graph structure.

### getParent()[#](#getparent)

  

Gets the parent of a block.

#### Parameters[#](#parameters-19)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-21)

`number`

The parent’s handle or null if the block has no parent.

#### Signature[#](#signature-15)

```
getParent(id: number): number
```

* * *

### getChildren()[#](#getchildren)

  

Gets all direct children of a block.

Children are sorted in their rendering order: Last child is rendered in front of other children.

#### Parameters[#](#parameters-20)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-22)

`number`\[\]

A list of block ids.

#### Signature[#](#signature-16)

```
getChildren(id: number): number[]
```

* * *

### insertChild()[#](#insertchild)

  

Inserts a child block at a specific index.

#### Parameters[#](#parameters-21)

| Parameter | Type | Description |
| --- | --- | --- |
| `parent` | `number` | The block whose children should be updated. |
| `child` | `number` | The child to insert. Can be an existing child of `parent`. |
| `index` | `number` | The index to insert or move to. |

#### Returns[#](#returns-23)

`void`

#### Signature[#](#signature-17)

```
insertChild(parent: number, child: number, index: number): void
```

* * *

### appendChild()[#](#appendchild)

  

Appends a child block to a parent.

#### Parameters[#](#parameters-22)

| Parameter | Type | Description |
| --- | --- | --- |
| `parent` | `number` | The block whose children should be updated. |
| `child` | `number` | The child to insert. Can be an existing child of `parent`. |

#### Returns[#](#returns-24)

`void`

#### Signature[#](#signature-18)

```
appendChild(parent: number, child: number): void
```

## Block Layout[#](#block-layout)

Structure designs by positioning, sizing, layering, aligning, and distributing blocks.

### isTransformLocked()[#](#istransformlocked)

  

Gets the transform-locked state of a block.

If true, the block’s transform can’t be changed.

#### Parameters[#](#parameters-23)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-25)

`boolean`

True if transform locked, false otherwise.

#### Signature[#](#signature-19)

```
isTransformLocked(id: number): boolean
```

* * *

### setTransformLocked()[#](#settransformlocked)

  

Sets the transform-locked state of a block.

#### Parameters[#](#parameters-24)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `locked` | `boolean` | Whether the block’s transform should be locked. |

#### Returns[#](#returns-26)

`void`

#### Signature[#](#signature-20)

```
setTransformLocked(id: number, locked: boolean): void
```

* * *

### getPositionX()[#](#getpositionx)

  

Gets the X position of a block.

#### Parameters[#](#parameters-25)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-27)

`number`

The value of the x position.

#### Signature[#](#signature-21)

```
getPositionX(id: number): number
```

* * *

### getPositionXMode()[#](#getpositionxmode)

  

Gets the mode for the block’s X position.

#### Parameters[#](#parameters-26)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-28)

`"Absolute"` | `"Percent"` | `"Auto"`

The current mode for the x position: ‘Absolute’ or ‘Percent’.

#### Signature[#](#signature-22)

```
getPositionXMode(id: number): "Absolute" | "Percent" | "Auto"
```

* * *

### getPositionY()[#](#getpositiony)

  

Gets the Y position of a block.

#### Parameters[#](#parameters-27)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-29)

`number`

The value of the y position.

#### Signature[#](#signature-23)

```
getPositionY(id: number): number
```

* * *

### getPositionYMode()[#](#getpositionymode)

  

Gets the mode for the block’s Y position.

#### Parameters[#](#parameters-28)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-30)

`"Absolute"` | `"Percent"` | `"Auto"`

The current mode for the y position: ‘Absolute’ or ‘Percent’.

#### Signature[#](#signature-24)

```
getPositionYMode(id: number): "Absolute" | "Percent" | "Auto"
```

* * *

### setPositionX()[#](#setpositionx)

  

Sets the X position of a block.

The position refers to the block’s local space, relative to its parent with the origin at the top left.

```
engine.block.setPositionX(block, 0.25);
```

#### Parameters[#](#parameters-29)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `value` | `number` | The value of the x position. |

#### Returns[#](#returns-31)

`void`

#### Signature[#](#signature-25)

```
setPositionX(id: number, value: number): void
```

* * *

### setPositionXMode()[#](#setpositionxmode)

  

Sets the mode for the block’s X position.

```
engine.block.setPositionXMode(block, 'Percent');
```

#### Parameters[#](#parameters-30)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `mode` | `"Absolute"` | `"Percent"` |

#### Returns[#](#returns-32)

`void`

#### Signature[#](#signature-26)

```
setPositionXMode(id: number, mode: "Absolute" | "Percent" | "Auto"): void
```

* * *

### setPositionY()[#](#setpositiony)

  

Sets the Y position of a block.

The position refers to the block’s local space, relative to its parent with the origin at the top left.

```
engine.block.setPositionY(block, 0.25);
```

#### Parameters[#](#parameters-31)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `value` | `number` | The value of the y position. |

#### Returns[#](#returns-33)

`void`

#### Signature[#](#signature-27)

```
setPositionY(id: number, value: number): void
```

* * *

### setPositionYMode()[#](#setpositionymode)

  

Sets the mode for the block’s Y position.

```
engine.block.setPositionYMode(block, 'Absolute');
```

#### Parameters[#](#parameters-32)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `mode` | `"Absolute"` | `"Percent"` |

#### Returns[#](#returns-34)

`void`

#### Signature[#](#signature-28)

```
setPositionYMode(id: number, mode: "Absolute" | "Percent" | "Auto"): void
```

* * *

### setAlwaysOnTop()[#](#setalwaysontop)

  

Sets a block to always be rendered on top of its siblings.

If true, this block’s sorting order is automatically adjusted to be higher than all other siblings without this property.

#### Parameters[#](#parameters-33)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | the block to update. |
| `enabled` | `boolean` | whether the block shall be always-on-top. |

#### Returns[#](#returns-35)

`void`

#### Signature[#](#signature-29)

```
setAlwaysOnTop(id: number, enabled: boolean): void
```

* * *

### setAlwaysOnBottom()[#](#setalwaysonbottom)

  

Sets a block to always be rendered below its siblings.

If true, this block’s sorting order is automatically adjusted to be lower than all other siblings without this property.

#### Parameters[#](#parameters-34)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | the block to update. |
| `enabled` | `boolean` | whether the block shall always be below its siblings. |

#### Returns[#](#returns-36)

`void`

#### Signature[#](#signature-30)

```
setAlwaysOnBottom(id: number, enabled: boolean): void
```

* * *

### isAlwaysOnTop()[#](#isalwaysontop)

  

Checks if a block is set to always be on top.

#### Parameters[#](#parameters-35)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | the block to query. |

#### Returns[#](#returns-37)

`boolean`

true if the block is set to be always-on-top, false otherwise.

#### Signature[#](#signature-31)

```
isAlwaysOnTop(id: number): boolean
```

* * *

### isAlwaysOnBottom()[#](#isalwaysonbottom)

  

Checks if a block is set to always be on the bottom.

#### Parameters[#](#parameters-36)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | the block to query. |

#### Returns[#](#returns-38)

`boolean`

true if the block is set to be always-on-bottom, false otherwise.

#### Signature[#](#signature-32)

```
isAlwaysOnBottom(id: number): boolean
```

* * *

### bringToFront()[#](#bringtofront)

  

Brings a block to the front of its siblings.

Updates the sorting order so that the given block has the highest sorting order.

#### Parameters[#](#parameters-37)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The id of the block to bring to the front. |

#### Returns[#](#returns-39)

`void`

#### Signature[#](#signature-33)

```
bringToFront(id: number): void
```

* * *

### sendToBack()[#](#sendtoback)

  

Sends a block to the back of its siblings.

Updates the sorting order so that the given block has the lowest sorting order.

#### Parameters[#](#parameters-38)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The id of the block to send to the back. |

#### Returns[#](#returns-40)

`void`

#### Signature[#](#signature-34)

```
sendToBack(id: number): void
```

* * *

### bringForward()[#](#bringforward)

  

Brings a block one layer forward.

Updates the sorting order to be higher than its next sibling.

#### Parameters[#](#parameters-39)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The id of the block to bring forward. |

#### Returns[#](#returns-41)

`void`

#### Signature[#](#signature-35)

```
bringForward(id: number): void
```

* * *

### sendBackward()[#](#sendbackward)

  

Sends a block one layer backward.

Updates the sorting order to be lower than its previous sibling.

#### Parameters[#](#parameters-40)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The id of the block to send backward. |

#### Returns[#](#returns-42)

`void`

#### Signature[#](#signature-36)

```
sendBackward(id: number): void
```

* * *

### getRotation()[#](#getrotation)

  

Gets the rotation of a block in radians.

#### Parameters[#](#parameters-41)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-43)

`number`

The block’s rotation around its center in radians.

#### Signature[#](#signature-37)

```
getRotation(id: number): number
```

* * *

### setRotation()[#](#setrotation)

  

Sets the rotation of a block in radians.

Rotation is applied around the block’s center.

#### Parameters[#](#parameters-42)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `radians` | `number` | The new rotation in radians. |

#### Returns[#](#returns-44)

`void`

#### Signature[#](#signature-38)

```
setRotation(id: number, radians: number): void
```

* * *

### getWidth()[#](#getwidth)

  

Gets the width of a block in the current width mode.

```
const width = engine.block.getWidth(block);
```

#### Parameters[#](#parameters-43)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-45)

`number`

The value of the block’s width.

#### Signature[#](#signature-39)

```
getWidth(id: number): number
```

* * *

### getWidthMode()[#](#getwidthmode)

  

Gets the mode for the block’s width.

```
const widthMode = engine.block.getWidthMode(block);
```

#### Parameters[#](#parameters-44)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-46)

`"Absolute"` | `"Percent"` | `"Auto"`

The current mode for the width: ‘Absolute’, ‘Percent’ or ‘Auto’.

#### Signature[#](#signature-40)

```
getWidthMode(id: number): "Absolute" | "Percent" | "Auto"
```

* * *

### getHeight()[#](#getheight)

  

Gets the height of a block in the current height mode.

```
const height = engine.block.getHeight(block);
```

#### Parameters[#](#parameters-45)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-47)

`number`

The value of the block’s height.

#### Signature[#](#signature-41)

```
getHeight(id: number): number
```

* * *

### getHeightMode()[#](#getheightmode)

  

Gets the mode for the block’s height.

```
const heightMode = engine.block.getHeightMode(block);
```

#### Parameters[#](#parameters-46)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-48)

`"Absolute"` | `"Percent"` | `"Auto"`

The current mode for the height: ‘Absolute’, ‘Percent’ or ‘Auto’.

#### Signature[#](#signature-42)

```
getHeightMode(id: number): "Absolute" | "Percent" | "Auto"
```

* * *

### setWidth()[#](#setwidth)

  

Sets the width of a block in the current width mode.

If the crop is maintained, the crop values will be automatically adjusted.

```
engine.block.setWidth(block, 2.5, true);
```

#### Parameters[#](#parameters-47)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `value` | `number` | The new width of the block. |
| `maintainCrop?` | `boolean` | Whether or not the crop values, if available, should be automatically adjusted. |

#### Returns[#](#returns-49)

`void`

#### Signature[#](#signature-43)

```
setWidth(id: number, value: number, maintainCrop?: boolean): void
```

* * *

### setWidthMode()[#](#setwidthmode)

  

Sets the mode for the block’s width.

```
engine.block.setWidthMode(block, 'Percent');
```

#### Parameters[#](#parameters-48)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `mode` | `"Absolute"` | `"Percent"` |

#### Returns[#](#returns-50)

`void`

#### Signature[#](#signature-44)

```
setWidthMode(id: number, mode: "Absolute" | "Percent" | "Auto"): void
```

* * *

### setHeight()[#](#setheight)

  

Sets the height of a block in the current height mode.

If the crop is maintained, the crop values will be automatically adjusted.

```
engine.block.setHeight(block, 0.5);engine.block.setHeight(block, 2.5, true);
```

#### Parameters[#](#parameters-49)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `value` | `number` | The new height of the block. |
| `maintainCrop?` | `boolean` | Whether or not the crop values, if available, should be automatically adjusted. |

#### Returns[#](#returns-51)

`void`

#### Signature[#](#signature-45)

```
setHeight(id: number, value: number, maintainCrop?: boolean): void
```

* * *

### setHeightMode()[#](#setheightmode)

  

Sets the mode for the block’s height.

```
engine.block.setHeightMode(block, 'Percent');
```

#### Parameters[#](#parameters-50)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `mode` | `"Absolute"` | `"Percent"` |

#### Returns[#](#returns-52)

`void`

#### Signature[#](#signature-46)

```
setHeightMode(id: number, mode: "Absolute" | "Percent" | "Auto"): void
```

* * *

### getFrameX()[#](#getframex)

  

Gets the final calculated X position of a block’s frame.

The position is only available after an internal update loop.

```
const frameX = engine.block.getFrameX(block);
```

#### Parameters[#](#parameters-51)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-53)

`number`

The layout position on the x-axis.

#### Signature[#](#signature-47)

```
getFrameX(id: number): number
```

* * *

### getFrameY()[#](#getframey)

  

Gets the final calculated Y position of a block’s frame.

The position is only available after an internal update loop.

```
const frameY = engine.block.getFrameY(block);
```

#### Parameters[#](#parameters-52)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-54)

`number`

The layout position on the y-axis.

#### Signature[#](#signature-48)

```
getFrameY(id: number): number
```

* * *

### getFrameWidth()[#](#getframewidth)

  

Gets the final calculated width of a block’s frame.

The width is only available after an internal update loop.

```
const frameWidth = engine.block.getFrameWidth(block);
```

#### Parameters[#](#parameters-53)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-55)

`number`

The layout width.

#### Signature[#](#signature-49)

```
getFrameWidth(id: number): number
```

* * *

### getFrameHeight()[#](#getframeheight)

  

Gets the final calculated height of a block’s frame.

The height is only available after an internal update loop.

```
const frameHeight = engine.block.getFrameHeight(block);
```

#### Parameters[#](#parameters-54)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-56)

`number`

The layout height.

#### Signature[#](#signature-50)

```
getFrameHeight(id: number): number
```

* * *

### getGlobalBoundingBoxX()[#](#getglobalboundingboxx)

  

Gets the X position of the block’s global bounding box.

The position is in the scene’s global coordinate space, with the origin at the top left.

```
const globalX = engine.block.getGlobalBoundingBoxX(block);
```

#### Parameters[#](#parameters-55)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose bounding box should be calculated. |

#### Returns[#](#returns-57)

`number`

The x coordinate of the axis-aligned bounding box.

#### Signature[#](#signature-51)

```
getGlobalBoundingBoxX(id: number): number
```

* * *

### getGlobalBoundingBoxY()[#](#getglobalboundingboxy)

  

Gets the Y position of the block’s global bounding box.

The position is in the scene’s global coordinate space, with the origin at the top left.

```
const globalY = engine.block.getGlobalBoundingBoxY(block);
```

#### Parameters[#](#parameters-56)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose bounding box should be calculated. |

#### Returns[#](#returns-58)

`number`

The y coordinate of the axis-aligned bounding box.

#### Signature[#](#signature-52)

```
getGlobalBoundingBoxY(id: number): number
```

* * *

### getGlobalBoundingBoxWidth()[#](#getglobalboundingboxwidth)

  

Gets the width of the block’s global bounding box.

The width is in the scene’s global coordinate space.

```
const globalWidth = engine.block.getGlobalBoundingBoxWidth(block);
```

#### Parameters[#](#parameters-57)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose bounding box should be calculated. |

#### Returns[#](#returns-59)

`number`

The width of the axis-aligned bounding box.

#### Signature[#](#signature-53)

```
getGlobalBoundingBoxWidth(id: number): number
```

* * *

### getGlobalBoundingBoxHeight()[#](#getglobalboundingboxheight)

  

Gets the height of the block’s global bounding box.

The height is in the scene’s global coordinate space.

```
const globalHeight = engine.block.getGlobalBoundingBoxHeight(block);
```

#### Parameters[#](#parameters-58)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose bounding box should be calculated. |

#### Returns[#](#returns-60)

`number`

The height of the axis-aligned bounding box.

#### Signature[#](#signature-54)

```
getGlobalBoundingBoxHeight(id: number): number
```

* * *

### getScreenSpaceBoundingBoxXYWH()[#](#getscreenspaceboundingboxxywh)

  

Gets the screen-space bounding box for a set of blocks.

```
const boundingBox = engine.block.getScreenSpaceBoundingBoxXYWH([block]);
```

#### Parameters[#](#parameters-59)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The block to query. |

#### Returns[#](#returns-61)

[`XYWH`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/xywh/)

The position and size of the bounding box.

#### Signature[#](#signature-55)

```
getScreenSpaceBoundingBoxXYWH(ids: number[]): XYWH
```

* * *

### alignHorizontally()[#](#alignhorizontally)

  

Aligns blocks horizontally.

Aligns multiple blocks within their bounding box or a single block to its parent.

#### Parameters[#](#parameters-60)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A non-empty array of block ids. |
| `horizontalBlockAlignment` | `"Left"` | `"Right"` |

#### Returns[#](#returns-62)

`void`

#### Signature[#](#signature-56)

```
alignHorizontally(ids: number[], horizontalBlockAlignment: "Left" | "Right" | "Center"): void
```

* * *

### alignVertically()[#](#alignvertically)

  

Aligns blocks vertically.

Aligns multiple blocks within their bounding box or a single block to its parent.

#### Parameters[#](#parameters-61)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A non-empty array of block ids. |
| `verticalBlockAlignment` | `"Center"` | `"Top"` |

#### Returns[#](#returns-63)

`void`

#### Signature[#](#signature-57)

```
alignVertically(ids: number[], verticalBlockAlignment: "Center" | "Top" | "Bottom"): void
```

* * *

### distributeHorizontally()[#](#distributehorizontally)

  

Distributes blocks horizontally with even spacing.

Distributes multiple blocks horizontally within their bounding box.

#### Parameters[#](#parameters-62)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A non-empty array of block ids. |

#### Returns[#](#returns-64)

`void`

#### Signature[#](#signature-58)

```
distributeHorizontally(ids: number[]): void
```

* * *

### distributeVertically()[#](#distributevertically)

  

Distributes blocks vertically with even spacing.

Distributes multiple blocks vertically within their bounding box.

#### Parameters[#](#parameters-63)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A non-empty array of block ids. |

#### Returns[#](#returns-65)

`void`

#### Signature[#](#signature-59)

```
distributeVertically(ids: number[]): void
```

* * *

### fillParent()[#](#fillparent)

  

Resizes and positions a block to fill its parent.

The crop values of the block are reset if it can be cropped.

#### Parameters[#](#parameters-64)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block that should fill its parent. |

#### Returns[#](#returns-66)

`void`

#### Signature[#](#signature-60)

```
fillParent(id: number): void
```

* * *

### resizeContentAware()[#](#resizecontentaware)

  

Resizes blocks while adjusting content to fit.

The content of the blocks is automatically adjusted to fit the new dimensions. Full-page blocks are resized to remain as full-page afterwards, while the blocks that are not full-page get resized as a group to the same scale factor and centered.

```
const pages = engine.scene.getPages();engine.block.resizeContentAware(pages, width: 100.0, 100.0);
```

#### Parameters[#](#parameters-65)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The blocks to resize. |
| `width` | `number` | The new width of the blocks. |
| `height` | `number` | The new height of the blocks. |

#### Returns[#](#returns-67)

`void`

#### Signature[#](#signature-61)

```
resizeContentAware(ids: number[], width: number, height: number): void
```

* * *

### scale()[#](#scale)

  

Scales a block and its children proportionally.

This updates the position, size and style properties (e.g. stroke width) of the block and its children around the specified anchor point.

```
// Scale a block to double its size, anchored at the center.engine.block.scale(block, 2.0, 0.5, 0.5);
```

#### Parameters[#](#parameters-66)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block that should be scaled. |
| `scale` | `number` | `undefined` | The scale factor to be applied to the current properties of the block. |
| `anchorX` | `number` | `0` | The relative position along the width of the block around which the scaling should occur (0=left, 0.5=center, 1=right). Defaults to 0. |
| `anchorY` | `number` | `0` | The relative position along the height of the block around which the scaling should occur (0=top, 0.5=center, 1=bottom). Defaults to 0. |

#### Returns[#](#returns-68)

`void`

#### Signature[#](#signature-62)

```
scale(id: number, scale: number, anchorX?: number, anchorY?: number): void
```

## Block Selection & Visibility[#](#block-selection--visibility)

Manage a block’s selection state and visibility on the canvas.

### select()[#](#select)

  

Selects a block, deselecting all others.

#### Parameters[#](#parameters-67)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to be selected. |

#### Returns[#](#returns-69)

`void`

#### Signature[#](#signature-63)

```
select(id: number): void
```

* * *

### setSelected()[#](#setselected)

  

Sets the selection state of a block.

#### Parameters[#](#parameters-68)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |
| `selected` | `boolean` | Whether or not the block should be selected. |

#### Returns[#](#returns-70)

`void`

#### Signature[#](#signature-64)

```
setSelected(id: number, selected: boolean): void
```

* * *

### isSelected()[#](#isselected)

  

Gets the selection state of a block.

#### Parameters[#](#parameters-69)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-71)

`boolean`

True if the block is selected, false otherwise.

#### Signature[#](#signature-65)

```
isSelected(id: number): boolean
```

* * *

### findAllSelected()[#](#findallselected)

  

Finds all currently selected blocks.

#### Returns[#](#returns-72)

`number`\[\]

An array of block ids.

#### Signature[#](#signature-66)

```
findAllSelected(): number[]
```

* * *

### isVisible()[#](#isvisible)

  

Gets the visibility state of a block.

#### Parameters[#](#parameters-70)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-73)

`boolean`

True if visible, false otherwise.

#### Signature[#](#signature-67)

```
isVisible(id: number): boolean
```

* * *

### setVisible()[#](#setvisible)

  

Sets the visibility state of a block.

#### Parameters[#](#parameters-71)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `visible` | `boolean` | Whether the block shall be visible. |

#### Returns[#](#returns-74)

`void`

#### Signature[#](#signature-68)

```
setVisible(id: number, visible: boolean): void
```

## Block Appearance[#](#block-appearance)

Control general appearance, including opacity, blend modes, flipping, and other visual properties.

### isClipped()[#](#isclipped)

  

Gets the clipped state of a block.

If true, the block should clip its contents to its frame.

#### Parameters[#](#parameters-72)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-75)

`boolean`

True if clipped, false otherwise.

#### Signature[#](#signature-69)

```
isClipped(id: number): boolean
```

* * *

### setClipped()[#](#setclipped)

  

Sets the clipped state of a block.

#### Parameters[#](#parameters-73)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `clipped` | `boolean` | Whether the block should clips its contents to its frame. |

#### Returns[#](#returns-76)

`void`

#### Signature[#](#signature-70)

```
setClipped(id: number, clipped: boolean): void
```

* * *

### getFlipHorizontal()[#](#getfliphorizontal)

  

Gets the horizontal flip state of a block.

#### Parameters[#](#parameters-74)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-77)

`boolean`

A boolean indicating whether the block is flipped horizontally.

#### Signature[#](#signature-71)

```
getFlipHorizontal(id: number): boolean
```

* * *

### getFlipVertical()[#](#getflipvertical)

  

Gets the vertical flip state of a block.

#### Parameters[#](#parameters-75)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-78)

`boolean`

A boolean indicating whether the block is flipped vertically.

#### Signature[#](#signature-72)

```
getFlipVertical(id: number): boolean
```

* * *

### setFlipHorizontal()[#](#setfliphorizontal)

  

Sets the horizontal flip state of a block.

#### Parameters[#](#parameters-76)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `flip` | `boolean` | If the flip should be enabled. |

#### Returns[#](#returns-79)

`void`

#### Signature[#](#signature-73)

```
setFlipHorizontal(id: number, flip: boolean): void
```

* * *

### setFlipVertical()[#](#setflipvertical)

  

Sets the vertical flip state of a block.

#### Parameters[#](#parameters-77)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `flip` | `boolean` | If the flip should be enabled. |

#### Returns[#](#returns-80)

`void`

#### Signature[#](#signature-74)

```
setFlipVertical(id: number, flip: boolean): void
```

* * *

### ~hasOpacity()~[#](#hasopacity)

  

Checks if a block has an opacity property.

#### Parameters[#](#parameters-78)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-81)

`boolean`

true, if the block has an opacity.

#### Deprecated[#](#deprecated-3)

Use supportsOpacity() instead.

* * *

### supportsOpacity()[#](#supportsopacity)

  

Checks if a block supports opacity.

#### Parameters[#](#parameters-79)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-82)

`boolean`

true, if the block supports opacity.

#### Signature[#](#signature-75)

```
supportsOpacity(id: number): boolean
```

* * *

### setOpacity()[#](#setopacity)

  

Sets the opacity of a block.

#### Parameters[#](#parameters-80)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose opacity should be set. |
| `opacity` | `number` | The opacity to be set. The valid range is 0 to 1. |

#### Returns[#](#returns-83)

`void`

#### Signature[#](#signature-76)

```
setOpacity(id: number, opacity: number): void
```

* * *

### getOpacity()[#](#getopacity)

  

Gets the opacity of a block.

#### Parameters[#](#parameters-81)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose opacity should be queried. |

#### Returns[#](#returns-84)

`number`

The opacity value.

#### Signature[#](#signature-77)

```
getOpacity(id: number): number
```

* * *

### ~hasBlendMode()~[#](#hasblendmode)

  

Checks if a block has a blend mode property.

#### Parameters[#](#parameters-82)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-85)

`boolean`

true, if the block has a blend mode.

#### Deprecated[#](#deprecated-4)

Use supportsBlendMode() instead.

* * *

### supportsBlendMode()[#](#supportsblendmode)

  

Checks if a block supports blend modes.

#### Parameters[#](#parameters-83)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-86)

`boolean`

true, if the block supports blend modes.

#### Signature[#](#signature-78)

```
supportsBlendMode(id: number): boolean
```

* * *

### setBlendMode()[#](#setblendmode)

  

Sets the blend mode of a block.

#### Parameters[#](#parameters-84)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose blend mode should be set. |
| `blendMode` |  | `"Color"` |

#### Returns[#](#returns-87)

`void`

#### Signature[#](#signature-79)

```
setBlendMode(id: number, blendMode: "Color" | "Difference" | "PassThrough" | "Normal" | "Darken" | "Multiply" | "ColorBurn" | "LinearBurn" | "DarkenColor" | "Lighten" | "Screen" | "ColorDodge" | "LinearDodge" | "LightenColor" | "Overlay" | "SoftLight" | "HardLight" | "VividLight" | "LinearLight" | "PinLight" | "HardMix" | "Exclusion" | "Subtract" | "Divide" | "Hue" | "Saturation" | "Luminosity"): void
```

* * *

### getBlendMode()[#](#getblendmode)

  

Gets the blend mode of a block.

#### Parameters[#](#parameters-85)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose blend mode should be queried. |

#### Returns[#](#returns-88)

| `"Color"` | `"Difference"` | `"PassThrough"` | `"Normal"` | `"Darken"` | `"Multiply"` | `"ColorBurn"` | `"LinearBurn"` | `"DarkenColor"` | `"Lighten"` | `"Screen"` | `"ColorDodge"` | `"LinearDodge"` | `"LightenColor"` | `"Overlay"` | `"SoftLight"` | `"HardLight"` | `"VividLight"` | `"LinearLight"` | `"PinLight"` | `"HardMix"` | `"Exclusion"` | `"Subtract"` | `"Divide"` | `"Hue"` | `"Saturation"` | `"Luminosity"`

The blend mode.

#### Signature[#](#signature-80)

```
getBlendMode(id: number): "Color" | "Difference" | "PassThrough" | "Normal" | "Darken" | "Multiply" | "ColorBurn" | "LinearBurn" | "DarkenColor" | "Lighten" | "Screen" | "ColorDodge" | "LinearDodge" | "LightenColor" | "Overlay" | "SoftLight" | "HardLight" | "VividLight" | "LinearLight" | "PinLight" | "HardMix" | "Exclusion" | "Subtract" | "Divide" | "Hue" | "Saturation" | "Luminosity"
```

* * *

### ~hasBackgroundColor()~[#](#hasbackgroundcolor)

  

Checks if a block has background color properties.

#### Parameters[#](#parameters-86)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-89)

`boolean`

true, if the block has background color properties.

#### Deprecated[#](#deprecated-5)

Use supportsBackgroundColor() instead.

* * *

### supportsBackgroundColor()[#](#supportsbackgroundcolor)

  

Checks if a block supports a background color.

#### Parameters[#](#parameters-87)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-90)

`boolean`

true, if the block supports a background color.

#### Signature[#](#signature-81)

```
supportsBackgroundColor(id: number): boolean
```

* * *

### ~setBackgroundColorRGBA()~[#](#setbackgroundcolorrgba)

  

Sets the background color of a block using RGBA values.

#### Parameters[#](#parameters-88)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose background color should be set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. |

#### Returns[#](#returns-91)

`void`

#### Deprecated[#](#deprecated-6)

Use `Use setColor() with the key path 'backgroundColor/color' instead.`.

* * *

### ~getBackgroundColorRGBA()~[#](#getbackgroundcolorrgba)

  

Gets the background color of a block as RGBA values.

#### Parameters[#](#parameters-89)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose background color should be queried. |

#### Returns[#](#returns-92)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

The background color.

#### Deprecated[#](#deprecated-7)

Use `Use getColor() with the key path 'backgroundColor/color' instead.`.

* * *

### setBackgroundColorEnabled()[#](#setbackgroundcolorenabled)

  

Enables or disables the background of a block.

```
engine.block.setBackgroundColorEnabled(block, true);
```

#### Parameters[#](#parameters-90)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose background should be enabled or disabled. |
| `enabled` | `boolean` | If true, the background will be enabled. |

#### Returns[#](#returns-93)

`void`

#### Signature[#](#signature-82)

```
setBackgroundColorEnabled(id: number, enabled: boolean): void
```

* * *

### isBackgroundColorEnabled()[#](#isbackgroundcolorenabled)

  

Checks if the background of a block is enabled.

```
const backgroundColorIsEnabled = engine.block.isBackgroundColorEnabled(block);
```

#### Parameters[#](#parameters-91)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose background state should be queried. |

#### Returns[#](#returns-94)

`boolean`

True, if background is enabled.

#### Signature[#](#signature-83)

```
isBackgroundColorEnabled(id: number): boolean
```

## Block Fills[#](#block-fills)

Create, configure, and manage block fills, including solid colors, gradients, and images.

### createFill()[#](#createfill)

  

Creates a new fill block.

```
const solidColoFill = engine.block.createFill('color');// Longhand fill types are also supportedconst imageFill = engine.block.createFill('//ly.img.ubq/fill/image');
```

#### Parameters[#](#parameters-92)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`FillType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/filltype/) | The type of the fill object that shall be created. |

#### Returns[#](#returns-95)

`number`

The created fill’s handle.

#### Signature[#](#signature-84)

```
createFill(type: FillType): number
```

* * *

### ~hasContentFillMode()~[#](#hascontentfillmode)

  

Checks if a block supports content fill modes.

#### Parameters[#](#parameters-93)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-96)

`boolean`

true, if the block has a content fill mode.

#### Deprecated[#](#deprecated-8)

Use supportsContentFillMode instead.

* * *

### supportsContentFillMode()[#](#supportscontentfillmode)

  

Checks if a block supports content fill modes.

#### Parameters[#](#parameters-94)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-97)

`boolean`

true, if the block has a content fill mode.

#### Signature[#](#signature-85)

```
supportsContentFillMode(id: number): boolean
```

* * *

### setContentFillMode()[#](#setcontentfillmode)

  

Sets the content fill mode of a block.

```
engine.block.setContentFillMode(image, 'Cover');
```

#### Parameters[#](#parameters-95)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `mode` | `"Crop"` | `"Cover"` |

#### Returns[#](#returns-98)

`void`

#### Signature[#](#signature-86)

```
setContentFillMode(id: number, mode: "Crop" | "Cover" | "Contain"): void
```

* * *

### getContentFillMode()[#](#getcontentfillmode)

  

Gets the content fill mode of a block.

```
engine.block.getContentFillMode(image);
```

#### Parameters[#](#parameters-96)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-99)

`"Crop"` | `"Cover"` | `"Contain"`

The current mode: ‘Crop’, ‘Cover’ or ‘Contain’.

#### Signature[#](#signature-87)

```
getContentFillMode(id: number): "Crop" | "Cover" | "Contain"
```

* * *

### setGradientColorStops()[#](#setgradientcolorstops)

  

Sets the color stops for a gradient property.

```
engine.block.setGradientColorStops(gradientFill, 'fill/gradient/colors', [  { color: { r: 1.0, g: 0.8, b: 0.2, a: 1.0 }, stop: 0 },  { color: { r: 0.3, g: 0.4, b: 0.7, a: 1.0 }, stop: 1 }]);
```

#### Parameters[#](#parameters-97)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `string` | The name of the property to set, e.g. ‘fill/gradient/colors’. |
| `colors` | [`GradientColorStop`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/gradientcolorstop/)\[\] | An array of gradient color stops. |

#### Returns[#](#returns-100)

`void`

#### Signature[#](#signature-88)

```
setGradientColorStops(id: number, property: string, colors: GradientColorStop[]): void
```

* * *

### getGradientColorStops()[#](#getgradientcolorstops)

  

Gets the color stops from a gradient property.

```
engine.block.getGradientColorStops(gradientFill, 'fill/gradient/colors');
```

#### Parameters[#](#parameters-98)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `string` | The name of the property to query. |

#### Returns[#](#returns-101)

[`GradientColorStop`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/gradientcolorstop/)\[\]

The gradient colors.

#### Signature[#](#signature-89)

```
getGradientColorStops(id: number, property: string): GradientColorStop[]
```

* * *

### getSourceSet()[#](#getsourceset)

  

Gets the source set from a block property.

```
const sourceSet = engine.block.getSourceSet(imageFill, 'fill/image/sourceSet');
```

#### Parameters[#](#parameters-99)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block that should be queried. |
| `property` | `SourceSetPropertyName` | The name of the property to query, e.g. ‘fill/image/sourceSet’. |

#### Returns[#](#returns-102)

[`Source`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/source/)\[\]

The block’s source set.

#### Signature[#](#signature-90)

```
getSourceSet(id: number, property: SourceSetPropertyName): Source[]
```

* * *

### setSourceSet()[#](#setsourceset)

  

Sets the source set for a block property.

The crop and content fill mode of the associated block will be reset to default values.

```
engine.block.setSourceSet(imageFill, 'fill/image/sourceSet', [{  uri: 'https://example.com/sample.jpg',  width: 800,  height: 600}]);
```

#### Parameters[#](#parameters-100)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `SourceSetPropertyName` | The name of the property to set. |
| `sourceSet` | [`Source`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/source/)\[\] | The block’s new source set. |

#### Returns[#](#returns-103)

`void`

#### Signature[#](#signature-91)

```
setSourceSet(id: number, property: SourceSetPropertyName, sourceSet: Source[]): void
```

* * *

### addImageFileURIToSourceSet()[#](#addimagefileuritosourceset)

  

Adds an image file URI to a source set property.

If an image with the same width already exists in the source set, it will be replaced.

```
await engine.block.addImageFileURIToSourceSet(imageFill, 'fill/image/sourceSet', 'https://example.com/sample.jpg');
```

#### Parameters[#](#parameters-101)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `property` | `SourceSetPropertyName` | The name of the property to modify. |
| `uri` | `string` | The source to add to the source set. |

#### Returns[#](#returns-104)

`Promise`<`void`\>

A promise that resolves when the operation is complete.

#### Signature[#](#signature-92)

```
addImageFileURIToSourceSet(id: number, property: SourceSetPropertyName, uri: string): Promise<void>
```

* * *

### addVideoFileURIToSourceSet()[#](#addvideofileuritosourceset)

  

Adds a video file URI to a source set property.

If a video with the same width already exists in the source set, it will be replaced.

```
await engine.block.addVideoFileURIToSourceSet(videoFill, 'fill/video/sourceSet', 'https://example.com/sample.mp4');
```

#### Parameters[#](#parameters-102)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `property` | `SourceSetPropertyName` | The name of the property to modify. |
| `uri` | `string` | The source to add to the source set. |

#### Returns[#](#returns-105)

`Promise`<`void`\>

A promise that resolves when the operation is complete.

#### Signature[#](#signature-93)

```
addVideoFileURIToSourceSet(id: number, property: SourceSetPropertyName, uri: string): Promise<void>
```

* * *

### ~hasFillColor()~[#](#hasfillcolor)

  

Checks if a block has fill color properties.

#### Parameters[#](#parameters-103)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-106)

`boolean`

true, if the block has fill color properties.

#### Deprecated[#](#deprecated-9)

Query the fill’s type using getFill() and getType() instead.

* * *

### ~setFillColorRGBA()~[#](#setfillcolorrgba)

  

Sets the fill color of a block using RGBA values.

#### Parameters[#](#parameters-104)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose fill color should be set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. |

#### Returns[#](#returns-107)

`void`

#### Deprecated[#](#deprecated-10)

Use setFillSolidColor() instead.

* * *

### ~getFillColorRGBA()~[#](#getfillcolorrgba)

  

Gets the fill color of a block as RGBA values.

#### Parameters[#](#parameters-105)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill color should be queried. |

#### Returns[#](#returns-108)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

The fill color.

#### Deprecated[#](#deprecated-11)

Use getFillSolidColor() instead.

* * *

### ~setFillColorEnabled()~[#](#setfillcolorenabled)

  

Enables or disables the fill of a block.

#### Parameters[#](#parameters-106)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill should be enabled or disabled. |
| `enabled` | `boolean` | If true, the fill will be enabled. |

#### Returns[#](#returns-109)

`void`

#### Deprecated[#](#deprecated-12)

Use setFillEnabled() instead.

* * *

### ~isFillColorEnabled()~[#](#isfillcolorenabled)

  

Checks if the fill of a block is enabled.

#### Parameters[#](#parameters-107)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill state should be queried. |

#### Returns[#](#returns-110)

`boolean`

True, if fill is enabled.

#### Deprecated[#](#deprecated-13)

Use isFillEnabled() instead.

* * *

### ~hasFill()~[#](#hasfill)

  

Checks if a block has fill properties.

#### Parameters[#](#parameters-108)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-111)

`boolean`

true, if the block has fill properties.

#### Deprecated[#](#deprecated-14)

Use supportsFill instead.

* * *

### supportsFill()[#](#supportsfill)

  

Checks if a block supports a fill.

#### Parameters[#](#parameters-109)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-112)

`boolean`

true, if the block supports a fill.

#### Signature[#](#signature-94)

```
supportsFill(id: number): boolean
```

* * *

### isFillEnabled()[#](#isfillenabled)

  

Checks if the fill of a block is enabled.

```
engine.block.isFillEnabled(block);
```

#### Parameters[#](#parameters-110)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill state should be queried. |

#### Returns[#](#returns-113)

`boolean`

The fill state.

#### Signature[#](#signature-95)

```
isFillEnabled(id: number): boolean
```

* * *

### setFillEnabled()[#](#setfillenabled)

  

Enables or disables the fill of a block.

```
engine.block.setFillEnabled(block, false);
```

#### Parameters[#](#parameters-111)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill should be enabled or disabled. |
| `enabled` | `boolean` | If true, the fill will be enabled. |

#### Returns[#](#returns-114)

`void`

#### Signature[#](#signature-96)

```
setFillEnabled(id: number, enabled: boolean): void
```

* * *

### getFill()[#](#getfill)

  

Gets the fill block attached to a given block.

#### Parameters[#](#parameters-112)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill block should be returned. |

#### Returns[#](#returns-115)

`number`

The block that currently defines the given block’s fill.

#### Signature[#](#signature-97)

```
getFill(id: number): number
```

* * *

### setFill()[#](#setfill)

  

Sets the fill block for a given block.

The previous fill block is not destroyed automatically.

#### Parameters[#](#parameters-113)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill should be changed. |
| `fill` | `number` | The new fill block. |

#### Returns[#](#returns-116)

`void`

#### Signature[#](#signature-98)

```
setFill(id: number, fill: number): void
```

* * *

### setFillSolidColor()[#](#setfillsolidcolor)

  

Sets the solid fill color of a block.

#### Parameters[#](#parameters-114)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose fill color should be set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. Defaults to 1. |

#### Returns[#](#returns-117)

`void`

#### Signature[#](#signature-99)

```
setFillSolidColor(id: number, r: number, g: number, b: number, a?: number): void
```

* * *

### getFillSolidColor()[#](#getfillsolidcolor)

  

Gets the solid fill color of a block as RGBA values.

#### Parameters[#](#parameters-115)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose fill color should be queried. |

#### Returns[#](#returns-118)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

The fill color.

#### Signature[#](#signature-100)

```
getFillSolidColor(id: number): RGBA
```

## Block Shapes[#](#block-shapes)

Create and configure shape blocks and geometric forms.

### createShape()[#](#createshape)

  

Creates a new shape block of a given type.

```
const star = engine.block.createShape('star');// Longhand shape types are also supportedconst rect = engine.block.createShape('//ly.img.ubq/shape/rect');
```

#### Parameters[#](#parameters-116)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`ShapeType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/shapetype/) | The type of the shape object that shall be created. |

#### Returns[#](#returns-119)

`number`

The created shape’s handle.

#### Signature[#](#signature-101)

```
createShape(type: ShapeType): number
```

* * *

### ~hasShape()~[#](#hasshape)

  

Checks if a block has a shape property.

#### Parameters[#](#parameters-117)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-120)

`boolean`

true, if the block has a shape property, an error otherwise.

#### Deprecated[#](#deprecated-15)

Use supportsShape instead.

* * *

### supportsShape()[#](#supportsshape)

  

Checks if a block supports having a shape.

#### Parameters[#](#parameters-118)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-121)

`boolean`

true, if the block has a shape property, an error otherwise.

#### Signature[#](#signature-102)

```
supportsShape(id: number): boolean
```

* * *

### getShape()[#](#getshape)

  

Gets the shape block attached to a given block.

#### Parameters[#](#parameters-119)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose shape block should be returned. |

#### Returns[#](#returns-122)

`number`

The block that currently defines the given block’s shape.

#### Signature[#](#signature-103)

```
getShape(id: number): number
```

* * *

### setShape()[#](#setshape)

  

Sets the shape block for a given block.

Note that the previous shape block is not destroyed automatically. The new shape is disconnected from its previously attached block.

#### Parameters[#](#parameters-120)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose shape should be changed. |
| `shape` | `number` | The new shape. |

#### Returns[#](#returns-123)

`void`

#### Signature[#](#signature-104)

```
setShape(id: number, shape: number): void
```

## Block Text[#](#block-text)

Create, edit, and style text content.

### replaceText()[#](#replacetext)

  

Replaces a range of text in a text block.

```
engine.block.replaceText(text, 'Hello World');engine.block.replaceText(text, 'Alex', 6, 11);
```

#### Parameters[#](#parameters-121)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block into which to insert the given text. |
| `text` | `string` | `undefined` | The text which should replace the selected range in the block. |
| `from` | `number` | `-1` | The start index of the UTF-16 range to replace. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range to replace. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-124)

`void`

#### Signature[#](#signature-105)

```
replaceText(id: number, text: string, from?: number, to?: number): void
```

* * *

### removeText()[#](#removetext)

  

Removes a range of text from a text block.

```
engine.block.removeText(text, 0, 6);
```

#### Parameters[#](#parameters-122)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block from which the selected text should be removed. |
| `from` | `number` | `-1` | The start index of the UTF-16 range to remove. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range to remove. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-125)

`void`

#### Signature[#](#signature-106)

```
removeText(id: number, from?: number, to?: number): void
```

* * *

### setTextColor()[#](#settextcolor)

  

Sets the color for a range of text.

```
engine.block.setTextColor(text, { r: 0.0, g: 0.0, b: 0.0, a: 1.0 }, 1, 4);
```

#### Parameters[#](#parameters-123)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose color should be changed. |
| `color` | `Color` | `undefined` | The new color of the selected text range. |
| `from` | `number` | `-1` | The start index of the UTF-16 range to change. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range to change. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-126)

`void`

#### Signature[#](#signature-107)

```
setTextColor(id: number, color: Color, from?: number, to?: number): void
```

* * *

### getTextColors()[#](#gettextcolors)

  

Gets the unique colors within a range of text.

```
const colorsInRange = engine.block.getTextColors(text, 2, 5);
```

#### Parameters[#](#parameters-124)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose colors should be returned. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-127)

`Color`\[\]

The ordered unique list of colors.

#### Signature[#](#signature-108)

```
getTextColors(id: number, from?: number, to?: number): Color[]
```

* * *

### setTextFontWeight()[#](#settextfontweight)

  

Sets the font weight for a range of text.

```
engine.block.setTextFontWeight(text, 'bold', 0, 5);
```

#### Parameters[#](#parameters-125)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose weight should be changed. |
| `fontWeight` | [`FontWeight`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontweight/) | `undefined` | The new weight of the selected text range. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-128)

`void`

#### Signature[#](#signature-109)

```
setTextFontWeight(id: number, fontWeight: FontWeight, from?: number, to?: number): void
```

* * *

### getTextFontWeights()[#](#gettextfontweights)

  

Gets the unique font weights within a range of text.

```
const fontWeights = engine.block.getTextFontWeights(text, 0, 6);
```

#### Parameters[#](#parameters-126)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose font weights should be returned. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-129)

[`FontWeight`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontweight/)\[\]

The ordered unique list of font weights.

#### Signature[#](#signature-110)

```
getTextFontWeights(id: number, from?: number, to?: number): FontWeight[]
```

* * *

### setTextFontSize()[#](#settextfontsize)

  

Sets the font size for a range of text.

```
// With numeric fontSize (in points)engine.block.setTextFontSize(text, 12, 0, 5);
// With font size and options objectengine.block.setTextFontSize(text, 16, { unit: 'Pixel' });engine.block.setTextFontSize(text, 24, { unit: 'Point', from: 0, to: 10 });
```

##### Parameters[#](#parameters-127)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose font size should be changed. |
| `fontSize` | `number` | The new font size value. |
| `options?` | `TextFontSizeOptions` | An options object with unit, from, and to properties. |

##### Returns[#](#returns-130)

`void`

#### Call Signature[#](#call-signature-3)

```
setTextFontSize(   id,   fontSize,   from?,   to?): void;
```

Sets the font size for a range of text.

##### Parameters[#](#parameters-128)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose font size should be changed. |
| `fontSize` | `number` | The new font size in points. |
| `from?` | `number` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to?` | `number` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

##### Returns[#](#returns-131)

`void`

##### Deprecated[#](#deprecated-16)

Use the new signature with options object instead.

##### Example[#](#example-9)

```
// Before migrationengine.block.setTextFontSize(text, 18, 0, 5);// After migrationengine.block.setTextFontSize(text, 18, { from: 0, to: 5 });
```

#### Signatures[#](#signatures-3)

```
setTextFontSize(id: number, fontSize: number, options?: TextFontSizeOptions): void
```

```
setTextFontSize(id: number, fontSize: number, from?: number, to?: number): void
```

* * *

### getTextFontSizes()[#](#gettextfontsizes)

  

Gets the unique font sizes within a range of text.

```
// Get all font sizesconst fontSizes = engine.block.getTextFontSizes(text);
// Get font sizes for a rangeconst fontSizes = engine.block.getTextFontSizes(text, 0, 10);
// With options objectconst sizesInPx = engine.block.getTextFontSizes(text, { unit: 'Pixel' });const sizesInRange = engine.block.getTextFontSizes(text, { unit: 'Millimeter', from: 5, to: 15 });
```

##### Parameters[#](#parameters-129)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose font sizes should be returned. |
| `options?` | `TextFontSizeOptions` | An options object with unit, from, and to properties. |

##### Returns[#](#returns-132)

`number`\[\]

The ordered unique list of font sizes.

#### Call Signature[#](#call-signature-4)

```
getTextFontSizes(   id,   from?,   to?): number[];
```

Gets the unique font sizes within a range of text.

##### Parameters[#](#parameters-130)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose font sizes should be returned. |
| `from?` | `number` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to?` | `number` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

##### Returns[#](#returns-133)

`number`\[\]

The ordered unique list of font sizes in points.

##### Deprecated[#](#deprecated-17)

Use the new signature with options object instead.

##### Example[#](#example-10)

```
// Before migrationconst fontSizes = engine.block.getTextFontSizes(text, 0, 10);// After migrationconst fontSizes = engine.block.getTextFontSizes(text, { from: 0, to: 10 });
```

#### Signatures[#](#signatures-4)

```
getTextFontSizes(id: number, options?: TextFontSizeOptions): number[]
```

```
getTextFontSizes(id: number, from?: number, to?: number): number[]
```

* * *

### setTextFontStyle()[#](#settextfontstyle)

  

Sets the font style for a range of text.

```
engine.block.setTextFontStyle(text, 'italic', 0, 5);
```

#### Parameters[#](#parameters-131)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose style should be changed. |
| `fontStyle` | [`FontStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontstyle/) | `undefined` | The new style of the selected text range. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-134)

`void`

#### Signature[#](#signature-111)

```
setTextFontStyle(id: number, fontStyle: FontStyle, from?: number, to?: number): void
```

* * *

### getTextFontStyles()[#](#gettextfontstyles)

  

Gets the unique font styles within a range of text.

```
const fontStyles = engine.block.getTextFontStyles(text);
```

#### Parameters[#](#parameters-132)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose font styles should be returned. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-135)

[`FontStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/fontstyle/)\[\]

The ordered unique list of font styles.

#### Signature[#](#signature-112)

```
getTextFontStyles(id: number, from?: number, to?: number): FontStyle[]
```

* * *

### getTextCases()[#](#gettextcases)

  

Gets the unique text cases within a range of text.

```
const textCases = engine.block.getTextCases(text);
```

#### Parameters[#](#parameters-133)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose text cases should be returned. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-136)

[`TextCase`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/textcase/)\[\]

The ordered list of text cases.

#### Signature[#](#signature-113)

```
getTextCases(id: number, from?: number, to?: number): TextCase[]
```

* * *

### setTextCase()[#](#settextcase)

  

Sets the text case for a range of text.

```
engine.block.setTextCase(text, 'Titlecase');
```

#### Parameters[#](#parameters-134)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose text case should be changed. |
| `textCase` | [`TextCase`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/textcase/) | `undefined` | The new text case value. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-137)

`void`

#### Signature[#](#signature-114)

```
setTextCase(id: number, textCase: TextCase, from?: number, to?: number): void
```

* * *

### canToggleBoldFont()[#](#cantoggleboldfont)

  

Checks if the bold font weight can be toggled for a range of text.

Returns true if any part of the range is not bold and the bold font is available.

```
const canToggleBold = engine.block.canToggleBoldFont(text);
```

#### Parameters[#](#parameters-135)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block to check. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-138)

`boolean`

Whether the font weight can be toggled.

#### Signature[#](#signature-115)

```
canToggleBoldFont(id: number, from?: number, to?: number): boolean
```

* * *

### canToggleItalicFont()[#](#cantoggleitalicfont)

  

Checks if the italic font style can be toggled for a range of text.

Returns true if any part of the range is not italic and the italic font is available.

```
const canToggleItalic = engine.block.canToggleItalicFont(text);
```

#### Parameters[#](#parameters-136)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block to check. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-139)

`boolean`

Whether the font style can be toggled.

#### Signature[#](#signature-116)

```
canToggleItalicFont(id: number, from?: number, to?: number): boolean
```

* * *

### toggleBoldFont()[#](#toggleboldfont)

  

Toggles the font weight of a text range between bold and normal.

If any part of the range is not bold, the entire range becomes bold. If the entire range is already bold, it becomes normal.

```
engine.block.toggleBoldFont(text);
```

#### Parameters[#](#parameters-137)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block to modify. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-140)

`void`

#### Signature[#](#signature-117)

```
toggleBoldFont(id: number, from?: number, to?: number): void
```

* * *

### toggleItalicFont()[#](#toggleitalicfont)

  

Toggles the font style of a text range between italic and normal.

If any part of the range is not italic, the entire range becomes italic. If the entire range is already italic, it becomes normal.

```
engine.block.toggleItalicFont(text);
```

#### Parameters[#](#parameters-138)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block to modify. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-141)

`void`

#### Signature[#](#signature-118)

```
toggleItalicFont(id: number, from?: number, to?: number): void
```

* * *

### setFont()[#](#setfont)

  

Sets the font and typeface for an entire text block.

Existing formatting is reset.

```
engine.block.setFont(text, font.uri, typeface);
```

#### Parameters[#](#parameters-139)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose font should be changed. |
| `fontFileUri` | `string` | The URI of the new font file. |
| `typeface` | [`Typeface`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/typeface/) | The typeface of the new font. |

#### Returns[#](#returns-142)

`void`

#### Signature[#](#signature-119)

```
setFont(id: number, fontFileUri: string, typeface: Typeface): void
```

* * *

### setTypeface()[#](#settypeface)

  

Sets the typeface for a range of text.

The current formatting is retained as much as possible.

```
engine.block.setTypeface(text, typeface, 2, 5);
```

#### Parameters[#](#parameters-140)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose font should be changed. |
| `typeface` | [`Typeface`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/typeface/) | `undefined` | The new typeface. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-143)

`void`

#### Signature[#](#signature-120)

```
setTypeface(id: number, typeface: Typeface, from?: number, to?: number): void
```

* * *

### getTypeface()[#](#gettypeface)

  

Gets the base typeface of a text block.

This does not return the typefaces of individual text runs.

```
const defaultTypeface = engine.block.getTypeface(text);
```

#### Parameters[#](#parameters-141)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose typeface should be queried. |

#### Returns[#](#returns-144)

[`Typeface`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/typeface/)

the typeface property of the text block.

#### Signature[#](#signature-121)

```
getTypeface(id: number): Typeface
```

* * *

### getTypefaces()[#](#gettypefaces)

  

Gets the unique typefaces within a range of text.

```
const currentTypefaces = engine.block.getTypefaces(text);
```

#### Parameters[#](#parameters-142)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The text block whose typefaces should be queried. |
| `from` | `number` | `-1` | The start index of the UTF-16 range. Defaults to the start of the current selection or text. |
| `to` | `number` | `-1` | The end index of the UTF-16 range. Defaults to the end of the current selection or text. |

#### Returns[#](#returns-145)

[`Typeface`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/typeface/)\[\]

The unique typefaces in the range.

#### Signature[#](#signature-122)

```
getTypefaces(id: number, from?: number, to?: number): Typeface[]
```

* * *

### getTextCursorRange()[#](#gettextcursorrange)

  

Gets the current text cursor or selection range.

Returns the UTF-16 indices of the selected range of the text block that is currently being edited.

```
const selectedRange = engine.block.getTextCursorRange();
```

#### Returns[#](#returns-146)

[`Range`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/range/)

The selected UTF-16 range or `{ from: -1, to: -1 }` if no text block is being edited.

#### Signature[#](#signature-123)

```
getTextCursorRange(): Range
```

* * *

### setTextCursorRange()[#](#settextcursorrange)

  

Sets the text cursor range (selection) within the text block that is currently being edited.

#### Parameters[#](#parameters-143)

| Parameter | Type | Description |
| --- | --- | --- |
| `range` | [`Range`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/range/) | The UTF-16 range to set as the selection. If `from` equals `to`, the cursor is positioned at that index. If `from` and `to` are set to -1, the whole text is selected. |

#### Returns[#](#returns-147)

`void`

#### Throws[#](#throws)

Error if no text block is currently being edited or if the range is invalid.

#### Signature[#](#signature-124)

```
setTextCursorRange(range: Range): void
```

* * *

### getTextVisibleLineCount()[#](#gettextvisiblelinecount)

  

Gets the number of visible lines in a text block.

```
const lineCount = engine.block.getTextVisibleLineCount(text);
```

#### Parameters[#](#parameters-144)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose line count should be returned. |

#### Returns[#](#returns-148)

`number`

The number of lines in the text block.

#### Signature[#](#signature-125)

```
getTextVisibleLineCount(id: number): number
```

* * *

### getTextVisibleLineGlobalBoundingBoxXYWH()[#](#gettextvisiblelineglobalboundingboxxywh)

  

Gets the global bounding box of a visible line of text.

The values are in the scene’s global coordinate space.

```
const lineBoundingBox = engine.block.getTextVisibleLineGlobalBoundingBoxXYWH(text, 0);
```

#### Parameters[#](#parameters-145)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose line bounding box should be returned. |
| `lineIndex` | `number` | The index of the line whose bounding box should be returned. |

#### Returns[#](#returns-149)

[`XYWH`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/xywh/)

The bounding box of the line.

#### Signature[#](#signature-126)

```
getTextVisibleLineGlobalBoundingBoxXYWH(id: number, lineIndex: number): XYWH
```

* * *

### getTextVisibleLineContent()[#](#gettextvisiblelinecontent)

  

Gets the text content of a visible line.

#### Parameters[#](#parameters-146)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The text block whose line content should be returned. |
| `lineIndex` | `number` | The index of the line whose content should be returned. |

#### Returns[#](#returns-150)

`string`

The text content of the line.

#### Signature[#](#signature-127)

```
getTextVisibleLineContent(id: number, lineIndex: number): string
```

## Block Video[#](#block-video)

Manage time-based media like video and audio, including playback, timing, and controls.

### createCaptionsFromURI()[#](#createcaptionsfromuri)

  

Creates new caption blocks from an SRT or VTT file URI.

#### Parameters[#](#parameters-147)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI for the captions file to load. Supported file formats are: SRT and VTT. |

#### Returns[#](#returns-151)

`Promise`<`number`\[\]>

A promise that resolves with a list of the created caption blocks.

#### Signature[#](#signature-128)

```
createCaptionsFromURI(uri: string): Promise<number[]>
```

* * *

### ~hasDuration()~[#](#hasduration)

  

Checks if a block has a duration property.

#### Parameters[#](#parameters-148)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-152)

`boolean`

true if the block has a duration property.

#### Deprecated[#](#deprecated-18)

Use supportsDuration instead.

* * *

### supportsDuration()[#](#supportsduration)

  

Checks if a block supports a duration property.

#### Parameters[#](#parameters-149)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-153)

`boolean`

true if the block supports a duration property.

#### Signature[#](#signature-129)

```
supportsDuration(id: number): boolean
```

* * *

### setDuration()[#](#setduration)

  

Sets the playback duration of a block.

The duration defines how long the block is active in the scene during playback.

#### Parameters[#](#parameters-150)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose duration should be changed. |
| `duration` | `number` | The new duration in seconds. |

#### Returns[#](#returns-154)

`void`

#### Signature[#](#signature-130)

```
setDuration(id: number, duration: number): void
```

* * *

### getDuration()[#](#getduration)

  

Gets the playback duration of a block.

#### Parameters[#](#parameters-151)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose duration should be returned. |

#### Returns[#](#returns-155)

`number`

The block’s duration in seconds.

#### Signature[#](#signature-131)

```
getDuration(id: number): number
```

* * *

### setPageDurationSource()[#](#setpagedurationsource)

  

Sets a block as the page’s duration source.

This causes the page’s total duration to be automatically determined by this block.

#### Parameters[#](#parameters-152)

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | `number` | The page block for which it should be enabled. |
| `id` | `number` | The block that should become the duration source. |

#### Returns[#](#returns-156)

`void`

#### Signature[#](#signature-132)

```
setPageDurationSource(page: number, id: number): void
```

* * *

### isPageDurationSource()[#](#ispagedurationsource)

  

Checks if a block is the duration source for its page.

#### Parameters[#](#parameters-153)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose duration source property should be queried. |

#### Returns[#](#returns-157)

`boolean`

true if the block is a duration source for a page.

#### Signature[#](#signature-133)

```
isPageDurationSource(id: number): boolean
```

* * *

### supportsPageDurationSource()[#](#supportspagedurationsource)

  

Checks if a block can be set as the page’s duration source.

#### Parameters[#](#parameters-154)

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | `number` | The page to check against. |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-158)

`boolean`

true, if the block can be marked as the page’s duration source.

#### Signature[#](#signature-134)

```
supportsPageDurationSource(page: number, id: number): boolean
```

* * *

### removePageDurationSource()[#](#removepagedurationsource)

  

Removes a block as the page’s duration source.

If a scene or page is given, it is deactivated for all blocks within it.

#### Parameters[#](#parameters-155)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose duration source property should be removed. |

#### Returns[#](#returns-159)

`void`

#### Signature[#](#signature-135)

```
removePageDurationSource(id: number): void
```

* * *

### ~hasTimeOffset()~[#](#hastimeoffset)

  

Checks if a block has a time offset property.

#### Parameters[#](#parameters-156)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-160)

`boolean`

true, if the block has a time offset property.

#### Deprecated[#](#deprecated-19)

Use supportsTimeOffset instead.

* * *

### supportsTimeOffset()[#](#supportstimeoffset)

  

Checks if a block supports a time offset.

#### Parameters[#](#parameters-157)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-161)

`boolean`

true, if the block supports a time offset.

#### Signature[#](#signature-136)

```
supportsTimeOffset(id: number): boolean
```

* * *

### setTimeOffset()[#](#settimeoffset)

  

Sets the time offset of a block relative to its parent.

The time offset controls when the block first becomes active in the timeline.

#### Parameters[#](#parameters-158)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose time offset should be changed. |
| `offset` | `number` | The new time offset in seconds. |

#### Returns[#](#returns-162)

`void`

#### Signature[#](#signature-137)

```
setTimeOffset(id: number, offset: number): void
```

* * *

### getTimeOffset()[#](#gettimeoffset)

  

Gets the time offset of a block relative to its parent.

#### Parameters[#](#parameters-159)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose time offset should be queried. |

#### Returns[#](#returns-163)

`number`

The time offset of the block in seconds.

#### Signature[#](#signature-138)

```
getTimeOffset(id: number): number
```

* * *

### ~hasTrim()~[#](#hastrim)

  

Checks if a block has trim properties.

#### Parameters[#](#parameters-160)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-164)

`boolean`

true, if the block has trim properties.

#### Deprecated[#](#deprecated-20)

Use supportsTrim instead.

* * *

### supportsTrim()[#](#supportstrim)

  

Checks if a block supports trim properties.

#### Parameters[#](#parameters-161)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-165)

`boolean`

true, if the block supports trim properties.

#### Signature[#](#signature-139)

```
supportsTrim(id: number): boolean
```

* * *

### setTrimOffset()[#](#settrimoffset)

  

Sets the trim offset of a block’s media content.

This sets the time within the media clip where playback should begin.

#### Parameters[#](#parameters-162)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose trim should be updated. |
| `offset` | `number` | The new trim offset, measured in timeline seconds (scaled by playback rate). |

#### Returns[#](#returns-166)

`void`

#### Signature[#](#signature-140)

```
setTrimOffset(id: number, offset: number): void
```

* * *

### getTrimOffset()[#](#gettrimoffset)

  

Gets the trim offset of a block’s media content.

#### Parameters[#](#parameters-163)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose trim offset should be queried. |

#### Returns[#](#returns-167)

`number`

the trim offset in seconds.

#### Signature[#](#signature-141)

```
getTrimOffset(id: number): number
```

* * *

### setTrimLength()[#](#settrimlength)

  

Sets the trim length of a block’s media content.

This is the duration of the media clip that should be used for playback.

#### Parameters[#](#parameters-164)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The object whose trim length should be updated. |
| `length` | `number` | The new trim length in seconds. |

#### Returns[#](#returns-168)

`void`

#### Signature[#](#signature-142)

```
setTrimLength(id: number, length: number): void
```

* * *

### getTrimLength()[#](#gettrimlength)

  

Gets the trim length of a block’s media content.

#### Parameters[#](#parameters-165)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The object whose trim length should be queried. |

#### Returns[#](#returns-169)

`number`

The trim length of the object in seconds.

#### Signature[#](#signature-143)

```
getTrimLength(id: number): number
```

* * *

### ~getTotalSceneDuration()~[#](#gettotalsceneduration)

  

Gets the total duration of a scene in video mode.

#### Parameters[#](#parameters-166)

| Parameter | Type | Description |
| --- | --- | --- |
| `scene` | `number` | The scene whose duration is being queried. |

#### Returns[#](#returns-170)

`number`

the total scene duration.

#### Deprecated[#](#deprecated-21)

Use `getDuration` and pass a page block.

* * *

### setPlaying()[#](#setplaying)

  

Sets whether a block should play its content during active playback.

#### Parameters[#](#parameters-167)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block that should be updated. |
| `enabled` | `boolean` | Whether the block should be playing its contents. |

#### Returns[#](#returns-171)

`void`

#### Signature[#](#signature-144)

```
setPlaying(id: number, enabled: boolean): void
```

* * *

### isPlaying()[#](#isplaying)

  

Checks if a block is playing its content.

#### Parameters[#](#parameters-168)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-172)

`boolean`

whether the block is playing during playback.

#### Signature[#](#signature-145)

```
isPlaying(id: number): boolean
```

* * *

### ~hasPlaybackTime()~[#](#hasplaybacktime)

  

Checks if a block has a playback time property.

#### Parameters[#](#parameters-169)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-173)

`boolean`

whether the block has a playback time property.

#### Deprecated[#](#deprecated-22)

Use supportsPlaybackTime instead.

* * *

### supportsPlaybackTime()[#](#supportsplaybacktime)

  

Checks if a block supports a playback time property.

#### Parameters[#](#parameters-170)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-174)

`boolean`

whether the block supports a playback time property.

#### Signature[#](#signature-146)

```
supportsPlaybackTime(id: number): boolean
```

* * *

### setPlaybackTime()[#](#setplaybacktime)

  

Sets the current playback time of a block’s content.

#### Parameters[#](#parameters-171)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose playback time should be updated. |
| `time` | `number` | The new playback time of the block in seconds. |

#### Returns[#](#returns-175)

`void`

#### Signature[#](#signature-147)

```
setPlaybackTime(id: number, time: number): void
```

* * *

### getPlaybackTime()[#](#getplaybacktime)

  

Gets the current playback time of a block’s content.

#### Parameters[#](#parameters-172)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-176)

`number`

The playback time of the block in seconds.

#### Signature[#](#signature-148)

```
getPlaybackTime(id: number): number
```

* * *

### setSoloPlaybackEnabled()[#](#setsoloplaybackenabled)

  

Enables or disables solo playback for a block.

When enabled, only this block’s content will play while the rest of the scene remains paused.

```
engine.block.setSoloPlaybackEnabled(videoFill, true);
```

#### Parameters[#](#parameters-173)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or fill to update. |
| `enabled` | `boolean` | Whether solo playback should be enabled. |

#### Returns[#](#returns-177)

`void`

#### Signature[#](#signature-149)

```
setSoloPlaybackEnabled(id: number, enabled: boolean): void
```

* * *

### isSoloPlaybackEnabled()[#](#issoloplaybackenabled)

  

Checks if solo playback is enabled for a block.

```
engine.block.isSoloPlaybackEnabled(videoFill);
```

#### Parameters[#](#parameters-174)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or fill to query. |

#### Returns[#](#returns-178)

`boolean`

Whether solo playback is enabled for this block.

#### Signature[#](#signature-150)

```
isSoloPlaybackEnabled(id: number): boolean
```

* * *

### ~hasPlaybackControl()~[#](#hasplaybackcontrol)

  

Checks if a block has playback controls.

#### Parameters[#](#parameters-175)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-179)

`boolean`

Whether the block has playback control.

#### Deprecated[#](#deprecated-23)

Use supportsPlaybackControl instead

* * *

### supportsPlaybackControl()[#](#supportsplaybackcontrol)

  

Checks if a block supports playback controls.

#### Parameters[#](#parameters-176)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-180)

`boolean`

Whether the block supports playback control.

#### Signature[#](#signature-151)

```
supportsPlaybackControl(id: number): boolean
```

* * *

### setLooping()[#](#setlooping)

  

Sets whether a block’s media content should loop.

#### Parameters[#](#parameters-177)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or video fill to update. |
| `looping` | `boolean` | Whether the block should loop to the beginning or stop. |

#### Returns[#](#returns-181)

`void`

#### Signature[#](#signature-152)

```
setLooping(id: number, looping: boolean): void
```

* * *

### isLooping()[#](#islooping)

  

Checks if a block’s media content is set to loop.

#### Parameters[#](#parameters-178)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-182)

`boolean`

Whether the block is looping.

#### Signature[#](#signature-153)

```
isLooping(id: number): boolean
```

* * *

### setMuted()[#](#setmuted)

  

Sets whether the audio of a block is muted.

#### Parameters[#](#parameters-179)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or video fill to update. |
| `muted` | `boolean` | Whether the audio should be muted. |

#### Returns[#](#returns-183)

`void`

#### Signature[#](#signature-154)

```
setMuted(id: number, muted: boolean): void
```

* * *

### isForceMuted()[#](#isforcemuted)

  

Checks if a block’s audio is muted due to engine rules.

#### Parameters[#](#parameters-180)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-184)

`boolean`

Whether the block is force muted.

#### Signature[#](#signature-155)

```
isForceMuted(id: number): boolean
```

* * *

### isMuted()[#](#ismuted)

  

Checks if a block’s audio is muted.

#### Parameters[#](#parameters-181)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-185)

`boolean`

Whether the block is muted.

#### Signature[#](#signature-156)

```
isMuted(id: number): boolean
```

* * *

### setVolume()[#](#setvolume)

  

Sets the audio volume of a block.

#### Parameters[#](#parameters-182)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or video fill to update. |
| `volume` | `number` | The desired volume, ranging from 0.0 to 1.0. |

#### Returns[#](#returns-186)

`void`

#### Signature[#](#signature-157)

```
setVolume(id: number, volume: number): void
```

* * *

### getVolume()[#](#getvolume)

  

Gets the audio volume of a block.

#### Parameters[#](#parameters-183)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-187)

`number`

The volume, ranging from 0.0 to 1.0.

#### Signature[#](#signature-158)

```
getVolume(id: number): number
```

* * *

### setPlaybackSpeed()[#](#setplaybackspeed)

  

Sets the playback speed multiplier of a block that supports playback control. Note: This also adjusts the trim and duration of the block. Video fills running faster than 3.0x are force muted until reduced to 3.0x or below.

#### Parameters[#](#parameters-184)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block or video fill to update. |
| `speed` | `number` | The desired playback speed multiplier. Valid range is \[0.25, 3.0\] for audio blocks and \[0.25, infinity) for video fills. |

#### Returns[#](#returns-188)

`void`

#### Signature[#](#signature-159)

```
setPlaybackSpeed(id: number, speed: number): void
```

* * *

### getPlaybackSpeed()[#](#getplaybackspeed)

  

Gets the playback speed multiplier of a block that supports playback control.

#### Parameters[#](#parameters-185)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-189)

`number`

The playback speed multiplier.

#### Signature[#](#signature-160)

```
getPlaybackSpeed(id: number): number
```

* * *

### forceLoadAVResource()[#](#forceloadavresource)

  

Forces the loading of a block’s audio/video resource.

If the resource failed to load previously, it will be reloaded.

#### Parameters[#](#parameters-186)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill or audio block whose resource should be loaded. |

#### Returns[#](#returns-190)

`Promise`<`void`\>

A Promise that resolves once the resource has finished loading.

#### Signature[#](#signature-161)

```
forceLoadAVResource(id: number): Promise<void>
```

* * *

### unstable\_isAVResourceLoaded()[#](#unstable_isavresourceloaded)

Checks if a block’s audio/video resource is loaded.

#### Parameters[#](#parameters-187)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill or audio block. |

#### Returns[#](#returns-191)

`boolean`

The loading state of the resource. This API is experimental and may change or be removed in future versions.

* * *

### getAVResourceTotalDuration()[#](#getavresourcetotalduration)

  

Gets the total duration of a block’s audio/video resource.

#### Parameters[#](#parameters-188)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill or audio block. |

#### Returns[#](#returns-192)

`number`

The video or audio file duration in seconds.

#### Signature[#](#signature-162)

```
getAVResourceTotalDuration(id: number): number
```

* * *

### getVideoWidth()[#](#getvideowidth)

  

Gets the width of a block’s video resource.

#### Parameters[#](#parameters-189)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill block. |

#### Returns[#](#returns-193)

`number`

The video width in pixels.

#### Signature[#](#signature-163)

```
getVideoWidth(id: number): number
```

* * *

### getVideoHeight()[#](#getvideoheight)

  

Gets the height of a block’s video resource.

#### Parameters[#](#parameters-190)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill block. |

#### Returns[#](#returns-194)

`number`

The video height in pixels.

#### Signature[#](#signature-164)

```
getVideoHeight(id: number): number
```

* * *

### generateVideoThumbnailSequence()[#](#generatevideothumbnailsequence)

  

Generate a sequence of thumbnails for the given video fill or design block.

Note: There can only be one thumbnail generation request in progress for a given block. Note: During playback, the thumbnail generation will be paused.

#### Parameters[#](#parameters-191)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill or design block. |
| `thumbnailHeight` | `number` | The height of each thumbnail. |
| `timeBegin` | `number` | The start time in seconds for the thumbnail sequence. |
| `timeEnd` | `number` | The end time in seconds for the thumbnail sequence. |
| `numberOfFrames` | `number` | The number of frames to generate. |
| `onFrame` | (`frameIndex`, `result`) => `void` | A callback that receives the frame index and image data. |

#### Returns[#](#returns-195)

A function to cancel the thumbnail generation request.

```
(): void;
```

##### Returns[#](#returns-196)

`void`

#### Signature[#](#signature-165)

```
generateVideoThumbnailSequence(id: number, thumbnailHeight: number, timeBegin: number, timeEnd: number, numberOfFrames: number, onFrame: (frameIndex: number, result: ImageData | Error) => void): () => void
```

* * *

### generateAudioThumbnailSequence()[#](#generateaudiothumbnailsequence)

  

Generate a thumbnail sequence for the given audio block or video fill.

A thumbnail in this case is a chunk of samples in the range of 0 to 1. In case stereo data is requested, the samples are interleaved, starting with the left channel. Note: During playback, the thumbnail generation will be paused.

#### Parameters[#](#parameters-192)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The audio block or video fill. |
| `samplesPerChunk` | `number` | The number of samples per chunk. |
| `timeBegin` | `number` | The start time in seconds for the thumbnail sequence. |
| `timeEnd` | `number` | The end time in seconds for the thumbnail sequence. |
| `numberOfSamples` | `number` | The total number of samples to generate. |
| `numberOfChannels` | `number` | The number of channels in the output (1 for mono, 2 for stereo). |
| `onChunk` | (`chunkIndex`, `result`) => `void` | A callback that receives the chunk index and sample data. |

#### Returns[#](#returns-197)

A function to cancel the thumbnail generation request.

```
(): void;
```

##### Returns[#](#returns-198)

`void`

#### Signature[#](#signature-166)

```
generateAudioThumbnailSequence(id: number, samplesPerChunk: number, timeBegin: number, timeEnd: number, numberOfSamples: number, numberOfChannels: number, onChunk: (chunkIndex: number, result: Error | Float32Array) => void): () => void
```

* * *

### ~getVideoFillThumbnail()~[#](#getvideofillthumbnail)

  

Generates a thumbnail for a video fill.

#### Parameters[#](#parameters-193)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill. |
| `thumbnailHeight` | `number` | The height of a thumbnail. The width will be calculated from the video aspect ratio. |

#### Returns[#](#returns-199)

`Promise`<`Blob`\>

A promise that resolves with a thumbnail encoded as a JPEG blob.

#### Deprecated[#](#deprecated-24)

Use `generateVideoThumbnailSequence` instead.

* * *

### ~getVideoFillThumbnailAtlas()~[#](#getvideofillthumbnailatlas)

  

Generates a thumbnail atlas for a video fill.

#### Parameters[#](#parameters-194)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The video fill. |
| `numberOfColumns` | `number` | The number of columns in the atlas. |
| `numberOfRows` | `number` | The number of rows in the atlas. |
| `thumbnailHeight` | `number` | The height of a single thumbnail. |

#### Returns[#](#returns-200)

`Promise`<`Blob`\>

A promise that resolves with a thumbnail atlas encoded as a JPEG blob.

#### Deprecated[#](#deprecated-25)

Use `generateVideoThumbnailSequence` instead.

* * *

### ~getPageThumbnailAtlas()~[#](#getpagethumbnailatlas)

  

Generates a thumbnail atlas for a page.

#### Parameters[#](#parameters-195)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The page. |
| `numberOfColumns` | `number` | The number of columns in the atlas. |
| `numberOfRows` | `number` | The number of rows in the atlas. |
| `thumbnailHeight` | `number` | The height of a single thumbnail. |

#### Returns[#](#returns-201)

`Promise`<`Blob`\>

A promise that resolves with a thumbnail atlas encoded as a JPEG blob.

#### Deprecated[#](#deprecated-26)

Use `generateVideoThumbnailSequence` instead.

* * *

### setNativePixelBuffer()[#](#setnativepixelbuffer)

  

Updates a pixel stream fill block with a new pixel buffer.

#### Parameters[#](#parameters-196)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The pixel stream fill block. |
| `buffer` | `HTMLCanvasElement` | `HTMLVideoElement` |

#### Returns[#](#returns-202)

`void`

#### Signature[#](#signature-167)

```
setNativePixelBuffer(id: number, buffer: HTMLCanvasElement | HTMLVideoElement): void
```

## Block Animations[#](#block-animations)

Create and manage animations and timeline-based effects.

### createAnimation()[#](#createanimation)

  

Creates a new animation block.

#### Parameters[#](#parameters-197)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`AnimationType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationtype/) | The type of animation to create. |

#### Returns[#](#returns-203)

`number`

The handle of the new animation instance.

#### Signature[#](#signature-168)

```
createAnimation(type: AnimationType): number
```

* * *

### supportsAnimation()[#](#supportsanimation)

  

Checks if a block supports animation.

#### Parameters[#](#parameters-198)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-204)

`boolean`

Whether the block supports animation.

#### Signature[#](#signature-169)

```
supportsAnimation(id: number): boolean
```

* * *

### setInAnimation()[#](#setinanimation)

  

Sets the “in” animation of a block.

#### Parameters[#](#parameters-199)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “in” animation should be set. |
| `animation` | `number` | The animation to set. |

#### Returns[#](#returns-205)

`void`

#### Signature[#](#signature-170)

```
setInAnimation(id: number, animation: number): void
```

* * *

### setLoopAnimation()[#](#setloopanimation)

  

Sets the “loop” animation of a block.

#### Parameters[#](#parameters-200)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “loop” animation should be set. |
| `animation` | `number` | The animation to set. |

#### Returns[#](#returns-206)

`void`

#### Signature[#](#signature-171)

```
setLoopAnimation(id: number, animation: number): void
```

* * *

### setOutAnimation()[#](#setoutanimation)

  

Sets the “out” animation of a block.

#### Parameters[#](#parameters-201)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “out” animation should be set. |
| `animation` | `number` | The animation to set. |

#### Returns[#](#returns-207)

`void`

#### Signature[#](#signature-172)

```
setOutAnimation(id: number, animation: number): void
```

* * *

### getInAnimation()[#](#getinanimation)

  

Gets the “in” animation of a block.

#### Parameters[#](#parameters-202)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “in” animation should be queried. |

#### Returns[#](#returns-208)

`number`

The “in” animation of the block.

#### Signature[#](#signature-173)

```
getInAnimation(id: number): number
```

* * *

### getLoopAnimation()[#](#getloopanimation)

  

Gets the “loop” animation of a block.

#### Parameters[#](#parameters-203)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “loop” animation should be queried. |

#### Returns[#](#returns-209)

`number`

The “loop” animation of the block.

#### Signature[#](#signature-174)

```
getLoopAnimation(id: number): number
```

* * *

### getOutAnimation()[#](#getoutanimation)

  

Gets the “out” animation of a block.

#### Parameters[#](#parameters-204)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose “out” animation should be queried. |

#### Returns[#](#returns-210)

`number`

The “out” animation of the block.

#### Signature[#](#signature-175)

```
getOutAnimation(id: number): number
```

## Block Groups[#](#block-groups)

Create and manage groups of blocks.

### isGroupable()[#](#isgroupable)

  

Checks if a set of blocks can be grouped.

A scene block or a block that is already part of a group cannot be grouped.

```
const groupable = engine.block.isGroupable([block1, block2])
```

#### Parameters[#](#parameters-205)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | An array of block ids. |

#### Returns[#](#returns-211)

`boolean`

Whether the blocks can be grouped together.

#### Signature[#](#signature-176)

```
isGroupable(ids: number[]): boolean
```

* * *

### group()[#](#group)

  

Groups multiple blocks into a new group block.

```
if (engine.block.isGroupable([block1, block2])) {  const group = engine.block.group(block1, block2]);}
```

#### Parameters[#](#parameters-206)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A non-empty array of block ids. |

#### Returns[#](#returns-212)

`number`

The block id of the created group.

#### Signature[#](#signature-177)

```
group(ids: number[]): number
```

* * *

### ungroup()[#](#ungroup)

  

Ungroups a group block, releasing its children.

```
engine.block.ungroup(group);
```

#### Parameters[#](#parameters-207)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The group id from a previous call to `group`. |

#### Returns[#](#returns-213)

`void`

#### Signature[#](#signature-178)

```
ungroup(id: number): void
```

* * *

### enterGroup()[#](#entergroup)

  

Changes selection to a block within a selected group.

Nothing happens if the target is not a group.

```
engine.block.enterGroup(group);
```

#### Parameters[#](#parameters-208)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The group id from a previous call to `group`. |

#### Returns[#](#returns-214)

`void`

#### Signature[#](#signature-179)

```
enterGroup(id: number): void
```

* * *

### exitGroup()[#](#exitgroup)

  

Changes selection from a block to its parent group.

Nothing happens if the block is not part of a group.

```
engine.block.exitGroup(member1);
```

#### Parameters[#](#parameters-209)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | A block id. |

#### Returns[#](#returns-215)

`void`

#### Signature[#](#signature-180)

```
exitGroup(id: number): void
```

## Block State[#](#block-state)

Query the intrinsic state or identity of a block, such as its name, UUID, or lock status.

### getType()[#](#gettype)

  

Gets the longhand type of a given block.

#### Parameters[#](#parameters-210)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-216)

[`ObjectTypeLonghand`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/objecttypelonghand/)

The block’s type.

#### Signature[#](#signature-181)

```
getType(id: number): ObjectTypeLonghand
```

* * *

### setName()[#](#setname)

  

Sets the name of a block.

#### Parameters[#](#parameters-211)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `name` | `string` | The name to set. |

#### Returns[#](#returns-217)

`void`

#### Signature[#](#signature-182)

```
setName(id: number, name: string): void
```

* * *

### getName()[#](#getname)

  

Gets the name of a block.

#### Parameters[#](#parameters-212)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-218)

`string`

The block’s name.

#### Signature[#](#signature-183)

```
getName(id: number): string
```

* * *

### getUUID()[#](#getuuid)

  

Gets the unique universal identifier (UUID) of a block.

#### Parameters[#](#parameters-213)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-219)

`string`

The block’s UUID.

#### Signature[#](#signature-184)

```
getUUID(id: number): string
```

* * *

### isValid()[#](#isvalid)

  

Checks if a block handle is valid.

A block becomes invalid once it has been destroyed.

#### Parameters[#](#parameters-214)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-220)

`boolean`

True, if the block is valid.

#### Signature[#](#signature-185)

```
isValid(id: number): boolean
```

* * *

### referencesAnyVariables()[#](#referencesanyvariables)

  

Checks if a block references any variables.

This check does not recurse into children.

#### Parameters[#](#parameters-215)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to inspect. |

#### Returns[#](#returns-221)

`boolean`

true if the block references variables and false otherwise.

#### Signature[#](#signature-186)

```
referencesAnyVariables(id: number): boolean
```

* * *

### isIncludedInExport()[#](#isincludedinexport)

  

Checks if a block is included in exports.

#### Parameters[#](#parameters-216)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-222)

`boolean`

true, if the block is included on the exported result, false otherwise.

#### Signature[#](#signature-187)

```
isIncludedInExport(id: number): boolean
```

* * *

### setIncludedInExport()[#](#setincludedinexport)

  

Sets whether a block should be included in exports.

#### Parameters[#](#parameters-217)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose exportable state should be set. |
| `enabled` | `boolean` | If true, the block will be included on the exported result. |

#### Returns[#](#returns-223)

`void`

#### Signature[#](#signature-188)

```
setIncludedInExport(id: number, enabled: boolean): void
```

* * *

### isVisibleAtCurrentPlaybackTime()[#](#isvisibleatcurrentplaybacktime)

  

Checks if a block is visible at the current scene playback time.

#### Parameters[#](#parameters-218)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-224)

`boolean`

Whether the block should be visible on the canvas at the current playback time.

#### Signature[#](#signature-189)

```
isVisibleAtCurrentPlaybackTime(id: number): boolean
```

* * *

### getState()[#](#getstate)

  

Gets the current state of a block.

A block’s state is determined by its own state and that of its shape, fill, and effects.

```
const state = engine.block.getState(block);
```

#### Parameters[#](#parameters-219)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-225)

[`BlockState`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blockstate/)

The block’s state: ‘Ready’, ‘Pending’, or ‘Error’.

#### Signature[#](#signature-190)

```
getState(id: number): BlockState
```

* * *

### setState()[#](#setstate)

  

Sets the state of a block.

```
engine.block.setState(video, {type: 'Pending', progress: 0.5});engine.block.setState(page, {type: 'Ready'});engine.block.setState(image, {type: 'Error', error: 'ImageDecoding'});
```

#### Parameters[#](#parameters-220)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose state should be set. |
| `state` | [`BlockState`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blockstate/) | The new state to set. |

#### Returns[#](#returns-226)

`void`

#### Signature[#](#signature-191)

```
setState(id: number, state: BlockState): void
```

## Block Crop[#](#block-crop)

Crop, scale, translate, and transform block content.

### ~hasCrop()~[#](#hascrop)

  

Checks if a block has crop properties.

#### Parameters[#](#parameters-221)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-227)

`boolean`

true, if the block has crop properties.

#### Deprecated[#](#deprecated-27)

Use supportsCrop() instead.

* * *

### supportsCrop()[#](#supportscrop)

  

Checks if a block supports cropping.

```
engine.block.supportsCrop(image);
```

#### Parameters[#](#parameters-222)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-228)

`boolean`

true, if the block supports cropping.

#### Signature[#](#signature-192)

```
supportsCrop(id: number): boolean
```

* * *

### setCropScaleX()[#](#setcropscalex)

  

Sets the horizontal crop scale of a block.

```
engine.block.setCropScaleX(image, 2.0);
```

#### Parameters[#](#parameters-223)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `scaleX` | `number` | The scale in x direction. |

#### Returns[#](#returns-229)

`void`

#### Signature[#](#signature-193)

```
setCropScaleX(id: number, scaleX: number): void
```

* * *

### setCropScaleY()[#](#setcropscaley)

  

Sets the vertical crop scale of a block.

```
engine.block.setCropScaleY(image, 1.5);
```

#### Parameters[#](#parameters-224)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `scaleY` | `number` | The scale in y direction. |

#### Returns[#](#returns-230)

`void`

#### Signature[#](#signature-194)

```
setCropScaleY(id: number, scaleY: number): void
```

* * *

### setCropRotation()[#](#setcroprotation)

  

Sets the crop rotation of a block in radians.

```
engine.block.setCropRotation(image, Math.PI);
```

#### Parameters[#](#parameters-225)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `rotation` | `number` | The rotation in radians. |

#### Returns[#](#returns-231)

`void`

#### Signature[#](#signature-195)

```
setCropRotation(id: number, rotation: number): void
```

* * *

### setCropScaleRatio()[#](#setcropscaleratio)

  

Sets the uniform crop scale ratio of a block.

This scales the content up or down from the center of the crop frame.

```
engine.block.setCropScaleRatio(image, 3.0);
```

#### Parameters[#](#parameters-226)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `scaleRatio` | `number` | The crop scale ratio. |

#### Returns[#](#returns-232)

`void`

#### Signature[#](#signature-196)

```
setCropScaleRatio(id: number, scaleRatio: number): void
```

* * *

### setCropTranslationX()[#](#setcroptranslationx)

  

Sets the horizontal crop translation of a block in percentage of the crop frame width.

```
engine.block.setCropTranslationX(image, -1.0);
```

#### Parameters[#](#parameters-227)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `translationX` | `number` | The translation in x direction. |

#### Returns[#](#returns-233)

`void`

#### Signature[#](#signature-197)

```
setCropTranslationX(id: number, translationX: number): void
```

* * *

### setCropTranslationY()[#](#setcroptranslationy)

  

Sets the vertical crop translation of a block in percentage of the crop frame height.

```
engine.block.setCropTranslationY(image, 1.0);
```

#### Parameters[#](#parameters-228)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be set. |
| `translationY` | `number` | The translation in y direction. |

#### Returns[#](#returns-234)

`void`

#### Signature[#](#signature-198)

```
setCropTranslationY(id: number, translationY: number): void
```

* * *

### resetCrop()[#](#resetcrop)

  

Resets the crop of a block to its default state.

The block’s content fill mode is set to ‘Cover’.

```
engine.block.resetCrop(image);
```

#### Parameters[#](#parameters-229)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be reset. |

#### Returns[#](#returns-235)

`void`

#### Signature[#](#signature-199)

```
resetCrop(id: number): void
```

* * *

### getCropScaleX()[#](#getcropscalex)

  

Gets the horizontal crop scale of a block.

```
const scaleX = engine.block.getCropScaleX(image);
```

#### Parameters[#](#parameters-230)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose scale should be queried. |

#### Returns[#](#returns-236)

`number`

The scale on the x axis.

#### Signature[#](#signature-200)

```
getCropScaleX(id: number): number
```

* * *

### getCropScaleY()[#](#getcropscaley)

  

Gets the vertical crop scale of a block.

```
const scaleY = engine.block.getCropScaleY(image);
```

#### Parameters[#](#parameters-231)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose scale should be queried. |

#### Returns[#](#returns-237)

`number`

The scale on the y axis.

#### Signature[#](#signature-201)

```
getCropScaleY(id: number): number
```

* * *

### getCropRotation()[#](#getcroprotation)

  

Gets the crop rotation of a block in radians.

```
const cropRotation = engine.block.getCropRotation(image);
```

#### Parameters[#](#parameters-232)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop rotation should be queried. |

#### Returns[#](#returns-238)

`number`

The crop rotation in radians.

#### Signature[#](#signature-202)

```
getCropRotation(id: number): number
```

* * *

### getCropScaleRatio()[#](#getcropscaleratio)

  

Gets the uniform crop scale ratio of a block.

```
const cropScaleRatio = engine.block.getCropScaleRatio(image);
```

#### Parameters[#](#parameters-233)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop scale ratio should be queried. |

#### Returns[#](#returns-239)

`number`

The crop scale ratio.

#### Signature[#](#signature-203)

```
getCropScaleRatio(id: number): number
```

* * *

### getCropTranslationX()[#](#getcroptranslationx)

  

Gets the horizontal crop translation of a block in percentage of the crop frame width.

```
const cropTranslationX = engine.block.getCropTranslationX(image);
```

#### Parameters[#](#parameters-234)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose translation should be queried. |

#### Returns[#](#returns-240)

`number`

The translation on the x axis.

#### Signature[#](#signature-204)

```
getCropTranslationX(id: number): number
```

* * *

### getCropTranslationY()[#](#getcroptranslationy)

  

Gets the vertical crop translation of a block in percentage of the crop frame height.

```
const cropTranslationY = engine.block.getCropTranslationY(image);
```

#### Parameters[#](#parameters-235)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose translation should be queried. |

#### Returns[#](#returns-241)

`number`

The translation on the y axis.

#### Signature[#](#signature-205)

```
getCropTranslationY(id: number): number
```

* * *

### adjustCropToFillFrame()[#](#adjustcroptofillframe)

  

Adjusts the crop position and scale of the given image block to fill its crop frame, while maintaining the position and size of the crop frame.

```
const adjustedScaleRatio = engine.block.adjustCropToFillFrame(image, 1.0);
```

#### Parameters[#](#parameters-236)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be adjusted. |
| `minScaleRatio` | `number` | The minimal crop scale ratio to use. |

#### Returns[#](#returns-242)

`number`

The adjusted scale ratio.

#### Signature[#](#signature-206)

```
adjustCropToFillFrame(id: number, minScaleRatio: number): number
```

* * *

### flipCropHorizontal()[#](#flipcrophorizontal)

  

Flips the content horizontally within its crop frame.

```
engine.block.flipCropHorizontal(image);
```

#### Parameters[#](#parameters-237)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be updated. |

#### Returns[#](#returns-243)

`void`

#### Signature[#](#signature-207)

```
flipCropHorizontal(id: number): void
```

* * *

### flipCropVertical()[#](#flipcropvertical)

  

Flips the content vertically within its crop frame.

```
engine.block.flipCropVertical(image);
```

#### Parameters[#](#parameters-238)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose crop should be updated. |

#### Returns[#](#returns-244)

`void`

#### Signature[#](#signature-208)

```
flipCropVertical(id: number): void
```

* * *

### isCropAspectRatioLocked()[#](#iscropaspectratiolocked)

  

Checks if the crop aspect ratio is locked for a block.

When locked, crop handles will maintain the current aspect ratio during resize.

```
const isLocked = engine.block.isCropAspectRatioLocked(block);
```

#### Parameters[#](#parameters-239)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-245)

`boolean`

True if aspect ratio is locked, false otherwise.

#### Signature[#](#signature-209)

```
isCropAspectRatioLocked(id: number): boolean
```

* * *

### setCropAspectRatioLocked()[#](#setcropaspectratiolocked)

  

Sets whether the crop aspect ratio should be locked for a block.

When enabled, crop handles will maintain the current aspect ratio. When disabled, free resizing is allowed.

```
engine.block.setCropAspectRatioLocked(block, true);
```

#### Parameters[#](#parameters-240)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `locked` | `boolean` | Whether aspect ratio should be locked. |

#### Returns[#](#returns-246)

`void`

#### Signature[#](#signature-210)

```
setCropAspectRatioLocked(id: number, locked: boolean): void
```

## Block Events[#](#block-events)

Subscribe to user actions and state changes related to blocks.

### onSelectionChanged()[#](#onselectionchanged)

  

Subscribes to changes in the selection.

#### Parameters[#](#parameters-241)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | This function is called at the end of the engine update if the selection has changed. |

#### Returns[#](#returns-247)

A method to unsubscribe.

```
(): void;
```

##### Returns[#](#returns-248)

`void`

#### Signature[#](#signature-211)

```
onSelectionChanged(callback: () => void): () => void
```

* * *

### onClicked()[#](#onclicked)

  

Subscribes to block click events.

#### Parameters[#](#parameters-242)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`id`) => `void` | This function is called at the end of the engine update if a block has been clicked. |

#### Returns[#](#returns-249)

A method to unsubscribe.

```
(): void;
```

##### Returns[#](#returns-250)

`void`

#### Signature[#](#signature-212)

```
onClicked(callback: (id: number) => void): () => void
```

* * *

### onStateChanged()[#](#onstatechanged)

  

Subscribes to state changes for a set of blocks.

The state is determined by the block and its associated shape, fill, and effects.

```
const unsubscribe = engine.block.onStateChanged([], (blocks) => {  blocks.forEach(block => console.log(block));});
```

#### Parameters[#](#parameters-243)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | A list of block IDs to monitor. If empty, all blocks are monitored. |
| `callback` | (`ids`) => `void` | The function to call when a state changes. |

#### Returns[#](#returns-251)

A function to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-252)

`void`

#### Signature[#](#signature-213)

```
onStateChanged(ids: number[], callback: (ids: number[]) => void): () => void
```

## Block Utils[#](#block-utils)

Check block capabilities like alignability or distributability.

### isAlignable()[#](#isalignable)

  

Checks if a set of blocks can be aligned.

#### Parameters[#](#parameters-244)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | An array of block ids. |

#### Returns[#](#returns-253)

`boolean`

Whether the blocks can be aligned.

#### Signature[#](#signature-214)

```
isAlignable(ids: number[]): boolean
```

* * *

### isDistributable()[#](#isdistributable)

  

Checks if a set of blocks can be distributed.

#### Parameters[#](#parameters-245)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | An array of block ids. |

#### Returns[#](#returns-254)

`boolean`

Whether the blocks can be distributed.

#### Signature[#](#signature-215)

```
isDistributable(ids: number[]): boolean
```

## Block Kind[#](#block-kind)

Get and set a block’s ‘kind’ identifier for custom categorization.

### getKind()[#](#getkind)

  

Gets the kind of a given block.

```
const kind = engine.block.getKind(block);
```

#### Parameters[#](#parameters-246)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-255)

`string`

The block’s kind.

#### Signature[#](#signature-216)

```
getKind(id: number): string
```

* * *

### setKind()[#](#setkind)

  

Sets the kind of a given block, a custom string for categorization of blocks.

```
engine.block.setKind(text, 'title');
```

#### Parameters[#](#parameters-247)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose kind should be changed. |
| `kind` | `string` | The new kind. |

#### Returns[#](#returns-256)

`void`

#### Signature[#](#signature-217)

```
setKind(id: number, kind: string): void
```

## Block Properties[#](#block-properties)

Get and set any block property by name using low-level, generic accessors.

### findAllProperties()[#](#findallproperties)

  

Gets all available properties of a block.

#### Parameters[#](#parameters-248)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose properties should be queried. |

#### Returns[#](#returns-257)

`string`\[\]

A list of the property names.

#### Signature[#](#signature-218)

```
findAllProperties(id: number): string[]
```

* * *

### isPropertyReadable()[#](#ispropertyreadable)

  

Checks if a property is readable.

#### Parameters[#](#parameters-249)

| Parameter | Type | Description |
| --- | --- | --- |
| `property` | `string` | The name of the property to check. |

#### Returns[#](#returns-258)

`boolean`

Whether the property is readable. Returns false for unknown properties.

#### Signature[#](#signature-219)

```
isPropertyReadable(property: string): boolean
```

* * *

### isPropertyWritable()[#](#ispropertywritable)

  

Checks if a property is writable.

#### Parameters[#](#parameters-250)

| Parameter | Type | Description |
| --- | --- | --- |
| `property` | `string` | The name of the property to check. |

#### Returns[#](#returns-259)

`boolean`

Whether the property is writable. Returns false for unknown properties.

#### Signature[#](#signature-220)

```
isPropertyWritable(property: string): boolean
```

* * *

### getPropertyType()[#](#getpropertytype)

  

Gets the type of a property by its name.

#### Parameters[#](#parameters-251)

| Parameter | Type | Description |
| --- | --- | --- |
| `property` | `string` | The name of the property whose type should be queried. |

#### Returns[#](#returns-260)

[`PropertyType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/propertytype/)

The property type.

#### Signature[#](#signature-221)

```
getPropertyType(property: string): PropertyType
```

* * *

### getEnumValues()[#](#getenumvalues)

  

Gets all possible values of an enum property.

#### Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `T` | `string` |

#### Parameters[#](#parameters-252)

| Parameter | Type | Description |
| --- | --- | --- |
| `enumProperty` | `string` | The name of the property whose enum values should be queried. |

#### Returns[#](#returns-261)

`T`\[\]

A list of the enum value names as a string array.

#### Signature[#](#signature-222)

```
getEnumValues(enumProperty: string): T[]
```

* * *

### setBool()[#](#setbool)

  

Sets a boolean property on a block.

```
engine.block.setBool(scene, 'scene/aspectRatioLock', false);
```

#### Parameters[#](#parameters-253)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `BoolPropertyName` | The name of the property to set. |
| `value` | `boolean` | The value to set. |

#### Returns[#](#returns-262)

`void`

#### Signature[#](#signature-223)

```
setBool(id: number, property: BoolPropertyName, value: boolean): void
```

* * *

### getBool()[#](#getbool)

  

Gets a boolean property from a block.

```
engine.block.getBool(scene, 'scene/aspectRatioLock');
```

#### Parameters[#](#parameters-254)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `BoolPropertyName` | The name of the property to query. |

#### Returns[#](#returns-263)

`boolean`

The value of the property.

#### Signature[#](#signature-224)

```
getBool(id: number, property: BoolPropertyName): boolean
```

* * *

### setInt()[#](#setint)

  

Sets an integer property on a block.

```
engine.block.setInt(starShape, 'shape/star/points', points + 2);
```

#### Parameters[#](#parameters-255)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `IntPropertyName` | The name of the property to set. |
| `value` | `number` | The value to set. |

#### Returns[#](#returns-264)

`void`

#### Signature[#](#signature-225)

```
setInt(id: number, property: IntPropertyName, value: number): void
```

* * *

### getInt()[#](#getint)

  

Gets an integer property from a block.

```
engine.block.setInt(starShape, 'shape/star/points', points + 2);
```

#### Parameters[#](#parameters-256)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `IntPropertyName` | The name of the property to query. |

#### Returns[#](#returns-265)

`number`

The value of the property.

#### Signature[#](#signature-226)

```
getInt(id: number, property: IntPropertyName): number
```

* * *

### setFloat()[#](#setfloat)

  

Sets a float property on a block.

```
engine.block.setFloat(text, "text/letterSpacing", 0.2);engine.block.setFloat(text, "text/lineHeight", 1.2);
```

#### Parameters[#](#parameters-257)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `FloatPropertyName` | The name of the property to set. |
| `value` | `number` | The value to set. |

#### Returns[#](#returns-266)

`void`

#### Signature[#](#signature-227)

```
setFloat(id: number, property: FloatPropertyName, value: number): void
```

* * *

### getFloat()[#](#getfloat)

  

Gets a float property from a block.

```
engine.block.getFloat(starShape, 'shape/star/innerDiameter');
```

#### Parameters[#](#parameters-258)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `FloatPropertyName` | The name of the property to query. |

#### Returns[#](#returns-267)

`number`

The value of the property.

#### Signature[#](#signature-228)

```
getFloat(id: number, property: FloatPropertyName): number
```

* * *

### setDouble()[#](#setdouble)

  

Sets a double-precision float property on a block.

```
engine.block.setDouble(audio, 'playback/duration', 1.0);
```

#### Parameters[#](#parameters-259)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `DoublePropertyName` | The name of the property to set. |
| `value` | `number` | The value to set. |

#### Returns[#](#returns-268)

`void`

#### Signature[#](#signature-229)

```
setDouble(id: number, property: DoublePropertyName, value: number): void
```

* * *

### getDouble()[#](#getdouble)

  

Gets a double-precision float property from a block.

```
engine.block.getDouble(audio, 'playback/duration');
```

#### Parameters[#](#parameters-260)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `DoublePropertyName` | The name of the property to query. |

#### Returns[#](#returns-269)

`number`

The value of the property.

#### Signature[#](#signature-230)

```
getDouble(id: number, property: DoublePropertyName): number
```

* * *

### setString()[#](#setstring)

  

Sets a string property on a block.

```
engine.block.setString(text, 'text/text', 'Hello World');engine.block.setString(imageFill, 'fill/image/imageFileURI', 'https://example.com/sample.jpg');
```

#### Parameters[#](#parameters-261)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `StringPropertyName` | The name of the property to set. |
| `value` | `string` | The value to set. |

#### Returns[#](#returns-270)

`void`

#### Signature[#](#signature-231)

```
setString(id: number, property: StringPropertyName, value: string): void
```

* * *

### getString()[#](#getstring)

  

Gets a string property from a block.

```
engine.block.getString(text, 'text/text');engine.block.getString(imageFill, 'fill/image/imageFileURI');
```

#### Parameters[#](#parameters-262)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `StringPropertyName` | The name of the property to query. |

#### Returns[#](#returns-271)

`string`

The value of the property.

#### Signature[#](#signature-232)

```
getString(id: number, property: StringPropertyName): string
```

* * *

### setColor()[#](#setcolor)

  

Sets a color property on a block.

```
// Set the block's fill color to white.engine.block.setColor(colorFill, 'fill/color/value', { r: 1, g: 1, b: 1, a: 1 });
```

#### Parameters[#](#parameters-263)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `ColorPropertyName` | The name of the property to set. |
| `value` | `Color` | The value to set. |

#### Returns[#](#returns-272)

`void`

#### Signature[#](#signature-233)

```
setColor(id: number, property: ColorPropertyName, value: Color): void
```

* * *

### getColor()[#](#getcolor)

  

Gets a color property from a block.

```
engine.block.getColor(colorFill, 'fill/color/value');
```

#### Parameters[#](#parameters-264)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `ColorPropertyName` | The name of the property to query. |

#### Returns[#](#returns-273)

`Color`

The value of the property.

#### Signature[#](#signature-234)

```
getColor(id: number, property: ColorPropertyName): Color
```

* * *

### ~setColorRGBA()~[#](#setcolorrgba)

  

Sets a color property on a block using RGBA values.

#### Parameters[#](#parameters-265)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose property should be set. |
| `property` | `string` | `undefined` | The name of the property to set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. Defaults to 1. |

#### Returns[#](#returns-274)

`void`

#### Deprecated[#](#deprecated-28)

Use setColor() instead.

* * *

### ~getColorRGBA()~[#](#getcolorrgba)

  

Gets a color property from a block as RGBA values.

#### Parameters[#](#parameters-266)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `string` | The name of the property to query. |

#### Returns[#](#returns-275)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

A tuple of channels red, green, blue and alpha in the range of 0 to 1.

#### Deprecated[#](#deprecated-29)

Use getColor() instead.

* * *

### ~setColorSpot()~[#](#setcolorspot)

  

Sets a spot color property on a block.

#### Parameters[#](#parameters-267)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose property should be set. |
| `property` | `string` | `undefined` | The name of the property to set. |
| `name` | `string` | `undefined` | The name of the spot color. |
| `tint` | `number` | `1` | The tint factor in the range of 0 to 1. Defaults to 1. |

#### Returns[#](#returns-276)

`void`

#### Deprecated[#](#deprecated-30)

Use setColor() instead.

* * *

### ~getColorSpotName()~[#](#getcolorspotname)

  

Gets the spot color name from a color property.

#### Parameters[#](#parameters-268)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `string` | The name of the property to query. |

#### Returns[#](#returns-277)

`string`

The name of the spot color.

#### Deprecated[#](#deprecated-31)

Use getColor() instead.

* * *

### ~getColorSpotTint()~[#](#getcolorspottint)

  

Gets the spot color tint from a color property.

#### Parameters[#](#parameters-269)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `string` | The name of the property to query. |

#### Returns[#](#returns-278)

`number`

The tint factor of the spot color.

#### Deprecated[#](#deprecated-32)

Use getColor() instead.

* * *

### setEnum()[#](#setenum)

  

Sets an enum property on a block.

```
engine.block.setEnum(text, 'text/horizontalAlignment', 'Center');engine.block.setEnum(text, 'text/verticalAlignment', 'Center');
```

##### Type Parameters[#](#type-parameters-1)

| Type Parameter |
| --- |
| `T` _extends_ keyof `BlockEnumType` |

##### Parameters[#](#parameters-270)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `T` | The name of the property to set. |
| `value` | `BlockEnumType`\[`T`\] | The enum value as a string. |

##### Returns[#](#returns-279)

`void`

#### Call Signature[#](#call-signature-5)

```
setEnum(   id,   property,   value): void;
```

Sets an enum property on a block.

```
engine.block.setEnum(text, 'text/horizontalAlignment', 'Center');engine.block.setEnum(text, 'text/verticalAlignment', 'Center');
```

##### Parameters[#](#parameters-271)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be set. |
| `property` | `string` | The name of the property to set. |
| `value` | `string` | The enum value as a string. |

##### Returns[#](#returns-280)

`void`

#### Signatures[#](#signatures-5)

```
setEnum(id: number, property: T, value: BlockEnumType[T]): void
```

```
setEnum(id: number, property: string, value: string): void
```

* * *

### getEnum()[#](#getenum)

  

Gets an enum property from a block.

```
engine.block.getEnum(text, 'text/horizontalAlignment');engine.block.getEnum(text, 'text/verticalAlignment');
```

##### Type Parameters[#](#type-parameters-2)

| Type Parameter |
| --- |
| `T` _extends_ keyof `BlockEnumType` |

##### Parameters[#](#parameters-272)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `T` | The name of the property to query. |

##### Returns[#](#returns-281)

`BlockEnumType`\[`T`\]

The value as a string.

#### Call Signature[#](#call-signature-6)

```
getEnum(id, property): string;
```

Gets an enum property from a block.

```
engine.block.getEnum(text, 'text/horizontalAlignment');engine.block.getEnum(text, 'text/verticalAlignment');
```

##### Parameters[#](#parameters-273)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose property should be queried. |
| `property` | `string` | The name of the property to query. |

##### Returns[#](#returns-282)

`string`

The value as a string.

#### Signatures[#](#signatures-6)

```
getEnum(id: number, property: T): BlockEnumType[T]
```

```
getEnum(id: number, property: string): string
```

## Block Strokes[#](#block-strokes)

Control stroke appearance, including color, width, style, and position.

### ~hasStroke()~[#](#hasstroke)

  

Checks if a block has a stroke property.

#### Parameters[#](#parameters-274)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-283)

`boolean`

True if the block has a stroke property.

#### Deprecated[#](#deprecated-33)

Use supportsStroke() instead.

* * *

### supportsStroke()[#](#supportsstroke)

  

Checks if a block supports a stroke.

#### Parameters[#](#parameters-275)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-284)

`boolean`

True if the block supports a stroke.

#### Signature[#](#signature-235)

```
supportsStroke(id: number): boolean
```

* * *

### setStrokeEnabled()[#](#setstrokeenabled)

  

Enables or disables the stroke of a block.

```
engine.block.setStrokeEnabled(block, true);
```

#### Parameters[#](#parameters-276)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke should be enabled or disabled. |
| `enabled` | `boolean` | If true, the stroke will be enabled. |

#### Returns[#](#returns-285)

`void`

#### Signature[#](#signature-236)

```
setStrokeEnabled(id: number, enabled: boolean): void
```

* * *

### isStrokeEnabled()[#](#isstrokeenabled)

  

Checks if the stroke of a block is enabled.

```
const strokeIsEnabled = engine.block.isStrokeEnabled(block);
```

#### Parameters[#](#parameters-277)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke state should be queried. |

#### Returns[#](#returns-286)

`boolean`

True if the block’s stroke is enabled.

#### Signature[#](#signature-237)

```
isStrokeEnabled(id: number): boolean
```

* * *

### ~setStrokeColorRGBA()~[#](#setstrokecolorrgba)

  

Sets the stroke color of a block using RGBA values.

#### Parameters[#](#parameters-278)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose stroke color should be set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. |

#### Returns[#](#returns-287)

`void`

#### Deprecated[#](#deprecated-34)

Use setStrokeColor() instead.

* * *

### setStrokeColor()[#](#setstrokecolor)

  

Sets the stroke color of a block.

#### Parameters[#](#parameters-279)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke color should be set. |
| `color` | `Color` | The color to set. |

#### Returns[#](#returns-288)

`void`

#### Signature[#](#signature-238)

```
setStrokeColor(id: number, color: Color): void
```

* * *

### ~getStrokeColorRGBA()~[#](#getstrokecolorrgba)

  

Gets the stroke color of a block as RGBA values.

#### Parameters[#](#parameters-280)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke color should be queried. |

#### Returns[#](#returns-289)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

The stroke color.

#### Deprecated[#](#deprecated-35)

Use getStrokeColor() instead.

* * *

### getStrokeColor()[#](#getstrokecolor)

  

Gets the stroke color of a block.

#### Parameters[#](#parameters-281)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke color should be queried. |

#### Returns[#](#returns-290)

`Color`

The stroke color.

#### Signature[#](#signature-239)

```
getStrokeColor(id: number): Color
```

* * *

### setStrokeWidth()[#](#setstrokewidth)

  

Sets the stroke width of a block.

#### Parameters[#](#parameters-282)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke width should be set. |
| `width` | `number` | The stroke width to be set. |

#### Returns[#](#returns-291)

`void`

#### Signature[#](#signature-240)

```
setStrokeWidth(id: number, width: number): void
```

* * *

### getStrokeWidth()[#](#getstrokewidth)

  

Gets the stroke width of a block.

#### Parameters[#](#parameters-283)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke width should be queried. |

#### Returns[#](#returns-292)

`number`

The stroke’s width.

#### Signature[#](#signature-241)

```
getStrokeWidth(id: number): number
```

* * *

### setStrokeStyle()[#](#setstrokestyle)

  

Sets the stroke style of a block.

#### Parameters[#](#parameters-284)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke style should be set. |
| `style` |  | `"Dashed"` |

#### Returns[#](#returns-293)

`void`

#### Signature[#](#signature-242)

```
setStrokeStyle(id: number, style: "Dashed" | "DashedRound" | "Dotted" | "LongDashed" | "LongDashedRound" | "Solid"): void
```

* * *

### getStrokeStyle()[#](#getstrokestyle)

  

Gets the stroke style of a block.

#### Parameters[#](#parameters-285)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke style should be queried. |

#### Returns[#](#returns-294)

| `"Dashed"` | `"DashedRound"` | `"Dotted"` | `"LongDashed"` | `"LongDashedRound"` | `"Solid"`

The stroke’s style.

#### Signature[#](#signature-243)

```
getStrokeStyle(id: number): "Dashed" | "DashedRound" | "Dotted" | "LongDashed" | "LongDashedRound" | "Solid"
```

* * *

### setStrokePosition()[#](#setstrokeposition)

  

Sets the stroke position of a block.

#### Parameters[#](#parameters-286)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke position should be set. |
| `position` | `"Center"` | `"Inner"` |

#### Returns[#](#returns-295)

`void`

#### Signature[#](#signature-244)

```
setStrokePosition(id: number, position: "Center" | "Inner" | "Outer"): void
```

* * *

### getStrokePosition()[#](#getstrokeposition)

  

Gets the stroke position of a block.

#### Parameters[#](#parameters-287)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke position should be queried. |

#### Returns[#](#returns-296)

`"Center"` | `"Inner"` | `"Outer"`

The stroke position.

#### Signature[#](#signature-245)

```
getStrokePosition(id: number): "Center" | "Inner" | "Outer"
```

* * *

### setStrokeCornerGeometry()[#](#setstrokecornergeometry)

  

Sets the stroke corner geometry of a block.

#### Parameters[#](#parameters-288)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke corner geometry should be set. |
| `cornerGeometry` | `"Bevel"` | `"Miter"` |

#### Returns[#](#returns-297)

`void`

#### Signature[#](#signature-246)

```
setStrokeCornerGeometry(id: number, cornerGeometry: "Bevel" | "Miter" | "Round"): void
```

* * *

### getStrokeCornerGeometry()[#](#getstrokecornergeometry)

  

Gets the stroke corner geometry of a block.

#### Parameters[#](#parameters-289)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose stroke corner geometry should be queried. |

#### Returns[#](#returns-298)

`"Bevel"` | `"Miter"` | `"Round"`

The stroke corner geometry.

#### Signature[#](#signature-247)

```
getStrokeCornerGeometry(id: number): "Bevel" | "Miter" | "Round"
```

## Block Drop Shadow[#](#block-drop-shadow)

Configure drop shadow effects, including blur, color, and offset.

### ~hasDropShadow()~[#](#hasdropshadow)

  

Checks if a block has a drop shadow property.

#### Parameters[#](#parameters-290)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-299)

`boolean`

True if the block has a drop shadow property.

#### Deprecated[#](#deprecated-36)

Use supportsDropShadow() instead.

* * *

### supportsDropShadow()[#](#supportsdropshadow)

  

Checks if a block supports a drop shadow.

#### Parameters[#](#parameters-291)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-300)

`boolean`

True if the block supports a drop shadow.

#### Signature[#](#signature-248)

```
supportsDropShadow(id: number): boolean
```

* * *

### setDropShadowEnabled()[#](#setdropshadowenabled)

  

Enables or disables the drop shadow of a block.

```
engine.block.setDropShadowEnabled(block, true);
```

#### Parameters[#](#parameters-292)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow should be enabled or disabled. |
| `enabled` | `boolean` | If true, the drop shadow will be enabled. |

#### Returns[#](#returns-301)

`void`

#### Signature[#](#signature-249)

```
setDropShadowEnabled(id: number, enabled: boolean): void
```

* * *

### isDropShadowEnabled()[#](#isdropshadowenabled)

  

Checks if the drop shadow of a block is enabled.

```
const dropShadowIsEnabled = engine.block.isDropShadowEnabled(block);
```

#### Parameters[#](#parameters-293)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow state should be queried. |

#### Returns[#](#returns-302)

`boolean`

True if the block’s drop shadow is enabled.

#### Signature[#](#signature-250)

```
isDropShadowEnabled(id: number): boolean
```

* * *

### ~setDropShadowColorRGBA()~[#](#setdropshadowcolorrgba)

  

Sets the drop shadow color of a block using RGBA values.

#### Parameters[#](#parameters-294)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `id` | `number` | `undefined` | The block whose drop shadow color should be set. |
| `r` | `number` | `undefined` | The red color component in the range of 0 to 1. |
| `g` | `number` | `undefined` | The green color component in the range of 0 to 1. |
| `b` | `number` | `undefined` | The blue color component in the range of 0 to 1. |
| `a` | `number` | `1` | The alpha color component in the range of 0 to 1. |

#### Returns[#](#returns-303)

`void`

#### Deprecated[#](#deprecated-37)

Use setDropShadowColor() instead.

* * *

### setDropShadowColor()[#](#setdropshadowcolor)

  

Sets the drop shadow color of a block.

#### Parameters[#](#parameters-295)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow color should be set. |
| `color` | `Color` | The color to set. |

#### Returns[#](#returns-304)

`void`

#### Signature[#](#signature-251)

```
setDropShadowColor(id: number, color: Color): void
```

* * *

### ~getDropShadowColorRGBA()~[#](#getdropshadowcolorrgba)

  

Gets the drop shadow color of a block as RGBA values.

#### Parameters[#](#parameters-296)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow color should be queried. |

#### Returns[#](#returns-305)

[`RGBA`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/rgba/)

The drop shadow color.

#### Deprecated[#](#deprecated-38)

Use getDropShadowColor instead.

* * *

### getDropShadowColor()[#](#getdropshadowcolor)

  

Gets the drop shadow color of a block.

#### Parameters[#](#parameters-297)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow color should be queried. |

#### Returns[#](#returns-306)

`Color`

The drop shadow color.

#### Signature[#](#signature-252)

```
getDropShadowColor(id: number): Color
```

* * *

### setDropShadowOffsetX()[#](#setdropshadowoffsetx)

  

Sets the drop shadow’s horizontal offset.

#### Parameters[#](#parameters-298)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s X offset should be set. |
| `offsetX` | `number` | The X offset to be set. |

#### Returns[#](#returns-307)

`void`

#### Signature[#](#signature-253)

```
setDropShadowOffsetX(id: number, offsetX: number): void
```

* * *

### getDropShadowOffsetX()[#](#getdropshadowoffsetx)

  

Gets the drop shadow’s horizontal offset.

#### Parameters[#](#parameters-299)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s X offset should be queried. |

#### Returns[#](#returns-308)

`number`

The offset.

#### Signature[#](#signature-254)

```
getDropShadowOffsetX(id: number): number
```

* * *

### setDropShadowOffsetY()[#](#setdropshadowoffsety)

  

Sets the drop shadow’s vertical offset.

#### Parameters[#](#parameters-300)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s Y offset should be set. |
| `offsetY` | `number` | The Y offset to be set. |

#### Returns[#](#returns-309)

`void`

#### Signature[#](#signature-255)

```
setDropShadowOffsetY(id: number, offsetY: number): void
```

* * *

### getDropShadowOffsetY()[#](#getdropshadowoffsety)

  

Gets the drop shadow’s vertical offset.

#### Parameters[#](#parameters-301)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s Y offset should be queried. |

#### Returns[#](#returns-310)

`number`

The offset.

#### Signature[#](#signature-256)

```
getDropShadowOffsetY(id: number): number
```

* * *

### setDropShadowBlurRadiusX()[#](#setdropshadowblurradiusx)

  

Sets the drop shadow’s horizontal blur radius.

#### Parameters[#](#parameters-302)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s blur radius should be set. |
| `blurRadiusX` | `number` | The blur radius to be set. |

#### Returns[#](#returns-311)

`void`

#### Signature[#](#signature-257)

```
setDropShadowBlurRadiusX(id: number, blurRadiusX: number): void
```

* * *

### getDropShadowBlurRadiusX()[#](#getdropshadowblurradiusx)

  

Gets the drop shadow’s horizontal blur radius.

#### Parameters[#](#parameters-303)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s blur radius should be queried. |

#### Returns[#](#returns-312)

`number`

The blur radius.

#### Signature[#](#signature-258)

```
getDropShadowBlurRadiusX(id: number): number
```

* * *

### setDropShadowBlurRadiusY()[#](#setdropshadowblurradiusy)

  

Sets the drop shadow’s vertical blur radius.

#### Parameters[#](#parameters-304)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s blur radius should be set. |
| `blurRadiusY` | `number` | The blur radius to be set. |

#### Returns[#](#returns-313)

`void`

#### Signature[#](#signature-259)

```
setDropShadowBlurRadiusY(id: number, blurRadiusY: number): void
```

* * *

### getDropShadowBlurRadiusY()[#](#getdropshadowblurradiusy)

  

Gets the drop shadow’s vertical blur radius.

#### Parameters[#](#parameters-305)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s blur radius should be queried. |

#### Returns[#](#returns-314)

`number`

The blur radius.

#### Signature[#](#signature-260)

```
getDropShadowBlurRadiusY(id: number): number
```

* * *

### setDropShadowClip()[#](#setdropshadowclip)

  

Sets the drop shadow’s clipping behavior.

This only applies to shapes.

#### Parameters[#](#parameters-306)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s clip should be set. |
| `clip` | `boolean` | The drop shadow’s clip to be set. |

#### Returns[#](#returns-315)

`void`

#### Signature[#](#signature-261)

```
setDropShadowClip(id: number, clip: boolean): void
```

* * *

### getDropShadowClip()[#](#getdropshadowclip)

  

Gets the drop shadow’s clipping behavior.

#### Parameters[#](#parameters-307)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose drop shadow’s clipping should be queried. |

#### Returns[#](#returns-316)

`boolean`

The drop shadow’s clipping state.

#### Signature[#](#signature-262)

```
getDropShadowClip(id: number): boolean
```

## Block Effects[#](#block-effects)

Create, manage, and apply various visual effects to blocks.

### createEffect()[#](#createeffect)

  

Creates a new effect block.

#### Parameters[#](#parameters-308)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`EffectType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/effecttype/) | The type of the effect. |

#### Returns[#](#returns-317)

`number`

The created effect’s handle.

#### Signature[#](#signature-263)

```
createEffect(type: EffectType): number
```

* * *

### ~hasEffects()~[#](#haseffects)

  

Checks if a block supports effects.

#### Parameters[#](#parameters-309)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-318)

`boolean`

True, if the block can render effects, false otherwise.

#### Deprecated[#](#deprecated-39)

Use supportsEffects instead.

* * *

### supportsEffects()[#](#supportseffects)

  

Checks if a block supports effects.

#### Parameters[#](#parameters-310)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-319)

`boolean`

True, if the block can render effects, false otherwise.

#### Signature[#](#signature-264)

```
supportsEffects(id: number): boolean
```

* * *

### getEffects()[#](#geteffects)

  

Gets all effects attached to a block.

#### Parameters[#](#parameters-311)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-320)

`number`\[\]

A list of effects or an error, if the block doesn’t support effects.

#### Signature[#](#signature-265)

```
getEffects(id: number): number[]
```

* * *

### insertEffect()[#](#inserteffect)

  

Inserts an effect into a block’s effect list at a given index.

#### Parameters[#](#parameters-312)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `effectId` | `number` | The effect to insert. |
| `index` | `number` | The index at which the effect shall be inserted. |

#### Returns[#](#returns-321)

`void`

#### Signature[#](#signature-266)

```
insertEffect(id: number, effectId: number, index: number): void
```

* * *

### appendEffect()[#](#appendeffect)

  

Appends an effect to a block’s effect list.

#### Parameters[#](#parameters-313)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to append the effect to. |
| `effectId` | `number` | The effect to append. |

#### Returns[#](#returns-322)

`void`

#### Signature[#](#signature-267)

```
appendEffect(id: number, effectId: number): void
```

* * *

### removeEffect()[#](#removeeffect)

  

Removes an effect from a block’s effect list at a given index.

#### Parameters[#](#parameters-314)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to remove the effect from. |
| `index` | `number` | The index where the effect is stored. |

#### Returns[#](#returns-323)

`void`

#### Signature[#](#signature-268)

```
removeEffect(id: number, index: number): void
```

* * *

### ~hasEffectEnabled()~[#](#haseffectenabled)

  

Checks if an effect block can be enabled or disabled.

#### Parameters[#](#parameters-315)

| Parameter | Type | Description |
| --- | --- | --- |
| `effectId` | `number` | The ‘effect’ block to query. |

#### Returns[#](#returns-324)

`boolean`

True, if the block supports enabling and disabling, false otherwise.

#### Deprecated[#](#deprecated-40)

Calls to this function can be removed. All effects can be enabled and disabled.

* * *

### setEffectEnabled()[#](#seteffectenabled)

  

Sets the enabled state of an effect block.

```
engine.block.setEffectEnabled(effects[0], false);
```

#### Parameters[#](#parameters-316)

| Parameter | Type | Description |
| --- | --- | --- |
| `effectId` | `number` | The ‘effect’ block to update. |
| `enabled` | `boolean` | The new state. |

#### Returns[#](#returns-325)

`void`

#### Signature[#](#signature-269)

```
setEffectEnabled(effectId: number, enabled: boolean): void
```

* * *

### isEffectEnabled()[#](#iseffectenabled)

  

Queries if an effect block is enabled.

```
engine.block.isEffectEnabled(effects[0]);
```

#### Parameters[#](#parameters-317)

| Parameter | Type | Description |
| --- | --- | --- |
| `effectId` | `number` | The ‘effect’ block to query. |

#### Returns[#](#returns-326)

`boolean`

True, if the effect is enabled. False otherwise.

#### Signature[#](#signature-270)

```
isEffectEnabled(effectId: number): boolean
```

## Block Blur[#](#block-blur)

Apply and configure blur effects on blocks.

### createBlur()[#](#createblur)

  

Creates a new blur block.

#### Parameters[#](#parameters-318)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | [`BlurType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/blurtype/) | The type of blur. |

#### Returns[#](#returns-327)

`number`

The handle of the newly created blur.

#### Signature[#](#signature-271)

```
createBlur(type: BlurType): number
```

* * *

### ~hasBlur()~[#](#hasblur)

  

Checks if a block supports blur.

#### Parameters[#](#parameters-319)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-328)

`boolean`

True, if the block supports blur.

#### Deprecated[#](#deprecated-41)

Use supportsBlur instead.

* * *

### supportsBlur()[#](#supportsblur)

  

Checks if a block supports blur.

#### Parameters[#](#parameters-320)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-329)

`boolean`

True, if the block supports blur.

#### Signature[#](#signature-272)

```
supportsBlur(id: number): boolean
```

* * *

### setBlur()[#](#setblur)

  

Sets the blur effect for a block.

#### Parameters[#](#parameters-321)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `blurId` | `number` | A ‘blur’ block to apply. |

#### Returns[#](#returns-330)

`void`

#### Signature[#](#signature-273)

```
setBlur(id: number, blurId: number): void
```

* * *

### getBlur()[#](#getblur)

  

Gets the blur block of a given design block.

#### Parameters[#](#parameters-322)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-331)

`number`

The ‘blur’ block.

#### Signature[#](#signature-274)

```
getBlur(id: number): number
```

* * *

### setBlurEnabled()[#](#setblurenabled)

  

Enables or disables the blur effect on a block.

```
engine.block.setBlurEnabled(block, true);
```

#### Parameters[#](#parameters-323)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `enabled` | `boolean` | The new enabled value. |

#### Returns[#](#returns-332)

`void`

#### Signature[#](#signature-275)

```
setBlurEnabled(id: number, enabled: boolean): void
```

* * *

### isBlurEnabled()[#](#isblurenabled)

  

Checks if blur is enabled for a block.

```
const isBlurEnabled = engine.block.isBlurEnabled(block);
```

#### Parameters[#](#parameters-324)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-333)

`boolean`

True, if the blur is enabled. False otherwise.

#### Signature[#](#signature-276)

```
isBlurEnabled(id: number): boolean
```

## Block Placeholder[#](#block-placeholder)

Manage placeholder functionality, controls, and behavior.

### setPlaceholderEnabled()[#](#setplaceholderenabled)

  

Enables or disables the placeholder function for a block.

When set to `true`, the given block becomes selectable by users and its placeholder capabilities are enabled in Adopter mode.

```
engine.block.setPlaceholderEnabled(block, true);
```

#### Parameters[#](#parameters-325)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder function should be enabled or disabled. |
| `enabled` | `boolean` | Whether the function should be enabled or disabled. |

#### Returns[#](#returns-334)

`void`

#### Signature[#](#signature-277)

```
setPlaceholderEnabled(id: number, enabled: boolean): void
```

* * *

### isPlaceholderEnabled()[#](#isplaceholderenabled)

  

Checks if the placeholder function for a block is enabled and can be selected by users in Adopter mode.

```
const placeholderIsEnabled = engine.block.isPlaceholderEnabled(block);
```

#### Parameters[#](#parameters-326)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder function state should be queried. |

#### Returns[#](#returns-335)

`boolean`

The enabled state of the placeholder function.

#### Signature[#](#signature-278)

```
isPlaceholderEnabled(id: number): boolean
```

* * *

### ~hasPlaceholderBehavior()~[#](#hasplaceholderbehavior)

  

Checks if a block supports placeholder behavior.

#### Parameters[#](#parameters-327)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-336)

`boolean`

True, if the block supports placeholder behavior.

#### Deprecated[#](#deprecated-42)

Use supportsPlaceholderBehavior instead.

* * *

### supportsPlaceholderBehavior()[#](#supportsplaceholderbehavior)

  

Checks if a block supports placeholder behavior.

```
const placeholderBehaviorSupported = engine.block.supportsPlaceholderBehavior(block);
```

#### Parameters[#](#parameters-328)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-337)

`boolean`

True, if the block supports placeholder behavior.

#### Signature[#](#signature-279)

```
supportsPlaceholderBehavior(id: number): boolean
```

* * *

### setPlaceholderBehaviorEnabled()[#](#setplaceholderbehaviorenabled)

  

Enables or disables the placeholder behavior for a block.

When its fill block is set to `true`, an image block will act as a placeholder, showing a control overlay and a replacement button.

```
engine.block.setPlaceholderBehaviorEnabled(block, true);
```

#### Parameters[#](#parameters-329)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder behavior should be enabled or disabled. |
| `enabled` | `boolean` | Whether the placeholder behavior should be enabled or disabled. |

#### Returns[#](#returns-338)

`void`

#### Signature[#](#signature-280)

```
setPlaceholderBehaviorEnabled(id: number, enabled: boolean): void
```

* * *

### isPlaceholderBehaviorEnabled()[#](#isplaceholderbehaviorenabled)

  

Checks if the placeholder behavior for a block is enabled.

```
engine.block.setPlaceholderBehaviorEnabled(block, true);
```

#### Parameters[#](#parameters-330)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder behavior state should be queried. |

#### Returns[#](#returns-339)

`boolean`

The enabled state of the placeholder behavior.

#### Signature[#](#signature-281)

```
isPlaceholderBehaviorEnabled(id: number): boolean
```

* * *

### ~hasPlaceholderControls()~[#](#hasplaceholdercontrols)

  

Checks if a block supports placeholder controls.

#### Parameters[#](#parameters-331)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-340)

`boolean`

True, if the block supports placeholder controls.

#### Deprecated[#](#deprecated-43)

Use supportsPlaceholderControls instead.

* * *

### supportsPlaceholderControls()[#](#supportsplaceholdercontrols)

  

Checks if a block supports placeholder controls, e.g. a control overlay and a replacement button.

#### Parameters[#](#parameters-332)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-341)

`boolean`

True, if the block supports placeholder controls.

#### Signature[#](#signature-282)

```
supportsPlaceholderControls(id: number): boolean
```

* * *

### setPlaceholderControlsOverlayEnabled()[#](#setplaceholdercontrolsoverlayenabled)

  

Enables or disables the placeholder overlay pattern.

```
engine.block.setPlaceholderControlsOverlayEnabled(block, true);
```

#### Parameters[#](#parameters-333)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder overlay should be enabled or disabled. |
| `enabled` | `boolean` | Whether the placeholder overlay should be shown or not. |

#### Returns[#](#returns-342)

`void`

#### Signature[#](#signature-283)

```
setPlaceholderControlsOverlayEnabled(id: number, enabled: boolean): void
```

* * *

### isPlaceholderControlsOverlayEnabled()[#](#isplaceholdercontrolsoverlayenabled)

  

Checks if the placeholder overlay pattern is enabled.

```
const overlayEnabled = engine.block.isPlaceholderControlsOverlayEnabled(block);
```

#### Parameters[#](#parameters-334)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder overlay visibility state should be queried. |

#### Returns[#](#returns-343)

`boolean`

The visibility state of the block’s placeholder overlay pattern.

#### Signature[#](#signature-284)

```
isPlaceholderControlsOverlayEnabled(id: number): boolean
```

* * *

### setPlaceholderControlsButtonEnabled()[#](#setplaceholdercontrolsbuttonenabled)

  

Enables or disables the placeholder button.

```
engine.block.setPlaceholderControlsButtonEnabled(block, true);
```

#### Parameters[#](#parameters-335)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder button should be shown or not. |
| `enabled` | `boolean` | Whether the placeholder button should be shown or not. |

#### Returns[#](#returns-344)

`void`

#### Signature[#](#signature-285)

```
setPlaceholderControlsButtonEnabled(id: number, enabled: boolean): void
```

* * *

### isPlaceholderControlsButtonEnabled()[#](#isplaceholdercontrolsbuttonenabled)

  

Checks if the placeholder button is enabled.

```
const buttonEnabled = engine.block.isPlaceholderControlsButtonEnabled(block);
```

#### Parameters[#](#parameters-336)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose placeholder button visibility state should be queried. |

#### Returns[#](#returns-345)

`boolean`

The visibility state of the block’s placeholder button.

#### Signature[#](#signature-286)

```
isPlaceholderControlsButtonEnabled(id: number): boolean
```

## Block Scopes[#](#block-scopes)

Manage permissions and capabilities per block.

### setScopeEnabled()[#](#setscopeenabled)

  

Enables or disables a scope for a block.

```
// Allow the user to move the image block.engine.block.setScopeEnabled(image, 'layer/move', true);
```

#### Parameters[#](#parameters-337)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose scope should be enabled or disabled. |
| `key` | [`Scope`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scope/) | The scope to enable or disable. |
| `enabled` | `boolean` | Whether the scope should be enabled or disabled. |

#### Returns[#](#returns-346)

`void`

#### Signature[#](#signature-287)

```
setScopeEnabled(id: number, key: Scope, enabled: boolean): void
```

* * *

### isScopeEnabled()[#](#isscopeenabled)

  

Checks if a scope is enabled for a block.

```
engine.block.isScopeEnabled(image, 'layer/move');
```

#### Parameters[#](#parameters-338)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose scope state should be queried. |
| `key` | [`Scope`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scope/) | The scope to query. |

#### Returns[#](#returns-347)

`boolean`

The enabled state of the scope for the given block.

#### Signature[#](#signature-288)

```
isScopeEnabled(id: number, key: Scope): boolean
```

* * *

### isAllowedByScope()[#](#isallowedbyscope)

  

Checks if an operation is allowed by a block’s scopes.

```
// This will return true when the global scope is set to 'Defer'.engine.block.isAllowedByScope(image, 'layer/move');
```

#### Parameters[#](#parameters-339)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to check. |
| `key` | [`Scope`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scope/) | The scope to check. |

#### Returns[#](#returns-348)

`boolean`

Whether the scope is allowed for the given block.

#### Signature[#](#signature-289)

```
isAllowedByScope(id: number, key: Scope): boolean
```

## Block Boolean Operations[#](#block-boolean-operations)

Combine multiple blocks into a single new block using boolean path operations.

### isCombinable()[#](#iscombinable)

  

Checks if a set of blocks can be combined using a boolean operation.

Only graphics blocks and text blocks can be combined. All blocks must have the “lifecycle/duplicate” scope enabled.

#### Parameters[#](#parameters-340)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | An array of block ids. |

#### Returns[#](#returns-349)

`boolean`

Whether the blocks can be combined.

#### Signature[#](#signature-290)

```
isCombinable(ids: number[]): boolean
```

* * *

### combine()[#](#combine)

  

Performs a boolean operation on a set of blocks.

All blocks must be combinable. See `isCombinable`. The parent, fill and sort order of the new block is that of the prioritized block.

#### Parameters[#](#parameters-341)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The blocks to combine. They will be destroyed if “lifecycle/destroy” scope is enabled. |
| `op` | [`BooleanOperation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/booleanoperation/) | The boolean operation to perform. |

#### Returns[#](#returns-350)

`number`

The newly created block or an error.

#### Signature[#](#signature-291)

```
combine(ids: number[], op: BooleanOperation): number
```

## Block Cutout[#](#block-cutout)

Create cutout operations and path-based modifications.

### createCutoutFromBlocks()[#](#createcutoutfromblocks)

  

Creates a cutout block from the contours of other blocks.

The path is derived from either existing vector paths or by vectorizing the block’s appearance.

#### Parameters[#](#parameters-342)

| Parameter | Type | Default value | Description |
| --- | --- | --- | --- |
| `ids` | `number`\[\] | `undefined` | The blocks whose shape will serve as the basis for the cutout’s path. |
| `vectorizeDistanceThreshold` | `number` | `2` | Max deviation from the original contour during vectorization. |
| `simplifyDistanceThreshold` | `number` | `4` | Max deviation for path simplification. 0 disables simplification. |
| `useExistingShapeInformation` | `boolean` | `true` | If true, use existing vector paths. |

#### Returns[#](#returns-351)

`number`

The newly created block or an error.

#### Signature[#](#signature-292)

```
createCutoutFromBlocks(ids: number[], vectorizeDistanceThreshold?: number, simplifyDistanceThreshold?: number, useExistingShapeInformation?: boolean): number
```

* * *

### createCutoutFromPath()[#](#createcutoutfrompath)

  

Creates a cutout block from an SVG path string.

#### Parameters[#](#parameters-343)

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | An SVG string describing a path. |

#### Returns[#](#returns-352)

`number`

The newly created block or an error.

#### Signature[#](#signature-293)

```
createCutoutFromPath(path: string): number
```

* * *

### createCutoutFromOperation()[#](#createcutoutfromoperation)

  

Creates a new cutout block by performing a boolean operation on existing cutout blocks.

#### Parameters[#](#parameters-344)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `number`\[\] | The cutout blocks with which to perform to the operation. |
| `op` | [`CutoutOperation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/cutoutoperation/) | The boolean operation to perform. |

#### Returns[#](#returns-353)

`number`

The newly created block or an error.

#### Signature[#](#signature-294)

```
createCutoutFromOperation(ids: number[], op: CutoutOperation): number
```

## Block[#](#block)

### split()[#](#split)

  

Splits a block at the specified time.

The original block will be trimmed to end at the split time, and the returned duplicate will start at the split time and continue to the original end time.

```
const duplicate = engine.block.split(video, 10.0);
```

#### Parameters[#](#parameters-345)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to split. |
| `atTime` | `number` | The time (in seconds) relative to the block’s time offset where the split should occur. |
| `options` | [`SplitOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/splitoptions/) | The options for configuring the split operation. |

#### Returns[#](#returns-354)

`number`

The newly created second half of the split block.

#### Signature[#](#signature-295)

```
split(id: number, atTime: number, options?: SplitOptions): number
```

## Block Audio[#](#block-audio)

### getAudioTrackCountFromVideo()[#](#getaudiotrackcountfromvideo)

  

Gets the number of available audio tracks in a video fill block.

```
const trackCount = engine.block.getAudioTrackCountFromVideo(videoBlock);console.log(`Video has ${trackCount} audio tracks`);
```

#### Parameters[#](#parameters-346)

| Parameter | Type | Description |
| --- | --- | --- |
| `videoFillBlock` | `number` | The video fill block to examine. |

#### Returns[#](#returns-355)

`number`

The number of audio tracks.

#### Throws[#](#throws-1)

Will throw an error if the block is not a video fill or has no audio.

#### Signature[#](#signature-296)

```
getAudioTrackCountFromVideo(videoFillBlock: number): number
```

* * *

### createAudioFromVideo()[#](#createaudiofromvideo)

  

Creates a new audio block by extracting a specific audio track from a video fill block.

```
// Extract the first audio track (usually the main mix) with trim settingsconst audioBlock = engine.block.createAudioFromVideo(videoFillBlock, 0);
// Extract full audio track without trim settingsconst audioBlock = engine.block.createAudioFromVideo(videoFillBlock, 0, { keepTrimSettings: false });
// Extract a specific track, keep trim settings, and mute the original videoconst dialogueTrack = engine.block.createAudioFromVideo(videoFillBlock, 1, { keepTrimSettings: true, muteOriginalVideo: true });
```

#### Parameters[#](#parameters-347)

| Parameter | Type | Description |
| --- | --- | --- |
| `videoFillBlock` | `number` | The video fill block to extract audio from. |
| `trackIndex` | `number` | The index of the audio track to extract (0-based). |
| `options` | `AudioFromVideoOptions` | Options for the audio extraction operation. |

#### Returns[#](#returns-356)

`number`

The handle of the newly created audio block with extracted audio from the specified track.

#### Throws[#](#throws-2)

Will throw an error if the track index is invalid or the block has no audio.

#### Signature[#](#signature-297)

```
createAudioFromVideo(videoFillBlock: number, trackIndex: number, options?: AudioFromVideoOptions): number
```

* * *

### createAudiosFromVideo()[#](#createaudiosfromvideo)

  

Creates multiple audio blocks by extracting all audio tracks from a video fill block.

```
// Extract all audio tracks from a video with trim settingsconst audioBlocks = engine.block.createAudiosFromVideo(videoFillBlock);console.log(`Created ${audioBlocks.length} audio blocks`);
// Extract all tracks without trim settings (full audio)const audioBlocks = engine.block.createAudiosFromVideo(videoFillBlock, { keepTrimSettings: false });
// Extract all tracks with trim settings and mute the original videoconst audioBlocks = engine.block.createAudiosFromVideo(videoFillBlock, { keepTrimSettings: true, muteOriginalVideo: true });
```

#### Parameters[#](#parameters-348)

| Parameter | Type | Description |
| --- | --- | --- |
| `videoFillBlock` | `number` | The video fill block to extract audio from. |
| `options` | `AudioFromVideoOptions` | Options for the audio extraction operation. |

#### Returns[#](#returns-357)

`number`\[\]

An array of handles for the newly created audio blocks, one per track.

#### Throws[#](#throws-3)

Will throw an error if the block has no audio or extraction fails.

#### Signature[#](#signature-298)

```
createAudiosFromVideo(videoFillBlock: number, options?: AudioFromVideoOptions): number[]
```

* * *

### getAudioInfoFromVideo()[#](#getaudioinfofromvideo)

  

Gets information about all audio tracks from a video fill block.

```
// Get information about all audio tracksconst trackInfos = engine.block.getAudioInfoFromVideo(videoFillBlock);console.log(`Video has ${trackInfos.length} audio tracks`);
// Display track informationtrackInfos.forEach((track, index) => {  console.log(`Track ${index}: ${track.channels} channels, ${track.sampleRate}Hz, ${track.language}`);});
// Use track info to create audio blocks selectivelyconst englishTracks = trackInfos.filter(track => track.language === 'eng');const audioBlocks = englishTracks.map(track =>  engine.block.createAudioFromVideo(videoFillBlock, track.trackIndex));
```

#### Parameters[#](#parameters-349)

| Parameter | Type | Description |
| --- | --- | --- |
| `videoFillBlock` | `number` | The video fill block to analyze for audio track information. |

#### Returns[#](#returns-358)

`AudioTrackInfo`\[\]

An array containing information about each audio track.

#### Throws[#](#throws-4)

Will throw an error if the block is not a video fill or has no audio.

#### Signature[#](#signature-299)

```
getAudioInfoFromVideo(videoFillBlock: number): AudioTrackInfo[]
```

## Block Metadata[#](#block-metadata)

### setMetadata()[#](#setmetadata)

  

Sets a metadata value for a given key on a block.

If the key does not exist, it will be added.

#### Parameters[#](#parameters-350)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose metadata will be accessed. |
| `key` | `string` | The key used to identify the desired piece of metadata. |
| `value` | `string` | The value to set. |

#### Returns[#](#returns-359)

`void`

#### Signature[#](#signature-300)

```
setMetadata(id: number, key: string, value: string): void
```

* * *

### getMetadata()[#](#getmetadata)

  

Gets a metadata value for a given key from a block.

#### Parameters[#](#parameters-351)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose metadata will be accessed. |
| `key` | `string` | The key used to identify the desired piece of metadata. |

#### Returns[#](#returns-360)

`string`

The value associated with the key.

#### Signature[#](#signature-301)

```
getMetadata(id: number, key: string): string
```

* * *

### hasMetadata()[#](#hasmetadata)

  

Checks if a block has metadata for a given key.

#### Parameters[#](#parameters-352)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose metadata will be accessed. |
| `key` | `string` | The key used to identify the desired piece of metadata. |

#### Returns[#](#returns-361)

`boolean`

Whether the key exists.

#### Signature[#](#signature-302)

```
hasMetadata(id: number, key: string): boolean
```

* * *

### findAllMetadata()[#](#findallmetadata)

  

Finds all metadata keys on a block.

#### Parameters[#](#parameters-353)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose metadata will be accessed. |

#### Returns[#](#returns-362)

`string`\[\]

A list of all metadata keys on this block.

#### Signature[#](#signature-303)

```
findAllMetadata(id: number): string[]
```

* * *

### removeMetadata()[#](#removemetadata)

  

Removes metadata for a given key from a block.

#### Parameters[#](#parameters-354)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block whose metadata will be accessed. |
| `key` | `string` | The key used to identify the desired piece of metadata. |

#### Returns[#](#returns-363)

`void`

#### Signature[#](#signature-304)

```
removeMetadata(id: number, key: string): void
```

## Helper[#](#helper)

Convenient high-level functions that combine multiple operations into single, easy-to-use methods for common tasks like adding media, applying effects, and positioning blocks.

### setSize()[#](#setsize)

  

Update a block’s size.

#### Parameters[#](#parameters-355)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `width` | `number` | The new width of the block. |
| `height` | `number` | The new height of the block. |
| `options?` | { `maintainCrop?`: `boolean`; `sizeMode?`: [`SizeMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sizemode/); } | Optional parameters for the size. Properties: - `maintainCrop` - Whether or not the crop values, if available, should be automatically adjusted. - `sizeMode` - The size mode: Absolute, Percent or Auto. |
| `options.maintainCrop?` | `boolean` | \- |
| `options.sizeMode?` | [`SizeMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sizemode/) | \- |

#### Returns[#](#returns-364)

`void`

#### Signature[#](#signature-305)

```
setSize(id: number, width: number, height: number, options?: object): void
```

* * *

### setPosition()[#](#setposition)

  

Update a block’s position.

#### Parameters[#](#parameters-356)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `x` | `number` | The new x position of the block. |
| `y` | `number` | The new y position of the block. |
| `options?` | { `positionMode?`: [`PositionMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/positionmode/); } | Optional parameters for the position. Properties: - `positionMode` - The position mode: absolute, percent or undefined. |
| `options.positionMode?` | [`PositionMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/positionmode/) | \- |

#### Returns[#](#returns-365)

`void`

#### Signature[#](#signature-306)

```
setPosition(id: number, x: number, y: number, options?: object): void
```

* * *

### addImage()[#](#addimage)

  

Adds an image to the current page. The image will be automatically loaded and sized appropriately. In Video mode, timeline and animation options can be applied.

#### Parameters[#](#parameters-357)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | URL or path to the image file |
| `options` | [`AddImageOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/addimageoptions/) | Configuration options for the image |

#### Returns[#](#returns-366)

`Promise`<`number`\>

Promise that resolves to the ID of the created image block

#### Throws[#](#throws-5)

Error if no current page exists

#### Signature[#](#signature-307)

```
addImage(url: string, options?: AddImageOptions): Promise<number>
```

* * *

### addVideo()[#](#addvideo)

  

Adds a video block to the current scene page. The video will be positioned and sized according to the provided parameters. Timeline and animation effects can be applied. Only works in Video mode, not in Design mode.

#### Parameters[#](#parameters-358)

| Parameter | Type | Description |
| --- | --- | --- |
| `url` | `string` | URL or path to the video file |
| `width` | `number` | Width of the video in scene design units |
| `height` | `number` | Height of the video in scene design units |
| `options` | [`AddVideoOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/addvideooptions/) | Configuration options for the video |

#### Returns[#](#returns-367)

`Promise`<`number`\>

Promise that resolves to the ID of the created video block

#### Throws[#](#throws-6)

Error if called in Design mode or if no current page exists

#### Signature[#](#signature-308)

```
addVideo(url: string, width: number, height: number, options?: AddVideoOptions): Promise<number>
```

* * *

### applyAnimation()[#](#applyanimation)

  

Applies an animation to a block.

#### Parameters[#](#parameters-359)

| Parameter | Type | Description |
| --- | --- | --- |
| `block` | `number` | The ID of the block to apply the animation to |
| `animation` | [`AnimationOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationoptions/) | The animation configuration options |

#### Returns[#](#returns-368)

`void`

#### Signature[#](#signature-309)

```
applyAnimation(block: number, animation?: AnimationOptions): void
```

* * *

### applyDropShadow()[#](#applydropshadow)

  

Applies a drop shadow effect to any block.

#### Parameters[#](#parameters-360)

| Parameter | Type | Description |
| --- | --- | --- |
| `block` | `number` | The ID of the block to apply the shadow to |
| `options` | [`DropShadowOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dropshadowoptions/) | Shadow configuration options. If not provided, enables shadow with default settings |

#### Returns[#](#returns-369)

`void`

#### Signature[#](#signature-310)

```
applyDropShadow(block: number, options?: DropShadowOptions): void
```

* * *

### generateThumbnailAtTimeOffset()[#](#generatethumbnailattimeoffset)

  

Generates a thumbnail image of the scene at a specific time. Only works in Video mode, not in Design mode.

#### Parameters[#](#parameters-361)

| Parameter | Type | Description |
| --- | --- | --- |
| `height` | `number` | Height of the thumbnail in scene design units (maximum 512) |
| `time` | `number` | Time position in seconds to capture the thumbnail |

#### Returns[#](#returns-370)

`Promise`<`Blob`\>

Promise that resolves to a Blob containing the PNG thumbnail image

#### Throws[#](#throws-7)

Error if no page exists, if called in Design mode, or if height exceeds 512 pixels

#### Signature[#](#signature-311)

```
generateThumbnailAtTimeOffset(height: number, time: number): Promise<Blob>
```

* * *

### getBackgroundTrack()[#](#getbackgroundtrack)

  

Gets the background track of the current scene. The background track is the track that determines the page duration. Only works in Video mode, not in Design mode.

#### Returns[#](#returns-371)

`number`

The ID of the background track, or null if none exists

#### Throws[#](#throws-8)

Error if called in Design mode

#### Signature[#](#signature-312)

```
getBackgroundTrack(): number
```

* * *

### moveToBackgroundTrack()[#](#movetobackgroundtrack)

  

Moves a block to the background track. This is useful for organizing content in video scenes where you want certain elements to be part of the background layer. The background track is the track that determines the page duration. If no background track exists, one will be created automatically.

#### Parameters[#](#parameters-362)

| Parameter | Type | Description |
| --- | --- | --- |
| `block` | `number` | The ID of the block to move to the background track |

#### Returns[#](#returns-372)

`void`

#### Signature[#](#signature-313)

```
moveToBackgroundTrack(block: number): void
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/classes/assetapi)