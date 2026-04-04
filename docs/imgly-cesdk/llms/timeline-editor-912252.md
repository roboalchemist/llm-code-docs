# Source: https://img.ly/docs/cesdk/android/create-video/timeline-editor-912252/

---
title: "Timeline Editor in Android (Kotlin)"
description: "Use the timeline editor to arrange and edit video clips, audio, and animations frame by frame using Kotlin."
platform: android
url: "https://img.ly/docs/cesdk/android/create-video/timeline-editor-912252/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/android/create-video-c41a08/) > [Timeline Editor](https://img.ly/docs/cesdk/android/create-video/timeline-editor-912252/)

---

Timeline editing is the heart of any professional video creation tool. With CE.SDK, you can build video editors that use a **timeline model**. Each scene contains tracks and clips that align precisely over time. Developers can build **custom headless timelines** using the `Engine` APIs to programmatically arrange, trim, and export video content.

## What You'll Learn

- How the CE.SDK timeline hierarchy works (`Scene → Page → Track → Clip`).
- How to create and organize video tracks programmatically.
- How to trim and arrange video clips in a timeline.
- How to generate thumbnails for a timeline view.
- How to connect timeline scenes to export or playback features.

## When You'll Use It

- You want to build a **custom video editing interface** that arranges clips.
- You need to **trim or rearrange** clips programmatically before export.
- You're adding **thumbnail visualization** or building a playback scrubber.
- You're automating video generation from templates or data.

## Understanding the Timeline Hierarchy

CE.SDK organizes time-based video projects into a structured hierarchy:

```text
Scene
└── Page (timeline segment)
    ├── Track (parallel layer)
    │   ├── Clip (video or audio content)
    │   ├── Clip …
```

- **Scene:** the root container of your video project.
- **Page:** a timeline segment (often a full video composition).
- **Track:** a parallel layer for clips (like separate video or audio lanes).
- **Clip:** an individual media item placed on a track.

> **Note:** By default, a new scene has dimensions of **100 × 100 units**, which is small. For realistic video compositions, explicitly set a size that matches your export or camera input:```kotlin
> import ly.img.engine.DesignBlockType
> import ly.img.engine.Engine
>
> val scene = engine.scene.createForVideo()
> val page = engine.block.create(DesignBlockType.Page)
>
> engine.block.appendChild(parent = scene, child = page)
>
> // Set page dimensions to match a 1080x1920 portrait video
> engine.block.setWidth(page, value = 1080F)
> engine.block.setHeight(page, value = 1920F)
> ```

## Creating a Timeline Programmatically

When you're building a custom UI, create a timeline structure directly through the block API.

```kotlin
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

val scene = engine.scene.createForVideo()
val page = engine.block.create(DesignBlockType.Page)

engine.block.appendChild(parent = scene, child = page)

// Always set a realistic frame size
engine.block.setWidth(page, value = 1080F)
engine.block.setHeight(page, value = 1920F)

// Create a video track
val track = engine.block.create(DesignBlockType.Track)
engine.block.appendChild(parent = page, child = track)

// Insert a video clip
val clip = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(clip, shape = engine.block.createShape(ShapeType.Rect))

val fill = engine.block.createFill(FillType.Video)
engine.block.setString(
    block = fill,
    property = "fill/video/fileURI",
    value = "https://example.com/video.mp4"
)
engine.block.setFill(clip, fill = fill)
engine.block.appendChild(parent = track, child = clip)
```

You can repeat this process for all clips and tracks, allowing for multi-layered compositions that include:

- background video
- overlays
- captions

When you append a clip to a track, CE.SDK automatically places the new clip **directly after the last clip in that track**. This gives you a continuous, gap-free sequence, so playback flows cleanly from one clip to the next without extra timing math.

If you need gaps or overlaps, either:

- Place the clips in separate tracks.
- Disable automatic offset management for the track and fully control offsets yourself.

