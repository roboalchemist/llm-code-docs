# Source: https://img.ly/docs/cesdk/android/user-interface/appearance/theming-4b0938/

---
title: "Theming"
description: "Customize the editor's visual theme to match your brand using flexible theming options."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/appearance/theming-4b0938/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Appearance](https://img.ly/docs/cesdk/android/user-interface/appearance-b155eb/) > [Theming](https://img.ly/docs/cesdk/android/user-interface/appearance/theming-4b0938/)

---

In this example, we will show you how to make theming configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

## Configuration

Theming configuration is part of the `EditorConfiguration` class. Use the `EditorConfiguration.getDefault` helper function to make theming configurations.

- `uiMode` - the UI mode of the editor. The default value is `EditorUiMode.SYSTEM`. These are the available values:
  - `EditorUiMode.SYSTEM` - editor will use the light color scheme if the system is in light mode and will use the dark color scheme if the system is in dark mode.
  - `EditorUiMode.LIGHT` - editor will always use the light color scheme.
  - `EditorUiMode.DARK` - editor will always use the dark color scheme.

```kotlin
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EditorUiMode
import ly.img.editor.EngineConfiguration
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ThemingEditorSolution(navController: NavHostController) {
    val engineConfiguration =
        EngineConfiguration.rememberForDesign(
            license = "<your license here>",
        )
    val editorConfiguration =
        EditorConfiguration.rememberForDesign(
            uiMode = EditorUiMode.DARK,
        )
    DesignEditor(
        engineConfiguration = engineConfiguration,
        editorConfiguration = editorConfiguration,
    ) {
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
