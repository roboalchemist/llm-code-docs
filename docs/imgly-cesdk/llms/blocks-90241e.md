# Source: https://img.ly/docs/cesdk/android/concepts/blocks-90241e/

---
title: "Blocks"
description: "Learn how blocks define elements in a scene and how to structure them for rendering in CE.SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/blocks-90241e/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Blocks](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/)

---

## Lifecycle

Only blocks that are direct or indirect children of a `page` block are rendered. Scenes without any `page` child may not be properly displayed by the CE.SDK editor.

### Functions

```kotlin
fun create(blockType: DesignBlockType): DesignBlock
```

Create a new block.

- `blockType`: the type of the block that shall be created.
- Returns the created blocks handle.

To create a scene, use [](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) instead.

```kotlin
suspend fun saveToString(
    blocks: List<DesignBlock>,
    allowedResourceSchemes: List<String> = listOf("bundle", "file", "http", "https"),
): String
```

Saves the given blocks to a proprietary string. If a resource uri has a scheme that is not in `allowedResourceSchemes`,

an exception will be thrown.

Note: All given block handles must be valid, otherwise an exception will be thrown.

- `blocks`: the blocks to save.
- `allowedResourceSchemes`: the list of allowed resource schemes in the scene.
- Returns a string representation of the blocks.

```kotlin
suspend fun saveToArchive(blocks: List<DesignBlock>): ByteBuffer
```

Saves the given blocks to an archive.

Note: All given block handles must be valid, otherwise this call returns an error.

- `blocks`: the blocks to save.
- Returns a string representation of the blocks.

```kotlin
suspend fun loadFromString(block: String): List<DesignBlock>
```

Loads existing blocks from the given string.

The blocks are not attached by default and won't be visible until attached to a page or the scene.

The UUID of the loaded blocks is replaced with a new one.

- `block`: a string representing the given blocks.
- Returns a list of loaded blocks.

```kotlin
suspend fun loadFromURL(url: Uri): List<DesignBlock>
```

Loads existing blocks from a URL.

The URL should point to a blocks file within an unzipped archive directory previously saved with `saveToArchive`.

The blocks are not attached by default and won't be visible until attached to a page or the scene.

The UUID of the loaded blocks is replaced with a new one.

- `url`: the URL to the blocks.blocks file.
- Returns a list of loaded blocks.

```kotlin
suspend fun loadFromArchive(archiveUri: Uri): List<DesignBlock>
```

Loads existing blocks from an archive.

The blocks are not attached by default and won't be visible until attached to a page or the scene.

The UUID of the loaded blocks is replaced with a new one.

- `archiveUri`: the uri of the blocks archive file.
- Returns a list of loaded blocks.

```kotlin
fun getType(block: DesignBlock): String
```

Get the type of the given block, fails if the block is invalid.

- `block`: the block to query.
- Returns the block type.

```kotlin
fun setName(
    block: DesignBlock,
    name: String,
)
```

Update a block's name.

- `block`: the block to update.
- `name`: the name to set.

```kotlin
fun getName(block: DesignBlock): String
```

Get a block's name.

- `block:`: The block to query.
- Returns The block's name.

```kotlin
fun duplicate(block: DesignBlock): DesignBlock
```

Duplicates a block including its children.

Required scope: "lifecycle/duplicate"

If the block is parented to a track that is set always-on-bottom, the duplicate is inserted in the same track

immediately after the block. Otherwise, the duplicate is moved up in the hierarchy.

- `block`: the block to duplicate.
- Returns the handle of the duplicate.

```kotlin
fun destroy(block: DesignBlock)
```

Destroys a block.

Required scope: "lifecycle/destroy"

- `block`: the block to destroy.

```kotlin
fun isValid(block: DesignBlock): Boolean
```

Check if a block is valid. A block becomes invalid once it has been destroyed.

- `block`: the block to query.
- Returns true if the block is valid, false otherwise.

### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes through the `block` Api.

```kotlin
// Create, save and load blocks
val block = engine.block.create(DesignBlockType.Graphic)
val savedBlocksString = engine.block.saveToString(blocks = listOf(block))
val loadedBlocksString = engine.block.loadFromString(savedBlocksString)
val savedBlocksArchive = engine.block.saveToArchive(blocks = listOf(block))
val loadedBlocksArchive = engine.block.loadFromArchive(blocksUri = Uri.parse("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1_blocks.zip"))
// Load blocks from an extracted zip file created with block.saveToArchive
val loadedBlocksURL = engine.block.loadFromURL(url = Uri.parse("https://cdn.img.ly/assets/v6/ly.img.text.components/box/blocks.blocks"))

// Check a blocks type
val blockType = engine.block.getType(block)

// Alter a blocks name
engine.block.setName(block, name = "someName")
val name = engine.block.getName(block)

// You may duplicate or destroy blocks
val duplicate = engine.block.duplicate(block)
engine.block.destroy(duplicate)
engine.block.isValid(duplicate) // false
```

