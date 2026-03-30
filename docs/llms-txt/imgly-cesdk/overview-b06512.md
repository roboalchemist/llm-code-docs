# Source: https://img.ly/docs/cesdk/android/create-video/overview-b06512/

---
title: "Create Videos Overview"
description: "Learn how to create and customize videos in CE.SDK using scenes, assets, and timeline-based editing."
platform: android
url: "https://img.ly/docs/cesdk/android/create-video/overview-b06512/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/android/create-video-c41a08/) > [Overview](https://img.ly/docs/cesdk/android/create-video/overview-b06512/)

---

```kotlin file=@cesdk_android_examples/engine-guides-video/Video.kt reference-only
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.MimeType
import ly.img.engine.ShapeType

fun editVideo(
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
    engine.block.setDuration(page, duration = 20.0)
    val video1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
    )
    engine.block.setFill(video1, fill = videoFill)

    val video2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill2 = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4",
    )
    engine.block.setFill(video2, fill = videoFill2)
    val track = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = track)
    engine.block.appendChild(parent = track, child = video1)
    engine.block.appendChild(parent = track, child = video2)
    engine.block.fillParent(track)
    engine.block.setDuration(video1, duration = 15.0)
    // Make sure that the video is loaded before calling the trim APIs.
    engine.block.forceLoadAVResource(videoFill)
    engine.block.setTrimOffset(videoFill, offset = 1.0)
    engine.block.setTrimLength(videoFill, length = 10.0)
    engine.block.setLooping(videoFill, looping = true)

    engine.block.setMuted(videoFill, muted = true)

    val audio = engine.block.create(DesignBlockType.Audio)
    engine.block.appendChild(parent = page, child = audio)
    engine.block.setString(
        block = audio,
        property = "audio/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
    )
    // Set the volume level to 70%.
    engine.block.setVolume(audio, volume = 0.7F)
    // Start the audio after two seconds of playback.
    engine.block.setTimeOffset(audio, offset = 2.0)
    // Give the Audio block a duration of 7 seconds.
    engine.block.setDuration(audio, duration = 7.0)
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

In addition to static designs, CE.SDK also allows you to create and edit videos. Working with videos introduces the concept of time into the scene, which requires you to switch the scene into the `"Video"` mode.

In this mode, each page in the scene has its own separate timeline within which its children can be placed. The `"playback/time"` property of each page controls the progress of time through the page.

In order to add videos to your pages, you can add a block with a `FillType.video` fill. As the playback time of the page progresses, the corresponding point in time of the video fill is rendered by the block.

You can also customize the video fill's trim in order to control the portion of the video that should be looped while the block is visible.

`DesignBlockType.Audio` blocks can be added to the scene in order to play an audio file during playback.

The `playback/timeOffset` property controls after how many seconds the audio should begin to play, while the duration property defines how long the audio should play. The same APIs can be used for other design blocks as well, such as text or graphic blocks.

Finally, the whole page can be exported as a video file using the `BlockApi.exportVideo` function.

## Creating a Video Scene

First, we create a scene that is set up for video editing by calling the `scene.createForVideo()` API. Then we create a page, add it to the scene and define its dimensions. This page will hold our composition.

```kotlin highlight-setupScene
val scene = engine.scene.createForVideo()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
engine.block.setWidth(page, value = 1280F)
engine.block.setHeight(page, value = 720F)
```

## Setting Page Durations

Next, we define the duration of the page using the `fun setDuration(block: DesignBlock, duration: Double)` API to be 20 seconds long. This will be the total duration of our exported video in the end.

```kotlin highlight-setPageDuration
engine.block.setDuration(page, duration = 20.0)
```

## Adding Videos

In this example, we want to show two videos, one after the other. For this, we first create two graphic blocks and assign two `'video'` fills to them.

```kotlin highlight-assignVideoFill
    val video1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
    )
    engine.block.setFill(video1, fill = videoFill)

    val video2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill2 = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4",
    )
    engine.block.setFill(video2, fill = videoFill2)
