# Source: https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/

---
title: "Customize"
description: "Adapt the asset library UI and behavior to suit your application's structure and user needs."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/mac-catalyst/import-media-4e3703/) > [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-library-65d6c4/) > [Customize](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/)

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-asset-library/DefaultAssetLibraryEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct DefaultAssetLibraryEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  @MainActor
  var editor: some View {
    DesignEditor(settings)
      .imgly.onCreate { engine in
        try await OnCreate.loadScene(from: DesignEditor.defaultScene)(engine)
        try engine.asset.addSource(UnsplashAssetSource(host: secrets.unsplashHost))
      }
      .imgly.assetLibrary {
        DefaultAssetLibrary(
          tabs: DefaultAssetLibrary.Tab.allCases.reversed().filter { tab in
            tab != .elements && tab != .photoRoll
          },
        )
        .images {
          AssetLibrarySource.image(.title("Unsplash"), source: .init(id: UnsplashAssetSource.id))
          DefaultAssetLibrary.images
        }
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
  DefaultAssetLibraryEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-asset-library/CustomAssetLibraryEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct CustomAssetLibraryEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  @MainActor
  var editor: some View {
    DesignEditor(settings)
      .imgly.onCreate { engine in
        try await OnCreate.loadScene(from: DesignEditor.defaultScene)(engine)
        try engine.asset.addSource(UnsplashAssetSource(host: secrets.unsplashHost))
      }
      .imgly.assetLibrary {
        CustomAssetLibrary()
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
  CustomAssetLibraryEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-asset-library/CustomAssetLibrary.swift reference-only
import IMGLYEditor
import IMGLYEngine
import SwiftUI

@MainActor
struct CustomAssetLibrary: AssetLibrary {

  @AssetLibraryBuilder func photoRoll(_ sceneMode: SceneMode?) -> AssetLibraryContent {
    AssetLibrarySource.photoRoll(
      .title("Photo Roll"),
      media: sceneMode == .video ? [.image, .video] : [.image],
    )
  }

  @AssetLibraryBuilder var videosAndImages: AssetLibraryContent {
    AssetLibraryGroup.video("Videos") { videos }
    AssetLibraryGroup.image("Images") { images }
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.image, .video])
  }

  @AssetLibraryBuilder var videos: AssetLibraryContent {
    AssetLibrarySource.video(.title("Videos"), source: .init(demoSource: .video))
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.video])
  }

  @AssetLibraryBuilder var audio: AssetLibraryContent {
    AssetLibrarySource.audio(.title("Audio"), source: .init(demoSource: .audio))
    AssetLibrarySource.audioUpload(.title("Uploads"), source: .init(demoSource: .audioUpload))
  }

  @AssetLibraryBuilder var images: AssetLibraryContent {
    AssetLibrarySource.image(.title("Unsplash"), source: .init(id: UnsplashAssetSource.id))
    AssetLibrarySource.image(.title("Images"), source: .init(demoSource: .image))
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.image])
  }

  @AssetLibraryBuilder var text: AssetLibraryContent {
    AssetLibrarySource.text(.title("Plain Text"), source: .init(id: TextAssetSource.id))
    AssetLibrarySource.textComponent(.title("Text Designs"), source: .init(demoSource: .textComponents))
  }

  @AssetLibraryBuilder var shapes: AssetLibraryContent {
    AssetLibrarySource.shape(.title("Basic"), source: .init(
      defaultSource: .vectorPath, config: .init(groups: ["//ly.img.cesdk.vectorpaths/category/vectorpaths"])))
    AssetLibrarySource.shape(.title("Abstract"), source: .init(
      defaultSource: .vectorPath, config: .init(groups: ["//ly.img.cesdk.vectorpaths.abstract/category/abstract"])))
  }

  @AssetLibraryBuilder var stickers: AssetLibraryContent {
    AssetLibrarySource.sticker(.titleForGroup { group in
      if let name = group?.split(separator: "/").last {
        "\(name.capitalized)"
      } else {
        "Stickers"
      }
    }, source: .init(defaultSource: .sticker))
  }

  @AssetLibraryBuilder func elements(_ sceneMode: SceneMode?) -> AssetLibraryContent {
    photoRoll(sceneMode)
    if sceneMode == .video {
      AssetLibraryGroup.video("Videos") { videos }
      AssetLibraryGroup.audio("Audio") { audio }
    }
    AssetLibraryGroup.image("Images") { images }
    AssetLibraryGroup.text("Text", excludedPreviewSources: [Engine.DemoAssetSource.textComponents.rawValue]) {
      text
    }
    AssetLibraryGroup.shape("Shapes") { shapes }
    AssetLibraryGroup.sticker("Stickers") { stickers }
  }

  @ViewBuilder var photoRollTab: some View {
    AssetLibrarySceneModeReader { sceneMode in
      AssetLibraryTab("Photo Roll") { photoRoll(sceneMode) } label: { DefaultAssetLibrary.photoRollLabel($0) }
    }
  }

  @ViewBuilder var elementsTab: some View {
    AssetLibrarySceneModeReader { sceneMode in
      AssetLibraryTab("Elements") { elements(sceneMode) } label: { DefaultAssetLibrary.elementsLabel($0) }
    }
  }

  @ViewBuilder var videosTab: some View {
    AssetLibraryTab("Videos") { videos } label: { DefaultAssetLibrary.videosLabel($0) }
  }

  @ViewBuilder var audioTab: some View {
    AssetLibraryTab("Audio") { audio } label: { DefaultAssetLibrary.audioLabel($0) }
  }

  @ViewBuilder var imagesTab: some View {
    AssetLibraryTab("Images") { images } label: { DefaultAssetLibrary.imagesLabel($0) }
  }

  @ViewBuilder var textTab: some View {
    AssetLibraryTab("Text") { text } label: { DefaultAssetLibrary.textLabel($0) }
  }

  @ViewBuilder var shapesTab: some View {
    AssetLibraryTab("Shapes") { shapes } label: { DefaultAssetLibrary.shapesLabel($0) }
  }

  @ViewBuilder var stickersTab: some View {
    AssetLibraryTab("Stickers") { stickers } label: { DefaultAssetLibrary.stickersLabel($0) }
  }

  @ViewBuilder public var clipsTab: some View {
    AssetLibraryTab("Clips") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var overlaysTab: some View {
    AssetLibraryTab("Overlays") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var stickersAndShapesTab: some View {
    AssetLibraryTab("Stickers") {
      stickers
      shapes
    } label: { _ in EmptyView() }
  }

  var body: some View {
    TabView {
      AssetLibrarySceneModeReader { sceneMode in
        if sceneMode == .video {
          elementsTab
          photoRollTab
          videosTab
          audioTab
          AssetLibraryMoreTab {
            imagesTab
            textTab
            shapesTab
            stickersTab
          }
        } else {
          elementsTab
          imagesTab
          textTab
          shapesTab
          stickersTab
        }
      }
    }
  }
}
```

In this example, we will show you how to customize the asset library for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/mac-catalyst/prebuilt-solutions-d0ed07/).

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-asset-library/).

## Modifiers

After initializing an editor SwiftUI view you can apply any SwiftUI *modifier* to customize it like for any other SwiftUI view.
All public Swift `extension`s of existing types provided by IMG.LY, e.g., for the SwiftUI `View` protocol, are exposed in a separate `.imgly` property namespace.
The asset library configuration to customize the editor is no exception to this rule and is implemented as a SwiftUI *modifier*.

```swift highlight-editor-default
DesignEditor(settings)
```

- `assetLibrary` - the asset library UI definition used by the editor. The result of the trailing closure needs to conform to the `AssetLibrary` protocol. By default, the predefined `DefaultAssetLibrary` is used.

```swift highlight-assetLibrary-default
.imgly.assetLibrary {
  DefaultAssetLibrary(
    tabs: DefaultAssetLibrary.Tab.allCases.reversed().filter { tab in
      tab != .elements && tab != .photoRoll
    },
  )
  .images {
    AssetLibrarySource.image(.title("Unsplash"), source: .init(id: UnsplashAssetSource.id))
    DefaultAssetLibrary.images
  }
}
```

### Custom Asset Source

To use custom asset sources in the asset library UI, the custom asset source must be first added to the engine. In addition to creating or loading a scene, registering the asset sources should be done in the [callback](https://img.ly/docs/cesdk/mac-catalyst/user-interface/events-514b70/). In this example, the `OnCreate.loadScene` default implementation is used and afterward, the [custom](https://img.ly/docs/cesdk/mac-catalyst/import-media/from-remote-source/unsplash-8f31f0/) is added.

```swift highlight-assetSource-default
.imgly.onCreate { engine in
  try await OnCreate.loadScene(from: DesignEditor.defaultScene)(engine)
  try engine.asset.addSource(UnsplashAssetSource(host: secrets.unsplashHost))
}
```

### Default Asset Library

The `DefaultAssetLibrary` is a predefined `AssetLibrary` intended to quickly customize some parts of the default asset library without implementing a complete `AssetLibrary` from scratch. It can be initialized with a custom selection and ordering of the available tabs. In this example, we reverse the ordering and exclude the elements and photo roll tab.

```swift highlight-defaultAssetLibrary
DefaultAssetLibrary(
  tabs: DefaultAssetLibrary.Tab.allCases.reversed().filter { tab in
    tab != .elements && tab != .photoRoll
  },
)
```

### Asset Library Builder

The content of some of the tabs can be changed with *modifiers* that are defined on the `DefaultAssetLibrary` type and expect a trailing `@AssetLibraryBuilder` closure similar to regular SwiftUI `@ViewBuilder` closures. These type-bound *modifiers* are `videos`, `audio`, `images`, `shapes`, and `stickers`. The elements tab will then be generated with these definitions. In this example, we reuse the `DefaultAssetLibrary.images` default implementation and add a new `AssetLibrarySource` for the [previously added](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/) which will add a new "Unsplash" section to the asset library UI.

```swift highlight-defaultAssetLibraryImages
.images {
  AssetLibrarySource.image(.title("Unsplash"), source: .init(id: UnsplashAssetSource.id))
  DefaultAssetLibrary.images
}
```

### Custom Asset Library

If the `DefaultAssetLibrary` is not customizable enough for your use case you can create your own custom `AssetLibrary`.

```swift highlight-assetLibrary-custom
.imgly.assetLibrary {
  CustomAssetLibrary()
}
```

In this example, we did exactly that by creating the `CustomAssetLibrary`. It resembles the above customized `DefaultAssetLibrary` with the added `UnsplashAssetSource` but without the custom tab configuration which is not needed as you control every section, layout, and grouping.

```swift highlight-customAssetLibrary
import IMGLYEditor
import IMGLYEngine
import SwiftUI

@MainActor
struct CustomAssetLibrary: AssetLibrary {
```

As used above for customizing the `DefaultAssetLibrary` with its *modifiers*, the `@AssetLibraryBuilder` concept is the foundation to quickly create any asset library hierarchy. It behaves and feels like the regular SwiftUI `@ViewBuilder` syntax. You compose your asset library out of `AssetLibrarySource`s that can be organized in named `AssetLibraryGroup`s. There are different flavors of these two for each asset type which define the used asset preview and section styling.

```swift highlight-assetLibraryBuilder
  @AssetLibraryBuilder func photoRoll(_ sceneMode: SceneMode?) -> AssetLibraryContent {
    AssetLibrarySource.photoRoll(
      .title("Photo Roll"),
      media: sceneMode == .video ? [.image, .video] : [.image],
    )
  }

  @AssetLibraryBuilder var videosAndImages: AssetLibraryContent {
    AssetLibraryGroup.video("Videos") { videos }
    AssetLibraryGroup.image("Images") { images }
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.image, .video])
  }

  @AssetLibraryBuilder var videos: AssetLibraryContent {
    AssetLibrarySource.video(.title("Videos"), source: .init(demoSource: .video))
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.video])
  }

  @AssetLibraryBuilder var audio: AssetLibraryContent {
    AssetLibrarySource.audio(.title("Audio"), source: .init(demoSource: .audio))
    AssetLibrarySource.audioUpload(.title("Uploads"), source: .init(demoSource: .audioUpload))
  }

  @AssetLibraryBuilder var images: AssetLibraryContent {
    AssetLibrarySource.image(.title("Unsplash"), source: .init(id: UnsplashAssetSource.id))
    AssetLibrarySource.image(.title("Images"), source: .init(demoSource: .image))
    AssetLibrarySource.photoRoll(.title("Photo Roll"), media: [.image])
  }

  @AssetLibraryBuilder var text: AssetLibraryContent {
    AssetLibrarySource.text(.title("Plain Text"), source: .init(id: TextAssetSource.id))
    AssetLibrarySource.textComponent(.title("Text Designs"), source: .init(demoSource: .textComponents))
  }

  @AssetLibraryBuilder var shapes: AssetLibraryContent {
    AssetLibrarySource.shape(.title("Basic"), source: .init(
      defaultSource: .vectorPath, config: .init(groups: ["//ly.img.cesdk.vectorpaths/category/vectorpaths"])))
    AssetLibrarySource.shape(.title("Abstract"), source: .init(
      defaultSource: .vectorPath, config: .init(groups: ["//ly.img.cesdk.vectorpaths.abstract/category/abstract"])))
  }

  @AssetLibraryBuilder var stickers: AssetLibraryContent {
    AssetLibrarySource.sticker(.titleForGroup { group in
      if let name = group?.split(separator: "/").last {
        "\(name.capitalized)"
      } else {
        "Stickers"
      }
    }, source: .init(defaultSource: .sticker))
  }

  @AssetLibraryBuilder func elements(_ sceneMode: SceneMode?) -> AssetLibraryContent {
    photoRoll(sceneMode)
    if sceneMode == .video {
      AssetLibraryGroup.video("Videos") { videos }
      AssetLibraryGroup.audio("Audio") { audio }
    }
    AssetLibraryGroup.image("Images") { images }
    AssetLibraryGroup.text("Text", excludedPreviewSources: [Engine.DemoAssetSource.textComponents.rawValue]) {
      text
    }
    AssetLibraryGroup.shape("Shapes") { shapes }
    AssetLibraryGroup.sticker("Stickers") { stickers }
  }