## Properties

### UUID

A universally unique identifier (UUID) is assigned to each block upon creation and can be queried. This is stable across save & load and may be used to reference blocks.

```kotlin
fun getUUID(block: DesignBlock): String
```

Get a block's unique identifier.

- `block:`: The block to query.
- Returns The block's UUID.

### Reflection

For every block, you can get a list of all its properties by calling `findAllProperties`. Properties specific to a block are prefixed with the block's type followed by a forward slash. There are also common properties shared between blocks which are prefixed by their respective type. A list of all properties can be found in the [Blocks Overview](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

```kotlin
fun findAllProperties(block: DesignBlock): List<String>
```

Get all available properties of a block.

- `block`: the block whose properties should be queried.
- Returns a list of the property names.

Given a property you can query its type using `getPropertyType`.

```kotlin
fun getPropertyType(property: String): PropertyType
```

Get the type of a property given its name.

- `property`: the name of the property whose type should be queried.
- Returns the property type.

To get a list of possible values for an enum property call `getEnumValues(enumProperty: string): string[]`.

```kotlin
fun getEnumValues(enumProperty: String): List<String>
```

Get all the possible values of an enum given an enum property.

- `enumProperty`: the name of the property whose enum values should be queried.
- Returns a list of the enum value names as string.

Some properties can only be written to or only be read.
To find out what is possible with a property, you can use the `isPropertyReadable` and `isPropertyWritable` methods.

```kotlin
fun isPropertyReadable(property: String): Boolean
```

Check if a property with a given name is readable.

- `property`: the name of the property whose type should be queried.
- Returns whether the property is readable or not. Will return false for unknown properties.

```kotlin
fun isPropertyWritable(property: String): Boolean
```

Check if a property with a given name is writeable.

- `property`: the name of the property whose type should be queried.
- Returns whether the property is writeable or not. Will return false for unknown properties.

### Generic Properties

There are dedicated setter and getter functions for each property type. You have to provide a block and the property path. Use `findAllProperties` to get a list of all the available properties a block has.

> **Note:** Please make sure you call the setter and getter function matching the type of
> the property you want to set or query or else you will get an error. Use
> `getType` to figure out the pair of functions you need to use.

```kotlin
fun findAllProperties(block: DesignBlock): List<String>
```

Get all available properties of a block.

- `block`: the block whose properties should be queried.
- Returns a list of the property names.

```kotlin
fun setBoolean(
    block: DesignBlock,
    property: String,
    value: Boolean,
)
```

Set a boolean property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getBoolean(
    block: DesignBlock,
    property: String,
): Boolean
```

Get the value of a boolean property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setInt(
    block: DesignBlock,
    property: String,
    value: Int,
)
```

Set an int property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getInt(
    block: DesignBlock,
    property: String,
): Int
```

Get the value of an int property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setFloat(
    block: DesignBlock,
    property: String,
    value: Float,
)
```

Set a float property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getFloat(
    block: DesignBlock,
    property: String,
): Float
```

Get the value of a float property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setDouble(
    block: DesignBlock,
    property: String,
    value: Double,
)
```

Set a double property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getDouble(
    block: DesignBlock,
    property: String,
): Double
```

Get the value of a double property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setString(
    block: DesignBlock,
    property: String,
    value: String,
)
```

Set a string property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getString(
    block: DesignBlock,
    property: String,
): String
```

Get the value of a string property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setColor(
    block: DesignBlock,
    property: String,
    value: Color,
)
```

