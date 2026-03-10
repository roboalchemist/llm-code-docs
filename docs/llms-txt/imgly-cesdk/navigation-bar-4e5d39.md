# Source: https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/

---
title: "Navigation Bar"
description: "Show, hide, or customize the editor's top navigation bar to match your app layout."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Navigation Bar](https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-navigation-bar/SimpleNavigationBarSolution.kt reference-only
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.LocalEditorScope
import ly.img.editor.core.component.NavigationBar
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun SimpleNavigationBarSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        navigationBar = {
            NavigationBar.remember(
                scope = LocalEditorScope.current.run {
                    remember(this) { NavigationBar.Scope(parentScope = this) }
                },
                visible = { true },
                enterTransition = { EnterTransition.None },
                exitTransition = { ExitTransition.None },
                decoration = {
                    // Also available via NavigationBar.DefaultDecoration
                    Box(
                        modifier =
                            Modifier
                                .fillMaxWidth()
                                .heightIn(min = 64.dp)
                                .background(MaterialTheme.colorScheme.surface)
                                .padding(PaddingValues(horizontal = 4.dp)),
                        contentAlignment = Alignment.Center,
                    ) {
                        it()
                    }
                },
                listBuilder = NavigationBar.ListBuilder.remember { },
                horizontalArrangement = { Arrangement.SpaceEvenly },
                // default value is { it() }
                itemDecoration = {
                    Box(modifier = Modifier.padding(2.dp)) {
                        it()
                    }
                },
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-navigation-bar/NavigationBarListBuilders.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.res.stringResource
import ly.img.editor.core.R
import ly.img.editor.core.component.NavigationBar
import ly.img.editor.core.component.rememberCloseEditor
import ly.img.editor.core.component.rememberExport
import ly.img.editor.core.component.rememberNextPage
import ly.img.editor.core.component.rememberPreviousPage
import ly.img.editor.core.component.rememberRedo
import ly.img.editor.core.component.rememberTogglePagesMode
import ly.img.editor.core.component.rememberTogglePreviewMode
import ly.img.editor.core.component.rememberUndo

@Composable
fun NavigationBar.ListBuilder.rememberForDesign() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePagesMode() }
        add { NavigationBar.Button.rememberExport() }
    }
}

@Composable
fun NavigationBar.ListBuilder.rememberForPhoto() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
        add { NavigationBar.Button.rememberExport() }
    }
}

@Composable
fun NavigationBar.ListBuilder.rememberForVideo() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberExport() }
    }
}

@Composable
fun NavigationBar.ListBuilder.rememberForApparel() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.CenterHorizontally) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberExport() }
    }
}

