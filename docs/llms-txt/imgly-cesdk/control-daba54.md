# Source: https://img.ly/docs/cesdk/android/create-video/control-daba54/

---
title: "Control Audio and Video"
description: "Learn how to configure and control audio and video through offset, trim, playback, and resource control."
platform: android
url: "https://img.ly/docs/cesdk/android/create-video/control-daba54/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/android/create-video-c41a08/) > [Control Audio and Video](https://img.ly/docs/cesdk/android/create-video/control-daba54/)

---

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to configure and control audio and video through the `block` API.

## Time Offset and Duration

The time offset determines when a block becomes active during playback on the scene's timeline, and the duration decides how long this block is active.
Page blocks are a special case in that they have an implicitly calculated time offset that is determined by their order and the total duration of their preceding pages.
As with any audio/video-related property, not every block supports these properties. Use `supportsTimeOffset` and `supportsDuration` to check.

```kotlin
fun supportsTimeOffset(block: DesignBlock): Boolean
```

Returns whether the block has a time offset property.

- `block`: the block to query.

- Returns true, if the block has a time offset property.

```kotlin
fun setTimeOffset(
    block: DesignBlock,
    offset: Double,
)
```

Set the time offset of the given block relative to its parent.

The time offset controls when the block is first active in the timeline.

Note: The time offset is not supported by the page block.

- `block`: the block whose time offset should be changed.

- `offset`: the new time offset in seconds.

```kotlin
fun getTimeOffset(block: DesignBlock): Double
```

Get the time offset of the given block relative to its parent.

- `block`: the block whose time offset should be queried.

- Returns the time offset of the block.

```kotlin
fun supportsDuration(block: DesignBlock): Boolean
```

Returns whether the block has a duration property.

- `block`: the block to query.

- Returns true if the block has a duration property.

```kotlin
fun setDuration(
    block: DesignBlock,
    duration: Double,
)
```

Set the playback duration of the given block in seconds.

The duration defines for how long the block is active in the scene during playback.

If a duration is set on the page block, it becomes the duration source block.

Note: The duration is ignored when the scene is not in "Video" mode.

Note: This also adjusts the trim for non looping blocks.

- `block`: the block whose duration should be changed.

- `duration`: the new duration in seconds.

```kotlin
fun getDuration(block: DesignBlock): Double
```

Get the playback duration of the given block in seconds.
The duration defines for how long the block is active in the scene during playback.
Note: The duration is ignored when the scene is not in `Video` mode.

- `block`: the block whose duration should be returned.

- Returns the block's duration.

```kotlin
fun supportsPageDurationSource(
    page: DesignBlock,
    block: DesignBlock,
): Boolean
```

Returns whether the block can be marked as the element that defines the duration of the given page.

- `page`: the page block for which to query for.

- `block`: the block to query.

- Returns true, if the block can be marked as the element that defines the duration of the given page.

```kotlin
fun setPageDurationSource(
    page: DesignBlock,
    block: DesignBlock,
)
```

Set an block as duration source so that the overall page duration is automatically determined by this.

If no defining block is set, the page duration is calculated over all children.

Only one block per page can be marked as duration source. Will automatically unmark the previously marked.

Note: This is only supported for blocks that have a duration.

- `page`: the page block for which it should be enabled.

- `block`: the block which should be marked as duration source.

```kotlin
fun isPageDurationSource(block: DesignBlock): Boolean
```

Returns whether the block is a duration source block.

- `block`: the block whose duration source property should be queried.

- Returns if the block is a duration source for a page.

```kotlin
fun removePageDurationSource(block: DesignBlock)
```

Remove the block as duration source block for the page.

If a scene or page given set as block, it is deactivated for all blocks in the scene or page.

- `block`: the block whose duration source property should be removed.

## Trim

You can select a specific range of footage from your audio/video resource by providing a trim offset and a trim length. The footage will loop if the trim's length is shorter than the block's duration. This behavior can also be disabled using the `setLooping` function.

```kotlin
fun supportsTrim(block: DesignBlock): Boolean
```

Returns whether the block has trim properties.

- `block`: the block to query.

- Returns true, if the block has trim properties.

```kotlin
fun setTrimOffset(
    block: DesignBlock,
    offset: Double,
)
```

Set the trim offset of the given block or fill.

Sets the time in seconds within the fill at which playback of the audio or video clip should begin.

Note: This requires the video or audio clip to be loaded.

- `block`: the block whose trim should be updated.

- `offset`: the new trim offset, measured in timeline seconds (scaled by playback rate).

```kotlin
fun getTrimOffset(block: DesignBlock): Double
```

Get the trim offset of this block.

Note: This requires the video or audio clip to be loaded.

- `block`: the block whose trim offset should be queried.

