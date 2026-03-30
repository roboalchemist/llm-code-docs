# Source: https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/create-shapes-64acc0/

---
title: "Create Shapes"
description: "Draw custom vector shapes and insert them into your design canvas."
platform: android
url: "https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/create-shapes-64acc0/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/android/shapes-9f1b2c/) > [Create Shapes](https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/create-shapes-64acc0/)

---

```kotlin file=@cesdk_android_examples/engine-guides-using-shapes/UsingShapes.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingShapes(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.create()

    val graphic = engine.block.create(DesignBlockType.Graphic)
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(graphic, fill = imageFill)
    engine.block.setWidth(graphic, value = 100F)
    engine.block.setHeight(graphic, value = 100F)
    engine.block.appendChild(parent = scene, child = graphic)

    engine.scene.zoomToBlock(
        graphic,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    engine.block.supportsShape(graphic) // Returns true
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.supportsShape(text) // Returns false

    val rectShape = engine.block.createShape(ShapeType.Rect)
    engine.block.setShape(graphic, shape = rectShape)
    val shape = engine.block.getShape(graphic)
    val shapeType = engine.block.getType(shape)

    val starShape = engine.block.createShape(ShapeType.Star)
    engine.block.destroy(engine.block.getShape(graphic))
    engine.block.setShape(graphic, shape = starShape)
    // The following line would also destroy the currently attached starShape
    // engine.block.destroy(graphic)

    val allShapeProperties = engine.block.findAllProperties(starShape)
    engine.block.setInt(starShape, property = "shape/star/points", value = 6)

    engine.stop()
}
```

The CE.SDK provides a flexible way to create and customize shapes, including rectangles, circles, lines, and polygons.

## Supported Shapes

The following shapes are supported in CE.SDK:

- `ShapeType.Rect`
- `ShapeType.Line`
- `ShapeType.Ellipse`
- `ShapeType.Polygon`
- `ShapeType.Star`
- `ShapeType.VectorPath`

## Creating Shapes

`graphic` blocks don't have any shape after you create them, which leaves them invisible by default.
In order to make them visible, we need to assign both a shape and a fill to the `graphic` block. You can find more
information on fills [here](https://img.ly/docs/cesdk/android/fills-402ddc/). In this example we have created and attached an image fill.

In order to create a new shape, we must call the `fun createShape(type: ShapeType): DesignBlock` API.

```kotlin highlight-createShape
val rectShape = engine.block.createShape(ShapeType.Rect)
```

In order to assign this shape to the `graphic` block, call the `fun setShape(block: DesignBlock, shape: DesignBlock)` API.

```kotlin highlight-setShape
engine.block.setShape(graphic, shape = rectShape)
```

Just like design blocks, shapes with different types have different properties that you can set via the API. Please refer to the [API docs](https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/edit-shapes-d67cfb/) for a complete list of all available properties for each type of shape.

## Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingShapes(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.create()

    val graphic = engine.block.create(DesignBlockType.Graphic)
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(graphic, fill = imageFill)
    engine.block.setWidth(graphic, value = 100F)
    engine.block.setHeight(graphic, value = 100F)
    engine.block.appendChild(parent = scene, child = graphic)

    engine.scene.zoomToBlock(
        graphic,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    engine.block.supportsShape(graphic) // Returns true
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.supportsShape(text) // Returns false

    val rectShape = engine.block.createShape(ShapeType.Rect)
    engine.block.setShape(graphic, shape = rectShape)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
