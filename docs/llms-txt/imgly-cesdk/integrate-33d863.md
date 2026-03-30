# Source: https://img.ly/docs/cesdk/android/import-media/capture-from-camera/integrate-33d863/

---
title: "Integrate Mobile Camera"
description: "Enable live camera capture in mobile apps to shoot and insert photos or video."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/capture-from-camera/integrate-33d863/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/android/import-media/capture-from-camera-92f388/) > [Integrate Mobile Camera](https://img.ly/docs/cesdk/android/import-media/capture-from-camera/integrate-33d863/)

---

In this example, we will show you how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s mobile camera in your Android app.

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/camera-guides-quickstart/).

## Adding dependency

Add IMG.LY maven repository to the list of maven urls in the `settings.gradle` file.

```
        maven {
            name "IMG.LY Artifactory"
            url "https://artifactory.img.ly/artifactory/maven"
            mavenContent {
                includeGroup("ly.img")
            }
        }
```

Add camera dependency in the `build.gradle` file of your application module.

```
    implementation "ly.img:camera:$UBQ_VERSION$"
```

## Requirements

In order to use the mobile camera, your application should meet the following requirements:

- `buildFeatures.compose` should be `true`, as the camera is written in Jetpack Compose.

```
    buildFeatures {
        compose true
    }
```

- `composeOptions.kotlinCompilerExtensionVersion` should match the kotlin version. Use the official compatibility map in [here](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).

```
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.3"
    }
```

- `compose-bom` version is `2023.05.01` or higher if your project uses Jetpack Compose dependencies. Note that using lower versions may cause crashes and issues in your own compose code, as our version will override yours. In case you are not using BOM, you can find the BOM to compose library version mapping in [here](https://developer.android.com/jetpack/compose/bom/bom-mapping).

```
    implementation(platform("androidx.compose:compose-bom:2023.05.01"))
```

- Kotlin version is 1.9.10 or higher.

- `minSdk` is 24 (Android 7) or higher.

```
        minSdk 24
```

By default, the mobile camera supports following ABIs: `arm64-v8a`, `armeabi-v7a`, `x86_64` and `x86`. If you want to filter out some of the ABIs, use `abiFilters`.

```
        ndk {
            abiFilters "arm64-v8a", "armeabi-v7a", "x86_64", "x86"
        }
```

## Usage

This example shows the basic usage of the camera using the [Activity Result APIs](https://developer.android.com/training/basics/intents/result).

In this integration example, on tapping the button, the `ActivityResultLauncher` is launched, presenting the camera `Activity`.

```kotlin
                    cameraLauncher.launch(cameraInput)
```

### Initialization

The camera input is initialized with `EngineConfiguration`. You need to provide the license key that you received from IMG.LY.
Optionally, you can provide a unique ID tied to your application's user. This helps us accurately calculate monthly active users (MAU) and it is especially useful when one person uses the app on multiple devices with a sign-in feature, ensuring they're counted once.

```kotlin
        val cameraInput = CaptureVideo.Input(
            engineConfiguration = EngineConfiguration(
                license = "<your license here>", // or null for evaluation mode with watermark
                userId = "<your unique user id>",
            ),
        )
```

### CaptureVideo ActivityResultContract

Here, we register a request to start the Camera designated by the `CaptureVideo` contract.

```kotlin
            val cameraLauncher = rememberLauncherForActivityResult(contract = CaptureVideo()) { result ->
```

### Result

The `CaptureVideo` contract's output is a `CameraResult?`. It is `null` when the camera is dismissed by the user and non-null when the user has recorded videos. `CameraResult` is a sealed interface and the result can be obtained by casting it appropriately.

```kotlin
                result ?: run {
                    Log.d(TAG, "Camera dismissed")
                    return@rememberLauncherForActivityResult
                }
                when (result) {
                    is CameraResult.Record -> {
                        val recordedVideoUris = result.recordings.flatMap { it.videos.map { it.uri } }
                        // Do something with the recorded videos
                        Log.d(TAG, "Recorded videos: $recordedVideoUris")
                    }

                    else -> {
                        Log.d(TAG, "Unhandled result")
                    }
                }
```

That is all. For more than basic configuration, check out all the available [configurations](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/).

## Full Code

Here's the full code for all 3 files.

### settings.gradle

```
pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven {
            name "IMG.LY Artifactory"
            url "https://artifactory.img.ly/artifactory/maven"
            mavenContent {
                includeGroup("ly.img")
            }
        }
    }
}

rootProject.name = "My App"
include ':app'
```

### build.gradle

```
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    namespace "ly.img.editor.showcase"
    compileSdk 35

    defaultConfig {
        applicationId "ly.img.editor.showcase"
        minSdk 24
        targetSdk 35
        versionCode 1
        versionName "1.0"
        ndk {
            abiFilters "arm64-v8a", "armeabi-v7a", "x86_64", "x86"
        }
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = '1.8'
    }

    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.3"
    }
}

dependencies {
    implementation "ly.img:camera:$UBQ_VERSION$"
    implementation(platform("androidx.compose:compose-bom:2023.05.01"))
    implementation "androidx.activity:activity-compose:1.8.2"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3"
}
```

### CameraActivity.kt

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

private const val TAG = "CameraActivity"

class CameraActivity : AppCompatActivity() {
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
                        val recordedVideoUris = result.recordings.flatMap { it.videos.map { it.uri } }
                        // Do something with the recorded videos
                        Log.d(TAG, "Recorded videos: $recordedVideoUris")
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
