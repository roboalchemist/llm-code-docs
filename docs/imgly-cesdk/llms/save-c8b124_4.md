# Source: https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/

---
title: "Save"
description: "Save design progress locally or to a backend service to allow for later editing or publishing."
platform: ios
url: "https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Save](https://img.ly/docs/cesdk/ios/export-save-publish/save-c8b124/)

---

The CreativeEngine allows you to save scenes in a binary format to share them between editors or store them for later editing.

Saving a scene can be done as a either scene file or as an archive file. A scene file does not include any fonts or images. Only the source URIs of assets, the general layout, and element properties are stored. When loading scenes in a new environment, ensure previously used asset URIs are available. Conversely, an archive file contains within it the scene's assets and references them as relative URIs.

> **Note:** **Warning** A scene file does not include any fonts or images. Only the source
> URIs of assets, the general layout, and element properties are stored. When
> loading scenes in a new environment, ensure previously used asset URIs are
> available.

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-archive/SaveSceneToArchive.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToArchive(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let blob = try await engine.scene.saveToArchive()

  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
}
```

## Save Scenes to an Archive

In this example, we will show you how to save scenes as an archive with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

As an archive, the resulting `Blob` includes all pages and any hidden elements and all the asset data.

To get hold of such a `Blob`, you need to use `engine.scene.saveToArchive()`.
This is an asynchronous method.
After waiting for the coroutine to finish, we receive a `Blob` holding the entire scene currently loaded in the editor including its assets' data.

```swift highlight-saveToArchive
let blob = try await engine.scene.saveToArchive()
```

That `Blob` can then be treated as a form file parameter and sent to a remote location.

```swift highlight-create-form-data-archive
  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
```

### Full Code

Here's the full code:

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-archive/SaveSceneToArchive.swift
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToArchive(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let blob = try await engine.scene.saveToArchive()

  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
}
```

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-blob/SaveSceneToBlob.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToBlob(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let savedSceneString = try await engine.scene.saveToString()

  let blob = savedSceneString.data(using: .utf8)!

  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
}
```

## Save Scenes to a Blob

In this example, we will show you how to save scenes as a `Blob` with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

This is done by converting the contents of a scene to a string, which can then be stored or transferred.
For sending these to a remote location, we wrap them in a `Blob` and treat it as a file object.

To get hold of the scene contents as string, you need to use `engine.scene.saveToString()`.
This is an asynchronous method.
After waiting for the coroutine to finish, we receive a plain string holding the entire scene currently loaded in the editor.
This includes all pages and any hidden elements but none of the actual asset data.

```swift highlight-saveToBlob
let savedSceneString = try await engine.scene.saveToString()
```

The returned string consists solely of ASCII characters and can safely be used further or written to a database.

```swift highlight-create-blob
let blob = savedSceneString.data(using: .utf8)!
```

That object can then be treated as a form file parameter and sent to a remote location.

```swift highlight-create-form-data-blob
  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
```

### Full Code

Here's the full code:

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-blob/SaveSceneToBlob.swift
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToBlob(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let savedSceneString = try await engine.scene.saveToString()

  let blob = savedSceneString.data(using: .utf8)!

  var request = URLRequest(url: .init(string: "https://example.com/upload/")!)
  request.httpMethod = "POST"

  let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
}
```

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-string/SaveSceneToString.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToString(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let sceneAsString = try await engine.scene.saveToString()

  print(sceneAsString)
}
```

## Save Scenes to a String

In this example, we will show you how to save scenes as a string with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

This is done by converting the contents of a scene to a single string, which can then be stored or transferred.

To get hold of such a string, you need to use `engine.scene.saveToString()`.
This is an asynchronous method.
After waiting for the coroutine to finish, we receive a plain string holding the entire scene currently loaded in the editor.
This includes all pages and any hidden elements, but none of the actual asset data.

```swift highlight-saveToString
let sceneAsString = try await engine.scene.saveToString()
```

The returned string consists solely of ASCII characters and can safely be used further or written to a database.

```swift highlight-result-string
print(sceneAsString)
```

### Full Code

Here's the full code:

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-string/SaveSceneToString.swift
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToString(engine: Engine) async throws {
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)

  let sceneAsString = try await engine.scene.saveToString()

  print(sceneAsString)
}
```

## Compression Options

CE.SDK supports optional compression for saved scenes to reduce file size. Compression is particularly useful for large scenes or when storage space is limited.

```swift
// Save with Zstd compression (recommended)
let compressed = try await engine.scene.saveToString(
  options: SaveToStringOptions(
    compression: CompressionOptions(format: .zstd, level: .default)
  )
)
```

**Compression Formats:**

- `.none` - No compression (default)
- `.zstd` - Zstandard compression (recommended for best performance)

**Compression Levels:**

- `.fastest` - Fastest compression, larger output
- `.default` - Balanced speed and size (recommended)
- `.best` - Best compression, slower

