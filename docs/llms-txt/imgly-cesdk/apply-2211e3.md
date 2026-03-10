# Source: https://img.ly/docs/cesdk/android/colors/apply-2211e3/

---
title: "Apply Colors"
description: "Apply solid colors to shapes, backgrounds, and other design elements."
platform: android
url: "https://img.ly/docs/cesdk/android/colors/apply-2211e3/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/android/colors-a9b79c/) > [Apply Color](https://img.ly/docs/cesdk/android/colors/apply-2211e3/)

---

```kotlin file=@cesdk_android_examples/engine-guides-colors/Colors.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.ColorSpace
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun colors(
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

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(block, value = 350F)
    engine.block.setPositionY(block, value = 400F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)

    val fill = engine.block.createFill(FillType.Color)
    engine.block.setFill(block, fill = fill)

    val rgbaBlue = Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F)
    val cmykRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 1F)
    val cmykPartialRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 0.5F)

    engine.editor.setSpotColor(
        name = "Pink-Flamingo",
        Color.fromRGBA(r = 0.988F, g = 0.455F, b = 0.992F),
    )
    engine.editor.setSpotColor(name = "Yellow", Color.fromCMYK(c = 0F, m = 0F, y = 1F, k = 0F))
    val spotPinkFlamingo = Color.fromSpotColor(
        name = "Pink-Flamingo",
        tint = 1F,
        externalReference = "Crayola",
    )
    val spotPartialYellow = Color.fromSpotColor(name = "Yellow", tint = 0.3F)

    engine.block.setColor(fill, property = "fill/color/value", value = rgbaBlue)
    engine.block.setColor(fill, property = "fill/color/value", value = cmykRed)
    engine.block.setColor(block, property = "stroke/color", value = cmykPartialRed)
    engine.block.setColor(fill, property = "fill/color/value", value = spotPinkFlamingo)
    engine.block.setColor(block, property = "dropShadow/color", value = spotPartialYellow)

    val cmykBlueConverted = engine.editor.convertColorToColorSpace(
        rgbaBlue,
        colorSpace = ColorSpace.CMYK,
    )
    val rgbaPinkFlamingoConverted = engine.editor.convertColorToColorSpace(
        spotPinkFlamingo,
        colorSpace = ColorSpace.SRGB,
    )

    engine.editor.findAllSpotColors() // ["Crayola-Pink-Flamingo", "Yellow"]

    engine.editor.setSpotColor("Yellow", Color.fromCMYK(c = 0.2F, m = 0F, y = 1F, k = 0F))

    engine.editor.removeSpotColor("Yellow")

    engine.stop()
}
```

## Setup the scene

We first create a new scene with a graphic block that has color fill.

```kotlin highlight-setup
    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(block, value = 350F)
    engine.block.setPositionY(block, value = 400F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)

    val fill = engine.block.createFill(FillType.Color)
    engine.block.setFill(block, fill = fill)
```

## Create colors

Here we instantiate a few colors with RGB and CMYK color spaces.
We also define two spot colors, one with an RGB approximation and another with a CMYK approximation.
Note that a spot colors can have both color space approximations.

```kotlin highlight-create-colors
    val rgbaBlue = Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F)
    val cmykRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 1F)
    val cmykPartialRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 0.5F)

    engine.editor.setSpotColor(
        name = "Pink-Flamingo",
        Color.fromRGBA(r = 0.988F, g = 0.455F, b = 0.992F),
    )
    engine.editor.setSpotColor(name = "Yellow", Color.fromCMYK(c = 0F, m = 0F, y = 1F, k = 0F))
    val spotPinkFlamingo = Color.fromSpotColor(
        name = "Pink-Flamingo",
        tint = 1F,
        externalReference = "Crayola",
    )
    val spotPartialYellow = Color.fromSpotColor(name = "Yellow", tint = 0.3F)
```

## Applying colors to a block

We can use the defined colors to modify certain properties of a fill or properties of a shape.
Here we apply it to `'fill/color/value'`, `'stroke/color'` and `'dropShadow/color'`.