Set a color property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getColor(
    block: DesignBlock,
    property: String,
): Color
```

Get the value of a color property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to set.
- Returns the value of the property.

```kotlin
fun setEnum(
    block: DesignBlock,
    property: String,
    value: String,
)
```

Set an enum property of the given design block to the given value.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `value`: the value to set.

```kotlin
fun getEnum(
    block: DesignBlock,
    property: String,
): String
```

Get the value of an enum property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to get.
- Returns the value of the property.

```kotlin
fun setGradientColorStops(
    block: DesignBlock,
    property: String,
    colorStops: List<GradientColorStop>,
)
```

Set a gradient color stops property of the given design block.

- `block`: the block whose property should be set.
- `property`: the name of the property to set.
- `colorStops`: the list of color stops.

```kotlin
fun getGradientColorStops(
    block: DesignBlock,
    property: String,
): List<GradientColorStop>
```

Get the gradient color stops property of the given design block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to query.
- Returns the list of gradient color stops.

```kotlin
fun setSourceSet(
    block: DesignBlock,
    property: String,
    sourceSet: List<Source>,
)
```

Set the source set of a source set property of the given block.

The crop and content fill mode of the associated block will be set to the default values.

- `block`: the block whose source set should be set.
- `property`: the name of the property to set.
- `sourceSet`: the new source set.

```kotlin
fun getSourceSet(
    block: DesignBlock,
    property: String,
): List<Source>
```

Returns the source set of a source set property of the given block.

- `block`: the block whose property should be queried.
- `property`: the name of the property to get.
- Returns the source set of the given block.

```kotlin
suspend fun addImageFileUriToSourceSet(
    block: DesignBlock,
    property: String,
    uri: String,
)
```

Add a source to the `sourceSet` property of the given block. If there already exists in source set an image with the same width, that existing image will be replaced. If the source set is or gets empty, the crop and content fill mode of the associated block will be set to the default values.

Note: This fetches the resource from the given URI to obtain the image dimensions. It is recommended to use setSourceSet if the dimension is known.

- `block`: the block to update.
- `property`: the name of the property to modify.
- `uri`: the source to add to the source set.

```kotlin
suspend fun addVideoFileUriToSourceSet(
    block: DesignBlock,
    property: String,
    uri: String,
)
```

Add a source to the `sourceSet` property of the given block. If there already exists in source set a video with the same width, that existing video will be replaced. If the source set is or gets empty, the crop and content fill mode of the associated block will be set to the default values.

Note: This fetches the resource from the given URI to obtain the video dimensions. It is recommended to use setSourceSet if the dimension is known.

- `block`: the block to update.
- `property`: the name of the property to modify.
- `uri`: the source to add to the source set.

### Modifying Properties

Here’s the full code snippet for modifying a block’s properties:

```kotlin
val uuid = engine.block.getUUID(block)
val propertyNamesStar = engine.block
	.findAllProperties(starShape) // List [ "shape/star/innerDiameter", "shape/star/points", "opacity/value", ... ]
val propertyNamesImage = engine.block
	.findAllProperties(imageFill) // List [ "fill/image/imageFileURI", "fill/image/previewFileURI", "fill/image/externalReference", ... ]
val propertyNamesText = engine.block
	.findAllProperties(text) // List [ "text/text", "text/fontFileUri", "text/externalReference", "text/fontSize", "text/horizontalAlignment", ... ]

val pointsType = engine.block.getPropertyType(property = "shape/star/points") // "Int"
val alignmentType = engine.block.getPropertyType(property = "text/horizontalAlignment") // "Enum"
engine.block.getEnumValues(enumProperty = "text/horizontalAlignment")
val readable = engine.block.isPropertyReadable("shape/star/points")
val writable = engine.block.isPropertyWritable("shape/star/points")

// Generic Properties
engine.block.setBoolean(scene, property = "scene/aspectRatioLock", value = false)
engine.block.getBoolean(scene, property = "scene/aspectRatioLock")
engine.block.setInt(star, property = "shape/star/points", value = points + 2)
val points = engine.block.getInt(star, property = "shape/star/points")
engine.block.setFloat(star, property = "shape/star/innerDiameter", value = 0.75F)
engine.block.getFloat(star, property = "shape/star/innerDiameter")
val audio = engine.block.create(DesignBlockType.Audio)
engine.block.appendChild(scene, audio)
engine.block.setDouble(audio, property = "playback/duration", value = 1.0)
engine.block.getDouble(audio, property = "playback/duration")
engine.block.setString(text, property = "text/text", value = "*o*")
engine.block.setString(
	imageFill,
	property = "fill/image/imageFileURI",
	value =  "https://img.ly/static/ubq_samples/sample_4.jpg"
)
engine.block.getString(text, property = "text/text")
engine.block.getString(imageFill, property = "fill/image/imageFileURI")
engine.block.setColor(
	colorFill,
	property = "fill/color/value",
	value = Color.fromString("#FFFFFFFF")
) // White
engine.block.getColor(colorFill, property = "fill/color/value")
engine.block.setEnum(text, property = "text/horizontalAlignment", value = "Center")
engine.block.setEnum(text, property = "text/verticalAlignment", value = "Center")
engine.block.getEnum(text, property = "text/horizontalAlignment")
engine.block.getEnum(text, property = "text/verticalAlignment")
engine.block.setGradientColorStops(
    block = gradientFill,
    property = "fill/gradient/colors",
    colorStops = listOf(
        GradientColorStop(stop = 0F, color = Color.fromRGBA(r = 0.1F, g = 0.2F, b = 0.3F, a = 0.4F)),
        GradientColorStop(stop = 1F, color = Color.fromSpotColor("test"))
    )
)
engine.block.getGradientColorStops(block = gradientFill, property = "fill/gradient/colors")