- Returns the trim offset in timeline seconds.

```kotlin
fun setTrimLength(
    block: DesignBlock,
    length: Double,
)
```

Set the trim length of the given block or fill.

The trim length is the duration of the audio or video clip that should be used for playback.

Note: After reaching this value during playback, the trim region will loop.

Note: This requires the video or audio clip to be loaded.

- `block`: the object whose trim length should be updated.

- `length`: the new trim length, measured in timeline seconds (scaled by playback rate).

```kotlin
fun getTrimLength(block: DesignBlock): Double
```

Get the trim length of the given block or fill.

- `block`: the object whose trim length should be queried.

- Returns the trim length of the object measured in timeline seconds (scaled by playback rate).

## Playback Control

You can start and pause playback and seek to a certain point on the scene's timeline. There's also a solo playback mode to preview audio and video blocks individually while the rest of the scene stays frozen. Finally, you can enable or disable the looping behavior of blocks and control their audio volume.

```kotlin
fun setPlaying(
    block: DesignBlock,
    enabled: Boolean,
)
```

Set whether the block should be during active playback.

- `block`: the block that should be updated.

- `enabled`: whether the block should be playing its contents.

```kotlin
fun isPlaying(block: DesignBlock): Boolean
```

Returns whether the block is currently during active playback.

- `block`: the block to query.

- Returns whether the block is during playback.

