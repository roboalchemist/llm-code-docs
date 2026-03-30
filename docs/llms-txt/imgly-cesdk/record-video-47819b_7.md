# Source: https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-video-47819b/

---
title: "Record Video"
description: "Record video directly inside the editor using a connected camera device."
platform: macos
url: "https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-video-47819b/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/macos/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera-92f388/) > [Record Video](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-video-47819b/)

---

```swift file=@cesdk_swift_examples/engine-guides-using-camera/UsingCamera.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func usingCamera(engine: Engine) async throws {
  let scene = try engine.scene.createVideo()
  let stack = try engine.block.find(byType: .stack).first!
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: stack, child: page)

  let pixelStreamFill = try engine.block.createFill(.pixelStream)
  try engine.block.setFill(page, fill: pixelStreamFill)

  try engine.block.appendEffect(page, effectID: try engine.block.createEffect(.halfTone))

  try engine.block.setEnum(
    pixelStreamFill,
    property: "fill/pixelStream/orientation",
    value: "UpMirrored",
  )

  let camera = try Camera()

  Task {
    try await engine.scene.zoom(to: page, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)
    for try await event in camera.captureVideo() {
      switch event {
      case let .frame(buffer):
        try engine.block.setNativePixelBuffer(pixelStreamFill, buffer: buffer)
      case let .videoCaptured(url):
        // Use a `VideoFill` for the recorded video file.
        let videoFill = try engine.block.createFill(.video)
        try engine.block.setFill(page, fill: videoFill)
        try engine.block.setString(
          videoFill,
          property: "fill/video/fileURI",
          value: url.absoluteString,
        )
      }
    }
  }

  // Stop capturing after 5 seconds.
  Task {
    try? await Task.sleep(nanoseconds: NSEC_PER_SEC * 5)
    camera.stopCapturing()
  }
}
```

```swift file=@cesdk_swift_examples/engine-guides-using-camera/Camera.swift reference-only
import AVFoundation
import Foundation

enum VideoCapture: @unchecked Sendable {
  case frame(CVImageBuffer)
  case videoCaptured(URL)
}

final class Camera: NSObject, @unchecked Sendable {
  private lazy var queue = DispatchQueue(label: "ly.img.camera", qos: .userInteractive)

  private var videoContinuation: AsyncThrowingStream<VideoCapture, Error>.Continuation?

  private let videoInput: AVCaptureDeviceInput
  private let audioInput: AVCaptureDeviceInput

  private var captureSession: AVCaptureSession!
  private var movieOutput: AVCaptureMovieFileOutput

  init(
    videoDevice: AVCaptureDevice = .default(for: .video)!,
    audioDevice: AVCaptureDevice = .default(for: .audio)!
  ) throws {
    videoInput = try AVCaptureDeviceInput(device: videoDevice)
    audioInput = try AVCaptureDeviceInput(device: audioDevice)
    movieOutput = AVCaptureMovieFileOutput()
  }

  func captureVideo(toURL fileURL: URL = .init(fileURLWithPath: NSTemporaryDirectory() + UUID().uuidString + ".mp4"))
    -> AsyncThrowingStream<VideoCapture, Error> {
    .init { continuation in
      videoContinuation = continuation

      captureSession = AVCaptureSession()
      captureSession.addInput(videoInput)
      captureSession.addInput(audioInput)

      let videoOutput = AVCaptureVideoDataOutput()
      videoOutput.videoSettings = [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA]
      videoOutput.setSampleBufferDelegate(self, queue: queue)

      captureSession.addOutput(videoOutput)

      captureSession.addOutput(movieOutput)

      queue.async {
        self.captureSession.startRunning()
        self.movieOutput.startRecording(to: fileURL, recordingDelegate: self)
      }

      continuation.onTermination = { _ in
        self.queue.async {
          self.movieOutput.stopRecording()
          self.captureSession.stopRunning()
        }
      }
    }
  }

  func stopCapturing() {
    queue.async {
      self.movieOutput.stopRecording()
      self.captureSession?.stopRunning()
    }
  }
}

extension Camera: AVCaptureVideoDataOutputSampleBufferDelegate {
  func captureOutput(
    _: AVCaptureOutput,
    didOutput sampleBuffer: CMSampleBuffer,
    from _: AVCaptureConnection,
  ) {
    guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
    videoContinuation?.yield(.frame(pixelBuffer))
  }
}

extension Camera: AVCaptureFileOutputRecordingDelegate {
  func fileOutput(
    _: AVCaptureFileOutput,
    didStartRecordingTo _: URL,
    from _: [AVCaptureConnection],
  ) {}
  func fileOutput(
    _: AVCaptureFileOutput,
    didFinishRecordingTo url: URL,
    from _: [AVCaptureConnection],
    error: Error?,
  ) {
    if let error {
      videoContinuation?.finish(throwing: error)
    } else {
      videoContinuation?.yield(.videoCaptured(url))
      videoContinuation?.finish()
    }
  }
}
```