val imageFill = engine.block.createFill(FillType.Image)
engine.block.setSourceSet(
        block = imageFill,
        property = "fill/image/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("http://img.ly/my-image.png"),
                width = 800,
                height = 600
            )
        )
    )
engine.block.getSourceSet(block = imageFill, property = "fill/image/sourceSet")
engine.block.addImageFileUriToSourceSet(block = imageFill, property = "fill/image/sourceSet", uri = "https://img.ly/static/ubq_samples/sample_1.jpg");
val videoFill = engine.block.createFill(FillType.Video)
engine.block.addVideoFileUriToSourceSet(block = videoFill, property = "fill/video/sourceSet", uri = "https://img.ly/static/example-assets/sourceset/1x.mp4");
```

### Kind Property

The `kind` of a design block is a custom string that can be assigned to a block in order to categorize it and distinguish it from other blocks that have the same type. The user interface can then customize its appearance based on the kind of the selected blocks. It can also be used for automation use cases in order to process blocks in a different way based on their kind.

```kotlin
fun setKind(
    block: DesignBlock,
    kind: String,
)
```

Set the kind of the given block, fails if the block is invalid.

- `block`: the block to modify.
- `kind`: the block kind.

```kotlin
fun getKind(block: DesignBlock): String
```

Get the kind of the given block, fails if the block is invalid.

- `block`: the block to query.
- Returns the block kind.

```kotlin
fun findByKind(blockKind: String): List<DesignBlock>
```

Finds all blocks with the given kind.

- `blockKind`: the kind to search for.
- Returns a list of block ids.

#### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify a and query the kind property of design blocks through the `block` API.

```kotlin
engine.block.setKind(text, kind = "title")
val kind = engine.block.getKind(text)
val allTitles = engine.block.findByKind(blockKind = "title")
```

## Selection & Visibility

A block can potentially be *invisible* (in the sense that you can't see it), even though
`isVisible()` returns true. This could be the case when a block has not been
added to a parent, the parent itself is not visible, or the block is obscured by another block on top of it.

### Select blocks and change their visibility

```kotlin
fun setSelected(
    block: DesignBlock,
    selected: Boolean,
)
```

Update the selection state of a block. Fails for invalid blocks. Note: Previously selected blocks remain selected. Required scope: "editor/select"

- `block`: the block to query.
- `selected`: whether or not the block should be selected.

```kotlin
fun isSelected(block: DesignBlock): Boolean
```

Get the selected state of a block.

- `block`: the block to query.
- Returns true if the block is selected, false otherwise.

```kotlin
fun select(block: DesignBlock)
```

Selects the given block and deselects all other blocks.

- `block`: the block to be selected.

```kotlin
fun findAllSelected(): List<DesignBlock>
```

Get all currently selected blocks.

- Returns An array of block ids.

```kotlin
fun setVisible(
    block: DesignBlock,
    visible: Boolean,
)
```

Update a block's visibility.

Required scope: "layer/visibility"

- `block`: the block to update.
- `visible`: whether the block shall be visible.

```kotlin
fun isVisible(block: DesignBlock): Boolean
```

Query a block's visibility.

- `block`: the block to query.
- Returns true if visible, false otherwise.

```kotlin
fun setClipped(
    block: DesignBlock,
    clipped: Boolean,
)
```

Update a block's clipped state.

Required scope: "layer/clipping"

- `block`: the block to update.
- `clipped`: whether the block should clips its contents to its frame.

```kotlin
fun isClipped(block: DesignBlock): Boolean
```

Query a block's clipped state. If `true`, the block should clip

- `block`: the block to query.
- Returns true if clipped, false otherwise.

```kotlin
fun onSelectionChanged(): Flow<Unit>
```

Subscribe to changes in the current set of selected blocks.

- Returns flow of selected block change events.

```kotlin
fun onClicked(): Flow<DesignBlock>
```

Subscribe to block click events.

Note: `DesignBlock` is emitted at the end of the engine update if it has been clicked.

- Returns flow of block click events.

```kotlin
fun isIncludedInExport(block: DesignBlock): Boolean
```

Query if the given block is included on the exported result.

- `block`: the block to query if it's included on the exported result.
- Returns true, if the block is included on the exported result, false otherwise.

```kotlin
fun setIncludedInExport(
    block: DesignBlock,
    enabled: Boolean,
)
```

Set if you want the given design block to be included in exported result.

- `block`: the block whose exportable state should be set.
- `enabled`: if true, the block will be included on the exported result.

### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes through the `block` API.

```kotlin
engine.block.setSelected(block, selected = true)
val isSelected = engine.block.isSelected(block)
engine.block.select(block)
val selectedIds = engine.block.findAllSelected()

