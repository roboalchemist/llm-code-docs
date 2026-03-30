# Source: https://img.ly/docs/cesdk/android/user-interface/events-514b70/

---
title: "UI Events"
description: "Listen to UI events and trigger custom logic based on user interactions in the editor interface."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/events-514b70/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [UI Events](https://img.ly/docs/cesdk/android/user-interface/events-514b70/)

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

In this example, we will show you how to configure the callbacks of various editor events for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Note that the bodies of all callbacks except `onUpload` are copied from the `Design Editor` default implementations.

## Configuration

All the callback configurations are part of the `EngineConfiguration` class. Note that all the callbacks receive `EditorEventHandler` parameter that can be used to send UI events.

- `onCreate` - the callback that is invoked when the editor is created. This is the main initialization block of both the editor and engine. Normally, you should [load](https://img.ly/docs/cesdk/android/open-the-editor/load-scene-478833/) or [create](https://img.ly/docs/cesdk/android/open-the-editor/blank-canvas-18ff05/) a scene as well as prepare asset sources in this block. We recommend that you check the availability of the scene before creating/loading a new scene since a recreated scene may already exist if the callback is invoked after a process recreation. Callback does not have a default implementation, as default scenes are solution-specific, however, `EditorDefaults.onCreate` contains the default logic. By default, it loads a scene and adds all default and demo asset sources. Note that the "create" coroutine job will survive configuration changes and will be cancelled only if the editor is closed or the process is killed when in the background.

```kotlin highlight-configuration-onCreate
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
```

- `onExport` - the callback that is invoked when the export button is tapped. You may want to call one of the [export functions](https://img.ly/docs/cesdk/android/export-save-publish/export/overview-9ed3a8/) in this callback. The default implementations call `BlockApi.export` or `BlockApi.exportVideo`, write the content into a temporary file and open a system dialog for sharing the exported file. Note that the "export" coroutine job will survive configuration changes and will be cancelled only if the editor is closed or the process is killed when in the background

```kotlin highlight-configuration-onExport
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
```

- `onUpload` - the callback that is invoked after an asset is added to `UploadAssetSourceType`. When selecting an asset to upload, a default `AssetDefinition` object is constructed based on the selected asset and the callback is invoked. By default, the callback leaves the asset definition unmodified and returns the same object. However, you may want to upload the selected asset to your server before adding it to the scene. This example demonstrates how you can access the URI of the new asset, use it to upload the file to your server, and then replace the URI with the URI of your server. Note that the "upload" coroutine job will survive configuration changes and will be cancelled only if the editor is closed or the process is killed when in the background.

```kotlin highlight-configuration-onUpload
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
```

- `onClose` - the callback that is invoked after a tap on the navigation icon of the toolbar or on the system back button. The callback receives a boolean parameter that indicates whether editor has unsaved changes. Default implementation sends `ShowCloseConfirmationDialogEvent` event in case that parameter is `true` and closes the editor if it is `false`. Note that the "close" coroutine job will survive configuration changes and will be cancelled only if the editor is closed or the process is killed when in the background.

```kotlin highlight-configuration-onClose
onClose = { hasUnsavedChanges ->
    if (hasUnsavedChanges) {
        editorContext.eventHandler.send(ShowCloseConfirmationDialogEvent)
    } else {
        editorContext.eventHandler.send(EditorEvent.CloseEditor())
    }
},
```

- `onError` - the callback that is invoked after the editor captures an error. Default implementation sends `ShowErrorDialogEvent` event which displays a popup dialog with action button that closes the editor. Note that the "error" coroutine job will survive configuration changes and will be cancelled only if the editor is closed or the process is killed when in the background.

```kotlin highlight-configuration-onError
onError = { error ->
    editorContext.eventHandler.send(ShowErrorDialogEvent(error))
},
```

### Full Code

Here's the full code for configuring events:

```kotlin
import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import kotlinx.coroutines.Job
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import ly.img.editor.DesignEditor
import ly.img.editor.EditorDefaults
import ly.img.editor.EngineConfiguration
import ly.img.editor.HideLoading
import ly.img.editor.ShareFileEvent
import ly.img.editor.ShowCloseConfirmationDialogEvent
import ly.img.editor.ShowErrorDialogEvent
import ly.img.editor.ShowLoading
import ly.img.editor.core.event.EditorEvent
import ly.img.editor.core.library.data.TextAssetSource
import ly.img.editor.core.library.data.TypefaceProvider
import ly.img.engine.MimeType
import ly.img.engine.addDefaultAssetSources
import ly.img.engine.addDemoAssetSources

// Add this composable to your NavHost
@Composable
fun CallbacksEditorSolution(navController: NavHostController) {
    val engineConfiguration =
        EngineConfiguration.remember(
            license = "<your license here>",
            onCreate = {
                // Note that lambda is copied from EditorDefaults.onCreate
                coroutineScope {
                    // In case of process recovery, engine automatically recovers the scene that is why we need to check
                    if (editorContext.engine.scene.get() == null) {
                        editorContext.engine.scene.load(EngineConfiguration.defaultDesignSceneUri)
                    }
                    launch {
                        val baseUri = Uri.parse("https://cdn.img.ly/assets/v4")
                        editorContext.engine.addDefaultAssetSources(baseUri = baseUri)
                        val defaultTypeface = TypefaceProvider().provideTypeface(editorContext.engine, "Roboto")
                        requireNotNull(defaultTypeface)
                        editorContext.engine.asset.addSource(TextAssetSource(editorContext.engine, defaultTypeface))
                    }
                    launch {
                        editorContext.engine.addDemoAssetSources(
                            sceneMode = editorContext.engine.scene.getMode(),
                            withUploadAssetSources = true,
                            baseUri = Uri.parse("https://cdn.img.ly/assets/demo/v3"),
                        )
                    }
                    coroutineContext[Job]?.invokeOnCompletion {
                        editorContext.eventHandler.send(HideLoading)
                    }
                }
            },
            onExport = {
                EditorDefaults.run {
                    editorContext.eventHandler.send(ShowLoading)
                    val blob =
                        editorContext.engine.block.export(
                            block = requireNotNull(editorContext.engine.scene.get()),
                            mimeType = MimeType.PDF,
                        ) {
                            scene.getPages().forEach {
                                block.setScopeEnabled(it, key = "layer/visibility", enabled = true)
                                block.setVisible(it, visible = true)
                            }
                        }
                    val tempFile = writeToTempFile(blob)
                    editorContext.eventHandler.send(HideLoading)
                    editorContext.eventHandler.send(ShareFileEvent(tempFile, MimeType.PDF.key))
                }
            },
            onUpload = { assetDefinition, _ ->
                val meta = assetDefinition.meta ?: return@remember assetDefinition
                val sourceUri = Uri.parse(meta["uri"])
                val uploadedUri = sourceUri // todo upload the asset here and return remote uri
                val newMeta =
                    meta +
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

## Updating the UI

When working with the callbacks, you may want to make UI updates before, during, or after the callback execution. This is when UI events come to help. All the callbacks receive an extra parameter EditorEventHandler, which can be used to send editor events. By default, there are existing ui events, which can be found in Events.kt file (i.e. ShowLoading, HideLoading etc).

```kotlin
            onCreate = {
                EditorDefaults.onCreate(
                    engine = editorContext.engine,
                    sceneUri = EngineConfiguration.defaultDesignSceneUri,
                    eventHandler = editorContext.eventHandler,
                )
                editorContext.eventHandler.send(OnCreateCustomEvent)
            },
```

You may want to declare your own custom event. Simply inherit from class EditorEvent.

```kotlin
data object OnCreateCustomEvent : EditorEvent
```

After declaring the event, you can send the UI event using send function. Note that EditorEventHandler has another function called sendCloseEditorEvent, which can be used to forcefully close the mobile editor.

```kotlin
                editorContext.eventHandler.send(OnCreateCustomEvent)

```

Once the event is sent, it can be captured in EditorConfiguration.onEvent. The lambda contains three parameters: activity, state and of course, the captured event. In this example, the editor state is of default type EditorUiState (initially provided in initialState), however, you can have your own state class that wraps the EditorUiState or does not contain EditorUiState at all. The only requirement is that it should be Parcelable. The lambda should return the updated state, which, if changed, will trigger overlay composable to be recomposed and the overlaying ui components will be updated.

```kotlin
            onEvent = { state, event ->
                when (event) {
                    OnCreateCustomEvent -> {
                        Toast.makeText(editorContext.activity, "Editor is created!", Toast.LENGTH_SHORT).show()
                        state
                    }
                    ShowLoading -> {
                        state.copy(showLoading = true)
                    }
                    else -> {
                        // handle other default events
                        EditorDefaults.onEvent(editorContext.activity, state, event)
                    }
                }
            },
```

To handle your brand new custom event, simply check the type of the event and handle it per your needs.

```kotlin
                    OnCreateCustomEvent -> {
                        Toast.makeText(editorContext.activity, "Editor is created!", Toast.LENGTH_SHORT).show()
                        state
                    }
```

Besides, you can override the behavior of existing events too. Simply extend your when block and override the behavior.

```kotlin
                    ShowLoading -> {
                        state.copy(showLoading = true)
                    }
```

If you want to leave the behavior of remaining default events unchanged, simply return the result of EditorDefaults.onEvent in the else block.

```kotlin
                    else -> {
                        // handle other default events
                        EditorDefaults.onEvent(editorContext.activity, state, event)
                    }
```

### Full Code

Here's the full code for making UI updates before, during, or after the callback execution

```kotlin
import android.widget.Toast
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EditorConfiguration
import ly.img.editor.EditorDefaults
import ly.img.editor.EditorUiState
import ly.img.editor.EngineConfiguration
import ly.img.editor.ShowLoading
import ly.img.editor.core.event.EditorEvent

data object OnCreateCustomEvent : EditorEvent

// Add this composable to your NavHost
@Composable
fun UiEventsEditorSolution(navController: NavHostController) {
    val engineConfiguration =
        EngineConfiguration.remember(
            license = "<your license here>",
            onCreate = {
                EditorDefaults.onCreate(
                    engine = editorContext.engine,
                    sceneUri = EngineConfiguration.defaultDesignSceneUri,
                    eventHandler = editorContext.eventHandler,
                )
                editorContext.eventHandler.send(OnCreateCustomEvent)
            },
        )
    val editorConfiguration =
        EditorConfiguration.remember(
            initialState = EditorUiState(),
            onEvent = { state, event ->
                when (event) {
                    OnCreateCustomEvent -> {
                        Toast.makeText(editorContext.activity, "Editor is created!", Toast.LENGTH_SHORT).show()
                        state
                    }
                    ShowLoading -> {
                        state.copy(showLoading = true)
                    }
                    else -> {
                        // handle other default events
                        EditorDefaults.onEvent(editorContext.activity, state, event)
                    }
                }
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
