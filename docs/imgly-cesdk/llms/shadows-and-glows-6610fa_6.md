# Source: https://img.ly/docs/cesdk/mac-catalyst/outlines/shadows-and-glows-6610fa/

---
title: "Shadows and Glows"
description: "Apply shadow and glow effects to elements for added depth, contrast, or emphasis."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/outlines/shadows-and-glows-6610fa/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Outlines](https://img.ly/docs/cesdk/mac-catalyst/outlines-b7820c/) > [Shadows and Glows](https://img.ly/docs/cesdk/mac-catalyst/outlines/shadows-and-glows-6610fa/)

---

```swift reference-only
// Configure a basic colored drop shadow if the block supports them
if try engine.block.supportsDropShadow(block) {
  try engine.block.setDropShadowEnabled(block, enabled: true)
  try engine.block.setDropShadowColor(block, color: .rgba(r: 1.0, g: 0.75, b: 0.8, a: 1.0))
  let dropShadowColor = try engine.block.getDropShadowColor(block)
  try engine.block.setDropShadowOffsetX(block, offsetX: -10)
  try engine.block.setDropShadowOffsetY(block, offsetY: 5)
  let dropShadowOffsetX = try engine.block.getDropShadowOffsetX(block)
  let dropShadowOffsetX = try engine.block.getDropShadowOffsetY(block)
  try engine.block.setDropShadowBlurRadiusX(block, blurRadiusX: -10)
  try engine.block.setDropShadowBlurRadiusY(block, blurRadiusY: 5)
  try engine.block.setDropShadowClip(block, clip: false)
  let dropShadowClip = try getDropShadowClip(block)

  // Query a blocks drop shadow properties
  let dropShadowIsEnabled = try engine.block.isDropShadowEnabled(block)
  let dropShadowBlurRadiusX = try engine.block.getDropShadowBlurRadiusX(block)
  let dropShadowBlurRadiusY = try engine.block.getDropShadowBlurRadiusY(block)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify an block's drop shadow through the `block` API.
Drop shadows can be added to any shape, text or image.
One can adjust its offset relative to its block on the X and Y axes, its blur factor on the X and Y axes and whether it is visible behind a transparent block.

## Functions

```swift
public func supportsDropShadow(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has a drop shadow property.

- `id:`: The block to query.
- Returns: `true` if the block has a drop shadow property.

```swift
public func setDropShadowEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the drop shadow of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow should be enabled or disabled.
- `enabled`: If `true`, the drop shadow will be enabled.

```swift
public func isDropShadowEnabled(_ id: DesignBlockID) throws -> Bool
```

Query if the drop shadow of the given design block is enabled.

- `id:`: The block whose drop shadow state should be queried.
- Returns: `true` if the block's drop shadow is enabled.

```swift
public func setDropShadowColor(_ id: DesignBlockID, color: Color) throws
```

Set the drop shadow color of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow color should be set.
- `color`: The color to set.

```swift
public func getDropShadowColor(_ id: DesignBlockID) throws -> Color
```

Get the drop shadow color of the given design block.

- `id:`: The block whose drop shadow color should be queried.
- Returns: The drop shadow color.

```swift
public func setDropShadowOffsetX(_ id: DesignBlockID, offsetX: Float) throws
```

Set the drop shadow's X offset of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow's X offset should be set.
- `offsetX`: The X offset to be set.

```swift
public func setDropShadowOffsetY(_ id: DesignBlockID, offsetY: Float) throws
```

Set the drop shadow's Y offset of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow's Y offset should be set.
- `offsetY`: The Y offset to be set.

```swift
public func getDropShadowOffsetX(_ id: DesignBlockID) throws -> Float
```

Get the drop shadow's X offset of the given design block.

- `id:`: The block whose drop shadow's X offset should be queried.
- Returns: The offset.

```swift
public func getDropShadowOffsetY(_ id: DesignBlockID) throws -> Float
```

Get the drop shadow's Y offset of the given design block.

- `id:`: The block whose drop shadow's Y offset should be queried.
- Returns: The offset.

```swift
public func setDropShadowBlurRadiusX(_ id: DesignBlockID, blurRadiusX: Float) throws
```

Set the drop shadow's blur radius on the X axis of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow's blur radius should be set.
- `blurRadiusX`: The blur radius to be set.

```swift
public func setDropShadowBlurRadiusY(_ id: DesignBlockID, blurRadiusY: Float) throws
```

Set the drop shadow's blur radius on the Y axis of the given design block.
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow's blur radius should be set.
- `blurRadiusY`: The blur radius to be set.

```swift
public func setDropShadowClip(_ id: DesignBlockID, clip: Bool) throws
```

Set the drop shadow's clipping of the given design block. (Only applies to shapes.)
Required scope: "appearance/shadow"

- `id`: The block whose drop shadow's clip should be set.
- `clip`: The drop shadow's clip to be set.

```swift
public func getDropShadowClip(_ id: DesignBlockID) throws -> Bool
```

Get the drop shadow's clipping of the given design block.

- `id:`: The block whose drop shadow's clipping should be queried.
- Returns: The drop shadow's clipping.

```swift
public func getDropShadowBlurRadiusX(_ id: DesignBlockID) throws -> Float
```

Get the drop shadow's blur radius on the X axis of the given design block.

- `id:`: The block whose drop shadow's blur radius should be queried.
- Returns: The blur radius.

```swift
public func getDropShadowBlurRadiusY(_ id: DesignBlockID) throws -> Float
```

Get the drop shadow's blur radius on the Y axis of the given design block.

- `id:`: The block whose drop shadow's blur radius should be queried.
- Returns: The blur radius.

## Full Code

Here's the full code:

```swift
// Configure a basic colored drop shadow if the block supports them
if try engine.block.supportsDropShadow(block) {
  try engine.block.setDropShadowEnabled(block, enabled: true)
  try engine.block.setDropShadowColor(block, color: .rgba(r: 1.0, g: 0.75, b: 0.8, a: 1.0))
  let dropShadowColor = try engine.block.getDropShadowColor(block)
  try engine.block.setDropShadowOffsetX(block, offsetX: -10)
  try engine.block.setDropShadowOffsetY(block, offsetY: 5)
  let dropShadowOffsetX = try engine.block.getDropShadowOffsetX(block)
  let dropShadowOffsetX = try engine.block.getDropShadowOffsetY(block)
  try engine.block.setDropShadowBlurRadiusX(block, blurRadiusX: -10)
  try engine.block.setDropShadowBlurRadiusY(block, blurRadiusY: 5)
  try engine.block.setDropShadowClip(block, clip: false)
  let dropShadowClip = try getDropShadowClip(block)

  // Query a blocks drop shadow properties
  let dropShadowIsEnabled = try engine.block.isDropShadowEnabled(block)
  let dropShadowBlurRadiusX = try engine.block.getDropShadowBlurRadiusX(block)
  let dropShadowBlurRadiusY = try engine.block.getDropShadowBlurRadiusY(block)
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
