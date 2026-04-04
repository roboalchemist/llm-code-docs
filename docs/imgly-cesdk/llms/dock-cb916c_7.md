# Source: https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/dock-cb916c/

---
title: "Dock"
description: "Configure the dock area to show or hide tools, panels, or quick access actions."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/dock-cb916c/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-dock/DockEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct DockEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.dockItems { context in
        Dock.Buttons.elementsLibrary()
        Dock.Buttons.photoRoll()
        Dock.Buttons.systemCamera()
        Dock.Buttons.imagesLibrary()
        Dock.Buttons.textLibrary()
        Dock.Buttons.shapesLibrary()
        Dock.Buttons.stickersLibrary()
        Dock.Buttons.resize()
      }
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(id: "my.package.dock.button.first") { context in
            print("First Button action")
          } label: { context in
            Label("First Button", systemImage: "arrow.backward.circle")
          }
        }
        items.addLast {
          Dock.Button(id: "my.package.dock.button.last") { context in
            print("Last Button action")
          } label: { context in
            Label("Last Button", systemImage: "arrow.forward.circle")
          }
        }
        items.addAfter(id: Dock.Buttons.ID.photoRoll) {
          Dock.Button(id: "my.package.dock.button.afterPhotoRoll") { context in
            print("After Photo Roll action")
          } label: { context in
            Label("After Photo Roll", systemImage: "arrow.forward.square")
          }
        }
        items.addBefore(id: Dock.Buttons.ID.systemCamera) {
          Dock.Button(id: "my.package.dock.button.beforeSystemCamera") { context in
            print("Before Camera action")
          } label: { context in
            Label("Before Camera", systemImage: "arrow.backward.square")
          }
        }
        items.replace(id: Dock.Buttons.ID.textLibrary) {
          Dock.Button(id: "my.package.dock.button.replacedTextLibrary") { context in
            print("Replaced Text action")
          } label: { context in
            Label("Replaced Text ", systemImage: "arrow.uturn.down.square")
          }
        }
        items.remove(id: Dock.Buttons.ID.shapesLibrary)
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
  DockEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-dock/DefaultDockItemsEditorSolution.swift reference-only
import IMGLYDesignEditor
import IMGLYPhotoEditor
import IMGLYVideoEditor
import SwiftUI

struct DefaultDockItemsEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var designEditor: some View {
    DesignEditor(settings)
      .imgly.dockItems { _ in
        Dock.Buttons.elementsLibrary()
        Dock.Buttons.photoRoll()
        Dock.Buttons.systemCamera()
        Dock.Buttons.imagesLibrary()
        Dock.Buttons.textLibrary()
        Dock.Buttons.shapesLibrary()
        Dock.Buttons.stickersLibrary()
        Dock.Buttons.resize()
      }
  }

  var photoEditor: some View {
    PhotoEditor(settings)
      .imgly.dockItems { _ in
        Dock.Buttons.adjustments()
        Dock.Buttons.filter()
        Dock.Buttons.effect()
        Dock.Buttons.blur()
        Dock.Buttons.crop()
        Dock.Buttons.textLibrary()
        Dock.Buttons.shapesLibrary()
        Dock.Buttons.stickersLibrary()
      }
  }

  var videoEditor: some View {
    VideoEditor(settings)
      .imgly.dockItems { _ in
        Dock.Buttons.photoRoll()
        Dock.Buttons.imglyCamera()
        Dock.Buttons.overlaysLibrary()
        Dock.Buttons.textLibrary()
        Dock.Buttons.stickersAndShapesLibrary()
        Dock.Buttons.audioLibrary()
        Dock.Buttons.voiceover()
        Dock.Buttons.reorder()
        Dock.Buttons.resize()
      }
  }

  private enum Solution: String, Identifiable, CaseIterable {
    case design, photo, video
    var id: Self { self }
  }

  @State private var solution: Solution = .design

  @State private var isPresented = false

  var body: some View {
    Picker("Solution", selection: $solution) {
      ForEach(Solution.allCases) {
        Text($0.rawValue.capitalized + " Editor")
      }
    }
    Button("Use the Editor") {
      isPresented = true
    }
    .fullScreenCover(isPresented: $isPresented) {
      ModalEditor {
        switch solution {
        case .design: designEditor
        case .photo: photoEditor
        case .video: videoEditor
        }
      }
    }
  }
}

