# Source: https://img.ly/docs/cesdk/mac-catalyst/create-video/overview-b06512/

---
title: "Create Videos Overview"
description: "Learn how to create and customize videos in CE.SDK using scenes, assets, and timeline-based editing."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/create-video/overview-b06512/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Create and Edit Videos](https://img.ly/docs/cesdk/mac-catalyst/create-video-c41a08/) > [Overview](https://img.ly/docs/cesdk/mac-catalyst/create-video/overview-b06512/)

---

```swift file=@cesdk_swift_examples/engine-guides-video/Video.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func editVideo(engine: Engine) async throws {
  let scene = try engine.scene.createVideo()
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: scene, child: page)
  try engine.block.setWidth(page, value: 1280)
  try engine.block.setHeight(page, value: 720)

  try engine.block.setDuration(page, duration: 20)

  let video1 = try engine.block.create(.graphic)
  try engine.block.setShape(video1, shape: engine.block.createShape(.rect))
  let videoFill = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill,
    property: "fill/video/fileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
  )
  try engine.block.setFill(video1, fill: videoFill)

  let video2 = try engine.block.create(.graphic)
  try engine.block.setShape(video2, shape: engine.block.createShape(.rect))
  let videoFill2 = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill2,
    property: "fill/video/fileURI",
    value: "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4",
  )
  try engine.block.setFill(video2, fill: videoFill2)

  let track = try engine.block.create(.track)
  try engine.block.appendChild(to: page, child: track)
  try engine.block.appendChild(to: track, child: video1)
  try engine.block.appendChild(to: track, child: video2)
  try engine.block.fillParent(track)

  try engine.block.setDuration(video1, duration: 15)

  // Make sure that the video is loaded before calling the trim APIs.
  try await engine.block.forceLoadAVResource(videoFill)
  try engine.block.setTrimOffset(videoFill, offset: 1)
  try engine.block.setTrimLength(videoFill, length: 10)

  try engine.block.setLooping(videoFill, looping: true)

  try engine.block.setMuted(videoFill, muted: true)

  let audio = try engine.block.create(.audio)
  try engine.block.appendChild(to: page, child: audio)
  try engine.block.setString(
    audio,
    property: "audio/fileURI",
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
  )

  // Set the volume level to 70%.
  try engine.block.setVolume(audio, volume: 0.7)

  // Start the audio after two seconds of playback.
  try engine.block.setTimeOffset(audio, offset: 2)

  // Give the Audio block a duration of 7 seconds.
  try engine.block.setDuration(audio, duration: 7)

  // Export page as mp4 video.
  let mimeType: MIMEType = .mp4
  let exportTask = Task {
    for try await export in try await engine.block.exportVideo(page, mimeType: mimeType) {
      switch export {
      case let .progress(renderedFrames, encodedFrames, totalFrames):
        print("Rendered", renderedFrames, "frames and encoded", encodedFrames, "frames out of", totalFrames)
      case let .finished(video: videoData):
        return videoData
      }
    }
    return Blob()
  }
  let blob = try await exportTask.value
}
```

In addition to static designs, CE.SDK also allows you to create and edit videos. Working with videos introduces the concept of time into the scene, which requires you to switch the scene into the `"Video"` mode.

In this mode, each page in the scene has its own separate timeline within which its children can be placed. The `"playback/time"` property of each page controls the progress of time through the page.

In order to add videos to your pages, you can add a block with a `FillType.video` fill. As the playback time of the page progresses, the corresponding point in time of the video fill is rendered by the block.

You can also customize the video fill's trim in order to control the portion of the video that should be looped while the block is visible.

`DesignBlockType.audio` blocks can be added to the page in order to play an audio file during playback.

The `playback/timeOffset` property controls after how many seconds the audio should begin to play, while the duration property defines how long the audio should play. The same APIs can be used for other design blocks as well, such as text or graphic blocks.

Finally, the whole page can be exported as a video file using the `block.exportVideo` function.

## Creating a Video Scene

First, we create a scene that is set up for video editing by calling the `scene.createVideo()` API. Then we create a page, add it to the scene and define its dimensions. This page will hold our composition.

```swift highlight-setupScene
let scene = try engine.scene.createVideo()
let page = try engine.block.create(.page)
try engine.block.appendChild(to: scene, child: page)
try engine.block.setWidth(page, value: 1280)
try engine.block.setHeight(page, value: 720)
```

## Setting Page Durations

Next, we define the duration of the page using the `func setDuration(_ id: DesignBlockID, duration: Double) throws` API to be 20 seconds long. This will be the total duration of our exported video in the end.

```swift highlight-setPageDuration
try engine.block.setDuration(page, duration: 20)
```

## Adding Videos

In this example, we want to show two videos, one after the other. For this, we first create two graphic blocks and assign two `'video'` fills to them.

```swift highlight-assignVideoFill
  let video1 = try engine.block.create(.graphic)
  try engine.block.setShape(video1, shape: engine.block.createShape(.rect))
  let videoFill = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill,
    property: "fill/video/fileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4",
  )
  try engine.block.setFill(video1, fill: videoFill)

  let video2 = try engine.block.create(.graphic)
  try engine.block.setShape(video2, shape: engine.block.createShape(.rect))
  let videoFill2 = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill2,
    property: "fill/video/fileURI",
    value: "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4",
  )
  try engine.block.setFill(video2, fill: videoFill2)
```

## Creating a Track

While we could add the two blocks directly to the page and and manually set their sizes and time offsets, we can alternatively also use the `track` block to simplify this work. A `track` automatically adjusts the time offsets of its children to make sure that they play one after another without any gaps, based on each child's duration.

Tracks themselves cannot be selected directly by clicking on the canvas, nor do they have any visual representation.

We create a `track` block, add it to the page and add both videos in the order in which they should play as the track's children. Next, we use the `fillParent` API, which will resize all children of the track to the same dimensions as the page.

The dimensions of a `track` are always derived from the dimensions of its children, so you should not call the `setWidth` or `setHeight` APIs on a track, but on its children instead if you can't use the `fillParent` API.

```swift highlight-addToTrack
let track = try engine.block.create(.track)
try engine.block.appendChild(to: page, child: track)
try engine.block.appendChild(to: track, child: video1)
try engine.block.appendChild(to: track, child: video2)
try engine.block.fillParent(track)
```

By default, each block has a duration of 5 seconds after it is created. If we want to show it on the page for a different amount of time, we can use the `setDuration` API.

Note that we can just increase the duration of the first video block to 15 seconds without having to adjust anything about the second video. The `track` takes care of that for us automatically so that the second video starts playing after 15 seconds.

```swift highlight-setDuration
try engine.block.setDuration(video1, duration: 15)
```

If the video is longer than the duration of the graphic block that it's attached to, it will cut off once the duration of the graphic is reached. If it is too short, the video will automatically loop for as long as its graphic block is visible.

We can also manually define the portion of our video that should loop within the graphic using the `func setTrimOffset(_ id: DesignBlockID, offset: Double) throws` and `func setTrimLength(_ id: DesignBlockID, length: Double) throws` APIs. We use the trim offset to cut away the first second of the video and the trim length to only play 10 seconds of the video. Since our graphic is 15 seconds long, the trimmed video will be played fully once and then start looping for the remaining 5 seconds.

```swift highlight-trim
// Make sure that the video is loaded before calling the trim APIs.
try await engine.block.forceLoadAVResource(videoFill)
try engine.block.setTrimOffset(videoFill, offset: 1)
try engine.block.setTrimLength(videoFill, length: 10)
```

We can control if a video will loop back to its beginning by calling `func setLooping(_ id: DesignBlockID, looping: Bool) throws`. Otherwise, the video will simply hold its last frame instead and audio will stop playing. Looping behavior is activated for all blocks by default.

```swift highlight-looping
try engine.block.setLooping(videoFill, looping: true)
```

## Audio

If the video of a video fill contains an audio track, that audio will play automatically by default when the video is playing. We can mute it by calling `func setMuted(_ id: DesignBlockID, muted: Bool) throws`.

```swift highlight-mute-audio
try engine.block.setMuted(videoFill, muted: true)
```

We can also add audio-only files to play together with the contents of the page by adding an `'audio'` block to the page and assigning it the URL of the audio file.

```swift highlight-audio
let audio = try engine.block.create(.audio)
try engine.block.appendChild(to: page, child: audio)
try engine.block.setString(
  audio,
  property: "audio/fileURI",
  value: "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a",
)
```

We can adjust the volume level of any audio block or video fill by calling `func setVolume(_ id: DesignBlockID, volume: Float) throws`. The volume is given as a fraction in the range of 0 to 1.

```swift highlight-audio-volume
// Set the volume level to 70%.
try engine.block.setVolume(audio, volume: 0.7)
```

By default, our audio block will start playing at the very beginning of the page. We can change this by specifying how many seconds into the scene it should begin to play using the `func setTimeOffset(_ id: DesignBlockID, offset: Double) throws` API.

```swift highlight-timeOffset
// Start the audio after two seconds of playback.
try engine.block.setTimeOffset(audio, offset: 2)
```

By default, our audio block will have a duration of 5 seconds. We can change this by specifying its duration in seconds by using the `func setDuration(_ id: DesignBlockID, duration: Double) throws` API.

```swift highlight-audioDuration
// Give the Audio block a duration of 7 seconds.
try engine.block.setDuration(audio, duration: 7)
```

## Exporting Video

You can start exporting the entire page as a video file by calling `func exportVideo(_ id: DesignBlockID, mimeType: MIMEType)`. The encoding process will run in the background. You can get notified about the progress of the encoding process by the `async` stream that's returned.

Since the encoding process runs in the background the engine will stay interactive. So, you can continue to use the engine to manipulate the scene. Please note that these changes won't be visible in the exported video file because the scene's state has been frozen at the start of the export.

```swift highlight-exportVideo
// Export page as mp4 video.
let mimeType: MIMEType = .mp4
let exportTask = Task {
  for try await export in try await engine.block.exportVideo(page, mimeType: mimeType) {
    switch export {
    case let .progress(renderedFrames, encodedFrames, totalFrames):
      print("Rendered", renderedFrames, "frames and encoded", encodedFrames, "frames out of", totalFrames)
    case let .finished(video: videoData):
      return videoData
    }
  }
  return Blob()
}
let blob = try await exportTask.value
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func editVideo(engine: Engine) async throws {
  let scene = try engine.scene.createVideo()
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: scene, child: page)
  try engine.block.setWidth(page, value: 1280)
  try engine.block.setHeight(page, value: 720)

  try engine.block.setDuration(page, duration: 20)

  let video1 = try engine.block.create(.graphic)
  try engine.block.setShape(video1, shape: engine.block.createShape(.rect))
  let videoFill = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill,
    property: "fill/video/fileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4"
  )
  try engine.block.setFill(video1, fill: videoFill)

  let video2 = try engine.block.create(.graphic)
  try engine.block.setShape(video2, shape: engine.block.createShape(.rect))
  let videoFill2 = try engine.block.createFill(.video)
  try engine.block.setString(
    videoFill2,
    property: "fill/video/fileURI",
    value: "https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-kampus-production-8154913.mp4"
  )
  try engine.block.setFill(video2, fill: videoFill2)

  let track = try engine.block.create(.track)
  try engine.block.appendChild(to: page, child: track)
  try engine.block.appendChild(to: track, child: video1)
  try engine.block.appendChild(to: track, child: video2)
  try engine.block.fillParent(track)

  try engine.block.setDuration(video1, duration: 15)

  // Make sure that the video is loaded before calling the trim APIs.
  try await engine.block.forceLoadAVResource(videoFill)
  try engine.block.setTrimOffset(videoFill, offset: 1)
  try engine.block.setTrimLength(videoFill, length: 10)

  try engine.block.setLooping(videoFill, looping: true)

  try engine.block.setMuted(videoFill, muted: true)

  let audio = try engine.block.create(.audio)
  try engine.block.appendChild(to: page, child: audio)
  try engine.block.setString(
    audio,
    property: "audio/fileURI",
    value: "https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a"
  )

  // Set the volume level to 70%.
  try engine.block.setVolume(audio, volume: 0.7)

  // Start the audio after two seconds of playback.
  try engine.block.setTimeOffset(audio, offset: 2)

  // Give the Audio block a duration of 7 seconds.
  try engine.block.setDuration(audio, duration: 7)

  // Export page as mp4 video.
  let mimeType: MIMEType = .mp4
  let exportTask = Task {
    for try await export in try await engine.block.exportVideo(page, mimeType: mimeType) {
      switch export {
      case let .progress(renderedFrames, encodedFrames, totalFrames):
        print("Rendered", renderedFrames, "frames and encoded", encodedFrames, "frames out of", totalFrames)
      case let .finished(video: videoData):
        return videoData
      }
    }
    return Blob()
  }
  let blob = try await exportTask.value
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