@Composable
fun NavigationBar.ListBuilder.rememberForPostcard() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
        add {
            NavigationBar.Button.rememberPreviousPage(
                text = { stringResource(R.string.ly_img_editor_navigation_bar_button_design) },
            )
        }
    }

    aligned(alignment = Alignment.CenterHorizontally) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
    }

    aligned(alignment = Alignment.End) {
        add {
            NavigationBar.Button.rememberNextPage(
                text = { stringResource(R.string.ly_img_editor_navigation_bar_button_write) },
            )
        }
        add { NavigationBar.Button.rememberExport() }
    }
}
```

```kotlin file=@cesdk_android_examples/editor-guides-configuration-navigation-bar/ModifyListBuilderNavigationBarSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.NavigationBar
import ly.img.editor.core.component.export
import ly.img.editor.core.component.redo
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.component.togglePagesMode
import ly.img.editor.core.component.undo
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ModifyListBuilderNavigationBarSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        navigationBar = {
            NavigationBar.remember(
                listBuilder = NavigationBar.ListBuilder.rememberForDesign().modify {
                    addFirst(alignment = Alignment.End) {
                        NavigationBar.Button.remember(
                            id = EditorComponentId("my.package.navigationBar.button.endAligned.first"),
                            vectorIcon = { IconPack.Music },
                            text = { "First Button" },
                            onClick = {},
                        )
                    }
                    addLast(alignment = Alignment.End) {
                        NavigationBar.Button.remember(
                            id = EditorComponentId("my.package.navigationBar.button.endAligned.last"),
                            vectorIcon = { IconPack.Music },
                            text = { "Last Button" },
                            onClick = {},
                        )
                    }
                    addAfter(id = NavigationBar.Button.Id.redo) {
                        NavigationBar.Button.remember(
                            id = EditorComponentId("my.package.navigationBar.button.afterRedo"),
                            vectorIcon = { IconPack.Music },
                            text = { "After Redo" },
                            onClick = {},
                        )
                    }
                    addBefore(id = NavigationBar.Button.Id.undo) {
                        NavigationBar.Button.remember(
                            id = EditorComponentId("my.package.navigationBar.button.beforeUndo"),
                            vectorIcon = { IconPack.Music },
                            text = { "Before Undo" },
                            onClick = {},
                        )
                    }
                    replace(id = NavigationBar.Button.Id.export) {
                        NavigationBar.Button.remember(
                            id = EditorComponentId("my.package.navigationBar.button.replacedExport"),
                            vectorIcon = null,
                            text = { "Replaced Export" },
                            onClick = {},
                        )
                    }
                    remove(id = NavigationBar.Button.Id.togglePagesMode)
                },
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-navigation-bar/NavigationBarItems.kt reference-only
import android.widget.Toast
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import ly.img.editor.ShowLoading
import ly.img.editor.core.LocalEditorScope
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.NavigationBar
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.core.sheet.SheetType

@Composable
fun rememberNavigationBarButton() = NavigationBar.Button.remember(
    id = EditorComponentId("my.package.navigationBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { NavigationBar.ButtonScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    // default value is { it() }
    decoration = {
        Surface(color = MaterialTheme.colorScheme.background) {
            it()
        }
    },
    onClick = { editorContext.eventHandler.send(EditorEvent.Sheet.Open(SheetType.Volume())) },
    // default value is null
    icon = {
        Icon(
            imageVector = IconPack.Music,
            contentDescription = null,
        )
    },
    // default value is null
    text = {
        Text(
            text = "Hello World",
        )
    },
    enabled = { true },
)

@Composable
fun rememberNavigationBarButtonSimpleOverload() = NavigationBar.Button.remember(
    id = EditorComponentId("my.package.navigationBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { NavigationBar.ButtonScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    decoration = {
        Surface(color = MaterialTheme.colorScheme.background) {
            it()
        }
    },
    onClick = { editorContext.eventHandler.send(ShowLoading) },
    vectorIcon = { IconPack.Music }, // default value is null
    text = { "Hello World" }, // default value is null
    tint = null,
    enabled = { true },
    contentDescription = null,
)

@Composable
fun rememberNavigationBarCustomItem() = NavigationBar.Custom.remember(
    id = EditorComponentId("my.package.navigationBar.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { NavigationBar.ItemScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
) {
    Box(
        modifier = Modifier
            .fillMaxHeight()
            .clickable {
                Toast
                    .makeText(editorContext.activity, "Hello World Clicked!", Toast.LENGTH_SHORT)
                    .show()
            },
    ) {
        Text(
            modifier = Modifier.align(Alignment.Center),
            text = "Hello World",
        )
    }
}
```

The navigation bar serves as the primary control interface at the top of the editor, housing essential functions like session management (close/save), editing operations (undo/redo), mode switching, and export capabilities. This guide shows you how to customize the navigation layout, button placement, and functionality to align with your app's information architecture and user flow patterns. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-navigation-bar).

## Navigation Bar Architecture

![Navigation Bar on Android](./assets/navigation-bar-android.png)

The navigation bar displays horizontally at the top of the editor, with items organized into alignment groups: start (left), center, and end (right).

**Key Components:**

- **`NavigationBar.Item`** - Abstract class that all navigation bar items inherit from
- **`NavigationBar.Button`** - Pre-built button implementation with icon and text
- **`NavigationBar.Custom`** - Fully custom component for arbitrary content rendering
- **`NavigationBar.Scope`** - Provides access to the engine, event handler, and editor state
- **Alignment Groups** - Container system that positions items by alignment (start, center, end)

## Configuration

Navigation bar customization is part of the `EditorConfiguration`, therefore, in order to configure the navigation bar we need to configure the `EditorConfiguration`. Below you can find the list of available configurations of the navigation bar. To demonstrate the default values, all parameters are assigned to their default values.

**Available configuration parameters:**

- **`scope`** - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the navigation bar. Prefer updating individual `NavigationBar.Item`s over updating the whole navigation bar. Ideally, scope should be updated when the parent scope (scope of the parent component) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent scope (accessed via `LocalEditorScope`) is updated.

- **`visible`** - Control navigation bar visibility. Default value is always true.

- **`enterTransition`** - Animation for when the navigation bar appears. Default value is always no enter transition.

- **`exitTransition`** - Animation for when the navigation bar disappears. Default value is always no exit transition.

- **`decoration`** - Apply custom styling like background, shadows, and padding. Default value is always no decoration.

- **`listBuilder`** - Define the complete list of navigation bar items and their alignment groups. Items are only displayed when `visible` returns `true`. By default, `listBuilder` does not add anything to the navigation bar.

- **`horizontalArrangement`** - Layout arrangement for navigation bar items. Controls spacing and alignment of items within the navigation bar. Default value is `Arrangement.SpaceEvenly`.

- **`itemDecoration`** - decoration of the items in the navigation bar. Useful when you want to add custom background, foreground, shadow, paddings etc to the items. Prefer using this decoration when you want to apply the same decoration to all the items, otherwise set decoration to individual items. Default value is always no decoration.

```kotlin highlight-navigationBarConfiguration
val editorConfiguration = EditorConfiguration.rememberForDesign(
    navigationBar = {
        NavigationBar.remember(
            scope = LocalEditorScope.current.run {
                remember(this) { NavigationBar.Scope(parentScope = this) }
            },
            visible = { true },
            enterTransition = { EnterTransition.None },
            exitTransition = { ExitTransition.None },
            decoration = {
                // Also available via NavigationBar.DefaultDecoration
                Box(
                    modifier =
                        Modifier
                            .fillMaxWidth()
                            .heightIn(min = 64.dp)
                            .background(MaterialTheme.colorScheme.surface)
                            .padding(PaddingValues(horizontal = 4.dp)),
                    contentAlignment = Alignment.Center,
                ) {
                    it()
                }
            },
            listBuilder = NavigationBar.ListBuilder.remember { },
            horizontalArrangement = { Arrangement.SpaceEvenly },
            // default value is { it() }
            itemDecoration = {
                Box(modifier = Modifier.padding(2.dp)) {
                    it()
                }
            },
        )
    },
)
```

### ListBuilder Configuration

You can configure the complete item list or modify the default items using two main approaches:

**Available approaches:**

- **`NavigationBar.ListBuilder.rememberForDesign()`** - Use the recommended default configuration for your editor solution (Design, Photo, Video, Apparel, Postcard). Each solution has optimized defaults for its workflow.

- **`NavigationBar.ListBuilder.rememberForDesign().modify()`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration. Use this when you want to keep most defaults but make targeted changes.

The `NavigationBar.Scope` provides access to the engine, event handler, and editor state. Use this for advanced customization logic and to maintain consistency with the current editor state. Items are organized into alignment groups for consistent positioning across different screen sizes.

### Default Navigation Bar Items

Each editor solution has its own default navigation bar configuration optimized for its workflow:

**Design Editor**:

```kotlin highlight-listBuilders-design
@Composable
fun NavigationBar.ListBuilder.rememberForDesign() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePagesMode() }
        add { NavigationBar.Button.rememberExport() }
    }
}
```

**Photo Editor**:

```kotlin highlight-listBuilders-photo
@Composable
fun NavigationBar.ListBuilder.rememberForPhoto() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
        add { NavigationBar.Button.rememberExport() }
    }
}
```

**Video Editor**:

```kotlin highlight-listBuilders-video
@Composable
fun NavigationBar.ListBuilder.rememberForVideo() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberExport() }
    }
}
```

**Apparel Editor**:

```kotlin highlight-listBuilders-apparel
@Composable
fun NavigationBar.ListBuilder.rememberForApparel() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
    }
    aligned(alignment = Alignment.CenterHorizontally) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
    }
    aligned(alignment = Alignment.End) {
        add { NavigationBar.Button.rememberExport() }
    }
}
```

**Postcard Editor**:

```kotlin highlight-listBuilders-postcard
@Composable
fun NavigationBar.ListBuilder.rememberForPostcard() = NavigationBar.ListBuilder.remember {
    aligned(alignment = Alignment.Start) {
        add { NavigationBar.Button.rememberCloseEditor() }
        add {
            NavigationBar.Button.rememberPreviousPage(
                text = { stringResource(R.string.ly_img_editor_navigation_bar_button_design) },
            )
        }
    }

    aligned(alignment = Alignment.CenterHorizontally) {
        add { NavigationBar.Button.rememberUndo() }
        add { NavigationBar.Button.rememberRedo() }
        add { NavigationBar.Button.rememberTogglePreviewMode() }
    }

    aligned(alignment = Alignment.End) {
        add {
            NavigationBar.Button.rememberNextPage(
                text = { stringResource(R.string.ly_img_editor_navigation_bar_button_write) },
            )
        }
        add { NavigationBar.Button.rememberExport() }
    }
}
```

### Modify Navigation Bar Items

Use the `modify` function to adjust the default item list without rebuilding the entire configuration:

```kotlin highlight-modifyListBuilderSignature
listBuilder = NavigationBar.ListBuilder.rememberForDesign().modify {
```

**Available modification operations:**

- `addFirst` - prepends a new item at the beginning of an alignment group:

```kotlin highlight-modifyListBuilder-addFirst
addFirst(alignment = Alignment.End) {
    NavigationBar.Button.remember(
        id = EditorComponentId("my.package.navigationBar.button.endAligned.first"),
        vectorIcon = { IconPack.Music },
        text = { "First Button" },
        onClick = {},
    )
}
```

- `addLast` - appends a new item at the end of an alignment group:

```kotlin highlight-modifyListBuilder-addLast
addLast(alignment = Alignment.End) {
    NavigationBar.Button.remember(
        id = EditorComponentId("my.package.navigationBar.button.endAligned.last"),
        vectorIcon = { IconPack.Music },
        text = { "Last Button" },
        onClick = {},
    )
}
```

- `addAfter` - adds a new item right after a specific item:

```kotlin highlight-modifyListBuilder-addAfter
addAfter(id = NavigationBar.Button.Id.redo) {
    NavigationBar.Button.remember(
        id = EditorComponentId("my.package.navigationBar.button.afterRedo"),
        vectorIcon = { IconPack.Music },
        text = { "After Redo" },
        onClick = {},
    )
}
```

- `addBefore` - adds a new item right before a specific item:

```kotlin highlight-modifyListBuilder-addBefore
addBefore(id = NavigationBar.Button.Id.undo) {
    NavigationBar.Button.remember(
        id = EditorComponentId("my.package.navigationBar.button.beforeUndo"),
        vectorIcon = { IconPack.Music },
        text = { "Before Undo" },
        onClick = {},
    )
}
```

- `replace` - replaces an existing item with a new item:

```kotlin highlight-modifyListBuilder-replace
replace(id = NavigationBar.Button.Id.export) {
    NavigationBar.Button.remember(
        id = EditorComponentId("my.package.navigationBar.button.replacedExport"),
        vectorIcon = null,
        text = { "Replaced Export" },
        onClick = {},
    )
}
```

- `remove` - removes an existing item:

```kotlin highlight-modifyListBuilder-remove
remove(id = NavigationBar.Button.Id.togglePagesMode)
```

> **Note:** **Warning**\
> Note that the order of items may change between editor versions, therefore `modify` must be used with care. Consider creating a new builder if you want to have strict ordering between different editor versions.

## NavigationBar.Item Configuration

Each `NavigationBar.Item` is an `EditorComponent`. Its `id` must be unique which is a requirement for proper component management. Items must be organized within alignment groups when using the aligned layout system.

### Use Predefined Buttons

Start with predefined buttons which are provided as composable functions. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/#list-of-available-navigationbarbuttons).

### Create New Buttons

Create custom buttons when predefined options don't meet your needs:

```kotlin highlight-navigationBarItems-newButton
@Composable
fun rememberNavigationBarButton() = NavigationBar.Button.remember(
    id = EditorComponentId("my.package.navigationBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { NavigationBar.ButtonScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    // default value is { it() }
    decoration = {
        Surface(color = MaterialTheme.colorScheme.background) {
            it()
        }
    },
    onClick = { editorContext.eventHandler.send(EditorEvent.Sheet.Open(SheetType.Volume())) },
    // default value is null
    icon = {
        Icon(
            imageVector = IconPack.Music,
            contentDescription = null,
        )
    },
    // default value is null
    text = {
        Text(
            text = "Hello World",
        )
    },
    enabled = { true },
)
```

**Required and optional parameters:**

- `id` - the id of the button. Note that it is highly recommended that every unique `EditorComponent` has a unique id. Parameter does not have a default value.

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the button. Ideally, scope should be updated when the parent scope (scope of the parent component `NavigationBar` - `NavigationBar.Scope`) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent component scope (accessed via `LocalEditorScope`) is updated.

- `visible` - whether the button should be visible. Default value is always true.

- `enterTransition` - transition of the button when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the button when it exits the parent composable. Default value is always no exit transition.

- `decoration` - decoration of the button. Useful when you want to add custom background, foreground, shadow, paddings etc. Default value is always no decoration.

- `onClick` - the callback that is invoked when the button is clicked. Parameter does not have a default value.

- `icon` - the icon content of the button. If null, it will not be rendered. Default value is null.

- `text` - the text content of the button. If null, it will not be rendered. Default value is null.

- `tint` - the tint color of the content. If null, then no tint is applied. Default value is null.

- `enabled` - whether the button is enabled. Default value is always true.

Other than the main `NavigationBar.Button.remember` function, there is one more convenience overload that has three differences:

1. `icon` is replaced with `vectorIcon` lambda, that returns `VectorIcon` instead of drawing the icon content.
2. `text` is replaced with `text` lambda, that returns `String` instead of drawing the text content.
3. An extra parameter `contentDescription` is added that is used by accessibility services to describe what the button does. Note that it is not required to provide value when `text` is not null, since its value will be used by accessibility services, however having both `text` and `contentDescription` as null will cause a crash.

### Create Custom Items

For completely custom implementations, use `NavigationBar.Custom` to render arbitrary content:

```kotlin highlight-navigationBarItems-newCustomItem
@Composable
fun rememberNavigationBarCustomItem() = NavigationBar.Custom.remember(
    id = EditorComponentId("my.package.navigationBar.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { NavigationBar.ItemScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
) {
    Box(
        modifier = Modifier
            .fillMaxHeight()
            .clickable {
                Toast
                    .makeText(editorContext.activity, "Hello World Clicked!", Toast.LENGTH_SHORT)
                    .show()
            },
    ) {
        Text(
            modifier = Modifier.align(Alignment.Center),
            text = "Hello World",
        )
    }
}
```

**Required and optional parameters:**

- `id` - the unique id of the custom item. Note that it is highly recommended that every unique `EditorComponent` has a unique id. Parameter does not have a default value.

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the custom item. Ideally, scope should be updated when the parent scope (scope of the parent component `NavigationBar` - `NavigationBar.Scope`) is updated and when you want to observe changes from the `Engine`. Parameter does not have a default value.

- `visible` - whether the custom item should be visible. Default value is always true.

- `enterTransition` - transition of the custom item when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the custom item when it exits the parent composable. Default value is always no exit transition.

- `content` - the content of the custom item. You are responsible for drawing it, handling clicks etc. Parameter does not have a default value.

### Alignment Groups

When using alignment groups, items are positioned in three areas:

- **`Alignment.Start`** - Items aligned to the start (left) of the navigation bar
- **`Alignment.CenterHorizontally`** - Items centered in the navigation bar
- **`Alignment.End`** - Items aligned to the end (right) of the navigation bar

```kotlin
aligned(alignment = Alignment.Start) {
    add { NavigationBar.Button.rememberCloseEditor() }
}
aligned(alignment = Alignment.End) {
    add { NavigationBar.Button.rememberExport() }
}
```

> **Note:** **Warning** It is not allowed to add items both inside and outside align
> blocks at the same time: either all items should be in aligned groups, or no
> items at all.

### List of Available NavigationBar.Buttons

All predefined buttons are available as composable functions in the `NavigationBar.Button` namespace. Each function returns a `NavigationBar.Button` with default parameters that you can customize as shown in the [Create New Buttons](https://img.ly/docs/cesdk/android/user-interface/customization/navigation-bar-4e5d39/#create-new-buttons) section.

| Button                                           | Id                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NavigationBar.Button.rememberCloseEditor`       | `NavigationBar.Button.Id.closeEditor`       | Triggers [EngineConfiguration.onClose](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) callback via `EditorEvent.OnClose`.                                                                                                                                                                                                                                                                                                                                |
| `NavigationBar.Button.rememberUndo`              | `NavigationBar.Button.Id.undo`              | Does undo operation in the editor via [EditorApi.undo](https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/) engine API.                                                                                                                                                                                                                                                                                                                                        |
| `NavigationBar.Button.rememberRedo`              | `NavigationBar.Button.Id.redo`              | Does redo operation in the editor via [EditorApi.redo](https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/) engine API.                                                                                                                                                                                                                                                                                                                                        |
| `NavigationBar.Button.rememberExport`            | `NavigationBar.Button.Id.export`            | Triggers [EngineConfiguration.onExport](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) callback via `EditorEvent.Export`.                                                                                                                                                                                                                                                                                                                                |
| `NavigationBar.Button.rememberTogglePreviewMode` | `NavigationBar.Button.Id.togglePreviewMode` | Updates editor view mode via `EditorEvent.SetViewMode`: when current view mode is `EditorViewMode.Edit`, then `EditorViewMode.Preview` is set and vice versa. Note that this button is intended to be used in Photo Editor, Apparel Editor and Postcard Editor and may cause unexpected behaviors when used in other solutions. |
| `NavigationBar.Button.rememberTogglePagesMode`   | `NavigationBar.Button.Id.togglePagesMode`   | Updates editor view mode via `EditorEvent.SetViewMode`: when current view mode is `EditorViewMode.Edit`, then `EditorViewMode.Pages` is set and vice versa. Note that this button is intended to be used in Design Editor and may cause unexpected behaviors when used in other solutions.                                                                                                              |
| `NavigationBar.Button.rememberPreviousPage`      | `NavigationBar.Button.Id.previousPage`      | Navigates to the previous page via `EditorEvent.Navigation.ToPreviousPage`.                                                                                                                                                                                                                                                                                                                                                                 |
| `NavigationBar.Button.rememberNextPage`          | `NavigationBar.Button.Id.nextPage`          | Navigates to the next page via `EditorEvent.Navigation.ToNextPage`.                                                                                                                                                                                                                                                                                                                                                                         |



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
