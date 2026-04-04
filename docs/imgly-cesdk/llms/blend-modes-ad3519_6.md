# Source: https://img.ly/docs/cesdk/mac-catalyst/create-composition/blend-modes-ad3519/

---
title: "Blend Modes"
description: "Apply blend modes to elements to control how colors and layers interact visually."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/create-composition/blend-modes-ad3519/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/mac-catalyst/create-composition-db709c/) > [Blend Modes](https://img.ly/docs/cesdk/mac-catalyst/create-composition/blend-modes-ad3519/)

---

```swift reference-only
try engine.block.supportsOpacity(image)
try engine.block.setOpacity(image, value: 0.5)
try engine.block.getOpacity(image)

try engine.block.supportsBlendMode(image)
try engine.block.setBlendMode(image, mode: .multiply)
try engine.block.getBlendMode(image)

if try engine.block.supportsBackgroundColor(image) {
  try engine.block.setBackgroundColor(page, r: 1, g: 0, b: 0, a: 1) // Red
  try engine.block.getBackgroundColor(page)
  try engine.block.setBackgroundColorEnabled(page, enabled: true)
  try engine.block.isBackgroundColorEnabled(page)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify a blocks appearance through the `block` API.

## Common Properties

Common properties are properties that occur on multiple block types. For instance, fill color properties are available for all the shape blocks and the text block. That's why we built convenient setter and getter functions for these properties. So you don't have to use the generic setters and getters and don't have to provide a specific property path. There are also `has*` functions to query if a block supports a set of common properties.

### Opacity

Set the translucency of the entire block.

```swift
public func supportsOpacity(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has an opacity.

- `id:`: The block to query.
- Returns: `true`, if the block has an opacity.

```swift
public func setOpacity(_ id: DesignBlockID, value: Float) throws
```

Set the opacity of the given design block.
Required scope: "layer/opacity"

- `id`: The block whose opacity should be set.
- `value`: The opacity to be set. The valid range is 0 to 1.

```swift
public func getOpacity(_ id: DesignBlockID) throws -> Float
```

Get the opacity of the given design block.

- `id:`: The block whose opacity should be queried.
- Returns: The opacity.

### Blend Mode

Define the blending behaviour of a block.

```swift
public func supportsBlendMode(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has a blend mode.

- `id:`: The block to query.
- Returns: `true`, if the block has a blend mode.

```swift
public func setBlendMode(_ id: DesignBlockID, mode: BlendMode) throws
```

Set the blend mode of the given design block.
Required scope: "layer/blendMode"

- `id`: The block whose blend mode should be set.
- `mode`: The blend mode to be set.

```swift
public func getBlendMode(_ id: DesignBlockID) throws -> BlendMode
```

Get the blend mode of the given design block.

- `id:`: The block whose blend mode should be queried.
- Returns: The blend mode.

### Background Color

Manipulate the background of a block.

To understand the difference between fill and background color take the text block. The glyphs of the text itself are colored by the fill color. The rectangular background given by the bounds of the block on which the text is drawn is colored by the background color.

```swift
public func supportsBackgroundColor(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has background color properties.

- `id:`: The block to query.
- Returns: `true`, if the block has background color properties.

```swift
public func setBackgroundColor(_ id: DesignBlockID, r: Float, g: Float, b: Float, a: Float = 1) throws
```

Set the background color of the given design block.
Required scope: "fill/change"

- `id`: The block whose background color should be set.
- `r`: The red color component in the range of 0 to 1.
- `g`: The green color component in the range of 0 to 1.
- `b`: The blue color component in the range of 0 to 1.
- `a`: The alpha color component in the range of 0 to 1.

```swift
public func getBackgroundColor(_ id: DesignBlockID) throws -> RGBA
```

Get the background color of the given design block.

- `id:`: The block whose background color should be queried.
- Returns: The background color.

```swift
public func setBackgroundColorEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the background of the given design block.
Required scope: "fill/change"

- `id`: The block whose background should be enabled or disabled.
- `enabled`: If `true`, the background will be enabled.

```swift
public func isBackgroundColorEnabled(_ id: DesignBlockID) throws -> Bool
```

Query if the background of the given design block is enabled.

- `id:`: The block whose background state should be queried.
- Returns: `true`, if background is enabled.

## Full Code

Here's the full code:

```swift
try engine.block.supportsOpacity(image)
try engine.block.setOpacity(image, value: 0.5)
try engine.block.getOpacity(image)

try engine.block.supportsBlendMode(image)
try engine.block.setBlendMode(image, mode: .multiply)
try engine.block.getBlendMode(image)

if try engine.block.supportsBackgroundColor(image) {
  try engine.block.setBackgroundColor(page, r: 1, g: 0, b: 0, a: 1) // Red
  try engine.block.getBackgroundColor(page)
  try engine.block.setBackgroundColorEnabled(page, enabled: true)
  try engine.block.isBackgroundColorEnabled(page)
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
