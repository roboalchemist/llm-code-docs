# Source: https://img.ly/docs/cesdk/android/stickers-and-shapes/combine-2a9e26/

---
title: "Combine"
description: "Group and merge multiple stickers or shapes into a single element for easier manipulation."
platform: android
url: "https://img.ly/docs/cesdk/android/stickers-and-shapes/combine-2a9e26/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/android/shapes-9f1b2c/) > [Combine](https://img.ly/docs/cesdk/android/stickers-and-shapes/combine-2a9e26/)

---

```kotlin file=@cesdk_android_examples/engine-guides-bool-ops/BoolOps.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.BooleanOperation
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingBoolOps(
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

    val circle1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle1, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle1, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle1, value = 30F)
    engine.block.setPositionY(circle1, value = 30F)
    engine.block.setWidth(circle1, value = 40F)
    engine.block.setHeight(circle1, value = 40F)
    engine.block.appendChild(parent = page, child = circle1)

    val circle2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle2, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle2, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle2, value = 80F)
    engine.block.setPositionY(circle2, value = 30F)
    engine.block.setWidth(circle2, value = 40F)
    engine.block.setHeight(circle2, value = 40F)
    engine.block.appendChild(parent = page, child = circle2)

    val circle3 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle3, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle3, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle3, value = 50F)
    engine.block.setPositionY(circle3, value = 50F)
    engine.block.setWidth(circle3, value = 50F)
    engine.block.setHeight(circle3, value = 50F)
    engine.block.appendChild(parent = page, child = circle3)

    engine.block.combine(listOf(circle1, circle2, circle3), op = BooleanOperation.UNION)

    val text = engine.block.create(DesignBlockType.Text)
    engine.block.replaceText(text, "Removed text")
    engine.block.setPositionX(text, value = 10F)
    engine.block.setPositionY(text, value = 40F)
    engine.block.setWidth(text, value = 80F)
    engine.block.setHeight(text, value = 10F)
    engine.block.appendChild(parent = page, child = text)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setFill(block = block, fill = imageFill)
    engine.block.setPositionX(block, value = 0F)
    engine.block.setPositionY(block, value = 0F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.appendChild(parent = page, child = block)

    engine.block.sendToBack(block)
    engine.block.forceLoadResources(listOf(block))
    val difference = engine.block.combine(listOf(block, text), op = BooleanOperation.DIFFERENCE)

    engine.stop()
}
```

You can use four different boolean operations on blocks to combine them into unique shapes. These operations are:

- `'Union'`: adds all the blocks' shapes into one
- `'Difference'`: removes from the bottom-most block the shapes of the other blocks overlapping with it
- `'Intersection'`: keeps only the overlapping parts of all the blocks' shapes
- `'XOR'`: removes the overlapping parts of all the block's shapes

Combining blocks allows you to create a new block with a customized shape.

Combining blocks with the `union`, `intersection` or `XOR` operation will result in the new block whose fill is that of the top-most block and whose shape is the result of applying the operation pair-wise on blocks from the top-most block to the bottom-most block.

Combining blocks with the `difference` operation will result in the new block whose fill is that of the bottom-most block and whose shape is the result of applying the operation pair-wise on blocks from the bottom-most block to the top-most block.

The combined blocks will be destroyed.

> **Note:** **Only the following blocks can be combined*** A graphics block
> * A text block

```kotlin
fun isCombinable(blocks: List<DesignBlock>): Boolean
```

Checks whether blocks could be combined. Only graphics blocks and text blocks can be combined. All blocks must have the "lifecycle/duplicate" scope enabled.

- `blocks`: blocks for which the confirm combinability.
- Returns whether the blocks can be combined or an error.

```kotlin
fun combine(
    blocks: List<DesignBlock>,
    op: BooleanOperation,
): DesignBlock
```

Perform a boolean operation on the given blocks. All blocks must be combinable. See `isCombinable`. The parent, fill and sort order of the new block is that of the prioritized block. When performing a `Union`, `Intersection` or `XOR`, the operation is performed pair-wise starting with the element with the highest sort order. When performing a `Difference`, the operation is performed pair-wise starting with the element with the lowest sort order.

