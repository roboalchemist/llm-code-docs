# Source: https://img.ly/docs/cesdk/macos/stickers-and-shapes/create-edit/create-shapes-64acc0/

---
title: "Create Shapes"
description: "Draw custom vector shapes and insert them into your design canvas."
platform: macos
url: "https://img.ly/docs/cesdk/macos/stickers-and-shapes/create-edit/create-shapes-64acc0/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/macos/shapes-9f1b2c/) > [Create Shapes](https://img.ly/docs/cesdk/macos/stickers-and-shapes/create-edit/create-shapes-64acc0/)

---

```swift file=@cesdk_swift_examples/engine-guides-using-shapes/UsingShapes.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func usingShapes(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let graphic = try engine.block.create(.graphic)
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg",
  )
  try engine.block.setFill(graphic, fill: imageFill)
  try engine.block.setWidth(graphic, value: 100)
  try engine.block.setHeight(graphic, value: 100)
  try engine.block.appendChild(to: scene, child: graphic)

  try await engine.scene.zoom(to: graphic, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)

  try engine.block.supportsShape(graphic) // Returns true
  let text = try engine.block.create(.text)
  try engine.block.supportsShape(text) // Returns false

  let rectShape = try engine.block.createShape(.rect)
  try engine.block.setShape(graphic, shape: rectShape)
  let shape = try engine.block.getShape(graphic)
  let shapeType = try engine.block.getType(shape)

  let starShape = try engine.block.createShape(.star)
  try engine.block.destroy(engine.block.getShape(graphic))
  try engine.block.setShape(graphic, shape: starShape)
  /* The following line would also destroy the currently attached starShape */
  // engine.block.destroy(graphic)

  let allShapeProperties = try engine.block.findAllProperties(starShape)
  try engine.block.setInt(starShape, property: "shape/star/points", value: 6)
}
```

The CE.SDK provides a flexible way to create and customize shapes, including rectangles, circles, lines, and polygons.

## Supported Shapes

The following shapes are supported in CE.SDK:

- `ShapeType.rect`
- `ShapeType.line`
- `ShapeType.ellipse`
- `ShapeType.polygon`
- `ShapeType.star`
- `ShapeType.vectorPath`

## Creating Shapes

`graphic` blocks don't have any shape after you create them, which leaves them invisible by default.
In order to make them visible, we need to assign both a shape and a fill to the `graphic` block. You can find more
information on fills [here](https://img.ly/docs/cesdk/macos/fills-402ddc/). In this example we have created and attached an image fill.

In order to create a new shape, we must call the `func createShape(_ type: ShapeType) throws -> DesignBlockID` API.

```swift highlight-createShape
let rectShape = try engine.block.createShape(.rect)
```

In order to assign this shape to the `graphic` block, call the `func setShape(_ id: DesignBlockID, shape: DesignBlockID) throws` API.

```swift highlight-setShape
try engine.block.setShape(graphic, shape: rectShape)
```

Just like design blocks, shapes with different types have different properties that you can set via the API. Please refer to the [API docs](https://img.ly/docs/cesdk/macos/stickers-and-shapes/create-edit/edit-shapes-d67cfb/) for a complete list of all available properties for each type of shape.

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func usingShapes(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let graphic = try engine.block.create(.graphic)
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg"
  )
  try engine.block.setFill(graphic, fill: imageFill)
  try engine.block.setWidth(graphic, value: 100)
  try engine.block.setHeight(graphic, value: 100)
  try engine.block.appendChild(to: scene, child: graphic)

  try await engine.scene.zoom(to: graphic, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)

  try engine.block.supportsShape(graphic) // Returns true
  let text = try engine.block.create(.text)
  try engine.block.supportsShape(text) // Returns false

  let rectShape = try engine.block.createShape(.rect)
  try engine.block.setShape(graphic, shape: rectShape)
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
