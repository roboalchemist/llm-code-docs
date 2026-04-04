# Source: https://img.ly/docs/cesdk/ios/concepts/scenes-e8596d/

---
title: "Scenes"
description: "Scenes act as the root container for blocks and define the full design structure in CE.SDK."
platform: ios
url: "https://img.ly/docs/cesdk/ios/concepts/scenes-e8596d/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/ios/concepts-c9ff51/) > [Scenes](https://img.ly/docs/cesdk/ios/concepts/scenes-e8596d/)

---

```swift file=@cesdk_swift_examples/engine-guides-modifying-scenes/ModifyingScenes.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func modifyingScenes(engine: Engine) async throws {
  let scene = try engine.scene.get()
  /* In engine only mode we have to create our own scene and page. */

  if scene == nil {
    let scene = try engine.scene.create()
    let page = try engine.block.create(.page)
    try engine.block.appendChild(to: scene, child: page)
  }

  /* Find all pages in our scene. */
  let pages = try engine.block.find(byType: .page)
  /* Use the first page we found. */
  let page = pages.first!

  /* Create a graphic block and add it to the scene's page. */
  let block = try engine.block.create(.graphic)
  let fill = try engine.block.createFill(.image)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  try engine.block.setFill(block, fill: fill)

  try engine.block.setString(
    fill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/imgly_logo.jpg",
  )

  /* The content fill mode 'Contain' ensures the entire image is visible. */
  try engine.block.setEnum(block, property: "contentFill/mode", value: "Contain")

  try engine.block.appendChild(to: page, child: block)

  /* Zoom the scene's camera on our page. */
  try await engine.scene.zoom(to: page)
}
```

Commonly, a scene contains several pages which in turn contain any other blocks such as images and texts. A block (or design block) is the main building unit in CE.SDK. Blocks are organized in a hierarchy through parent-child relationships. A scene is a specialized block that acts as the root of this hierarchy.

At any time, the engine holds only a single scene. Loading or creating a scene will replace the current one.

## Interacting With The Scene

### Creating or Using an Existing Scene

