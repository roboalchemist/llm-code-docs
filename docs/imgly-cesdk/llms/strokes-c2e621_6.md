# Source: https://img.ly/docs/cesdk/mac-catalyst/outlines/strokes-c2e621/

---
title: "Using Strokes"
description: "Add and customize outlines around shapes, text, or images using stroke settings."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/outlines/strokes-c2e621/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Outlines](https://img.ly/docs/cesdk/mac-catalyst/outlines-b7820c/) > [Stroke (Outline)](https://img.ly/docs/cesdk/mac-catalyst/outlines/strokes-c2e621/)

---

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify strokes through the `block` API. Strokes can be added to any shape or text and stroke styles are varying from plain solid lines to dashes and gaps of varying lengths and can have different end caps.

## Strokes

```swift
public func supportsStroke(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has a stroke property.

- `id:`: The block to query.
- Returns: `true` if the block has a stroke property.

```swift
public func setStrokeEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the stroke of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke should be enabled or disabled.
- `enabled`: If `true`, the stroke will be enabled.

```swift
public func isStrokeEnabled(_ id: DesignBlockID) throws -> Bool
```

Query if the stroke of the given design block is enabled.

- `id:`: The block whose stroke state should be queried.
- Returns: `true` if the block's stroke is enabled.

```swift
public func setStrokeColor(_ id: DesignBlockID, color: Color) throws
```

Set the stroke color of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke color should be set.
- `color`: The color to set.

```swift
public func getStrokeColor(_ id: DesignBlockID) throws -> Color
```

Get the stroke color of the given design block.

- `id:`: The block whose stroke color should be queried.
- Returns: The stroke color.

```swift
public func setStrokeWidth(_ id: DesignBlockID, width: Float) throws
```

Set the stroke width of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke width should be set.
- `width`: The stroke width to be set.

```swift
public func getStrokeWidth(_ id: DesignBlockID) throws -> Float
```

Get the stroke width of the given design block.

- `id:`: The block whose stroke width should be queried.
- Returns: The stroke's width.

```swift
public func setStrokeStyle(_ id: DesignBlockID, style: StrokeStyle) throws
```

Set the stroke style of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke style should be set.
- `style`: The stroke style to be set.

```swift
public func getStrokeStyle(_ id: DesignBlockID) throws -> StrokeStyle
```

Get the stroke style of the given design block.

- `id:`: The block whose stroke style should be queried.
- Returns: The stroke's style.

```swift
public func setStrokePosition(_ id: DesignBlockID, position: StrokePosition) throws
```

Set the stroke position of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke position should be set.
- `position`: The stroke position to be set.

```swift
public func getStrokePosition(_ id: DesignBlockID) throws -> StrokePosition
```

Get the stroke position of the given design block.

- `id:`: The block whose stroke position should be queried.
- Returns: The stroke position.

```swift
public func setStrokeCornerGeometry(_ id: DesignBlockID, cornerGeometry: StrokeCornerGeometry) throws
```

Set the stroke corner geometry of the given design block.
Required scope: "stroke/change"

- `id`: The block whose stroke join geometry should be set.
- `cornerGeometry`: The stroke join geometry to be set.

```swift
public func getStrokeCornerGeometry(_ id: DesignBlockID) throws -> StrokeCornerGeometry
```

Get the stroke corner geometry of the given design block.

- `id:`: The block whose stroke join geometry should be queried.
- Returns: The stroke join geometry.

## Full Code

Here's the full code for using strokes:

```swift
// Check if block supports strokes
if try engine.block.supportsStroke(block) {
  // Enable the stroke
  try engine.block.setStrokeEnabled(block, enabled: true)
  let strokeIsEnabled = try engine.block.isStrokeEnabled(block)

  // Configure it
  try engine.block.setStrokeColor(block, color: .rgba(r: 1.0, g: 0.75, b: 0.8, a: 1.0))
  let strokeColor = try engine.block.getStrokeColor(block)
  try engine.block.setStrokeWidth(block, width: 5)
  let strokeWidth = try engine.block.getStrokeWidth(block)
  try engine.block.setStrokeStyle(block, style: .dashed)
  let strokeStlye = try engine.block.getStrokeStyle(block)
  try engine.block.setStrokePosition(block, position: .outer)
  let strokePosition = try engine.block.getStrokePosition(block)
  try engine.block.setStrokeCornerGeometry(block, cornerGeometry: .round)
  let strokeCornerGeometry = try engine.block.getStrokeCornerGeometry(block)
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
