# Source: https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-filters-c796ba/

---
title: "Add a Filter or Effect"
description: "Programmatically or manually add effects to design elements to modify their visual style."
platform: android
url: "https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-filters-c796ba/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Filters and Effects](https://img.ly/docs/cesdk/android/filters-and-effects-6f88ac/) > [Create Custom Filters](https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-filters-c796ba/)

---

```kotlin file=@cesdk_android_examples/engine-guides-using-effects/UsingEffects.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.EffectType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingEffects(
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
    engine.block.setPositionX(block, value = 100F)
    engine.block.setPositionY(block, value = 50F)
    engine.block.setWidth(block, value = 300F)
    engine.block.setHeight(block, value = 300F)
    engine.block.appendChild(parent = page, child = block)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = fill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(block, fill = fill)

    engine.block.supportsEffects(scene) // Returns false
    engine.block.supportsEffects(block) // Returns true

    val pixelize = engine.block.createEffect(type = EffectType.Pixelize)
    val adjustments = engine.block.createEffect(type = EffectType.Adjustments)

    engine.block.appendEffect(block, effectBlock = pixelize)
    engine.block.insertEffect(block, effectBlock = adjustments, index = 0)
    // engine.block.removeEffect(rect, index = 0)

    // This will return [adjustments, pixelize]
    val effectsList = engine.block.getEffects(block)

    val unusedEffect = engine.block.createEffect(type = EffectType.HalfTone)
    engine.block.destroy(unusedEffect)

    val allPixelizeProperties = engine.block.findAllProperties(pixelize)
    val allAdjustmentProperties = engine.block.findAllProperties(adjustments)

    engine.block.setInt(pixelize, property = "pixelize/horizontalPixelSize", value = 20)
    engine.block.setFloat(adjustments, property = "effect/adjustments/brightness", value = 0.2F)

    engine.block.setEffectEnabled(pixelize, enabled = false)
    engine.block.setEffectEnabled(pixelize, !engine.block.isEffectEnabled(pixelize))

    engine.stop()
}
```

Some [design blocks](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) in CE.SDK such as pages and graphic blocks allow you to add effects to them. An effect can modify the visual output of a block's [fill](https://img.ly/docs/cesdk/android/fills-402ddc/). CreativeEditor SDK supports many different types of effects, such as adjustments, LUT filters, pixelization, glow, vignette and more.

Similarly to blocks, each effect instance has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

We create a scene containing a graphic block with an image fill and want to apply effects to this image.

```kotlin highlight-setup
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
    engine.block.setPositionX(block, value = 100F)
    engine.block.setPositionY(block, value = 50F)
    engine.block.setWidth(block, value = 300F)
    engine.block.setHeight(block, value = 300F)
    engine.block.appendChild(parent = page, child = block)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = fill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(block, fill = fill)
```

## Accessing Effects

Not all types of design blocks support effects, so you should always first call the `fun supportsEffects(block: DesignBlock): Boolean` API before accessing any of the following APIs.

```kotlin highlight-supportsEffects
engine.block.supportsEffects(scene) // Returns false
engine.block.supportsEffects(block) // Returns true
```

## Creating an Effect

In order to add effects to our block, we first have to create a new effect instance, which we can do by calling `fun createEffect(type: EffectType): DesignBlock` and passing it the type of effect that we want. In this example, we create a pixelization and an adjustment effect.

