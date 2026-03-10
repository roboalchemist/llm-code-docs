# Source: https://img.ly/docs/cesdk/android/user-interface/customization/inspector-bar-8ca1cd/

---
title: "Inspector Bar"
description: "Customize the inspector bar for editing properties like position, color, and size."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/inspector-bar-8ca1cd/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Inspector Bar](https://img.ly/docs/cesdk/android/user-interface/customization/inspector-bar-8ca1cd/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-inspector-bar/SimpleInspectorBarSolution.kt reference-only
import androidx.compose.animation.ExitTransition
import androidx.compose.animation.core.CubicBezierEasing
import androidx.compose.animation.core.tween
import androidx.compose.animation.slideInHorizontally
import androidx.compose.animation.slideInVertically
import androidx.compose.animation.slideOutVertically
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.InspectorBar
import ly.img.editor.core.component.InspectorBar.Companion.DefaultDecoration
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun SimpleInspectorBarSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        inspectorBar = {
            InspectorBar.remember(
                // Implementation is too large, check the implementation of InspectorBar.defaultScope
                scope = InspectorBar.defaultScope,
                visible = { editorContext.safeSelection != null },
                // Also available via InspectorBar.defaultEnterTransition
                enterTransition = {
                    remember {
                        slideInVertically(
                            animationSpec = tween(
                                durationMillis = 400,
                                easing = CubicBezierEasing(0.05f, 0.7f, 0.1f, 1f),
                            ),
                            initialOffsetY = { it },
                        )
                    }
                },
                // Also available via InspectorBar.defaultExitTransition
                exitTransition = {
                    remember {
                        slideOutVertically(
                            animationSpec = tween(
                                durationMillis = 150,
                                easing = CubicBezierEasing(0.3f, 0f, 0.8f, 0.15f),
                            ),
                            targetOffsetY = { it },
                        )
                    }
                },
                // Implementation is too large, check the implementation of InspectorBar.DefaultDecoration
                decoration = { DefaultDecoration { it() } },
                listBuilder = InspectorBar.ListBuilder.remember(),
                horizontalArrangement = { Arrangement.Start },
                // Also available via InspectorBar.defaultItemsRowEnterTransition
                itemsRowEnterTransition = {
                    remember {
                        slideInHorizontally(
                            animationSpec = tween(400, easing = CubicBezierEasing(0.05F, 0.7F, 0.1F, 1F)),
                            initialOffsetX = { it / 3 },
                        )
                    }
                },
                // Also available via InspectorBar.defaultItemsRowExitTransition
                itemsRowExitTransition = { ExitTransition.None },
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-inspector-bar/InspectorBarListBuilders.kt reference-only
import androidx.compose.runtime.Composable
import ly.img.editor.core.component.InspectorBar
import ly.img.editor.core.component.rememberAdjustments
import ly.img.editor.core.component.rememberBlur
import ly.img.editor.core.component.rememberCrop
import ly.img.editor.core.component.rememberDelete
import ly.img.editor.core.component.rememberDuplicate
import ly.img.editor.core.component.rememberEditText
import ly.img.editor.core.component.rememberEffect
import ly.img.editor.core.component.rememberEnterGroup
import ly.img.editor.core.component.rememberFillStroke
import ly.img.editor.core.component.rememberFilter
import ly.img.editor.core.component.rememberFormatText
import ly.img.editor.core.component.rememberLayer
import ly.img.editor.core.component.rememberMoveAsClip
import ly.img.editor.core.component.rememberMoveAsOverlay
import ly.img.editor.core.component.rememberReorder
import ly.img.editor.core.component.rememberReplace
import ly.img.editor.core.component.rememberSelectGroup
import ly.img.editor.core.component.rememberShape
import ly.img.editor.core.component.rememberSplit
import ly.img.editor.core.component.rememberTextBackground
import ly.img.editor.core.component.rememberVolume

@Composable
fun InspectorBar.ListBuilder.remember() = InspectorBar.ListBuilder.remember {
    add { InspectorBar.Button.rememberReplace() } // Video, Image, Sticker, Audio
    add { InspectorBar.Button.rememberEditText() } // Text
    add { InspectorBar.Button.rememberFormatText() } // Text
    add { InspectorBar.Button.rememberFillStroke() } // Page, Video, Image, Shape, Text
    add { InspectorBar.Button.rememberTextBackground() } // Text
    add { InspectorBar.Button.rememberVolume() } // Video, Audio
    add { InspectorBar.Button.rememberCrop() } // Video, Image
    add { InspectorBar.Button.rememberAdjustments() } // Video, Image
    add { InspectorBar.Button.rememberFilter() } // Video, Image
    add { InspectorBar.Button.rememberEffect() } // Video, Image
    add { InspectorBar.Button.rememberBlur() } // Video, Image
    add { InspectorBar.Button.rememberShape() } // Video, Image, Shape
    add { InspectorBar.Button.rememberSelectGroup() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberEnterGroup() } // Group
    add { InspectorBar.Button.rememberLayer() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberSplit() } // Video, Image, Sticker, Shape, Text, Audio
    add { InspectorBar.Button.rememberMoveAsClip() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberMoveAsOverlay() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberReorder() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberDuplicate() } // Video, Image, Sticker, Shape, Text, Audio
    add { InspectorBar.Button.rememberDelete() } // Video, Image, Sticker, Shape, Text, Audio
}
```

```kotlin file=@cesdk_android_examples/editor-guides-configuration-inspector-bar/ModifyListBuilderInspectorBarSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.component.EditorComponent.ListBuilder.Companion.modify
import ly.img.editor.core.component.EditorComponentId
import ly.img.editor.core.component.InspectorBar
import ly.img.editor.core.component.crop
import ly.img.editor.core.component.delete
import ly.img.editor.core.component.formatText
import ly.img.editor.core.component.layer
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun ModifyListBuilderInspectorBarSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )

    val editorConfiguration = EditorConfiguration.rememberForDesign(
        inspectorBar = {
            InspectorBar.remember(
                listBuilder = InspectorBar.ListBuilder.remember().modify {
                    addFirst {
                        InspectorBar.Button.remember(
                            id = EditorComponentId("my.package.inspectorBar.button.first"),
                            vectorIcon = null,
                            text = { "First Button" },
                            onClick = {},
                        )
                    }
                    addLast {
                        InspectorBar.Button.remember(
                            id = EditorComponentId("my.package.inspectorBar.button.last"),
                            vectorIcon = null,
                            text = { "Last Button" },
                            onClick = {},
                        )
                    }
                    addAfter(id = InspectorBar.Button.Id.layer) {
                        InspectorBar.Button.remember(
                            id = EditorComponentId("my.package.inspectorBar.button.afterLayer"),
                            vectorIcon = null,
                            text = { "After Layer" },
                            onClick = {},
                        )
                    }
                    addBefore(id = InspectorBar.Button.Id.crop) {
                        InspectorBar.Button.remember(
                            id = EditorComponentId("my.package.inspectorBar.button.beforeCrop"),
                            vectorIcon = null,
                            text = { "Before Crop" },
                            onClick = {},
                        )
                    }
                    replace(id = InspectorBar.Button.Id.formatText) {
                        InspectorBar.Button.remember(
                            id = EditorComponentId("my.package.inspectorBar.button.replacedFormatText"),
                            vectorIcon = null,
                            text = { "Replaced Format Text" },
                            onClick = {},
                        )
                    }
                    remove(id = InspectorBar.Button.Id.delete)
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-inspector-bar/InspectorBarItems.kt reference-only
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
import ly.img.editor.core.component.InspectorBar
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.Music
import ly.img.editor.core.sheet.SheetType

@Composable
fun rememberInspectorBarButton() = InspectorBar.Button.remember(
    id = EditorComponentId("my.package.inspectorBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { InspectorBar.ButtonScope(parentScope = this) }
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
fun rememberInspectorBarButtonSimpleOverload() = InspectorBar.Button.remember(
    id = EditorComponentId("my.package.inspectorBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { InspectorBar.ButtonScope(parentScope = this) }
    },
    onClick = { editorContext.eventHandler.send(ShowLoading) },
    visible = { true },
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None },
    decoration = {
        Surface(color = MaterialTheme.colorScheme.background) {
            it()
        }
    },
    vectorIcon = { IconPack.Music }, // default value is null
    text = { "Hello World" }, // default value is null
    tint = null,
    enabled = { true },
    contentDescription = null,
)

@Composable
fun rememberInspectorBarCustomItem() = InspectorBar.Custom.remember(
    id = EditorComponentId("my.package.inspectorBar.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { InspectorBar.ItemScope(parentScope = this) }
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

The inspector bar provides context-sensitive editing controls that appear when you select a design element, offering tools specific to that element type like text formatting, image adjustments, or shape properties. This guide shows you how to customize these editing controls to match your app's feature set and user experience goals. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-inspector-bar).

## Inspector Bar Architecture

![Inspector Bar](./assets/inspector-bar-android.png)

The inspector bar displays horizontally at the bottom when a design element is selected. It contains context-sensitive editing tools that adapt based on the selected element type (text, image, video, etc.).

**Key Components:**

- **`InspectorBar.Item`** - Abstract class that all inspector items inherit from
- **`InspectorBar.Button`** - Pre-built button implementation with icon and text
- **`InspectorBar.Custom`** - Fully custom component for arbitrary content rendering
- **`InspectorBar.Scope`** - Provides access to the engine, event handler, and selected element

## Configuration

Inspector bar customization is part of the `EditorConfiguration`, therefore, in order to configure the inspector bar we need to configure the `EditorConfiguration`. Below you can find the list of available configurations of the inspector bar. To demonstrate the default values, all parameters are assigned to their default values.

**Available configuration parameters:**

- **`scope`** - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the inspector bar. Prefer updating individual `InspectorBar.Item`s over updating the whole inspector bar. Ideally, scope should be updated when the parent scope (scope of the parent component) is updated and when you want to observe changes from the `Engine`.

- **`visible`** - Control inspector bar visibility based on selection state. Default value is always true.

- **`enterTransition`** - Animation for when the inspector bar appears. By default, a vertical slide in animation is used.

- **`exitTransition`** - Animation for when the inspector bar disappears. By default, a vertical slide out animation is used.

- **`decoration`** - Apply custom styling like background, shadows, and padding. Default value is always no decoration.

- **`listBuilder`** - Define the complete list of inspector bar items and their order. Items are only displayed when `visible` returns `true`.

- **`horizontalArrangement`** - Layout arrangement for inspector bar items. Controls spacing and alignment of items within the inspector bar. Default value is `Arrangement.Start`.

- **`itemDecoration`** - decoration of the items in the inspector bar. Useful when you want to add custom background, foreground, shadow, paddings etc to the items. Prefer using this decoration when you want to apply the same decoration to all the items, otherwise set decoration to individual items. Default value is always no decoration.

- **`itemsRowEnterTransition`** - Animation for when the items row appears. By default, a horizontal slide in animation is used.

- **`itemsRowExitTransition`** - Animation for when the items row disappears. Default value is always no exit transition.

```kotlin highlight-inspectorBarConfiguration
val editorConfiguration = EditorConfiguration.rememberForDesign(
    inspectorBar = {
        InspectorBar.remember(
            // Implementation is too large, check the implementation of InspectorBar.defaultScope
            scope = InspectorBar.defaultScope,
            visible = { editorContext.safeSelection != null },
            // Also available via InspectorBar.defaultEnterTransition
            enterTransition = {
                remember {
                    slideInVertically(
                        animationSpec = tween(
                            durationMillis = 400,
                            easing = CubicBezierEasing(0.05f, 0.7f, 0.1f, 1f),
                        ),
                        initialOffsetY = { it },
                    )
                }
            },
            // Also available via InspectorBar.defaultExitTransition
            exitTransition = {
                remember {
                    slideOutVertically(
                        animationSpec = tween(
                            durationMillis = 150,
                            easing = CubicBezierEasing(0.3f, 0f, 0.8f, 0.15f),
                        ),
                        targetOffsetY = { it },
                    )
                }
            },
            // Implementation is too large, check the implementation of InspectorBar.DefaultDecoration
            decoration = { DefaultDecoration { it() } },
            listBuilder = InspectorBar.ListBuilder.remember(),
            horizontalArrangement = { Arrangement.Start },
            // Also available via InspectorBar.defaultItemsRowEnterTransition
            itemsRowEnterTransition = {
                remember {
                    slideInHorizontally(
                        animationSpec = tween(400, easing = CubicBezierEasing(0.05F, 0.7F, 0.1F, 1F)),
                        initialOffsetX = { it / 3 },
                    )
                }
            },
            // Also available via InspectorBar.defaultItemsRowExitTransition
            itemsRowExitTransition = { ExitTransition.None },
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

- **`InspectorBar.ListBuilder.remember()`** - Define the complete list of inspector bar items from scratch. Use this when you want full control over the inspector bar configuration.

- **`InspectorBar.ListBuilder.remember().modify()`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration. Use this when you want to keep most defaults but make targeted changes.

The `InspectorBar.Scope` provides access to the engine, event handler, and selected element state. Use this for advanced customization logic and to maintain consistency with the current editor context.

### Default Inspector Bar Items

The default configuration includes all essential editing tools for different element types:

```kotlin highlight-listBuilders
@Composable
fun InspectorBar.ListBuilder.remember() = InspectorBar.ListBuilder.remember {
    add { InspectorBar.Button.rememberReplace() } // Video, Image, Sticker, Audio
    add { InspectorBar.Button.rememberEditText() } // Text
    add { InspectorBar.Button.rememberFormatText() } // Text
    add { InspectorBar.Button.rememberFillStroke() } // Page, Video, Image, Shape, Text
    add { InspectorBar.Button.rememberTextBackground() } // Text
    add { InspectorBar.Button.rememberVolume() } // Video, Audio
    add { InspectorBar.Button.rememberCrop() } // Video, Image
    add { InspectorBar.Button.rememberAdjustments() } // Video, Image
    add { InspectorBar.Button.rememberFilter() } // Video, Image
    add { InspectorBar.Button.rememberEffect() } // Video, Image
    add { InspectorBar.Button.rememberBlur() } // Video, Image
    add { InspectorBar.Button.rememberShape() } // Video, Image, Shape
    add { InspectorBar.Button.rememberSelectGroup() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberEnterGroup() } // Group
    add { InspectorBar.Button.rememberLayer() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberSplit() } // Video, Image, Sticker, Shape, Text, Audio
    add { InspectorBar.Button.rememberMoveAsClip() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberMoveAsOverlay() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberReorder() } // Video, Image, Sticker, Shape, Text
    add { InspectorBar.Button.rememberDuplicate() } // Video, Image, Sticker, Shape, Text, Audio
    add { InspectorBar.Button.rememberDelete() } // Video, Image, Sticker, Shape, Text, Audio
}
```

### Modify Inspector Bar Items

Use the `modify` function to adjust the default item list without rebuilding the entire configuration:

```kotlin highlight-modifyListBuilderSignature
listBuilder = InspectorBar.ListBuilder.remember().modify {
```

**Available modification operations:**

- `addFirst` - prepends a new item at the beginning:

```kotlin highlight-modifyListBuilder-addFirst
addFirst {
    InspectorBar.Button.remember(
        id = EditorComponentId("my.package.inspectorBar.button.first"),
        vectorIcon = null,
        text = { "First Button" },
        onClick = {},
    )
}
```

- `addLast` - appends a new item at the end:

```kotlin highlight-modifyListBuilder-addLast
addLast {
    InspectorBar.Button.remember(
        id = EditorComponentId("my.package.inspectorBar.button.last"),
        vectorIcon = null,
        text = { "Last Button" },
        onClick = {},
    )
}
```

- `addAfter` - adds a new item right after a specific item:

```kotlin highlight-modifyListBuilder-addAfter
addAfter(id = InspectorBar.Button.Id.layer) {
    InspectorBar.Button.remember(
        id = EditorComponentId("my.package.inspectorBar.button.afterLayer"),
        vectorIcon = null,
        text = { "After Layer" },
        onClick = {},
    )
}
```

- `addBefore` - adds a new item right before a specific item:

```kotlin highlight-modifyListBuilder-addBefore
addBefore(id = InspectorBar.Button.Id.crop) {
    InspectorBar.Button.remember(
        id = EditorComponentId("my.package.inspectorBar.button.beforeCrop"),
        vectorIcon = null,
        text = { "Before Crop" },
        onClick = {},
    )
}
```

- `replace` - replaces an existing item with a new item:

```kotlin highlight-modifyListBuilder-replace
replace(id = InspectorBar.Button.Id.formatText) {
    InspectorBar.Button.remember(
        id = EditorComponentId("my.package.inspectorBar.button.replacedFormatText"),
        vectorIcon = null,
        text = { "Replaced Format Text" },
        onClick = {},
    )
}
```

- `remove` - removes an existing item:

```kotlin highlight-modifyListBuilder-remove
remove(id = InspectorBar.Button.Id.delete)
```

> **Note:** **Warning** Note that the order of items may change between editor versions,
> therefore `modify` must be used with care. Consider creating a new builder if
> you want to have strict ordering between different editor versions.

## InspectorBar.Item Configuration

Each `InspectorBar.Item` is an `EditorComponent`. Its `id` must be unique which is a requirement for proper component management.
You have multiple options for creating inspector bar items, from simple predefined buttons to fully custom implementations.

### Use Predefined Buttons

Start with predefined buttons which are provided as composable functions. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/android/user-interface/customization/inspector-bar-8ca1cd/#list-of-available-inspectorbarbuttons).

### Create New Buttons

Create custom buttons when predefined options don't meet your needs:

```kotlin highlight-inspectorBarItems-newButton
@Composable
fun rememberInspectorBarButton() = InspectorBar.Button.remember(
    id = EditorComponentId("my.package.inspectorBar.button.newButton"),
    scope = LocalEditorScope.current.run {
        remember(this) { InspectorBar.ButtonScope(parentScope = this) }
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

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the button. Ideally, scope should be updated when the parent scope (scope of the parent component `InspectorBar` - `InspectorBar.Scope`) is updated and when you want to observe changes from the `Engine`. By default the scope is updated only when the parent component scope (`InspectorBar.scope`, accessed via `LocalEditorScope`) is updated.

- `visible` - whether the button should be visible. Default value is always true.

- `enterTransition` - transition of the button when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the button when it exits the parent composable. Default value is always no exit transition.

- `decoration` - decoration of the button. Useful when you want to add custom background, foreground, shadow, paddings etc. Default value is always no decoration.

- `onClick` - the callback that is invoked when the button is clicked. Parameter does not have a default value.

- `icon` - the icon content of the button. If null, it will not be rendered. Default value is null.

- `text` - the text content of the button. If null, it will not be rendered. Default value is null.

- `tint` - the tint color of the content. If null, then no tint is applied. Default value is null.

- `enabled` - whether the button is enabled. Default value is always true.

Other than the main `InspectorBar.Button.remember` function, there is one more convenience overload that has three differences:

1. `icon` is replaced with `vectorIcon` lambda, that returns `VectorIcon` instead of drawing the icon content.
2. `text` is replaced with `text` lambda, that returns `String` instead of drawing the text content.
3. An extra parameter `contentDescription` is added that is used by accessibility services to describe what the button does. Note that it is not required to provide value when `text` is not null, since its value will be used by accessibility services, however having both `text` and `contentDescription` as null will cause a crash.

### Create Custom Items

For completely custom implementations, use `InspectorBar.Custom` to render arbitrary content:

```kotlin highlight-inspectorBarItems-newCustomItem
@Composable
fun rememberInspectorBarCustomItem() = InspectorBar.Custom.remember(
    id = EditorComponentId("my.package.inspectorBar.newCustomItem"),
    scope = LocalEditorScope.current.run {
        remember(this) { InspectorBar.ItemScope(parentScope = this) }
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

- `scope` - the scope of this component. Every new value will trigger recomposition of all the lambda parameters below. If you need to access `EditorScope` to construct the scope, use `LocalEditorScope`. Consider using Compose `State` objects in the lambda parameters below for granular recompositions over updating the scope, since scope change triggers full recomposition of the custom item. Ideally, scope should be updated when the parent scope (scope of the parent component `InspectorBar` - `InspectorBar.Scope`) is updated and when you want to observe changes from the `Engine`. Parameter does not have a default value.

- `visible` - whether the custom item should be visible. Default value is always true.

- `enterTransition` - transition of the custom item when it enters the parent composable. Default value is always no enter transition.

- `exitTransition` - transition of the custom item when it exits the parent composable. Default value is always no exit transition.

- `content` - the content of the custom item. You are responsible for drawing it, handling clicks etc. Parameter does not have a default value.

### List of Available InspectorBar.Buttons

As you often saw in the previous sections, there are composable functions that look like this: `InspectorBar.Button.remember{name}`. All these functions return an `InspectorBar.Button`, they are public and can be used in your application. Note that all the parameters of these functions have default values, therefore, you do not need to provide any values, however, if you want to modify any of the parameters, it is exactly the same as described in [Create New Buttons](https://img.ly/docs/cesdk/android/user-interface/customization/inspector-bar-8ca1cd/#create-new-buttons) section.

| Button                                       | ID                                      | Description                                                                                                                                                                                                                                                                                              | Renders For                                          |
| -------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `InspectorBar.Button.rememberReplace`        | `InspectorBar.Button.Id.replace`        | Opens library sheet via `EditorEvent.Sheet.Open`. By default, `DesignBlockType`, `FillType` and kind of the selected design block are used to find the library in the [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/). Selected asset will replace the content of the currently selected design block. | Video, Image, Sticker, Audio                         |
| `InspectorBar.Button.rememberEditText`       | `InspectorBar.Button.Id.editText`       | Enters text editing mode for the selected design block.                                                                                                                                                                                                                                                  | Text                                                 |
| `InspectorBar.Button.rememberFormatText`     | `InspectorBar.Button.Id.formatText`     | Opens format text sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                    | Text                                                 |
| `InspectorBar.Button.rememberFillStroke`     | `InspectorBar.Button.Id.fillStroke`     | Opens fill & stroke sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                  | Page, Video, Image, Shape, Text                      |
| `InspectorBar.Button.rememberTextBackground` | `InspectorBar.Button.Id.textBackground` | Opens text background sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                | Text                                                 |
| `InspectorBar.Button.rememberEditVoiceover`  | `InspectorBar.Button.Id.editVoiceover`  | Opens voiceover sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                      | Video, Audio, Voiceover                              |
| `InspectorBar.Button.rememberVolume`         | `InspectorBar.Button.Id.volume`         | Opens volume sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                         | Video, Audio, Voiceover                              |
| `InspectorBar.Button.rememberCrop`           | `InspectorBar.Button.Id.crop`           | Opens crop sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                           | Video, Image                                         |
| `InspectorBar.Button.rememberAdjustments`    | `InspectorBar.Button.Id.adjustments`    | Opens adjustments sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                    | Video, Image                                         |
| `InspectorBar.Button.rememberFilter`         | `InspectorBar.Button.Id.filter`         | Opens filter sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                         | Video, Image                                         |
| `InspectorBar.Button.rememberEffect`         | `InspectorBar.Button.Id.effect`         | Opens effect sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                         | Video, Image                                         |
| `InspectorBar.Button.rememberBlur`           | `InspectorBar.Button.Id.blur`           | Opens blur sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                           | Video, Image                                         |
| `InspectorBar.Button.rememberShape`          | `InspectorBar.Button.Id.shape`          | Opens shape sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                          | Video, Image, Shape                                  |
| `InspectorBar.Button.rememberSelectGroup`    | `InspectorBar.Button.Id.selectGroup`    | Selects the group design block that contains the currently selected design block via `EditorEvent.selectGroupForSelection`.                                                                                                                                                                              | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Button.rememberEnterGroup`     | `InspectorBar.Button.Id.enterGroup`     | Changes selection from the selected group design block to a design block within that group via `EditorEvent.enterGroupForSelection`.                                                                                                                                                                     | Group                                                |
| `InspectorBar.Button.rememberLayer`          | `InspectorBar.Button.Id.layer`          | Opens layer sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                          | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Button.rememberSplit`          | `InspectorBar.Button.Id.split`          | Splits currently selected design block via `EditorEvent.splitSelection` in a video scene.                                                                                                                                                                                                                | Video, Image, Sticker, Shape, Text, Audio            |
| `InspectorBar.Button.rememberMoveAsClip`     | `InspectorBar.Button.Id.moveAsClip`     | Moves currently selected design block into the background track as clip via `EditorEvent.moveSelectionAsClip`.                                                                                                                                                                                           | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Button.rememberMoveAsOverlay`  | `InspectorBar.Button.Id.moveAsOverlay`  | Moves currently selected design block from the background track to an overlay via `EditorEvent.moveSelectionAsOverlay`.                                                                                                                                                                                  | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Button.rememberReorder`        | `InspectorBar.Button.Id.reorder`        | Opens reorder sheet via `EditorEvent.Sheet.Open`.                                                                                                                                                                                                                                                        | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Button.rememberDuplicate`      | `InspectorBar.Button.Id.duplicate`      | Duplicates currently selected design block via `EditorEvent.duplicateSelection`.                                                                                                                                                                                                                         | Video, Image, Sticker, Shape, Text, Audio            |
| `InspectorBar.Button.rememberDelete`         | `InspectorBar.Button.Id.delete`         | Deletes currently selected design block via `EditorEvent.deleteSelection`.                                                                                                                                                                                                                               | Video, Image, Sticker, Shape, Text, Audio, Voiceover |



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
