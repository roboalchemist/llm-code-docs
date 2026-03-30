# Source: https://img.ly/docs/cesdk/android/user-interface/customization/canvas-menu-0d2b5b/

---
title: "Canvas Menu"
description: "Control visibility and options in the canvas context menu."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/canvas-menu-0d2b5b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Canvas Menu](https://img.ly/docs/cesdk/android/user-interface/customization/canvas-menu-0d2b5b/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-canvas-menu/SimpleCanvasMenuSolution.kt reference-only
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.CanvasMenu
import ly.img.editor.core.component.CanvasMenu.Companion.DefaultDecoration
import ly.img.editor.rememberForDesign
import ly.img.engine.DesignBlockType

// Add this composable to your NavHost
@Composable
fun SimpleCanvasMenuSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        canvasMenu = {
            CanvasMenu.remember(
                // Implementation is too large, check the implementation of CanvasMenu.defaultScope
                scope = CanvasMenu.defaultScope,
                visible = {
                    val editorState by editorContext.state.collectAsState()
                    remember(this, editorState) {
                        editorState.isTouchActive.not() &&
                            editorState.activeSheet == null &&
                            editorContext.safeSelection != null &&
                            editorContext.selection.type != DesignBlockType.Page &&
                            editorContext.selection.type != DesignBlockType.Audio &&
                            editorContext.engine.editor.getEditMode() != "Text" &&
                            editorContext.isScenePlaying.not() &&
                            editorContext.selection.isVisibleAtCurrentPlaybackTime
                    }
                },
                enterTransition = { EnterTransition.None },
                exitTransition = { ExitTransition.None },
                // Implementation is too large, check the implementation of CanvasMenu.DefaultDecoration
                decoration = { DefaultDecoration { it() } },
                listBuilder = CanvasMenu.ListBuilder.remember(),
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-canvas-menu/CanvasMenuListBuilders.kt reference-only
import androidx.compose.runtime.Composable
import ly.img.editor.core.component.CanvasMenu
import ly.img.editor.core.component.rememberBringForward
import ly.img.editor.core.component.rememberDelete
import ly.img.editor.core.component.rememberDuplicate
import ly.img.editor.core.component.rememberSelectGroup
import ly.img.editor.core.component.rememberSendBackward

@Composable
fun CanvasMenu.ListBuilder.remember() = CanvasMenu.ListBuilder.remember {
    add { CanvasMenu.Button.rememberSelectGroup() }
    add { CanvasMenu.Divider.remember(visible = { editorContext.isSelectionInGroup }) }
    add { CanvasMenu.Button.rememberBringForward() }
    add { CanvasMenu.Button.rememberSendBackward() }
    add { CanvasMenu.Divider.remember(visible = { editorContext.canSelectionMove }) }
    add { CanvasMenu.Button.rememberDuplicate() }
    add { CanvasMenu.Button.rememberDelete() }
}
```

```kotlin file=@cesdk_android_examples/editor-guides-configuration-canvas-menu/ModifyListBuilderCanvasMenuSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.CanvasMenu
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.bringForward
import ly.img.editor.core.component.delete
import ly.img.editor.core.component.duplicate
import ly.img.editor.core.component.rememberDuplicate
import ly.img.editor.core.component.sendBackward
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ModifyListBuilderCanvasMenuSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        canvasMenu = {
            CanvasMenu.remember(
                listBuilder = CanvasMenu.ListBuilder.remember().modify {
                    addFirst {
                        CanvasMenu.Button.remember(
                            id = EditorComponentId("my.package.canvasMenu.button.first"),
                            vectorIcon = null,
                            text = { "First Button" },
                            onClick = {},
                        )
                    }
                    addLast {
                        CanvasMenu.Button.remember(
                            id = EditorComponentId("my.package.canvasMenu.button.last"),
                            vectorIcon = null,
                            text = { "Last Button" },
                            onClick = {},
                        )
                    }
                    addAfter(id = CanvasMenu.Button.Id.bringForward) {
                        CanvasMenu.Button.remember(
                            id = EditorComponentId("my.package.canvasMenu.button.afterBringForward"),
                            vectorIcon = null,
                            text = { "After Bring Forward" },
                            onClick = {},
                        )
                    }
                    addBefore(id = CanvasMenu.Button.Id.sendBackward) {
                        CanvasMenu.Button.remember(
                            id = EditorComponentId("my.package.canvasMenu.button.beforeSendBackward"),
                            vectorIcon = null,
                            text = { "Before Send Backward" },
                            onClick = {},
                        )
                    }
                    replace(id = CanvasMenu.Button.Id.duplicate) {
                        // Note that it can be replaced with a component that has a different id.
                        CanvasMenu.Button.rememberDuplicate(
                            vectorIcon = { IconPack.Music },
                        )
                    }
                    remove(id = CanvasMenu.Button.Id.delete)
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-canvas-menu/CanvasMenuItems.kt reference-only
import android.widget.Toast
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import ly.img.editor.ShowLoading
import ly.img.editor.core.LocalEditorScope
import ly.img.editor.core.component.CanvasMenu
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.core.sheet.SheetType

@Composable
fun rememberCanvasMenuButton() = CanvasMenu.Button.remember(
    id = EditorComponentId("my.package.canvasMenu.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.ButtonScope(parentScope = this) }
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
fun rememberCanvasMenuButtonSimpleOverload() = CanvasMenu.Button.remember(
    id = EditorComponentId("my.package.canvasMenu.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.ButtonScope(parentScope = this) }
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
fun rememberCanvasMenuDivider() = CanvasMenu.Divider.remember(
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.DividerScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    decoration = { it() },
    modifier = {
        remember(this) {
            Modifier
                .padding(horizontal = 8.dp)
                .size(width = 1.dp, height = 24.dp)
        }
    },
)

@Composable
fun rememberCanvasMenuCustomItem() = CanvasMenu.Custom.remember(
    id = EditorComponentId("my.package.canvasMenu.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.ItemScope(parentScope = this) }
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

The canvas menu provides immediate access to frequently-used actions when you select a design element, offering operations like duplicate, delete, layer reordering, and grouping controls directly on the canvas. This guide shows you how to customize these contextual actions to streamline your users' editing workflow and match your app's feature priorities. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-canvas-menu).

## Canvas Menu Architecture

![Canvas Menu](./assets/canvas-menu-android.png)

The canvas menu displays horizontally when a design element is selected, offering quick access to editing actions relevant to that element type.

**Key Components:**

- **`CanvasMenu.Item`** - Abstract class that all canvas menu items inherit from
- **`CanvasMenu.Button`** - Pre-built button implementation with icon and text
- **`CanvasMenu.Divider`** - Visual separator between menu groups
- **`CanvasMenu.Custom`** - Fully custom component for arbitrary content rendering
- **`CanvasMenu.Scope`** - Provides access to the engine, event handler, and selected element

## Configuration

Canvas menu customization is part of the `EditorConfiguration`, therefore, in order to configure the canvas menu we need to configure the `EditorConfiguration`. Below you can find the list of available configurations of the canvas menu. To demonstrate the default values, all parameters are assigned to their default values.

**Available configuration parameters:**

- **`scope`** - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the canvas menu. Prefer updating individual `CanvasMenu.Item`s over updating the whole canvas menu. Ideally, scope should be updated when the parent scope (scope of the parent component) is updated and when you want to observe changes from the `Engine`. By default, the scope is updated when the parent scope (accessed via `LocalEditorScope`) is updated, when selection is changed to a different design block (or unselected), and when the parent of the currently selected design block is changed to a different design block.

- **`visible`** - Control canvas menu visibility based on selection state and editor conditions. By default the value is true when a design block is selected, it is not part of a group, canvas is not moving (finger is not on canvas), selected design block does not have a type `DesignBlockType.Audio` or `DesignBlockType.Page`, no sheet is displayed currently and the keyboard is not visible. In addition, selected design block should be visible at current playback time and containing scene should be on pause if design block is selected in a video scene.

- **`enterTransition`** - Animation for when the canvas menu appears. Default value is always no enter transition.

- **`exitTransition`** - Animation for when the canvas menu disappears. Default value is always no exit transition.

- **`decoration`** - Apply custom styling like background, shadows, and positioning relative to the selected element. The default decoration adds background color, applies rounded corners and positions the list of items next to the selected design block.

- **`listBuilder`** - Define the complete list of canvas menu items and their order. Items are only displayed when `visible` returns `true`.

- **`itemDecoration`** - decoration of the items in the canvas menu. Useful when you want to add custom background, foreground, shadow, paddings etc to the items. Prefer using this decoration when you want to apply the same decoration to all the items, otherwise set decoration to individual items. Default value is always no decoration.

```kotlin highlight-canvasMenuConfiguration
val editorConfiguration = EditorConfiguration.rememberForDesign(
    canvasMenu = {
        CanvasMenu.remember(
            // Implementation is too large, check the implementation of CanvasMenu.defaultScope
            scope = CanvasMenu.defaultScope,
            visible = {
                val editorState by editorContext.state.collectAsState()
                remember(this, editorState) {
                    editorState.isTouchActive.not() &&
                        editorState.activeSheet == null &&
                        editorContext.safeSelection != null &&
                        editorContext.selection.type != DesignBlockType.Page &&
                        editorContext.selection.type != DesignBlockType.Audio &&
                        editorContext.engine.editor.getEditMode() != "Text" &&
                        editorContext.isScenePlaying.not() &&
                        editorContext.selection.isVisibleAtCurrentPlaybackTime
                }
            },
            enterTransition = { EnterTransition.None },
            exitTransition = { ExitTransition.None },
            // Implementation is too large, check the implementation of CanvasMenu.DefaultDecoration
            decoration = { DefaultDecoration { it() } },
            listBuilder = CanvasMenu.ListBuilder.remember(),
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

- **`CanvasMenu.ListBuilder.remember()`** - Define the complete list of canvas menu items from scratch. Use this when you want full control over the canvas menu configuration.

- **`CanvasMenu.ListBuilder.remember().modify()`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration. Use this when you want to keep most defaults but make targeted changes.

The `CanvasMenu.Scope` provides access to the engine, event handler, and selected element state. Use this for advanced customization logic and to maintain consistency with the current editor context.

### Default Canvas Menu Items

The default configuration includes essential editing actions with logical grouping:

```kotlin highlight-listBuilders
@Composable
fun CanvasMenu.ListBuilder.remember() = CanvasMenu.ListBuilder.remember {
    add { CanvasMenu.Button.rememberSelectGroup() }
    add { CanvasMenu.Divider.remember(visible = { editorContext.isSelectionInGroup }) }
    add { CanvasMenu.Button.rememberBringForward() }
    add { CanvasMenu.Button.rememberSendBackward() }
    add { CanvasMenu.Divider.remember(visible = { editorContext.canSelectionMove }) }
    add { CanvasMenu.Button.rememberDuplicate() }
    add { CanvasMenu.Button.rememberDelete() }
}
```

### Modify Canvas Menu Items

Use the `modify` function to adjust the default item list without rebuilding the entire configuration:

```kotlin highlight-modifyListBuilderSignature
listBuilder = CanvasMenu.ListBuilder.remember().modify {
```

**Available modification operations:**

- `addFirst` - prepends a new item at the beginning:

```kotlin highlight-modifyListBuilder-addFirst
addFirst {
    CanvasMenu.Button.remember(
        id = EditorComponentId("my.package.canvasMenu.button.first"),
        vectorIcon = null,
        text = { "First Button" },
        onClick = {},
    )
}
```

- `addLast` - appends a new item at the end:

```kotlin highlight-modifyListBuilder-addLast
addLast {
    CanvasMenu.Button.remember(
        id = EditorComponentId("my.package.canvasMenu.button.last"),
        vectorIcon = null,
        text = { "Last Button" },
        onClick = {},
    )
}
```

- `addAfter` - adds a new item right after a specific item:

```kotlin highlight-modifyListBuilder-addAfter
addAfter(id = CanvasMenu.Button.Id.bringForward) {
    CanvasMenu.Button.remember(
        id = EditorComponentId("my.package.canvasMenu.button.afterBringForward"),
        vectorIcon = null,
        text = { "After Bring Forward" },
        onClick = {},
    )
}
```

- `addBefore` - adds a new item right before a specific item:

```kotlin highlight-modifyListBuilder-addBefore
addBefore(id = CanvasMenu.Button.Id.sendBackward) {
    CanvasMenu.Button.remember(
        id = EditorComponentId("my.package.canvasMenu.button.beforeSendBackward"),
        vectorIcon = null,
        text = { "Before Send Backward" },
        onClick = {},
    )
}
```

- `replace` - replaces an existing item with a new item:

```kotlin highlight-modifyListBuilder-replace
replace(id = CanvasMenu.Button.Id.duplicate) {
    // Note that it can be replaced with a component that has a different id.
    CanvasMenu.Button.rememberDuplicate(
        vectorIcon = { IconPack.Music },
    )
}
```

- `remove` - removes an existing item:

```kotlin highlight-modifyListBuilder-remove
remove(id = CanvasMenu.Button.Id.delete)
```

> **Note:** **Warning** Note that the order of items may change between editor versions,
> therefore `modify` must be used with care. Consider creating a new builder if
> you want to have strict ordering between different editor versions.

## CanvasMenu.Item Configuration

Each `CanvasMenu.Item` is an `EditorComponent`. Its `id` must be unique which is a requirement for proper component management.
You have multiple options for creating canvas menu items, from simple predefined buttons to fully custom implementations.

### Use Predefined Buttons

Start with predefined buttons which are provided as composable functions. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/android/user-interface/customization/canvas-menu-0d2b5b/#list-of-available-canvasmenubuttons).

### Create New Buttons

Create custom buttons when predefined options don't meet your needs:

```kotlin highlight-canvasMenuItems-newButton
@Composable
fun rememberCanvasMenuButton() = CanvasMenu.Button.remember(
    id = EditorComponentId("my.package.canvasMenu.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.ButtonScope(parentScope = this) }
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

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the button. Ideally, scope should be updated when the parent scope (scope of the parent component `CanvasMenu` - `CanvasMenu.Scope`) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent component scope (`CanvasMenu.scope`, accessed via `LocalEditorScope`) is updated.

- `visible` - whether the button should be visible. Default value is always true.

- `enterTransition` - transition of the button when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the button when it exits the parent composable. Default value is always no exit transition.

- `decoration` - decoration of the button. Useful when you want to add custom background, foreground, shadow, paddings etc. Default value is always no decoration.

- `onClick` - the callback that is invoked when the button is clicked. Parameter does not have a default value.

- `icon` - the icon content of the button. If null, it will not be rendered. Default value is null.

- `text` - the text content of the button. If null, it will not be rendered. Default value is null.

- `tint` - the tint color of the content. If null, then no tint is applied. Default value is null.

- `enabled` - whether the button is enabled. Default value is always true.

Other than the main `CanvasMenu.Button.remember` function, there is one more convenience overload that has three differences:

1. `icon` is replaced with `vectorIcon` lambda, that returns `VectorIcon` instead of drawing the icon content.
2. `text` is replaced with `text` lambda, that returns `String` instead of drawing the text content.
3. An extra parameter `contentDescription` is added that is used by accessibility services to describe what the button does. Note that it is not required to provide value when `text` is not null, since its value will be used by accessibility services, however having both `text` and `contentDescription` as null will cause a crash.

### Create Dividers

Use dividers to visually separate groups of related actions:

```kotlin highlight-canvasMenuItems-newDivider
@Composable
fun rememberCanvasMenuDivider() = CanvasMenu.Divider.remember(
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.DividerScope(parentScope = this) }
    },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    decoration = { it() },
    modifier = {
        remember(this) {
            Modifier
                .padding(horizontal = 8.dp)
                .size(width = 1.dp, height = 24.dp)
        }
    },
)
```

**Required and optional parameters:**

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the divider. Ideally, scope should be updated when the parent scope (scope of the parent component `CanvasMenu` - `CanvasMenu.Scope`) is updated and when you want to observe changes from the `Engine`. Parameter does not have a default value.

- `visible` - whether the divider should be visible. Default value is always true.

- `enterTransition` - transition of the divider when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the divider when it exits the parent composable. Default value is always no exit transition.

- `decoration` - decoration of the divider. Useful when you want to add custom background, foreground, shadow, paddings etc. Default value is always no decoration.

- `modifier` - the modifier of the divider. Default value is always a `Modifier` that sets size and paddings to the divider.

### Create Custom Items

For completely custom implementations, use `CanvasMenu.Custom` to render arbitrary content:

```kotlin highlight-canvasMenuItems-newCustomItem
@Composable
fun rememberCanvasMenuCustomItem() = CanvasMenu.Custom.remember(
    id = EditorComponentId("my.package.canvasMenu.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { CanvasMenu.ItemScope(parentScope = this) }
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

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the custom item. Ideally, scope should be updated when the parent scope (scope of the parent component `CanvasMenu` - `CanvasMenu.Scope`) is updated and when you want to observe changes from the `Engine`. Parameter does not have a default value.

- `visible` - whether the custom item should be visible. Default value is always true.

- `enterTransition` - transition of the custom item when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the custom item when it exits the parent composable. Default value is always no exit transition.

- `content` - the content of the custom item. You are responsible for drawing it, handling clicks etc. Parameter does not have a default value.

### List of Available CanvasMenu.Buttons

All predefined buttons are available as composable functions in the `CanvasMenu.Button` namespace. Each function returns a `CanvasMenu.Button` with default parameters that you can customize as shown in the [Create New Buttons](https://img.ly/docs/cesdk/android/user-interface/customization/canvas-menu-0d2b5b/#create-new-buttons) section.

| Button                                   | ID                                  | Description                                                                                                               |
| ---------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `CanvasMenu.Button.rememberBringForward` | `CanvasMenu.Button.Id.bringForward` | Brings forward currently selected design block via `EditorEvent.Selection.BringForward`.                                  |
| `CanvasMenu.Button.rememberSendBackward` | `CanvasMenu.Button.Id.sendBackward` | Sends backward currently selected design block via `EditorEvent.Selection.SendBackward`.                                  |
| `CanvasMenu.Button.rememberDuplicate`    | `CanvasMenu.Button.Id.duplicate`    | Duplicates currently selected design block via `EditorEvent.Selection.Duplicate`.                                         |
| `CanvasMenu.Button.rememberDelete`       | `CanvasMenu.Button.Id.delete`       | Deletes currently selected design block via `EditorEvent.Selection.Delete`.                                               |
| `CanvasMenu.Button.rememberSelectGroup`  | `CanvasMenu.Button.Id.selectGroup`  | Selects the group design block that contains the currently selected design block via `EditorEvent.Selection.SelectGroup`. |



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
