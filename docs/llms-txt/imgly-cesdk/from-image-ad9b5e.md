# Source: https://img.ly/docs/cesdk/android/open-the-editor/from-image-ad9b5e/

---
title: "Create From Image"
description: "Open the editor using an image as the base design, with tools ready for immediate editing."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/from-image-ad9b5e/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [Create From Image](https://img.ly/docs/cesdk/android/open-the-editor/from-image-ad9b5e/)

---

```kotlin file=@cesdk_android_examples/engine-guides-create-scene-from-image-blob/CreateSceneFromImageBlob.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import java.io.ByteArrayOutputStream
import java.io.File
import java.net.URL
import java.util.UUID

fun createSceneFromImageBlob(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val blobUrl = URL("https://img.ly/static/ubq_samples/sample_4.jpg")
    val blob = withContext(Dispatchers.IO) {
        val outputStream = ByteArrayOutputStream()
        blobUrl.openStream().use { inputStream ->
            outputStream.use(inputStream::copyTo)
        }
        outputStream.toByteArray()
    }

    val blobFile = withContext(Dispatchers.IO) {
        File.createTempFile(UUID.randomUUID().toString(), ".tmp").apply {
            outputStream().use { it.write(blob) }
        }
    }
    val blobUri = Uri.fromFile(blobFile)

    val scene = engine.scene.createFromImage(blobUri)

    val page = engine.block.findByType(DesignBlockType.Page).first()

    val pageFill = engine.block.getFill(page)
    val imageFillType = engine.block.getType(pageFill)

    engine.stop()
}
```

Starting from an existing image allows you to use the editor for customizing individual assets.
This is done by using `suspend fun createFromImage(imageUri: URI, dpi: Float = 300F, pixelScaleFactor: Float = 1F): DesignBlock` and passing a URI as argument.
The `dpi` argument sets the dots per inch of the scene.
The `pixelScaleFactor` sets the display's pixel scale factor.

```kotlin file=@cesdk_android_examples/engine-guides-create-scene-from-image-url/CreateSceneFromImageURL.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun createSceneFromImageURL(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val imageRemoteUri = Uri.parse("https://img.ly/static/ubq_samples/sample_4.jpg")
    val scene = engine.scene.createFromImage(imageRemoteUri)

    val page = engine.block.findByType(DesignBlockType.Page).first()

    // Get the fill from the page and verify it's an image fill
    val pageFill = engine.block.getFill(page)
    val imageFillType = engine.block.getType(pageFill)

    engine.stop()
}
```

## Create a Scene From an Image URL

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial image. Create an instance of `Uri` using the remote url. Use the object `imageRemoteUri` as a source for the initial image.

```kotlin highlight-createFromImage
val imageRemoteUri = Uri.parse("https://img.ly/static/ubq_samples/sample_4.jpg")
val scene = engine.scene.createFromImage(imageRemoteUri)
```

When starting with an initial image, the scene's page dimensions match the given resource and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun createSceneFromImageURL(
    license: String,
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val imageRemoteUri = Uri.parse("https://img.ly/static/ubq_samples/sample_4.jpg")
    val scene = engine.scene.createFromImage(imageRemoteUri)

    engine.stop()
}
```

## Create A Scene From an Image Blob

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial image provided from a blob. First, get hold of a `blob` by fetching an image from the web. This is just for demonstration purposes and your `blob` object may come from a different source.

```kotlin highlight-blob
val blobUrl = URL("https://img.ly/static/ubq_samples/sample_4.jpg")
val blob = withContext(Dispatchers.IO) {
    val outputStream = ByteArrayOutputStream()
    blobUrl.openStream().use { inputStream ->
        outputStream.use(inputStream::copyTo)
    }
    outputStream.toByteArray()
}
```

Afterward, create a temporary file and save the `Data`. Create an instance of `Uri` using the temporary file.

```kotlin highlight-objectURL
val blobFile = withContext(Dispatchers.IO) {
    File.createTempFile(UUID.randomUUID().toString(), ".tmp").apply {
        outputStream().use { it.write(blob) }
    }
}
val blobUri = Uri.fromFile(blobFile)
```

Use the object `blobUri` as a source for the initial image.

```kotlin highlight-initialImageURL
val scene = engine.scene.createFromImage(blobUri)
```

When starting with an initial image, the scenes page dimensions match the given image, and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import java.io.ByteArrayOutputStream
import java.io.File
import java.net.URL
import java.util.UUID

fun createSceneFromImageBlob(
    license: String,
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val blobUrl = URL("https://img.ly/static/ubq_samples/sample_4.jpg")
    val blob = withContext(Dispatchers.IO) {
        val outputStream = ByteArrayOutputStream()
        blobUrl.openStream().use { inputStream ->
            outputStream.use(inputStream::copyTo)
        }
        outputStream.toByteArray()
    }

    val blobFile = withContext(Dispatchers.IO) {
        File.createTempFile(UUID.randomUUID().toString(), ".tmp").apply {
            outputStream().use { it.write(blob) }
        }
    }
    val blobUri = Uri.fromFile(blobFile)

    val scene = engine.scene.createFromImage(blobUri)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
