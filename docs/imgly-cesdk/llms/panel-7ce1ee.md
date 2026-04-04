# Source: https://img.ly/docs/cesdk/android/user-interface/customization/panel-7ce1ee/

---
title: "Panel"
description: "Show or hide side panels to focus the user interface on what matters most for your use case."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/panel-7ce1ee/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Panel](https://img.ly/docs/cesdk/android/user-interface/customization/panel-7ce1ee/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-panel/DefaultPanelSolution.kt reference-only
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.KeyboardArrowUp
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.sheet.SheetType
import ly.img.editor.rememberForDesign

@Composable
fun DefaultPanelSolution(navController: NavHostController) {
    val engineConfig = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfig = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.rememberForDesign(
                listBuilder = Dock.ListBuilder.rememberForDesign().modify {
                    addFirst {
                        openPanelDockButton
                    }
                },
            )
        },
    )

    DesignEditor(
        engineConfiguration = engineConfig,
        editorConfiguration = editorConfig,
    ) {
        navController.popBackStack()
    }
}

val openPanelDockButton
    @Composable get() = Dock.Button.remember(
        id = EditorComponentId("open_library_panel"),
        text = { Text("Open Library") },
        icon = { Icon(Icons.Rounded.KeyboardArrowUp, null) },
        onClick = {
            editorContext.eventHandler.send(
                EditorEvent.Sheet.Open(
                    SheetType.LibraryAdd(),
                ),
            )
        },
    )
```

```kotlin file=@cesdk_android_examples/editor-guides-configuration-panel/CustomPanelSolution.kt reference-only
import androidx.compose.foundation.layout.Column
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.KeyboardArrowUp
import androidx.compose.material3.Button
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.data.Height
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.sheet.SheetStyle
import ly.img.editor.core.sheet.SheetType
import ly.img.editor.rememberForDesign

@Composable
fun CustomPanelSolution(navController: NavHostController) {
    val engineConfig = EngineConfiguration.rememberForDesign(
        license = null, // evaluation mode with watermark
    )

    val editorConfig = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.rememberForDesign(
                listBuilder = Dock.ListBuilder.rememberForDesign().modify {
                    addFirst {
                        openCustomPanelDockButton
                    }
                },
            )
        },
    )

    DesignEditor(
        engineConfiguration = engineConfig,
        editorConfiguration = editorConfig,
    ) {
        navController.popBackStack()
    }
}

val openCustomPanelDockButton
    @Composable get() = Dock.Button.remember(
        id = EditorComponentId("open_panel"),
        text = { Text("Open Panel") },
        icon = { Icon(Icons.Rounded.KeyboardArrowUp, null) },
        onClick = {
            editorContext.eventHandler.send(
                EditorEvent.Sheet.Open(
                    customSheetType,
                ),
            )
        },
    )

val customSheetType: SheetType
    get() =
        SheetType.Custom(
            style = SheetStyle(
                isFloating = false,
                minHeight = Height.Exactly(0.dp),
                maxHeight = Height.Fraction(0.7F),
                isHalfExpandingEnabled = true,
                isHalfExpandedInitially = true,
                animateInitialValue = true,
            ),
            content = {
                Column {
                    Text("Custom Panel")
                    Button(
                        onClick = {
                            editorContext.eventHandler.send(
                                EditorEvent.Sheet.Close(animate = true),
                            )
                        },
                    ) { Text("Close Panel") }
                }
            },
        )
```

A panel is a UI layer that displays above the canvas, and allows the user perform a scoped task like accessing asset library, selecting filters, or any custom action.

![Panel on Android](./assets/panel-android.png)

## Controlling a Panel

Panels are implemented as different types of `SheetType` that allow you to display content in standard sheet overlays. Panels are opened using the `EditorEvent.Sheet.Open` event, and passing in the desired `sheetType`

```kotlin highlight-open-panel
editorContext.eventHandler.send(
    EditorEvent.Sheet.Open(
        SheetType.LibraryAdd(),
    ),
)
```

After use, they can be closed using the `EditorEvent.Sheet.Close` event.

```kotlin highlight-close-panel
editorContext.eventHandler.send(
    EditorEvent.Sheet.Close(animate = true),
)
```

The boolean parameter indicates whether the panel should be closed with animation.

## Creating a Custom Panel

To create a custom panel, you can make a new `SheetType.Custom()` and define your UI inside the `content` parameter.

```kotlin highlight-open-custom-panel
SheetType.Custom(
    style = SheetStyle(
        isFloating = false,
        minHeight = Height.Exactly(0.dp),
        maxHeight = Height.Fraction(0.7F),
        isHalfExpandingEnabled = true,
        isHalfExpandedInitially = true,
        animateInitialValue = true,
    ),
    content = {
        Column {
            Text("Custom Panel")
            Button(
                onClick = {
                    editorContext.eventHandler.send(
                        EditorEvent.Sheet.Close(animate = true),
                    )
                },
            ) { Text("Close Panel") }
        }
    },
)
```

In the `style` parameter, you can define how the sheet will look like.
These are the parameters available for `SheetStyle` constructor, and what they change:

| Parameter                 | Default Value           | Description                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isFloating`              | `false`                 | whether the sheet should be floating. If `true` the sheet will be rendered over the editor, if `false` then the canvas will be zoomed to adjust the sheet.                                                                                                                                                  |
| `minHeight`               | `Height.Exactly(0.dp)`  | the minimum height of the sheet.                                                                                                                                                                                                                                                                            |
| `maxHeight`               | `Height.Fraction(0.5f)` | the maximum height of the sheet. If null, then there is no limit to the height. Once the maximum height is reached, the content of the sheet becomes vertically scrollable, if it is supported. Note that if you need the content to be scrollable in `SheetType.Custom`, then you need to add it manually. |
| `isHalfExpandingEnabled`  | `false`                 | whether the sheet should have a half expanded state. If false, then the sheet gets only 2 states: hidden and expanded.                                                                                                                                                                                      |
| `isHaldExpandedInitially` | `false`                 | whether the sheet should be opened as half expanded initially. This flag takes effect only if `isHalfExpandingEnabled` is true.                                                                                                                                                                             |
| `animateInitialValue`     | `true`                  | whether initial expanded or half-expanded state should be animated.                                                                                                                                                                                                                                         |

