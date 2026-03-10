# Source: https://img.ly/docs/cesdk/android/outlines/shadows-and-glows-6610fa/

---
title: "Shadows and Glows"
description: "Apply shadow and glow effects to elements for added depth, contrast, or emphasis."
platform: android
url: "https://img.ly/docs/cesdk/android/outlines/shadows-and-glows-6610fa/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Outlines](https://img.ly/docs/cesdk/android/outlines-b7820c/) > [Shadows and Glows](https://img.ly/docs/cesdk/android/outlines/shadows-and-glows-6610fa/)

---

```kotlin reference-only
// Configure a basic colored drop shadow if the block supports them
if (engine.block.supportsDropShadow(block)) {
    engine.block.setDropShadowEnabled(block, enabled = true)
    engine.block.setDropShadowColor(block, Color.fromRGBA(r = 1F, g = 0.75F, b = 0.8F, a = 1F))
    val dropShadowColor = engine.block.getDropShadowColor(block)
    engine.block.setDropShadowOffsetX(block, offsetX = -10F)
    engine.block.setDropShadowOffsetY(block, offsetY = 5F)
    val dropShadowOffsetX = engine.block.getDropShadowOffsetX(block);
    val dropShadowOffsetY = engine.block.getDropShadowOffsetY(block);
    engine.block.setDropShadowBlurRadiusX(block, blurRadiusX = -10F)
    engine.block.setDropShadowBlurRadiusY(block, blurRadiusY = 5F)
    engine.block.setDropShadowClip(block, clip = false)
    val dropShadowClip = engine.block.getDropShadowClip(block)

    // Query a blocks drop shadow properties
    val dropShadowIsEnabled = engine.block.isDropShadowEnabled(block)
    val dropShadowBlurRadiusX = engine.block.getDropShadowBlurRadiusX(block)
    val dropShadowBlurRadiusY = engine.block.getDropShadowBlurRadiusY(block)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify an block's drop shadow through the `block` API.
Drop shadows can be added to any shape, text or image.
One can adjust its offset relative to its block on the X and Y axes, its blur factor on the X and Y axes and whether it is visible behind a transparent block.

## Functions

```kotlin
fun supportsDropShadow(block: DesignBlock): Boolean
```

Query if the given block has a drop shadow property.

- `block`: the block to query.

- Returns true if the block has a drop shadow property, false otherwise.

```kotlin
fun setDropShadowEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the drop shadow of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow should be enabled or disabled.

- `enabled`: if true, the drop shadow will be enabled.

```kotlin
fun isDropShadowEnabled(block: DesignBlock): Boolean
```

Query if the drop shadow of the given design block is enabled.

- `block`: the block whose drop shadow should be queried.

- Returns true if the block's drop shadow is enabled, false otherwise.

```kotlin
fun setDropShadowColor(
    block: DesignBlock,
    color: Color,
)
```

Set the drop shadow color of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow color should be set.

- `color`: the color to set.

```kotlin
fun getDropShadowColor(block: DesignBlock): Color
```

Get the drop shadow color of the given design block.

- `block`: the block whose drop shadow color should be queried.

- Returns the drop shadow color.

```kotlin
fun setDropShadowOffsetX(
    block: DesignBlock,
    offsetX: Float,
)
```

Set the drop shadow's x offset of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow's x offset should be set.

- `offsetX`: the x offset to be set.

```kotlin
fun setDropShadowOffsetY(
    block: DesignBlock,
    offsetY: Float,
)
```

Set the drop shadow's y offset of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow's y offset should be set.

- `offsetY`: the y offset to be set.

```kotlin
fun getDropShadowOffsetX(block: DesignBlock): Float
```

Get the drop shadow's x offset of the given design block.

- `block`: the block whose drop shadow's x offset should be queried.

- Returns the offset.

```kotlin
fun getDropShadowOffsetY(block: DesignBlock): Float
```

Get the drop shadow's y offset of the given design block.

- `block`: the block whose drop shadow's y offset should be queried.

- Returns the offset.

```kotlin
fun setDropShadowBlurRadiusX(
    block: DesignBlock,
    blurRadiusX: Float,
)
```

Set the drop shadow's blur radius on the x axis of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow's blur radius on the x axis should be set.

- `blurRadiusX`: the blur radius to be set.

```kotlin
fun setDropShadowBlurRadiusY(
    block: DesignBlock,
    blurRadiusY: Float,
)
```

Set the drop shadow's blur radius on the y axis of the given design block.

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow's blur radius on the y axis should be set.

- `blurRadiusY`: the blur radius to be set.

```kotlin
fun setDropShadowClip(
    block: DesignBlock,
    clip: Boolean,
)
```

Set the drop shadow's clipping of the given design block. (Only applies to shapes.)

Required scope: "appearance/shadow"

- `block`: the block whose drop shadow's clip should be set.

- `clip`: the drop shadow's clip to be set.

```kotlin
fun getDropShadowClip(block: DesignBlock): Boolean
```

Get the drop shadow's clipping of the given design block.

- `block`: the block whose drop shadow's clipping should be queried.

- Returns the drop shadow's clipping.

```kotlin
fun getDropShadowBlurRadiusX(block: DesignBlock): Float
```

Get the drop shadow's blur radius on the x axis of the given design block.

- `block`: the block whose drop shadow's blur radius on the x axis should be queried.

- Returns the blur radius.

```kotlin
fun getDropShadowBlurRadiusY(block: DesignBlock): Float
```

Get the drop shadow's blur radius on the y axis of the given design block.

- `block`: the block whose drop shadow's blur radius on the y axis should be queried.

- Returns the blur radius.

## Full Code

Here's the full code:

```kotlin
// Configure a basic colored drop shadow if the block supports them
if (engine.block.supportsDropShadow(block)) {
    engine.block.setDropShadowEnabled(block, enabled = true)
    engine.block.setDropShadowColor(block, Color.fromRGBA(r = 1F, g = 0.75F, b = 0.8F, a = 1F))
    val dropShadowColor = engine.block.getDropShadowColor(block)
    engine.block.setDropShadowOffsetX(block, offsetX = -10F)
    engine.block.setDropShadowOffsetY(block, offsetY = 5F)
    val dropShadowOffsetX = engine.block.getDropShadowOffsetX(block);
    val dropShadowOffsetY = engine.block.getDropShadowOffsetY(block);
    engine.block.setDropShadowBlurRadiusX(block, blurRadiusX = -10F)
    engine.block.setDropShadowBlurRadiusY(block, blurRadiusY = 5F)
    engine.block.setDropShadowClip(block, clip = false)
    val dropShadowClip = engine.block.getDropShadowClip(block)

    // Query a blocks drop shadow properties
    val dropShadowIsEnabled = engine.block.isDropShadowEnabled(block)
    val dropShadowBlurRadiusX = engine.block.getDropShadowBlurRadiusX(block)
    val dropShadowBlurRadiusY = engine.block.getDropShadowBlurRadiusY(block)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