```kotlin
import ly.img.engine.Engine

// Disable automatic offset management for this track
engine.block.setBool(
    videoTrack,
    property = "track/automaticallyManageBlockOffsets",
    value = false
)

// Manage playback/timeOffset on each clip manually
engine.block.setTimeOffset(aRoll, offset = 0.0)
engine.block.setTimeOffset(overlayClip, offset = 3.0)
```

### Multi-Track Example (Video + Overlay + Audio)

You can build layered timelines by adding tracks to the same page. Each track maintains its own sequence of clips. The following code creates two video tracks to create a picture-in-picture display with an audio track accompaniment.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

fun createMultiTrackTimeline(
    license: String,
    userId: String
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.timeline")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    // Create a video scene and page
    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    
    // Set page dimensions and duration
    engine.block.setWidth(page, value = 1080F)
    engine.block.setHeight(page, value = 1920F)
    
    // Focus the canvas on this page
    engine.scene.zoomToBlock(
        page,
        paddingLeft = 0F,
        paddingTop = 0F,
        paddingRight = 0F,
        paddingBottom = 0F
    )
    
    // A-roll primary video track
    val videoTrack = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = videoTrack)
    
    val aRoll = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(aRoll, shape = engine.block.createShape(ShapeType.Rect))
    
    val aRollFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = aRollFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4"
    )
    
    engine.block.setFill(aRoll, fill = aRollFill)
    engine.block.appendChild(parent = videoTrack, child = aRoll)
    
    // Force load to get duration
    engine.block.forceLoadAVResource(aRollFill)
    val rollDuration = engine.block.getAVResourceTotalDuration(aRollFill)
    engine.block.setDuration(aRoll, duration = rollDuration)
    
    engine.block.fillParent(videoTrack)
    
    // Overlay track (B-roll or picture-in-picture)
    val overlayTrack = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = overlayTrack)
    
    val overlayClip = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(overlayClip, shape = engine.block.createShape(ShapeType.Rect))
    
    val overlayFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = overlayFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v2/ly.img.video/videos/pexels-kampus-production-8154913.mp4"
    )
    engine.block.setFill(overlayClip, fill = overlayFill)
    
    // Position overlay visually
    engine.block.setPositionX(overlayClip, value = 400F)
    engine.block.setPositionY(overlayClip, value = 200F)
    engine.block.setWidth(overlayClip, value = 225F)
    engine.block.setHeight(overlayClip, value = 500F)
    
    engine.block.appendChild(parent = overlayTrack, child = overlayClip)
    
    engine.block.forceLoadAVResource(overlayFill)
    val duration = engine.block.getAVResourceTotalDuration(overlayFill)
    engine.block.setDuration(overlayClip, duration = duration)
    
    // Audio bed track
    val audioTrack = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = audioTrack)
    
    val audioClip = engine.block.create(DesignBlockType.Audio)
    engine.block.setString(
        block = audioClip,
        property = "audio/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a"
    )
    engine.block.appendChild(parent = audioTrack, child = audioClip)
    
    // Set duration of composition to be the same as the longer clip
    engine.block.setDuration(page, duration = maxOf(rollDuration, duration))
    
    // Start playing
    engine.block.setPlaying(page, enabled = true)
}
```

The preceding code creates a complete multi-track video timeline with A-roll, B-roll overlay, and background audio.

## Trimming and Clip Duration

The `duration` of the page block controls the length of the final composition. If you don't set a duration for clips, they truncate after a few seconds. Setting a duration for a clip that's longer than the video asset for that clip causes the asset to loop. Setting a duration for a page that's longer than the duration of its clips results in a blank screen. Use `getAVResourceTotalDuration()` on audio clips or video fills to get the duration of the underlying source media.

CE.SDK gives you fine control over:

- **trim start**
- **trim length**
- **timeline position**

Each clip can define how much of its source video to display and where it begins in the composition's timeline.

Assume `aRoll` is a `Graphic` block and `aRollFill` is its `Video` fill.

```kotlin
import ly.img.engine.Engine

// Skip the first 2 seconds of the source
engine.block.setTrimOffset(
    block = aRollFill,
    offset = 2.0
)