```kotlin
fun setSoloPlaybackEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Set whether the given block or fill should play its contents while the rest of the scene remains paused.

Note: Setting this to true for one block will automatically set it to false on all other blocks.

- `block`: the block or fill to update.

- `enabled`: whether the block's playback should progress as time moves on.

```kotlin
fun isSoloPlaybackEnabled(block: DesignBlock): Boolean
```

Return whether the given block or fill is currently set to play its contents while the rest of the scene remains paused.

- `block`: the block or fill to query.

- Returns whether solo playback is enabled for this block.

```kotlin
fun supportsPlaybackTime(block: DesignBlock): Boolean
```

Returns whether the block has a playback time property.

- `block`: the block to query.

- Returns whether the block has a playback time property.

```kotlin
fun setPlaybackTime(
    block: DesignBlock,
    time: Double,
)
```

Set the playback time of the given block.

- `block`: the block whose playback time should be updated.

- `time`: the new playback time of the block in seconds.

```kotlin
fun getPlaybackTime(block: DesignBlock): Double
```

Get the playback time of the given block.

- `block`: the block to query.

- Returns the playback time of the block in seconds.

```kotlin
fun isVisibleAtCurrentPlaybackTime(block: DesignBlock): Boolean
```

Returns whether the block should be visible on the canvas at the current playback time.

- `block`: the block to query.

- Returns the visibility state if the query succeeded.

```kotlin
fun supportsPlaybackControl(block: DesignBlock): Boolean
```

Returns whether the block supports a playback control.

- `block`: the block to query.

- Returns whether the block has playback control.

```kotlin
fun setLooping(
    block: DesignBlock,
    looping: Boolean,
)
```

Set whether the block should start from the beginning again or stop.

- `block`: the block or video fill to update.

- Returns whether the block should loop to the beginning or stop.

```kotlin
fun isLooping(block: DesignBlock): Boolean
```

Query whether the block is looping.

- `block`: the block to query.

- Returns whether the block is looping.

```kotlin
fun setMuted(
    block: DesignBlock,
    muted: Boolean,
)
```

Set whether the audio of the block is muted.

- `block`: the block or video fill to update.

- `muted`: whether the audio should be muted.

```kotlin
fun isMuted(block: DesignBlock): Boolean
```

Query whether the block is muted.

- `block`: the block to query.

- Returns whether the block is muted.

```kotlin
fun setVolume(
    block: DesignBlock,
    @FloatRange(from = 0.0, to = 1.0) volume: Float,
)
```

Set the audio volume of the given block.

- `block`: the block or video fill to update.

- `volume`: the desired volume with a range of `0, 1`.

```kotlin
@FloatRange(from = 0.0, to = 1.0)
fun getVolume(block: DesignBlock): Float
```

Get the audio volume of the given block.

- `block`: the block to query.

- Returns volume with a range of `0, 1`.

## Playback Speed

You can control the playback speed of audio and video blocks to create slow-motion or fast-forward effects. The playback speed is a multiplier that affects how quickly the content plays back. Audio blocks accept values from 0.25x (quarter speed) to 3.0x (triple speed). Video fills can exceed 3.0x whenever you need more aggressive fast-forward playback.

Note that changing the playback speed automatically adjusts both the trim and duration of the block to maintain the same visual timeline length.

```kotlin
fun setPlaybackSpeed(block: DesignBlock, speed: Float): Unit
```

Set the playback speed of the given block.

Note: This also adjusts the trim and duration of the block. Video fills running faster than 3.0x are force muted until their speed is reduced to 3.0x or below.

- `block`: the block or video fill to update.

- `speed`: The desired playback speed multiplier. Valid range is \[0.25, 3.0] for audio blocks and \[0.25, ∞) for video fills.

```kotlin
fun getPlaybackSpeed(block: DesignBlock): Float
```

Get the playback speed of the given block.

- `block`: the block to query.

- Returns the playback speed multiplier.

## Resource Control

Until an audio/video resource referenced by a block is loaded, properties like the duration of the resource aren't available, and accessing those will lead to an error. You can avoid this by forcing the resource you want to access to load using `forceLoadAVResource`.

```kotlin
suspend fun forceLoadAVResource(block: DesignBlock)
```

Begins loading the required audio and video resource for the given video fill or audio block.

If the resource had been loaded earlier and resulted in an error, it will be reloaded.

- `block`: the video fill or audio block whose resource should be loaded.

```kotlin
@UnstableEngineApi
fun isAVResourceLoaded(block: DesignBlock): Boolean
```

Returns whether the audio and video resource for the given video fill or audio block is loaded.

Note that the function is unstable and mared with `UnstableEngineApi`.

- `block`: the video fill or audio block.

- Returns whether the resource is loaded.

```kotlin
fun getAVResourceTotalDuration(block: DesignBlock): Double
```

Get the duration in seconds of the video or audio resource that is attached to the given block.

- `block`: the video fill or audio block.

- Returns the video or audio file duration.

```kotlin
fun getVideoWidth(videoFill: DesignBlock): Int
```

Get the video width in pixels of the video resource that is attached to the given block.

- `videoFill`: the video fill.

- Returns the video width in pixels.

```kotlin
fun getVideoHeight(videoFill: DesignBlock): Int
```

Get the video height in pixels of the video resource that is attached to the given block.

- `videoFill`: the video fill.

- Returns the video height in pixels.

## Thumbnail Previews

For a user interface, it can be helpful to have image previews in the form of thumbnails for any given video resource. For videos, the engine can provide one or more frames using `generateVideoThumbnailSequence`. Pass the video fill that references the video resource. In addition to video thumbnails, the engine can also render compositions of design blocks over time. To do this pass in the respective design block. The video editor uses these to visually represent blocks in the timeline.

In order to visualize audio signals `generateAudioThumbnailSequence` can be used. This generates a sequence of values in the range of 0 to 1 that represent the loudness of the signal. These values can be used to render a waveform pattern in any custom style.

Note: there can be at most one thumbnail generation request per block at any given time. If you don't want to wait for the request to finish before issuing a new request, you can cancel it by calling `cancel()` on the `Job` object returned on launching the flow.

```kotlin
fun generateVideoThumbnailSequence(
    block: DesignBlock,
    thumbnailHeight: Int,
    timeBegin: Double,
    timeEnd: Double,
    numberOfFrames: Int,
): Flow<VideoThumbnailResult>
```

Generate a thumbnail sequence for the given video fill or design block.
Note: There can only be one thumbnail generation request in progress for a given block.
Note: During playback, the thumbnail generation will be paused.

- `block`: the video fill or a design block.

- `thumbnailHeight`: the height of a thumbnail. The width will be calculated from the video aspect ratio.

- `timeBegin`: the time in seconds relative to the time offset of the design block at which the thumbnail sequence should start.

- `timeEnd`: the time in seconds relative to the time offset of the design block at which the thumbnail sequence should end.

- `numberOfFrames`: the number of frames to generate.

- Returns a flow of `VideoThumbnailResult` object which emits for every generated frame thumbnail. It emits

exactly `numberOfFrames` times.

```kotlin
fun generateAudioThumbnailSequence(
    block: DesignBlock,
    samplesPerChunk: Int,
    timeBegin: Double,
    timeEnd: Double,
    numberOfSamples: Int,
    numberOfChannels: Int,
): Flow<AudioThumbnailResult>
```

Generate a thumbnail sequence for the given audio block or video fill.

A thumbnail in this case is a chunk of samples in the range of 0 to 1.

In case stereo data is requested, the samples are interleaved, starting with the left channel.

Note: During playback, the thumbnail generation will be paused.

- `block`: the audio block or video fill.

- `samplesPerChunk`: the number of samples per chunk.

- `timeBegin`: the time in seconds at which the thumbnail sequence should start.

- `timeEnd`: the time in seconds at which the thumbnail sequence should end.

- `numberOfSamples`: the total number of samples to generate.

- `numberOfChannels`: the number of channels in the output. 1 for mono, 2 for stereo.

- Returns a flow of `AudioThumbnailResult` object which emits numberOfSamples / samplesPerChunk times.

## Full Code

Here's the full code:

```kotlin file=@cesdk_android_examples/engine-guides-control-av/ControlAudioVideo.kt
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.flow.onEach
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

