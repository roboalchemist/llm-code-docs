# Source: https://img.ly/docs/cesdk/android/edit-video/add-captions-f67565/

---
title: "Add Captions"
description: "Documentation for adding captions to videos"
platform: android
url: "https://img.ly/docs/cesdk/android/edit-video/add-captions-f67565/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/android/create-video-c41a08/) > [Add Captions](https://img.ly/docs/cesdk/android/edit-video/add-captions-f67565/)

---

```kotlin file=@cesdk_android_examples/engine-guides-captions/Captions.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.MimeType
import ly.img.engine.PositionMode
import ly.img.engine.SizeMode

fun editVideoCaptions(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1280, height = 720)

    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    engine.block.setWidth(page, value = 1280F)
    engine.block.setHeight(page, value = 720F)
    engine.editor.setSettingBoolean(keypath = "features/videoCaptionsEnabled", value = true)

    engine.block.setDuration(page, duration = 20.0)

    val caption1 = engine.block.create(DesignBlockType.Caption)
    engine.block.setString(caption1, property = "caption/text", value = "Caption text 1")
    val caption2 = engine.block.create(DesignBlockType.Caption)
    engine.block.setString(caption2, property = "caption/text", value = "Caption text 2")

    val captionTrack = engine.block.create("captionTrack")
    engine.block.appendChild(parent = page, child = captionTrack)
    engine.block.appendChild(parent = captionTrack, child = caption1)
    engine.block.appendChild(parent = captionTrack, child = caption2)

    engine.block.setDuration(caption1, duration = 3.0)
    engine.block.setDuration(caption2, duration = 5.0)

    engine.block.setTimeOffset(caption1, offset = 0.0)
    engine.block.setTimeOffset(caption2, offset = 3.0)

    // Captions can also be loaded from a caption file, i.e., from SRT and VTT files.
    // The text and timing of the captions are read from the file.
    val captions = engine.block.createCaptionsFromURI("https://img.ly/static/examples/captions.srt")
    for (caption in captions) {
        engine.block.appendChild(parent = captionTrack, child = caption)
    }

    // The position and size are synced with all caption blocks in the scene so only needs to be set once.
    engine.block.setPositionX(caption1, 0.05F)
    engine.block.setPositionXMode(caption1, PositionMode.PERCENT)
    engine.block.setPositionY(caption1, 0.8F)
    engine.block.setPositionYMode(caption1, PositionMode.PERCENT)
    engine.block.setHeight(caption1, 0.15F)
    engine.block.setHeightMode(caption1, SizeMode.PERCENT)
    engine.block.setWidth(caption1, 0.9F)
    engine.block.setWidthMode(caption1, SizeMode.PERCENT)

    // The style is synced with all caption blocks in the scene so only needs to be set once.
    engine.block.setColor(caption1, property = "fill/solid/color", value = Color.fromRGBA(0.9F, 0.9F, 0F, 1F))
    engine.block.setBoolean(caption1, property = "dropShadow/enabled", value = true)
    engine.block.setColor(caption1, property = "dropShadow/color", value = Color.fromRGBA(0F, 0F, 0F, 0.8F))

    // Export page as mp4 video.
    val blob = engine.block.exportVideo(
        block = page,
        timeOffset = 0.0,
        duration = engine.block.getDuration(page),
        mimeType = MimeType.MP4,
        progressCallback = {
            println(
                "Rendered ${it.renderedFrames} frames and encoded ${it.encodedFrames} frames out of ${it.totalFrames} frames",
            )
        },
    )

    engine.stop()
}
```

For video scenes, open captions can be added in CE.SDK. These allow to follow the content without the audio.

Two blocks are available for this. The `DesignBlockType.Caption` blocks hold the text of individual captions and the `DesignBlockType.CaptionTrack` is an optional structuring block to hold the `Caption` blocks, e.g., all captions for one video.

The `"playback/timeOffset"` property of each caption block controls when the caption should be shown and the `"playback/duration"` property how long the caption should be shown. Usually, the captions do not overlap. As the playback time of the page progresses, the corresponding caption is shown.

With the `"caption/text"` property, the text of the caption can be set. In addition, all text properties are also available for captions, e.g., to change the font, the font size, or the alignment.

