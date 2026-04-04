# Source: https://img.ly/docs/cesdk/android/import-media/from-local-source/local-asset-3f93f2/

---
title: "Import Local Asset"
description: "Import files directly from the user's device and insert them into the design canvas."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/from-local-source/local-asset-3f93f2/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Import From Local Source](https://img.ly/docs/cesdk/android/import-media/from-local-source-39b2a9/) > [Import Local Asset](https://img.ly/docs/cesdk/android/import-media/from-local-source/local-asset-3f93f2/)

---

The Android editor provides an optional asset source that indexes the device gallery (images and videos) via the Android `MediaStore`. This section explains how to opt in, how the default (upload-only) workflow behaves, and how to take care of the required permissions when the gallery integration is enabled.

## Default behavior

- By default, the SDK keeps the system gallery disabled and relies on the upload buttons and camera intents. The Gallery section stays visible but starts empty and fills with the media that users add or capture while editing. This means no storage permissions are requested automatically and the media picker is handled by system intents.
- Opt in by calling `SystemGalleryPermission.setMode` inside your `EngineConfiguration.onCreate` callback (or any later editor scope). This keeps the opt-in explicit even when you rely on the helper composables.
- Once enabled, the asset library shows a **Gallery** section and the dock/timeline expose a *Gallery* quick action (`Dock.Button.rememberSystemGallery`). When end users only grant partial access (Android 13+ “selected photos”), the UI combines the selected items with the MediaStore listing.

```kotlin
import ly.img.editor.EngineConfiguration
import ly.img.editor.EditorDefaults
import ly.img.editor.core.library.data.SystemGalleryConfiguration
import ly.img.editor.core.library.data.SystemGalleryPermission

@Composable
fun rememberEngineConfiguration(license: String): EngineConfiguration =
    EngineConfiguration.remember(
        license = license,
        onCreate = {
            EditorDefaults.onCreate(
                editorContext.engine,
                EngineConfiguration.defaultDesignSceneUri,
                editorContext.eventHandler,
            )
            SystemGalleryPermission.setMode(SystemGalleryConfiguration.Enabled)
        },
    )
```

If you override the default `onCreate` handler or build your own engine bootstrap, add the sources manually as shown below.

## Adding the system gallery sources manually

```kotlin
import ly.img.editor.core.library.data.SystemGalleryConfiguration
import ly.img.editor.core.library.data.SystemGalleryPermission

suspend fun onCreate(engine: Engine) {
    engine.addDefaultAssetSources()
    SystemGalleryPermission.setMode(SystemGalleryConfiguration.Enabled)
    // …register any additional asset sources that you need afterwards
}
```

If you delegate to `EditorDefaults.onCreate`, call the scope helper afterwards:

```kotlin
import ly.img.editor.EditorDefaults
import ly.img.editor.core.library.data.SystemGalleryConfiguration

EditorDefaults.onCreate(
    engine = engine,
    sceneUri = sceneUri,
    eventHandler = eventHandler,
)
SystemGalleryPermission.setMode(SystemGalleryConfiguration.Enabled)
```

`SystemGalleryPermission.setMode` updates the gallery permission mode; `EditorDefaults` wire the sources automatically. If you build the engine manually, add the sources as shown above. The in-editor gallery relies on three sources:

- `AssetSourceType.GalleryAllVisuals` – combined images and videos (used for the default Gallery section)
- `AssetSourceType.GalleryImage`
- `AssetSourceType.GalleryVideo`

They are exposed in `LibraryCategory.getElements` and can also be consumed directly from custom `LibraryContent` definitions. When `SystemGalleryConfiguration.Disabled` is used, the sources only list the URIs that were manually added during the current session.

## Permissions and manifest setup

- Declare the following permissions in your app manifest so the runtime requests can be triggered:

  - `READ_MEDIA_IMAGES` and `READ_MEDIA_VIDEO` on Android 13+
  - `READ_MEDIA_VISUAL_USER_SELECTED` on Android 14+ (to support the *selected photos* mode)
  - Fallback to `READ_EXTERNAL_STORAGE` on Android 12 and lower

- The built-in UI components (`LibrarySectionHeader`, `SystemGalleryAddMenu`, `Dock.Button.rememberSystemGallery`) request the appropriate permissions via `ActivityResultContracts.RequestMultiplePermissions` and update `GalleryPermissionManager` automatically.

- If you build your own UI layer, use `GalleryPermissionManager.requiredPermission(mimeType)` to obtain the permission set and call `GalleryPermissionManager.setSelected(uris, context)` when the user picks a limited set of media.

Once the permissions are granted, `SystemGalleryAssetSource` paginates over MediaStore and refreshes the gallery section automatically.

## Legacy upload flow

```kotlin file=@cesdk_android_examples/editor-guides-configuration-asset-library/UploadsOnlyAssetLibraryEditorSolution.kt reference-only
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EngineConfiguration
import ly.img.editor.core.library.AssetLibrary
import ly.img.editor.core.library.AssetType
import ly.img.editor.core.library.LibraryCategory
import ly.img.editor.core.library.LibraryContent
import ly.img.editor.core.library.data.AssetSourceType
import ly.img.editor.rememberForDesign
import ly.img.editor.smoketests.Secrets

@Composable
fun UploadsOnlyAssetLibraryEditorSolution(navController: NavHostController) {
    val uploadsOnlyImages = remember {
        LibraryCategory.Images.copy(
            content = LibraryContent.Sections(
                titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_title_images,
                sections = listOf(
                    LibraryContent.Section(
                        titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_section_image_uploads,
                        sourceTypes = listOf(AssetSourceType.ImageUploads),
                        assetType = AssetType.Image,
                        expandContent = LibraryContent.Grid(
                            titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_section_image_uploads,
                            sourceType = AssetSourceType.ImageUploads,
                            assetType = AssetType.Image,
                        ),
                    ),
                ),
            ),
        )
    }
    val assetLibrary = remember {
        AssetLibrary.getDefault(images = uploadsOnlyImages)
    }

    val engineConfiguration = EngineConfiguration.remember(
        license = Secrets.license,
        onCreate = {},
    )
    val editorConfiguration = EditorConfiguration.rememberForDesign(
        assetLibrary = assetLibrary,
    )

    DesignEditor(
        engineConfiguration = engineConfiguration,
        editorConfiguration = editorConfiguration,
    ) {
        navController.popBackStack()
    }
}
```

The `UploadsOnlyAssetLibraryEditorSolution` sample demonstrates how to replace the default gallery sections with the classic uploads picker and how to adjust the timeline options accordingly.

```kotlin highlight-uploads-only-asset-library
val uploadsOnlyImages = remember {
    LibraryCategory.Images.copy(
        content = LibraryContent.Sections(
            titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_title_images,
            sections = listOf(
                LibraryContent.Section(
                    titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_section_image_uploads,
                    sourceTypes = listOf(AssetSourceType.ImageUploads),
                    assetType = AssetType.Image,
                    expandContent = LibraryContent.Grid(
                        titleRes = ly.img.editor.core.R.string.ly_img_editor_asset_library_section_image_uploads,
                        sourceType = AssetSourceType.ImageUploads,
                        assetType = AssetType.Image,
                    ),
                ),
            ),
        ),
    )
}
val assetLibrary = remember {
    AssetLibrary.getDefault(images = uploadsOnlyImages)
}
```

If you also want to hide the gallery quick action from the timeline menu, update the global configuration:

> **Optional:** `TimelineConfiguration` lives in the `editor-base` module. You can only adjust it if your app includes is.

```kotlin
import ly.img.editor.base.timeline.state.AddClipOption
import ly.img.editor.base.timeline.state.TimelineConfiguration

TimelineConfiguration.addClipOptions = listOf(AddClipOption.Camera, AddClipOption.Library)
```

- Update other categories (for example the combined `LibraryCategory.getElements`) the same way if you need to hide gallery sections globally.
- The stock dock and timeline buttons open the image category, so once that category only contains `AssetSourceType.ImageUploads`, the uploads picker shows up automatically.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
