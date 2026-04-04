# Source: https://img.ly/docs/cesdk/react-native/user-interface/customization-72b2f8/

---
title: "Customization"
description: "Control which features are available and how UI components behave, appear, or are arranged in the editor."
platform: react-native
url: "https://img.ly/docs/cesdk/react-native/user-interface/customization-72b2f8/"
---

> This is one page of the CE.SDK React Native documentation. For a complete overview, see the [React Native Documentation Index](https://img.ly/docs/cesdk/react-native.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/react-native/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/react-native/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/react-native/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/react-native/user-interface/customization-72b2f8/)

---

```swift file=@cesdk_react_native_examples/../ios/Guides/ConfigurationGuide.swift reference-only
import IMGLYCameraModule

import IMGLYEditorModule
import SwiftUI

func useCustomEditor() {
  IMGLYEditorModuleSwiftAdapter.shared.builderClosure = { _, metadata in
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

func configureCamera() {
  IMGLYCameraModuleSwiftAdapter.shared.cameraBuilderClosure = { metadata in
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

private struct CustomEditor: View {
  init(settings _: EditorSettings, result _: @escaping EditorBuilder.EditorBuilderResult) {}

  var body: some View {
    Text("Custom Editor")
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

```kotlin file=@cesdk_react_native_examples/../android/app/src/main/java/ly/img/editor/reactnative/showcases/guides/ConfigurationGuide.kt reference-only
@file:Suppress("ktlint:standard:import-ordering")

package ly.img.editor.reactnative.showcases.guides

import androidx.compose.runtime.Composable
import ly.img.camera.core.CaptureVideo
import ly.img.camera.core.EngineConfiguration
import ly.img.camera.reactnative.module.IMGLYCameraModule
import ly.img.camera.reactnative.module.model.CameraResult
import ly.img.editor.reactnative.module.IMGLYEditorModule
import ly.img.editor.reactnative.module.builder.EditorBuilder
import ly.img.editor.reactnative.module.builder.EditorBuilderResult
import ly.img.editor.reactnative.module.model.EditorSettings

private fun useCustomEditor() {
    IMGLYEditorModule.builderClosure = { _, metadata ->
        if (metadata?.get("custom") == true) {
            EditorBuilder.custom {
                CustomEditor(settings, result, onClose)
            }
        } else {
            EditorBuilder.design()
        }
    }
}

private fun customizeCamera() {
    // Configure the [CaptureVideo.Input].
    IMGLYCameraModule.configurationClosure = { metadata ->
        val engineConfiguration = EngineConfiguration("MY_LICENSE")
        CaptureVideo.Input(engineConfiguration)
    }

    // Modify the [CameraResult].
    IMGLYCameraModule.resultClosure = { result ->
        CameraResult(result?.recording, mapOf("MY_CUSTOM_KEY" to "MY_CUSTOM_VALUE"))
    }
}

@Composable
private fun CustomEditor(
    settings: EditorSettings,
    result: EditorBuilderResult,
    onClose: (Throwable?) -> Unit,
) {}
```

The React Native `@imgly/editor-react-native` module is built on top of the native Android and iOS UI implementation and has no dedicated React Native UI.
However, you still have access to the same customization options as for iOS and Android.
To use them you need to configure them natively for both platforms.

## Native Interfaces

In order to allow intuitive and easily accessible native customization of the editors, we provide dedicated interfaces and convenience functions for both iOS and Android.
This layer is written in **Swift** and available via the `IMGLYEditorModuleSwiftAdapter.shared` instance.
The editor that is opened via the `IMGLYEditorModuleSwiftAdapter.openEditor()` function can be completely customized and exchanged.
For this to work you can use the `IMGLYEditorModuleSwiftAdapter.builderClosure` which provides an optional `EditorPreset` and `metadata`
with which you can provide any prebuilt or custom editor view. The `metadata` parameter of the `openEditor` function can be utilized
to provide customization details from the React Native side of your app to the native side:

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
import IMGLYEditorModule
import SwiftUI
```

#### 2. Assign your custom editor:

```swift highlight-closure-swift
IMGLYEditorModuleSwiftAdapter.shared.builderClosure = { _, metadata in
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
- `EditorBuilder.postcard()`
- `EditorBuilder.video()`.

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
+      kotlinCompilerExtensionVersion = "1.5.10"
+    }
}

dependencies {
+  implementation "ly.img:editor:$UBQ_VERSION$"
+  implementation(platform("androidx.compose:compose-bom:2023.05.01"))
+  implementation "androidx.activity:activity-compose:1.6.1"
}
```

#### 2. Import the dependencies:

```kotlin highlight-import-compose
import androidx.compose.runtime.Composable
```

```kotlin highlight-import-editor
import ly.img.editor.reactnative.module.IMGLYEditorModule
import ly.img.editor.reactnative.module.builder.EditorBuilder
import ly.img.editor.reactnative.module.builder.EditorBuilderResult
import ly.img.editor.reactnative.module.model.EditorSettings
```

#### 3. Assign your custom editor:

```kotlin highlight-closure-kotlin
IMGLYEditorModule.builderClosure = { _, metadata ->
    if (metadata?.get("custom") == true) {
        EditorBuilder.custom {
            CustomEditor(settings, result, onClose)
        }
    } else {
        EditorBuilder.design()
    }
}
```

Further, we provide a class called `EditorDefaults` which contains convenience methods for both the `OnCreate` and `OnExport` callbacks to reduce the amount of code you need to write. For a detailed example, please take a look here.



---

## Related Pages

- [Dock](https://img.ly/docs/cesdk/react-native/user-interface/customization/dock-cb916c/) - Configure the dock area to show or hide tools, panels, or quick access actions.


---

## More Resources

- **[React Native Documentation Index](https://img.ly/docs/cesdk/react-native.md)** - Browse all React Native documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/react-native/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/react-native/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