## Default Sheet Types

The editor provides several built-in sheet types for common functionality:

| Panel Type                   | Description                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| `SheetType.LibraryAdd()`     | Display `LibraryCategory` in order to add assets to the scene     |
| `SheetType.LibraryReplace()` | Display `LibraryCategory` in order to replace assets in the scene |
| `SheetType.Reorder()`        | Reorder videos on the background track                            |
| `SheetType.Adjustments()`    | Make adjustments to design blocks with image and video fills      |
| `SheetType.Filter()`         | Set filters to design blocks with image and video fills           |
| `SheetType.Effect()`         | Set effects to design blocks with image and video fills           |
| `SheetType.Blur()`           | Set blurs to design blocks with image and video fills             |
| `SheetType.Crop()`           | Crop design blocks with image and video fills                     |
| `SheetType.Layer()`          | Control the layering of design blocks                             |
| `SheetType.FormatText()`     | Control formatting of text blocks                                 |
| `SheetType.Shape()`          | Control the shape of various blocks                               |
| `SheetType.FillStroke()`     | Control the fill and/or stroke of various blocks                  |
| `SheetType.Volume()`         | Control the volume of audio/video                                 |
| `SheetType.Animation()`      | Set in/out/loop animation to design blocks                        |

## Full source code

#### Default Panel Solution

```kotlin file=@cesdk_android_examples/editor-guides-configuration-panel/DefaultPanelSolution.kt
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.KeyboardArrowUp
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.sheet.SheetType
import ly.img.editor.rememberForDesign

@Composable
fun DefaultPanelSolution(navController: NavHostController) {
    val engineConfig = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfig = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.rememberForDesign(
                listBuilder = Dock.ListBuilder.rememberForDesign().modify {
                    addFirst {
                        openPanelDockButton
                    }
                },
            )
        },
    )

    DesignEditor(
        engineConfiguration = engineConfig,
        editorConfiguration = editorConfig,
    ) {
        navController.popBackStack()
    }
}

val openPanelDockButton
    @Composable get() = Dock.Button.remember(
        id = EditorComponentId("open_library_panel"),
        text = { Text("Open Library") },
        icon = { Icon(Icons.Rounded.KeyboardArrowUp, null) },
        onClick = {
            editorContext.eventHandler.send(
                EditorEvent.Sheet.Open(
                    SheetType.LibraryAdd(),
                ),
            )
        },
    )
```

#### Custom Panel Solution

```kotlin file=@cesdk_android_examples/editor-guides-configuration-panel/CustomPanelSolution.kt
import androidx.compose.foundation.layout.Column
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.KeyboardArrowUp
import androidx.compose.material3.Button
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.data.Height
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.sheet.SheetStyle
import ly.img.editor.core.sheet.SheetType
import ly.img.editor.rememberForDesign

@Composable
fun CustomPanelSolution(navController: NavHostController) {
    val engineConfig = EngineConfiguration.rememberForDesign(
        license = null, // evaluation mode with watermark
    )

    val editorConfig = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.rememberForDesign(
                listBuilder = Dock.ListBuilder.rememberForDesign().modify {
                    addFirst {
                        openCustomPanelDockButton
                    }
                },
            )
        },
    )

    DesignEditor(
        engineConfiguration = engineConfig,
        editorConfiguration = editorConfig,
    ) {
        navController.popBackStack()
    }
}

val openCustomPanelDockButton
    @Composable get() = Dock.Button.remember(
        id = EditorComponentId("open_panel"),
        text = { Text("Open Panel") },
        icon = { Icon(Icons.Rounded.KeyboardArrowUp, null) },
        onClick = {
            editorContext.eventHandler.send(
                EditorEvent.Sheet.Open(
                    customSheetType,
                ),
            )
        },
    )

val customSheetType: SheetType
    get() =
        SheetType.Custom(
            style = SheetStyle(
                isFloating = false,
                minHeight = Height.Exactly(0.dp),
                maxHeight = Height.Fraction(0.7F),
                isHalfExpandingEnabled = true,
                isHalfExpandedInitially = true,
                animateInitialValue = true,
            ),
            content = {
                Column {
                    Text("Custom Panel")
                    Button(
                        onClick = {
                            editorContext.eventHandler.send(
                                EditorEvent.Sheet.Close(animate = true),
                            )
                        },
                    ) { Text("Close Panel") }
                }
            },
        )
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