#Preview {
  DefaultDockItemsEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-dock/DockItemEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct DockItemEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.dockItems { context in
        Dock.Buttons.elementsLibrary()

        Dock.Buttons.imagesLibrary(
          action: { context in
            context.eventHandler.send(.openSheet(type: .libraryAdd { context.assetLibrary.imagesTab }))
          },
          title: { context in Text("Image") },
          icon: { context in Image.imgly.addImage },
          isEnabled: { context in true },
          isVisible: { context in true },
        )

        Dock.Button(
          id: "my.package.dock.button.newButton",
        ) { context in
          print("New Button action")
        } label: { context in
          Label("New Button", systemImage: "star.circle")
        } isEnabled: { context in
          true
        } isVisible: { context in
          true
        }

        CustomDockItem()
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

private struct CustomDockItem: Dock.Item {
  var id: EditorComponentID { "my.package.dock.newCustomItem" }

  func body(_ context: Dock.Context) throws -> some View {
    ZStack {
      RoundedRectangle(cornerRadius: 10)
        .fill(.conicGradient(colors: [.red, .yellow, .green, .cyan, .blue, .purple, .red], center: .center))
      Text("New Custom Item")
        .padding(4)
    }
    .onTapGesture {
      print("New Custom Item action")
    }
  }

  func isVisible(_ context: Dock.Context) throws -> Bool {
    true
  }
}

#Preview {
  DockItemEditorSolution()
}
```

The dock provides quick access to content libraries and editing tools, appearing at the bottom of the editor interface. This guide shows you how to customize dock items and their layout to match your app's content strategy and user workflow. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/mac-catalyst/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-dock).

## Dock Architecture

![Dock](./assets/dock-ios.png)

The dock displays horizontally at the bottom of the editor and provides quick access to content libraries and editing tools. It adapts its content based on the selected editor solution.

**Key Components:**

- **`Dock.Item`** - Protocol that all dock items conform to
- **`Dock.Button`** - Pre-built button implementation with icon and title
- **`Dock.Context`** - Provides access to the engine, asset library, and event handler
- **Custom Items** - Create fully custom components by implementing `Dock.Item`

## Configuration

Dock customization uses SwiftUI modifiers in the `.imgly` namespace. You can configure the complete item list or modify the default items.

**Available modifiers:**

- **`dockItems`** - Define the complete list of dock items and their order. Items are only displayed when `isVisible(_:)` returns `true`.

- **`modifyDockItems`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration.

The `Dock.Context` provides access to the engine, asset library, and event handler. Use this for advanced customization logic and to maintain consistency with the current editor state.

### Default Dock Items

Each editor solution has its own default dock configuration optimized for its content workflow:

These are the default items recommended to be used with the Design Editor:

```swift highlight-designEditor-dockItems
.imgly.dockItems { _ in
  Dock.Buttons.elementsLibrary()
  Dock.Buttons.photoRoll()
  Dock.Buttons.systemCamera()
  Dock.Buttons.imagesLibrary()
  Dock.Buttons.textLibrary()
  Dock.Buttons.shapesLibrary()
  Dock.Buttons.stickersLibrary()
  Dock.Buttons.resize()
}
```

These are the default items recommended to be used with the Photo Editor:

```swift highlight-photoEditor-dockItems
.imgly.dockItems { _ in
  Dock.Buttons.adjustments()
  Dock.Buttons.filter()
  Dock.Buttons.effect()
  Dock.Buttons.blur()
  Dock.Buttons.crop()
  Dock.Buttons.textLibrary()
  Dock.Buttons.shapesLibrary()
  Dock.Buttons.stickersLibrary()
}
```

These are the default items recommended to be used with the Video Editor:

```swift highlight-videoEditor-dockItems
.imgly.dockItems { _ in
  Dock.Buttons.photoRoll()
  Dock.Buttons.imglyCamera()
  Dock.Buttons.overlaysLibrary()
  Dock.Buttons.textLibrary()
  Dock.Buttons.stickersAndShapesLibrary()
  Dock.Buttons.audioLibrary()
  Dock.Buttons.voiceover()
  Dock.Buttons.reorder()
  Dock.Buttons.resize()
}
```

Apparel Editor and
Postcard Editor don't have predefined dock
items by default, but you can customize them by providing your own dock
configuration using `.imgly.dockItems`. This will also enable the use of
`.imgly.modifyDockItems` for fine-tuning.

### Modify Dock Items

Use the `.imgly.modifyDockItems` modifier to adjust the default item list without rebuilding the entire configuration:

```swift highlight-modifyDockItemsSignature
.imgly.modifyDockItems { context, items in
```

Parameters:

- `context` - provides access to the engine, asset library, and event handler
- `items` - mutable array of dock items that can be modified

**Available modification operations:**

- `addFirst` - prepends new `Dock.Item`s:

```swift highlight-addFirst
items.addFirst {
  Dock.Button(id: "my.package.dock.button.first") { context in
    print("First Button action")
  } label: { context in
    Label("First Button", systemImage: "arrow.backward.circle")
  }
}
```

- `addLast` - appends new `Dock.Item`s:

```swift highlight-addLast
items.addLast {
  Dock.Button(id: "my.package.dock.button.last") { context in
    print("Last Button action")
  } label: { context in
    Label("Last Button", systemImage: "arrow.forward.circle")
  }
}
```

- `addAfter` - adds new `Dock.Item`s right after the item with the provided id:

```swift highlight-addAfter
items.addAfter(id: Dock.Buttons.ID.photoRoll) {
  Dock.Button(id: "my.package.dock.button.afterPhotoRoll") { context in
    print("After Photo Roll action")
  } label: { context in
    Label("After Photo Roll", systemImage: "arrow.forward.square")
  }
}
```

- `addBefore` - adds new `Dock.Item`s right before the item with the provided id:

```swift highlight-addBefore
items.addBefore(id: Dock.Buttons.ID.systemCamera) {
  Dock.Button(id: "my.package.dock.button.beforeSystemCamera") { context in
    print("Before Camera action")
  } label: { context in
    Label("Before Camera", systemImage: "arrow.backward.square")
  }
}
```

- `replace` - replaces the `Dock.Item` with the provided id with new `Dock.Item`s:

```swift highlight-replace
items.replace(id: Dock.Buttons.ID.textLibrary) {
  Dock.Button(id: "my.package.dock.button.replacedTextLibrary") { context in
    print("Replaced Text action")
  } label: { context in
    Label("Replaced Text ", systemImage: "arrow.uturn.down.square")
  }
}
```

- `remove` - removes the `Dock.Item` with the provided id:

```swift highlight-remove
items.remove(id: Dock.Buttons.ID.shapesLibrary)
```

> **Note:** **Warning** Note that the order of items may change between editor versions,
> therefore `.imgly.modifyDockItems` must be used with care. Consider
> overwriting the default items instead with `.imgly.dockItems` if you want to
> have strict ordering between different editor versions.

## Dock.Item Configuration

Each `Dock.Item` conforms to `EditorComponent`. Its `id` must be unique which is a requirement of the underlying SwiftUI [`ForEach`](https://developer.apple.com/documentation/swiftui/foreach) type.
Depending on your needs there are multiple ways to define an item. In this example, we demonstrate your options with increasing complexity.

### Use Predefined Buttons

The most basic option is to use our predefined buttons which are provided in the nested `Dock.Buttons.` namespace. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/dock-cb916c/#list-of-available-dockbuttons).

```swift highlight-predefinedButton
Dock.Buttons.elementsLibrary()
```

### Customize Predefined Buttons

All parameters of our predefined buttons are initialized with default values which allows you to change any of them if needed to finetune the button's behavior and style:

```swift highlight-customizePredefinedButton
Dock.Buttons.imagesLibrary(
  action: { context in
    context.eventHandler.send(.openSheet(type: .libraryAdd { context.assetLibrary.imagesTab }))
  },
  title: { context in Text("Image") },
  icon: { context in Image.imgly.addImage },
  isEnabled: { context in true },
  isVisible: { context in true },
)
```

**Available parameters:**

- `action` - the action to perform when the user triggers the button. In this example, the event handler is used to open a sheet with the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/) for adding an image.

- `title` - the title `View` that should be used to label the button. Don't encode the visibility in this view. Use `isVisible` instead. In this example, a `Text` view is used.

- `icon` - the icon `View` that should be used to label the button. Don't encode the visibility in this view. Use `isVisible` instead. You can use any custom icon or system image. We also provide icon images in the `Image.imgly` namespace for convenience.

- `isEnabled` - whether the button is enabled. In this example, true is always used.

- `isVisible` - whether the button should be visible. Prefer using this parameter to toggle the visibility instead of encoding it in the `title` and `icon` views. In this example, true is always used.

### Create New Buttons

If our predefined buttons don't fit your needs you can create your own:

```swift highlight-newButton
Dock.Button(
  id: "my.package.dock.button.newButton",
) { context in
  print("New Button action")
} label: { context in
  Label("New Button", systemImage: "star.circle")
} isEnabled: { context in
  true
} isVisible: { context in
  true
}
```

**Required and optional parameters:**

- `id` - the unique id of the button. This parameter is required.

- `action` - the action to perform when the user triggers the button. This parameter is required.

- `label` - a `View` that describes the purpose of the button's `action`. Don't encode the visibility in this view. Use `isVisible` instead. This parameter is required.

- `isEnabled` - whether the button is enabled. By default, true is always used.

- `isVisible` - whether the button should be visible. Prefer using this parameter to toggle the visibility instead of encoding it in the `label` view. By default, true is always used.

### Create New Custom Items

If you need something completely custom you can use arbitrary views as items.

Therefore, you need to conform your type to the `Dock.Item` protocol:

```swift highlight-newCustomItem-conformance
private struct CustomDockItem: Dock.Item {
  var id: EditorComponentID { "my.package.dock.newCustomItem" }

  func body(_ context: Dock.Context) throws -> some View {
    ZStack {
      RoundedRectangle(cornerRadius: 10)
        .fill(.conicGradient(colors: [.red, .yellow, .green, .cyan, .blue, .purple, .red], center: .center))
      Text("New Custom Item")
        .padding(4)
    }
    .onTapGesture {
      print("New Custom Item action")
    }
  }

  func isVisible(_ context: Dock.Context) throws -> Bool {
    true
  }
}
```

Then use it in your dock items:

```swift highlight-newCustomItem
CustomDockItem()
```

**Protocol requirements:**

- `var id: EditorComponentID { get }` - the unique id of the item. This property is required.

- `func body(_: Dock.Context) throws -> some View` - the body of your view. Don't encode the visibility in this view. Use `isVisible` instead. This property is required.

- `func isVisible(_: Dock.Context) throws -> Bool` - whether the item should be visible. Prefer using this parameter to toggle the visibility instead of encoding it in the `body` view. By default, true is always used.

### List of Available Dock.Buttons

All predefined buttons are available as static functions in the `Dock.Buttons` namespace. Each function returns a `Dock.Button` with default parameters that you can customize as shown in the [Customize Predefined Buttons](https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/dock-cb916c/#customize-predefined-buttons) section.

| Button                                  | ID                                         | Description                                                                                                                                                                             |
| --------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Dock.Buttons.elementsLibrary`          | `Dock.Buttons.ID.elementsLibrary`          | Opens library sheet with elements via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).            |
| `Dock.Buttons.overlaysLibrary`          | `Dock.Buttons.ID.overlaysLibrary`          | Opens library sheet with overlays via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).            |
| `Dock.Buttons.stickersAndShapesLibrary` | `Dock.Buttons.ID.stickersAndShapesLibrary` | Opens library sheet with stickers and shapes via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/). |
| `Dock.Buttons.imagesLibrary`            | `Dock.Buttons.ID.imagesLibrary`            | Opens library sheet with images via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).              |
| `Dock.Buttons.textLibrary`              | `Dock.Buttons.ID.textLibrary`              | Opens library sheet with text via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).                |
| `Dock.Buttons.shapesLibrary`            | `Dock.Buttons.ID.shapesLibrary`            | Opens library sheet with shapes via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).              |
| `Dock.Buttons.stickersLibrary`          | `Dock.Buttons.ID.stickersLibrary`          | Opens library sheet with stickers via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).            |
| `Dock.Buttons.audioLibrary`             | `Dock.Buttons.ID.audioLibrary`             | Opens library sheet with audio via editor event `.openSheet`. By default, the corresponding library is picked from the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/).               |
| `Dock.Buttons.systemPhotoRoll`          | `Dock.Buttons.ID.systemPhotoRoll`          | Opens the system photo roll via editor event `.addFromSystemPhotoRoll`.                                                                                                                 |
| `Dock.Buttons.imglyPhotoRoll`           | `Dock.Buttons.ID.imglyPhotoRoll`           | Opens the IMG.LY photo roll via editor event `.addFromIMGLYPhotoRoll`.                                                                                                                  |
| `Dock.Buttons.systemCamera`             | `Dock.Buttons.ID.systemCamera`             | Opens the system camera via editor event `.addFromSystemCamera`.                                                                                                                        |
| `Dock.Buttons.imglyCamera`              | `Dock.Buttons.ID.imglyCamera`              | Opens the IMG.LY camera via editor event `.addFromIMGLYCamera`.                                                                                                                         |
| `Dock.Buttons.voiceover`                | `Dock.Buttons.ID.voiceover`                | Opens voiceover sheet via editor event `.openSheet`.                                                                                                                                    |
| `Dock.Buttons.reorder`                  | `Dock.Buttons.ID.reorder`                  | Opens reorder sheet via editor event `.openSheet`.                                                                                                                                      |
| `Dock.Buttons.adjustments`              | `Dock.Buttons.ID.adjustments`              | Opens adjustment sheet via editor event `.openSheet`.                                                                                                                                   |
| `Dock.Buttons.filter`                   | `Dock.Buttons.ID.filter`                   | Opens filter sheet via editor event `.openSheet`.                                                                                                                                       |
| `Dock.Buttons.effect`                   | `Dock.Buttons.ID.effect`                   | Opens effect sheet via editor event `.openSheet`.                                                                                                                                       |
| `Dock.Buttons.blur`                     | `Dock.Buttons.ID.blur`                     | Opens blur sheet via editor event `.openSheet`.                                                                                                                                         |
| `Dock.Buttons.crop`                     | `Dock.Buttons.ID.crop`                     | Opens crop sheet via editor event `.openSheet`.                                                                                                                                         |
| `Dock.Buttons.resize`                   | `Dock.Buttons.ID.resize`                   | Opens resize sheet via editor event `.openSheet`.                                                                                                                                       |
| `Dock.Buttons.assetLibrary`             | `Dock.Buttons.ID.assetLibrary`             | Opens asset library sheet via editor event `.openSheet`.                                                                                                                                |



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
