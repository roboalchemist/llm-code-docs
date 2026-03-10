# Source: https://img.ly/docs/cesdk/ios/user-interface/events-514b70/

---
title: "UI Events"
description: "Listen to UI events and trigger custom logic based on user interactions in the editor interface."
platform: ios
url: "https://img.ly/docs/cesdk/ios/user-interface/events-514b70/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/ios/user-interface-5a089a/) > [UI Events](https://img.ly/docs/cesdk/ios/user-interface/events-514b70/)

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-callbacks/CallbacksEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import IMGLYEngine

import SwiftUI

private enum CallbackError: Error {
  case unknownSceneMode
  case noScene
  case noPage
  case couldNotExport
}

struct CallbacksEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.onCreate { engine in
        // Load or create scene
        try await engine.scene.load(from: DesignEditor.defaultScene) // or `engine.scene.create*`
        // Add asset sources
        try await engine.addDefaultAssetSources(baseURL: Engine.assetBaseURL)
        try await engine.addDemoAssetSources(sceneMode: engine.scene.getMode(),
                                             withUploadAssetSources: true)
        try await engine.asset.addSource(TextAssetSource(engine: engine))
        try engine.asset.addSource(PhotoRollAssetSource(engine: engine))
      }
      .imgly.onExport { mainEngine, eventHandler in
        // Export design scene
        @MainActor func export() async throws -> (Data, MIMEType) {
          guard let scene = try mainEngine.scene.get() else {
            throw CallbackError.noScene
          }
          let mimeType: MIMEType = .pdf
          let data = try await mainEngine.block.export(scene, mimeType: mimeType) { backgroundEngine in
            // Modify state of the background engine for export without affecting
            // the main engine that renders the preview on the canvas
            try backgroundEngine.scene.getPages().forEach {
              try backgroundEngine.block.setScopeEnabled($0, key: "layer/visibility", enabled: true)
              try backgroundEngine.block.setVisible($0, visible: true)
            }
          }
          return (data, mimeType)
        }

        // Export video scene
        @MainActor func exportVideo() async throws -> (Data, MIMEType) {
          guard let page = try mainEngine.scene.getCurrentPage() else {
            throw CallbackError.noPage
          }
          eventHandler.send(.exportProgress(.relative(.zero)))
          let mimeType: MIMEType = .mp4
          let stream = try await mainEngine.block.exportVideo(page, mimeType: mimeType) { backgroundEngine in
            // Modify state of the background engine for export without affecting
            // the main engine that renders the preview on the canvas
          }
          for try await export in stream {
            try Task.checkCancellation()
            switch export {
            case let .progress(_, encodedFrames, totalFrames):
              let percentage = Float(encodedFrames) / Float(totalFrames)
              eventHandler.send(.exportProgress(.relative(percentage)))
            case let .finished(video: videoData):
              return (videoData, mimeType)
            }
          }
          try Task.checkCancellation()
          throw CallbackError.couldNotExport
        }

        // Export scene based on `SceneMode`
        let data: Data, mimeType: MIMEType
        switch try mainEngine.scene.getMode() {
        case .design: (data, mimeType) = try await export()
        case .video: (data, mimeType) = try await exportVideo()
        @unknown default:
          throw CallbackError.unknownSceneMode
        }

        // Write and share file
        let url = FileManager.default.temporaryDirectory.appendingPathComponent(
          "Export",
          conformingTo: mimeType.uniformType,
        )
        try data.write(to: url, options: [.atomic])
        switch try mainEngine.scene.getMode() {
        case .design: eventHandler.send(.shareFile(url))
        case .video: eventHandler.send(.exportCompleted { eventHandler.send(.shareFile(url)) })
        @unknown default:
          throw CallbackError.unknownSceneMode
        }
      }
      .imgly.onUpload { engine, sourceID, asset in
        var newMeta = asset.meta ?? [:]
        for (key, value) in newMeta {
          switch key {
          case "uri", "thumbUri":
            if let sourceURL = URL(string: value) {
              let uploadedURL = sourceURL // Upload the asset here and return remote URL
              newMeta[key] = uploadedURL.absoluteString
            }
          default:
            break
          }
        }
        return .init(id: asset.id, groups: asset.groups, meta: newMeta, label: asset.label, tags: asset.tags)
      }
      .imgly.onClose { engine, eventHandler in
        let hasUnsavedChanges = (try? engine.editor.canUndo()) ?? false

        if hasUnsavedChanges {
          eventHandler.send(.showCloseConfirmationAlert)
        } else {
          eventHandler.send(.closeEditor)
        }
      }
      .imgly.onError { error, eventHandler in
        eventHandler.send(.showErrorAlert(error))
      }
      .imgly.onLoaded { context in
        // Example: Open the elements library sheet after the editor loaded as `Dock.Buttons.elementsLibrary()` would do.
        context.eventHandler.send(.openSheet(type: .libraryAdd { context.assetLibrary.elementsTab }))
      }
  }

  @State private var isPresented = false

  var body: some View {
    Button("Use the Editor") {
      isPresented = true
    }
    .fullScreenCover(isPresented: $isPresented) {
      ModalEditor {
        editor
      }
    }
  }
}

