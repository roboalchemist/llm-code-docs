# Source: https://img.ly/docs/cesdk/android/import-media/capture-from-camera/camera-configuration-46afd0/

---
title: "Mobile Camera Configuration"
description: "Set up camera permissions, quality, and behavior when capturing within CE.SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/capture-from-camera/camera-configuration-46afd0/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/android/import-media/capture-from-camera-92f388/) > [Camera Configuration](https://img.ly/docs/cesdk/android/import-media/capture-from-camera/camera-configuration-46afd0/)

---

```kotlin file=@cesdk_android_examples/camera-guides-configuration/ConfiguredCameraActivity.kt reference-only
import android.os.Bundle
import android.util.Log
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.ui.graphics.Color
import ly.img.camera.core.CameraConfiguration
import ly.img.camera.core.CameraMode
import ly.img.camera.core.CaptureVideo
import ly.img.camera.core.EngineConfiguration
import kotlin.time.Duration.Companion.seconds

private const val TAG = "ConfiguredCameraActivity"

class ConfiguredCameraActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val cameraInput = CaptureVideo.Input(
            engineConfiguration = EngineConfiguration(
                license = "<your license here>", // pass null or empty for evaluation mode with watermark
                userId = "<your unique user id>",
            ),
            cameraConfiguration = CameraConfiguration(
                recordingColor = Color.Blue,
                maxTotalDuration = 30.seconds,
                allowExceedingMaxDuration = false,
            ),
            cameraMode = CameraMode.Standard(),
        )

        setContent {
            val cameraLauncher = rememberLauncherForActivityResult(contract = CaptureVideo()) { result ->
                result ?: run {
                    Log.d(TAG, "Camera dismissed")
                    return@rememberLauncherForActivityResult
                }
                Log.d(TAG, "Result: $result")
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

In this example, we will show you how to configure the camera.

## EngineConfiguration

All the basic engine configuration settings are part of the `EngineConfiguration` which are required to initialize the camera.

```kotlin highlight-engine-configuration
engineConfiguration = EngineConfiguration(
    license = "<your license here>", // pass null or empty for evaluation mode with watermark
    userId = "<your unique user id>",
),
```

- `license` – the license to activate the [Engine](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) with.

```kotlin highlight-license
license = "<your license here>", // pass null or empty for evaluation mode with watermark
```

- `userID` – an optional unique ID tied to your application's user. This helps us accurately calculate monthly active users (MAU). Especially useful when one person uses the app on multiple devices with a sign-in feature, ensuring they're counted once. Providing this aids in better data accuracy. The default value is `null`.

```kotlin highlight-userId
userId = "<your unique user id>",
```

## CameraConfiguration

You can optionally pass a `CameraConfiguration` object to the `CaptureVideo.Input` constructor to customise the camera experience and behaviour.

```kotlin highlight-camera-configuration
cameraConfiguration = CameraConfiguration(
    recordingColor = Color.Blue,
    maxTotalDuration = 30.seconds,
    allowExceedingMaxDuration = false,
),
```

- `recordingColor` – the color of the record button.

```kotlin highlight-recording-color
recordingColor = Color.Blue,
```

- `maxTotalDuration` – the total duration that the camera is allowed to record.

```kotlin highlight-max-duration
maxTotalDuration = 30.seconds,
```

- `allowExceedingMaxDuration` – Set to `true` to allow exceeding the `maxTotalDuration`.

```kotlin highlight-allow-exceeding-max-duration
allowExceedingMaxDuration = false,
```

## Mode

You can optionally configure the initial mode of the camera.

### Available Modes

- `Standard`: the regular camera. This is the default.
- `Reaction(video, cameraLayoutMode, positionsSwapped)`: records with the camera while playing back a video.
  - `video` Uri of the video to react to.
  - `cameraLayoutMode` The layout mode. Available options are `Horizontal` and `Vertical`.
  - `positionsSwapped` A boolean indicating if the video and camera feed should swap positions. By default, it is false and the video being reacted to is on the top/left (depending on `cameraLayoutMode`)

```kotlin highlight-camera-mode
cameraMode = CameraMode.Standard(),
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
import androidx.compose.ui.graphics.Color
import ly.img.camera.core.CameraConfiguration
import ly.img.camera.core.CameraMode
import ly.img.camera.core.CaptureVideo
import ly.img.camera.core.EngineConfiguration
import kotlin.time.Duration.Companion.seconds

private const val TAG = "ConfiguredCameraActivity"

class ConfiguredCameraActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val cameraInput = CaptureVideo.Input(
            engineConfiguration = EngineConfiguration(
                license = "<your license here>",
                userId = "<your unique user id>",
            ),
            cameraConfiguration = CameraConfiguration(
                recordingColor = Color.Blue,
                maxTotalDuration = 30.seconds,
                allowExceedingMaxDuration = false,
            ),
            cameraMode = CameraMode.Standard(),
        )

        setContent {
            val cameraLauncher = rememberLauncherForActivityResult(contract = CaptureVideo()) { result ->
                result ?: run {
                    Log.d(TAG, "Camera dismissed")
                    return@rememberLauncherForActivityResult
                }
                Log.d(TAG, "Result: $result")
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

## Localization

The CE.SDK camera currently supports English and German languages on Android, however it provides convenient API to replace the values of existing localization keys or add support for more languages.

All the camera keys are located [here](https://github.com/imgly/cesdk-android/blob/v$UBQ_VERSION$/sources/camera-core/src/main/res/values/strings.xml) and they all follow strict naming convention to make locating keys simple and self-explanatory.
For instance, the timer off button can be found via `ly_img_camera_timer_option_off` key, or the title in the alert dialog of deleting last recording can be found via `ly_img_camera_dialog_delete_last_recording_title` key.

### Replacing existing keys

In order to replace any of the existing camera keys, find the key of the desired text, copy the key to `res/values/strings.xml` file of your app module and replace with the desired value.

### Supporting new languages

In order to add support for a language that is not supported by the CE.SDK camera, copy the content of the English localization [file](https://github.com/imgly/cesdk-android/blob/v$UBQ_VERSION$/sources/camera-core/src/main/res/values/strings.xml) to `res/values-{desired-language-code}/strings.xml` file and replace the values with desired translations.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