When using the Engine's API in the context of the CE.SDK editor, there's already an existing scene.
You can obtain a handle to this scene by calling the [SceneAPI](https://img.ly/docs/cesdk/ios/concepts/scenes-e8596d/)'s `func get() throws -> DesignBlockID?` method.
However, when using the Engine on its own you first have to create a scene, e.g. using `func create() throws -> DesignBlockID`.
See the [Creating Scenes](https://img.ly/docs/cesdk/ios/open-the-editor-23a1db/) guide for more details and options.

```swift
    // In engine only mode we have to create our own scene and page.
    if (engine.scene.get() == null) {
        val scene = engine.scene.create()
```

Next, we need a page to place our blocks on.
The scene automatically arranges its pages either in a vertical (the default) or horizontal layout.
Again in the context of the editor, there's already an existing page.
To fetch that page call the [BlockAPI](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/)'s `func find(byType type: DesignBlockType) throws -> [DesignBlockID]` method and use the first element of the returned array.

When only using the engine, you have to create a page yourself and append it to the scene.
To do that create the page using `func create(_ type: DesignBlockType) throws -> DesignBlockID` and append it to the scene with `func appendChild(to parent: DesignBlockID, child: DesignBlockID) throws`.

```swift
        val page = engine.block.create(DesignBlockType.Page)
        engine.block.appendChild(parent = scene, child = page)
    }

    // Find all pages in our scene.
    val pages = engine.block.findByType(DesignBlockType.Page)
    // Use the first page we found.
    val page = pages.first()
```

At this point, you should have a handle to an existing scene as well as a handle to its page.
Now it gets interesting when we start to add different types of blocks to the scene's page.

### Modifying the Scene

As an example, we create a graphic block using the [BlockAPI](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/)'s `create()` method
which we already used for creating our page. Then we set a rect shape and an image fill to this newly created block to give it a visual representation.
To see what other kinds of blocks are available see the [Block Types](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) in the API Reference.

```swift
    // Create a graphic block and add it to the scene's page.
    val block = engine.block.create(DesignBlockType.Graphic)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setFill(block = block, fill = fill)
```

We set a property of our newly created image fill by giving it a URL to reference an image file from.
We also make sure the entire image stays visible by setting the block's content fill mode to `'Contain'`.
To learn more about block properties check out the [Block Properties](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) API Reference.

```swift
    engine.block.setString(
        block = fill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/imgly_logo.jpg",
    )

    // The content fill mode 'Contain' ensures the entire image is visible.
    engine.block.setEnum(
        block = block,
        property = "contentFill/mode",
        value = "Contain",
    )
```

And finally, for our image to be visible we have to add it to our page using `appendChild`.

```swift
    engine.block.appendChild(parent = page, child = block)
```

To frame everything nicely and put it into view we direct the scene's camera to zoom on our page.

```swift
    // Zoom the scene's camera on our page.
    engine.scene.zoomToBlock(page)
```

### Full Code

Here's the full code snippet:

```swift
import Foundation
import IMGLYEngine

@MainActor
func modifyingScenes(engine: Engine) async throws {
  let scene = try engine.scene.get()
  /* In engine only mode we have to create our own scene and page. */

  if scene == nil {
    let scene = try engine.scene.create()
    let page = try engine.block.create(.page)
    try engine.block.appendChild(to: scene, child: page)
  }

  /* Find all pages in our scene. */
  let pages = try engine.block.find(byType: .page)
  /* Use the first page we found. */
  let page = pages.first!

  /* Create a graphic block and add it to the scene's page. */
  let block = try engine.block.create(.graphic)
  let fill = try engine.block.createFill(.image)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  try engine.block.setFill(block, fill: fill)

  try engine.block.setString(
    fill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/imgly_logo.jpg"
  )

  /* The content fill mode 'Contain' ensures the entire image is visible. */
  try engine.block.setEnum(block, property: "contentFill/mode", value: "Contain")

  try engine.block.appendChild(to: page, child: block)

  /* Zoom the scene's camera on our page. */
  try await engine.scene.zoom(to: page)
}
```

## Exploring Scene Contents Using The Scene API

Learn how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to explore scene contents through the `scene` API.

```swift
public func getPages() throws -> [DesignBlockID]
```

Get the sorted list of pages in the scene.

- Returns: The sorted list of pages in the scene.

```swift
public func setDesignUnit(_ designUnit: DesignUnit) throws
```

Converts all values of the current scene into the given design unit.

- `designUnit:`: The new design unit of the scene.

```swift
public func getDesignUnit() throws -> DesignUnit
```

Returns the design unit of the current scene.

- Returns: The current design unit.

```swift
public func getCurrentPage() throws -> DesignBlockID?
```

Get the current page, i.e., the page of the first selected element if this page is at least 25% visible,
otherwise, the page nearest to the viewport center.

- Returns: The current page in the scene or an error.

```swift
public func findNearestToViewPortCenter(byKind kind: String) throws -> [DesignBlockID]
```

Finds all blocks with the given kind sorted by distance to viewport center.

- `kind:`: The kind to search for.
- Returns: A list of block ids with the given kind sorted by distance to viewport center.

```swift
public func findNearestToViewPortCenter(byType type: DesignBlockType) throws -> [DesignBlockID]
```

Finds all blocks with the given type sorted by distance to viewport center.

- `type:`: The type to search for.
- Returns: A list of block ids with the given type sorted by distance to viewport center.

### Full Code

Here's the full code snippet for exploring a scene's contents using the `scene` API:

```swift
let pages = try engine.scene.getPages()
val currentPage = engine.scene.getCurrentPage()
val nearestPageByType = engine.scene.findNearestToViewPortCenter(byType: .page).first!
val nearestImageByKind = engine.scene.findNearestToViewPortCenter(byKind: "image").first!

try engine.scene.setDesignUnit(.px)

/* Now returns DesignUnit.px */
_ = try engine.scene.getDesignUnit()
```

## Exploring Scene Contents Using The Block API

Learn how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to explore scenes through the `block` API.

### Functions

```swift
public func findAll() -> [DesignBlockID]
```

Return all blocks currently known to the engine.

- Returns: A list of block ids.

```swift
public func findAllPlaceholders() -> [DesignBlockID]
```

Return all placeholder blocks in the current scene.

- Returns: A list of block ids.

```swift
public func find(byType type: DesignBlockType) throws -> [DesignBlockID]
```

Finds all blocks with the given type.

- `type:`: The type to search for.
- Returns: A list of block ids.

```swift
public func find(byType type: FillType) throws -> [DesignBlockID]
```

Finds all blocks with the given type.

- `type:`: The type to search for.
- Returns: A list of block ids.

```swift
public func find(byType type: ShapeType) throws -> [DesignBlockID]
```

Finds all blocks with the given type.

- `type:`: The type to search for.
- Returns: A list of block ids.

```swift
public func find(byType type: EffectType) throws -> [DesignBlockID]
```

Finds all blocks with the given type.

- `type:`: The type to search for.
- Returns: A list of block ids.

```swift
public func find(byType type: BlurType) throws -> [DesignBlockID]
```

Finds all blocks with the given type.

- `type:`: The type to search for.
- Returns: A list of block ids.

```swift
public func find(byKind kind: String) throws -> [DesignBlockID]
```

Finds all blocks with the given kind.

- `kind:`: The kind to search for.
- Returns: A list of block ids.

```swift
public func find(byName name: String) -> [DesignBlockID]
```

Finds all blocks with the given name.

- `name:`: The name to search for.
- Returns: A list of block ids.

### Full Code

Here's the full code snippet for exploring a scene's contents using the `block` API:

```swift
let allIds = engine.block.findAll()
let allPlaceholderIds = engine.block.findAllPlaceholders()
let allPages = try engine.block.find(byType: .page)
let allImageFills = try engine.block.find(byType: .image)
let allStarShapes = try engine.block.find(byType: .star)
let allHalfToneEffects = try engine.block.find(byType: .halfTone)
let allUniformBlurs = try engine.block.find(byType: .uniform)
let allStickers = try engine.block.find(byKind: "sticker")
let ids = engine.block.find(byName: "someName")
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
