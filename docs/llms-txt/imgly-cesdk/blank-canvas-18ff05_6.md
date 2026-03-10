# Source: https://img.ly/docs/cesdk/mac-catalyst/open-the-editor/blank-canvas-18ff05/

---
title: "Start With Blank Canvas"
description: "Launch the editor with an empty canvas as a starting point for new designs."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/open-the-editor/blank-canvas-18ff05/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/mac-catalyst/open-the-editor-23a1db/) > [Start With Blank Canvas](https://img.ly/docs/cesdk/mac-catalyst/open-the-editor/blank-canvas-18ff05/)

---

```swift file=@cesdk_swift_examples/engine-guides-create-scene-from-scratch/CreateSceneFromScratch.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromScratch(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: scene, child: page)

  let block = try engine.block.create(.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.star))
  try engine.block.setFill(block, fill: engine.block.createFill(.color))
  try engine.block.appendChild(to: page, child: block)
}
```

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) from scratch and add a star shape.

We create an empty scene via `try engine.scene.create()` which sets up the default scene block with a camera attached.
Afterwards, the scene can be populated by creating additional blocks and appending them to the scene.
See [Modifying Scenes](https://img.ly/docs/cesdk/mac-catalyst/concepts/blocks-90241e/) for more details.

```swift highlight-create
let scene = try engine.scene.create()
```

We first add a page with `func create(_ type: DesignBlockType) throws -> DesignBlockID` specifying a `.page` and set a parent-child relationship between the scene and this page.

```swift highlight-add-page
let page = try engine.block.create(.page)
try engine.block.appendChild(to: scene, child: page)
```

To this page, we add a graphic design block, again with `func create(_ type: DesignBlockType) throws -> DesignBlockID`.
To make it more interesting, we set a star shape and a color fill to this block to give it a visual representation.
Like for the page, we set the parent-child relationship between the page and the newly added block.
From then on, modifications to this block are relative to the page.

```swift highlight-add-block-with-star-shape
let block = try engine.block.create(.graphic)
try engine.block.setShape(block, shape: engine.block.createShape(.star))
try engine.block.setFill(block, fill: engine.block.createFill(.color))
try engine.block.appendChild(to: page, child: block)
```

This example first appends a page child to the scene as would typically be done but it is not strictly necessary and any child block can be appended directly to a scene.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromScratch(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: scene, child: page)

  let block = try engine.block.create(.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.star))
  try engine.block.setFill(block, fill: engine.block.createFill(.color))
  try engine.block.appendChild(to: page, child: block)
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
