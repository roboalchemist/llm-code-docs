# Source: https://img.ly/docs/cesdk/android/import-media/capture-from-camera/record-video-47819b/

---
title: "Record Video"
description: "Record video directly inside the editor using a connected camera device."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/capture-from-camera/record-video-47819b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/android/import-media/capture-from-camera-92f388/) > [Record Video](https://img.ly/docs/cesdk/android/import-media/capture-from-camera/record-video-47819b/)

---

```kotlin file=@cesdk_android_examples/engine-guides-using-camera/build.gradle reference-only
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    namespace "ly.img.editor.camera"
    compileSdk 35

    defaultConfig {
        applicationId "ly.img.editor.camera"
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
}

dependencies {
    implementation "ly.img:engine-camera:1.70.0"
    implementation "androidx.camera:camera-core:1.2.3"
    implementation "androidx.camera:camera-camera2:1.2.3"
    implementation "androidx.camera:camera-view:1.2.3"
    implementation "androidx.camera:camera-lifecycle:1.2.3"
    implementation "androidx.camera:camera-video:1.2.3"
    implementation "ly.img:engine:1.70.0"
    implementation "androidx.appcompat:appcompat:1.6.0"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3"
}
```

```kotlin file=@cesdk_android_examples/engine-guides-using-camera/UsingCamera.kt reference-only
import android.view.SurfaceView
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.CameraSelector
import androidx.camera.core.MirrorMode
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.video.FileOutputOptions
import androidx.camera.video.Quality
import androidx.camera.video.QualitySelector
import androidx.camera.video.Recorder
import androidx.camera.video.VideoCapture
import androidx.camera.video.VideoRecordEvent
import androidx.core.content.ContextCompat
import androidx.core.net.toUri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.EffectType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.camera.setCameraPreview
import java.io.File

fun usingCamera(
    activity: AppCompatActivity,
    surfaceView: SurfaceView,
    cameraProvider: ProcessCameraProvider,
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindSurfaceView(surfaceView)

    val cameraSelector = CameraSelector.Builder()
        .requireLensFacing(CameraSelector.LENS_FACING_FRONT)
        .build()
    val preview = Preview.Builder().build()
    val qualitySelector = QualitySelector.from(Quality.FHD)
    val recorder = Recorder.Builder()
        .setQualitySelector(qualitySelector)
        .build()
    val videoCapture = VideoCapture.Builder(recorder)
        .setMirrorMode(MirrorMode.MIRROR_MODE_ON_FRONT_ONLY)
        .build()

    cameraProvider.bindToLifecycle(activity, cameraSelector, preview, videoCapture)

    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    val pixelStreamFill = engine.block.createFill(FillType.PixelStream)
    engine.block.setFill(block = page, fill = pixelStreamFill)
    engine.setCameraPreview(pixelStreamFill, preview, mirrored = false)
    engine.block.appendEffect(
        block = page,
        effectBlock = engine.block.createEffect(EffectType.HalfTone),
    )

    // If camerax preview transformation info rotation is 90, this will return Left. If we passed mirrored = true, this would be LeftMirrored.
    val orientation = engine.block.getEnum(
        block = pixelStreamFill,
        property = "fill/pixelStream/orientation",
    )

    val recordingFile = File(surfaceView.context.filesDir, "temp.mp4")
    val fileOutputOptions = FileOutputOptions.Builder(recordingFile).build()
    val recording = videoCapture.output
        .prepareRecording(activity, fileOutputOptions)
        .start(ContextCompat.getMainExecutor(surfaceView.context)) {
            if (it !is VideoRecordEvent.Finalize) return@start
            val videoFill = engine.block.createFill(FillType.Video)
            engine.block.setFill(block = page, fill = videoFill)
            engine.block.setString(
                block = videoFill,
                property = "fill/video/fileURI",
                value = recordingFile.toUri().toString(),
            )
        }
    delay(5000L)
    recording.stop()
}
```

Other than having pre-recorded [video](https://img.ly/docs/cesdk/android/create-video-c41a08/) in your scene you can also have a live preview from a camera in the engine. This allows you to make full use of the engine's capabilities such as [effects](https://img.ly/docs/cesdk/android/filters-and-effects-6f88ac/), [strokes](https://img.ly/docs/cesdk/android/outlines/strokes-c2e621/) and [drop shadows](https://img.ly/docs/cesdk/android/outlines/shadows-and-glows-6610fa/), while the preview integrates with the composition of your scene. Simply swap out the `VideoFill` of a block with a `PixelStreamFill`. This guide shows you how the `PixelStreamFill` can be used in combination with a camera.

Before starting the implementation, we are going to need couple more dependencies other than the Engine itself. Camera preview implementation
is based on the android library [camerax](https://developer.android.com/training/camerax), therefore, we should include all required camerax
dependencies to our project. You can check all available dependencies [here](https://developer.android.com/training/camerax/architecture).
Other than camerax, we also need to include the Engine camera extension dependency. This dependency provides API for a single line bridging
between camerax and the Engine.

It is important that we use camerax version >= 1.1.0 in order to avoid unexpected crashes due to API signature changes. Also, it is highly
recommended to always use the exact same version for both `engine` and `engine-camera` dependencies.

```kotlin highlight-dependencies
implementation "ly.img:engine-camera:1.70.0"
implementation "androidx.camera:camera-core:1.2.3"
implementation "androidx.camera:camera-camera2:1.2.3"
implementation "androidx.camera:camera-view:1.2.3"
implementation "androidx.camera:camera-lifecycle:1.2.3"
implementation "androidx.camera:camera-video:1.2.3"
```

Now we have all the required dependencies to work with the camera. We instantiate all required camerax objects in order to start previewing.
You can check all available camerax preview configurations [here](https://developer.android.com/training/camerax/architecture).

```kotlin highlight-setupCamera
    val cameraSelector = CameraSelector.Builder()
        .requireLensFacing(CameraSelector.LENS_FACING_FRONT)
        .build()
    val preview = Preview.Builder().build()
    val qualitySelector = QualitySelector.from(Quality.FHD)
    val recorder = Recorder.Builder()
        .setQualitySelector(qualitySelector)
        .build()
    val videoCapture = VideoCapture.Builder(recorder)
        .setMirrorMode(MirrorMode.MIRROR_MODE_ON_FRONT_ONLY)
        .build()

    cameraProvider.bindToLifecycle(activity, cameraSelector, preview, videoCapture)
```

We create a video scene with a single page. Then we create a `PixelStreamFill` and assign it to the page.
Then we connect camerax `Preview` and `PixelStreamFill` objects via `setCameraPreview` extension function that is provided by `engine-camera` dependency.
To demonstrate the live preview capabilities of the engine we also apply an effect to the page.

```kotlin highlight-setupScene
val scene = engine.scene.createForVideo()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)
val pixelStreamFill = engine.block.createFill(FillType.PixelStream)
engine.block.setFill(block = page, fill = pixelStreamFill)
engine.setCameraPreview(pixelStreamFill, preview, mirrored = false)
engine.block.appendEffect(
    block = page,
    effectBlock = engine.block.createEffect(EffectType.HalfTone),
)
```

## Orientation

To not waste expensive compute time by transforming the pixel data of the buffer itself, it's often beneficial to apply a transformation during rendering and let the GPU handle this work much more efficiently. For this purpose the `PixelStreamFill` has an `orientation` property. You can use it to mirror the image or rotate it in 90° steps.
This property lets you easily mirror an image from a front facing camera or rotate the image by 90° when the user holds a device sideways. Note that its initial value is set in `setCameraPreview` based on camerax preview transformation info listener and `mirrored` flag.
Available values are `Left`, `LeftMirrored`, `Down`, `DownMirrored`, `Right`, `RightMirrored`, `Up`, `UpMirrored`.

```kotlin highlight-orientation
// If camerax preview transformation info rotation is 90, this will return Left. If we passed mirrored = true, this would be LeftMirrored.
val orientation = engine.block.getEnum(
    block = pixelStreamFill,
    property = "fill/pixelStream/orientation",
)
```

## Camera

Camerax is a very powerful library and it allows video capturing, image capturing and other use cases. Note that the Engine does not limit usage of any of the camerax use cases:
it only provides a mechanism to render camera preview into the Engine canvas. For demonstration purposes, we will proceed with video capture.
We create a video capture session and start recording the frames into a temporary file in `filesDir`. Once the recording is finished we swap the `PixelStreamFill` with a `VideoFill` to play back the recorded video file.

```kotlin highlight-camera
val recordingFile = File(surfaceView.context.filesDir, "temp.mp4")
val fileOutputOptions = FileOutputOptions.Builder(recordingFile).build()
val recording = videoCapture.output
    .prepareRecording(activity, fileOutputOptions)
    .start(ContextCompat.getMainExecutor(surfaceView.context)) {
        if (it !is VideoRecordEvent.Finalize) return@start
        val videoFill = engine.block.createFill(FillType.Video)
        engine.block.setFill(block = page, fill = videoFill)
        engine.block.setString(
            block = videoFill,
            property = "fill/video/fileURI",
            value = recordingFile.toUri().toString(),
        )
    }
delay(5000L)
recording.stop()
```

## Full Code

Here's the full code for both files:

### build.gradle

```
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    namespace "ly.img.editor.camera"
    compileSdk 35

    defaultConfig {
        applicationId "ly.img.editor.camera"
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
}

dependencies {
    implementation "ly.img:engine-camera:$UBQ_VERSION$"
    implementation "androidx.camera:camera-core:1.2.3"
    implementation "androidx.camera:camera-camera2:1.2.3"
    implementation "androidx.camera:camera-view:1.2.3"
    implementation "androidx.camera:camera-lifecycle:1.2.3"
    implementation "androidx.camera:camera-video:1.2.3"
    implementation "ly.img:engine:$UBQ_VERSION$"
    implementation "androidx.appcompat:appcompat:1.6.0"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3"
}
```

### UsingCamera.kt

```kotlin
import android.view.SurfaceView
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.CameraSelector
import androidx.camera.core.MirrorMode
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.video.FileOutputOptions
import androidx.camera.video.Quality
import androidx.camera.video.QualitySelector
import androidx.camera.video.Recorder
import androidx.camera.video.VideoCapture
import androidx.camera.video.VideoRecordEvent
import androidx.core.content.ContextCompat
import androidx.core.net.toUri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.EffectType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.camera.setCameraPreview
import java.io.File

fun usingCamera(
    activity: AppCompatActivity,
    surfaceView: SurfaceView,
    cameraProvider: ProcessCameraProvider,
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindSurfaceView(surfaceView)

    val cameraSelector = CameraSelector.Builder()
        .requireLensFacing(CameraSelector.LENS_FACING_FRONT)
        .build()
    val preview = Preview.Builder().build()
    val qualitySelector = QualitySelector.from(Quality.FHD)
    val recorder = Recorder.Builder()
        .setQualitySelector(qualitySelector)
        .build()
    val videoCapture = VideoCapture.Builder(recorder)
        .setMirrorMode(MirrorMode.MIRROR_MODE_ON_FRONT_ONLY)
        .build()

    cameraProvider.bindToLifecycle(activity, cameraSelector, preview, videoCapture)

    val scene = engine.scene.createForVideo()
    val page = engine.block.create(DesignBlockType.Page)
    engine.block.appendChild(parent = scene, child = page)
    val pixelStreamFill = engine.block.createFill(FillType.PixelStream)
    engine.block.setFill(block = page, fill = pixelStreamFill)
    engine.setCameraPreview(pixelStreamFill, preview, mirrored = false)
    engine.block.appendEffect(
        block = page,
        effectBlock = engine.block.createEffect(EffectType.HalfTone),
    )

    // If camerax preview transformation info rotation is 90, this will return Left. If we passed mirrored = true, this would be LeftMirrored.
    val orientation = engine.block.getEnum(
        block = pixelStreamFill,
        property = "fill/pixelStream/orientation",
    )

    val recordingFile = File(surfaceView.context.filesDir, "temp.mp4")
    val fileOutputOptions = FileOutputOptions.Builder(recordingFile).build()
    val recording = videoCapture.output
        .prepareRecording(activity, fileOutputOptions)
        .start(ContextCompat.getMainExecutor(surfaceView.context)) {
            if (it !is VideoRecordEvent.Finalize) return@start
            val videoFill = engine.block.createFill(FillType.Video)
            engine.block.setFill(block = page, fill = videoFill)
            engine.block.setString(
                block = videoFill,
                property = "fill/video/fileURI",
                value = recordingFile.toUri().toString(),
            )
        }
    delay(5000L)
    recording.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