#Preview {
  CallbacksEditorSolution()
}
```

In this example, we will show you how to configure the callbacks of various editor events for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/ios/prebuilt-solutions-d0ed07/).

Note that the bodies of all callbacks except `onUpload` are copied from the `Design Editor` default implementations.

## Import

In addition to importing an editor module, you also need to import the engine module if you are explicitly referencing its symbols like `Engine` or `MIMEType` in the following.

```swift highlight-import
import IMGLYDesignEditor
import IMGLYEngine
```

## Modifiers

After initializing an editor SwiftUI view you can apply any SwiftUI *modifier* to customize it like for any other SwiftUI view.
All public Swift `extension`s of existing types provided by IMG.LY, e.g., for the SwiftUI `View` protocol, are exposed in a separate `.imgly` property namespace.
The callbacks to customize the editor behavior are no exception to this rule and are implemented as SwiftUI *modifiers*.

The default implementation of the callbacks depends on the used [editor solution](https://img.ly/docs/cesdk/ios/prebuilt-solutions-d0ed07/) as each editor provides the most reasonable default behavior for its use case with minimal required code.
In addition to controlling the engine, some of the callbacks receive the `EditorEventHandler` parameter that can be used to send UI events.

```swift highlight-editor
DesignEditor(settings)
```

- `onCreate` - the callback that is invoked when the editor is created. This is the main initialization block of both the editor and engine. Normally, you should [load](https://img.ly/docs/cesdk/ios/open-the-editor/load-scene-478833/) or [create](https://img.ly/docs/cesdk/ios/open-the-editor/blank-canvas-18ff05/) a scene as well as prepare asset sources in this block. This callback does not have a default implementation, as default scenes are solution-specific, however, `OnCreate.loadScene` contains the default logic for most solutions. By default, it loads a scene and adds all default and demo asset sources.

```swift highlight-onCreate
.imgly.onCreate { engine in
  // Load or create scene
  try await engine.scene.load(from: DesignEditor.defaultScene) // or `engine.scene.create*`
  // Add asset sources
  try await engine.addDefaultAssetSources(baseURL: Engine.assetBaseURL)
  try await engine.addDemoAssetSources(sceneMode: engine.scene.getMode(),
                                       withUploadAssetSources: true)
  try await engine.asset.addSource(TextAssetSource(engine: engine))
  try engine.asset.addSource(PhotoRollAssetSource(engine: engine))
}
```

- `onExport` - the callback that is invoked when the export button is tapped. You may want to call one of the [export functions](https://img.ly/docs/cesdk/ios/export-save-publish/export/overview-9ed3a8/) in this callback. The default implementations call `BlockAPI.export` or `BlockAPI.exportVideo` based on the engine's `SceneMode`, display a progress indicator for video exports, write the content into a temporary file, and open a system dialog for sharing the exported file.

```swift highlight-onExport
      .imgly.onExport { mainEngine, eventHandler in
        // Export design scene
        @MainActor func export() async throws -> (Data, MIMEType) {
          guard let scene = try mainEngine.scene.get() else {
            throw CallbackError.noScene
          }
          let mimeType: MIMEType = .pdf
          let data = try await mainEngine.block.export(scene, mimeType: mimeType) { backgroundEngine in
            // Modify state of the background engine for export without affecting
            // the main engine that renders the preview on the canvas
            try backgroundEngine.scene.getPages().forEach {
              try backgroundEngine.block.setScopeEnabled($0, key: "layer/visibility", enabled: true)
              try backgroundEngine.block.setVisible($0, visible: true)
            }
          }
          return (data, mimeType)
        }

        // Export video scene
        @MainActor func exportVideo() async throws -> (Data, MIMEType) {
          guard let page = try mainEngine.scene.getCurrentPage() else {
            throw CallbackError.noPage
          }
          eventHandler.send(.exportProgress(.relative(.zero)))
          let mimeType: MIMEType = .mp4
          let stream = try await mainEngine.block.exportVideo(page, mimeType: mimeType) { backgroundEngine in
            // Modify state of the background engine for export without affecting
            // the main engine that renders the preview on the canvas
          }
          for try await export in stream {
            try Task.checkCancellation()
            switch export {
            case let .progress(_, encodedFrames, totalFrames):
              let percentage = Float(encodedFrames) / Float(totalFrames)
              eventHandler.send(.exportProgress(.relative(percentage)))
            case let .finished(video: videoData):
              return (videoData, mimeType)
            }
          }
          try Task.checkCancellation()
          throw CallbackError.couldNotExport
        }

        // Export scene based on `SceneMode`
        let data: Data, mimeType: MIMEType
        switch try mainEngine.scene.getMode() {
        case .design: (data, mimeType) = try await export()
        case .video: (data, mimeType) = try await exportVideo()
        @unknown default:
          throw CallbackError.unknownSceneMode
        }

        // Write and share file
        let url = FileManager.default.temporaryDirectory.appendingPathComponent(
          "Export",
          conformingTo: mimeType.uniformType,
        )
        try data.write(to: url, options: [.atomic])
        switch try mainEngine.scene.getMode() {
        case .design: eventHandler.send(.shareFile(url))
        case .video: eventHandler.send(.exportCompleted { eventHandler.send(.shareFile(url)) })
        @unknown default:
          throw CallbackError.unknownSceneMode
        }
      }
