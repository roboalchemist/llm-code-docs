# Source: https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/inspector-bar-8ca1cd/

---
title: "Inspector Bar"
description: "Customize the inspector bar for editing properties like position, color, and size."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/inspector-bar-8ca1cd/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-inspector-bar/InspectorBarEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct InspectorBarEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.inspectorBarItems { context in
        InspectorBar.Buttons.replace() // Video, Image, Sticker, Audio
        InspectorBar.Buttons.editText() // Text
        InspectorBar.Buttons.formatText() // Text
        InspectorBar.Buttons.fillStroke() // Page, Video, Image, Shape, Text
        InspectorBar.Buttons.textBackground() // Text
        InspectorBar.Buttons.editVoiceover() // Voiceover
        InspectorBar.Buttons.volume() // Video, Audio, Voiceover
        InspectorBar.Buttons.crop() // Video, Image
        InspectorBar.Buttons.adjustments() // Video, Image
        InspectorBar.Buttons.filter() // Video, Image
        InspectorBar.Buttons.effect() // Video, Image
        InspectorBar.Buttons.blur() // Video, Image
        InspectorBar.Buttons.shape() // Video, Image, Shape
        InspectorBar.Buttons.selectGroup() // Video, Image, Sticker, Shape, Text
        InspectorBar.Buttons.enterGroup() // Group
        InspectorBar.Buttons.layer() // Video, Image, Sticker, Shape, Text
        InspectorBar.Buttons.split() // Video, Image, Sticker, Shape, Text, Audio
        InspectorBar.Buttons.moveAsClip() // Video, Image, Sticker, Shape, Text
        InspectorBar.Buttons.moveAsOverlay() // Video, Image, Sticker, Shape, Text
        InspectorBar.Buttons.reorder() // Video, Image, Sticker, Shape, Text
        InspectorBar.Buttons.duplicate() // Video, Image, Sticker, Shape, Text, Audio
        InspectorBar.Buttons.delete() // Video, Image, Sticker, Shape, Text, Audio, Voiceover
      }
      .imgly.modifyInspectorBarItems { context, items in
        items.addFirst {
          InspectorBar.Button(id: "my.package.inspectorBar.button.first") { context in
            print("First Button action")
          } label: { context in
            Label("First Button", systemImage: "arrow.backward.circle")
          }
        }
        items.addLast {
          InspectorBar.Button(id: "my.package.inspectorBar.button.last") { context in
            print("Last Button action")
          } label: { context in
            Label("Last Button", systemImage: "arrow.forward.circle")
          }
        }
        items.addAfter(id: InspectorBar.Buttons.ID.layer) {
          InspectorBar.Button(id: "my.package.inspectorBar.button.afterLayer") { context in
            print("After Layer action")
          } label: { context in
            Label("After Layer", systemImage: "arrow.forward.square")
          }
        }
        items.addBefore(id: InspectorBar.Buttons.ID.crop) {
          InspectorBar.Button(id: "my.package.inspectorBar.button.beforeCrop") { context in
            print("Before Crop action")
          } label: { context in
            Label("Before Crop", systemImage: "arrow.backward.square")
          }
        }
        items.replace(id: InspectorBar.Buttons.ID.formatText) {
          InspectorBar.Button(id: "my.package.inspectorBar.button.replacedFormatText") { context in
            print("Replaced Format action")
          } label: { context in
            Label("Replaced Format", systemImage: "arrow.uturn.down.square")
          }
        }
        items.remove(id: InspectorBar.Buttons.ID.delete)
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
  InspectorBarEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-inspector-bar/InspectorBarItemEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct InspectorBarItemEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.inspectorBarItems { context in
        InspectorBar.Buttons.layer()

        InspectorBar.Buttons.formatText(
          action: { context in
            context.eventHandler.send(.openSheet(type: .formatText()))
          },
          title: { context in Text("Format") },
          icon: { context in Image.imgly.formatText },
          isEnabled: { context in true },
          isVisible: { context in
            try context.selection.type == .text &&
              context.engine.block.isAllowedByScope(context.selection.block, key: "text/character")
          },
        )

        InspectorBar.Button(
          id: "my.package.inspectorBar.button.newButton",
        ) { context in
          print("New Button action")
        } label: { context in
          Label("New Button", systemImage: "star.circle")
        } isEnabled: { context in
          true
        } isVisible: { context in
          true
        }

        CustomInspectorBarItem()
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

private struct CustomInspectorBarItem: InspectorBar.Item {
  var id: EditorComponentID { "my.package.inspectorBar.newCustomItem" }

  func body(_ context: InspectorBar.Context) throws -> some View {
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

  func isVisible(_ context: InspectorBar.Context) throws -> Bool {
    true
  }
}

#Preview {
  InspectorBarItemEditorSolution()
}
```

The inspector bar provides context-sensitive editing controls that appear when you select a design element, offering tools specific to that element type like text formatting, image adjustments, or shape properties. This guide shows you how to customize these editing controls to match your app's feature set and user experience goals. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/mac-catalyst/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-inspector-bar).

## Inspector Bar Architecture

![Inspector Bar](./assets/inspector-bar-ios.png)

The inspector bar displays horizontally at the bottom when a design element is selected. It contains context-sensitive editing tools that adapt based on the selected element type (text, image, video, etc.).

**Key Components:**

- **`InspectorBar.Item`** - Protocol that all inspector items conform to
- **`InspectorBar.Button`** - Pre-built button implementation with icon and title
- **`InspectorBar.Context`** - Provides access to the engine, asset library, and selected element
- **Custom Items** - Create fully custom components by implementing `InspectorBar.Item`

## Configuration

Inspector bar customization uses SwiftUI modifiers in the `.imgly` namespace. You can configure the complete item list or modify the default items.

**Available modifiers:**

- **`inspectorBarItems`** - Define the complete list of inspector bar items and their order. Items are only displayed when `isVisible(_:)` returns `true`.

- **`modifyInspectorBarItems`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration.

The `InspectorBar.Context` provides access to the engine, asset library, event handler, and currently selected element. Use the provided selection for logic instead of querying the engine directly, as it's optimized for UI presentation timing.

### Default Inspector Bar Items

The default configuration includes all essential editing tools for different element types:

```swift highlight-inspectorBarItems
.imgly.inspectorBarItems { context in
  InspectorBar.Buttons.replace() // Video, Image, Sticker, Audio
  InspectorBar.Buttons.editText() // Text
  InspectorBar.Buttons.formatText() // Text
  InspectorBar.Buttons.fillStroke() // Page, Video, Image, Shape, Text
  InspectorBar.Buttons.textBackground() // Text
  InspectorBar.Buttons.editVoiceover() // Voiceover
  InspectorBar.Buttons.volume() // Video, Audio, Voiceover
  InspectorBar.Buttons.crop() // Video, Image
  InspectorBar.Buttons.adjustments() // Video, Image
  InspectorBar.Buttons.filter() // Video, Image
  InspectorBar.Buttons.effect() // Video, Image
  InspectorBar.Buttons.blur() // Video, Image
  InspectorBar.Buttons.shape() // Video, Image, Shape
  InspectorBar.Buttons.selectGroup() // Video, Image, Sticker, Shape, Text
  InspectorBar.Buttons.enterGroup() // Group
  InspectorBar.Buttons.layer() // Video, Image, Sticker, Shape, Text
  InspectorBar.Buttons.split() // Video, Image, Sticker, Shape, Text, Audio
  InspectorBar.Buttons.moveAsClip() // Video, Image, Sticker, Shape, Text
  InspectorBar.Buttons.moveAsOverlay() // Video, Image, Sticker, Shape, Text
  InspectorBar.Buttons.reorder() // Video, Image, Sticker, Shape, Text
  InspectorBar.Buttons.duplicate() // Video, Image, Sticker, Shape, Text, Audio
  InspectorBar.Buttons.delete() // Video, Image, Sticker, Shape, Text, Audio, Voiceover
}
```

### Modify Inspector Bar Items

Use the `.imgly.modifyInspectorBarItems` modifier to adjust the default item list without rebuilding the entire configuration:

```swift highlight-modifyInspectorBarItemsSignature
.imgly.modifyInspectorBarItems { context, items in
```

Parameters:

- `context` - provides access to the engine, asset library, and selected element
- `items` - mutable array of inspector bar items that can be modified

**Available modification operations:**

- `addFirst` - prepends new items at the beginning:

```swift highlight-addFirst
items.addFirst {
  InspectorBar.Button(id: "my.package.inspectorBar.button.first") { context in
    print("First Button action")
  } label: { context in
    Label("First Button", systemImage: "arrow.backward.circle")
  }
}
```

- `addLast` - appends new items at the end:

```swift highlight-addLast
items.addLast {
  InspectorBar.Button(id: "my.package.inspectorBar.button.last") { context in
    print("Last Button action")
  } label: { context in
    Label("Last Button", systemImage: "arrow.forward.circle")
  }
}
```

- `addAfter` - adds new items right after a specific item:

```swift highlight-addAfter
items.addAfter(id: InspectorBar.Buttons.ID.layer) {
  InspectorBar.Button(id: "my.package.inspectorBar.button.afterLayer") { context in
    print("After Layer action")
  } label: { context in
    Label("After Layer", systemImage: "arrow.forward.square")
  }
}
```

- `addBefore` - adds new items right before a specific item:

```swift highlight-addBefore
items.addBefore(id: InspectorBar.Buttons.ID.crop) {
  InspectorBar.Button(id: "my.package.inspectorBar.button.beforeCrop") { context in
    print("Before Crop action")
  } label: { context in
    Label("Before Crop", systemImage: "arrow.backward.square")
  }
}
```

- `replace` - replaces an existing item with new items:

```swift highlight-replace
items.replace(id: InspectorBar.Buttons.ID.formatText) {
  InspectorBar.Button(id: "my.package.inspectorBar.button.replacedFormatText") { context in
    print("Replaced Format action")
  } label: { context in
    Label("Replaced Format", systemImage: "arrow.uturn.down.square")
  }
}
```

- `remove` - removes an existing item:

```swift highlight-remove
items.remove(id: InspectorBar.Buttons.ID.delete)
```

> **Note:** **Warning** Note that the order of items may change between editor versions,
> therefore `.imgly.modifyInspectorBarItems` must be used with care. Consider
> overwriting the default items instead with `.imgly.inspectorBarItems` if you
> want to have strict ordering between different editor versions.

## InspectorBar.Item Configuration

Each `InspectorBar.Item` requires a unique `id` for SwiftUI's `ForEach` rendering. You have multiple options for creating inspector bar items, from simple predefined buttons to fully custom implementations.

### Use Predefined Buttons

Start with predefined buttons from the `InspectorBar.Buttons` namespace. All [available predefined buttons are listed below](https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/inspector-bar-8ca1cd/#list-of-available-inspectorbarbuttons).

```swift highlight-predefinedButton
InspectorBar.Buttons.layer()
```

### Customize Predefined Buttons

Customize any predefined button by overriding its default parameters:

```swift highlight-customizePredefinedButton
InspectorBar.Buttons.formatText(
  action: { context in
    context.eventHandler.send(.openSheet(type: .formatText()))
  },
  title: { context in Text("Format") },
  icon: { context in Image.imgly.formatText },
  isEnabled: { context in true },
  isVisible: { context in
    try context.selection.type == .text &&
      context.engine.block.isAllowedByScope(context.selection.block, key: "text/character")
  },
)
```

**Available parameters:**

- `action` - the action to perform when the user triggers the button. Opens a format text sheet in this example.

- `title` - the title `View` that should be used to label the button. Don't encode visibility logic in this view.

- `icon` - the icon `View` that should be used to label the button. Don't encode visibility logic in this view. Use `isVisible` instead. You can use any custom icon or system image. We also provide icon images in the `Image.imgly` namespace for convenience.

- `isEnabled` - whether the button is enabled. Use context to determine state.

- `isVisible` - whether the button should be visible. This example shows visibility logic based on selection type and editing scope.

### Create New Buttons

Create custom buttons when predefined options don't meet your needs:

```swift highlight-newButton
InspectorBar.Button(
  id: "my.package.inspectorBar.button.newButton",
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

- `label` - a `View` that describes the purpose of the button's `action`. Don't encode visibility logic in this view. This parameter is required.

- `isEnabled` - whether the button is enabled. By default, true is always used.

- `isVisible` - whether the button should be visible. Prefer using this parameter for visibility logic. By default, true is always used.

### Create New Custom Items

For completely custom implementations, create a type conforming to the `InspectorBar.Item` protocol:

```swift highlight-newCustomItem-conformance
private struct CustomInspectorBarItem: InspectorBar.Item {
  var id: EditorComponentID { "my.package.inspectorBar.newCustomItem" }

  func body(_ context: InspectorBar.Context) throws -> some View {
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

  func isVisible(_ context: InspectorBar.Context) throws -> Bool {
    true
  }
}
```

Then use it in your inspector bar items:

```swift highlight-newCustomItem
CustomInspectorBarItem()
```

**Protocol requirements:**

- `var id: EditorComponentID { get }` - the unique id of the item. This property is required.

- `func body(_: InspectorBar.Context) throws -> some View` - the body of your view. Don't encode visibility logic in this view. This property is required.

- `func isVisible(_: InspectorBar.Context) throws -> Bool` - whether the item should be visible. Prefer using this parameter for visibility logic. By default, true is always used.

### List of Available InspectorBar.Buttons

All predefined buttons are available as static functions in the `InspectorBar.Buttons` namespace. Each function returns a `InspectorBar.Button` with default parameters that you can customize as shown in the [Customize Predefined Buttons](https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/inspector-bar-8ca1cd/#customize-predefined-buttons) section.

| Button                                | ID                                       | Description                                                                                                                                                                                                                                                                                                     | Renders For                                          |
| ------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `InspectorBar.Buttons.replace`        | `InspectorBar.Buttons.ID.replace`        | Opens a library sheet via editor event `.openSheet`. By default `DesignBlockType`, `FillType` and kind of the selected design block are used to find the library in the [Asset Library](https://img.ly/docs/cesdk/mac-catalyst/import-media/asset-panel/customize-c9a4de/). Selected asset will replace the content of the currently selected design block. | Video, Image, Sticker, Audio                         |
| `InspectorBar.Buttons.editText`       | `InspectorBar.Buttons.ID.editText`       | Enters text editing mode for the selected design block.                                                                                                                                                                                                                                                         | Text                                                 |
| `InspectorBar.Buttons.formatText`     | `InspectorBar.Buttons.ID.formatText`     | Opens format text sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                          | Text                                                 |
| `InspectorBar.Buttons.fillStroke`     | `InspectorBar.Buttons.ID.fillStroke`     | Opens fill & stroke sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                        | Page, Video, Image, Shape, Text                      |
| `InspectorBar.Buttons.textBackground` | `InspectorBar.Buttons.ID.textBackground` | Opens text background sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                      | Text                                                 |
| `InspectorBar.Buttons.editVoiceover`  | `InspectorBar.Buttons.ID.editVoiceover`  | Opens voiceover sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                            | Video, Audio, Voiceover                              |
| `InspectorBar.Buttons.volume`         | `InspectorBar.Buttons.ID.volume`         | Opens volume sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                               | Video, Audio, Voiceover                              |
| `InspectorBar.Buttons.crop`           | `InspectorBar.Buttons.ID.crop`           | Opens crop sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                                 | Video, Image                                         |
| `InspectorBar.Buttons.adjustments`    | `InspectorBar.Buttons.ID.adjustments`    | Opens adjustments sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                          | Video, Image                                         |
| `InspectorBar.Buttons.filter`         | `InspectorBar.Buttons.ID.filter`         | Opens filter sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                               | Video, Image                                         |
| `InspectorBar.Buttons.effect`         | `InspectorBar.Buttons.ID.effect`         | Opens effect sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                               | Video, Image                                         |
| `InspectorBar.Buttons.blur`           | `InspectorBar.Buttons.ID.blur`           | Opens blur sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                                 | Video, Image                                         |
| `InspectorBar.Buttons.shape`          | `InspectorBar.Buttons.ID.shape`          | Opens shape sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                                | Video, Image, Shape                                  |
| `InspectorBar.Buttons.selectGroup`    | `InspectorBar.Buttons.ID.selectGroup`    | Selects the group design block that contains the currently selected design block via editor event `.selectGroupForSelection`.                                                                                                                                                                                   | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Buttons.enterGroup`     | `InspectorBar.Buttons.ID.enterGroup`     | Changes selection from the selected group design block to a design block within that group via editor event `.enterGroupForSelection`.                                                                                                                                                                          | Group                                                |
| `InspectorBar.Buttons.layer`          | `InspectorBar.Buttons.ID.layer`          | Opens layer sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                                | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Buttons.split`          | `InspectorBar.Buttons.ID.split`          | Splits currently selected design block via editor event `.splitSelection` in a video scene.                                                                                                                                                                                                                     | Video, Image, Sticker, Shape, Text, Audio            |
| `InspectorBar.Buttons.moveAsClip`     | `InspectorBar.Buttons.ID.moveAsClip`     | Moves currently selected design block into the background track as clip via editor event `.moveSelectionAsClip`                                                                                                                                                                                                 | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Buttons.moveAsOverlay`  | `InspectorBar.Buttons.ID.moveAsOverlay`  | Moves currently selected design block from the background track to an overlay via editor event `.moveSelectionAsOverlay`                                                                                                                                                                                        | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Buttons.reorder`        | `InspectorBar.Buttons.ID.reorder`        | Opens reorder sheet via editor event `.openSheet`.                                                                                                                                                                                                                                                              | Video, Image, Sticker, Shape, Text                   |
| `InspectorBar.Buttons.duplicate`      | `InspectorBar.Buttons.ID.duplicate`      | Duplicates currently selected design block via editor event `.duplicateSelection`.                                                                                                                                                                                                                              | Video, Image, Sticker, Shape, Text, Audio            |
| `InspectorBar.Buttons.delete`         | `InspectorBar.Buttons.ID.delete`         | Deletes currently selected design block via editor event `.deleteSelection`.                                                                                                                                                                                                                                    | Video, Image, Sticker, Shape, Text, Audio, Voiceover |



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
