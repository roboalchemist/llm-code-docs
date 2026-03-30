# Source: https://img.ly/docs/cesdk/mac-catalyst/create-video/control-daba54/

---
title: "Control Audio and Video"
description: "Learn how to configure and control audio and video through offset, trim, playback, and resource control."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/create-video/control-daba54/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/mac-catalyst/create-video-c41a08/) > [Control Audio and Video](https://img.ly/docs/cesdk/mac-catalyst/create-video/control-daba54/)

---

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to configure and control audio and video through the `block` API.

## Time Offset and Duration

The time offset determines when a block becomes active during playback on the page's timeline, and the duration decides how long this block is active.
Blocks within tracks are a special case in that they have an implicitly calculated time offset that is determined by their order and the total duration of their preceding blocks in the same track.
As with any audio/video-related property, not every block supports these properties. Use `hasTimeOffset` and `hasDuration` to check.

```swift
public func supportsTimeOffset(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block has a time offset property.

- `id:`: The block to query.
- Returns: `true`, if the block has a time offset property.

```swift
public func setTimeOffset(_ id: DesignBlockID, offset: Double) throws
```

Set the time offset of the given block relative to its parent.
The time offset controls when the block is first active in the timeline.

- Note: The time offset is not supported by the page block.
- `id`: The block whose time offset should be changed.
- `offset`: The new time offset in seconds.

```swift
public func getTimeOffset(_ id: DesignBlockID) throws -> Double
```

Get the time offset of the given block relative to its parent.

- `id:`: The block whose time offset should be queried.
- Returns: The time offset of the block.

```swift
public func supportsDuration(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block has a duration property.

- Note: This also adjusts the trim for non looping blocks.
- `id:`: The block to query.
- Returns: `true` if the block has a duration property.

```swift
public func setDuration(_ id: DesignBlockID, duration: Double) throws
```

Set the playback duration of the given block in seconds.
The duration defines for how long the block is active in the scene during playback.
If a duration is set on the page block, it becomes the duration source block.

- Note: The duration is ignored when the scene is not in "Video" mode.
- Note: This also adjusts the trim for non looping blocks.
- `id`: The block whose duration should be changed.
- `duration`: The new duration in seconds.

```swift
public func getDuration(_ id: DesignBlockID) throws -> Double
```

Get the playback duration of the given block in seconds.
The duration defines for how long the block is active in the scene during playback.
Note: The duration is ignored when the scene is not in `Video` mode.

- `id:`: The block whose duration should be returned.
- Returns: The block's duration.

```swift
public func supportsPageDurationSource(_ page: DesignBlockID, id: DesignBlockID) throws -> Bool
```

Returns whether the block can be marked as the element that defines the duration of the given page.

- `id:`: The block to query.
- Returns: `true`, if the block has a time offset property.

```swift
public func setPageDurationSource(_ page: DesignBlockID, id: DesignBlockID) throws
```

Set an block as duration source so that the overall page duration is automatically determined by this.
If no defining block is set, the page duration is calculated over all children.
Only one block per page can be marked as duration source. Will automatically unmark the previously marked.
Note: This is only supported for blocks that have a duration.

- `page:`: The page block for which it should be enabled.
- `id:`: The block which should be marked as duration source.

```swift
public func isPageDurationSource(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block is a duration source block.

- `id:`: The block whose duration source property should be queried.
- Returns: `true`, if the block is a duration source block.

```swift
public func removePageDurationSource(_ id: DesignBlockID) throws
```

Remove the block as duration source block for the page.
If a scene or page is given as block, it is deactivated for all blocks in the scene or page.

- `id:`: The block whose duration source property should be removed.

```swift
public func setNativePixelBuffer(_ id: DesignBlockID, buffer: CVPixelBuffer) throws
```

Update the pixels of the given pixel stream fill block.

- `id`: The pixel stream fill block.
- `buffer`: The buffer to copy the pixel data from.

## Trim

You can select a specific range of footage from your audio/video resource by providing a trim offset and a trim length. The footage will loop if the trim's length is shorter than the block's duration. This behavior can also be disabled using the `setLooping` function.

```swift
public func supportsTrim(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block has trim properties.

- `id:`: The block to query.
- Returns: `true`, if the block has trim properties.

```swift
public func setTrimOffset(_ id: DesignBlockID, offset: Double) throws
```

Set the trim offset of the given block or fill.
Sets the time in seconds within the fill at which playback of the audio or video clip should begin.

- Note: This requires the video or audio clip to be loaded.
- `id`: The block whose trim should be updated.
- `offset`: The new trim offset, measured in timeline seconds (scaled by playback rate).

```swift
public func getTrimOffset(_ id: DesignBlockID) throws -> Double
```

Get the trim offset of this block.

- Note: This requires the video or audio clip to be loaded.
- `id:`: The block whose trim offset should be queried.
- Returns: The trim offset in timeline seconds.

```swift
public func setTrimLength(_ id: DesignBlockID, length: Double) throws
```

Set the trim length of the given block or fill.
The trim length is the duration of the audio or video clip that should be used for playback.

- Note: After reaching this value during playback, the trim region will loop.
- Note: This requires the video or audio clip to be loaded.
- `id`: The object whose trim length should be updated.
- `length`: The new trim length, measured in timeline seconds (scaled by playback rate).

```swift
public func getTrimLength(_ id: DesignBlockID) throws -> Double
```

Get the trim length of the given block or fill.

- `id:`: The object whose trim length should be queried.
- Returns: The trim length of the object measured in timeline seconds (scaled by playback rate).

## Playback Control

You can start and pause playback and seek to a certain point on the scene's timeline. There's also a solo playback mode to preview audio and video blocks individually while the rest of the scene stays frozen. Finally, you can enable or disable the looping behavior of blocks and control their audio volume.

```swift
public func setPlaying(_ id: DesignBlockID, enabled: Bool) throws
```

Set whether the block should be during active playback.

- `id`: The block that should be updated.
- `enabled`: Whether the block should be playing its contents.

```swift
public func isPlaying(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block is currently during active playback.

- `id:`: The block to query.
- Returns: Whether the block is during playback.

```swift
public func setSoloPlaybackEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Set whether the given block or fill should play its contents while the rest of the scene remains paused.

- Note: Setting this to true for one block will automatically set it to false on all other blocks.
- `id`: The block or fill to update.
- `enabled`: Whether the block's playback should progress as time moves on.

```swift
public func isSoloPlaybackEnabled(_ id: DesignBlockID) throws -> Bool
```

Return whether the given block or fill is currently set to play its contents while the rest of the scene remains
paused.

- `id:`: The block or fill to query.
- Returns: Whether solo playback is enabled for this block.

```swift
public func supportsPlaybackTime(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block has a playback time property.

- `id:`: The block to query.
- Returns: Whether the block has a playback time property.

```swift
public func setPlaybackTime(_ id: DesignBlockID, time: Double) throws
```

Set the playback time of the given block.

- `id`: The block whose playback time should be updated.
- `time`: The new playback time of the block in seconds.

```swift
public func getPlaybackTime(_ id: DesignBlockID) throws -> Double
```

Get the playback time of the given block.

- `id:`: The block to query.
- Returns: The playback time of the block in seconds.

```swift
public func isVisibleAtCurrentPlaybackTime(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block is visible on the canvas at the current playback time.

- `id:`: The block to query.
- Returns: The visibility state.

```swift
public func supportsPlaybackControl(_ id: DesignBlockID) throws -> Bool
```

Returns whether the block supports a playback control.

- `id:`: The block to query.
- Returns: Whether the block has playback control.

```swift
public func setLooping(_ id: DesignBlockID, looping: Bool) throws
```

Set whether the block should start from the beginning again or stop.

- `id`: The block or video fill to update.
- `looping`: Whether the block should loop to the beginning or stop.

```swift
public func isLooping(_ id: DesignBlockID) throws -> Bool
```

Query whether the block is looping.

- `id:`: The block to query.
- Returns: Whether the block is looping.

```swift
public func setMuted(_ id: DesignBlockID, muted: Bool) throws
```

Set whether the audio of the block is muted.

- `id`: The block or video fill to update.
- `muted`: Whether the audio should be muted.

```swift
public func isMuted(_ id: DesignBlockID) throws -> Bool
```

Query whether the block is muted.

- `id:`: The block to query.
- Returns: The volume with a range of `0, 1`.

```swift
public func setVolume(_ id: DesignBlockID, volume: Float) throws
```

Set the audio volume of the given block.

- `id`: The block or video fill to update.
- `volume`: The desired volume with a range of `0, 1`.

```swift
public func getVolume(_ id: DesignBlockID) throws -> Float
```

Get the audio volume of the given block.

- `id:`: The block to query.
- Returns: The volume with a range of `0, 1`.

```swift
public func getVideoWidth(_ id: DesignBlockID) throws -> Int
```

Get the video width in pixels of the video resource that is attached to the given block.

- `block:`: The video fill.
- Returns: The video width in pixels.

```swift
public func getVideoHeight(_ id: DesignBlockID) throws -> Int
```

Get the video height in pixels of the video resource that is attached to the given block.

- `block:`: The video fill.
- Returns: The video height in pixels.

## Playback Speed

You can control the playback speed of audio and video blocks to create slow-motion or fast-forward effects. The playback speed is a multiplier that affects how quickly the content plays back. Audio blocks accept values from 0.25x (quarter speed) to 3.0x (triple speed). Video fills can be pushed beyond 3.0x when you need extreme fast-forward playback.

Note that changing the playback speed automatically adjusts both the trim and duration of the block to maintain the same visual timeline length.

```swift
public func setPlaybackSpeed(_ id: DesignBlockID, speed: Float) throws
```

Set the playback speed of the given block.

- Note: This also adjusts the trim and duration of the block. Video fills running faster than 3.0x are force muted until their speed is reduced to 3.0x or below.
- `id`: The block or video fill to update.
- `speed`: The desired playback speed multiplier. Valid range is \[0.25, 3.0] for audio blocks and \[0.25, ∞) for video fills.

```swift
public func getPlaybackSpeed(_ id: DesignBlockID) throws -> Float
```

Get the playback speed of the given block.

- `id`: The block to query.
- Returns: The playback speed multiplier.

## Resource Control

Until an audio/video resource referenced by a block is loaded, properties like the duration of the resource aren't available, and accessing those will lead to an error. You can avoid this by forcing the resource you want to access to load using `forceLoadAVResource`.

```swift
public func forceLoadAVResource(_ id: DesignBlockID) async throws
```

Begins loading the required audio and video resource for the given video fill or audio block.
If the resource had been loaded earlier and resulted in an error, it will be reloaded.

- `id:`: The video fill or audio block whose resource should be loaded.

```swift
public func unstable_isAVResourceLoaded(_ id: DesignBlockID) throws -> Bool
```

Returns whether the audio and video resource for the given video fill or audio block is loaded.

- `id:`: The video fill or audio block.
- Returns: Whether the resource is loaded.

```swift
public func getAVResourceTotalDuration(_ id: DesignBlockID) throws -> Double
```

Get the duration in seconds of the video or audio resource that is attached to the given block.

- `id:`: The video fill or audio block.
- Returns: The video or audio file duration.

## Thumbnail Previews

For a user interface, it can be helpful to have image previews in the form of thumbnails for any given video resource. For videos, the engine can provide one or more frames using `generateVideoThumbnailSequence`. Pass the video fill that references the video resource. In addition to video thumbnails, the engine can also render compositions of design blocks over time. To do this pass in the respective design block. The video editor uses these to visually represent blocks in the timeline.

In order to visualize audio signals `generateAudioThumbnailSequence` can be used. This generates a sequence of values in the range of 0 to 1 that represent the loudness of the signal. These values can be used to render a waveform pattern in any custom style.

Note: There can be at most one thumbnail generation request per block at any given time. If you don't want to wait for the request to finish before issuing a new request, you can cancel the task.

```swift
public func generateVideoThumbnailSequence(_ id: DesignBlockID, thumbnailHeight: Int, timeRange: ClosedRange<Double>, numberOfFrames: Int) -> AsyncThrowingStream<VideoThumbnail, Error>
```

Generate a thumbnail sequence for the given video fill or design block.

- Note: There can only be one thumbnail generation request in progress for a given block.
- Note: During playback, the thumbnail generation will be paused.
- `id`: A video fill or a design block.
- `thumbnailHeight`: The height of a thumbnail. The width will be calculated from the video aspect ratio.
- `timeRange`: The time range of the generated thumbnails relative to the time offset of the design block.
- `numberOfFrames`: The number of thumbnails to generate within the given time range.
- Returns: A stream of VideoThumbnail objects.

```swift
public func generateAudioThumbnailSequence(_ id: DesignBlockID, samplesPerChunk: Int, timeRange: ClosedRange<Double>, numberOfSamples: Int, numberOfChannels: Int) -> AsyncThrowingStream<AudioThumbnail, Error>
```

Generate a thumbnail sequence for the given audio block or video fill.
A thumbnail in this case is a chunk of samples in the range of 0 to 1.
In case stereo data is requested, the samples are interleaved, starting with the left channel.

- Note: During playback, the thumbnail generation will be paused.
- `id`: The audio block or video fill.
- `samplesPerChunk`: The number of samples per chunk.
- `timeRange`: The time range of the generated thumbnails.
- `numberOfSamples`: The total number of samples to generate.
- `numberOfChannels`: The number of channels in the output. 1 for mono, 2 for stereo.
- Returns: A stream of AudioThumbnail objects.

## Full Code

Here's the full code:

```swift file=@cesdk_swift_examples/engine-guides-control-av/ControlAudioVideo.swift
import Foundation
import IMGLYEngine

// swiftlint:disable for_where

@MainActor
func controlAudioVideo(engine: Engine) async throws {
  // Setup a minimal video scene
  let scene = try engine.scene.createVideo()
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: scene, child: page)
  try engine.block.setWidth(page, value: 1280)
  try engine.block.setHeight(page, value: 720)

  // Create a video block and track
  let videoBlock = try engine.block.create(.graphic)
  try engine.block.setShape(videoBlock, shape: try engine.block.createShape(.rect))
  let videoFill = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill,
    property: "fill/video/fileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
  )
  try engine.block.setFill(videoBlock, fill: videoFill)
  let track = try engine.block.create(.track)
  try engine.block.appendChild(to: page, child: track)
  try engine.block.appendChild(to: track, child: videoBlock)
  try engine.block.fillParent(track)

  // Create an audio block
  let audio = try engine.block.create(.audio)
  try engine.block.appendChild(to: page, child: audio)
  try engine.block.setString(
    audio,
    property: "audio/fileURI",
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
  )

  // Time Offset and Duration
  try engine.block.supportsTimeOffset(audio)
  try engine.block.setTimeOffset(audio, offset: 2)
  try engine.block.getTimeOffset(audio) /* Returns 2 */

  try engine.block.supportsDuration(page)
  try engine.block.setDuration(page, duration: 10)
  try engine.block.getDuration(page) /* Returns 10 */

  // Duration of the page can be that of a block
  try engine.block.supportsPageDurationSource(page, id: videoBlock)
  try engine.block.setPageDurationSource(page, id: videoBlock)
  try engine.block.isPageDurationSource(videoBlock)
  try engine.block.getDuration(page) /* Returns duration plus offset of the block */

  // Duration of the page can be the maximum end time of all page child blocks
  try engine.block.removePageDurationSource(page)
  try engine.block.getDuration(page) /* Returns the maximum end time of all page child blocks */

  // Trim
  try engine.block.supportsTrim(videoFill)
  try engine.block.setTrimOffset(videoFill, offset: 1)
  try engine.block.getTrimOffset(videoFill) /* Returns 1 */
  try engine.block.setTrimLength(videoFill, length: 5)
  try engine.block.getTrimLength(videoFill) /* Returns 5 */

  // Playback Control
  try engine.block.setPlaying(page, enabled: true)
  try engine.block.isPlaying(page)

  try engine.block.setSoloPlaybackEnabled(videoFill, enabled: true)
  try engine.block.isSoloPlaybackEnabled(videoFill)

  try engine.block.supportsPlaybackTime(page)
  try engine.block.setPlaybackTime(page, time: 1)
  try engine.block.getPlaybackTime(page)
  try engine.block.isVisibleAtCurrentPlaybackTime(videoBlock)

  try engine.block.supportsPlaybackControl(videoFill)
  try engine.block.setLooping(videoFill, looping: true)
  try engine.block.isLooping(videoFill)
  try engine.block.setMuted(videoFill, muted: true)
  try engine.block.isMuted(videoFill)
  try engine.block.setVolume(videoFill, volume: 0.5) /* 50% volume */
  try engine.block.getVolume(videoFill)

  // Playback Speed
  try engine.block.setPlaybackSpeed(videoFill, speed: 0.5) /* Half speed */
  let currentSpeed = try engine.block.getPlaybackSpeed(videoFill) /* 0.5 */
  try engine.block.setPlaybackSpeed(videoFill, speed: 2.0) /* Double speed */
  try engine.block.setPlaybackSpeed(videoFill, speed: 1.0) /* Normal speed */

  // Resource Control
  try await engine.block.forceLoadAVResource(videoFill)
  try engine.block.unstable_isAVResourceLoaded(videoFill)
  try engine.block.getAVResourceTotalDuration(videoFill)
  try engine.block.getVideoWidth(videoFill)
  try engine.block.getVideoHeight(videoFill)

  // Thumbnail Previews
  let videoThumbnailTask = Task {
    for try await thumbnail in engine.block.generateVideoThumbnailSequence(
      videoFill, /* video fill or page */
      thumbnailHeight: 128, /* width will be calculated from aspect ratio */
      timeRange: 0.5 ... 9.5, /* inclusive time range in seconds */
      numberOfFrames: 10, /* number of thumbnails to generate */
    ) {
      if Task.isCancelled { break }

      // Use the thumbnail...
    }
  }
  let audioThumbnailTask = Task {
    for try await thumbnail in engine.block.generateAudioThumbnailSequence(
      audio,
      samplesPerChunk: 20,
      timeRange: 0.5 ... 9.5,
      numberOfSamples: 10 * 20,
      numberOfChannels: 2,
    ) {
      if Task.isCancelled { break }

      // Draw wave pattern...
    }
  }

  // Piping a native camera stream into the engine
  var pixelBuffer: CVPixelBuffer?
  CVPixelBufferCreate(kCFAllocatorDefault, 600, 400, kCVPixelFormatType_32BGRA, nil, &pixelBuffer)

  let pixelStreamFill = try engine.block.createFill(.pixelStream)
  try engine.block.setNativePixelBuffer(pixelStreamFill, buffer: pixelBuffer!)
  _ = videoThumbnailTask
  _ = audioThumbnailTask
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
