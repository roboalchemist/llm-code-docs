# Source: https://img.ly/docs/cesdk/android/colors/create-color-palette-7012e0/

---
title: "Create a Color Palette"
description: "Build reusable color palettes to maintain consistency and streamline user choices."
platform: android
url: "https://img.ly/docs/cesdk/android/colors/create-color-palette-7012e0/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/android/colors-a9b79c/) > [Create a Color Palette](https://img.ly/docs/cesdk/android/colors/create-color-palette-7012e0/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-color-palette/ColorPaletteEditorSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Color
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ColorPaletteEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        colorPalette = remember {
            listOf(
                Color(0xFF4A67FF),
                Color(0xFFFFD333),
                Color(0xFFC41230),
                Color(0xFF000000),
                Color(0xFFFFFFFF),
            )
        },
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

In this example, we will show you how to make color palette configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

## Configuration

Color palette configuration is part of the `EditorConfiguration` class. Use the `EditorConfiguration.getDefault` helper function to make color palette configurations.

- `colorPalette` - the color palette used for UI elements that contain predefined color options, e.g., for "Fill Color" or "Stroke Color".

```kotlin highlight-configuration-colorPalette
colorPalette = remember {
    listOf(
        Color(0xFF4A67FF),
        Color(0xFFFFD333),
        Color(0xFFC41230),
        Color(0xFF000000),
        Color(0xFFFFFFFF),
    )
},
```

## Full Code

Here's the full code:

```kotlin
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Color
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ColorPaletteEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>",
    )
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        colorPalette = remember {
            listOf(
                Color(0xFF4A67FF),
                Color(0xFFFFD333),
                Color(0xFFC41230),
                Color(0xFF000000),
                Color(0xFFFFFFFF),
            )
        },
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
