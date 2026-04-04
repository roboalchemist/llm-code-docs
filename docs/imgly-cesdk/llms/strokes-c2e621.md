# Source: https://img.ly/docs/cesdk/android/outlines/strokes-c2e621/

---
title: "Using Strokes"
description: "Add and customize outlines around shapes, text, or images using stroke settings."
platform: android
url: "https://img.ly/docs/cesdk/android/outlines/strokes-c2e621/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Outlines](https://img.ly/docs/cesdk/android/outlines-b7820c/) > [Stroke (Outline)](https://img.ly/docs/cesdk/android/outlines/strokes-c2e621/)

---

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify strokes through the `block` API. Strokes can be added to any shape or text and stroke styles are varying from plain solid lines to dashes and gaps of varying lengths and can have different end caps.

## Strokes

```kotlin
fun supportsStroke(block: DesignBlock): Boolean
```

Query if the given block has a stroke property.

- `block`: the block to query.
- Returns true if the block has a stroke property, false otherwise.

```kotlin
fun setStrokeEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the stroke of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke should be enabled or disabled.
- `enabled`: if true, the stroke will be enabled.

```kotlin
fun isStrokeEnabled(block: DesignBlock): Boolean
```

Query if the stroke of the given design block is enabled.

- `block`: the block whose stroke state should be queried.
- Returns true if the block's stroke is enabled, false otherwise.

```kotlin
fun setStrokeColor(
    block: DesignBlock,
    color: Color,
)
```

Set the stroke color of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke color should be set.
- `color`: the color to set.

```kotlin
fun getStrokeColor(block: DesignBlock): Color
```

Get the stroke color of the given design block.

- `block`: he block whose stroke color should be queried.
- Returns the stroke color.

```kotlin
fun setStrokeWidth(
    block: DesignBlock,
    width: Float,
)
```

Set the stroke width of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke width should be set.
- `width`: the stroke width to be set.

```kotlin
fun getStrokeWidth(block: DesignBlock): Float
```

Get the stroke width of the given design block.

- `block`: the block whose stroke width should be queried.
- Returns the stroke's width.

```kotlin
fun setStrokeStyle(
    block: DesignBlock,
    style: StrokeStyle,
)
```

Set the stroke style of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke style should be set.
- `style`: the stroke style to be set.

```kotlin
fun getStrokeStyle(block: DesignBlock): StrokeStyle
```

Get the stroke style of the given design block.

- `block`: the block whose stroke style should be queried.
- Returns the stroke's style.

```kotlin
fun setStrokePosition(
    block: DesignBlock,
    position: StrokePosition,
)
```

Set the stroke position of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke position should be set.
- `position`: the stroke position to be set.

```kotlin
fun getStrokePosition(block: DesignBlock): StrokePosition
```

Get the stroke position of the given design block.

- `block`: the block whose stroke position should be queried.
- Returns the stroke position.

```kotlin
fun setStrokeCornerGeometry(
    block: DesignBlock,
    geometry: StrokeCornerGeometry,
)
```

Set the stroke corner geometry of the given design block.

Required scope: "stroke/change"

- `block`: the block whose stroke join geometry should be set.
- `geometry`: the stroke join geometry to be set.

```kotlin
fun getStrokeCornerGeometry(block: DesignBlock): StrokeCornerGeometry
```

Get the stroke corner geometry of the given design block.

- `block`: the block whose stroke join geometry should be queried.
- Returns the stroke join geometry.

## Full Code

Here's the full code for using strokes:

```kotlin
// Check if block supports strokes
if (engine.block.supportsStroke(block)) {
	// Enable the stroke
	engine.block.setStrokeEnabled(block, enabled = true)
	val strokeIsEnabled = engine.block.isStrokeEnabled(block)

	// Configure it
	engine.block.setStrokeColor(block, color = Color.fromRGBA(r = 1F, g = 0.75F, b = 0.8F, a = 1F))
	val strokeColor = engine.block.getStrokeColor(block)
	engine.block.setStrokeWidth(block, width = 5F)
	val strokeWidth = engine.block.getStrokeWidth(block)
	engine.block.setStrokeStyle(block, style = StrokeStyle.DASHED)
	val strokeStyle = engine.block.getStrokeStyle(block)
	engine.block.setStrokePosition(block, position = StrokePosition.OUTER)
	val strokePosition = engine.block.getStrokePosition(block)
	engine.block.setStrokeCornerGeometry(block, geometry = StrokeCornerGeometry.ROUND)
	val strokeCornerGeometry = engine.block.getStrokeCornerGeometry(block)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