val isVisible = engine.block.isVisible(block)
engine.block.setVisible(block, visible = true)

val isClipped = engine.block.isClipped(page)
engine.block.setClipped(page, clipped = true)

val coroutineScope = CoroutineScope(Dispatchers.Main)
engine.block.onSelectionChanged()
    .onEach {
        println("Change in the set of selected blocks")
    }
    .launchIn(coroutineScope)
engine.block.onClicked()
    .onEach {
        println("Block $it was clicked")
    }
    .launchIn(coroutineScope)

val isIncludedInExport = engine.block.isIncludedInExport(block)
engine.block.setIncludedInExport(block, enabled = true)
```

## State

Blocks can perform operations that take some time or that can end in bad results.
When that happens, blocks put themselves in a pending state or an error state and visual feedback is shown pertaining to the state.
When an external operation is done to blocks, for example with a plugin, you may want to manually set the block's state to pending (if that external operation takes time) or to error (if that operation resulted in an error).

The possible states of a block are:

```
data object Ready : BlockState

data class Pending(
    @FloatRange(from = 0.0, to = 1.0) val progress: Float
) : BlockState

data class Error(val type: Type) : BlockState {
    enum class Type {
        AUDIO_DECODING, // Failed to decode the block's audio stream.
        IMAGE_DECODING, // Failed to decode the block's image stream.
        FILE_FETCH, // Failed to retrieve the block's remote content.
        UNKNOWN, // An unknown error occurred.
        VIDEO_DECODING // Failed to decode the block's video stream.
    }
}
```

When calling `getState`, the returned state reflects the combined state of a block, the block's fill, the block's shape and the block's effects.
If any of these blocks is in an `Error` state, the returned state will reflect that error.
If none of these blocks is in error state but any is in `Pending` state, the returned state will reflect the aggregate progress of the block's progress.
If none of the blocks are in error state or pending state, the returned state is `Ready`.

```kotlin
fun getState(block: DesignBlock): BlockState
```

Get the current state of a block.

Note If this block is in error state or this block has a `Shape` block, `Fill` block or `Effect` block(s), that
is in error state, the returned state will be `BlockState.Error`.

Else, if this block is in pending state or this block has a `Shape` block, `Fill` block or `Effect` block(s), that
is in pending state, the returned state will be `BlockState.Pending`.

Else, the returned state will be `BlockState.Ready`.

- `block`: the block whose state should be queried.
- Returns the state of the block.

```kotlin
fun setState(
    block: DesignBlock,
    state: BlockState,
)
```

Set the state of a block.

- `block`: the block whose state should be set.
- `state`: the new state to set.

```kotlin
fun onStateChanged(blocks: List<DesignBlock>): Flow<List<DesignBlock>>
```

Subscribe to changes to the state of a block. Like `getState`, the state of a block is determined by the state of itself and its `Shape`, `Fill` and `Effect` block(s).

- `blocks`: a list of blocks to filter events by. If the list is empty, events for every block are sent.
- Returns flow of block state change events.

### Full Code

In this example, we will show you how to use [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to retrieve's a block's state and to manually set a block in a pending state, an error state or back to a ready state.

```kotlin
engine.block.onStateChanged(listOf(block))
    .onEach { println("State of blocks $it is updated.") }
    .launchIn(CoroutineScope(Dispatchers.Main))
val state = engine.block.getState(block)
engine.block.setState(block, state = BlockState.Pending(progress = 0.5F))
engine.block.setState(block, state = BlockState.Ready)
engine.block.setState(block, state = BlockState.Error(BlockState.Error.Type.IMAGE_DECODING))
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
