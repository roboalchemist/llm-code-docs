# Source: https://img.ly/docs/cesdk/android/create-composition/blend-modes-ad3519/

---
title: "Blend Modes"
description: "Apply blend modes to elements to control how colors and layers interact visually."
platform: android
url: "https://img.ly/docs/cesdk/android/create-composition/blend-modes-ad3519/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/android/create-composition-db709c/) > [Blend Modes](https://img.ly/docs/cesdk/android/create-composition/blend-modes-ad3519/)

---

```kotlin reference-only
engine.block.supportsOpacity(image)
engine.block.setOpacity(image, value = 0.5F)
engine.block.getOpacity(image)

engine.block.supportsBlendMode(image)
engine.block.setBlendMode(image, blendMode = BlendMode.MULTIPLY)
engine.block.getBlendMode(image)

if (engine.block.supportsBackgroundColor(image)) {
    engine.block.setBackgroundColor(page, Color.fromRGBA(r = 1F, g = 0F, b = 0F, a = 1F) // Red
    engine.block.getBackgroundColor(page)
    engine.block.setBackgroundColorEnabled(page, enabled = true)
    engine.block.isBackgroundColorEnabled(page)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify a blocks appearance through the `block` API.

## Common Properties

Common properties are properties that occur on multiple block types. For instance, fill color properties are available for all the shape blocks and the text block. That's why we built convenient setter and getter functions for these properties. So you don't have to use the generic setters and getters and don't have to provide a specific property path. There are also `has*` functions to query if a block supports a set of common properties.

### Opacity

Set the translucency of the entire block.

```kotlin
fun supportsOpacity(block: DesignBlock): Boolean
```

Query if the given block has an opacity.

- `block`: the block to query.

- Returns true if the block has an opacity, false otherwise.

```kotlin
fun setOpacity(
    block: DesignBlock,
    @FloatRange(from = 0.0, to = 1.0) value: Float,
)
```

Set the opacity of the given design block.

Required scope: "layer/opacity"

- `block`: the block whose opacity should be set.

- `value`: the opacity to be set. The valid range is 0 to 1.

```kotlin
@FloatRange(from = 0.0, to = 1.0)
fun getOpacity(block: DesignBlock): Float
```

Get the opacity of the given design block.

- `block`: the block whose opacity should be queried.

- Returns the opacity.

### Blend Mode

Define the blending behaviour of a block.

```kotlin
fun supportsBlendMode(block: DesignBlock): Boolean
```

Query if the given block has a blend mode.

- `block`: the block to query.

- Returns true if the block has a blend mode, false otherwise.

```kotlin
fun setBlendMode(
    block: DesignBlock,
    blendMode: BlendMode,
)
```

Set the blend mode of the given design block.

Required scope: "layer/blendMode"

- `block`: the block whose blend mode should be set.

- `blendMode`: the blend mode to be set.

```kotlin
fun getBlendMode(block: DesignBlock): BlendMode
```

Get the blend mode of the given design block.

- `block`: the block whose blend mode should be queried.

- Returns the blend mode.

### Background Color

Manipulate the background of a block.

To understand the difference between fill and background color take the text block. The glyphs of the text itself are colored by the fill color. The rectangular background given by the bounds of the block on which the text is drawn is colored by the background color.

```kotlin
fun supportsBackgroundColor(block: DesignBlock): Boolean
```

Query if the given block has background color properties.

- `block`: the block to query.

- Returns true if the block has background color properties, false otherwise.

```kotlin
fun setBackgroundColor(
    block: DesignBlock,
    color: RGBAColor,
)
```

Set the background color of the given design block.

Required scope: "fill/change"

- `block`: the block whose background color should be set.

- `color`: the color to set.

```kotlin
fun getBackgroundColor(block: DesignBlock): RGBAColor
```

Get the background color of the given design block.

- `block`: the block whose background color should be queried.

- Returns the background color.

```kotlin
fun setBackgroundColorEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the background of the given design block.

Required scope: "fill/change"

- `block`: the block whose background should be enabled or disabled.

- `enabled`: if true, the background will be enabled.

```kotlin
fun isBackgroundColorEnabled(block: DesignBlock): Boolean
```

Query if the background of the given design block is enabled.

- `block`: the block whose background state should be queried.

- Returns true if background is enabled, false otherwise.

## Full Code

Here's the full code:

```kotlin
engine.block.supportsOpacity(image)
engine.block.setOpacity(image, value = 0.5F)
engine.block.getOpacity(image)

engine.block.supportsBlendMode(image)
engine.block.setBlendMode(image, blendMode = BlendMode.MULTIPLY)
engine.block.getBlendMode(image)

if (engine.block.supportsBackgroundColor(image)) {
    engine.block.setBackgroundColor(page, Color.fromRGBA(r = 1F, g = 0F, b = 0F, a = 1F) // Red
    engine.block.getBackgroundColor(page)
    engine.block.setBackgroundColorEnabled(page, enabled = true)
    engine.block.isBackgroundColorEnabled(page)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
