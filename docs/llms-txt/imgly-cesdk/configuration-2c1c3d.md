# Source: https://img.ly/docs/cesdk/android/configuration-2c1c3d/

---
title: "Configuration"
description: "Learn how to configure CE.SDK to match your application's functional, visual, and performance requirements."
platform: android
url: "https://img.ly/docs/cesdk/android/configuration-2c1c3d/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Configuration](https://img.ly/docs/cesdk/android/configuration-2c1c3d/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-basics/BasicEditorSolution.kt reference-only
import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.engine.EngineRenderTarget
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun BasicEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
        userId = "<your unique user id>",
        baseUri = Uri.parse("file:///android_asset/"),
        sceneUri = EngineConfiguration.defaultDesignSceneUri,
        renderTarget = EngineRenderTarget.SURFACE_VIEW,
    )
    DesignEditor(engineConfiguration = engineConfiguration) {
        // You can set result here
        navController.popBackStack()
    }
}
```

In this example, we will show you how to make basic configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

## Configuration

All the basic configuration settings are part of the `EngineConfiguration`.

- `license` - the license to activate the [Engine](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) with.

```kotlin highlight-configuration-license
license = "<your license here>", // pass null or empty for evaluation mode with watermark
```

- `userId` - an optional unique ID tied to your application's user. This helps us accurately calculate monthly active users (MAU). Especially useful when one person uses the app on multiple devices with a sign-in feature, ensuring they're counted once. Providing this aids in better data accuracy. The default value is `null`.

```kotlin highlight-configuration-userId
userId = "<your unique user id>",
```

- `baseUri` - is used to initialize the engine's [setting](https://img.ly/docs/cesdk/android/settings-970c98/) before the editor's [callback](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) is run. It is the foundational URI for constructing absolute paths from relative ones. For example, setting it to the Android assets directory allows loading resources directly from there: `file:///android_asset/`. This URI enables the loading of specific scenes or assets using their relative paths. The default value is pointing at the versioned IMG.LY CDN but it should be changed in production environments.

```kotlin highlight-configuration-baseUri
baseUri = Uri.parse("file:///android_asset/"),
```

- `sceneUri` - the [scene](https://img.ly/docs/cesdk/android/open-the-editor/blank-canvas-18ff05/) URI to load content within the editor. Note that this configuration is only available in `EngineConfiguration.rememberFor{solution-name}` helper functions. This URI is used to load the scene in `EdiorConfiguration.onCreate`, therefore, you can configure the scene you load without helper functions too: simply invoke `EditorDefaults.onCreate(engine, sceneUri, eventHandler)` in `EdiorConfiguration.onCreate`. By default, helper functions load the scenes that are available at `EdiorConfiguration.default{solution-name}Scene`. Normally, you should not modify the `sceneUri`, however, you may want to save/restore the editing progress for your customers. If that is the case, you should [save the scene](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/) in one of the [callbacks](https://img.ly/docs/cesdk/android/user-interface/events-514b70/), then provide the URI of the newly saved scene when your customer opens the editor next time.

```kotlin highlight-configuration-sceneUri
sceneUri = EngineConfiguration.defaultDesignSceneUri,
```

- `renderTarget` - the target which should be used by the [Engine](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/) to render. The engine is able to render on both [SurfaceView](https://developer.android.com/reference/android/view/SurfaceView) and [TextureView](https://developer.android.com/reference/android/view/TextureView). The default value is `EngineRenderTarget.SURFACE_VIEW`.

```kotlin highlight-configuration-renderTarget
renderTarget = EngineRenderTarget.SURFACE_VIEW,
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.engine.EngineRenderTarget
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun BasicEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>",
        userId = "<your unique user id>",
        baseUri = Uri.parse("file:///android_asset/"),
        sceneUri = EngineConfiguration.defaultDesignSceneUri,
        renderTarget = EngineRenderTarget.SURFACE_VIEW,
    )
    DesignEditor(engineConfiguration = engineConfiguration) {
        // You can set result here
        navController.popBackStack()
    }
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
