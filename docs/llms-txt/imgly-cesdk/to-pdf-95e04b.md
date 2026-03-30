# Source: https://img.ly/docs/cesdk/android/export-save-publish/export/to-pdf-95e04b/

---
title: "To PDF"
description: "Learn how to export pages to PDF."
platform: android
url: "https://img.ly/docs/cesdk/android/export-save-publish/export/to-pdf-95e04b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Export Media Assets](https://img.ly/docs/cesdk/android/export-save-publish/export-82f968/) > [To PDF](https://img.ly/docs/cesdk/android/export-save-publish/export/to-pdf-95e04b/)

---

```kotlin file=@cesdk_android_examples/editor-guides-configuration-callbacks/CallbacksEditorSolution.kt reference-only
import android.net.Uri
import android.widget.Toast
import androidx.compose.runtime.Composable
import androidx.core.content.FileProvider
import androidx.navigation.NavHostController
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.distinctUntilChanged
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.editor.DesignEditor
import ly.img.editor.DismissVideoExportEvent
import ly.img.editor.EditorDefaults
import ly.img.editor.EngineConfiguration
import ly.img.editor.HideLoading
import ly.img.editor.OnSceneLoaded
import ly.img.editor.ShareUriEvent
import ly.img.editor.ShowCloseConfirmationDialogEvent
import ly.img.editor.ShowErrorDialogEvent
import ly.img.editor.ShowLoading
import ly.img.editor.ShowVideoExportErrorEvent
import ly.img.editor.ShowVideoExportProgressEvent
import ly.img.editor.ShowVideoExportSuccessEvent
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.library.data.TextAssetSource
import ly.img.editor.core.library.data.TypefaceProvider
import ly.img.engine.MimeType
import ly.img.engine.SceneMode
import ly.img.engine.addDefaultAssetSources
import ly.img.engine.addDemoAssetSources
import kotlin.coroutines.cancellation.CancellationException

// Add this composable to your NavHost
@Composable
fun CallbacksEditorSolution(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.remember(
        license = "<your license here>", // pass null or empty for evaluation mode with watermark
        onCreate = {
            // Note that lambda is copied from EditorDefaults.onCreate
            coroutineScope {
                // In case of process recovery, engine automatically recovers the scene that is why we need to check
                if (editorContext.engine.scene.get() == null) {
                    editorContext.engine.scene.load(EngineConfiguration.defaultDesignSceneUri)
                }
                launch {
                    editorContext.engine.addDefaultAssetSources()
                    val defaultTypeface = TypefaceProvider().provideTypeface(editorContext.engine, "Roboto")
                    requireNotNull(defaultTypeface)
                    editorContext.engine.asset.addSource(TextAssetSource(editorContext.engine, defaultTypeface))
                }
                launch {
                    editorContext.engine.addDemoAssetSources(
                        sceneMode = editorContext.engine.scene.getMode(),
                        withUploadAssetSources = true,
                    )
                }
            }
            editorContext.eventHandler.send(HideLoading)
            editorContext.eventHandler.send(OnSceneLoaded())
        },
        onLoaded = {
            editorContext.engine.editor.setSettingEnum("touch/pinchAction", "Scale")
            coroutineScope {
                launch {
                    editorContext.engine.editor
                        .onHistoryUpdated()
                        .collect { Toast.makeText(editorContext.activity, "History is updated!", Toast.LENGTH_SHORT).show() }
                }
                launch {
                    editorContext.engine.editor
                        .onStateChanged()
                        .map { editorContext.engine.editor.getEditMode() }
                        .distinctUntilChanged()
                        .collect { Toast.makeText(editorContext.activity, "Edit mode is updated to $it!", Toast.LENGTH_SHORT).show() }
                }
            }
        },
        onExport = {
            val engine = editorContext.engine
            val eventHandler = editorContext.eventHandler
            val context = engine.applicationContext
            EditorDefaults.run {
                if (engine.scene.getMode() == SceneMode.VIDEO) {
                    val page = engine.scene.getCurrentPage() ?: engine.scene.getPages()[0]
                    var exportProgress = 0f
                    eventHandler.send(ShowVideoExportProgressEvent(exportProgress))
                    runCatching {
                        val buffer = engine.block.exportVideo(
                            block = page,
                            timeOffset = 0.0,
                            duration = engine.block.getDuration(page),
                            mimeType = MimeType.MP4,
                            progressCallback = { progress ->
                                val newProgress = progress.encodedFrames.toFloat() / progress.totalFrames
                                if (newProgress >= exportProgress + 0.01f) {
                                    exportProgress = newProgress
                                    eventHandler.send(ShowVideoExportProgressEvent(exportProgress))
                                }
                            },
                        )
                        val file = writeToTempFile(buffer, MimeType.MP4)
                        withContext(Dispatchers.IO) {
                            FileProvider.getUriForFile(
                                context,
                                "${context.packageName}.ly.img.editor.fileprovider",
                                file,
                            )
                        }
                    }.onSuccess { uri ->
                        eventHandler.send(ShowVideoExportSuccessEvent(uri, MimeType.MP4.key))
                    }.onFailure {
                        if (it is CancellationException) {
                            eventHandler.send(DismissVideoExportEvent)
                        } else {
                            eventHandler.send(ShowVideoExportErrorEvent)
                        }
                    }
                } else {
                    eventHandler.send(ShowLoading)
                    runCatching {
                        val buffer = engine.block.export(
                            block = requireNotNull(engine.scene.get()),
                            mimeType = MimeType.PDF,
                        ) {
                            scene.getPages().forEach {
                                block.setScopeEnabled(it, key = "layer/visibility", enabled = true)
                                block.setVisible(it, visible = true)
                            }
                        }
                        val file = writeToTempFile(buffer, MimeType.PDF)
                        withContext(Dispatchers.IO) {
                            FileProvider.getUriForFile(
                                context,
                                "${context.packageName}.ly.img.editor.fileprovider",
                                file,
                            )
                        }
                    }.onSuccess { uri ->
                        eventHandler.send(HideLoading)
                        eventHandler.send(ShareUriEvent(uri, MimeType.PDF.key))
                    }.onFailure {
                        eventHandler.send(HideLoading)
                        eventHandler.send(ShowErrorDialogEvent(error = it))
                    }
                }
            }
        },
        onUpload = { assetDefinition, _ ->
            val meta = assetDefinition.meta ?: return@remember assetDefinition
            val sourceUri = Uri.parse(meta["uri"])
            val uploadedUri = sourceUri // todo upload the asset here and return remote uri
            val newMeta = meta +
                listOf(
                    "uri" to uploadedUri.toString(),
                    "thumbUri" to uploadedUri.toString(),
                )
            assetDefinition.copy(meta = newMeta)
        },
        onClose = { hasUnsavedChanges ->
            if (hasUnsavedChanges) {
                editorContext.eventHandler.send(ShowCloseConfirmationDialogEvent)
            } else {
                editorContext.eventHandler.send(EditorEvent.CloseEditor())
            }
        },
        onError = { error ->
            editorContext.eventHandler.send(ShowErrorDialogEvent(error))
        },
    )
    DesignEditor(engineConfiguration = engineConfiguration) {
        // You can set result here
        navController.popBackStack()
    }
}
```