**Performance:** Compression adds minimal overhead while reducing scene size by approximately 64%. The default level provides the best balance of speed and compression ratio.

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-string-with-persistence-callback/SaveSceneToStringWithPersistenceCallback.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToStringWithPersistenceCallback(engine: Engine) async throws {
  try engine.editor.setSettingString("basePath", value: "https://cdn.img.ly/packages/imgly/cesdk-engine/1.70.0/assets")
  try await engine.addDefaultAssetSources()
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)
  let blob = try await engine.scene.saveToArchive()
  let sceneArchiveUrl = FileManager.default.temporaryDirectory.appendingPathComponent(
    UUID().uuidString,
    conformingTo: .zip,
  )
  try blob.write(to: sceneArchiveUrl)
  try await engine.scene.loadArchive(from: sceneArchiveUrl)

  var alreadyPersistedURLs: [String: URL] = [:]
  let sceneAsString = try await engine.scene.saveToString(allowedResourceSchemes: ["http", "https"]) { url, hash in
    guard let persistedURL = alreadyPersistedURLs[hash] else {
      do {
        var blob = Data()
        try engine.editor.getResourceData(url: url, chunkSize: 10_000_000) {
          blob.append($0)
          return true
        }
        let persistedURL = URL(string: "https://example.com/" + url.absoluteString.components(separatedBy: "://")[1])!
        var request = URLRequest(url: persistedURL)
        request.httpMethod = "POST"
        let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
        alreadyPersistedURLs[hash] = persistedURL
        return persistedURL
      } catch {
        print("Failed to persist \(url):", error)
        return url
      }
    }
    return persistedURL
  }

  print(sceneAsString)
}
```

## Save Previously Archived Scenes to a String and Persist Resources

In this example, we will show you how to save scenes that were loaded from an archive to a string with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

Some scenes contain resources that are only transient and may be lost after the scene is destroyed.
An example is a scene that was previously saved as an archive.
When loaded, the data of the archived scene's resources is held in in-memory buffers.
Saving again that scene to string would result in a scene with URLs whose schemes are `buffer` which is unusable in any other instance of the editor.
It is best that all resources are put online so they are always available.

To that end, you can use the `saveToString()`'s `allowedResourceSchemes` and `onDisallowedResourceScheme` parameters to be notified of resources whose URL should not end in the final string.
Set the `allowedResourceSchemes` argument to an array of schemes whose values can be kept as-is and set the `onDisallowedResourceScheme` to a function that will save the resource's data to a permanent location and call an embedded callback with the new URL to refer to that resource.
Any resource whose URL scheme is not found in the `allowedResourceSchemes` array will trigger a call of the passed `onDisallowedResourceScheme` argument with the resource's URL, a hash of its data and the embedded callback to call with the new URL.

```swift highlight-saveToStringWithPersistenceCallback
var alreadyPersistedURLs: [String: URL] = [:]
let sceneAsString = try await engine.scene.saveToString(allowedResourceSchemes: ["http", "https"]) { url, hash in
  guard let persistedURL = alreadyPersistedURLs[hash] else {
    do {
      var blob = Data()
      try engine.editor.getResourceData(url: url, chunkSize: 10_000_000) {
        blob.append($0)
        return true
      }
      let persistedURL = URL(string: "https://example.com/" + url.absoluteString.components(separatedBy: "://")[1])!
      var request = URLRequest(url: persistedURL)
      request.httpMethod = "POST"
      let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
      alreadyPersistedURLs[hash] = persistedURL
      return persistedURL
    } catch {
      print("Failed to persist \(url):", error)
      return url
    }
  }
  return persistedURL
}
```

The returned string consists solely of ASCII characters and can safely be used further or written to a database.

```swift highlight-result-callback
print(sceneAsString)
```

### Full Code

Here's the full code:

```swift file=@cesdk_swift_examples/engine-guides-save-scene-to-string-with-persistence-callback/SaveSceneToStringWithPersistenceCallback.swift
import Foundation
import IMGLYEngine

@MainActor
func saveSceneToStringWithPersistenceCallback(engine: Engine) async throws {
  try engine.editor.setSettingString("basePath", value: "https://cdn.img.ly/packages/imgly/cesdk-engine/1.70.0/assets")
  try await engine.addDefaultAssetSources()
  let sceneUrl =
    URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
  try await engine.scene.load(from: sceneUrl)
  let blob = try await engine.scene.saveToArchive()
  let sceneArchiveUrl = FileManager.default.temporaryDirectory.appendingPathComponent(
    UUID().uuidString,
    conformingTo: .zip,
  )
  try blob.write(to: sceneArchiveUrl)
  try await engine.scene.loadArchive(from: sceneArchiveUrl)

  var alreadyPersistedURLs: [String: URL] = [:]
  let sceneAsString = try await engine.scene.saveToString(allowedResourceSchemes: ["http", "https"]) { url, hash in
    guard let persistedURL = alreadyPersistedURLs[hash] else {
      do {
        var blob = Data()
        try engine.editor.getResourceData(url: url, chunkSize: 10_000_000) {
          blob.append($0)
          return true
        }
        let persistedURL = URL(string: "https://example.com/" + url.absoluteString.components(separatedBy: "://")[1])!
        var request = URLRequest(url: persistedURL)
        request.httpMethod = "POST"
        let (data, response) = try await URLSession.shared.upload(for: request, from: blob)
        alreadyPersistedURLs[hash] = persistedURL
        return persistedURL
      } catch {
        print("Failed to persist \(url):", error)
        return url
      }
    }
    return persistedURL
  }

  print(sceneAsString)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