```kotlin highlight-apply-colors
engine.block.setColor(fill, property = "fill/color/value", value = rgbaBlue)
engine.block.setColor(fill, property = "fill/color/value", value = cmykRed)
engine.block.setColor(block, property = "stroke/color", value = cmykPartialRed)
engine.block.setColor(fill, property = "fill/color/value", value = spotPinkFlamingo)
engine.block.setColor(block, property = "dropShadow/color", value = spotPartialYellow)
```

## Converting colors

Using the utility function `convertColorToColorSpace` we create a new color in the CMYK color space by converting the `rgbaBlue` color to the CMYK color space.
We also create a new color in the RGB color space by converting the `spotPinkFlamingo` color to the RGB color space.

```kotlin highlight-convert-color
val cmykBlueConverted = engine.editor.convertColorToColorSpace(
    rgbaBlue,
    colorSpace = ColorSpace.CMYK,
)
val rgbaPinkFlamingoConverted = engine.editor.convertColorToColorSpace(
    spotPinkFlamingo,
    colorSpace = ColorSpace.SRGB,
)
```

## Listing spot colors

This function returns the list of currently defined spot colors.

```kotlin highlight-find-spot
engine.editor.findAllSpotColors() // ["Crayola-Pink-Flamingo", "Yellow"]
```

## Redefine a spot color

We can re-define the RGB and CMYK approximations of an already defined spot color.
Doing so will change the rendered color of the blocks.
We change it for the CMYK approximation of `'Yellow'` and make it a bit greenish.
The properties that have `'Yellow'` as their spot color will change when re-rendered.

```kotlin highlight-change-spot
engine.editor.setSpotColor("Yellow", Color.fromCMYK(c = 0.2F, m = 0F, y = 1F, k = 0F))
```

## Removing the definition of a spot color

We can undefine a spot color.
Doing so will make all the properties still referring to that spot color (`'Yellow'` in this case) use the default magenta RGB approximation.

```kotlin highlight-undefine-spot
engine.editor.removeSpotColor("Yellow")
```

## Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.ColorSpace
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun colors(
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

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, shape = engine.block.createShape(ShapeType.Rect))
    engine.block.setPositionX(block, value = 350F)
    engine.block.setPositionY(block, value = 400F)
    engine.block.setWidth(block, value = 100F)
    engine.block.setHeight(block, value = 100F)

    val fill = engine.block.createFill(FillType.Color)
    engine.block.setFill(block, fill = fill)

    val rgbaBlue = Color.fromRGBA(r = 0F, g = 0F, b = 1F, a = 1F)
    val cmykRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 1F)
    val cmykPartialRed = Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F, tint = 0.5F)

    engine.editor.setSpotColor(
        name = "Pink-Flamingo",
        Color.fromRGBA(r = 0.988F, g = 0.455F, b = 0.992F),
    )
    engine.editor.setSpotColor(name = "Yellow", Color.fromCMYK(c = 0F, m = 0F, y = 1F, k = 0F))
    val spotPinkFlamingo = Color.fromSpotColor(
        name = "Pink-Flamingo",
        tint = 1F,
        externalReference = "Crayola",
    )
    val spotPartialYellow = Color.fromSpotColor(name = "Yellow", tint = 0.3F)

    engine.block.setColor(fill, property = "fill/color/value", value = rgbaBlue)
    engine.block.setColor(fill, property = "fill/color/value", value = cmykRed)
    engine.block.setColor(block, property = "stroke/color", value = cmykPartialRed)
    engine.block.setColor(fill, property = "fill/color/value", value = spotPinkFlamingo)
    engine.block.setColor(block, property = "dropShadow/color", value = spotPartialYellow)

    val cmykBlueConverted = engine.editor.convertColorToColorSpace(
        rgbaBlue,
        colorSpace = ColorSpace.CMYK,
    )
    val rgbaPinkFlamingoConverted = engine.editor.convertColorToColorSpace(
        spotPinkFlamingo,
        colorSpace = ColorSpace.SRGB,
    )

    engine.editor.findAllSpotColors() // ["Crayola-Pink-Flamingo", "Yellow"]

    engine.editor.setSpotColor("Yellow", Color.fromCMYK(c = 0.2F, m = 0F, y = 1F, k = 0F))

    engine.editor.removeSpotColor("Yellow")

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
