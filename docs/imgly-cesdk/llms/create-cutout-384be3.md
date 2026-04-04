# Source: https://img.ly/docs/cesdk/android/stickers-and-shapes/create-cutout-384be3/

---
title: "Create Cutout"
description: "Create cutouts from images or shapes by masking or removing specific areas."
platform: android
url: "https://img.ly/docs/cesdk/android/stickers-and-shapes/create-cutout-384be3/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Stickers](https://img.ly/docs/cesdk/android/stickers-3d4e5f/) > [Create Cutout](https://img.ly/docs/cesdk/android/stickers-and-shapes/create-cutout-384be3/)

---

```kotlin file=@cesdk_android_examples/engine-guides-cutouts/Cutouts.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.CutoutOperation
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun cutouts(
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

    val circle = engine.block.createCutoutFromPath(
        "M 0,25 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0 Z",
    )
    engine.block.setFloat(circle, "cutout/offset", 3F)
    engine.block.setEnum(circle, "cutout/type", "Dashed")

    val square = engine.block.createCutoutFromPath("M 0,0 H 50 V 50 H 0 Z")
    engine.block.setFloat(square, "cutout/offset", 6F)

    val union = engine.block.createCutoutFromOperation(
        listOf(circle, square),
        op = CutoutOperation.UNION,
    )
    engine.block.destroy(circle)
    engine.block.destroy(square)

    engine.editor.setSpotColor("CutContour", Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F))

    engine.stop()
}
```

Cutouts are a special feature one can use with cuttings printers.
When printing a PDF file containing cutouts paths, a cutting printer will cut these paths with a cutter rather than print them with ink.
Use cutouts to create stickers, iron on decals, etc.

Cutouts can be created from an SVG string describing its underlying shape.
Cutouts can also be created from combining multiple existing cutouts using the boolean operations `UNION`, `DIFFERENCE`, `INTERSECTION` and `XOR`.

Cutouts have a type property which can take one of two values: `SOLID` and `DASHED`.
Cutting printers recognize cutouts paths through their specially named spot colors.
By default, `SOLID` cutouts have the spot color `"CutContour"` to produce a continuous cutting line and `DASHED` cutouts have the spot colors `"PerfCutContour"` to produce a perforated cutting line.
You may need to adjust these spot color names for you printer.

> **Note:** **Note** Note that the actual color approximation given to the spot color does
> not affect how the cutting printer interprets the cutout, only how it is
> rendered. The default color approximations are magenta for "CutContour" and
> green for "PerfCutContour".

Cutouts have an offset property that determines the distance at which the cutout path is rendered from the underlying path set when created.

## Setup the scene

We first create a new scene with a new page.

```kotlin highlight-setup
    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)
```

## Create cutouts

Here we add two cutouts.
First, a circle of type `DASHED` and with an offset of 3.0.
Second, a square of default type `SOLID` and an offset of 6.0.

```kotlin create-cutouts
```

## Combining multiple cutouts into one

Here we use the `UNION` operation to create a new cutout that consists of the combination of the earlier two cutouts we have created.
Note that we destroy the previously created `circle` and `square` cutouts as we don't need them anymore and we certainly don't want to printer to cut through those paths as well.

When combining multiple cutouts, the resulting cutout will be of the type of the first cutout given and an offset of 0.
In this example, since the `circle` cutout is of type `DASHED`, the newly created cutout will also be of type `DASHED`.

> **Note:** **Warning** When using the Difference operation, the first cutout is the
> cutout that is subtracted <em>from</em>. For other operations, the order of
> the cutouts don't matter.

```kotlin highlight-cutout-union
val union = engine.block.createCutoutFromOperation(
    listOf(circle, square),
    op = CutoutOperation.UNION,
)
engine.block.destroy(circle)
engine.block.destroy(square)
```

## Change the default color for Solid cutouts

For some reason, we'd like the cutouts of type `SOLID` to not render as magenta but as blue.
Knowing that `"CutContour"` is the spot color associated with `SOLID`, we change it RGB approximation to blue.
Thought the cutout will render as blue, the printer will still interpret this path as a cutting because of its special spot color name.

```kotlin highlight-spot-color-solid
engine.editor.setSpotColor("CutContour", Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F))
```

## Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.*
import ly.img.engine.*

fun cutouts(
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

    val circle =
        engine.block.createCutoutFromPath(
            "M 0,25 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0 Z",
        )
    engine.block.setFloat(circle, "cutout/offset", 3F)
    engine.block.setEnum(circle, "cutout/type", CutoutType.DASHED.key)

    val square = engine.block.createCutoutFromPath("M 0,0 H 50 V 50 H 0 Z")
    engine.block.setFloat(square, "cutout/offset", 6F)

    val union =
        engine.block.createCutoutFromOperation(
            listOf(circle, square),
            op = CutoutOperation.UNION,
        )
    engine.block.destroy(circle)
    engine.block.destroy(square)

    engine.editor.setSpotColor("CutContour", Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F))

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
