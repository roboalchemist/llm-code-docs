# Source: https://img.ly/docs/cesdk/android/concepts/scenes-e8596d/

---
title: "Scenes"
description: "Scenes act as the root container for blocks and define the full design structure in CE.SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/scenes-e8596d/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Scenes](https://img.ly/docs/cesdk/android/concepts/scenes-e8596d/)

---

```kotlin file=@cesdk_android_examples/engine-guides-modifying-scenes/ModifyingScenes.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun modifyingScenes(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    // In engine only mode we have to create our own scene and page.
    if (engine.scene.get() == null) {
        val scene = engine.scene.create()
        val page = engine.block.create(DesignBlockType.Page)
        engine.block.appendChild(parent = scene, child = page)
    }

    // Find all pages in our scene.
    val pages = engine.block.findByType(DesignBlockType.Page)
    // Use the first page we found.
    val page = pages.first()

    // Create a graphic block and add it to the scene's page.
    val block = engine.block.create(DesignBlockType.Graphic)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setFill(block = block, fill = fill)

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

    engine.block.appendChild(parent = page, child = block)

    // Zoom the scene's camera on our page.
    engine.scene.zoomToBlock(page)

    engine.stop()
}
```

Commonly, a scene contains several pages which in turn contain any other blocks such as images and texts. A block (or design block) is the main building unit in CE.SDK. Blocks are organized in a hierarchy through parent-child relationships. A scene is a specialized block that acts as the root of this hierarchy.

At any time, the engine holds only a single scene. Loading or creating a scene will replace the current one.

## Interacting With The Scene

### Creating or Using an Existing Scene