Position, size, and style changes on caption blocks are automatically synced across all caption blocks.

Finally, the whole page can be exported as a video file using the `block.exportVideo` function.

## Creating a Video Scene

First, we create a scene that is set up for captions editing by calling the `scene.createForCaptions()` API. Then we create a page, add it to the scene and define its dimensions. This page will hold our composition.

```kotlin highlight-setupScene
val scene = engine.scene.createForVideo()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
engine.block.setWidth(page, value = 1280F)
engine.block.setHeight(page, value = 720F)
engine.editor.setSettingBoolean(keypath = "features/videoCaptionsEnabled", value = true)
```

## Setting Page Durations

Next, we define the duration of the page using the `fun setDuration(block: DesignBlock, duration: Double)` API to be 20 seconds long. This will be the total duration of our exported captions in the end.

```kotlin highlight-setPageDuration
engine.block.setDuration(page, duration = 20.0)
```

## Adding Captions

In this example, we want to show two captions, one after the other. For this, we create two caption blocks.

```kotlin highlight-createCaptions
val caption1 = engine.block.create(DesignBlockType.Caption)
engine.block.setString(caption1, property = "caption/text", value = "Caption text 1")
val caption2 = engine.block.create(DesignBlockType.Caption)
engine.block.setString(caption2, property = "caption/text", value = "Caption text 2")
```

As an alternative to manually creating the captions, changing the text, and adjusting the timings, the captions can also be loaded from a caption file, i.e., an SRT or VTT file with the `createCaptionsFromURI` API.
This return a list of caption blocks, with the parsed texts and timings. These can be added to a caption track as well.

```kotlin highlight-createCaptionsFromURI
// Captions can also be loaded from a caption file, i.e., from SRT and VTT files.
// The text and timing of the captions are read from the file.
val captions = engine.block.createCaptionsFromURI("https://img.ly/static/examples/captions.srt")
for (caption in captions) {
    engine.block.appendChild(parent = captionTrack, child = caption)
}
```

## Creating a Captions Track

While we could add the two blocks directly to the page, we can alternatively also use the `captionTrack` block to group them.

Caption tracks themselves cannot be selected directly by clicking on the canvas, nor do they have any visual representation.

We create a `captionTrack` block, add it to the page and add both captions in the order in which they should play as the track's children.

The dimensions of a `captionTrack` are always derived from the dimensions of its children, so you should not call the `setWidth` or `setHeight` APIs on a track, but on its children instead.

```kotlin highlight-addToTrack
val captionTrack = engine.block.create("captionTrack")
engine.block.appendChild(parent = page, child = captionTrack)
engine.block.appendChild(parent = captionTrack, child = caption1)
engine.block.appendChild(parent = captionTrack, child = caption2)
```

## Modifying Captions

By default, each caption block has a duration of 3 seconds after it is created. If we want to show it on the page for a different amount of time, we can use the `setDuration` API.

```kotlin highlight-setDuration
engine.block.setDuration(caption1, duration = 3.0)
engine.block.setDuration(caption2, duration = 5.0)
```

```kotlin highlight-setTimeOffset
engine.block.setTimeOffset(caption1, offset = 0.0)
engine.block.setTimeOffset(caption2, offset = 3.0)
```

The position and size of the captions is automatically synced across all captions that are attached to the scene. Therefore, changes only need to be made on one of the caption blocks.

```kotlin highlight-positionAndSize
// The position and size are synced with all caption blocks in the scene so only needs to be set once.
engine.block.setPositionX(caption1, 0.05F)
engine.block.setPositionXMode(caption1, PositionMode.PERCENT)
engine.block.setPositionY(caption1, 0.8F)
engine.block.setPositionYMode(caption1, PositionMode.PERCENT)
engine.block.setHeight(caption1, 0.15F)
engine.block.setHeightMode(caption1, SizeMode.PERCENT)
engine.block.setWidth(caption1, 0.9F)
engine.block.setWidthMode(caption1, SizeMode.PERCENT)
```

The styling of the captions is also automatically synced across all captions that are attached to the scene. For example, changing the text color to red on the first block, changes it on all caption blocks.

