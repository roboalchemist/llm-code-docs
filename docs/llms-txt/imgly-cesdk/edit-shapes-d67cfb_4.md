# Source: https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-edit/edit-shapes-d67cfb/

---
title: "Edit Shapes"
description: "Modify shape properties like size, color, position, and border radius."
platform: ios
url: "https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-edit/edit-shapes-d67cfb/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/ios/shapes-9f1b2c/) > [Edit Shapes](https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-edit/edit-shapes-d67cfb/)

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

The `graphic` [design block](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) in CE.SDK allows you to modify and replace its shape. CreativeEditor SDK supports many different types of shapes, such as rectangles, lines, ellipses, polygons and custom vector paths.

Similarly to blocks, each shape object has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/).

## Accessing Shapes

In order to query whether a block supports shapes, you should call the `func supportsShape(_ id: DesignBlockID) throws -> Bool` API.
Currently, only the `graphic` design block supports shape objects.

```swift highlight-supportsShape
try engine.block.supportsShape(graphic) // Returns true
let text = try engine.block.create(.text)
try engine.block.supportsShape(text) // Returns false
```

To query the shape of a design block, call the `func getShape(_ id: DesignBlockID) throws -> DesignBlockID` API.
You can now pass the returned result into other APIs in order to query more information about the shape,
e.g. its type via the `func getType(_ id: DesignBlockID) throws -> String` API.

```swift highlight-getShape
let shape = try engine.block.getShape(graphic)
let shapeType = try engine.block.getType(shape)
```

When replacing the shape of a design block, remember to destroy the previous shape object if you don't
intend to use it any further. Shape objects that are not attached to a design block will never be automatically destroyed.

Destroying a design block will also destroy its attached shape block.

```swift highlight-replaceShape
let starShape = try engine.block.createShape(.star)
try engine.block.destroy(engine.block.getShape(graphic))
try engine.block.setShape(graphic, shape: starShape)
/* The following line would also destroy the currently attached starShape */
// engine.block.destroy(graphic)
```

## Shape Properties

Just like design blocks, shapes with different types have different properties that you can query and modify via the API. Use `func findAllProperties(_ id: DesignBlockID) throws -> [String]` in order to get a list of all properties of a given shape.

For the star shape in this example, the call would return
`["name", "shape/star/innerDiameter", "shape/star/points", "type", "uuid"]`.

Please refer to the [API docs](https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-edit/edit-shapes-d67cfb/) for a complete list of all available properties for each type of shape.

```swift highlight-getProperties
let allShapeProperties = try engine.block.findAllProperties(starShape)
```

Once we know the property keys of a shape, we can use the same APIs as for design blocks in order to modify those properties. For example, we can use `func setInt(_ id: DesignBlockID, property: String, value: Int) throws` in order to change the number of points
of the star to six.

```swift highlight-modifyProperties
try engine.block.setInt(starShape, property: "shape/star/points", value: 6)
```

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



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
