# Source: https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/

---
title: "Save"
description: "Save design progress locally or to a backend service to allow for later editing or publishing."
platform: android
url: "https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Save](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/)

---

The CreativeEngine allows you to save scenes in a binary format to share them between editors or store them for later editing.

Saving a scene can be done as a either scene file or as an archive file. A scene file does not include any fonts or images. Only the source URIs of assets, the general layout, and element properties are stored. When loading scenes in a new environment, ensure previously used asset URIs are available. Conversely, an archive file contains within it the scene's assets and references them as relative URIs.

> **Note:** **Warning** A scene file does not include any fonts or images. Only the source
> URIs of assets, the general layout, and element properties are stored. When
> loading scenes in a new environment, ensure previously used asset URIs are
> available.

```kotlin file=@cesdk_android_examples/engine-guides-save-scene-to-archive/SaveSceneToArchive.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.net.HttpURLConnection
import java.net.URL
import java.nio.channels.Channels

fun saveSceneToArchive(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val blob = engine.scene.saveToArchive(scene = scene)

    withContext(Dispatchers.IO) {
        val connection = URL("https://example.com/upload/").openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.doOutput = true
        connection.outputStream.use { Channels.newChannel(it).write(blob) }
        connection.connect()
    }

    engine.stop()
}
```

## Save Scenes to an Archive

In this example, we will show you how to save scenes as an archive with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

As an archive, the resulting `Blob` includes all pages and any hidden elements and all the asset data.

To get hold of such a `Blob`, you need to use `engine.scene.saveToArchive()`.
This is an asynchronous method.
After waiting for the coroutine to finish, we receive a `Blob` holding the entire scene currently loaded in the editor including its assets' data.

```kotlin highlight-saveToArchive
val blob = engine.scene.saveToArchive(scene = scene)
```

That `Blob` can then be treated as a form file parameter and sent to a remote location.

```kotlin highlight-create-form-data-archive
withContext(Dispatchers.IO) {
    val connection = URL("https://example.com/upload/").openConnection() as HttpURLConnection
    connection.requestMethod = "POST"
    connection.doOutput = true
    connection.outputStream.use { Channels.newChannel(it).write(blob) }
    connection.connect()
}
```

### Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.net.HttpURLConnection
import java.net.URL
import java.nio.channels.Channels

fun saveSceneToArchive(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val blob = engine.scene.saveToArchive(scene = scene)

    withContext(Dispatchers.IO) {
        val connection = URL("https://example.com/upload/").openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.doOutput = true
        connection.outputStream.use { Channels.newChannel(it).write(blob) }
        connection.connect()
    }

    engine.stop()
}
```

```kotlin file=@cesdk_android_examples/engine-guides-save-scene-to-blob/SaveSceneToBlob.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.net.HttpURLConnection
import java.net.URL

fun saveSceneToBlob(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
    uploadUrl: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val savedSceneString = engine.scene.saveToString(scene = scene)

    val blob = savedSceneString.toByteArray(Charsets.UTF_8)

    runCatching {
        withContext(Dispatchers.IO) {
            val connection = URL(uploadUrl).openConnection() as HttpURLConnection
            connection.requestMethod = "POST"
            connection.doOutput = true
            connection.outputStream.use { it.write(blob) }
            connection.connect()
        }
    }

    engine.stop()
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

```kotlin highlight-saveToBlob
val savedSceneString = engine.scene.saveToString(scene = scene)
```

The returned string consists solely of ASCII characters and can safely be used further or written to a database.

```kotlin highlight-create-blob
val blob = savedSceneString.toByteArray(Charsets.UTF_8)
```

That object can then be treated as a form file parameter and sent to a remote location.

```kotlin highlight-create-form-data-blob
runCatching {
    withContext(Dispatchers.IO) {
        val connection = URL(uploadUrl).openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.doOutput = true
        connection.outputStream.use { it.write(blob) }
        connection.connect()
    }
}
```

### Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.net.HttpURLConnection
import java.net.URL

fun saveSceneToBlob(
    license: String,
    userId: String,
    uploadUrl: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val savedSceneString = engine.scene.saveToString(scene = scene)

    val blob = savedSceneString.toByteArray(Charsets.UTF_8)

    runCatching {
        withContext(Dispatchers.IO) {
            val connection = URL(uploadUrl).openConnection() as HttpURLConnection
            connection.requestMethod = "POST"
            connection.doOutput = true
            connection.outputStream.use { it.write(blob) }
            connection.connect()
        }
    }

    engine.stop()
}
```

```kotlin file=@cesdk_android_examples/engine-guides-save-scene-to-string/SaveSceneToString.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun saveSceneToString(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val savedSceneString = engine.scene.saveToString(scene = scene)

    println(savedSceneString)

    engine.stop()
}
```

## Save Scenes to a String

In this example, we will show you how to save scenes as a string with the [CreativeEditor SDK](https://img.ly/products/creative-sdk).

This is done by converting the contents of a scene to a single string, which can then be stored or transferred.

To get hold of such a string, you need to use `engine.scene.saveToString()`.
This is an asynchronous method.
After waiting for the coroutine to finish, we receive a plain string holding the entire scene currently loaded in the editor.
This includes all pages and any hidden elements, but none of the actual asset data.

```kotlin highlight-saveToString
val savedSceneString = engine.scene.saveToString(scene = scene)
```

The returned string consists solely of ASCII characters and can safely be used further or written to a database.

```kotlin highlight-result-string
println(savedSceneString)
```

## Full Code

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun saveSceneToString(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUri = Uri.parse(
        "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
    )
    val scene = engine.scene.load(sceneUri = sceneUri)

    val savedSceneString = engine.scene.saveToString(scene = scene)

    println(savedSceneString)

    engine.stop()
}
```

## Compression Options

CE.SDK supports optional compression for saved scenes to reduce file size. Compression is particularly useful for large scenes or when storage space is limited.

```kotlin
// Save with Zstd compression (recommended)
val compressed = engine.scene.saveToString(
    scene = scene,
    options = SaveToStringOptions(
        compression = CompressionOptions(
            format = CompressionFormat.ZSTD,
            level = CompressionLevel.DEFAULT
        )
    )
)
```

**Compression Formats:**

- `CompressionFormat.NONE` - No compression (default)
- `CompressionFormat.ZSTD` - Zstandard compression (recommended for best performance)

**Compression Levels:**

- `CompressionLevel.FASTEST` - Fastest compression, larger output
- `CompressionLevel.DEFAULT` - Balanced speed and size (recommended)
- `CompressionLevel.BEST` - Best compression, slower

**Performance:** Compression adds minimal overhead while reducing scene size by approximately 64%. The default level provides the best balance of speed and compression ratio.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