Other than having pre-recorded [video](https://img.ly/docs/cesdk/macos/create-video-c41a08/) in your scene you can also have a live preview from a camera in the engine. This allows you to make full use of the engine's capabilities such as [effects](https://img.ly/docs/cesdk/macos/filters-and-effects-6f88ac/), [strokes](https://img.ly/docs/cesdk/macos/outlines/strokes-c2e621/) and [drop shadows](https://img.ly/docs/cesdk/macos/outlines/shadows-and-glows-6610fa/), while the preview integrates with the composition of your scene. Simply swap out the `VideoFill` of a block with a `PixelStreamFill`. This guide shows you how the `PixelStreamFill` can be used in combination with a camera.

We create a video scene with a single page. Then we create a `PixelStreamFill` and assign it to the page. To demonstrate the live preview capabilities of the engine we also apply an effect to the page.

```swift highlight-setup
  let scene = try engine.scene.createVideo()
  let stack = try engine.block.find(byType: .stack).first!
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: stack, child: page)

  let pixelStreamFill = try engine.block.createFill(.pixelStream)
  try engine.block.setFill(page, fill: pixelStreamFill)

  try engine.block.appendEffect(page, effectID: try engine.block.createEffect(.halfTone))
```

## Orientation

To not waste expensive compute time by transforming the pixel data of the buffer itself, it's often beneficial to apply a transformation during rendering and let the GPU handle this work much more efficiently. For this purpose the `PixelStreamFill` has an `orientation` property. You can use it to mirror the image or rotate it in 90° steps.
This property lets you easily mirror an image from a front facing camera or rotate the image by 90° when the user holds a device sideways.

```swift highlight-orientation
try engine.block.setEnum(
  pixelStreamFill,
  property: "fill/pixelStream/orientation",
  value: "UpMirrored",
)
```

## Camera

We use the `Camera` helper class that internally creates an `AVCaptureSession` and connects it with audio/video inputs and frame and file outputs.
We bring the page fully into view using `engine.scene.zoom`.
By calling `camera.captureVideo()` we simultaneously start the frame output and file recording. We can then switch on the `.frame` event and the `.videoCaptured` event. Once the recording is finished we swap the `PixelStreamFill` with a `VideoFill` to play back the recorded video file.

```swift highlight-camera
  let camera = try Camera()

  Task {
    try await engine.scene.zoom(to: page, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)
    for try await event in camera.captureVideo() {
```

## Updating the Fill

In the `.frame` event we update the `PixelStreamFill` with the pixel buffer of the new video frame using `setNativePixelBuffer`. `setNativePixelBuffer` accepts a `CVPixelBuffer`.

```swift highlight-setNativePixelBuffer
case let .frame(buffer):
  try engine.block.setNativePixelBuffer(pixelStreamFill, buffer: buffer)
```

## Full Code

Here's the full code for both files.

### UsingCamera.swift

```swift
import Foundation
import IMGLYEngine

@MainActor
func usingCamera(engine: Engine) async throws {
  let scene = try engine.scene.createVideo()
  let stack = try engine.block.find(byType: .stack).first!
  let page = try engine.block.create(.page)
  try engine.block.appendChild(to: stack, child: page)

  let pixelStreamFill = try engine.block.createFill(.pixelStream)
  try engine.block.setFill(page, fill: pixelStreamFill)

  try engine.block.appendEffect(page, effectID: try engine.block.createEffect(.halfTone))

  try engine.block.setEnum(
    pixelStreamFill,
    property: "fill/pixelStream/orientation",
    value: "UpMirrored"
  )

  let camera = try Camera()

  Task {
    try await engine.scene.zoom(to: page, paddingLeft: 40, paddingTop: 40, paddingRight: 40, paddingBottom: 40)
    for try await event in camera.captureVideo() {
      switch event {
      case let .frame(buffer):
        try engine.block.setNativePixelBuffer(pixelStreamFill, buffer: buffer)
      case let .videoCaptured(url):
        // Use a `VideoFill` for the recorded video file.
        let videoFill = try engine.block.createFill(.video)
        try engine.block.setFill(page, fill: videoFill)
        try engine.block.setString(
          videoFill,
          property: "fill/video/fileURI",
          value: url.absoluteString
        )
      }
    }
  }

  // Stop capturing after 5 seconds.
  Task {
    try? await Task.sleep(nanoseconds: NSEC_PER_SEC * 5)
    camera.stopCapturing()
  }
}
```

### Camera.swift

```swift
import AVFoundation
import Foundation

@frozen
enum VideoCapture {
  case frame(CVImageBuffer)
  case videoCaptured(URL)
}

final class Camera: NSObject {
  private lazy var queue = DispatchQueue(label: "ly.img.camera", qos: .userInteractive)

  private var videoContinuation: AsyncThrowingStream<VideoCapture, Error>.Continuation?

  private let videoInput: AVCaptureDeviceInput
  private let audioInput: AVCaptureDeviceInput

  private var captureSession: AVCaptureSession!
  private var movieOutput: AVCaptureMovieFileOutput

  init(
    videoDevice: AVCaptureDevice = .default(for: .video)!,
    audioDevice: AVCaptureDevice = .default(for: .audio)!
  ) throws {
    videoInput = try AVCaptureDeviceInput(device: videoDevice)
    audioInput = try AVCaptureDeviceInput(device: audioDevice)
    movieOutput = AVCaptureMovieFileOutput()
  }

  func captureVideo(toURL fileURL: URL = .init(fileURLWithPath: NSTemporaryDirectory() + UUID().uuidString + ".mp4"))
    -> AsyncThrowingStream<VideoCapture, Error> {
    .init { continuation in
      videoContinuation = continuation

      captureSession = AVCaptureSession()
      captureSession.addInput(videoInput)
      captureSession.addInput(audioInput)

      let videoOutput = AVCaptureVideoDataOutput()
      videoOutput.videoSettings = [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA]
      videoOutput.setSampleBufferDelegate(self, queue: queue)

      captureSession.addOutput(videoOutput)

      captureSession.addOutput(movieOutput)

      queue.async {
        self.captureSession.startRunning()
        self.movieOutput.startRecording(to: fileURL, recordingDelegate: self)
      }

      continuation.onTermination = { _ in
        self.queue.async {
          self.movieOutput.stopRecording()
          self.captureSession.stopRunning()
        }
      }
    }
  }

  func stopCapturing() {
    queue.async {
      self.movieOutput.stopRecording()
      self.captureSession?.stopRunning()
    }
  }
}

extension Camera: AVCaptureVideoDataOutputSampleBufferDelegate {
  func captureOutput(
    _: AVCaptureOutput,
    didOutput sampleBuffer: CMSampleBuffer,
    from _: AVCaptureConnection
  ) {
    guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
    videoContinuation?.yield(.frame(pixelBuffer))
  }
}

extension Camera: AVCaptureFileOutputRecordingDelegate {
  func fileOutput(
    _: AVCaptureFileOutput,
    didStartRecordingTo _: URL,
    from _: [AVCaptureConnection]
  ) {}
  func fileOutput(
    _: AVCaptureFileOutput,
    didFinishRecordingTo url: URL,
    from _: [AVCaptureConnection],
    error: Error?
  ) {
    if let error {
      videoContinuation?.finish(throwing: error)
    } else {
      videoContinuation?.yield(.videoCaptured(url))
      videoContinuation?.finish()
    }
  }
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