```

- `onUpload` - the callback that is invoked after an asset is added to an asset source. When selecting an asset to upload, a default `AssetDefinition` object is constructed based on the selected asset and the callback is invoked. By default, the callback leaves the asset definition unmodified and returns the same object. However, you may want to upload the selected asset to your server before adding it to the scene. This example demonstrates how you can access the URL of the new asset, use it to upload the file to your server, and then replace the URL with the URL of your server.

```swift highlight-onUpload
.imgly.onUpload { engine, sourceID, asset in
  var newMeta = asset.meta ?? [:]
  for (key, value) in newMeta {
    switch key {
    case "uri", "thumbUri":
      if let sourceURL = URL(string: value) {
        let uploadedURL = sourceURL // Upload the asset here and return remote URL
        newMeta[key] = uploadedURL.absoluteString
      }
    default:
      break
    }
  }
  return .init(id: asset.id, groups: asset.groups, meta: newMeta, label: asset.label, tags: asset.tags)
}
```

- `onClose` - the callback that is invoked after a tap on the navigation icon of the navigation bar. The callback receives the engine. Default implementation sends `ShowCloseConfirmationAlert` event if there are unsaved changes and closes the editor if there are no unsaved changes.

```swift highlight-onClose
      .imgly.onClose { engine, eventHandler in
        let hasUnsavedChanges = (try? engine.editor.canUndo()) ?? false

        if hasUnsavedChanges {
          eventHandler.send(.showCloseConfirmationAlert)
        } else {
          eventHandler.send(.closeEditor)
        }
      }
```

- `onError` - the callback that is invoked when an error is thrown while loading the editor. Default implementation sends `ShowErrorAlert` event which displays an alert with action button that closes the editor.

```swift highlight-onError
.imgly.onError { error, eventHandler in
  eventHandler.send(.showErrorAlert(error))
}
```

- `onLoaded` - the callback that is invoked when the editor has been created and finished loading. The callback receives the `OnLoaded.Context` which includes the engine, the event handler, and the asset library. It is intended for programmatic UI operations or managing custom engine subscriptions. By default, an empty callback is executed.

```swift highlight-onLoaded
.imgly.onLoaded { context in
  // Example: Open the elements library sheet after the editor loaded as `Dock.Buttons.elementsLibrary()` would do.
  context.eventHandler.send(.openSheet(type: .libraryAdd { context.assetLibrary.elementsTab }))
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
