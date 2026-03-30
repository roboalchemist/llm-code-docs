# Source: https://img.ly/docs/cesdk/flutter/import-media/capture-from-camera/recordings-c2ca1e/

---
title: "Access Recordings"
description: "Manage access to recorded videos or reactions for playback or editing."
platform: flutter
url: "https://img.ly/docs/cesdk/flutter/import-media/capture-from-camera/recordings-c2ca1e/"
---

> This is one page of the CE.SDK Flutter documentation. For a complete overview, see the [Flutter Documentation Index](https://img.ly/docs/cesdk/flutter.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/flutter/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/flutter/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/flutter/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/flutter/import-media/capture-from-camera-92f388/) > [Access Recordings](https://img.ly/docs/cesdk/flutter/import-media/capture-from-camera/recordings-c2ca1e/)

---

```dart file=@cesdk_flutter_examples/camera-guides-recordings/recordings_camera_solution.dart reference-only
import 'package:flutter/material.dart';
import 'package:imgly_camera/imgly_camera.dart';

class RecordingsCameraSolution extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        const settings = CameraSettings(
          license:
              "YOUR-LICENSE-KEY", // Get your license from https://img.ly/forms/free-trial, pass null for evaluation mode with watermark
        );
        try {
          final result = await IMGLYCamera.openCamera(settings);
          if (result == null) {
            print('The editor has been cancelled.');
            return;
          }
          final recordedVideos = result.recording?.recordings;
          if (recordedVideos != null) {
            for (final recording in recordedVideos) {
              print('Recording duration: ${recording.duration}');
              for (final video in recording.videos) {
                print('Video path: ${video.uri}');
                print('Video rect: ${video.rect}');
              }
            }
          }
        } catch (error) {
          print('Error occurred in the camera session: $error');
        }
      },
      child: const Text('Open Camera'),
    );
  }
}
```

```dart file=@cesdk_flutter_examples/camera-guides-recordings/recordings_reaction_camera_solution.dart reference-only
import 'package:flutter/material.dart';
import 'package:imgly_camera/imgly_camera.dart';

class RecordingsReactionCameraSolution extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        const settings = CameraSettings(
          license:
              "YOUR-LICENSE-KEY", // Get your license from https://img.ly/forms/free-trial, pass null for evaluation mode with watermark
        );
        try {
          final result = await IMGLYCamera.openCamera(
            settings,
            video: 'YOUR-VIDEO-URL',
          );
          if (result == null) {
            print('The editor has been cancelled.');
            return;
          }
          print('Reaction video duration: ${result.reaction?.video.duration}');

          // Get the reaction video data.
          final originalVideos = result.reaction?.video.videos;
          if (originalVideos != null) {
            for (final video in originalVideos) {
              print('Video path: ${video.uri}');
              print('Video rect: ${video.rect}');
            }
          }
        } catch (error) {
          print('Error occurred in the camera session: $error');
        }
      },
      child: const Text('Open Reaction Camera'),
    );
  }
}
```

Learn how to get the recorded videos from the `CameraReactionResult` and `CameraRecordingResult` type of the `openCamera` function.

Explore a full code sample on GitHub.

## Success

A `Recording` has a `duration` and contains an array of `Video`s. The array contains either one `Video` (for single camera recordings or a video that was reacted to) or two `Video`s (for dual camera recordings.)

Each `Video` has:

- A `path` to the video file that is stored in a temporary location. Make sure to copy the file to a permanent location if you want to access it later.
- A `rect` that contains the position of each video as it was shown in the camera preview. For dual camera recordings, you can use these `Rect`s to arrange the videos as they were laid out in the camera.

### Standard and Dual Camera

> **Note:** Dual camera is currently only available for iOS.

If the user has recorded videos, the `openCamera` will return a `CameraRecordingResult` which will contain an array of `Recording`s, each representing a segment of the recorded video.

```dart highlight-standard
final recordedVideos = result.recording?.recordings;
if (recordedVideos != null) {
  for (final recording in recordedVideos) {
    print('Recording duration: ${recording.duration}');
    for (final video in recording.videos) {
      print('Video path: ${video.uri}');
      print('Video rect: ${video.rect}');
    }
  }
}
```

### Video Reaction

> **Note:** Video reaction is currently only available for iOS.

If the user has recorded a reaction, the `openCamera` will return a `CameraReactionResult` which will contain the video that was reacted to and an array of `Recording`s, each representing a segment of the recorded video.

```dart highlight-camera
          print('Reaction video duration: ${result.reaction?.video.duration}');

          // Get the reaction video data.
          final originalVideos = result.reaction?.video.videos;
          if (originalVideos != null) {
            for (final video in originalVideos) {
              print('Video path: ${video.uri}');
              print('Video rect: ${video.rect}');
            }
          }
```

## Cancellation

If the user has cancelled the camera session the `openCamera` function will return `null`.

```dart highlight-cancelled
if (result == null) {
  print('The editor has been cancelled.');
  return;
}
```

## Failure

The `openCamera` function will throw if the user has not allowed accessing their camera and/or microphone or any other parsing/argument error occurred.

```dart highlight-failure
print('Error occurred in the camera session: $error');
```

## Full Code

Here's the full code for both files:

### recordings\_camera\_solution.dart

```dart file=@cesdk_flutter_examples/camera-guides-recordings/recordings_camera_solution.dart
import 'package:flutter/material.dart';
import 'package:imgly_camera/imgly_camera.dart';

class RecordingsCameraSolution extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        const settings = CameraSettings(
          license:
              "YOUR-LICENSE-KEY", // Get your license from https://img.ly/forms/free-trial, pass null for evaluation mode with watermark
        );
        try {
          final result = await IMGLYCamera.openCamera(settings);
          if (result == null) {
            print('The editor has been cancelled.');
            return;
          }
          final recordedVideos = result.recording?.recordings;
          if (recordedVideos != null) {
            for (final recording in recordedVideos) {
              print('Recording duration: ${recording.duration}');
              for (final video in recording.videos) {
                print('Video path: ${video.uri}');
                print('Video rect: ${video.rect}');
              }
            }
          }
        } catch (error) {
          print('Error occurred in the camera session: $error');
        }
      },
      child: const Text('Open Camera'),
    );
  }
}
```



---

## More Resources

- **[Flutter Documentation Index](https://img.ly/docs/cesdk/flutter.md)** - Browse all Flutter documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/flutter/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/flutter/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
