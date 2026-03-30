# Source: https://img.ly/docs/cesdk/android/export-save-publish/store-custom-metadata-337248/

---
title: "Store Custom Metadata"
description: "Attach and persist metadata alongside your design, such as tags, version info, or creator details."
platform: android
url: "https://img.ly/docs/cesdk/android/export-save-publish/store-custom-metadata-337248/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Store Custom Metadata](https://img.ly/docs/cesdk/android/export-save-publish/store-custom-metadata-337248/)

---

```kotlin file=@cesdk_android_examples/engine-guides-store-metadata/StoreMetadata.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun storeMetadata(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    var scene = engine.scene.createFromImage(
        Uri.parse("https://img.ly/static/ubq_samples/imgly_logo.jpg"),
    )
    val block = engine.block.findByType(DesignBlockType.Page).first()

    engine.block.setMetadata(scene, key = "author", value = "img.ly")
    engine.block.setMetadata(block, key = "customer_id", value = "1234567890")
    engine.block.setMetadata(block, key = "customer_name", value = "Name")

    // This will return "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // This will return "1000000"
    engine.block.getMetadata(block, key = "customer_id")

    // This will return ["customer_id", "customer_name"]
    engine.block.findAllMetadata(block)

    engine.block.removeMetadata(block, key = "customer_id")

    // This will return false
    engine.block.hasMetadata(block, key = "customer_id")

    // We save our scene and reload it from scratch
    val sceneString = engine.scene.saveToString(scene)
    scene = engine.scene.load(scene = sceneString)

    // This still returns "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // And this still returns "Name"
    engine.block.getMetadata(block, key = "customer_name")

    engine.stop()
}
```

CE.SDK allows you to store custom metadata in your scenes. You can attach metadata to your scene or directly to your individual design blocks within the scene. This metadata is persistent across saving and loading of scenes. It simply consists of key value pairs of strings. Using any string-based serialization format such as JSON will allow you to store even complex objects. Please note that when duplicating blocks their metadata will also be duplicated.

## Working with Metadata

We can add metadata to any design block using `fun setMetadata(block: DesignBlock, key: String, value: String)`. This also includes the scene block.

```kotlin highlight-setMetadata
engine.block.setMetadata(scene, key = "author", value = "img.ly")
engine.block.setMetadata(block, key = "customer_id", value = "1234567890")
engine.block.setMetadata(block, key = "customer_name", value = "Name")
```

We can retrieve metadata from any design block or scene using `fun getMetadata(block: DesignBlock, key: String): String`. Before accessing the metadata you check for its existence using `fun hasMetadata(block: DesignBlock, key: String): Boolean`.

```kotlin highlight-getMetadata
    // This will return "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // This will return "1000000"
    engine.block.getMetadata(block, key = "customer_id")
```

We can query all metadata keys from any design block or scene using `fun findAllMetadata(block: DesignBlock): List<String>`. For blocks without any metadata, this will return an empty list.

```kotlin highlight-findAllMetadata
// This will return ["customer_id", "customer_name"]
engine.block.findAllMetadata(block)
```

If you want to get rid of any metadata, you can use `fun removeMetadata(block: DesignBlock, key: String)`.

```kotlin highlight-removeMetadata
    engine.block.removeMetadata(block, key = "customer_id")

    // This will return false
    engine.block.hasMetadata(block, key = "customer_id")
```

Metadata will automatically be saved and loaded as part the scene. So you don't have to worry about it getting lost or having to save it separately.

```kotlin highlight-persistence
    // We save our scene and reload it from scratch
    val sceneString = engine.scene.saveToString(scene)
    scene = engine.scene.load(scene = sceneString)

    // This still returns "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // And this still returns "Name"
    engine.block.getMetadata(block, key = "customer_name")
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun storeMetadata(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    var scene = engine.scene.createFromImage(
        Uri.parse("https://img.ly/static/ubq_samples/imgly_logo.jpg"),
    )
    val block = engine.block.findByType(DesignBlockType.Graphic).first()

    engine.block.setMetadata(scene, key = "author", value = "img.ly")
    engine.block.setMetadata(block, key = "customer_id", value = "1234567890")
    engine.block.setMetadata(block, key = "customer_name", value = "Name")

    // This will return "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // This will return "1000000"
    engine.block.getMetadata(block, key = "customer_id")

    // This will return ["customer_id", "customer_name"]
    engine.block.findAllMetadata(block)

    engine.block.removeMetadata(block, key = "customer_id")

    // This will return false
    engine.block.hasMetadata(block, key = "customer_id")

    // We save our scene and reload it from scratch
    val sceneString = engine.scene.saveToString(scene)
    scene = engine.scene.load(scene = sceneString)

    // This still returns "img.ly"
    engine.block.getMetadata(scene, key = "author")

    // And this still returns "Name"
    engine.block.getMetadata(block, key = "customer_name")

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
