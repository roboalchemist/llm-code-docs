# Source: https://img.ly/docs/cesdk/android/import-media/capture-from-camera/recordings-c2ca1e/

---
title: "Access Recordings"
description: "Manage access to recorded videos or reactions for playback or editing."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/capture-from-camera/recordings-c2ca1e/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/android/import-media/capture-from-camera-92f388/) > [Access Recordings](https://img.ly/docs/cesdk/android/import-media/capture-from-camera/recordings-c2ca1e/)

---

```kotlin file=@cesdk_android_examples/camera-guides-recordings/RecordingsCameraActivity.kt reference-only
import android.os.Bundle
import android.util.Log
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import ly.img.camera.core.CameraResult
import ly.img.camera.core.CaptureVideo
import ly.img.camera.core.EngineConfiguration

private const val TAG = "RecordingsCameraActivity"

class RecordingsCameraActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val cameraInput = CaptureVideo.Input(
            engineConfiguration = EngineConfiguration(
                license = "<your license here>", // pass null or empty for evaluation mode with watermark
                userId = "<your unique user id>",
            ),
        )

        setContent {
            val cameraLauncher = rememberLauncherForActivityResult(contract = CaptureVideo()) { result ->
                result ?: run {
                    Log.d(TAG, "Camera dismissed")
                    return@rememberLauncherForActivityResult
                }
                when (result) {
                    is CameraResult.Record -> {
                        for (recording in result.recordings) {
                            Log.d(TAG, "Duration: ${recording.duration}")
                            for (video in recording.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }
                    is CameraResult.Reaction -> {
                        Log.d(TAG, "Video uri: ${result.video.uri}")
                        for (reaction in result.reaction) {
                            Log.d(TAG, "Duration: ${reaction.duration}")
                            for (video in reaction.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }

                    else -> {
                        Log.d(TAG, "Unhandled result")
                    }
                }
            }

            Button(
                onClick = {
                    cameraLauncher.launch(cameraInput)
                },
            ) {
                Text(text = "Open Camera")
            }
        }
    }
}
```

Learn how to get the recorded videos from the `CameraResult` type using the Activity Result APIs.

## Success

A `Recording` has a `duration` and contains a list of `Video`s. The list contains either one `Video` (for single camera recording) or two `Video`s (for dual camera recordings).

> **Note:** Dual camera is currently only available for iOS.

Each `Video` has:

- A `uri` to the video file that is stored in `Context::getFilesDir()`. Make sure to copy the file to a permanent location if you want to access it later.
- A `rect` that contains the position of the video as it was shown in the camera preview.

```kotlin highlight-success
                when (result) {
                    is CameraResult.Record -> {
                        for (recording in result.recordings) {
                            Log.d(TAG, "Duration: ${recording.duration}")
                            for (video in recording.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }
                    is CameraResult.Reaction -> {
                        Log.d(TAG, "Video uri: ${result.video.uri}")
                        for (reaction in result.reaction) {
                            Log.d(TAG, "Duration: ${reaction.duration}")
                            for (video in reaction.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }

                    else -> {
                        Log.d(TAG, "Unhandled result")
                    }
                }
```

### Standard Camera

If the user has recorded videos, the `CameraResult.Record` case will contain a list of `Recording`s, each representing a segment of the recorded video.

```kotlin highlight-standard
is CameraResult.Record -> {
    for (recording in result.recordings) {
        Log.d(TAG, "Duration: ${recording.duration}")
        for (video in recording.videos) {
            Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
        }
    }
}
```

### Video Reaction

If the user has recorded a reaction, the `CameraResult.Reaction` case will contain the video that was reacted to and a list of `Recording`s, each representing a segment of the recorded video.

```kotlin highlight-reaction
is CameraResult.Reaction -> {
    Log.d(TAG, "Video uri: ${result.video.uri}")
    for (reaction in result.reaction) {
        Log.d(TAG, "Duration: ${reaction.duration}")
        for (video in reaction.videos) {
            Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
        }
    }
}
```

## Failure

The result is `null` in case the user dismissed the camera at any point.

```kotlin highlight-failure
result ?: run {
    Log.d(TAG, "Camera dismissed")
    return@rememberLauncherForActivityResult
}
```

## Full Code

Here's the full code:

```kotlin
import android.os.Bundle
import android.util.Log
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import ly.img.camera.core.CameraResult
import ly.img.camera.core.CaptureVideo
import ly.img.camera.core.EngineConfiguration

private const val TAG = "RecordingsCameraActivity"

class RecordingsCameraActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val cameraInput = CaptureVideo.Input(
            engineConfiguration = EngineConfiguration(
                license = "<your license here>",
                userId = "<your unique user id>",
            ),
        )

        setContent {
            val cameraLauncher = rememberLauncherForActivityResult(contract = CaptureVideo()) { result ->
                result ?: run {
                    Log.d(TAG, "Camera dismissed")
                    return@rememberLauncherForActivityResult
                }
                when (result) {
                    is CameraResult.Record -> {
                        for (recording in result.recordings) {
                            Log.d(TAG, "Duration: ${recording.duration}")
                            for (video in recording.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }
                    is CameraResult.Reaction -> {
                        Log.d(TAG, "Video uri: ${result.video.uri}")
                        for (reaction in result.reaction) {
                            Log.d(TAG, "Duration: ${reaction.duration}")
                            for (video in reaction.videos) {
                                Log.d(TAG, "Video Uri: ${video.uri} Video Rect: ${video.rect}")
                            }
                        }
                    }

                    else -> {
                        Log.d(TAG, "Unhandled result")
                    }
                }
            }

            Button(
                onClick = {
                    cameraLauncher.launch(cameraInput)
                },
            ) {
                Text(text = "Open Camera")
            }
        }
    }
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