Please refer to [API Docs](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for a complete list of supported effect types.

```kotlin highlight-createEffect
val pixelize = engine.block.createEffect(type = EffectType.Pixelize)
val adjustments = engine.block.createEffect(type = EffectType.Adjustments)
```

## Adding Effects

Now we have two effects but the output of our scene looks exactly the same as before. That is because we still need to append these effects to the graphic design block's list of effects, which we can do by calling `fun appendEffect(block: DesignBlock, effectBlock: DesignBlock)`.

We can also insert or remove effects from specific indices of a block's effect list using the `fun insertEffect(block: DesignBlock, effectBlock: DesignBlock, index: Int)` and `fun removeEffect(block: DesignBlock, index: Int)` APIs.

Effects will be applied to the block in the order they are placed in the block's effects list. If the same effect appears multiple times in the list, it will also be applied multiple times. In our case, the adjustments effect will be applied to the image first, before the result of that is then pixelated.

```kotlin highlight-addEffect
engine.block.appendEffect(block, effectBlock = pixelize)
engine.block.insertEffect(block, effectBlock = adjustments, index = 0)
// engine.block.removeEffect(rect, index = 0)
```

## Querying Effects

Use the `fun getEffects(block: DesignBlock): List<DesignBlock>` API to query the ordered list of effect ids of a block.

```kotlin highlight-getEffects
// This will return [adjustments, pixelize]
val effectsList = engine.block.getEffects(block)
```

## Destroying Effects

If we created an effect that we don't want anymore, we have to make sure to destroy it using the same `fun destroy(block: DesignBlock)` API that we also call for design blocks.

Effects that are attached to a design block will be automatically destroyed when the design block is destroyed.

```kotlin highlight-destroyEffect
val unusedEffect = engine.block.createEffect(type = EffectType.HalfTone)
engine.block.destroy(unusedEffect)
```

## Effect Properties

Just like design blocks, effects with different types have different properties that you can query and modify via the API. Use `fun findAllProperties(block: DesignBlock): List<String>` in order to get a list of all properties of a given effect.

Please refer to the [API Docs](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for a complete list of all available properties for each type of effect.

```kotlin highlight-getProperties
val allPixelizeProperties = engine.block.findAllProperties(pixelize)
val allAdjustmentProperties = engine.block.findAllProperties(adjustments)
```

Once we know the property keys of an effect, we can use the same APIs as for design blocks in order to [modify those properties](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/).

Our adjustment effect here for example will not modify the output unless we at least change one of its adjustment properties - such as the brightness - to not be zero.

```kotlin highlight-modifyProperties
engine.block.setInt(pixelize, property = "pixelize/horizontalPixelSize", value = 20)
engine.block.setFloat(adjustments, property = "effect/adjustments/brightness", value = 0.2F)
```

## Disabling Effects

You can temporarily disable and enable the individual effects using the `fun setEffectEnabled(effectBlock: DesignBlock, enabled: Boolean)` API. When the effects are applied to a block, all disabled effects are simply skipped. Whether an effect is currently enabled or disabled can be queried with `fun isEffectEnabled(effectBlock: DesignBlock): Boolean`.

```kotlin highlight-disableEffect
engine.block.setEffectEnabled(pixelize, enabled = false)
engine.block.setEffectEnabled(pixelize, !engine.block.isEffectEnabled(pixelize))
```

## Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.EffectType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun usingEffects(
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
    engine.block.setPositionX(block, value = 100F)
    engine.block.setPositionY(block, value = 50F)
    engine.block.setWidth(block, value = 300F)
    engine.block.setHeight(block, value = 300F)
    engine.block.appendChild(parent = page, child = block)
    val fill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        block = fill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )
    engine.block.setFill(block, fill = fill)

    engine.block.supportsEffects(scene) // Returns false
    engine.block.supportsEffects(block) // Returns true

    val pixelize = engine.block.createEffect(type = EffectType.Pixelize)
    val adjustments = engine.block.createEffect(type = EffectType.Adjustments)

    engine.block.appendEffect(block, effectBlock = pixelize)
    engine.block.insertEffect(block, effectBlock = adjustments, index = 0)
    // engine.block.removeEffect(rect, index = 0)

    // This will return [adjustments, pixelize]
    val effectsList = engine.block.getEffects(block)

    val unusedEffect = engine.block.createEffect(type = EffectType.HalfTone)
    engine.block.destroy(unusedEffect)

    val allPixelizeProperties = engine.block.findAllProperties(pixelize)
    val allAdjustmentProperties = engine.block.findAllProperties(adjustments)

    engine.block.setInt(pixelize, property = "pixelize/horizontalPixelSize", value = 20)
    engine.block.setFloat(adjustments, property = "effect/adjustments/brightness", value = 0.2F)

    engine.block.setEffectEnabled(pixelize, enabled = false)
    engine.block.setEffectEnabled(pixelize, !engine.block.isEffectEnabled(pixelize))

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