```kotlin highlight-changeStyle
// The style is synced with all caption blocks in the scene so only needs to be set once.
engine.block.setColor(caption1, property = "fill/solid/color", value = Color.fromRGBA(0.9F, 0.9F, 0F, 1F))
engine.block.setBoolean(caption1, property = "dropShadow/enabled", value = true)
engine.block.setColor(caption1, property = "dropShadow/color", value = Color.fromRGBA(0F, 0F, 0F, 0.8F))
```

## Exporting Video

You can start exporting the entire page as a captions file by calling `block.exportVideo`. The encoding process will run in the background. You can get notified about the progress of the encoding process by using `progressCallback` parameter.

Since the encoding process runs in the background, the engine will stay interactive. So, you can continue to use the engine to manipulate the scene. Please note that these changes won't be visible in the exported captions file because the scene's state has been frozen at the start of the export.

```kotlin highlight-exportVideo
// Export page as mp4 video.
val blob = engine.block.exportVideo(
    block = page,
    timeOffset = 0.0,
    duration = engine.block.getDuration(page),
    mimeType = MimeType.MP4,
    progressCallback = {
        println(
            "Rendered ${it.renderedFrames} frames and encoded ${it.encodedFrames} frames out of ${it.totalFrames} frames",
        )
    },
)
```

## Full Code

Here's the full code:

```kotlin file=@cesdk_android_examples/engine-guides-captions/Captions.kt
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.MimeType
import ly.img.engine.PositionMode
import ly.img.engine.SizeMode

fun editVideoCaptions(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1280, height = 720)

    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    engine.block.setWidth(page, value = 1280F)
    engine.block.setHeight(page, value = 720F)
    engine.editor.setSettingBoolean(keypath = "features/videoCaptionsEnabled", value = true)

    engine.block.setDuration(page, duration = 20.0)

    val caption1 = engine.block.create(DesignBlockType.Caption)
    engine.block.setString(caption1, property = "caption/text", value = "Caption text 1")
    val caption2 = engine.block.create(DesignBlockType.Caption)
    engine.block.setString(caption2, property = "caption/text", value = "Caption text 2")

    val captionTrack = engine.block.create("captionTrack")
    engine.block.appendChild(parent = page, child = captionTrack)
    engine.block.appendChild(parent = captionTrack, child = caption1)
    engine.block.appendChild(parent = captionTrack, child = caption2)

    engine.block.setDuration(caption1, duration = 3.0)
    engine.block.setDuration(caption2, duration = 5.0)

    engine.block.setTimeOffset(caption1, offset = 0.0)
    engine.block.setTimeOffset(caption2, offset = 3.0)

    // Captions can also be loaded from a caption file, i.e., from SRT and VTT files.
    // The text and timing of the captions are read from the file.
    val captions = engine.block.createCaptionsFromURI("https://img.ly/static/examples/captions.srt")
    for (caption in captions) {
        engine.block.appendChild(parent = captionTrack, child = caption)
    }

    // The position and size are synced with all caption blocks in the scene so only needs to be set once.
    engine.block.setPositionX(caption1, 0.05F)
    engine.block.setPositionXMode(caption1, PositionMode.PERCENT)
    engine.block.setPositionY(caption1, 0.8F)
    engine.block.setPositionYMode(caption1, PositionMode.PERCENT)
    engine.block.setHeight(caption1, 0.15F)
    engine.block.setHeightMode(caption1, SizeMode.PERCENT)
    engine.block.setWidth(caption1, 0.9F)
    engine.block.setWidthMode(caption1, SizeMode.PERCENT)

    // The style is synced with all caption blocks in the scene so only needs to be set once.
    engine.block.setColor(caption1, property = "fill/solid/color", value = Color.fromRGBA(0.9F, 0.9F, 0F, 1F))
    engine.block.setBoolean(caption1, property = "dropShadow/enabled", value = true)
    engine.block.setColor(caption1, property = "dropShadow/color", value = Color.fromRGBA(0F, 0F, 0F, 0.8F))

    // Export page as mp4 video.
    val blob = engine.block.exportVideo(
        block = page,
        timeOffset = 0.0,
        duration = engine.block.getDuration(page),
        mimeType = MimeType.MP4,
        progressCallback = {
            println(
                "Rendered ${it.renderedFrames} frames and encoded ${it.encodedFrames} frames out of ${it.totalFrames} frames",
            )
        },
    )

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