// Play only 5 seconds after the trim offset
engine.block.setTrimLength(
    block = aRollFill,
    length = 5.0
)
```

Use `setTimeOffset` on the clip block to move it along the track:

```kotlin
// Start this clip 10 seconds into the track
engine.block.setTimeOffset(
    block = aRoll,
    offset = 10.0
)
```

## Timeline Playback Control

You can preview playback using the **Block API** after you've placed and trimmed clips. See [Control Audio and Video](https://img.ly/docs/cesdk/android/create-video/control-daba54/) for detailed playback control.

That guide covers:

- Play, pause, and seek.
- Playback speed and looping.
- Current playback time queries.
- Synchronization across different tracks.

Here's a quick example:

```kotlin
import ly.img.engine.Engine

// Start playback
engine.block.setPlaying(page, enabled = true)

// Check if playing
val isPlaying = engine.block.isPlaying(page)

// Seek to specific time (in seconds)
engine.block.setPlaybackTime(page, time = 5.0)

// Get current playback time
val currentTime = engine.block.getPlaybackTime(page)

// Pause playback
engine.block.setPlaying(page, enabled = false)
```

## Generating Timeline Thumbnails

You can render thumbnails directly from any video clip using CE.SDK's **asynchronous** thumbnail generator. The API returns a `Flow` that emits thumbnail frames.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.flow.onEach
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun generateVideoThumbnails(
    engine: Engine,
    videoFill: Int
) = CoroutineScope(Dispatchers.Main).launch {
    engine.block.generateVideoThumbnailSequence(
        block = videoFill,
        thumbnailHeight = 128,
        timeBegin = 0.0,
        timeEnd = 10.0,
        numberOfFrames = 20
    ).onEach { thumbnail ->
        // thumbnail.frameIndex: Int
        // thumbnail.width: Int
        // thumbnail.height: Int
        // thumbnail.data: ByteBuffer (RGBA pixel data)
        
        println("Frame ${thumbnail.frameIndex}: ${thumbnail.width}x${thumbnail.height}")
        
        // Convert ByteBuffer to Bitmap if needed for display
        // val bitmap = Bitmap.createBitmap(thumbnail.width, thumbnail.height, Bitmap.Config.ARGB_8888)
        // bitmap.copyPixelsFromBuffer(thumbnail.data)
    }.collect()
}
```

Each emitted `VideoThumbnail` corresponds to a frame sample along the clip's timeline. You can display these in a `RecyclerView` or custom view to create a scrubber or timeline strip.

### Audio Waveforms

Generate **Audio waveforms** in a similar way using `generateAudioThumbnailSequence`. This function emits a `Flow` of `AudioThumbnail` structs, which contain normalized audio samples (0…1). You can use the samples to render a waveform in a custom view.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.flow.onEach
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun generateAudioWaveform(
    engine: Engine,
    audioClip: Int
) = CoroutineScope(Dispatchers.Main).launch {
    engine.block.generateAudioThumbnailSequence(
        block = audioClip,
        samplesPerChunk = 512,
        timeBegin = 0.0,
        timeEnd = 10.0,
        numberOfSamples = 8192,
        numberOfChannels = 2  // 1 = mono, 2 = stereo (interleaved L/R)
    ).onEach { audioThumbnail ->
        // audioThumbnail.chunkIndex: Int
        // audioThumbnail.samples: FloatArray (normalized 0.0 to 1.0)
        
        println("Audio chunk ${audioThumbnail.chunkIndex}: ${audioThumbnail.samples.size} samples")
        
        // Use samples to draw waveform
        // drawWaveform(audioThumbnail.samples)
    }.collect()
}
```

> **Note:** Rendering a waveform is application-specific and must be implemented using a custom Android view or Canvas drawing.

## Exporting the Timeline

To export a timeline, you export the `page` block as a video file. `exportVideo` accepts a progress callback to report export progress.

```kotlin
import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.MimeType
import java.io.File

