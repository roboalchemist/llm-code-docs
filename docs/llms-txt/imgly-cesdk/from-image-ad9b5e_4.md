# Source: https://img.ly/docs/cesdk/ios/open-the-editor/from-image-ad9b5e/

---
title: "Create From Image"
description: "Open the editor using an image as the base design, with tools ready for immediate editing."
platform: ios
url: "https://img.ly/docs/cesdk/ios/open-the-editor/from-image-ad9b5e/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/ios/open-the-editor-23a1db/) > [Create From Image](https://img.ly/docs/cesdk/ios/open-the-editor/from-image-ad9b5e/)

---

```swift file=@cesdk_swift_examples/engine-guides-create-scene-from-image-blob/CreateSceneFromImageBlob.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromImageBlob(engine: Engine) async throws {
  let blob = try await URLSession.shared.data(from: .init(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!).0

  let url = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("jpg")
  try blob.write(to: url, options: .atomic)

  let scene = try await engine.scene.create(fromImage: url)

  let page = try engine.block.find(byType: .page).first!

  let pageFill = try engine.block.getFill(page)
  let imageFillType = try engine.block.getType(pageFill)
}
```

```swift file=@cesdk_swift_examples/engine-guides-create-scene-from-image-url/CreateSceneFromImageURL.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromImageURL(engine: Engine) async throws {
  let scene = try await engine.scene.create(fromImage: URL(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!)

  // Get the fill from the page and verify it's an image fill
  let page = try engine.block.find(byType: .page).first!

  let pageFill = try engine.block.getFill(page)
  let imageFillType = try engine.block.getType(pageFill)
}
```

Starting from an existing image allows you to use the editor for customizing individual assets.
This is done by using `func create(from imageURL: URL, dpi: Float = 300, pixelScaleFactor: Float = 1) async throws -> DesignBlockID` and passing a URL as argument.
The `dpi` argument sets the dots per inch of the scene.
The `pixelScaleFactor` sets the display's pixel scale factor.

## Create a Scene From an Image

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial image.

Specify the source to use for the initial image.
This can be a relative path or a remote URL.

```swift highlight-createFromImage-url
let scene = try await engine.scene.create(fromImage: URL(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!)
```

When starting with an initial image, the scene's page dimensions match the given resource and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromImageURL(engine: Engine) async throws {
  let scene = try await engine.scene.create(fromImage: URL(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!)
}
```

## Create a Scene From a Blob

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial image provided from a blob.

First, get hold of a `blob` by fetching an image from the web.
This is just for demonstration purposes and your `blob` object may come from a different source.

```swift highlight-blob-swift
let blob = try await URLSession.shared.data(from: .init(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!).0
```

Afterward, create a temporary URL and save the `Data`.

```swift highlight-objectURL-swift
let url = FileManager.default.temporaryDirectory
  .appendingPathComponent(UUID().uuidString)
  .appendingPathExtension("jpg")
try blob.write(to: url, options: .atomic)
```

Use the created URL as a source for the initial image.

```swift highlight-initialImageURL-swift
let scene = try await engine.scene.create(fromImage: url)
```

When starting with an initial image, the scenes page dimensions match the given image, and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromImageBlob(engine: Engine) async throws {
  let blob = try await URLSession.shared.data(from: .init(string: "https://img.ly/static/ubq_samples/sample_4.jpg")!).0

  let url = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString)
    .appendingPathExtension("jpg")
  try blob.write(to: url, options: .atomic)

  let scene = try await engine.scene.create(fromImage: url)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
