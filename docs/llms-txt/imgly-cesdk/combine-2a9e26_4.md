# Source: https://img.ly/docs/cesdk/ios/stickers-and-shapes/combine-2a9e26/

---
title: "Combine"
description: "Group and merge multiple stickers or shapes into a single element for easier manipulation."
platform: ios
url: "https://img.ly/docs/cesdk/ios/stickers-and-shapes/combine-2a9e26/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/ios/shapes-9f1b2c/) > [Combine](https://img.ly/docs/cesdk/ios/stickers-and-shapes/combine-2a9e26/)

---

```swift file=@cesdk_swift_examples/engine-guides-bool-ops/BoolOps.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func boolOps(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  let circle1 = try engine.block.create(.graphic)
  try engine.block.setShape(circle1, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle1, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle1, value: 30)
  try engine.block.setPositionY(circle1, value: 30)
  try engine.block.setWidth(circle1, value: 40)
  try engine.block.setHeight(circle1, value: 40)
  try engine.block.appendChild(to: page, child: circle1)

  let circle2 = try engine.block.create(.graphic)
  try engine.block.setShape(circle2, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle2, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle2, value: 80)
  try engine.block.setPositionY(circle2, value: 30)
  try engine.block.setWidth(circle2, value: 40)
  try engine.block.setHeight(circle2, value: 40)
  try engine.block.appendChild(to: page, child: circle2)

  let circle3 = try engine.block.create(.graphic)
  try engine.block.setShape(circle3, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle3, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle3, value: 50)
  try engine.block.setPositionY(circle3, value: 50)
  try engine.block.setWidth(circle3, value: 50)
  try engine.block.setHeight(circle3, value: 50)
  try engine.block.appendChild(to: page, child: circle3)

  let union = try engine.block.combine([circle1, circle2, circle3], booleanOperation: .union)

  let text = try engine.block.create(.text)
  try engine.block.replaceText(text, text: "Removed text")
  try engine.block.setPositionX(text, value: 10)
  try engine.block.setPositionY(text, value: 40)
  try engine.block.setWidth(text, value: 80)
  try engine.block.setHeight(text, value: 10)
  try engine.block.appendChild(to: page, child: text)

  let image = try engine.block.create(.graphic)
  try engine.block.setShape(image, shape: engine.block.createShape(.rect))
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setFill(image, fill: imageFill)
  try engine.block.setPositionX(image, value: 0)
  try engine.block.setPositionY(image, value: 0)
  try engine.block.setWidth(image, value: 100)
  try engine.block.setHeight(image, value: 100)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg",
  )
  try engine.block.appendChild(to: page, child: image)

  try engine.block.sendToBack(image)
  let difference = try engine.block.combine([image, text], booleanOperation: .difference)
}
```

You can use four different boolean operations on blocks to combine them into unique shapes. These operations are:

- `'Union'`: adds all the blocks' shapes into one
- `'Difference'`: removes from the bottom-most block the shapes of the other blocks overlapping with it
- `'Intersection'`: keeps only the overlapping parts of all the blocks' shapes
- `'XOR'`: removes the overlapping parts of all the block's shapes

Combining blocks allows you to create a new block with a customized shape.

Combining blocks with the `union`, `intersection` or `XOR` operation will result in the new block whose fill is that of the top-most block and whose shape is the result of applying the operation pair-wise on blocks from the top-most block to the bottom-most block.

Combining blocks with the `difference` operation will result in the new block whose fill is that of the bottom-most block and whose shape is the result of applying the operation pair-wise on blocks from the bottom-most block to the top-most block.

The combined blocks will be destroyed.

> **Note:** **Only the following blocks can be combined*** A graphics block
> * A text block

```swift
public func isCombinable(_ ids: [DesignBlockID]) throws -> Bool
```

Checks whether blocks could be combined.
Only graphics blocks and text blocks can be combined.
All blocks must have the "lifecycle/duplicate" scope enabled.

- `ids:`: The blocks for which the confirm combinability.
- Returns: Whether the blocks can be combined.

```swift
public func combine(_ ids: [DesignBlockID], booleanOperation: BooleanOperation) throws -> DesignBlockID
```

Perform a boolean operation on the given blocks.
All blocks must be combinable. See `isCombinable`.
The parent, fill and sort order of the new block is that of the prioritized block.
When performing a `Union`, `Intersection` or `XOR`, the operation is performed pair-wise starting with the element
with the highest sort order.
When performing a `Difference`, the operation is performed pair-wise starting with
the element with the lowest sort order.
Required scope: "editor/select"

- `ids`: The blocks to combine. They will be destroyed if "lifecycle/destroy" scope is enabled.
- `booleanOperation`: The boolean operation to perform.
- Returns: The newly created block.

Here's the full code:

```swift
// Create blocks and append to scene
let star = try engine.block.create(.starShape)
let rect = try engine.block.create(.rectShape)
try engine.block.appendChild(to: scene, child: star)
try engine.block.appendChild(to: scene, child: rect)

// Check whether the blocks may be combined
if try engine.block.isCombinable([star, rect]) {
  let combined = try engine.block.combine([star, rect], booleanOperation: .union)
}
```