Required scopes: "lifecycle/duplicate", "lifecycle/destroy"

- `blocks`: blocks to combine. They will be destroyed if "lifecycle/destroy" scope is enabled.
- `op`: boolean operation to perform.
- Returns the newly created block or an error.

Here's the full code:

```kotlin
// Create blocks and append to scene
val star = engine.block.create(DesignBlockType.STAR_SHAPE)
val rect = engine.block.create(DesignBlockType.RECT_SHAPE)
engine.block.appendChild(scene, child = star)
engine.block.appendChild(scene, child = rect)

// Check whether the blocks may be combined
if (engine.block.isCombinable(listOf(star, rect))) {
	val combined = engine.block.combine(listOf(star, rect), op = BooleanOperation.UNION)
}
```

## Combining three circles together

We create three circles and arrange in a recognizable pattern.
Combing them with `'Union'` result in a single block with a unique shape.
The result will inherit the top-most block's fill, in this case `circle3`'s fill.

```kotlin highlight-combine-union
val circle1 = engine.block.create(DesignBlockType.Graphic)
```

To create a special effect of text punched out from an image, we create an image and a text.
We ensure that the image is at the bottom as that is the base block from which we want to remove shapes.
The result will be a block with the size, shape and fill of the image but with a hole in it in the shape of the removed text.

```kotlin highlight-combine-difference
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.replaceText(text, "Removed text")
    engine.block.setPositionX(text, value = 10F)
    engine.block.setPositionY(text, value = 40F)
    engine.block.setWidth(text, value = 80F)
    engine.block.setHeight(text, value = 10F)
    engine.block.appendChild(parent = page, child = text)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setFill(block = block, fill = imageFill)
    engine.block.setPositionX(block, value = 0F)
    engine.block.setPositionY(block, value = 0F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.appendChild(parent = page, child = block)

    engine.block.sendToBack(block)
    engine.block.forceLoadResources(listOf(block))
    val difference = engine.block.combine(listOf(block, text), op = BooleanOperation.DIFFERENCE)
```

### Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.BooleanOperation
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingBoolOps(
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

    val circle1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle1, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle1, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle1, value = 30F)
    engine.block.setPositionY(circle1, value = 30F)
    engine.block.setWidth(circle1, value = 40F)
    engine.block.setHeight(circle1, value = 40F)
    engine.block.appendChild(parent = page, child = circle1)

    val circle2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle2, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle2, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle2, value = 80F)
    engine.block.setPositionY(circle2, value = 30F)
    engine.block.setWidth(circle2, value = 40F)
    engine.block.setHeight(circle2, value = 40F)
    engine.block.appendChild(parent = page, child = circle2)

    val circle3 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(circle3, shape = engine.block.createShape(ShapeType.Ellipse))
    engine.block.setFill(circle3, fill = engine.block.createFill(FillType.Color))
    engine.block.setPositionX(circle3, value = 50F)
    engine.block.setPositionY(circle3, value = 50F)
    engine.block.setWidth(circle3, value = 50F)
    engine.block.setHeight(circle3, value = 50F)
    engine.block.appendChild(parent = page, child = circle3)

    engine.block.combine(listOf(circle1, circle2, circle3), op = BooleanOperation.UNION)

    val text = engine.block.create(DesignBlockType.Text)
    engine.block.replaceText(text, "Removed text")
    engine.block.setPositionX(text, value = 10F)
    engine.block.setPositionY(text, value = 40F)
    engine.block.setWidth(text, value = 80F)
    engine.block.setHeight(text, value = 10F)
    engine.block.appendChild(parent = page, child = text)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setFill(block = block, fill = imageFill)
    engine.block.setPositionX(block, value = 0F)
    engine.block.setPositionY(block, value = 0F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)
    engine.block.setString(
        block = imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.appendChild(parent = page, child = block)

    engine.block.sendToBack(block)
    engine.block.forceLoadResources(listOf(block))
    val difference = engine.block.combine(listOf(block, text), op = BooleanOperation.DIFFERENCE)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
