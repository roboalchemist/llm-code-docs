# Source: https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-reaction-42e4c5/

---
title: "Record Reaction"
description: "Record user’s reaction while watching a video."
platform: macos
url: "https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-reaction-42e4c5/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/macos/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera-92f388/) > [Record Reaction](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/record-reaction-42e4c5/)

---

Reaction Mode lets your users record themselves while watching a video. The
base video plays back in the preview, while the front camera and microphone
capture the user’s reaction. When recording stops, you get two assets: the
original base video and one or more reaction clips. You can then bring both
into the editor and place the reaction video as a picture-in-picture overlay
for export.

## What You’ll Learn

- How Reaction Mode differs from Standard and Dual Camera modes.
- How to launch the CE.SDK camera in Reaction Mode with a base video URL.
- How to record the user’s reaction (front camera + mic) while the base video plays.
- How to retrieve the reaction recording as a separate file.

## When to Use It

Choose Reaction Mode when you want users to capture their response to a video:

- Watch-along commentary, tutorials, or educational content
- Social media formats like reaction videos or duets
- Sports replays or event commentary where facial expressions matter
- Any scenario where the user’s reaction is the content

🚫 Not appropriate when:

- You only need a selfie-style recording → use Standard mode.
- You want to capture both front and back cameras simultaneously → use Dual Camera mode.
- You expect an auto-composited reaction + base video → Reaction Mode only records the reaction; you compose both in the editor.

### Launching the Camera

Initialize the IMGLYCamera in Reaction Mode with:

```swift
Camera(engineSettings, mode: .reaction(.vertical, video: baseURL, positionsSwapped: false)) { result in
  // Handle results here
}
```

- `video: baseURL` — the video to play back during recording
- `positionsSwapped` — swaps layout between playback and selfie preview (UI only)
- `.vertical` (or `.horizontal`) — how to lay out preview windows while recording

![Camera UI when in Reaction Mode](assets/reaction-ios-159-1.jpeg)

It’s also a good idea to lock the mode so that the user cannot switch out of reaction mode. Learn how to lock the mode in the [Camera Configuration](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/camera-configuration-46afd0/) guide.

### Retrieving the Recording

When the recording finishes, you receive a `.reaction(video: Recording, reaction: [Recording])` result with both the base and the reaction clips.

Here is a minimal code example that extracts the `URL` for each of the recordings:

```swift

Camera(engineSettings, mode: .reaction(.vertical, video: baseURL)) { result in
  switch result {
    case let .success(.reaction(video: base, reaction: reactions)):
      let baseVideoURL = base.videos.first?.url
      let reactionURL = reactions.first?.videos.first?.url
      print("Base video:", baseVideoURL as Any)
      print("Reaction video:", reactionURL as Any)

    case let .failure(error):
      print("Error:", error.localizedDescription)

    case let .success(.recording(recordings)):
      // This case is returned in Standard/Dual modes, not Reaction
      break
  }
}

```

You can learn more about the `Recording` struct in the [Access Recordings guide](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/recordings-c2ca1e/). The reaction `URL` points to the `Caches` directory on the device. Be sure to copy it somewhere if you want to save it long-term.

Here is a simple helper function to copy a file to the `Documents` directory and return the `URL` of the new file location.

```swift
func persistFile(from sourceURL: URL, fileName: String) throws -> URL {
  let docs = try FileManager.default.url(for: .documentDirectory,
                                         in: .userDomainMask,
                                         appropriateFor: nil,
                                         create: true)
  let dest = docs.appendingPathComponent(fileName)
  if FileManager.default.fileExists(atPath: dest.path) {
    try FileManager.default.removeItem(at: dest)
  }
  try FileManager.default.copyItem(at: sourceURL, to: dest)
  return dest
}
```

The video previews are cropped to fit the screen, but the `Recording` struct contains full-screen data. The reaction video starts at time 0 of the base video. If the user pauses, both the base and the reaction videos will pause to preserve the time sync.

![Captured recordings from Reaction Mode](assets/reaction-ios-159-2.png)

> **Note:** It is beyond the scope of this guide, but the `rect` of each of the previews
> is set in `CameraMode.swift` in the CE.SDK package. You can change the layout
> of the previews by changing each `rect`. Changing the `rect` values **only
> affects the live UI, not the captured recording**.

## Troubleshooting

❌ **Reaction Video is Incomplete**

When the user pauses and restarts the recording, the camera will create a new file for each segment. Process the array of recordings.

❌ **Audio Echo**

The base video’s audio may be picked up by the mic. Lower preview volume or suggest headphones.

## Next Steps

Reaction Mode is a powerful way to create engaging, social-friendly content. By combining playback and live recording, your users can produce watch-along or commentary videos with minimal setup. Continue exploring with these guides:

- Learn how to [integrate the IMGLY Camera](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/integrate-33d863/) into your project.
- [Configure](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/camera-configuration-46afd0/) the UI and other properties of the camera.
- Learn how to [retrieve and manage recordings](https://img.ly/docs/cesdk/macos/import-media/capture-from-camera/recordings-c2ca1e/).



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
