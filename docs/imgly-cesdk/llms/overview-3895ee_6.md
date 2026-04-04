# Source: https://img.ly/docs/cesdk/mac-catalyst/fills/overview-3895ee/

---
title: "Fills"
description: "Apply solid colors, gradients, images, or videos as fills to shapes, text, and other design elements."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/fills/overview-3895ee/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Fills](https://img.ly/docs/cesdk/mac-catalyst/fills-402ddc/) > [Overview](https://img.ly/docs/cesdk/mac-catalyst/fills/overview-3895ee/)

---

```swift file=@cesdk_swift_examples/engine-guides-using-fills/UsingFills.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func usingFills(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  try await engine.scene.zoom(to: page, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)

  let block = try engine.block.create(.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  try engine.block.setWidth(block, value: 100)
  try engine.block.setHeight(block, value: 100)
  try engine.block.setFill(block, fill: engine.block.createFill(.color))
  try engine.block.appendChild(to: page, child: block)

  try engine.block.supportsFill(scene) // Returns false
  try engine.block.supportsFill(block) // Returns true

  let colorFill = try engine.block.getFill(block)
  let defaultRectFillType = try engine.block.getType(colorFill)
  let allFillProperties = try engine.block.findAllProperties(colorFill)
  try engine.block.setColor(colorFill, property: "fill/color/value", color: .rgba(r: 1.0, g: 0.0, b: 0.0, a: 1.0))

  try engine.block.setFillEnabled(block, enabled: false)
  try engine.block.setFillEnabled(block, enabled: !engine.block.isFillEnabled(block))

  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg",
  )

  try engine.block.destroy(colorFill)
  try engine.block.setFill(block, fill: imageFill)

  /* The following line would also destroy imageFill */
  // try engine.block.destroy(circle)

  let duplicateBlock = try engine.block.duplicate(block)
  try engine.block.setPositionX(duplicateBlock, value: 450)
  let autoDuplicateFill = try engine.block.getFill(duplicateBlock)
  try engine.block.setString(
    autoDuplicateFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_2.jpg",
  )

  // let manualDuplicateFill = try engine.block.duplicate(autoDuplicateFill)
  // /* We could now assign this fill to another block. */
  // try engine.block.destroy(manualDuplicateFill)

  let sharedFillBlock = try engine.block.create(.graphic)
  try engine.block.setShape(sharedFillBlock, shape: engine.block.createShape(.rect))
  try engine.block.setPositionX(sharedFillBlock, value: 350)
  try engine.block.setPositionY(sharedFillBlock, value: 400)
  try engine.block.setWidth(sharedFillBlock, value: 100)
  try engine.block.setHeight(sharedFillBlock, value: 100)
  try engine.block.appendChild(to: page, child: sharedFillBlock)

  try engine.block.setFill(sharedFillBlock, fill: engine.block.getFill(block))
}
```

Some [design blocks](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/) in CE.SDK allow you to modify or replace their fill. The fill is an object that defines the contents within the shape of a block. CreativeEditor SDK supports many different types of fills, such as images, solid colors, gradients and videos.

Similarly to blocks, each fill has a numeric id which can be used to query and [modify its properties](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/).

We currently support the following fill types:

- `FillType.color`
- `FillType.linearGradient`
- `FillType.radialGradient`
- `FillType.conicalGradient`
- `FillType.image`
- `FillType.video`
- `FillType.pixelStream`

## Accessing Fills

Not all types of design blocks support fills, so you should always first call the `func supportsFill(_ id: DesignBlockID) throws -> Bool` API before accessing any of the following APIs.

```swift highlight-supportsFill
try engine.block.supportsFill(scene) // Returns false
try engine.block.supportsFill(block) // Returns true
```

In order to receive the fill id of a design block, call the `func getFill(_ id: DesignBlockID) throws -> DesignBlockID` API. You can now pass this id into other APIs in order to query more information about the fill, e.g. its type via the `func getType(_ id: DesignBlockID) throws -> String` API.

```swift highlight-getFill
let colorFill = try engine.block.getFill(block)
let defaultRectFillType = try engine.block.getType(colorFill)
```

## Fill Properties

Just like design blocks, fills with different types have different properties that you can query and modify via the API. Use `func findAllProperties(_ id: DesignBlockID) throws -> [String]` in order to get a list of all properties of a given fill.

For the solid color fill in this example, the call would return `["fill/color/value", "type"]`.

Please refer to the [design blocks](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/) for a complete list of all available properties for each type of fill.

```swift highlight-getProperties
let allFillProperties = try engine.block.findAllProperties(colorFill)
```

Once we know the property keys of a fill, we can use the same APIs as for design blocks in order to modify those properties. For example, we can use `func setColor(_ id: DesignBlockID, property: String, color: Color) throws` in order to change the color of the fill to red.

Once we do this, our graphic block with rect shape will be filled with solid red.

```swift highlight-modifyProperties
try engine.block.setColor(colorFill, property: "fill/color/value", color: .rgba(r: 1.0, g: 0.0, b: 0.0, a: 1.0))
```

## Disabling Fills

You can disable and enable a fill using the `func setFillEnabled(_ id: DesignBlockID, enabled: Bool) throws` API, for example in cases where the design block should only have a stroke but no fill. Notice that you have to pass the id of the design block and not of the fill to the API.

```swift highlight-disableFill
try engine.block.setFillEnabled(block, enabled: false)
try engine.block.setFillEnabled(block, enabled: !engine.block.isFillEnabled(block))
```

## Changing Fill Types

All design blocks that support fills allow you to also exchange their current fill for any other type of fill. In order to do this, you need to first create a new fill object using `func createFill(_ type: FillType) throws -> DesignBlockID`.

```swift highlight-createFill
let imageFill = try engine.block.createFill(.image)
try engine.block.setString(
  imageFill,
  property: "fill/image/imageFileURI",
  value: "https://img.ly/static/ubq_samples/sample_1.jpg",
)
```

In order to assign a fill to a design block, simply call `func setFill(_ id: DesignBlockID, fill: DesignBlockID) throws`. Make sure to delete the previous fill of the design block first if you don't need it any more, otherwise we will have leaked it into the scene and won't be able to access it any more, because we don't know its id.

Notice that we don't use the `appendChild` API here, which only works with design blocks and not fills.

When a fill is attached to one design block, it will be automatically destroyed when the block itself gets destroyed.

```swift highlight-replaceFill
  try engine.block.destroy(colorFill)
  try engine.block.setFill(block, fill: imageFill)

  /* The following line would also destroy imageFill */
  // try engine.block.destroy(circle)
```

## Duplicating Fills

If we duplicate a design block with a fill that is only attached to this block, the fill will automatically be duplicated as well. In order to modify the properties of the duplicate fill, we have to query its id from the duplicate block.

```swift highlight-duplicateFill
  let duplicateBlock = try engine.block.duplicate(block)
  try engine.block.setPositionX(duplicateBlock, value: 450)
  let autoDuplicateFill = try engine.block.getFill(duplicateBlock)
  try engine.block.setString(
    autoDuplicateFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_2.jpg",
  )

  // let manualDuplicateFill = try engine.block.duplicate(autoDuplicateFill)
  // /* We could now assign this fill to another block. */
  // try engine.block.destroy(manualDuplicateFill)
```

## Sharing Fills

It is also possible to share a single fill instance between multiple design blocks. In that case, changing the properties of the fill will apply to all of the blocks that it's attached to at once.

Destroying a block with a shared fill will not destroy the fill until there are no other design blocks left that still use that fill.

```swift highlight-sharedFill
  let sharedFillBlock = try engine.block.create(.graphic)
  try engine.block.setShape(sharedFillBlock, shape: engine.block.createShape(.rect))
  try engine.block.setPositionX(sharedFillBlock, value: 350)
  try engine.block.setPositionY(sharedFillBlock, value: 400)
  try engine.block.setWidth(sharedFillBlock, value: 100)
  try engine.block.setHeight(sharedFillBlock, value: 100)
  try engine.block.appendChild(to: page, child: sharedFillBlock)

  try engine.block.setFill(sharedFillBlock, fill: engine.block.getFill(block))
```

## Full Code

Here is the full code for working with fills:

```swift
import Foundation
import IMGLYEngine

@MainActor
func usingFills(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  try await engine.scene.zoom(to: page, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)

  let block = try engine.block.create(.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  try engine.block.setWidth(block, value: 100)
  try engine.block.setHeight(block, value: 100)
  try engine.block.setFill(block, fill: engine.block.createFill(.color))
  try engine.block.appendChild(to: page, child: block)

  try engine.block.supportsFill(scene) // Returns false
  try engine.block.supportsFill(block) // Returns true

  let colorFill = try engine.block.getFill(block)
  let defaultRectFillType = try engine.block.getType(colorFill)
  let allFillProperties = try engine.block.findAllProperties(colorFill)
  try engine.block.setColor(colorFill, property: "fill/color/value", color: .rgba(r: 1.0, g: 0.0, b: 0.0, a: 1.0))

  try engine.block.setFillEnabled(block, enabled: false)
  try engine.block.setFillEnabled(block, enabled: !engine.block.isFillEnabled(block))

  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg"
  )

  try engine.block.destroy(colorFill)
  try engine.block.setFill(block, fill: imageFill)

  /* The following line would also destroy imageFill */
  // try engine.block.destroy(circle)

  let duplicateBlock = try engine.block.duplicate(block)
  try engine.block.setPositionX(duplicateBlock, value: 450)
  let autoDuplicateFill = try engine.block.getFill(duplicateBlock)
  try engine.block.setString(
    autoDuplicateFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_2.jpg"
  )

  // let manualDuplicateFill = try engine.block.duplicate(autoDuplicateFill)
  // /* We could now assign this fill to another block. */
  // try engine.block.destroy(manualDuplicateFill)

  let sharedFillBlock = try engine.block.create(.graphic)
  try engine.block.setShape(sharedFillBlock, shape: engine.block.createShape(.rect))
  try engine.block.setPositionX(sharedFillBlock, value: 350)
  try engine.block.setPositionY(sharedFillBlock, value: 400)
  try engine.block.setWidth(sharedFillBlock, value: 100)
  try engine.block.setHeight(sharedFillBlock, value: 100)
  try engine.block.appendChild(to: page, child: sharedFillBlock)

  try engine.block.setFill(sharedFillBlock, fill: engine.block.getFill(block))
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
