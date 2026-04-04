# Source: https://img.ly/docs/cesdk/ios/concepts/resources-a58d71/

---
title: "Working With Resources"
description: "Preload all resources for blocks or scenes in CE.SDK to improve performance and avoid runtime delays."
platform: ios
url: "https://img.ly/docs/cesdk/ios/concepts/resources-a58d71/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/ios/concepts-c9ff51/) > [Resources](https://img.ly/docs/cesdk/ios/concepts/resources-a58d71/)

---

```swift reference-only
let scene = try engine.scene.get()!

// Forcing  all resources of all the blocks in a scene or the resources of graphic block to load
try await engine.block.forceLoadResources([scene])

let graphics = try engine.block.find(byType: .graphic)
try await engine.block.forceLoadResources(graphics)
```

By default, a scene's resources are loaded on-demand.
You can manually trigger the loading of all resources in a scene of for specific blocks by calling `forceLoadResources`.
Any set of blocks can be passed as argument and whatever resources these blocks require will be loaded.

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to forcibly pre-load all resources contained in a scene.

```swift
public func forceLoadResources(_ ids: [DesignBlockID]) async throws
```

Begins loading the resources of the given blocks and their children. If the resource had been loaded earlier and
resulted in an error, it will be reloaded. This function is useful for preloading
resources before they are needed.
Warning: For elements with a source set, all elements in the source set will be loaded.

- `ids:`: The blocks whose resources should be loaded. The given blocks don't require to have resources and
  can have children blocks (e.g. a scene block or a page block).

### Full Code

Here's the full code:

```swift
let scene = try engine.scene.get()!

// Forcing  all resources of all the blocks in a scene or the resources of graphic block to load
try await engine.block.forceLoadResources([scene])

let graphics = try engine.block.find(byType: .graphic)
try await engine.block.forceLoadResources(graphics)
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