```

To compose a SwiftUI view for any `AssetLibraryBuilder` result you use an `AssetLibraryTab` which can be added to your view hierarchy. In this example, we reuse the labels defined in the `DefaultAssetLibrary` but you can also use your own SwiftUI `Label` or any other view. The argument of the `label` closure just forwards the title that was used to initialize the `AssetLibraryTab` so that you don't have to type it twice.

```swift highlight-assetLibraryView
  @ViewBuilder var photoRollTab: some View {
    AssetLibrarySceneModeReader { sceneMode in
      AssetLibraryTab("Photo Roll") { photoRoll(sceneMode) } label: { DefaultAssetLibrary.photoRollLabel($0) }
    }
  }

  @ViewBuilder var elementsTab: some View {
    AssetLibrarySceneModeReader { sceneMode in
      AssetLibraryTab("Elements") { elements(sceneMode) } label: { DefaultAssetLibrary.elementsLabel($0) }
    }
  }

  @ViewBuilder var videosTab: some View {
    AssetLibraryTab("Videos") { videos } label: { DefaultAssetLibrary.videosLabel($0) }
  }

  @ViewBuilder var audioTab: some View {
    AssetLibraryTab("Audio") { audio } label: { DefaultAssetLibrary.audioLabel($0) }
  }

  @ViewBuilder var imagesTab: some View {
    AssetLibraryTab("Images") { images } label: { DefaultAssetLibrary.imagesLabel($0) }
  }

  @ViewBuilder var textTab: some View {
    AssetLibraryTab("Text") { text } label: { DefaultAssetLibrary.textLabel($0) }
  }

  @ViewBuilder var shapesTab: some View {
    AssetLibraryTab("Shapes") { shapes } label: { DefaultAssetLibrary.shapesLabel($0) }
  }

  @ViewBuilder var stickersTab: some View {
    AssetLibraryTab("Stickers") { stickers } label: { DefaultAssetLibrary.stickersLabel($0) }
  }

  @ViewBuilder public var clipsTab: some View {
    AssetLibraryTab("Clips") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var overlaysTab: some View {
    AssetLibraryTab("Overlays") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var stickersAndShapesTab: some View {
    AssetLibraryTab("Stickers") {
      stickers
      shapes
    } label: { _ in EmptyView() }
  }

```

### Asset Library `body` View

Finally, multiple `AssetLibraryTab`s are ready to be used in a SwiftUI `TabView` environment. Use an `AssetLibraryMoreTab` if you have more than five tabs to workaround various SwiftUI `TabView` shortcomings. Editor solutions with a floating "+" action button (FAB) show this `AssetLibrary.body` `View`.

```swift highlight-assetLibraryTabView
var body: some View {
  TabView {
    AssetLibrarySceneModeReader { sceneMode in
      if sceneMode == .video {
        elementsTab
        photoRollTab
        videosTab
        audioTab
        AssetLibraryMoreTab {
          imagesTab
          textTab
          shapesTab
          stickersTab
        }
      } else {
        elementsTab
        imagesTab
        textTab
        shapesTab
        stickersTab
      }
    }
  }
}
```

### Asset Library Tab Views

In addition to its `View.body`, the `AssetLibrary` protocol requires to define `elementsTab`, `videosTab`, `audioTab`, `imagesTab`, `textTab`, `shapesTab`, and `stickersTab` `View`s. These are used when displaying isolated asset libraries just for the corresponding asset type, e.g., for replacing an asset.

```swift highlight-assetLibraryTabViews
  @ViewBuilder var elementsTab: some View {
    AssetLibrarySceneModeReader { sceneMode in
      AssetLibraryTab("Elements") { elements(sceneMode) } label: { DefaultAssetLibrary.elementsLabel($0) }
    }
  }

  @ViewBuilder var videosTab: some View {
    AssetLibraryTab("Videos") { videos } label: { DefaultAssetLibrary.videosLabel($0) }
  }

  @ViewBuilder var audioTab: some View {
    AssetLibraryTab("Audio") { audio } label: { DefaultAssetLibrary.audioLabel($0) }
  }

  @ViewBuilder var imagesTab: some View {
    AssetLibraryTab("Images") { images } label: { DefaultAssetLibrary.imagesLabel($0) }
  }

  @ViewBuilder var textTab: some View {
    AssetLibraryTab("Text") { text } label: { DefaultAssetLibrary.textLabel($0) }
  }

  @ViewBuilder var shapesTab: some View {
    AssetLibraryTab("Shapes") { shapes } label: { DefaultAssetLibrary.shapesLabel($0) }
  }

  @ViewBuilder var stickersTab: some View {
    AssetLibraryTab("Stickers") { stickers } label: { DefaultAssetLibrary.stickersLabel($0) }
  }
```

For the video editor solution, it is also required to define `clipsTab`, `overlaysTab`, and `stickersAndShapesTab` `View`s. These composed libraries are used as entry points instead of the FAB.

```swift highlight-assetLibraryVideoEditor
  @ViewBuilder public var clipsTab: some View {
    AssetLibraryTab("Clips") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var overlaysTab: some View {
    AssetLibraryTab("Overlays") { videosAndImages } label: { _ in EmptyView() }
  }

  @ViewBuilder public var stickersAndShapesTab: some View {
    AssetLibraryTab("Stickers") {
      stickers
      shapes
    } label: { _ in EmptyView() }
  }
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
