# Source: https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/

---
title: "Blocks"
description: "Learn how blocks define elements in a scene and how to structure them for rendering in CE.SDK."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/mac-catalyst/concepts-c9ff51/) > [Blocks](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/)

---

## Lifecycle

Only blocks that are direct or indirect children of a `page` block are rendered. Scenes without any `page` child may not be properly displayed by the CE.SDK editor.

## Functions

```swift
public func create(_ type: DesignBlockType) throws -> DesignBlockID
```

Create a new block.

- `type:`: The type of the block that shall be created.
- Returns: The created blocks handle.

To create a scene, use [](https://img.ly/docs/cesdk/mac-catalyst/open-the-editor-23a1db/) instead.

```swift
public func saveToString(blocks: [DesignBlockID], allowedResourceSchemes: [String] = ["bundle", "file", "http", "https"]) async throws -> String
```

Saves the given blocks into a string. If given the root of a block hierarchy, e.g. a
page with multiple children, the entire hierarchy is saved.

- `blocks`: The blocks to save.
- `allowedResourceSchemes`: If a resource URL has a scheme that is not in this list an error will be thrown.
- Returns: A string representation of the blocks.

```swift
public func saveToArchive(blocks: [DesignBlockID]) async throws -> Blob
```

Saves the given blocks and all of their referenced assets into an archive.
The archive contains all assets that were accessible when this function was called.
Blocks in the archived scene reference assets relative from to the location of the scene
file. These references are resolved when loading such a scene via `scene.load(from url:)`.

- `blocks:`: The blocks to save.
- Returns: A serialized scene data blob.

```swift
public func load(from string: String) async throws -> [DesignBlockID]
```

Loads existing blocks from the given string.
The blocks are not attached by default and won't be visible until attached to a page or the scene.
The UUID of the loaded blocks is replaced with a new one.

- `string:`: A string representing the given blocks.
- Returns: A list of loaded blocks.

```swift
public func load(from url: URL) async throws -> [DesignBlockID]
```

Loads existing blocks from a URL.
The URL should point to a blocks file within an unzipped archive directory previously saved with
`block.saveToArchive`.
The blocks are not attached by default and won't be visible until attached to a page or the scene.
The UUID of the loaded blocks is replaced with a new one.

- `url:`: The URL to the blocks file.
- Returns: A list of loaded blocks.

```swift
public func loadArchive(from url: URL) async throws -> [DesignBlockID]
```

Loads existing blocks from an archive.
The blocks are not attached by default and won't be visible until attached to a page or the scene.
The UUID of the loaded blocks is replaced with a new one.

- `url:`: The URL of the blocks archive file.
- Returns: A list of loaded blocks.

```swift
public func getType(_ id: DesignBlockID) throws -> String
```

Get the type of the given block, fails if the block is invalid.

- `id:`: The block to query.
- Returns: The blocks type.

```swift
public func setName(_ id: DesignBlockID, name: String) throws
```

Update a block's name.

- `id`: The block to update.
- `name`: The name to set.

```swift
public func getName(_ id: DesignBlockID) throws -> String
```

Get a block's name.

- `id:`: The block to query.
- Returns: The block's name.

```swift
public func duplicate(_ id: DesignBlockID) throws -> DesignBlockID
```

Duplicates a block including its children.
Required scope: "lifecycle/duplicate"
If the block is parented to a track that is set always-on-bottom, the duplicate is inserted in the same track
immediately after the block. Otherwise, the duplicate is moved up in the hierarchy.

- `id:`: The block to duplicate.
- Returns: The handle of the duplicate.

```swift
public func destroy(_ id: DesignBlockID) throws
```

Destroys a block.
Required scope: "lifecycle/destroy"

- `id:`: The block to destroy.

```swift
public func isValid(_ id: DesignBlockID) -> Bool
```

Check if a block is valid. A block becomes invalid once it has been destroyed.

- `id:`: The block to query.
- Returns: `true`, if the block is valid.

### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes through the `block` API.

```swift

// Create, save and load blocks
let block = try engine.block.create(.graphic)
let savedBlocksString = try await engine.block.saveToString(blocks: [block])
let loadedBlocksString = try await engine.block.load(from: savedBlocksString)
let savedBlocksArchive = try await engine.block.saveToArchive(blocks: [block])
let loadedBlocksArchive = try await engine.block.loadArchive(from: .init(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1_blocks.zip")!)
// Load blocks from an extracted zip file created with block.saveToArchive
let loadedBlocksURL = try await engine.block.load(from: URL(string: "https://cdn.img.ly/assets/v6/ly.img.text.components/box/blocks.blocks")!)

// Check a blocks type
let blockType = try engine.block.getType(block)

// Alter a blocks name
try engine.block.setName(block, name: "someName")
let name = try engine.block.getName(block)

// You may duplicate or destroy blocks
let duplicate = try engine.block.duplicate(block)
try engine.block.destroy(duplicate)
engine.block.isValid(duplicate) // false
```

## Properties

### UUID

A universally unique identifier (UUID) is assigned to each block upon creation and can be queried. This is stable across save & load and may be used to reference blocks.

```swift
public func getUUID(_ id: DesignBlockID) throws -> String
```

Get a block's unique identifier.

- `id:`: The block to query.
- Returns: The block's UUID.

### Reflection

For every block, you can get a list of all its properties by calling `findAllProperties(id: number): string[]`. Properties specific to a block are prefixed with the block's type followed by a forward slash. There are also common properties shared between blocks which are prefixed by their respective type. A list of all properties can be found in the [Blocks Overview](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/).

```swift
public func findAllProperties(_ id: DesignBlockID) throws -> [String]
```

Get all available properties of a block.

- `id:`: The block whose properties should be queried.
- Returns: A list of the property names.

Given a property, you can query its type using `getType(ofProperty:)`.

```swift
public func getType(ofProperty property: String) throws -> PropertyType
```

Get the type of a property given its name.

- `property:`: The name of the property whose type should be queried.
- Returns: The property type.

The property type `'Enum'` is a special type. Properties of this type only accept a set of certain strings. To get a list of possible values for an enum property call `getEnumValues(enumProperty: string): string[]`.

```swift
public func getEnumValues(ofProperty enumProperty: String) throws -> [String]
```

Get all the possible values of an enum given an enum property.

- `enumProperty:`: The name of the property whose enum values should be queried.
- Returns: A list of the enum value names as string.

Some properties can only be written to or only be read.
To find out what is possible with a property, you can use the `isPropertyReadable` and `isPropertyWritable` methods.

```swift
public func isPropertyReadable(property: String) throws -> Bool
```

Check if a property with a given name is readable.

- `property:`: The name of the property whose type should be queried.
- Returns: Whether the property is readable or not. Will return false for unknown properties.

```swift
public func isPropertyWritable(property: String) throws -> Bool
```

Check if a property with a given name is writable.

- `property:`: The name of the property whose type should be queried.
- Returns: Whether the property is writable or not. Will return false for unknown properties.

### Generic Properties

There are dedicated setter and getter functions for each property type. You have to provide a block and the property path. Use `findAllProperties` to get a list of all the available properties a block has.

> **Note:** Please make sure you call the setter and getter function matching the type of
> the property you want to set or query or else you will get an error. Use
> `getType` to figure out the pair of functions you need to use.

```swift
public func findAllProperties(_ id: DesignBlockID) throws -> [String]
```

Get all available properties of a block.

- `id:`: The block whose properties should be queried.
- Returns: A list of the property names.

```swift
public func setBool(_ id: DesignBlockID, property: String, value: Bool) throws
```

Set a bool property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getBool(_ id: DesignBlockID, property: String) throws -> Bool
```

Get the value of a bool property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value of the property.

```swift
public func setInt(_ id: DesignBlockID, property: String, value: Int) throws
```

Set an int property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getInt(_ id: DesignBlockID, property: String) throws -> Int
```

Get the value of an int property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value of the property.

```swift
public func setFloat(_ id: DesignBlockID, property: String, value: Float) throws
```

Set a float property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getFloat(_ id: DesignBlockID, property: String) throws -> Float
```

Get the value of a float property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value of the property.

```swift
public func setDouble(_ id: DesignBlockID, property: String, value: Double) throws
```

Set a double property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getDouble(_ id: DesignBlockID, property: String) throws -> Double
```

Get the value of a double property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value of the property.

```swift
public func setString(_ id: DesignBlockID, property: String, value: String) throws
```

Set a string property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getString(_ id: DesignBlockID, property: String) throws -> String
```

Get the value of a string property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value of the property.

```swift
public func setURL(_ id: DesignBlockID, property: String, value: URL) throws
```

Set a URL property of the given design block to the given value.

- `block`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The value to set.

```swift
public func getURL(_ id: DesignBlockID, property: String) throws -> URL
```

Get the value of a URL property of the given design block.

- `block`: The block whose property should be queried.
- `property`: The name of the property to set.
- Returns: The value of the property.

```swift
public func setColor(_ id: DesignBlockID, property: String, color: Color) throws
```

Set a color property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `color`: The value to set.

```swift
public func getColor(_ id: DesignBlockID, property: String) throws -> Color
```

Get the value of a color property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The color value of the property.

```swift
public func setEnum(_ id: DesignBlockID, property: String, value: String) throws
```

Set an enum property of the given design block to the given value.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `value`: The enum value as string.

```swift
public func getEnum(_ id: DesignBlockID, property: String) throws -> String
```

Get the value of an enum property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The value as string.

```swift
public func setGradientColorStops(_ id: DesignBlockID, property: String, colors: [GradientColorStop]) throws
```

Set a gradient color stops property of the given design block.

- `id`: The block whose property should be set.
- `property`: The name of the property to set.
- `colors`: The colors to set.

```swift
public func getGradientColorStops(_ id: DesignBlockID, property: String) throws -> [GradientColorStop]
```

Get the gradient color stops property of the given design block.

- `id`: The block whose property should be queried.
- `property`: The name of the property to query.
- Returns: The gradient colors.

```swift
public func setSourceSet(_ id: DesignBlockID, property: String, sourceSet: [Source]) throws
```

Set the source set of the given block.
The crop and content fill mode of the associated block will be set to the default values.

- `id`: The block whose source set should be set.
- `sourceSet`: The new source set.

```swift
public func getSourceSet(_ id: DesignBlockID, property: String) throws -> [Source]
```

Returns the source set of the given block.

- `id:`: The block whose source set should be returned.
- Returns: The source set of the given block.

```swift
public func addImageFileURIToSourceSet(_ id: DesignBlockID, property: String, uri: URL) async throws
```

Add a source to the `sourceSet` property of the given block.
If there already exists in source set an image with the same width, that existing image will be replaced.
If the source set is or gets empty, the crop and content fill mode of the associated block will be set to the
default values.
Note: This fetches the resource from the given URI to obtain the image dimensions. It is recommended to use
setSourceSet if the dimension is known.

- `id`: The block whose source set should be set.
- `property`: The name of the property to modify.
- `uri`: The source to add to the source set.

```swift
public func addVideoFileURIToSourceSet(_ id: DesignBlockID, property: String, uri: URL) async throws
```

Add a source to the `sourceSet` property of the given block.
If there already exists in source set a video with the same width, that existing video will be replaced.
If the source set is or gets empty, the crop and content fill mode of the associated block will be set to the
default values.
Note: This fetches the resource from the given URI to obtain the video dimensions. It is recommended to use
setSourceSet if the dimension is known.

- `id`: The block whose source set should be set.
- `property`: The name of the property to modify.
- `uri`: The source to add to the source set.

### Modifying Properties

Here’s the full code snippet for modifying a block’s properties:

```swift
let uuid = try engine.block.getUUID(block)
let propertyNamesStar = try engine.block
  .findAllProperties(starShape) // Array [ "shape/star/innerDiameter", "shape/star/points", "opacity/value", ... ]
let propertyNamesImage = try engine.block
  .findAllProperties(imageFill) // Array [ "fill/image/imageFileURI", "fill/image/previewFileURI", "fill/image/externalReference", ... ]
let propertyNamesText = try engine.block
  .findAllProperties(text) // Array [ "text/text", "text/fontFileUri", "text/externalReference", "text/fontSize", "text/horizontalAlignment", ... ]

let pointsType = try engine.block.getType(ofProperty: "shape/star/points") // "Int"
let alignmentType = try engine.block.getType(ofProperty: "text/horizontalAlignment") // "Enum"
try engine.block.getEnumValues(ofProperty: "text/horizontalAlignment")
let readable = try engine.block.isPropertyReadable(property: "shape/star/points")
let writable = try engine.block.isPropertyWritable(property: "shape/star/points")

// Generic Properties
try engine.block.setBool(scene, property: "scene/aspectRatioLock", value: false)
try engine.block.getBool(scene, property: "scene/aspectRatioLock")
let points = try engine.block.getInt(starShape, property: "shape/star/points")
try engine.block.setInt(starShape, property: "shape/star/points", value: points + 2)
try engine.block.setFloat(starShape, property: "shape/star/innerDiameter", value: 0.75)
try engine.block.getFloat(starShape, property: "shape/star/innerDiameter")
let audio = try engine.block.create(.audio)
try engine.block.appendChild(to: scene, child: audio)
try engine.block.setDouble(audio, property: "playback/duration", value: 1.0)
try engine.block.getDouble(audio, property: "playback/duration")
try engine.block.setString(text, property: "text/text", value: "*o*")
try engine.block.getString(text, property: "text/text")
try engine.block.setURL(
  imageFill,
  property: "fill/image/imageFileURI",
  value: URL(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!
)
try engine.block.getURL(imageFill, property: "fill/image/imageFileURI")
try engine.block.setColor(colorFill, property: "fill/color/value", color: .rgba(r: 1, g: 1, b: 1, a: 1)) // White
try engine.block.getColor(colorFill, property: "fill/color/value") as Color
try engine.block.setEnum(text, property: "text/horizontalAlignment", value: "Center")
try engine.block.setEnum(text, property: "text/verticalAlignment", value: "Center")
try engine.block.getEnum(text, property: "text/horizontalAlignment")
try engine.block.getEnum(text, property: "text/verticalAlignment")
try engine.block.setGradientColorStops(gradientFill, property: "fill/gradient/colors", colors: [
  .init(color: .rgba(r: 1.0, g: 0.8, b: 0.2, a: 1.0), stop: 0),
  .init(color: .rgba(r: 0.3, g: 0.4, b: 0.7, a: 1.0), stop: 1)
])
try engine.block.getGradientColorStops(gradientFill, property: "fill/gradient/colors")

let imageFill = try engine.block.createFill(.image)
try engine.block.setSourceSet(imageFill, property: "fill/image/sourceSet", sourceSet: [
  .init(
    uri: URL(string: "http://img.ly/my-image.png")!,
    width: 800,
    height: 600
  )
])
_ = try engine.block.getSourceSet(imageFill, property: "fill/image/sourceSet")
try await engine.block.addImageFileURIToSourceSet(imageFill, property: "fill/image/sourceSet", uri: "https://img.ly/static/ubq_samples/sample_1.jpg")
let videoFill = try engine.block.createFill(.video)
try await engine.block.addVideoFileURIToSourceSet(videoFill, property: "fill/video/sourceSet", uri: "https://img.ly/static/example-assets/sourceset/1x.mp4")
```

## Kind Property

The `kind` of a design block is a custom string that can be assigned to a block in order to categorize it and distinguish it from other blocks that have the same type. The user interface can then customize its appearance based on the kind of the selected blocks. It can also be used for automation use cases in order to process blocks in a different way based on their kind.

```swift
public func setKind(_ id: DesignBlockID, kind: String) throws
```

Get the kind of the given block, fails if the block is invalid.

- `id`: The block to query.
- `kind`: The block's kind.

```swift
public func getKind(_ id: DesignBlockID) throws -> String
```

Get the kind of the given block, fails if the block is invalid.

- `id:`: The block to query.
- Returns: The block's kind.

```swift
public func find(byKind kind: String) throws -> [DesignBlockID]
```

Finds all blocks with the given kind.

- `kind:`: The kind to search for.
- Returns: A list of block ids.

### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify a and query the kind property of design blocks through the `block` API.

```swift
try engine.block.setKind(text, kind: "title")
let kind = try engine.block.getKind(text)
let allTitles = try engine.block.find(byKind: "title")
```

## Selection & Visibility

A block can potentially be *invisible* (in the sense that you can't see it), even though
`isVisible()` returns true. This could be the case when a block has not been
added to a parent, the parent itself is not visible, or the block is obscured by another block on top of it.

```swift
public func setSelected(_ id: DesignBlockID, selected: Bool) throws
```

Update the selection state of a block.

- Note: Previously selected blocks remain selected.
  Required scope: "editor/select"
- `id`: The block to query.
- `selected`: Whether or not the block should be selected.

```swift
public func isSelected(_ id: DesignBlockID) throws -> Bool
```

Get the selected state of a block.

- `id:`: The block to query.
- Returns: `true` if the block is selected, `false` otherwise.

```swift
public func select(_ id: DesignBlockID) throws
```

Selects the given block and deselects all other blocks.

- `id:`: The block to be selected.

```swift
public func findAllSelected() -> [DesignBlockID]
```

Get all currently selected blocks.

- Returns: An array of block ids.

```swift
public var onSelectionChanged: AsyncStream<Void> { get }
```

Subscribe to changes in the current set of selected blocks.

```swift
public var onClicked: AsyncStream<DesignBlockID> { get }
```

Subscribe to block click events.

```swift
public func setVisible(_ id: DesignBlockID, visible: Bool) throws
```

Update a block's visibility.
Required scope: "layer/visibility"

- `id`: The block to update.
- `visible`: Whether the block shall be visible.

```swift
public func isVisible(_ id: DesignBlockID) throws -> Bool
```

Query a block's visibility.

- `id:`: The block to query.
- Returns: `true` if visible, `false` otherwise.

```swift
public func setClipped(_ id: DesignBlockID, clipped: Bool) throws
```

Update a block's clipped state.
Required scope: "layer/clipping"

- `id`: The block to update.
- `clipped`: Whether the block should clips its contents to its frame.

```swift
public func isClipped(_ id: DesignBlockID) throws -> Bool
```

Query a block's clipped state. If `true`, the block should clip

- `id:`: The block to query.
- Returns: `True` if clipped, `false` otherwise.

```swift
public func isIncludedInExport(_ id: DesignBlockID) throws -> Bool
```

Check if the given block is included on the exported result.

- `id:`: The block id to query.
- Returns: True if block will be included on the exported result.

```swift
public func setIncludedInExport(_ id: DesignBlockID, enabled: Bool) throws
```

Set whether you want the given design block to be included in exported result.

- `id`: The block to include/exclude from export.
- `enabled`: If true, block will be included in the export.

### Full Code

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes through the `block` API.

```swift
try engine.block.setSelected(block, selected: true)
let isSelected = try engine.block.isSelected(block)
try engine.block.select(block)
let selectedIds = engine.block.findAllSelected()

let isVisible = try engine.block.isVisible(block)
try engine.block.setVisible(block, visible: true)

let isClipped = try engine.block.isClipped(page)
try engine.block.setClipped(page, clipped: true)

let selectionTask = Task {
  for await _ in engine.block.onSelectionChanged {
    let selectedIDs = engine.block.findAllSelected()
    print("Selection changed: \(selectedIDs)")
  }
}
let clickedTask = Task {
  for await block in engine.block.onClicked {
    print("Block clicked: \(block)")
  }
}

let isIncludedInExport = try engine.block.isIncludedInExport(block)
try engine.block.setIncludedInExport(block, enabled: true)
```

## State

Blocks can perform operations that take some time or that can end in bad results.
When that happens, blocks put themselves in a pending state or an error state and visual feedback is shown pertaining to the state.
When an external operation is done to blocks, for example with a plugin, you may want to manually set the block's state to pending (if that external operation takes time) or to error (if that operation resulted in an error).

The possible states of a block are:

```
public enum BlockState {
  /// The block is ready to be rendered.
  case ready
  /// There is an ongoing operation on the block. Rendering may be affected.
  /// - Parameter progress: The progress is in the range of [0, 1].
  case pending(progress: Float)
  /// There's an error preventing rendering.
  case error(BlockStateError)
}

public enum BlockStateError {
  /// Failed to decode the block's audio stream.
  case audioDecoding
  /// Failed to decode the block's image stream.
  case imageDecoding
  /// Failed to retrieve the block's remote content.
  case fileFetch
  /// An unknown error occurred.
  case unknown
  /// Failed to decode the block's video stream.
  case videoDecoding
}
```

When calling `getState`, the returned state reflects the combined state of a block, the block's fill, the block's shape and the block's effects.
If any of these blocks is in an `.error` state, the returned state will reflect that error.
If none of these blocks is in error state but any is in `.pending` state, the returned state will reflect the aggregate progress of the block's progress.
If none of the blocks are in error state or pending state, the returned state is `.ready`.

```swift
public func getState(_ id: DesignBlockID) throws -> BlockState
```

Get the current state of a block.

- Note: If this block is in error state or this block has a `Shape` block, `Fill` block or `Effect` block(s), that
  is in error state, the returned state will be `.error`. Else, if this block is in pending state or this block has
  a `Shape` block, `Fill` block or `Effect` block(s), that is in pending state, the returned state will be
  `.pending`. Else, the returned state will be `.ready`.
- `id:`: The block whose state should be queried.
- Returns: The state of the block.

```swift
public func setState(_ id: DesignBlockID, state: BlockState) throws
```

Set the state of a block.

- `id`: The block whose state should be set.
- `state`: The new state to set.

```swift
public func onStateChanged(_ ids: [DesignBlockID]) -> AsyncStream<[DesignBlockID]>
```

Subscribe to changes to the state of a block.

- Note: Like `getState`, the state of a block is determined by the state of itself and its `Shape`, `Fill` and
  `Effect` block(s).
- `ids:`: A list of blocks to filter events by. If the list is empty, events for every block are sent.
- Returns: A stream of block state change events.

### Full Code

In this example, we will show you how to use [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to retrieve's a block's state and to manually set a block in a pending state, an error state or back to a ready state.

```swift
let stateTask = Task {
  for await blocks in engine.block.onStateChanged([block]) {
    print("State of blocks \(blocks) is updated.")
  }
}
let state = try engine.block.getState(block)
try engine.block.setState(block, state: .pending(progress: 0.5))
try engine.block.setState(block, state: .ready)
try engine.block.setState(block, state: .error(.imageDecoding))
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