```

## Creating a Track

While we could add the two blocks directly to the page and manually set their sizes and time offsets, we can alternatively also use the `DesignBlockType.Track` block to simplify this work. A track automatically adjusts the time offsets of its children to make sure that they play one after another without any gaps, based on each child's duration.

Tracks themselves cannot be selected directly by clicking on the canvas, nor do they have any visual representation.

We create a `DesignBlockType.Track` block, add it to the page and add both videos in the order in which they should play as the track's children. Next, we use the `fillParent` API, which will resize all children of the track to the same dimensions as the page.

The dimensions of a track are always derived from the dimensions of its children, so you should not call the `setWidth` or `setHeight` APIs on a track, but on its children instead if you can't use the `fillParent` API.

```kotlin highlight-addToTrack
val track = engine.block.create(DesignBlockType.Track)
engine.block.appendChild(parent = page, child = track)
engine.block.appendChild(parent = track, child = video1)
engine.block.appendChild(parent = track, child = video2)
engine.block.fillParent(track)
```

By default, each block has a duration of 5 seconds after it is created. If we want to show it on the page for a different amount of time, we can use the `setDuration` API.

Note that we can just increase the duration of the first video block to 15 seconds without having to adjust anything about the second video. The `track` takes care of that for us automatically so that the second video starts playing after 15 seconds.

```kotlin highlight-setDuration
engine.block.setDuration(video1, duration = 15.0)
```

If the video is longer than the duration of the graphic block that it's attached to, it will cut off once the duration of the graphic is reached. If it is too short, the video will automatically loop for as long as its graphic block is visible.

We can also manually define the portion of our video that should loop within the page using the `fun setTrimOffset(block: DesignBlock, offset: Double)` and `fun setTrimLength(block: DesignBlock, length: Double)` APIs. We use the trim offset to cut away the first second of the video and the trim length to only play 10 seconds of the video.

```kotlin highlight-trim
// Make sure that the video is loaded before calling the trim APIs.
engine.block.forceLoadAVResource(videoFill)
engine.block.setTrimOffset(videoFill, offset = 1.0)
engine.block.setTrimLength(videoFill, length = 10.0)
```

We can control if a video will loop back to its beginning by calling `fun setLooping(block: DesignBlock, looping: Boolean)`. Otherwise, the video will simply hold its last frame instead and audio will stop playing. Looping behavior is activated for all blocks by default.

```kotlin highlight-looping
engine.block.setLooping(videoFill, looping = true)
```

## Audio

If the video of a video fill contains an audio track, that audio will play automatically by default when the video is playing. We can mute it by calling `fun setMuted(block: DesignBlock, muted: Boolean)`.

```kotlin highlight-mute-audio
engine.block.setMuted(videoFill, muted = true)
```

We can also add audio-only files to play together with the contents of the scene by adding an `audio` block to the scene and assigning it the uri of the audio file.

```kotlin highlight-audio
val audio = engine.block.create(DesignBlockType.Audio)
engine.block.appendChild(parent = page, child = audio)
engine.block.setString(
    block = audio,
    property = "audio/fileURI",
    value = "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
)
```

We can adjust the volume level of any audio block or video fill by calling `fun setVolume(block: DesignBlock, volume: Float)`. The volume is given as a fraction in the range of 0 to 1.

```kotlin highlight-audio-volume
// Set the volume level to 70%.
engine.block.setVolume(audio, volume = 0.7F)
```

By default, our audio block will start playing at the very beginning of the page. We can change this by specifying how many seconds into the page it should begin to play using the `fun setTimeOffset(block: DesignBlock, offset: Double)` API.

```kotlin highlight-timeOffset
// Start the audio after two seconds of playback.
engine.block.setTimeOffset(audio, offset = 2.0)
```

By default, our audio block will have a duration of 5 seconds. We can change this by specifying its duration in seconds by using the `fun setDuration(block: DesignBlock, duration: Double)` API.

```kotlin highlight-audioDuration
// Give the Audio block a duration of 7 seconds.
engine.block.setDuration(audio, duration = 7.0)
```

## Exporting Video

You can start exporting the entire page as a video file by calling `blockApi.exportVideo`. The encoding process will run in the background. You can get notified about the progress of the encoding process by using `progressCallback` parameter.

Since the encoding process runs in the background, the engine will stay interactive. So, you can continue to use the engine to manipulate the scene. Please note that these changes won't be visible in the exported video file because the scene's state has been frozen at the start of the export.

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

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.MimeType
import ly.img.engine.ShapeType

fun editVideo(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    engine.block.setWidth(page, value = 1280F)
    engine.block.setHeight(page, value = 720F)
    engine.block.setDuration(page, duration = 20.0)
    val video1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
    )
    engine.block.setFill(video1, fill = videoFill)

    val video2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill2 = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4",
    )
    engine.block.setFill(video2, fill = videoFill2)
    val track = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = track)
    engine.block.appendChild(parent = track, child = video1)
    engine.block.appendChild(parent = track, child = video2)
    engine.block.fillParent(track)
    engine.block.setDuration(video1, duration = 15.0)
    // Make sure that the video is loaded before calling the trim APIs.
    engine.block.forceLoadAVResource(videoFill)
    engine.block.setTrimOffset(videoFill, offset = 1.0)
    engine.block.setTrimLength(videoFill, length = 10.0)
    engine.block.setLooping(videoFill, looping = true)

    engine.block.setMuted(videoFill, muted = true)

    val audio = engine.block.create(DesignBlockType.Audio)
    engine.block.appendChild(parent = page, child = audio)
    engine.block.setString(
        block = audio,
        property = "audio/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
    )
    // Set the volume level to 70%.
    engine.block.setVolume(audio, volume = 0.7F)
    // Start the audio after two seconds of playback.
    engine.block.setTimeOffset(audio, offset = 2.0)
    // Give the Audio block a duration of 7 seconds.
    engine.block.setDuration(audio, duration = 7.0)
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