When using the Engine's API in the context of the CE.SDK editor, there's already an existing scene.
You can obtain a handle to this scene by calling the [SceneAPI](https://img.ly/docs/cesdk/android/concepts/scenes-e8596d/)'s `fun get(): DesignBlock?` method.
However, when using the Engine on its own you first have to create a scene, e.g. using `fun create(): DesignBlock`.
See the [Creating Scenes](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) guide for more details and options.

```kotlin
    // In engine only mode we have to create our own scene and page.
    if (engine.scene.get() == null) {
        val scene = engine.scene.create()
```

Next, we need a page to place our blocks on.
The scene automatically arranges its pages either in a vertical (the default) or horizontal layout.
Again in the context of the editor, there's already an existing page.
To fetch that page call the [BlockAPI](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/)'s `fun findByType(blockType: DesignBlockType): List<DesignBlock>` method and use the first element of the returned list.

When only using the engine, you have to create a page yourself and append it to the scene.
To do that create the page using `fun fun create(): DesignBlock` and append it to the scene with `fun appendChild(parent: DesignBlock, child: DesignBlock)`.

```kotlin
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

As an example, we create a graphic block using the [BlockAPI](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/)'s `create()` method
which we already used for creating our page. Then we set a rect shape and an image fill to this newly created block to give it a visual representation.
To see what other kinds of blocks are available see the [Block Types](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) in the API Reference.

```kotlin
    // Create a graphic block and add it to the scene's page.
    val block = engine.block.create(DesignBlockType.Graphic)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setFill(block = block, fill = fill)
```

We set a property of our newly created image fill by giving it a URL to reference an image file from.
We also make sure the entire image stays visible by setting the block's content fill mode to `'Contain'`.
To learn more about block properties check out the [Block Properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) API Reference.

```kotlin
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

```kotlin
    engine.block.appendChild(parent = page, child = block)
```

To frame everything nicely and put it into view we direct the scene's camera to zoom on our page.

```kotlin
    // Zoom the scene's camera on our page.
    engine.scene.zoomToBlock(page)
```

### Full Code

Here's the full code snippet for interacting with the scene:

```kotlin
import kotlinx.coroutines.*
import ly.img.engine.*

fun modifyingScenes(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    // In engine only mode we have to create our own scene and page.
    if (engine.scene.get() == null) {
        val scene = engine.scene.create()
        val page = engine.block.create(DesignBlockType.Page)
        engine.block.appendChild(parent = scene, child = page)
    }

    // Find all pages in our scene.
    val pages = engine.block.findByType(DesignBlockType.Page)
    // Use the first page we found.
    val page = pages.first()

    // Create a graphic block and add it to the scene's page.
    val block = engine.block.create(DesignBlockType.Graphic)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setFill(block = block, fill = fill)

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

    engine.block.appendChild(parent = page, child = block)

    // Zoom the scene's camera on our page.
    engine.scene.zoomToBlock(page)

    engine.stop()
}
```

## Exploring Scene Contents Using The Scene API

Learn how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to explore scene contents through the `scene` API.

```kotlin
fun getPages(): List<DesignBlock>
```

Get the sorted list of pages in the scene.

- Returns the sorted list of pages in the scene.

```kotlin
fun getCurrentPage(): DesignBlock?
```

Get the current page, i.e., the page of the first selected element if this page is at least 25% visible or,

otherwise, the page nearest to the viewport center.

- Returns the current page in the scene or null.

```kotlin
fun findNearestToViewPortCenterByType(blockType: DesignBlockType): List<DesignBlock>
```

Finds all blocks with the given type sorted by distance to viewport center.

- `blockType`: the type to search for.

- Returns a list of block ids sorted by distance to viewport center.

```kotlin
fun findNearestToViewPortCenterByKind(blockKind: String): List<DesignBlock>
```

Finds all blocks with the given kind sorted by distance to viewport center.

- `blockKind`: the kind to search for.

- Returns a list of block ids sorted by distance to viewport center.

```kotlin
fun setDesignUnit(designUnit: DesignUnit)
```

Converts all values of the current scene into the given design unit.

- `designUnit`: the new design unit of the scene.

```kotlin
fun getDesignUnit(): DesignUnit
```

Returns the design unit of the current scene.

- Returns The current design unit.

### Full Code

Here's the full code snippet for exploring a scene's contents using the `scene` API:

```kotlin
val pages = engine.scene.getPages()
val currentPage = engine.scene.getCurrentPage();
val nearestPageByType = engine.scene.findNearestToViewPortCenterByType(DesignBlockType.Page).first();
val nearestImageByKind = engine.sce.findNearestToViewPortCenterByKind("image").first();

engine.scene.setDesignUnit(DesignUnit.PIXEL)

/* Now returns DesignUnit.PIXEL */
engine.scene.getDesignUnit()
```

## Exploring Scene Contents Using The Block API

Learn how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to explore scenes through the `block` API.

### Functions

```kotlin
fun findAll(): List<DesignBlock>
```

Return all blocks currently known to the engine.

- Returns a list of block ids.

```kotlin
fun findAllPlaceholders(): List<DesignBlock>
```

Return all placeholder blocks in the current scene.

- Returns a list of block ids.

```kotlin
fun findByType(type: DesignBlockType): List<DesignBlock>
```

Finds all design blocks with the given type.

- `type`: the type to search for.

- Returns a list of block ids.

```kotlin
fun findByType(type: ShapeType): List<DesignBlock>
```

Finds all shape blocks with the given type.

- `type`: the type to search for.

- Returns a list of block ids.

```kotlin
fun findByType(type: EffectType): List<DesignBlock>
```

Finds all effect blocks with the given type.

- `type`: the type to search for.

- Returns a list of block ids.

```kotlin
fun findByType(type: BlurType): List<DesignBlock>
```

Finds all blur blocks with the given type.

- `type`: the type to search for.

- Returns a list of block ids.

```kotlin
fun findByKind(blockKind: String): List<DesignBlock>
```

Finds all blocks with the given kind.

- `blockKind`: the kind to search for.

- Returns a list of block ids.

```kotlin
fun findByName(name: String): List<DesignBlock>
```

Finds all blocks with the given name.

- `name`: the name to search for.

- Returns a list of block ids.

### Full Code

Here's the full code snippet for exploring a scene's contents using the `block` API:

```kotlin
val allIds = engine.block.findAll()
val allPlaceholderIds = engine.block.findAllPlaceholders()
val allPages = engine.block.findByType(DesignBlockType.Page)
val allImageFills = engine.block.findByType(FillType.Image)
val allStarShapes = engine.block.findByType(ShapeType.Star)
val allHalfToneEffects = engine.block.findByType(EffectType.HalfTone)
val allUniformBlurs = engine.block.findByType(BlurType.Uniform)
val allStickers = engine.block.findByKind("sticker")
val ids = engine.block.findByName("someName")
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