In this guide, you'll learn how to configure the prebuilt editor (Design Editor, Photo Editor, etc.) to export designs as PDFs. You can keep the built-in file write and share behavior, or inject export options (DPI, underlayer, high compatibility) while preserving the default flow.

## What You'll Learn

- Switch the prebuilt editor's export to PDF via `onExport`.
- Preserve the default event flow (share file) without custom UI code.
- Add export options (DPI, high-compat, underlayer) for design scenes.
- Keep MP4 export for video scenes while using PDF for design scenes.

## When to Use It

- You want editor UI out of the box, with export customized to PDF.
- You want to avoid writing your own share/save UI.
- You need optional export tweaks but prefer the editor's default UX.

## Export Control

The prebuilt editors have a share control in the navigation bar. This control exports the current scene as either a PNG or MP4, depending on the scene's mode. Then it displays a share sheet or system share dialog.

![Location of export button in prebuilt editors](assets/create-pdf-android-1.png)

The editors provide an `onExport` callback you can use to control this behavior. If your export to PDF isn't complicated, configuring the MIME type may be all you need.

```kotlin
val engineConfiguration = EngineConfiguration.remember(
    license = "<your license here>",
    onExport = {
        val engine = editorContext.engine
        val eventHandler = editorContext.eventHandler
        EditorDefaults.run {
            eventHandler.send(ShowLoading)
            runCatching {
                val buffer = engine.block.export(
                    block = requireNotNull(engine.scene.get()),
                    mimeType = MimeType.PDF,
                )
                writeToTempFile(buffer, MimeType.PDF)
            }.onSuccess { file ->
                eventHandler.send(HideLoading)
                eventHandler.send(ShareFileEvent(file, MimeType.PDF.key))
            }.onFailure {
                eventHandler.send(HideLoading)
                eventHandler.send(ShowErrorDialogEvent(error = it))
            }
        }
    }
)

DesignEditor(engineConfiguration = engineConfiguration) {
    navController.popBackStack()
}
```

