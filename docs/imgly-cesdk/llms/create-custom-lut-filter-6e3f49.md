# Source: https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-lut-filter-6e3f49/

---
title: "Create a Custom LUT Filter"
description: "Create and apply custom LUT filters to achieve consistent, brand-aligned visual styles."
platform: android
url: "https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-lut-filter-6e3f49/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Filters and Effects](https://img.ly/docs/cesdk/android/filters-and-effects-6f88ac/) > [Apply Custom LUT Filter](https://img.ly/docs/cesdk/android/filters-and-effects/create-custom-lut-filter-6e3f49/)

---

```kotlin file=@cesdk_android_examples/engine-guides-custom-lut-filter/CustomLUTFilter.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.EffectType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun customLUTFilter(
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
    engine.block.setWidth(page, value = 100F)
    engine.block.setHeight(page, value = 100F)
    engine.block.appendChild(parent = scene, child = page)
    engine.scene.zoomToBlock(
        scene,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val rect = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(rect, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setWidth(rect, value = 100F)
    engine.block.setHeight(rect, value = 100F)
    engine.block.appendChild(parent = page, child = rect)

    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )

    val lutFilter = engine.block.createEffect(EffectType.LutFilter)
    engine.block.setBoolean(lutFilter, property = "effect/enabled", value = true)
    engine.block.setFloat(lutFilter, property = "effect/lut_filter/intensity", value = 0.9F)

    @Suppress("ktlint:standard:max-line-length")
    val lutUri = "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png"

    engine.block.setString(
        lutFilter,
        property = "effect/lut_filter/lutFileURI",
        value = lutUri,
    )
    engine.block.setInt(lutFilter, property = "effect/lut_filter/verticalTileCount", value = 5)
    engine.block.setInt(lutFilter, property = "effect/lut_filter/horizontalTileCount", value = 5)

    engine.block.appendEffect(rect, effectBlock = lutFilter)
    engine.block.setFill(rect, fill = imageFill)

    engine.stop()
}
```

We use a technology called Lookup Tables (LUTs) in order to add new filters to our SDK.
The main idea is that colors respond to operations that are carried out during the filtering process. We 'record' that very response by applying the filter to the identity image shown below.

<img src="content-assets/6e3f49/identity.png" alt="Identity LUT" />

The resulting image can be used within our SDK and the recorded changes can then be applied to any image by looking up the transformed colors in the modified LUT.

If you want to create a new filter, you'll need to [download](content-assets/6e3f49/imgly_lut_ad1920_5_5_128.png) the identity LUT shown above, load it into an image editing software of your
choice, apply your operations, save it and add it to your app.

> **WARNING:** As any compression artifacts in the edited LUT could lead to distorted results when applying the filter, you need to save your LUT as a PNG file.

## Using Custom Filters

In this example, we will use a hosted CDN LUT filter file.
First we will load one of our demo scenes and change the first image to use LUT filter we will provide.
We will also configure the necessary setting based on the file.

LUT file we will use:

<img src="content-assets/6e3f49/imgly_lut_ad1920_5_5_128.png" alt="Color grading LUT showcasing a grid of color variations used for applying a specific visual style to images." />

## Load Scene

After the setup, we create a new scene. Within this scene, we create a page, set its dimensions, and append it to the scene. Lastly, we adjust the zoom level to properly fit the page into the view.

```kotlin highlight-load-scene
val page = engine.block.create(DesignBlockType.Page)
engine.block.setWidth(page, value = 100F)
engine.block.setHeight(page, value = 100F)
engine.block.appendChild(parent = scene, child = page)
engine.scene.zoomToBlock(
    scene,
    paddingLeft = 40F,
    paddingTop = 40F,
    paddingRight = 40F,
    paddingBottom = 40F,
)
```

## Create Rectangle

Next, we create a rectangle with defined dimensions and append it to the page. We will apply our LUT filter to this rectangle.

```kotlin highlight-create-rect
val rect = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(rect, shape = engine.block.createShape(ShapeType.Rect))
engine.block.setWidth(rect, value = 100F)
engine.block.setHeight(rect, value = 100F)
engine.block.appendChild(parent = page, child = rect)
```

## Load Image

After creating the rectangle, we create an image fill with a specified URL. This will load the image as a fill for the rectangle to which we will apply the LUT filter.

```kotlin highlight-create-image-fill
val imageFill = engine.block.createFill(FillType.Image)
engine.block.setString(
    imageFill,
    property = "fill/image/imageFileURI",
    value = "https://img.ly/static/ubq_samples/sample_1.jpg",
)
```

## Create LUT Filter

Now, we create a Look-Up Table (LUT) filter effect. We enable the filter, set its intensity, and provide a URL for the LUT file. We also define the tile count for the filter. The LUT filter effect is then applied to the rectangle and image should appear black and white.

```kotlin highlight-create-lut-filter
    val lutFilter = engine.block.createEffect(EffectType.LutFilter)
    engine.block.setBoolean(lutFilter, property = "effect/enabled", value = true)
    engine.block.setFloat(lutFilter, property = "effect/lut_filter/intensity", value = 0.9F)

    @Suppress("ktlint:standard:max-line-length")
    val lutUri = "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png"

    engine.block.setString(
        lutFilter,
        property = "effect/lut_filter/lutFileURI",
        value = lutUri,
    )
    engine.block.setInt(lutFilter, property = "effect/lut_filter/verticalTileCount", value = 5)
    engine.block.setInt(lutFilter, property = "effect/lut_filter/horizontalTileCount", value = 5)
```

## Apply LUT Filter

Finally, we apply the LUT filter effect to the rectangle, and set the image fill to the rectangle.
Before setting an image fill, we destroy the default rectangle fill.

```kotlin highlight-apply-lut-filter
engine.block.appendEffect(rect, effectBlock = lutFilter)
engine.block.setFill(rect, fill = imageFill)
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

fun customLUTFilter(
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
    engine.block.setWidth(page, value = 100F)
    engine.block.setHeight(page, value = 100F)
    engine.block.appendChild(parent = scene, child = page)
    engine.scene.zoomToBlock(
        scene,
        paddingLeft = 40F,
        paddingTop = 40F,
        paddingRight = 40F,
        paddingBottom = 40F,
    )

    val rect = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(rect, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setWidth(rect, value = 100F)
    engine.block.setHeight(rect, value = 100F)
    engine.block.appendChild(parent = page, child = rect)

    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(
        imageFill,
        property = "fill/image/imageFileURI",
        value = "https://img.ly/static/ubq_samples/sample_1.jpg",
    )

    val lutFilter = engine.block.createEffect(EffectType.LutFilter)
    engine.block.setBoolean(lutFilter, property = "effect/enabled", value = true)
    engine.block.setFloat(lutFilter, property = "effect/lut_filter/intensity", value = 0.9F)

    @Suppress("ktlint:standard:max-line-length")
    val lutUri = "https://cdn.img.ly/packages/imgly/cesdk-js/$UBQ_VERSION$/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png"

    engine.block.setString(
        lutFilter,
        property = "effect/lut_filter/lutFileURI",
        value = lutUri,
    )
    engine.block.setInt(lutFilter, property = "effect/lut_filter/verticalTileCount", value = 5)
    engine.block.setInt(lutFilter, property = "effect/lut_filter/horizontalTileCount", value = 5)

    engine.block.appendEffect(rect, effectBlock = lutFilter)
    engine.block.setFill(rect, fill = imageFill)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
