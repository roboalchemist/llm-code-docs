# Source: https://img.ly/docs/cesdk/android/open-the-editor/from-video-86beb0/

---
title: "Create From Video"
description: "Load a video file into the editor to start editing frame-based or timeline-based video content."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/from-video-86beb0/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [Create From Video](https://img.ly/docs/cesdk/android/open-the-editor/from-video-86beb0/)

---

```kotlin file=@cesdk_android_examples/engine-guides-create-scene-from-video-url/CreateSceneFromVideoURL.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine

fun createSceneFromVideoURL(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val videoRemoteUri = Uri.parse("https://img.ly/static/ubq_video_samples/bbb.mp4")
    val scene = engine.scene.createFromVideo(videoRemoteUri)

    // Find the automatically added graphic block in the scene that contains the video fill.
    val block = engine.block.findByType(DesignBlockType.Graphic).first()

    // Change its opacity.
    engine.block.setOpacity(block, value = 0.5F)

    engine.stop()
}
```

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk) with an initial video.

Starting from an existing video allows you to use the editor for customizing individual assets.
This is done by using `suspend fun createFromVideo(videoUri: URI): DesignBlock` and passing a URI as argument.

Create an instance of `Uri` using the remote url.
Use the object `videoRemoteUri` as a source for the initial video.

```kotlin highlight-createFromVideo
val videoRemoteUri = Uri.parse("https://img.ly/static/ubq_video_samples/bbb.mp4")
val scene = engine.scene.createFromVideo(videoRemoteUri)
```

We can retrieve the graphic block id of this initial video using `fun findByType(blockType: DesignBlockType): List<DesignBlock>`.
Note that that function returns an array.
Since there's only a single graphic block in the scene, the block is at index `0`.

```kotlin highlight-findByType
// Find the automatically added graphic block in the scene that contains the video fill.
val block = engine.block.findByType(DesignBlockType.Graphic).first()
```

We can then manipulate and modify this block.
Here we modify its opacity with `fun setOpacity(block: DesignBlock, @FloatRange(from = 0.0, to = 1.0) value: Float)`.
See [Modifying Scenes](https://img.ly/docs/cesdk/android/concepts/blocks-90241e/) for more details.

```kotlin highlight-setOpacity
// Change its opacity.
engine.block.setOpacity(block, value = 0.5F)
```

When starting with an initial video, the scene's page dimensions match the given resource and the scene is configured to be in pixel design units.

To later save your scene, see [Saving Scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/).

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.*
import ly.img.engine.*

fun createSceneFromVideoURL(
    license: String,
    userId: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val videoRemoteUri = Uri.parse("https://img.ly/static/ubq_video_samples/bbb.mp4")
    val scene = engine.scene.createFromVideo(videoRemoteUri)

    // Find the automatically added graphic block in the scene that contains the video fill.
    val block = engine.block.findByType(DesignBlockType.Graphic).first()

    // Change its opacity.
    engine.block.setOpacity(block, value = 0.5F)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
