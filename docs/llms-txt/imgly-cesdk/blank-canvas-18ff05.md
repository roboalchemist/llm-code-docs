# Source: https://img.ly/docs/cesdk/android/open-the-editor/blank-canvas-18ff05/

---
title: "Start With Blank Canvas"
description: "Launch the editor with an empty canvas as a starting point for new designs."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/blank-canvas-18ff05/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [Start With Blank Canvas](https://img.ly/docs/cesdk/android/open-the-editor/blank-canvas-18ff05/)

---

```kotlin file=@cesdk_android_examples/engine-guides-create-scene-from-scratch/CreateSceneFromScratch.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun createSceneFromScratch(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block = block, shape = engine.block.createShape(ShapeType.Star))
    engine.block.setFill(block = block, fill = engine.block.createFill(FillType.Color))
    engine.block.appendChild(parent = page, child = block)

    engine.stop()
}
```

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) from scratch and add a star shape.

We create an empty scene via `engine.scene.create()` which sets up the default scene block with a camera attached.
Afterwards, the scene can be populated by creating additional blocks and appending them to the scene.
See [Modifying Scenes](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for more details.

```kotlin highlight-create
val scene = engine.scene.create()
```

We first add a page with `fun create(blockType: DesignBlockType): DesignBlock` specifying a `DesignBlockType.Page` and set a parent-child relationship between the scene and this page.

```kotlin highlight-add-page
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
```

To this page, we add a graphic design block, again with `fun create(blockType: DesignBlockType): DesignBlock`.
To make it more interesting, we set a star shape and a color fill to this block to give it a visual representation.
Like for the page, we set the parent-child relationship between the page and the newly added block.
From then on, modifications to this block are relative to the page.

```kotlin highlight-add-block-with-star-shape
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(block = block, shape = engine.block.createShape(ShapeType.Star))
engine.block.setFill(block = block, fill = engine.block.createFill(FillType.Color))
engine.block.appendChild(parent = page, child = block)
```

This example first appends a page child to the scene as would typically be done but it is not strictly necessary and any child block can be appended directly to a scene.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun createSceneFromScratch(
    license: String,
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block = block, shape = engine.block.createShape(ShapeType.Star))
    engine.block.setFill(block = block, fill = engine.block.createFill(FillType.Color))
    engine.block.appendChild(parent = page, child = block)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
