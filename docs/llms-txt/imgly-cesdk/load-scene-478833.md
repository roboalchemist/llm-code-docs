# Source: https://img.ly/docs/cesdk/android/open-the-editor/load-scene-478833/

---
title: "Load a Scene"
description: "Load existing design scenes into the editor to resume or modify previous work."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/load-scene-478833/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [Load a Scene](https://img.ly/docs/cesdk/android/open-the-editor/load-scene-478833/)

---

```kotlin file=@cesdk_android_examples/engine-guides-load-scene-from-blob/LoadSceneFromBlob.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import java.io.ByteArrayOutputStream
import java.net.URL

fun loadSceneFromBlob(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val sceneUrl = URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val sceneBlob = withContext(Dispatchers.IO) {
        val outputStream = ByteArrayOutputStream()
        sceneUrl.openStream().use { inputStream ->
            outputStream.use(inputStream::copyTo)
        }
        outputStream.toByteArray()
    }

    val blobString = String(sceneBlob, Charsets.UTF_8)

    val scene = engine.scene.load(scene = blobString)

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

```kotlin file=@cesdk_android_examples/engine-guides-load-scene-from-string/LoadSceneFromString.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import java.io.ByteArrayOutputStream
import java.net.URL

fun loadSceneFromString(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val sceneUrl = URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val sceneBlob = withContext(Dispatchers.IO) {
        val outputStream = ByteArrayOutputStream()
        sceneUrl.openStream().use { inputStream ->
            outputStream.use(inputStream::copyTo)
        }
        outputStream.toByteArray()
    }
    val blobString = String(sceneBlob, Charsets.UTF_8)

    val scene = engine.scene.load(scene = blobString)

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

```kotlin file=@cesdk_android_examples/engine-guides-load-scene-from-remote/LoadSceneFromRemote.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun loadSceneFromRemote(
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

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

Loading an existing scene allows resuming work on a previous session or adapting an existing template to your needs.

> **Note:** **Warning** Saving a scene can be done as a either <em>scene file</em> or as
> an <em>archive file</em> (c.f.
> [Saving scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/)). A <em>scene file</em> does
> not include any fonts or images. Only the source URIs of assets, the general
> layout, and element properties are stored. When loading scenes in a new
> environment, ensure previously used asset URIs are available. Conversely, an
> <em>archive file</em> contains within it the scene's assets and references
> them as relative URIs.

## Load Scenes from a Remote URL

Determine a url that points to a scene binary string.
Create an instance of `Uri` using the remote url.

```kotlin highlight-url
val sceneUri = Uri.parse(
    "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
)
```

We can then pass the object `sceneUri` to the `suspend fun load(sceneUri: Uri): DesignBlock` function.
The editor will reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```kotlin highlight-load-remote
val scene = engine.scene.load(sceneUri = sceneUri)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for more details.

```kotlin highlight-modify-text-remote
val text = engine.block.findByType(DesignBlockType.Text).first()
engine.block.setDropShadowEnabled(text, enabled = true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.*
import ly.img.engine.*

fun loadSceneFromRemote(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUri =
        Uri.parse(
            "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene",
        )

    val scene = engine.scene.load(sceneUri = sceneUri)

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

## Load Scenes from a String

In this example, we fetch a scene from a remote url and load it as a string.
This string could also come from the result of `suspend fun saveToString(): String`.

```kotlin highlight-fetch-string
val sceneUrl = URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
val sceneBlob = withContext(Dispatchers.IO) {
    val outputStream = ByteArrayOutputStream()
    sceneUrl.openStream().use { inputStream ->
        outputStream.use(inputStream::copyTo)
    }
    outputStream.toByteArray()
}
val blobString = String(sceneBlob, Charsets.UTF_8)
```

We can then pass that string to the `suspend fun load(scene: String): DesignBlock` function.
The editor will then reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```kotlin highlight-load-string
val scene = engine.scene.load(scene = blobString)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for more details.

```kotlin highlight-modify-text-string
val text = engine.block.findByType(DesignBlockType.Text).first()
engine.block.setDropShadowEnabled(text, enabled = true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.*
import ly.img.engine.*
import java.io.ByteArrayOutputStream
import java.net.URL

fun loadSceneFromString(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUrl =
        URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val sceneBlob =
        withContext(Dispatchers.IO) {
            val outputStream = ByteArrayOutputStream()
            sceneUrl.openStream().use { inputStream ->
                outputStream.use(inputStream::copyTo)
            }
            outputStream.toByteArray()
        }
    val blobString = String(sceneBlob, Charsets.UTF_8)

    val scene = engine.scene.load(scene = blobString)

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

## Load Scenes From a Blob

In this example, we fetch a scene from a remote url and load it as `sceneBlob`.

```kotlin highlight-fetch-blob
val sceneUrl = URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
val sceneBlob = withContext(Dispatchers.IO) {
    val outputStream = ByteArrayOutputStream()
    sceneUrl.openStream().use { inputStream ->
        outputStream.use(inputStream::copyTo)
    }
    outputStream.toByteArray()
}
```

To acquire a scene string from `sceneBlob`, we need to read its contents into a string.

```kotlin highlight-read-blob
val blobString = String(sceneBlob, Charsets.UTF_8)
```

We can then pass that string to the `suspend fun load(scene: String): DesignBlock` function.
The editor will reset and present the given scene to the user.
The function is asynchronous and it does not throw if the scene load succeeded.

```kotlin highlight-load-blob
val scene = engine.scene.load(scene = blobString)
```

From this point on we can continue to modify our scene.
In this example, assuming the scene contains a text element, we add a drop shadow to it.
See [Modifying Scenes](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for more details.

```kotlin highlight-modify-text-blob
val text = engine.block.findByType(DesignBlockType.Text).first()
engine.block.setDropShadowEnabled(text, enabled = true)
```

Scene loads may be reverted using `engine.editor.undo()`.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

### Full Code

Here's the full code:

```kotlin
import kotlinx.coroutines.*
import ly.img.engine.*
import java.io.ByteArrayOutputStream
import java.net.URL

fun loadSceneFromBlob(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val sceneUrl =
        URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val sceneBlob =
        withContext(Dispatchers.IO) {
            val outputStream = ByteArrayOutputStream()
            sceneUrl.openStream().use { inputStream ->
                outputStream.use(inputStream::copyTo)
            }
            outputStream.toByteArray()
        }

    val blobString = String(sceneBlob, Charsets.UTF_8)

    val scene = engine.scene.load(scene = blobString)

    val text = engine.block.findByType(DesignBlockType.Text).first()
    engine.block.setDropShadowEnabled(text, enabled = true)

    engine.stop()
}
```

```kotlin reference-only
val scene = requireNotNull(engine.scene.get())

// Forcing  all resources of all the blocks in a scene or the resources of graphic block to load
engine.block.forceLoadResources(listOf(scene))

val graphics = engine.block.findByType(DesignBlockType)
engine.block.forceLoadResources(graphics)
```

## Loading Scene Archives

Loading a scene archives requires unzipping the archives contents to a location, that's accessible to the CreativeEngine. One could for example unzip the archive via `unzip archive.zip` and then serve its contents using `$ npx serve`. This spins up a local test server, that serves everything contained in the current directory at `http://localhost:3000`

The archive can then be loaded by calling `engine.scene.load("http://localhost:3000/scene.scene")`. See [loading scenes](https://img.ly/docs/cesdk/android/open-the-editor/load-scene-478833/) for more details. All asset paths in the archive are then resolved relative to the location of the `scene.scene` file. For an image, that would result in `'http://localhost:3000/images/1234.jpeg'`. After loading all URLs are fully resolved with the location of the `scene.scene` file and the scene behaves like any other scene.

### Resolving assets from a different source

The engine will use its [URI resolver](https://img.ly/docs/cesdk/android/open-the-editor/uri-resolver-36b624/) to resolve all asset paths it encounters. This allows you to redirect requests for the assets contained in archive to a different location. To do so, you can add a custom resolver, that redirects requests for assets to a different location. Assuming you store your archived scenes in a `scenes/` directory, this would be an example of how to do so:

```kotlin
	engine.editor.setURIResolver {
		val uri = java.net.URI(it.path)
		if (uri.host == "localhost" && uri.path.startsWith("/scenes") && !uri.path.endsWith(".scene")) {
			// Apply custom logic here, e.g. redirect to a different server
		}
		engine.editor.defaultURIResolver(it)
	}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