The preceding code:

- Tells the default handler to export design scenes to PDF.
- Writes the PDF to a temp file and shares it.
- Displays loading and error states using the event handler.

## Adding Options to Export

For more complex configurations, you can use `ExportOptions` to customize the PDF output. The `onExport` callback gets access to the engine and event handler.

```kotlin
val engineConfiguration = EngineConfiguration.remember(
    license = "<your license here>",
    onExport = {
        val engine = editorContext.engine
        val eventHandler = editorContext.eventHandler
        EditorDefaults.run {
            when (engine.scene.getMode()) {
                SceneMode.VIDEO -> {
                    val page = engine.scene.getCurrentPage() ?: engine.scene.getPages()[0]
                    runCatching {
                        val buffer = engine.block.exportVideo(
                            block = page,
                            timeOffset = 0.0,
                            duration = engine.block.getDuration(page),
                            mimeType = MimeType.MP4,
                        )
                        writeToTempFile(buffer, MimeType.MP4)
                    }.onSuccess { file ->
                        eventHandler.send(ShareFileEvent(file, MimeType.MP4.key))
                    }
                }
                else -> {
                    eventHandler.send(ShowLoading)
                    runCatching {
                        val options = ExportOptions(
                            exportPdfWithHighCompatibility = true,
                        )
                        val buffer = engine.block.export(
                            block = requireNotNull(engine.scene.get()),
                            mimeType = MimeType.PDF,
                            options = options,
                        )
                        writeToTempFile(buffer, MimeType.PDF)
                    }.onSuccess { file ->
                        eventHandler.send(HideLoading)
                        eventHandler.send(ShareFileEvent(file, MimeType.PDF.key))
                    }.onFailure {
                        eventHandler.send(HideLoading)
                        eventHandler.send(ShowErrorDialogEvent(error = it))
                    }
                }
            }
        }
    }
)
```

The preceding code creates an `ExportOptions` object and passes it to the PDF export function. You can configure additional options like underlayer generation and DPI settings.

Once the PDF has been written to disk, the callback passes it to the event handler to display the share dialog. For video scenes, the callback exports as MP4 instead.

## Export Options

The `ExportOptions` class provides these parameters for PDF customization:

```kotlin
val options = ExportOptions(
    exportPdfWithHighCompatibility = true,  // Flatten complex elements
    exportPdfWithUnderlayer = true,         // Generate print underlayer
    underlayerSpotColorName = "White",      // Spot color for underlayer ink
    underlayerOffset = -2.0f,                // Offset in design units
)
```

**Available options:**

- `exportPdfWithHighCompatibility`: Flatten PDF for better compatibility with older viewers.
- `exportPdfWithUnderlayer`: Generate an underlayer shape for specialized printing (fabric, glass).
- `underlayerSpotColorName`: Specify the spot color name for the underlayer ink.
- `underlayerOffset`: Adjust underlayer size with positive (larger) or negative (smaller) offset.

> **Note:** When using underlayer, do not flatten the resulting PDF or you will remove the underlayer. The underlayer sits behind your design as a separate layer.

## Troubleshooting

**❌ Export still shares PNG/MP4**:

- Ensure `MimeType.PDF` is specified in the `onExport` callback.
- Verify the callback is properly configured in `EngineConfiguration`.

**❌ PDF looks soft**:

- Check the "scene/dpi" property of the scene and increase it if necessary.
- Ensure placed images have enough pixels to cover the frame.

**❌ Underlayer absent in output**:

- Verify the spot color name is correct and matches what the printer expects.
- Ensure `exportPdfWithUnderlayer = true` is set in `ExportOptions`.
- Do not flatten the PDF or the underlayer will be lost.

**❌ Video scene shows different flow**:

- This is expected. The SDK exports videos slightly differently than static image scenes.

## Next Steps

Now that you know how to configure the editor to export to PDF, here are some topics to explore:

- [Spot Colors](https://img.ly/docs/cesdk/android/colors-a9b79c/) – use spot colors for specialized printing.
- [Asset Sources & Upload](https://img.ly/docs/cesdk/android/import-media-4e3703/) – bring user images/videos in, then export as PDF.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
