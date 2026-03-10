# Source: https://img.ly/docs/cesdk/android/concepts/resources-a58d71/

---
title: "Working With Resources"
description: "Preload all resources for blocks or scenes in CE.SDK to improve performance and avoid runtime delays."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/resources-a58d71/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Resources](https://img.ly/docs/cesdk/android/concepts/resources-a58d71/)

---

By default, a scene's resources are loaded on-demand.
You can manually trigger the loading of all resources in a scene of for specific blocks by calling `forceLoadResources`.
Any set of blocks can be passed as argument and whatever resources these blocks require will be loaded.

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to forcibly pre-load all resources contained in a scene.

```kotlin
suspend fun forceLoadResources(blocks: List<DesignBlock>)
```

Begins loading the resources of the given blocks and their children.

If the resource had been loaded earlier and resulted in an error, it will be reloaded.

Note: This function is useful for preloading resources before they are needed.

Warning: For elements with a source set, all elements in the source set will be loaded.

- `blocks`: the blocks whose resources should be loaded. The given blocks don't require to have resources and

can have children blocks (e.g. a scene block or a page block).

### Full Code

Here's the full code:

```kotlin
val scene = requireNotNull(engine.scene.get())

// Forcing  all resources of all the blocks in a scene or the resources of graphic block to load
engine.block.forceLoadResources(listOf(scene))

val graphics = engine.block.findByType(DesignBlockType)
engine.block.forceLoadResources(graphics)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