suspend fun exportTimeline(
    engine: Engine,
    context: Context,
    page: Int
): File {
    // Get page duration
    val duration = engine.block.getDuration(page)
    
    // Export the page as MP4
    val blob = engine.block.exportVideo(
        block = page,
        timeOffset = 0.0,
        duration = duration,
        mimeType = MimeType.MP4,
        progressCallback = { progress ->
            println("Export progress: ${progress.renderedFrames}/${progress.totalFrames} frames")
            println("Encoded: ${progress.encodedFrames} frames")
        }
    )
    
    // Save to file
    val outputFile = File(context.filesDir, "export_${System.currentTimeMillis()}.mp4")
    withContext(Dispatchers.IO) {
        outputFile.outputStream().channel.use { channel ->
            channel.write(blob)
        }
    }
    
    return outputFile
}
```

CE.SDK supports standard formats (MP4, MOV, WebM, and audio-only tracks).

## Complete Timeline Example

Here's a complete example that creates a timeline, adds multiple clips, trims them, and exports:

```kotlin
import android.content.Context
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.MimeType
import ly.img.engine.ShapeType
import java.io.File

fun buildAndExportTimeline(
    context: Context,
    license: String,
    userId: String
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.timeline")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1280, height = 720)
    
    // Create scene and page
    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    engine.block.setWidth(page, value = 1280F)
    engine.block.setHeight(page, value = 720F)
    
    // Create track
    val track = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = track)
    
    // Add first video clip
    val video1 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video1, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill1 = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill1,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4"
    )
    engine.block.setFill(video1, fill = videoFill1)
    engine.block.appendChild(parent = track, child = video1)
    
    // Trim first clip: skip first 1 second, play 10 seconds
    engine.block.forceLoadAVResource(videoFill1)
    engine.block.setTrimOffset(videoFill1, offset = 1.0)
    engine.block.setTrimLength(videoFill1, length = 10.0)
    engine.block.setDuration(video1, duration = 10.0)
    
    // Add second video clip (automatically placed after first)
    val video2 = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(video2, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill2 = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill2,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v2/ly.img.video/videos/pexels-kampus-production-8154913.mp4"
    )
    engine.block.setFill(video2, fill = videoFill2)
    engine.block.appendChild(parent = track, child = video2)
    engine.block.setDuration(video2, duration = 8.0)
    
    engine.block.fillParent(track)
    
    // Set page duration (10 + 8 = 18 seconds)
    engine.block.setDuration(page, duration = 18.0)
    
    // Export the timeline
    val blob = engine.block.exportVideo(
        block = page,
        timeOffset = 0.0,
        duration = 18.0,
        mimeType = MimeType.MP4,
        progressCallback = { progress ->
            println("Rendering: ${progress.renderedFrames}/${progress.totalFrames}")
        }
    )
    
    // Save to file
    val outputFile = File(context.filesDir, "timeline_export.mp4")
    withContext(Dispatchers.IO) {
        outputFile.outputStream().channel.use { it.write(blob) }
    }
    
    println("Timeline exported to: ${outputFile.absolutePath}")
    
    engine.stop()
}
```

## Troubleshooting

| Symptom | Likely Cause | Solution |
|----------|---------------|-----------|
| Clips overlap or play out of order | Misaligned time offset values | Ensure each clip's start time is unique and sequential |
| Trim changes ignored | Trim start + duration exceed source length | Use `getAVResourceTotalDuration()` to confirm clip duration |
| Thumbnails are blank | Resource not loaded yet | Call `forceLoadAVResource()` before generating thumbnails |
| Playback stutters | Too many parallel HD tracks | Reduce simultaneous tracks or use compressed preview |
| Export fails | Page duration not set | Always set page duration using `setDuration()` |

***

## Next Steps

- Use [Control Audio and Video](https://img.ly/docs/cesdk/android/create-video/control-daba54/) to play, pause, seek, loop, and adjust volume or speed for timeline content.
- [Add Captions](https://img.ly/docs/cesdk/android/edit-video/add-captions-f67565/) to place timed text that stays in sync with video and audio.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