suspend fun controlAudioVideo(engine: Engine) = coroutineScope {
    // Setup a minimal video scene
    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    engine.block.setWidth(page, value = 1280.0f)
    engine.block.setHeight(page, value = 720.0f)

    // Create a video block and track
    val videoBlock = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(videoBlock, shape = engine.block.createShape(ShapeType.Rect))
    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setString(
        block = videoFill,
        property = "fill/video/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
    )
    engine.block.setFill(videoBlock, fill = videoFill)
    val track = engine.block.create(DesignBlockType.Track)
    engine.block.appendChild(parent = page, child = track)
    engine.block.appendChild(parent = track, child = videoBlock)
    engine.block.fillParent(track)

    // Create an audio block
    val audio = engine.block.create(DesignBlockType.Audio)
    engine.block.appendChild(parent = page, child = audio)
    engine.block.setString(
        block = audio,
        property = "audio/fileURI",
        value = "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
    )

    // Time Offset and Duration
    engine.block.supportsTimeOffset(audio)
    engine.block.setTimeOffset(audio, offset = 2.0)
    engine.block.getTimeOffset(audio) // Returns 2

    engine.block.supportsDuration(page)
    engine.block.setDuration(page, duration = 10.0)
    engine.block.getDuration(page) // Returns 10

    // Duration of the page can be that of a block
    engine.block.supportsPageDurationSource(page, videoBlock)
    engine.block.setPageDurationSource(page, videoBlock)
    engine.block.isPageDurationSource(videoBlock)
    engine.block.getDuration(page) // Returns duration plus offset of the block

    // Duration of the page can be the maximum end time of all page child blocks
    engine.block.removePageDurationSource(page)
    engine.block.getDuration(page) // Returns the maximum end time of all page child blocks

    // Trim
    engine.block.supportsTrim(videoFill)
    engine.block.setTrimOffset(videoFill, offset = 1.0)
    engine.block.getTrimOffset(videoFill) // Returns 1
    engine.block.setTrimLength(videoFill, length = 5.0)
    engine.block.getTrimLength(videoFill) // Returns 5

    // Playback Control
    engine.block.setPlaying(page, enabled = true)
    engine.block.isPlaying(page)

    engine.block.setSoloPlaybackEnabled(videoFill, enabled = true)
    engine.block.isSoloPlaybackEnabled(videoFill)

    engine.block.supportsPlaybackTime(page)
    engine.block.setPlaybackTime(page, time = 1.0)
    engine.block.getPlaybackTime(page)
    engine.block.isVisibleAtCurrentPlaybackTime(videoBlock)

    engine.block.supportsPlaybackControl(videoFill)
    engine.block.setLooping(videoFill, looping = true)
    engine.block.isLooping(videoFill)
    engine.block.setMuted(videoFill, muted = true)
    engine.block.isMuted(videoFill)
    engine.block.setVolume(videoFill, volume = 0.5F) // 50% volume
    engine.block.getVolume(videoFill)

    // Playback Speed
    engine.block.setPlaybackSpeed(videoFill, speed = 0.5f) // Half speed
    val currentSpeed = engine.block.getPlaybackSpeed(videoFill) // 0.5
    engine.block.setPlaybackSpeed(videoFill, speed = 2.0f) // Double speed
    engine.block.setPlaybackSpeed(videoFill, speed = 1.0f) // Normal speed

    // Resource Control
    engine.block.forceLoadAVResource(videoFill)
    // Unstable engine api
    engine.block.isAVResourceLoaded(videoFill)
    engine.block.getAVResourceTotalDuration(videoFill)
    val videoWidth = engine.block.getVideoWidth(videoFill)
    val videoHeight = engine.block.getVideoHeight(videoFill)

    // Thumbnail Previews
    launch {
        engine.block.generateVideoThumbnailSequence(
            block = videoFill,
            thumbnailHeight = 128,
            timeBegin = 0.5,
            timeEnd = 9.5,
            numberOfFrames = 10,
        ).onEach {
            println("frameIndex = ${it.frameIndex}, width = ${it.width}, height = ${it.height}")
        }.collect()
    }

    launch {
        engine.block.generateAudioThumbnailSequence(
            block = audio,
            samplesPerChunk = 20,
            timeBegin = 0.5,
            timeEnd = 9.5,
            numberOfSamples = 10 * 20,
            numberOfChannels = 2,
        ).onEach {
            println("chunkIndex = ${it.chunkIndex}, samples:size = ${it.samples.size}")
            // drawWavePattern(it.samples)
        }.collect()
    }
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
