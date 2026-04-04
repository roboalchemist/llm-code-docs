# Source: https://img.ly/docs/cesdk/android/fills/overview-3895ee/

---
title: "Fills"
description: "Apply solid colors, gradients, images, or videos as fills to shapes, text, and other design elements."
platform: android
url: "https://img.ly/docs/cesdk/android/fills/overview-3895ee/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Fills](https://img.ly/docs/cesdk/android/fills-402ddc/) > [Overview](https://img.ly/docs/cesdk/android/fills/overview-3895ee/)

---

```kotlin file=@cesdk_android_examples/engine-guides-using-fills/UsingFills.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingFills(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)

    engine.scene.zoomToBlock(
        page,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)
    engine.block.setFill(block, fill = engine.block.createFill(FillType.Color))
    engine.block.appendChild(parent = page, child = block)

    engine.block.supportsFill(scene) // Returns false
    engine.block.supportsFill(block) // Returns true

    val colorFill = engine.block.getFill(block)
    val defaultRectFillType = engine.block.getType(colorFill)
    val allFillProperties = engine.block.findAllProperties(colorFill)
    engine.block.setColor(
        block = colorFill,
        property = "fill/color/value",
        value = Color.fromRGBA(r = 1.0F, g = 0.0F, b = 0.0F, a = 1.0F),
    )

    engine.block.setFillEnabled(block, enabled = false)
    engine.block.setFillEnabled(block, enabled = !engine.block.isFillEnabled(block))

    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )

    engine.block.destroy(colorFill)
    engine.block.setFill(block, fill = imageFill)

    /*
    // The following line would also destroy imageFill
    engine.block.destroy(circle)
     */

    val duplicateBlock = engine.block.duplicate(block)
    engine.block.setPositionX(duplicateBlock, value = 450F)
    val autoDuplicateFill = engine.block.getFill(duplicateBlock)
    engine.block.setString(
        block = autoDuplicateFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_2.jpg",
    )

    /*
    // We could now assign this fill to another block.
    val manualDuplicateFill = engine.block.duplicate(autoDuplicateFill)
    engine.block.destroy(manualDuplicateFill)
     */

    val sharedFillBlock = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(sharedFillBlock, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(sharedFillBlock, value = 350F)
    engine.block.setPositionY(sharedFillBlock, value = 400F)
    engine.block.setWidth(sharedFillBlock, value = 100F)
    engine.block.setHeight(sharedFillBlock, value = 100F)
    engine.block.appendChild(parent = page, child = sharedFillBlock)
    engine.block.setFill(sharedFillBlock, fill = engine.block.getFill(block))

    engine.stop()
}
```

Some [design blocks](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) in CE.SDK allow you to modify or replace their fill. The fill is an object that defines the contents within the shape of a block. CreativeEditor SDK supports many different types of fills, such as images, solid colors, gradients and videos.

Similarly to blocks, each fill has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

We currently support the following fill types:

- `FillType.Color`
- `FillType.LinearGradient`
- `FillType.RadialGradient`
- `FillType.ConicalGradient`
- `FillType.Image`
- `FillType.Video`
- `FillType.PixelStream`

## Accessing Fills

Not all types of design blocks support fills, so you should always first call the `fun supportsFill(block: DesignBlock): Boolean` API before accessing any of the following APIs.

```kotlin highlight-supportsFill
engine.block.supportsFill(scene) // Returns false
engine.block.supportsFill(block) // Returns true
```

In order to receive the fill id of a design block, call the `fun getFill(block: DesignBlock): DesignBlock` API. You can now pass this id into other APIs in order to query more information about the fill, e.g. its type via the `fun getType(block: DesignBlock): String` API.

```kotlin highlight-getFill
val colorFill = engine.block.getFill(block)
val defaultRectFillType = engine.block.getType(colorFill)
```

## Fill Properties

Just like design blocks, fills with different types have different properties that you can query and modify via the API. Use `fun findAllProperties(block: DesignBlock): List<String>` in order to get a list of all properties of a given fill.

For the solid color fill in this example, the call would return `["fill/color/value", "type"]`.

