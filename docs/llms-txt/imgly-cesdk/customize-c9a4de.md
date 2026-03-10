# Source: https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/

---
title: "Customize"
description: "Adapt the asset library UI and behavior to suit your application’s structure and user needs."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-library-65d6c4/) > [Customize](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-asset-library/AssetLibraryEditorSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.library.AssetLibrary
import ly.img.editor.rememberForDesign

// Add this composable to your NavHost
@Composable
fun AssetLibraryEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
    )
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        assetLibrary = AssetLibrary.getDefault(),
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-asset-library/DefaultAssetLibraryEditorSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EditorDefaults
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.library.AssetLibrary
import ly.img.editor.core.library.AssetType
import ly.img.editor.core.library.LibraryCategory
import ly.img.editor.core.library.LibraryContent
import ly.img.editor.core.library.addSection
import ly.img.editor.core.library.data.AssetSourceType
import ly.img.editor.core.library.dropSection
import ly.img.editor.core.library.replaceSection
import ly.img.editor.rememberForDesign
import ly.img.editor.smoketests.R

// Add this composable to your NavHost
@Composable
fun DefaultAssetLibraryEditorSolution(navController: NavHostController) {
    val unsplashAssetSource = remember {
        UnsplashAssetSource("<your Unsplash API host endpoint here>")
    }
    val engineConfiguration = EngineConfiguration.remember(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
        onCreate = {
            EditorDefaults.onCreate(
                engine = editorContext.engine,
                sceneUri = EngineConfiguration.defaultDesignSceneUri,
                eventHandler = editorContext.eventHandler,
            ) { _, _ ->
                editorContext.engine.asset.addSource(unsplashAssetSource)
            }
        },
    )
    val assetLibrary = remember {
        val unsplashSection = LibraryContent.Section(
            titleRes = R.string.unsplash,
            sourceTypes = listOf(AssetSourceType(sourceId = unsplashAssetSource.sourceId)),
            assetType = AssetType.Image,
        )
        AssetLibrary.getDefault(
            tabs = listOf(
                AssetLibrary.Tab.IMAGES,
                AssetLibrary.Tab.SHAPES,
                AssetLibrary.Tab.STICKERS,
                AssetLibrary.Tab.TEXT,
            ),
            images = LibraryCategory.Images
                .replaceSection(index = 0) {
                    // We replace the title: "Image Uploads" -> "Uploads"
                    copy(titleRes = R.string.uploads)
                }
                .dropSection(index = 1)
                .addSection(unsplashSection),
        )
    }
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        assetLibrary = assetLibrary,
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

```kotlin file=@cesdk_android_examples/editor-guides-configuration-asset-library/CustomAssetLibraryEditorSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EditorDefaults
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.R
import ly.img.editor.core.iconpack.IconPack
import ly.img.editor.core.iconpack.LibraryElements
import ly.img.editor.core.library.AssetLibrary
import ly.img.editor.core.library.AssetType
import ly.img.editor.core.library.LibraryCategory
import ly.img.editor.core.library.LibraryCategory.Companion.sourceTypes
import ly.img.editor.core.library.LibraryContent
import ly.img.editor.core.library.addSection
import ly.img.editor.core.library.data.AssetSourceType
import ly.img.editor.rememberForDesign
import ly.img.editor.smoketests.R as SmokeTestR

// Add this composable to your NavHost
@Composable
fun CustomAssetLibraryEditorSolution(navController: NavHostController) {
    val unsplashAssetSource = remember {
        UnsplashAssetSource("<your Unsplash API host endpoint here>")
    }
    val engineConfiguration = EngineConfiguration.remember(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
        onCreate = {
            EditorDefaults.onCreate(
                engine = editorContext.engine,
                sceneUri = EngineConfiguration.defaultDesignSceneUri,
                eventHandler = editorContext.eventHandler,
            ) { _, _ ->
                editorContext.engine.asset.addSource(unsplashAssetSource)
            }
        },
    )
    val assetLibrary = remember {
        // We create a custom tab with title "My Assets" that contains 2 sections:
        // 1. Stickers - expanding it opens the default stickers content
        // 2. Text - expanding it opens the default text content. Note that the title is skipped.
        val myAssetsCategory = LibraryCategory(
            tabTitleRes = SmokeTestR.string.my_assets,
            tabSelectedIcon = IconPack.LibraryElements,
            tabUnselectedIcon = IconPack.LibraryElements,
            content = LibraryContent.Sections(
                titleRes = SmokeTestR.string.my_assets,
                sections = listOf(
                    LibraryContent.Section(
                        titleRes = R.string.ly_img_editor_asset_library_title_stickers,
                        sourceTypes = LibraryContent.Stickers.sourceTypes,
                        assetType = AssetType.Sticker,
                        expandContent = LibraryContent.Stickers,
                    ),
                    LibraryContent.Section(
                        sourceTypes = LibraryContent.Text.sourceTypes,
                        assetType = AssetType.Text,
                        expandContent = LibraryContent.Text,
                    ),
                ),
            ),
        )
        AssetLibrary(
            tabs = {
                listOf(
                    myAssetsCategory,
                    LibraryCategory.Images,
                )
            },
            images = {
                val unsplashSection = LibraryContent.Section(
                    titleRes = SmokeTestR.string.unsplash,
                    sourceTypes = listOf(AssetSourceType(sourceId = unsplashAssetSource.sourceId)),
                    assetType = AssetType.Image,
                )
                // See how the images is different in tabs and here
                LibraryCategory.Images.addSection(unsplashSection)
            },
        )
    }
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        assetLibrary = assetLibrary,
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

In this example, we will show you how to customize the asset library for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-asset-library/).

## Configuration

Asset library configuration is part of the `EditorConfiguration` class. Use the `EditorConfiguration.getDefault` helper function to make asset library configurations.

- `assetLibrary` - the asset library UI definition used by the editor. It defines the content of the tabs when floating action button is clicked as well as the content of sheets when images and stickers are replaced. By default, `AssetLibrary.getDefault()` is used.

```kotlin highlight-configuration-asset-library
val editorConfiguration = EditorConfiguration.rememberForDesign(
    assetLibrary = AssetLibrary.getDefault(),
)
```

### Custom Asset Source

To use custom asset sources in the asset library UI, the custom asset source must be first added to the engine. In addition to creating or loading a scene, registering the asset sources should be done in the [callback](https://img.ly/docs/cesdk/android/user-interface/events-514b70/). In this example, the `EditorDefaults.onCreate` default implementation is used and afterwards, the [custom](https://img.ly/docs/cesdk/android/import-media/from-remote-source/unsplash-8f31f0/) is added.

```kotlin highlight-configuration-custom-asset-source
val unsplashAssetSource = remember {
    UnsplashAssetSource("<your Unsplash API host endpoint here>")
}
val engineConfiguration = EngineConfiguration.remember(
    license = "<your license here>", // pass null or empty for evaluation mode with watermark
    onCreate = {
        EditorDefaults.onCreate(
            engine = editorContext.engine,
            sceneUri = EngineConfiguration.defaultDesignSceneUri,
            eventHandler = editorContext.eventHandler,
        ) { _, _ ->
            editorContext.engine.asset.addSource(unsplashAssetSource)
        }
    },
)
```

### Default Asset Library

`AssetLibrary.getDefault()` provides a simple API in case you want to reorder/drop predefined tabs, as well as adjust the content of the tabs. In this example, firstly, we drop the `Elements` tab and reorder the remaining ones and secondly, we manipulate the sections of the `images` tab by dropping, swapping and appending sections. Note that we append the section based on the `UnsplashAssetSource` shown above.

```kotlin highlight-configuration-default-asset-library
val assetLibrary = remember {
    val unsplashSection = LibraryContent.Section(
        titleRes = R.string.unsplash,
        sourceTypes = listOf(AssetSourceType(sourceId = unsplashAssetSource.sourceId)),
        assetType = AssetType.Image,
    )
    AssetLibrary.getDefault(
        tabs = listOf(
            AssetLibrary.Tab.IMAGES,
            AssetLibrary.Tab.SHAPES,
            AssetLibrary.Tab.STICKERS,
            AssetLibrary.Tab.TEXT,
        ),
        images = LibraryCategory.Images
            .replaceSection(index = 0) {
                // We replace the title: "Image Uploads" -> "Uploads"
                copy(titleRes = R.string.uploads)
            }
            .dropSection(index = 1)
            .addSection(unsplashSection),
    )
}
val editorConfiguration = EditorConfiguration.rememberForDesign(
    assetLibrary = assetLibrary,
)
```

### Custom Asset Library

In case you want to adjust the asset library even further (i.e. create your own completely custom tabs, use different `images` category in FAB and replace sheets etc), you should use the constructor of the `AssetLibrary` instead of the helper `AssetLibrary.getDefault()` function. In this example, firstly, we fill the tabs with a custom `My Assets` tab as well as with the default `images` tab and secondly, we use a different `images` category for the replace sheet, which contains the default `images` + `UnsplashAssetSource` section.

```kotlin highlight-configuration-custom-asset-library
val assetLibrary = remember {
    // We create a custom tab with title "My Assets" that contains 2 sections:
    // 1. Stickers - expanding it opens the default stickers content
    // 2. Text - expanding it opens the default text content. Note that the title is skipped.
    val myAssetsCategory = LibraryCategory(
        tabTitleRes = SmokeTestR.string.my_assets,
        tabSelectedIcon = IconPack.LibraryElements,
        tabUnselectedIcon = IconPack.LibraryElements,
        content = LibraryContent.Sections(
            titleRes = SmokeTestR.string.my_assets,
            sections = listOf(
                LibraryContent.Section(
                    titleRes = R.string.ly_img_editor_asset_library_title_stickers,
                    sourceTypes = LibraryContent.Stickers.sourceTypes,
                    assetType = AssetType.Sticker,
                    expandContent = LibraryContent.Stickers,
                ),
                LibraryContent.Section(
                    sourceTypes = LibraryContent.Text.sourceTypes,
                    assetType = AssetType.Text,
                    expandContent = LibraryContent.Text,
                ),
            ),
        ),
    )
    AssetLibrary(
        tabs = {
            listOf(
                myAssetsCategory,
                LibraryCategory.Images,
            )
        },
        images = {
            val unsplashSection = LibraryContent.Section(
                titleRes = SmokeTestR.string.unsplash,
                sourceTypes = listOf(AssetSourceType(sourceId = unsplashAssetSource.sourceId)),
                assetType = AssetType.Image,
            )
            // See how the images is different in tabs and here
            LibraryCategory.Images.addSection(unsplashSection)
        },
    )
}
val editorConfiguration = EditorConfiguration.rememberForDesign(
    assetLibrary = assetLibrary,
)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
