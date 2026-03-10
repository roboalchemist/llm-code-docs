# Source: https://img.ly/docs/cesdk/android/user-interface/customization/dock-cb916c/

---
title: "Dock"
description: "Configure the dock area to show or hide tools, panels, or quick access actions."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/dock-cb916c/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Dock](https://img.ly/docs/cesdk/android/user-interface/customization/dock-cb916c/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-dock/SimpleDockSolution.kt reference-only
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.LocalEditorScope
import ly.img.editor.core.component.Dock
import ly.img.editor.core.theme.surface1
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun SimpleDockSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = null, // evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.remember(
                scope = LocalEditorScope.current.run {
                    remember(this) { Dock.Scope(parentScope = this) }
                },
                visible = { true },
                enterTransition = { EnterTransition.None },
                exitTransition = { ExitTransition.None },
                decoration = {
                    // Also available via Dock.DefaultDecoration
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(MaterialTheme.colorScheme.surface1.copy(alpha = 0.95f))
                            .padding(vertical = 10.dp),
                    ) {
                        it()
                    }
                },
                listBuilder = Dock.ListBuilder.remember { },
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-dock/DockListBuilders.kt reference-only
import androidx.compose.runtime.Composable
import ly.img.camera.core.CaptureVideo
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.rememberAdjustments
import ly.img.editor.core.component.rememberAudiosLibrary
import ly.img.editor.core.component.rememberBlur
import ly.img.editor.core.component.rememberCrop
import ly.img.editor.core.component.rememberEffect
import ly.img.editor.core.component.rememberElementsLibrary
import ly.img.editor.core.component.rememberFilter
import ly.img.editor.core.component.rememberImagesLibrary
import ly.img.editor.core.component.rememberImglyCamera
import ly.img.editor.core.component.rememberOverlaysLibrary
import ly.img.editor.core.component.rememberReorder
import ly.img.editor.core.component.rememberShapesLibrary
import ly.img.editor.core.component.rememberStickersLibrary
import ly.img.editor.core.component.rememberSystemCamera
import ly.img.editor.core.component.rememberSystemGallery
import ly.img.editor.core.component.rememberTextLibrary

@Composable
fun Dock.ListBuilder.rememberForDesign() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberElementsLibrary() }
    add { Dock.Button.rememberSystemGallery() }
    add { Dock.Button.rememberSystemCamera() }
    add { Dock.Button.rememberImagesLibrary() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberShapesLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
}

@Composable
fun Dock.ListBuilder.rememberForPhoto() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberAdjustments() }
    add { Dock.Button.rememberFilter() }
    add { Dock.Button.rememberEffect() }
    add { Dock.Button.rememberBlur() }
    add { Dock.Button.rememberCrop() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberShapesLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
}

