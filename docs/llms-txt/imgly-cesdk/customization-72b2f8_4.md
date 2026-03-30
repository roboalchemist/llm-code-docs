# Source: https://img.ly/docs/cesdk/flutter/user-interface/customization-72b2f8/

---
title: "Customization"
description: "Control which features are available and how UI components behave, appear, or are arranged in the editor."
platform: flutter
url: "https://img.ly/docs/cesdk/flutter/user-interface/customization-72b2f8/"
---

> This is one page of the CE.SDK Flutter documentation. For a complete overview, see the [Flutter Documentation Index](https://img.ly/docs/cesdk/flutter.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/flutter/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/flutter/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/flutter/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/flutter/user-interface/customization-72b2f8/)

---

```swift file=@cesdk_flutter_examples/../ios/Runner/Guides/ConfigurationGuide.swift reference-only
import imgly_camera
import imgly_editor
import SwiftUI

func useCustomEditor() {
  IMGLYEditorPlugin.builderClosure = { _, metadata in
    // Make decisions based on your own metadata.
    if metadata?["use_custom_editor"] as? Bool == true {
      // Return your custom editor.
      EditorBuilder.custom { settings, _, _, result in
        CustomEditor(settings: settings, result: result)
      }
    } else {
      // Return a custom or prebuilt editor.
      EditorBuilder.design()
    }
  }
}

private struct CustomEditor: View {
  init(settings _: EditorSettings, result _: @escaping EditorBuilder.EditorBuilderResult) {}

  var body: some View {
    Text("Custom Editor")
  }
}

func configureCamera() {
  IMGLYCameraPlugin.builderClosure = { metadata in
    // Make decisions based on your own metadata.
    if metadata?["use_custom_camera"] as? Bool == true {
      // Return your custom camera.
      CameraBuilder.custom { settings, url, metadata, result in
        CustomCamera(settings: settings, url: url, metadata: metadata, result: result)
      }
    } else {
      // Return a custom or prebuilt camera.
      CameraBuilder.default()
    }
  }
}

private struct CustomCamera: View {
  init(
    settings _: CameraSettings,
    url _: URL?,
    metadata _: [String: Any]?,
    result _: @escaping CameraBuilder.CameraBuilderResult
  ) {}

  var body: some View {
    Text("Custom Camera")
  }
}

```

```kotlin file=@cesdk_flutter_examples/../android/app/src/main/kotlin/ly/img/editor/flutter/showcases/guides/ConfigurationGuide.kt reference-only
package ly.img.editor.flutter.showcases.guides

import androidx.compose.runtime.Composable
import ly.img.camera.core.CameraLayoutMode
import ly.img.camera.core.CameraMode
import ly.img.camera.core.CameraResult
import ly.img.camera.core.CaptureVideo
import ly.img.camera.flutter.plugin.IMGLYCameraPlugin
import ly.img.editor.flutter.plugin.IMGLYEditorPlugin
import ly.img.editor.flutter.plugin.builder.EditorBuilder
import ly.img.editor.flutter.plugin.builder.EditorBuilderResult
import ly.img.editor.flutter.plugin.model.EditorSettings

private fun useCustomEditor() {
    IMGLYEditorPlugin.builderClosure = { _, metadata ->
        if (metadata?.get("custom") == true) {
            EditorBuilder.custom { settings, _, _, result, onClose ->
                @Composable {
                    CustomEditor(settings, result, onClose)
                }
            }
        } else {
            EditorBuilder.design()
        }
    }
}

private fun customizeCamera() {
    // Configure the [CaptureVideo.Input].
    IMGLYCameraPlugin.configurationClosure = {
        /*
         * This closure requires returning a [CaptureVideo.Input].
         *
         * You can access the following parameters:
         * - "cameraSettings": The CameraSettings passed from the Flutter side.
         * - "engineConfiguration": The EngineConfiguration that includes your license.
         * - "metadata": Metadata passed from the Flutter side.
         * - "videoUri": The video reaction URL passed from Flutter, or null.
         */

        if (metadata["is_reactions"] == true) {
            CaptureVideo.Input(
                engineConfiguration = engineConfiguration,
                cameraMode = CameraMode.Reaction(
                    videoUri ?: throw RuntimeException("Missing video URL."),
                    cameraLayoutMode = CameraLayoutMode.Horizontal,
                    positionsSwapped = false,
                ),
            )
        } else {
            // Simply return null to use the default camera configuration.
            null
        }
    }

    // Adding custom metadata to the CameraResult.
    IMGLYCameraPlugin.resultClosure = {
        /*
         * This closure allows you to add custom metadata of type [Map<String, Any?>] to the CameraResult.
         * You can access the following values:
         * - "cameraResult": The native CameraResult returned by the camera.
         * - "inputMetadata": Metadata passed from the Flutter side when the camera was opened.
         *
         * The return value must be a [Map<String, Any?>], which will be passed to the Dart-side
         * representation of the CameraResult.
         *
         * Notes:
         * - Use `mapOf<String, Any?>()` to return key-value pairs.
         * - Return `null` if no metadata should be added.
         */

        // Example: Read the result data...
        val recordings = when (val result = cameraResult) {
            is CameraResult.Record -> result.recordings
            is CameraResult.Reaction -> result.reaction
            else -> emptyList()
        }

        // Return a custom metadata map
        mapOf(
            "MY_CUSTOM_KEY" to "MY_CUSTOM_VALUE",
        )
    }
}

@Composable
private fun CustomEditor(
    settings: EditorSettings,
    result: EditorBuilderResult,
    onClose: (Throwable?) -> Unit,
) {
}
```

The Flutter `imgly_editor` plugin is built on top of the native Android and iOS UI implementation and has no dedicated Flutter UI.
However, you still have access to the same customization options as for iOS and Android.
To use them you need to configure them natively for both platforms.

## Native Interfaces

In order to allow intuitive and easily accessible native customization of the editors, we provide dedicated interfaces and convenience functions for both iOS and Android.
The editor that is opened via the `IMGLYEditor.openEditor()` function can be completely customized and exchanged.
For this to work you can use the `IMGLYEditorPlugin.builderClosure` which provides an optional `EditorPreset` and `metadata`
with which you can provide any prebuilt or custom editor view. The `metadata` parameter of the `openEditor` function can be utilized
to provide customization details from the Flutter side of your app to the native side:

### iOS

On iOS, we provide fallback functions for our default editors via:

- `EditorBuilder.design()`
- `EditorBuilder.apparel()`
- `EditorBuilder.photo()`
- `EditorBuilder.video()`
- `EditorBuilder.postcard()`

In case you want a completely custom UI, you can use the `EditorBuilder.custom` function that allows you to return a custom `View` based on a given `EditorConfig`, an `EditorPreset`, `metadata` and an `EditorBuilderResult`:

#### 1. Import the dependencies:

```swift highlight-import-swift
import imgly_camera
import imgly_editor
import SwiftUI
```

#### 2. Assign your custom editor:

```swift highlight-closure-swift
IMGLYEditorPlugin.builderClosure = { _, metadata in
  // Make decisions based on your own metadata.
  if metadata?["use_custom_editor"] as? Bool == true {
    // Return your custom editor.
    EditorBuilder.custom { settings, _, _, result in
      CustomEditor(settings: settings, result: result)
    }
  } else {
    // Return a custom or prebuilt editor.
    EditorBuilder.design()
  }
}
```

Further, we provide convenience extensions both for the `OnCreate` and `OnExport` callbacks to reduce the amount of code you need to write. For a detailed example, please take a look at our showcases app.

### Android

On Android, we provide fallback functions for our default editors via

- `EditorBuilder.design()`
- `EditorBuilder.apparel()`
- `EditorBuilder.photo()`
- `EditorBuilder.postcard()`.

In case you want a completely custom UI, you can use the `EditorBuilder.custom` function that allows you to return a custom `@Composable` function based on a given `EditorConfig`, an `EditorPreset`, `metadata` and an `EditorBuilderResult`:

#### 1. Update the `android/app/build.gradle` file and add the following:

```diff
android {
    (...)
+    kotlinOptions {
+        jvmTarget = "1.8"
+    }

+    buildFeatures {
+      compose true
+    }

+    composeOptions {
+      kotlinCompilerExtensionVersion = "1.5.3"
+    }
}

dependencies {
+  implementation "ly.img:editor:$UBQ_VERSION$"
+  implementation(platform("androidx.compose:compose-bom:2023.05.01"))
+  implementation "androidx.activity:activity-compose:1.8.2"
}
```

#### 2. Import the dependencies:

```kotlin highlight-import-kotlin
import androidx.compose.runtime.Composable
import ly.img.camera.core.CameraLayoutMode
import ly.img.camera.core.CameraMode
import ly.img.camera.core.CameraResult
import ly.img.camera.core.CaptureVideo
import ly.img.camera.flutter.plugin.IMGLYCameraPlugin
import ly.img.editor.flutter.plugin.IMGLYEditorPlugin
import ly.img.editor.flutter.plugin.builder.EditorBuilder
import ly.img.editor.flutter.plugin.builder.EditorBuilderResult
import ly.img.editor.flutter.plugin.model.EditorSettings
```

#### 3. Assign your custom editor:

```kotlin highlight-closure-kotlin
IMGLYEditorPlugin.builderClosure = { _, metadata ->
    if (metadata?.get("custom") == true) {
        EditorBuilder.custom { settings, _, _, result, onClose ->
            @Composable {
                CustomEditor(settings, result, onClose)
            }
        }
    } else {
        EditorBuilder.design()
    }
}
```

Further, we provide a class called `EditorDefaults` which contains convenience methods for both the `OnCreate` and `OnExport` callbacks to reduce the amount of code you need to write. For a detailed example, please take a look here.



---

## Related Pages

- [Dock](https://img.ly/docs/cesdk/flutter/user-interface/customization/dock-cb916c/) - Configure the dock area to show or hide tools, panels, or quick access actions.


---

## More Resources

- **[Flutter Documentation Index](https://img.ly/docs/cesdk/flutter.md)** - Browse all Flutter documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/flutter/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/flutter/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
