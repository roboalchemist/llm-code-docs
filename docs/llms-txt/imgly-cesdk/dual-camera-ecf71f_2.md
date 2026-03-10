# Source: https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/dual-camera-ecf71f/

---
title: "Dual Camera"
description: "Record with the front and back cameras at the same time."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/dual-camera-ecf71f/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/mac-catalyst/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera-92f388/) > [Dual Camera](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/dual-camera-ecf71f/)

---

Dual Camera Mode lets your users record with both the front and back cameras simultaneously. This is ideal for vlogging, interviews, and live reactions where you want to capture the subject and the user’s perspective at the same time. The result is one or more recordings containing synchronized tracks from each camera that you can bring into the editor and arrange in layouts like split-screen or picture-in-picture.

## What You’ll Learn

- How Dual Camera Mode differs from Standard and Reaction modes.
- How to launch the CE.SDK camera in Dual Camera mode with a layout.
- How to record with both cameras at once.
- How to retrieve the dual-camera recordings and access their video URLs.

## When to Use It

Choose Dual Camera when you want to capture two perspectives at once:

- Interviews, conversations, or podcasts where both participants should be visible.
- Reactions during events (e.g., filming a concert while capturing the audience’s response).
- Vlogging and storytelling that show both the subject and the narrator.
- Any scenario where capturing both front and back cameras adds context.

**Not appropriate when:**

- You only need a single selfie or back-camera video → use **Standard** mode
- You want to play back a base video while recording → use **Reaction** mode
- You expect an auto-composited video (e.g., side-by-side output) — Dual Camera returns two video assets; you assemble them in the editor.

### Understanding Dual Camera Mode

![A screenshot of a dual-camera mode recording in progress.](assets/dual-camera-ios-0.jpg)

Initialize the `IMGLYCamera` in Dual Camera mode with:

```swift
Camera(engineSettings, mode: .dualCamera(.vertical)) { result in
  // Handle results here
}
```

- `.vertical` (or `.horizontal`) — defines how the preview windows are arranged during capture.
- The recording `result` returns synchronized clips for both cameras.
- When the recording finishes, you receive a .recording(\[Recording]) result containing both the front and back camera recordings.

Here is a minimal code example that extracts the URL for each recording:

```swift
Camera(engineSettings, mode: .dualCamera(.vertical)) { result in
  switch result {
    case let .success(.recording(recordings)):
      let urls = recordings.flatMap { $0.videos.map(\.url) }
      print("Recorded videos:", urls)

    case let .failure(error):
      print("Error:", error.localizedDescription)

    default:
      break
  }
}
```

You can learn more about the Recording struct in the [Access Recordings guide](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/recordings-c2ca1e/). Each returned Recording corresponds to a camera feed. The videos property contains the captured media tracks and their URLs.

> **Note:** **About flipping cameras:**![Location of the flip control in the UI](assets/ios-flip-button-161.jpeg)The two rectangles in Dual Camera mode aren’t permanently tied to the front or back camera. When the user taps the **flip camera** control, the feed shown in each rectangle is swapped, but the rectangles themselves keep their identity.This means that if the user flips during recording, the video tracks will reflect that flip — each rectangle continues recording its assigned view, regardless of which camera it’s showing at that moment.

The video previews are cropped to fit the screen, but the Recording struct contains full-screen data. All returned videos are time-synced so that they align correctly in the editor.

![Full screen images from the front and back cameras.](assets/dual-camera-ios-3.png)

> **Note:** The layout of the preview windows (side-by-side or top-and-bottom) is controlled in `CameraMode.swift` in the CE.SDK package. You can change the preview `rect` values if you want to customize the live UI.

## Troubleshooting

❌ **Only one video returned**

Be sure you’re using a device that supports simultaneous front-and-back capture. Some older iPhones only support one active camera.

❌ **Videos out of sync**

All returned recordings are time-aligned. If playback appears unsynced, check how you’re handling the array of recordings — don’t manually offset them.

❌ **Performance issues**

Capturing from two cameras at once can be demanding. Test on a range of devices and consider limiting resolution for smoother performance.

## Next Steps

Dual Camera Mode is a powerful way to capture two perspectives at once. By recording both front and back cameras together, your users can create richer, more engaging stories. Continue exploring with these guides:

- Learn how to [integrate the IMGLY Camera](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/integrate-33d863/) into your project.
- [Configure](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/camera-configuration-46afd0/) the UI and other properties of the camera.
- Learn how to [retrieve and manage](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera/recordings-c2ca1e/) recordings.



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