@Composable
fun Dock.ListBuilder.rememberForVideo() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberSystemGallery() }
    add {
            /*
            Make sure to add the gradle dependency of our camera library if you want to use the [rememberImglyCamera] button:
            implementation "ly.img:camera:<same version as editor>".
            If the dependency is missing, then [rememberSystemCamera] is used.
             */
        val isImglyCameraAvailable = androidx.compose.runtime.remember {
            runCatching { CaptureVideo() }.isSuccess
        }
        if (isImglyCameraAvailable) {
            Dock.Button.rememberImglyCamera()
        } else {
            Dock.Button.rememberSystemCamera()
        }
    }
    add { Dock.Button.rememberOverlaysLibrary() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
    add { Dock.Button.rememberAudiosLibrary() }
    add { Dock.Button.rememberReorder() }
}
```

```kotlin file=@cesdk_android_examples/editor-guides-configuration-dock/ModifyListBuilderDockSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.rememberForDesign
import ly.img.editor.core.component.shapesLibrary
import ly.img.editor.core.component.systemCamera
import ly.img.editor.core.component.systemGallery
import ly.img.editor.core.component.textLibrary
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ModifyListBuilderDockSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = null, // evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        dock = {
            Dock.remember(
                listBuilder = Dock.ListBuilder.rememberForDesign().modify {
                    addFirst {
                        Dock.Button.remember(
                            id = EditorComponentId("my.package.dock.button.first"),
                            vectorIcon = null,
                            text = { "First Button" },
                            onClick = {},
                        )
                    }
                    addLast {
                        Dock.Button.remember(
                            id = EditorComponentId("my.package.dock.button.last"),
                            vectorIcon = null,
                            text = { "Last Button" },
                            onClick = {},
                        )
                    }
                    addAfter(id = Dock.Button.Id.systemGallery) {
                        Dock.Button.remember(
                            id = EditorComponentId("my.package.dock.button.afterSystemGallery"),
                            vectorIcon = null,
                            text = { "After System Gallery" },
                            onClick = {},
                        )
                    }
                    addBefore(id = Dock.Button.Id.systemCamera) {
                        Dock.Button.remember(
                            id = EditorComponentId("my.package.dock.button.beforeSystemCamera"),
                            vectorIcon = null,
                            text = { "Before System Camera" },
                            onClick = {},
                        )
                    }
                    replace(id = Dock.Button.Id.textLibrary) {
                        Dock.Button.remember(
                            id = EditorComponentId("my.package.dock.button.replacedTextLibrary"),
                            vectorIcon = null,
                            text = { "Replaced Text Library" },
                            onClick = {},
                        )
                    }
                    remove(id = Dock.Button.Id.shapesLibrary)
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-dock/DockItems.kt reference-only
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
import ly.img.editor.core.component.Dock
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.core.sheet.SheetType

@Composable
fun rememberDockButton() = Dock.Button.remember(
    id = EditorComponentId("my.package.dock.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { Dock.ButtonScope(parentScope = this) }
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
fun rememberDockButtonSimpleOverload() = Dock.Button.remember(
    id = EditorComponentId("my.package.dock.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { Dock.ButtonScope(parentScope = this) }
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
fun rememberCustomItem() = Dock.Custom.remember(
    id = EditorComponentId("my.package.dock.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { Dock.ItemScope(parentScope = this) }
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

The dock provides quick access to content libraries and editing tools, appearing at the bottom of the editor interface. This guide shows you how to customize dock items and their layout to match your app's content strategy and user workflow. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-dock).

## Dock Architecture

![Dock](./assets/dock-android.png)

The dock displays horizontally at the bottom of the editor and provides quick access to content libraries and editing tools. It adapts its content based on the selected editor solution.

**Key Components:**

- **`Dock.Item`** - Abstract class that all dock items inherit from
- **`Dock.Button`** - Pre-built button implementation with icon and text
- **`Dock.Custom`** - Fully custom component for arbitrary content rendering
- **`Dock.Scope`** - Provides access to the engine, event handler, and editor context

## Configuration

Dock customization is part of the `EditorConfiguration`, therefore, in order to configure the dock we need to configure the `EditorConfiguration`. Below you can find the list of available configurations of the dock. To demonstrate the default values, all parameters are assigned to their default values.

**Available configuration parameters:**

- **`scope`** - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the dock. Prefer updating individual `Dock.Item`s over updating the whole dock. Ideally, scope should be updated when the parent scope (scope of the parent component) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent scope (accessed via `LocalEditorScope`) is updated.

- **`visible`** - Control dock visibility. Default value is always true.

- **`enterTransition`** - Animation for when the dock appears. Default value is always no enter transition.

- **`exitTransition`** - Animation for when the dock disappears. Default value is always no exit transition.

- **`decoration`** - Apply custom styling like background, shadows, and padding. The default decoration adds background color and applies paddings to the dock.

- **`listBuilder`** - Define the complete list of dock items and their order. Items are only displayed when `visible` returns `true`. By default, `listBuilder` does not add anything to the dock.

- **`horizontalArrangement`** - Layout arrangement for dock items. Controls spacing and alignment of items within the dock. Default value is `Arrangement.SpaceEvenly`.

- **`itemDecoration`** - decoration of the items in the dock. Useful when you want to add custom background, foreground, shadow, paddings etc to the items. Prefer using this decoration when you want to apply the same decoration to all the items, otherwise set decoration to individual items. Default value is always no decoration.

```kotlin highlight-dockConfiguration
val editorConfiguration = EditorConfiguration.rememberForDesign(
    dock = {
        Dock.remember(
            scope = LocalEditorScope.current.run {
                remember(this) { Dock.Scope(parentScope = this) }
            },
            visible = { true },
            enterTransition = { EnterTransition.None },
            exitTransition = { ExitTransition.None },
            decoration = {
                // Also available via Dock.DefaultDecoration
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(MaterialTheme.colorScheme.surface1.copy(alpha = 0.95f))
                        .padding(vertical = 10.dp),
                ) {
                    it()
                }
            },
            listBuilder = Dock.ListBuilder.remember { },
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

- **`Dock.ListBuilder.rememberForDesign()`** - Use the recommended default configuration for your editor solution (Design, Photo, Video). Each solution has optimized defaults for its workflow.

- **`Dock.ListBuilder.rememberForDesign().modify()`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration. Use this when you want to keep most defaults but make targeted changes.

The `Dock.Scope` provides access to the engine, event handler, and editor context. Use this for advanced customization logic and to maintain consistency with the current editor state.

### Default Dock Items

Each editor solution has its own default dock configuration optimized for its content workflow:

These are the default items recommended to be used with the Design Editor:

```kotlin highlight-listBuilders-design
@Composable
fun Dock.ListBuilder.rememberForDesign() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberElementsLibrary() }
    add { Dock.Button.rememberSystemGallery() }
    add { Dock.Button.rememberSystemCamera() }
    add { Dock.Button.rememberImagesLibrary() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberShapesLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
}
```

These are the default items recommended to be used with the Photo Editor:

```kotlin highlight-listBuilders-photo
@Composable
fun Dock.ListBuilder.rememberForPhoto() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberAdjustments() }
    add { Dock.Button.rememberFilter() }
    add { Dock.Button.rememberEffect() }
    add { Dock.Button.rememberBlur() }
    add { Dock.Button.rememberCrop() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberShapesLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
}
```

These are the default items recommended to be used with the Video Editor:

```kotlin highlight-listBuilders-video
@Composable
fun Dock.ListBuilder.rememberForVideo() = Dock.ListBuilder.remember {
    add { Dock.Button.rememberSystemGallery() }
    add {
            /*
            Make sure to add the gradle dependency of our camera library if you want to use the [rememberImglyCamera] button:
            implementation "ly.img:camera:<same version as editor>".
            If the dependency is missing, then [rememberSystemCamera] is used.
             */
        val isImglyCameraAvailable = androidx.compose.runtime.remember {
            runCatching { CaptureVideo() }.isSuccess
        }
        if (isImglyCameraAvailable) {
            Dock.Button.rememberImglyCamera()
        } else {
            Dock.Button.rememberSystemCamera()
        }
    }
    add { Dock.Button.rememberOverlaysLibrary() }
    add { Dock.Button.rememberTextLibrary() }
    add { Dock.Button.rememberStickersLibrary() }
    add { Dock.Button.rememberAudiosLibrary() }
    add { Dock.Button.rememberReorder() }
}
```

### Modify Dock Items

Use the `modify` function to adjust the default item list without rebuilding the entire configuration:

```kotlin highlight-modifyListBuilderSignature
listBuilder = Dock.ListBuilder.rememberForDesign().modify {
```

**Available modification operations:**

- `addFirst` - prepends new `Dock.Item`:

```kotlin highlight-modifyListBuilder-addFirst
addFirst {
    Dock.Button.remember(
        id = EditorComponentId("my.package.dock.button.first"),
        vectorIcon = null,
        text = { "First Button" },
        onClick = {},
    )
}
```

- `addLast` - appends new `Dock.Item`:

```kotlin highlight-modifyListBuilder-addLast
addLast {
    Dock.Button.remember(
        id = EditorComponentId("my.package.dock.button.last"),
        vectorIcon = null,
        text = { "Last Button" },
        onClick = {},
    )
}
```

- `addAfter` - adds new `Dock.Item` right after the item with the provided id:

```kotlin highlight-modifyListBuilder-addAfter
addAfter(id = Dock.Button.Id.systemGallery) {
    Dock.Button.remember(
        id = EditorComponentId("my.package.dock.button.afterSystemGallery"),
        vectorIcon = null,
        text = { "After System Gallery" },
        onClick = {},
    )
}
```

- `addBefore` - adds new `Dock.Item` right before the item with the provided id:

```kotlin highlight-modifyListBuilder-addBefore
addBefore(id = Dock.Button.Id.systemCamera) {
    Dock.Button.remember(
        id = EditorComponentId("my.package.dock.button.beforeSystemCamera"),
        vectorIcon = null,
        text = { "Before System Camera" },
        onClick = {},
    )
}
```

- `replace` - replaces the `Dock.Item` with the provided id with new item:

```kotlin highlight-modifyListBuilder-replace
replace(id = Dock.Button.Id.textLibrary) {
    Dock.Button.remember(
        id = EditorComponentId("my.package.dock.button.replacedTextLibrary"),
        vectorIcon = null,
        text = { "Replaced Text Library" },
        onClick = {},
    )
}
```

- `remove` - removes the `Dock.Item` with the provided id:

```kotlin highlight-modifyListBuilder-remove
remove(id = Dock.Button.Id.shapesLibrary)
```

> **Note:** **Warning** Note that the order of items may change between editor versions,
> therefore `modify` must be used with care. Consider creating a new builder if
> you want to have strict ordering between different editor versions.

## Dock.Item Configuration

Each `Dock.Item` is an `EditorComponent`. Its `id` must be unique which is a requirement for proper component management.
Depending on your needs there are multiple ways to define an item. In this example, we demonstrate your options with increasing complexity.

### Use Predefined Buttons

The most basic option is to use our predefined buttons which are provided as composable functions. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/android/user-interface/customization/dock-cb916c/#list-of-available-dockbuttons).

### Create New Buttons

If our predefined buttons don't fit your needs you can create your own:

```kotlin highlight-dockItems-newButton
@Composable
fun rememberDockButton() = Dock.Button.remember(
    id = EditorComponentId("my.package.dock.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { Dock.ButtonScope(parentScope = this) }
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

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the button. Ideally, scope should be updated when the parent scope (scope of the parent component `Dock` - `Dock.Scope`) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent component scope (`Dock.scope`, accessed via `LocalEditorScope`) is updated.

- `visible` - whether the button should be visible. Default value is always true.

- `enterTransition` - transition of the button when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the button when it exits the parent composable. Default value is always no exit transition.

- `decoration` - decoration of the button. Useful when you want to add custom background, foreground, shadow, paddings etc. Default value is always no decoration.

- `onClick` - the callback that is invoked when the button is clicked. Parameter does not have a default value.

- `icon` - the icon content of the button. If null, it will not be rendered. Default value is null.

- `text` - the text content of the button. If null, it will not be rendered. Default value is null.

- `tint` - the tint color of the content. If null, then no tint is applied. Default value is null.

- `enabled` - whether the button is enabled. Default value is always true.

Other than the main `Dock.Button.remember` function, there is one more convenience overload that has three differences:

1. `icon` is replaced with `vectorIcon` lambda, that returns `VectorIcon` instead of drawing the icon content.
2. `text` is replaced with `text` lambda, that returns `String` instead of drawing the text content.
3. An extra parameter `contentDescription` is added that is used by accessibility services to describe what the button does. Note that it is not required to provide value when `text` is not null, since its value will be used by accessibility services, however having both `text` and `contentDescription` as null will cause a crash.

### Create Custom Items

For completely custom implementations, use `Dock.Custom` to render arbitrary content:

```kotlin highlight-dockItems-newCustomItem
@Composable
fun rememberCustomItem() = Dock.Custom.remember(
    id = EditorComponentId("my.package.dock.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { Dock.ItemScope(parentScope = this) }
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

- `id` - the id of the custom item. Note that it is highly recommended that every unique `EditorComponent` has a unique id. Parameter does not have a default value.

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the custom item. Ideally, scope should be updated when the parent scope (scope of the parent component `Dock` - `Dock.Scope`) is updated and when you want to observe changes from the `Engine`. Parameter does not have a default value.

- `visible` - whether the custom item should be visible. Default value is always true.

- `enterTransition` - transition of the custom item when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the custom item when it exits the parent composable. Default value is always no exit transition.

- `content` - the content of the custom item. You are responsible for drawing it, handling clicks etc. Parameter does not have a default value.

### List of Available Dock.Buttons

As you often saw in the previous sections, there are composable functions that look like this: `Dock.Button.remember{name}`. All these functions return a `Dock.Button`, they are public and can be used in your application. Note that all the parameters of these functions have default values, therefore, you do not need to provide any values, however, if you want to modify any of the parameters, it is exactly the same as described in [Create New Buttons](https://img.ly/docs/cesdk/android/user-interface/customization/dock-cb916c/#create-new-buttons) section.

| Button                                | ID                               | Description                                                                                                                                                                                                                                                                            |
| ------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Dock.Button.rememberElementsLibrary` | `Dock.Button.Id.elementsLibrary` | Opens library sheet with elements via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                |
| `Dock.Button.rememberOverlaysLibrary` | `Dock.Button.Id.overlaysLibrary` | Opens library sheet with overlays via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                |
| `Dock.Button.rememberImagesLibrary`   | `Dock.Button.Id.imagesLibrary`   | Opens library sheet with images via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                  |
| `Dock.Button.rememberTextLibrary`     | `Dock.Button.Id.textLibrary`     | Opens library sheet with text via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                    |
| `Dock.Button.rememberShapesLibrary`   | `Dock.Button.Id.shapesLibrary`   | Opens library sheet with shapes via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                  |
| `Dock.Button.rememberStickersLibrary` | `Dock.Button.Id.stickersLibrary` | Opens library sheet with stickers via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                |
| `Dock.Button.rememberAudiosLibrary`   | `Dock.Button.Id.audiosLibrary`   | Opens library sheet with audios via `EditorEvent.Sheet.Open`. By default, the `LibraryCategory` is picked from the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/).                                                                                                                  |
| `Dock.Button.rememberSystemGallery`   | `Dock.Button.Id.systemGallery`   | Opens the system gallery via `EditorEvent.LaunchContract`.                                                                                                                                                                                                                             |
| `Dock.Button.rememberSystemCamera`    | `Dock.Button.Id.systemCamera`    | Opens the system camera via `EditorEvent.LaunchContract`.                                                                                                                                                                                                                              |
| `Dock.Button.rememberImglyCamera`     | `Dock.Button.Id.imglyCamera`     | Opens the IMG.LY camera via `EditorEvent.LaunchContract`. Note that the button can be used only if `ly.img:camera:<same version as editor>` dependency is added in your `build.gradle` file. For more information, check the camera [documentation](https://img.ly/docs/cesdk/android/get-started/overview-e18f40/). |
| `Dock.Button.rememberReorder`         | `Dock.Button.Id.reorder`         | Opens reorder sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                      |
| `Dock.Button.rememberAdjustments`     | `Dock.Button.Id.adjustments`     | Opens adjustment sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                   |
| `Dock.Button.rememberFilter`          | `Dock.Button.Id.filter`          | Opens filter sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                       |
| `Dock.Button.rememberEffect`          | `Dock.Button.Id.effect`          | Opens effect sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                       |
| `Dock.Button.rememberBlur`            | `Dock.Button.Id.blur`            | Opens blur sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                         |
| `Dock.Button.rememberCrop`            | `Dock.Button.Id.crop`            | Opens crop sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                         |
| `Dock.Button.rememberResizeAll`       | `Dock.Button.Id.crop`            | Opens resize sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                       |



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
