# Source: https://img.ly/docs/cesdk/ios/open-the-editor/from-video-86beb0/

---
title: "Create From Video"
description: "Load a video file into the editor to start editing frame-based or timeline-based video content."
platform: ios
url: "https://img.ly/docs/cesdk/ios/open-the-editor/from-video-86beb0/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/ios/open-the-editor-23a1db/) > [Create From Video](https://img.ly/docs/cesdk/ios/open-the-editor/from-video-86beb0/)

---

```swift file=@cesdk_swift_examples/engine-guides-create-scene-from-video-url/CreateSceneFromVideoURL.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromVideoURL(engine: Engine) async throws {
  let scene = try await engine.scene.create(fromVideo: URL(string: "https://img.ly/static/ubq_video_samples/bbb.mp4")!)

  // Find the automatically added graphic block in the scene that contains the video fill.
  let block = try engine.block.find(byType: .graphic).first!

  // Change its opacity.
  try engine.block.setOpacity(block, value: 0.5)
}
```

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial video.

Starting from an existing video allows you to use the editor for customizing individual assets.
This is done by using `func create(fromVideo url: URL) async throws -> DesignBlockID` and passing a URL as argument.

Specify the source to use for the initial video.
This can be a relative path or a remote URL.

```javascript highlight-createFromVideo
let scene = try await engine.scene.create(fromVideo: URL(string: "https://img.ly/static/ubq_video_samples/bbb.mp4")!)
```

We can retrieve the graphic block id of this initial video using `func find(byType type: DesignBlockType) throws -> [DesignBlockID]`.
Note that that function returns an array.
Since there's only a single graphic block in the scene, the block is at index `0`.

```javascript highlight-findByType
// Find the automatically added graphic block in the scene that contains the video fill.
let block = try engine.block.find(byType: .graphic).first!
```

We can then manipulate and modify this block.
Here we modify its opacity with `func setOpacity(_ id: DesignBlockID, value: Float) throws`.
See [Modifying Scenes](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) for more details.

```javascript highlight-setOpacity
// Change its opacity.
try engine.block.setOpacity(block, value: 0.5)
```

When starting with an initial video, the scene's page dimensions match the given resource and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func createSceneFromVideoURL(engine: Engine) async throws {
  let scene = try await engine.scene.create(fromVideo: URL(string: "https://img.ly/static/ubq_video_samples/bbb.mp4")!)

  // Find the automatically added graphic block in the scene that contains the video fill.
  let block = try engine.block.find(byType: .graphic).first!

  // Change its opacity.
  try engine.block.setOpacity(block, value: 0.5)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