## Combining three circles together

We create three circles and arrange in a recognizable pattern.
Combing them with `'Union'` result in a single block with a unique shape.
The result will inherit the top-most block's fill, in this case `circle3`'s fill.

```swift highlight-combine-union
  let circle1 = try engine.block.create(.graphic)
  try engine.block.setShape(circle1, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle1, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle1, value: 30)
  try engine.block.setPositionY(circle1, value: 30)
  try engine.block.setWidth(circle1, value: 40)
  try engine.block.setHeight(circle1, value: 40)
  try engine.block.appendChild(to: page, child: circle1)

  let circle2 = try engine.block.create(.graphic)
  try engine.block.setShape(circle2, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle2, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle2, value: 80)
  try engine.block.setPositionY(circle2, value: 30)
  try engine.block.setWidth(circle2, value: 40)
  try engine.block.setHeight(circle2, value: 40)
  try engine.block.appendChild(to: page, child: circle2)

  let circle3 = try engine.block.create(.graphic)
  try engine.block.setShape(circle3, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle3, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle3, value: 50)
  try engine.block.setPositionY(circle3, value: 50)
  try engine.block.setWidth(circle3, value: 50)
  try engine.block.setHeight(circle3, value: 50)
  try engine.block.appendChild(to: page, child: circle3)

  let union = try engine.block.combine([circle1, circle2, circle3], booleanOperation: .union)
```

To create a special effect of text punched out from an image, we create an image and a text.
We ensure that the image is at the bottom as that is the base block from which we want to remove shapes.
The result will be a block with the size, shape and fill of the image but with a hole in it in the shape of the removed text.

```swift highlight-combine-difference
  let text = try engine.block.create(.text)
  try engine.block.replaceText(text, text: "Removed text")
  try engine.block.setPositionX(text, value: 10)
  try engine.block.setPositionY(text, value: 40)
  try engine.block.setWidth(text, value: 80)
  try engine.block.setHeight(text, value: 10)
  try engine.block.appendChild(to: page, child: text)

  let image = try engine.block.create(.graphic)
  try engine.block.setShape(image, shape: engine.block.createShape(.rect))
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setFill(image, fill: imageFill)
  try engine.block.setPositionX(image, value: 0)
  try engine.block.setPositionY(image, value: 0)
  try engine.block.setWidth(image, value: 100)
  try engine.block.setHeight(image, value: 100)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg",
  )
  try engine.block.appendChild(to: page, child: image)

  try engine.block.sendToBack(image)
  let difference = try engine.block.combine([image, text], booleanOperation: .difference)
```

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func boolOps(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  let circle1 = try engine.block.create(.graphic)
  try engine.block.setShape(circle1, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle1, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle1, value: 30)
  try engine.block.setPositionY(circle1, value: 30)
  try engine.block.setWidth(circle1, value: 40)
  try engine.block.setHeight(circle1, value: 40)
  try engine.block.appendChild(to: page, child: circle1)

  let circle2 = try engine.block.create(.graphic)
  try engine.block.setShape(circle2, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle2, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle2, value: 80)
  try engine.block.setPositionY(circle2, value: 30)
  try engine.block.setWidth(circle2, value: 40)
  try engine.block.setHeight(circle2, value: 40)
  try engine.block.appendChild(to: page, child: circle2)

  let circle3 = try engine.block.create(.graphic)
  try engine.block.setShape(circle3, shape: engine.block.createShape(.ellipse))
  try engine.block.setFill(circle3, fill: engine.block.createFill(.color))
  try engine.block.setPositionX(circle3, value: 50)
  try engine.block.setPositionY(circle3, value: 50)
  try engine.block.setWidth(circle3, value: 50)
  try engine.block.setHeight(circle3, value: 50)
  try engine.block.appendChild(to: page, child: circle3)

  let union = try engine.block.combine([circle1, circle2, circle3], booleanOperation: .union)

  let text = try engine.block.create(.text)
  try engine.block.replaceText(text, text: "Removed text")
  try engine.block.setPositionX(text, value: 10)
  try engine.block.setPositionY(text, value: 40)
  try engine.block.setWidth(text, value: 80)
  try engine.block.setHeight(text, value: 10)
  try engine.block.appendChild(to: page, child: text)

  let image = try engine.block.create(.graphic)
  try engine.block.setShape(image, shape: engine.block.createShape(.rect))
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setFill(image, fill: imageFill)
  try engine.block.setPositionX(image, value: 0)
  try engine.block.setPositionY(image, value: 0)
  try engine.block.setWidth(image, value: 100)
  try engine.block.setHeight(image, value: 100)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg"
  )
  try engine.block.appendChild(to: page, child: image)

  try engine.block.sendToBack(image)
  let difference = try engine.block.combine([image, text], booleanOperation: .difference)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
