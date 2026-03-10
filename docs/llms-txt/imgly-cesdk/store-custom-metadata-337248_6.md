# Source: https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/store-custom-metadata-337248/

---
title: "Store Custom Metadata"
description: "Attach and persist metadata alongside your design, such as tags, version info, or creator details."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/store-custom-metadata-337248/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Store Custom Metadata](https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/store-custom-metadata-337248/)

---

```swift file=@cesdk_swift_examples/engine-guides-store-metadata/StoreMetadata.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func storeMetadata(engine: Engine) async throws {
  var scene = try await engine.scene.create(fromImage:
    .init(string: "https://img.ly/static/ubq_samples/imgly_logo.jpg")!)
  let block = try engine.block.find(byType: .page).first!

  try engine.block.setMetadata(scene, key: "author", value: "img.ly")
  try engine.block.setMetadata(block, key: "customer_id", value: "1234567890")

  /* We can even store complex objects */
  struct Payment: Encodable {
    let id: Int
    let method: String
    let received: Bool
  }

  let payment = Payment(id: 5, method: "credit_card", received: true)

  try engine.block.setMetadata(
    block,
    key: "payment",
    value: String(data: JSONEncoder().encode(payment), encoding: .utf8)!,
  )

  /* This will return "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* This will return "1000000" */
  try engine.block.getMetadata(block, key: "customer_id")

  /* This will return ["customer_id"] */
  try engine.block.findAllMetadata(block)

  try engine.block.removeMetadata(block, key: "payment")

  /* This will return false */
  try engine.block.hasMetadata(block, key: "payment")

  /* We save our scene and reload it from scratch */
  let sceneString = try await engine.scene.saveToString()
  scene = try await engine.scene.load(from: sceneString)

  /* This still returns "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* And this still returns "1234567890" */
  try engine.block.getMetadata(block, key: "customer_id")
}
```

CE.SDK allows you to store custom metadata in your scenes. You can attach metadata to your scene or directly to your individual design blocks within the scene. This metadata is persistent across saving and loading of scenes. It simply consists of key value pairs of strings. Using any string-based serialization format such as JSON will allow you to store even complex objects. Please note that when duplicating blocks their metadata will also be duplicated.

## Working with Metadata

We can add metadata to any design block using `func setMetadata(_ id: DesignBlockID, key: String, value: String) throws`. This also includes the scene block.

```swift highlight-setMetadata
  try engine.block.setMetadata(scene, key: "author", value: "img.ly")
  try engine.block.setMetadata(block, key: "customer_id", value: "1234567890")

  /* We can even store complex objects */
  struct Payment: Encodable {
    let id: Int
    let method: String
    let received: Bool
  }

  let payment = Payment(id: 5, method: "credit_card", received: true)

  try engine.block.setMetadata(
    block,
    key: "payment",
    value: String(data: JSONEncoder().encode(payment), encoding: .utf8)!,
  )
```

We can retrieve metadata from any design block or scene using `func getMetadata(_ id: DesignBlockID, key: String) throws`. Before accessing the metadata you check for its existence using `func hasMetadata(_ id: DesignBlockID, key: String) throws -> Bool`.

```swift highlight-getMetadata
  /* This will return "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* This will return "1000000" */
  try engine.block.getMetadata(block, key: "customer_id")
```

We can query all metadata keys from any design block or scene using `func findAllMetadata(_ id: DesignBlockID) throws -> [String]`. For blocks without any metadata, this will return an empty list.

```swift highlight-findAllMetadata
/* This will return ["customer_id"] */
try engine.block.findAllMetadata(block)
```

If you want to get rid of any metadata, you can use `func removeMetadata(_ id: DesignBlockID, key: String) throws`.

```swift highlight-removeMetadata
  try engine.block.removeMetadata(block, key: "payment")

  /* This will return false */
  try engine.block.hasMetadata(block, key: "payment")
```

Metadata will automatically be saved and loaded as part the scene. So you don't have to worry about it getting lost or having to save it separately.

```swift highlight-persistence
  /* We save our scene and reload it from scratch */
  let sceneString = try await engine.scene.saveToString()
  scene = try await engine.scene.load(from: sceneString)

  /* This still returns "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* And this still returns "1234567890" */
  try engine.block.getMetadata(block, key: "customer_id")
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func storeMetadata(engine: Engine) async throws {
  var scene = try await engine.scene.create(fromImage:
    .init(string: "https://img.ly/static/ubq_samples/imgly_logo.jpg")!)
  let block = try engine.block.find(byType: .graphic).first!

  try engine.block.setMetadata(scene, key: "author", value: "img.ly")
  try engine.block.setMetadata(block, key: "customer_id", value: "1234567890")

  /* We can even store complex objects */
  struct Payment: Encodable {
    let id: Int
    let method: String
    let received: Bool
  }

  let payment = Payment(id: 5, method: "credit_card", received: true)

  try engine.block.setMetadata(
    block,
    key: "payment",
    value: String(data: JSONEncoder().encode(payment), encoding: .utf8)!
  )

  /* This will return "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* This will return "1000000" */
  try engine.block.getMetadata(block, key: "customer_id")

  /* This will return ["customer_id"] */
  try engine.block.findAllMetadata(block)

  try engine.block.removeMetadata(block, key: "payment")

  /* This will return false */
  try engine.block.hasMetadata(block, key: "payment")

  /* We save our scene and reload it from scratch */
  let sceneString = try await engine.scene.saveToString()
  scene = try await engine.scene.load(from: sceneString)

  /* This still returns "img.ly" */
  try engine.block.getMetadata(scene, key: "author")

  /* And this still returns "1234567890" */
  try engine.block.getMetadata(block, key: "customer_id")
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
