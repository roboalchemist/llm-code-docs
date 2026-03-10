# Source: https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/edit-shapes-d67cfb/

---
title: "Edit Shapes"
description: "Modify shape properties like size, color, position, and border radius."
platform: android
url: "https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/edit-shapes-d67cfb/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/android/shapes-9f1b2c/) > [Edit Shapes](https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/edit-shapes-d67cfb/)

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

The `graphic` [design block](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) in CE.SDK allows you to modify and replace its shape. CreativeEditor SDK supports many different types of shapes, such as rectangles, lines, ellipses, polygons and custom vector paths.

Similarly to blocks, each shape object has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

## Accessing Shapes

In order to query whether a block supports shapes, you should call the `fun supportsShape(block: DesignBlock): Boolean` API.
Currently, only the `graphic` design block supports shape objects.

```kotlin highlight-supportsShape
engine.block.supportsShape(graphic) // Returns true
val text = engine.block.create(DesignBlockType.Text)
engine.block.supportsShape(text) // Returns false
```

To query the shape of a design block, call the `fun getShape(block: DesignBlock): DesignBlock` API.
You can now pass the returned result into other APIs in order to query more information about the shape,
e.g. its type via the `fun getType(block: DesignBlock): String` API.

```kotlin highlight-getShape
val shape = engine.block.getShape(graphic)
val shapeType = engine.block.getType(shape)
```

When replacing the shape of a design block, remember to destroy the previous shape object if you don't
intend to use it any further. Shape objects that are not attached to a design block will never be automatically destroyed.

Destroying a design block will also destroy its attached shape block.

```kotlin highlight-replaceShape
val starShape = engine.block.createShape(ShapeType.Star)
engine.block.destroy(engine.block.getShape(graphic))
engine.block.setShape(graphic, shape = starShape)
// The following line would also destroy the currently attached starShape
// engine.block.destroy(graphic)
```

## Shape Properties

Just like design blocks, shapes with different types have different properties that you can query and modify via the API. Use `fun findAllProperties(block: DesignBlock): List<String>` in order to get a list of all properties of a given shape.

For the star shape in this example, the call would return
`["name", "shape/star/innerDiameter", "shape/star/points", "type", "uuid"]`.

Please refer to the [API docs](https://img.ly/docs/cesdk/android/stickers-and-shapes/create-edit/edit-shapes-d67cfb/) for a complete list of all available properties for each type of shape.

```kotlin highlight-getProperties
val allShapeProperties = engine.block.findAllProperties(starShape)
```

Once we know the property keys of a shape, we can use the same APIs as for design blocks in order to modify those properties. For example, we can use `fun setInt(block: DesignBlock, property: String, value: Int)` in order to change the number of points
of the star to six.

```kotlin highlight-modifyProperties
engine.block.setInt(starShape, property = "shape/star/points", value = 6)
```

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



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
