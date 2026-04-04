# Source: https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-cutout-384be3/

---
title: "Create Cutout"
description: "Create cutouts from images or shapes by masking or removing specific areas."
platform: ios
url: "https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-cutout-384be3/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Edit Stickers](https://img.ly/docs/cesdk/ios/stickers-3d4e5f/) > [Create Cutout](https://img.ly/docs/cesdk/ios/stickers-and-shapes/create-cutout-384be3/)

---

```swift file=@cesdk_swift_examples/engine-guides-cutouts/Cutouts.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func cutouts(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  let circle = try engine.block.createCutoutFromPath("M 0,25 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0 Z")
  try engine.block.setFloat(circle, property: "cutout/offset", value: 3.0)
  try engine.block.setEnum(circle, property: "cutout/type", value: "Dashed")

  var square = try engine.block.createCutoutFromPath("M 0,0 H 50 V 50 H 0 Z")
  try engine.block.setFloat(square, property: "cutout/offset", value: 6.0)

  var union = try engine.block.createCutoutFromOperation(containing: [circle, square], cutoutOperation: .union)
  try engine.block.destroy(circle)
  try engine.block.destroy(square)

  engine.editor.setSpotColor(name: "CutContour", r: 0.0, g: 0.0, b: 1.0)
}
```

Cutouts are a special feature one can use with cuttings printers.
When printing a PDF file containing cutouts paths, a cutting printer will cut these paths with a cutter rather than print them with ink.
Use cutouts to create stickers, iron on decals, etc.

Cutouts can be created from an SVG string describing its underlying shape.
Cutouts can also be created from combining multiple existing cutouts using the boolean operations `union`, `difference`, `intersection` and `xor`.

Cutouts have a type property which can take one of two values: `solid` and `dashed`.
Cutting printers recognize cutouts paths through their specially named spot colors.
By default, `solid` cutouts have the spot color `"CutContour"` to produce a continuous cutting line and `dashed` cutouts have the spot colors `"PerfCutContour"` to produce a perforated cutting line.
You may need to adjust these spot color names for you printer.

> **Note:** **Note** Note that the actual color approximation given to the spot color does
> not affect how the cutting printer interprets the cutout, only how it is
> rendered. The default color approximations are magenta for "CutContour" and
> green for "PerfCutContour".

Cutouts have an offset property that determines the distance at which the cutout path is rendered from the underlying path set when created.

## Setup the scene

We first create a new scene with a new page.

```swift highlight-setup
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)
```

## Create cutouts

Here we add two cutouts.
First, a circle of type `dashed` and with an offset of 3.0.
Second, a square of default type `solid` and an offset of 6.0.

```swift highlight-create-cutouts
  let circle = try engine.block.createCutoutFromPath("M 0,25 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0 Z")
  try engine.block.setFloat(circle, property: "cutout/offset", value: 3.0)
  try engine.block.setEnum(circle, property: "cutout/type", value: "Dashed")

  var square = try engine.block.createCutoutFromPath("M 0,0 H 50 V 50 H 0 Z")
  try engine.block.setFloat(square, property: "cutout/offset", value: 6.0)
```

## Combining multiple cutouts into one

Here we use the `union` operation to create a new cutout that consists of the combination of the earlier two cutouts we have created.
Note that we destroy the previously created `circle` and `square` cutouts as we don't need them anymore and we certainly don't want to printer to cut through those paths as well.

When combining multiple cutouts, the resulting cutout will be of the type of the first cutout given and an offset of 0.
In this example, since the `circle` cutout is of type `dashed`, the newly created cutout will also be of type `dashed`.

> **Note:** **Warning** When using the Difference operation, the first cutout is the
> cutout that is subtracted <em>from</em>. For other operations, the order of
> the cutouts don't matter.

```swift highlight-cutout-union
var union = try engine.block.createCutoutFromOperation(containing: [circle, square], cutoutOperation: .union)
try engine.block.destroy(circle)
try engine.block.destroy(square)
```

## Change the default color for Solid cutouts

For some reason, we'd like the cutouts of type `solid` to not render as magenta but as blue.
Knowing that `"CutContour"` is the spot color associated with `solid`, we change it RGB approximation to blue.
Thought the cutout will render as blue, the printer will still interpret this path as a cutting because of its special spot color name.

```swift highlight-spot-color-solid
engine.editor.setSpotColor(name: "CutContour", r: 0.0, g: 0.0, b: 1.0)
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func cutouts(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)

  let circle = try engine.block.createCutoutFromPath("M 0,25 a 25,25 0 1,1 50,0 a 25,25 0 1,1 -50,0 Z")
  try engine.block.setFloat(circle, property: "cutout/offset", value: 3.0)
  try engine.block.setEnum(circle, property: "cutout/type", value: "Dashed")

  var square = try engine.block.createCutoutFromPath("M 0,0 H 50 V 50 H 0 Z")
  try engine.block.setFloat(square, property: "cutout/offset", value: 6.0)

  var union = try engine.block.createCutoutFromOperation(containing: [circle, square], cutoutOperation: .union)
  try engine.block.destroy(circle)
  try engine.block.destroy(square)

  engine.editor.setSpotColor(name: "CutContour", r: 0.0, g: 0.0, b: 1.0)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