Please refer to the [design blocks](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for a complete list of all available properties for each type of fill.

```kotlin highlight-getProperties
val allFillProperties = engine.block.findAllProperties(colorFill)
```

Once we know the property keys of a fill, we can use the same APIs as for design blocks in order to modify those properties. For example, we can use `fun setColor(block: DesignBlock, property: String, value: Color)` in order to change the color of the fill to red.

Once we do this, our graphic block with rect shape will be filled with solid red.

```kotlin highlight-modifyProperties
engine.block.setColor(
    block = colorFill,
    property = "fill/color/value",
    value = Color.fromRGBA(r = 1.0F, g = 0.0F, b = 0.0F, a = 1.0F),
)
```

## Disabling Fills

You can disable and enable a fill using the `fun setFillEnabled(block: DesignBlock, enabled: Boolean)` API, for example in cases where the design block should only have a stroke but no fill. Notice that you have to pass the id of the design block and not of the fill to the API.

```kotlin highlight-disableFill
engine.block.setFillEnabled(block, enabled = false)
engine.block.setFillEnabled(block, enabled = !engine.block.isFillEnabled(block))
```

## Changing Fill Types

All design blocks that support fills allow you to also exchange their current fill for any other type of fill. In order to do this, you need to first create a new fill object using `fun createFill(fillType: FillType): DesignBlock`.

```kotlin highlight-createFill
val imageFill = engine.block.createFill(FillType.Image)
engine.block.setString(
    block = imageFill,
    property = "fill/image/imageFileURI",
    value = "https://img.ly/static/ubq_samples/sample_1.jpg",
)
```

In order to assign a fill to a design block, simply call `fun setFill(block: DesignBlock, fill: DesignBlock)`. Make sure to delete the previous fill of the design block first if you don't need it any more, otherwise we will have leaked it into the scene and won't be able to access it any more, because we don't know its id.

Notice that we don't use the `appendChild` API here, which only works with design blocks and not fills.

When a fill is attached to one design block, it will be automatically destroyed when the block itself gets destroyed.

```kotlin highlight-replaceFill
    engine.block.destroy(colorFill)
    engine.block.setFill(block, fill = imageFill)

    /*
    // The following line would also destroy imageFill
    engine.block.destroy(circle)
     */
```

## Duplicating Fills

If we duplicate a design block with a fill that is only attached to this block, the fill will automatically be duplicated as well. In order to modify the properties of the duplicate fill, we have to query its id from the duplicate block.

```kotlin highlight-duplicateFill
    val duplicateBlock = engine.block.duplicate(block)
    engine.block.setPositionX(duplicateBlock, value = 450F)
    val autoDuplicateFill = engine.block.getFill(duplicateBlock)
    engine.block.setString(
        block = autoDuplicateFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_2.jpg",
    )

    /*
    // We could now assign this fill to another block.
    val manualDuplicateFill = engine.block.duplicate(autoDuplicateFill)
    engine.block.destroy(manualDuplicateFill)
     */
```

## Sharing Fills

It is also possible to share a single fill instance between multiple design blocks. In that case, changing the properties of the fill will apply to all of the blocks that it's attached to at once.

Destroying a block with a shared fill will not destroy the fill until there are no other design blocks left that still use that fill.

```kotlin highlight-sharedFill
val sharedFillBlock = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(sharedFillBlock, shape = engine.block.createShape(ShapeType.Rect))
engine.block.setPositionX(sharedFillBlock, value = 350F)
engine.block.setPositionY(sharedFillBlock, value = 400F)
engine.block.setWidth(sharedFillBlock, value = 100F)
engine.block.setHeight(sharedFillBlock, value = 100F)
engine.block.appendChild(parent = page, child = sharedFillBlock)
engine.block.setFill(sharedFillBlock, fill = engine.block.getFill(block))
```

## Full Code

Here is the full code for working with fills:

```kotlin
import kotlinx.coroutines.*
import ly.img.engine.*

fun usingFills(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)

    engine.scene.zoomToBlock(
        page,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)
    engine.block.setFill(block, fill = engine.block.createFill(FillType.Color))
    engine.block.appendChild(parent = page, child = block)

    engine.block.supportsFill(scene) // Returns false
    engine.block.supportsFill(block) // Returns true

    val colorFill = engine.block.getFill(block)
    val defaultRectFillType = engine.block.getType(colorFill)
    val allFillProperties = engine.block.findAllProperties(colorFill)
    engine.block.setColor(
        block = colorFill,
        property = "fill/color/value",
        value = Color.fromRGBA(r = 1.0F, g = 0.0F, b = 0.0F, a = 1.0F),
    )

    engine.block.setFillEnabled(block, enabled = false)
    engine.block.setFillEnabled(block, enabled = !engine.block.isFillEnabled(block))

    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )

    engine.block.destroy(colorFill)
    engine.block.setFill(block, fill = imageFill)

    /*
    // The following line would also destroy imageFill
    engine.block.destroy(circle)
     */

    val duplicateBlock = engine.block.duplicate(block)
    engine.block.setPositionX(duplicateBlock, value = 450F)
    val autoDuplicateFill = engine.block.getFill(duplicateBlock)
    engine.block.setString(
        block = autoDuplicateFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_2.jpg",
    )

    /*
    // We could now assign this fill to another block.
    val manualDuplicateFill = engine.block.duplicate(autoDuplicateFill)
    engine.block.destroy(manualDuplicateFill)
     */

    val sharedFillBlock = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(sharedFillBlock, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(sharedFillBlock, value = 350F)
    engine.block.setPositionY(sharedFillBlock, value = 400F)
    engine.block.setWidth(sharedFillBlock, value = 100F)
    engine.block.setHeight(sharedFillBlock, value = 100F)
    engine.block.appendChild(parent = page, child = sharedFillBlock)
    engine.block.setFill(sharedFillBlock, fill = engine.block.getFill(block))

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
