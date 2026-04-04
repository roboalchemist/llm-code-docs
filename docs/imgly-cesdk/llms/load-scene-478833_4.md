# Source: https://img.ly/docs/cesdk/ios/open-the-editor/load-scene-478833/

---
title: "Load a Scene"
description: "Load existing design scenes into the editor to resume or modify previous work."
platform: ios
url: "https://img.ly/docs/cesdk/ios/open-the-editor/load-scene-478833/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/ios/open-the-editor-23a1db/) > [Load a Scene](https://img.ly/docs/cesdk/ios/open-the-editor/load-scene-478833/)

---

```swift file=@cesdk_swift_examples/engine-guides-load-scene-from-blob/LoadSceneFromBlob.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromBlob(engine: Engine) async throws {
  let sceneURL =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  let sceneBlob = try await URLSession.shared.data(from: sceneURL).0

  let blobString = String(data: sceneBlob, encoding: .utf8)!

  let scene = try await engine.scene.load(from: blobString)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

```swift file=@cesdk_swift_examples/engine-guides-load-scene-from-string/LoadSceneFromString.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromString(engine: Engine) async throws {
  let sceneURL =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  let sceneBlob = try await URLSession.shared.data(from: sceneURL).0
  let blobString = String(data: sceneBlob, encoding: .utf8)!

  let scene = try await engine.scene.load(from: blobString)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

```swift file=@cesdk_swift_examples/engine-guides-load-scene-from-remote/LoadSceneFromRemote.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromRemote(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!

  let scene = try await engine.scene.load(from: sceneUrl)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

Loading an existing scene allows resuming work on a previous session or adapting an existing template to your needs.

> **Note:** **Warning** Saving a scene can be done as a either <em>scene file</em> or as
> an <em>archive file</em> (c.f.
> [Saving scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/)). A <em>scene file</em> does
> not include any fonts or images. Only the source URIs of assets, the general
> layout, and element properties are stored. When loading scenes in a new
> environment, ensure previously used asset URIs are available. Conversely, an
> <em>archive file</em> contains within it the scene's assets and references
> them as relative URIs.

## Load Scenes from a Remote URL

Determine a URL that points to a scene binary string.

```swift highlight-url
let sceneUrl =
  URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
```

We can then pass that string to the `func load(from url: URL) async throws -> DesignBlockID` function.
The editor will reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```swift highlight-load-remote
let scene = try await engine.scene.load(from: sceneUrl)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) for more details.

```swift highlight-modify-text-remote
let text = try engine.block.find(byType: .text).first!
try engine.block.setDropShadowEnabled(text, enabled: true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromRemote(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!

  let scene = try await engine.scene.load(from: sceneUrl)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

## Load Scenes from a String

In this example, we fetch a scene from a remote URL and load it as a string.
This string could also come from the result of `func saveToString() async throws -> String`.

```swift highlight-fetch-string
let sceneURL =
  URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
let sceneBlob = try await URLSession.shared.data(from: sceneURL).0
let blobString = String(data: sceneBlob, encoding: .utf8)!
```

We can pass that string to the `func load(from string: String) async throws -> DesignBlockID` function.
The editor will then reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```swift highlight-load-string
let scene = try await engine.scene.load(from: blobString)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) for more details.

```swift highlight-modify-text-string
let text = try engine.block.find(byType: .text).first!
try engine.block.setDropShadowEnabled(text, enabled: true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

```swift
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromString(engine: Engine) async throws {
  let sceneURL =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  let sceneBlob = try await URLSession.shared.data(from: sceneURL).0
  let blobString = String(data: sceneBlob, encoding: .utf8)!

  let scene = try await engine.scene.load(from: blobString)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

## Load Scenes From a Blob

In this example, we fetch a scene from a remote URL and load it as `sceneBlob`.

```swift highlight-fetch-blob
let sceneURL =
  URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
let sceneBlob = try await URLSession.shared.data(from: sceneURL).0
```

To acquire a scene string from `sceneBlob`, we need to read its contents into a string.

```swift highlight-read-blob
let blobString = String(data: sceneBlob, encoding: .utf8)!
```

We can then pass that string to the `func load(from string: String) async throws -> DesignBlockID` function.
The editor will reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```swift highlight-load-blob
let scene = try await engine.scene.load(from: blobString)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/ios/concepts/blocks-90241e/) for more details.

```swift highlight-modify-text-blob
let text = try engine.block.find(byType: .text).first!
try engine.block.setDropShadowEnabled(text, enabled: true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func loadSceneFromBlob(engine: Engine) async throws {
  let sceneURL =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  let sceneBlob = try await URLSession.shared.data(from: sceneURL).0

  let blobString = String(data: sceneBlob, encoding: .utf8)!

  let scene = try await engine.scene.load(from: blobString)

  let text = try engine.block.find(byType: .text).first!
  try engine.block.setDropShadowEnabled(text, enabled: true)
}
```

## Loading Scene Archives

Loading a scene archives requires unzipping the archives contents to a location, that's accessible to the CreativeEngine. One could for example unzip the archive via `unzip archive.zip` and then serve its contents using `$ npx serve`. This spins up a local test server, that serves everything contained in the current directory at `http://localhost:3000`

The archive can then be loaded by calling `await engine.scene.loadFromURL('http://localhost:3000/scene.scene')`. See [loading scenes](https://img.ly/docs/cesdk/ios/open-the-editor/load-scene-478833/) for more details. All asset paths in the archive are then resolved relative to the location of the `scene.scene` file. For an image, that would result in `'http://localhost:3000/images/1234.jpeg'`. After loading all URLs are fully resolved with the location of the `scene.scene` file and the scene behaves like any other scene.

### Resolving assets from a different source

The engine will use its [URI resolver](https://img.ly/docs/cesdk/ios/open-the-editor/uri-resolver-36b624/) to resolve all asset paths it encounters. This allows you to redirect requests for the assets contained in archive to a different location. To do so, you can add a custom resolver, that redirects requests for assets to a different location. Assuming you store your archived scenes in a `scenes/` directory, this would be an example of how to do so:

```swift
try engine.editor.setURIResolver { path in
  let url = URL(string: path)!
  let components = URLComponents(string: path)!

  if components.host == "localhost" && components.path.hasPrefix("/scenes") && !components.path.hasSuffix(".scene") {
    // Apply custom logic here, e.g. redirect to a different server
  }

  // Use default behaviour for everything else
  return URL(string: engine.editor.defaultURIResolver(relativePath: path))!
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
