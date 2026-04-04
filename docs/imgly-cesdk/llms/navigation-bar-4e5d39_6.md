# Source: https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/navigation-bar-4e5d39/

---
title: "Navigation Bar"
description: "Show, hide, or customize the editor’s top navigation bar to match your app layout."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/navigation-bar-4e5d39/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-navigation-bar/DefaultNavigationBarItemsEditorSolution.swift reference-only
import IMGLYApparelEditor
import IMGLYDesignEditor
import IMGLYPhotoEditor
import IMGLYPostcardEditor
import IMGLYVideoEditor
import SwiftUI

struct DefaultNavigationBarItemsEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var designEditor: some View {
    DesignEditor(settings)
      .imgly.navigationBarItems { _ in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.togglePagesMode()
          NavigationBar.Buttons.export()
        }
      }
  }

  var photoEditor: some View {
    PhotoEditor(settings)
      .imgly.navigationBarItems { _ in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.togglePreviewMode()
          NavigationBar.Buttons.export()
        }
      }
  }

  var videoEditor: some View {
    VideoEditor(settings)
      .imgly.navigationBarItems { _ in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.export()
        }
      }
  }

  var apparelEditor: some View {
    ApparelEditor(settings)
      .imgly.navigationBarItems { _ in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
        NavigationBar.ItemGroup(placement: .principal) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.togglePreviewMode()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.export()
        }
      }
  }

  var postcardEditor: some View {
    PostcardEditor(settings)
      .imgly.navigationBarItems { _ in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
          NavigationBar.Buttons.previousPage(
            label: { _ in NavigationLabel("Design", direction: .backward) },
          )
        }
        NavigationBar.ItemGroup(placement: .principal) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.togglePreviewMode()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.nextPage(
            label: { _ in NavigationLabel("Write", direction: .forward) },
          )
          NavigationBar.Buttons.export()
        }
      }
  }

  private enum Solution: String, Identifiable, CaseIterable {
    case design, photo, video, apparel, postcard
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
        case .apparel: apparelEditor
        case .postcard: postcardEditor
        }
      }
    }
  }
}

#Preview {
  DefaultNavigationBarItemsEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-navigation-bar/NavigationBarEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct NavigationBarEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.navigationBarItems { context in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
          NavigationBar.Buttons.togglePagesMode()
          NavigationBar.Buttons.export()
        }
      }
      .imgly.modifyNavigationBarItems { context, items in
        items.addFirst(placement: .topBarTrailing) {
          NavigationBar.Button(id: "my.package.inspectorBar.button.first") { context in
            print("First Button in top bar trailing placement group action")
          } label: { context in
            Label("First Button", systemImage: "arrow.backward.circle")
          }
        }
        items.addLast(placement: .topBarLeading) {
          NavigationBar.Button(id: "my.package.inspectorBar.button.last") { context in
            print("Last Button in top bar leading placement group action")
          } label: { context in
            Label("Last Button", systemImage: "arrow.forward.circle")
          }
        }
        items.addAfter(id: NavigationBar.Buttons.ID.undo) {
          NavigationBar.Button(id: "my.package.inspectorBar.button.afterUndo") { context in
            print("After Undo")
          } label: { context in
            Label("After Undo", systemImage: "arrow.forward.square")
          }
        }
        items.addBefore(id: NavigationBar.Buttons.ID.redo) {
          NavigationBar.Button(id: "my.package.inspectorBar.button.beforeRedo") { context in
            print("Before Redo")
          } label: { context in
            Label("Before Redo", systemImage: "arrow.backward.square")
          }
        }
        items.replace(id: NavigationBar.Buttons.ID.closeEditor) {
          NavigationBar.Buttons.closeEditor(
            label: { _ in Label("Cancel", systemImage: "xmark") },
          )
        }
        items.replace(id: NavigationBar.Buttons.ID.export) {
          NavigationBar.Buttons.export(
            label: { _ in Label("Done", systemImage: "checkmark") },
          )
        }
        items.remove(id: NavigationBar.Buttons.ID.togglePagesMode)
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
  NavigationBarEditorSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-navigation-bar/NavigationBarItemEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct NavigationBarItemEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.navigationBarItems { context in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }

        NavigationBar.ItemGroup(placement: .principal) {
          NavigationBar.Buttons.undo(
            action: { context in
              try context.engine?.editor.undo()
            },
            label: { context in
              Label { Text("Undo") } icon: { Image.imgly.undo }
                .opacity(context.state.viewMode == .preview ? 0 : 1)
                .labelStyle(.imgly.adaptiveIconOnly)
            },
            isEnabled: { context in
              try !context.state.isCreating &&
                context.state.viewMode != .preview &&
                context.engine?.editor.canUndo() == true
            },
            isVisible: { context in true },
          )

          NavigationBar.Button(
            id: "my.package.navigationBar.button.newButton",
          ) { context in
            print("New Button action")
          } label: { context in
            Label("New Button", systemImage: "star.circle")
          } isEnabled: { context in
            true
          } isVisible: { context in
            true
          }
        }

        NavigationBar.ItemGroup(placement: .topBarTrailing) {
          CustomNavigationBarItem()
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

private struct CustomNavigationBarItem: NavigationBar.Item {
  var id: EditorComponentID { "my.package.navigationBar.newCustomItem" }

  func body(_ context: NavigationBar.Context) throws -> some View {
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

  func isVisible(_ context: NavigationBar.Context) throws -> Bool {
    true
  }
}

#Preview {
  NavigationBarItemEditorSolution()
}
```

The navigation bar serves as the primary control interface at the top of the editor, housing essential functions like session management (close/save), editing operations (undo/redo), mode switching, and export capabilities. This guide shows you how to customize the navigation layout, button placement, and functionality to align with your app's information architecture and user flow patterns. While examples use the Design Editor, the same configuration principles apply to all [editor solutions](https://img.ly/docs/cesdk/mac-catalyst/prebuilt-solutions-d0ed07/).

Explore a complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-navigation-bar).

## Navigation Bar Architecture

![Navigation Bar on iOS](./assets/navigation-bar-ios.png)

The navigation bar displays horizontally at the top of the editor, organized into three placement areas: leading (left), principal (center), and trailing (right).

**Key Components:**

- **`NavigationBar.Item`** - Protocol that all navigation bar items conform to
- **`NavigationBar.Button`** - Pre-built button implementation with action and label
- **`NavigationBar.ItemGroup`** - Container that groups items by placement (leading, principal, trailing)
- **`NavigationBar.Context`** - Provides access to the engine, editor state, and event handler
- **Custom Items** - Create fully custom components by implementing `NavigationBar.Item`

## Configuration

Navigation bar customization uses SwiftUI modifiers in the `.imgly` namespace. Items are organized into placement groups similar to SwiftUI's `ToolbarItemGroup`.

**Available modifiers:**

- **`navigationBarItems`** - Define the complete list of navigation bar items grouped by placement. Items are only displayed when `isVisible(_:)` returns `true`.

- **`modifyNavigationBarItems`** - Modify the default item list by adding, replacing, or removing specific items without rebuilding the entire configuration.

The `NavigationBar.Context` provides access to the engine, editor state, asset library, and event handler for advanced customization logic.

### Default Navigation Bar Items

Each editor solution has its own default navigation bar configuration optimized for its workflow:

**Design Editor**:

```swift highlight-designEditor-navigationBarItems
.imgly.navigationBarItems { _ in
  NavigationBar.ItemGroup(placement: .topBarLeading) {
    NavigationBar.Buttons.closeEditor()
  }
  NavigationBar.ItemGroup(placement: .topBarTrailing) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
    NavigationBar.Buttons.togglePagesMode()
    NavigationBar.Buttons.export()
  }
}
```

**Photo Editor**:

```swift highlight-photoEditor-navigationBarItems
.imgly.navigationBarItems { _ in
  NavigationBar.ItemGroup(placement: .topBarLeading) {
    NavigationBar.Buttons.closeEditor()
  }
  NavigationBar.ItemGroup(placement: .topBarTrailing) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
    NavigationBar.Buttons.togglePreviewMode()
    NavigationBar.Buttons.export()
  }
}
```

**Video Editor**:

```swift highlight-videoEditor-navigationBarItems
.imgly.navigationBarItems { _ in
  NavigationBar.ItemGroup(placement: .topBarLeading) {
    NavigationBar.Buttons.closeEditor()
  }
  NavigationBar.ItemGroup(placement: .topBarTrailing) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
    NavigationBar.Buttons.export()
  }
}
```

**Apparel Editor**:

```swift highlight-apparelEditor-navigationBarItems
.imgly.navigationBarItems { _ in
  NavigationBar.ItemGroup(placement: .topBarLeading) {
    NavigationBar.Buttons.closeEditor()
  }
  NavigationBar.ItemGroup(placement: .principal) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
    NavigationBar.Buttons.togglePreviewMode()
  }
  NavigationBar.ItemGroup(placement: .topBarTrailing) {
    NavigationBar.Buttons.export()
  }
}
```

**Postcard Editor**:

```swift highlight-postcardEditor-navigationBarItems
.imgly.navigationBarItems { _ in
  NavigationBar.ItemGroup(placement: .topBarLeading) {
    NavigationBar.Buttons.closeEditor()
    NavigationBar.Buttons.previousPage(
      label: { _ in NavigationLabel("Design", direction: .backward) },
    )
  }
  NavigationBar.ItemGroup(placement: .principal) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
    NavigationBar.Buttons.togglePreviewMode()
  }
  NavigationBar.ItemGroup(placement: .topBarTrailing) {
    NavigationBar.Buttons.nextPage(
      label: { _ in NavigationLabel("Write", direction: .forward) },
    )
    NavigationBar.Buttons.export()
  }
}
```

### Modify Navigation Bar Items

Use the `.imgly.modifyNavigationBarItems` modifier to adjust the default item list without rebuilding the entire configuration:

```swift highlight-modifyNavigationBarItemsSignature
.imgly.modifyNavigationBarItems { context, items in
```

Parameters:

- `context` - provides access to the engine, editor state, and event handler
- `items` - mutable array of navigation bar item groups that can be modified

**Available modification operations:**

- `addFirst` - prepends new items at the beginning of a placement group:

```swift highlight-addFirst
items.addFirst(placement: .topBarTrailing) {
  NavigationBar.Button(id: "my.package.inspectorBar.button.first") { context in
    print("First Button in top bar trailing placement group action")
  } label: { context in
    Label("First Button", systemImage: "arrow.backward.circle")
  }
}
```

- `addLast` - appends new items at the end of a placement group:

```swift highlight-addLast
items.addLast(placement: .topBarLeading) {
  NavigationBar.Button(id: "my.package.inspectorBar.button.last") { context in
    print("Last Button in top bar leading placement group action")
  } label: { context in
    Label("Last Button", systemImage: "arrow.forward.circle")
  }
}
```

- `addAfter` - adds new items right after a specific item:

```swift highlight-addAfter
items.addAfter(id: NavigationBar.Buttons.ID.undo) {
  NavigationBar.Button(id: "my.package.inspectorBar.button.afterUndo") { context in
    print("After Undo")
  } label: { context in
    Label("After Undo", systemImage: "arrow.forward.square")
  }
}
```

- `addBefore` - adds new items right before a specific item:

```swift highlight-addBefore
items.addBefore(id: NavigationBar.Buttons.ID.redo) {
  NavigationBar.Button(id: "my.package.inspectorBar.button.beforeRedo") { context in
    print("Before Redo")
  } label: { context in
    Label("Before Redo", systemImage: "arrow.backward.square")
  }
}
```

- `replace` - replaces an existing item with new items:

```swift highlight-replace
items.replace(id: NavigationBar.Buttons.ID.closeEditor) {
  NavigationBar.Buttons.closeEditor(
    label: { _ in Label("Cancel", systemImage: "xmark") },
  )
}
items.replace(id: NavigationBar.Buttons.ID.export) {
  NavigationBar.Buttons.export(
    label: { _ in Label("Done", systemImage: "checkmark") },
  )
}
```

- `remove` - removes an existing item:

```swift highlight-remove
items.remove(id: NavigationBar.Buttons.ID.togglePagesMode)
```

> **Note:** **Warning**\
> Note that the order of items may change between editor versions, therefore `.imgly.modifyNavigationBarItems` must be used with care. Consider overwriting the default items instead with `.imgly.navigationBarItems` if you want to have strict ordering between different editor versions.

## NavigationBar.Item Configuration

Each `NavigationBar.Item` requires a unique `id` for SwiftUI's `ForEach` rendering. You have multiple options for creating navigation bar items, from simple predefined buttons to fully custom implementations. Items must be organized within `NavigationBar.ItemGroup` containers.

### Use Predefined Buttons

Start with predefined buttons from the `NavigationBar.Buttons` namespace. All available predefined buttons are listed below.

```swift highlight-predefinedButton
NavigationBar.Buttons.closeEditor()
```

### Customize Predefined Buttons

Customize any predefined button by overriding its default parameters:

```swift highlight-customizePredefinedButton
NavigationBar.Buttons.undo(
  action: { context in
    try context.engine?.editor.undo()
  },
  label: { context in
    Label { Text("Undo") } icon: { Image.imgly.undo }
      .opacity(context.state.viewMode == .preview ? 0 : 1)
      .labelStyle(.imgly.adaptiveIconOnly)
  },
  isEnabled: { context in
    try !context.state.isCreating &&
      context.state.viewMode != .preview &&
      context.engine?.editor.canUndo() == true
  },
  isVisible: { context in true },
)
```

**Available parameters:**

- `action` - the action to perform when the user triggers the button. Uses the engine to perform an undo step in this example.

- `label` - the view that describes the purpose of the button's action. Shows conditional opacity based on view mode in this example.

- `isEnabled` - whether the button is enabled. This example checks if undo is available and editor state.

- `isVisible` - whether the button should be visible. Can reserve layout space when hidden using the label view instead of this parameter.

### Create New Buttons

Create custom buttons when predefined options don't meet your needs:

```swift highlight-newButton
NavigationBar.Button(
  id: "my.package.navigationBar.button.newButton",
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

- `label` - a `View` that describes the purpose of the button's action. Don't encode visibility logic in this view. This parameter is required.

- `isEnabled` - whether the button is enabled. By default, true is always used.

- `isVisible` - whether the button should be visible. Can reserve layout space when hidden using the label view instead of this parameter. By default, true is always used.

### Create New Custom Items

For completely custom implementations, create a type conforming to the `NavigationBar.Item` protocol:

```swift highlight-newCustomItem-conformance
private struct CustomNavigationBarItem: NavigationBar.Item {
  var id: EditorComponentID { "my.package.navigationBar.newCustomItem" }

  func body(_ context: NavigationBar.Context) throws -> some View {
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

  func isVisible(_ context: NavigationBar.Context) throws -> Bool {
    true
  }
}
```

Then use it in your navigation bar items:

```swift highlight-newCustomItem
CustomNavigationBarItem()
```

**Protocol requirements:**

- `var id: EditorComponentID { get }` - the unique id of the item. This property is required.

- `func body(_: NavigationBar.Context) throws -> some View` - the body of your view. Don't encode visibility logic in this view unless layout space should be reserved when hidden. This property is required.

- `func isVisible(_: NavigationBar.Context) throws -> Bool` - whether the item should be visible. Prefer using this parameter for visibility logic unless layout space should be reserved when hidden. By default, true is always used.

### List of Available NavigationBar.Buttons

All predefined buttons are available as static functions in the `NavigationBar.Buttons` namespace. Each function returns a `NavigationBar.Button` with default parameters that you can customize as shown in the Customize Predefined Buttons section.

| Button                                    | ID                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NavigationBar.Buttons.closeEditor`       | `NavigationBar.Buttons.ID.closeEditor`       | Closes editor via editor event `.closeEditor`.                                                                                                                                                                                                                                                                                                                                                                                                |
| `NavigationBar.Buttons.undo`              | `NavigationBar.Buttons.ID.undo`              | Does undo operation in the editor via [EditorAPI.undo](https://img.ly/docs/cesdk/mac-catalyst/concepts/undo-and-history-99479d/) engine API.                                                                                                                                                                                                                                                                                                                                          |
| `NavigationBar.Buttons.redo`              | `NavigationBar.Buttons.ID.redo`              | Does redo operation in the editor via [EditorAPI.redo](https://img.ly/docs/cesdk/mac-catalyst/concepts/undo-and-history-99479d/) engine API.                                                                                                                                                                                                                                                                                                                                          |
| `NavigationBar.Buttons.export`            | `NavigationBar.Buttons.ID.export`            | Triggers [onExport](https://img.ly/docs/cesdk/mac-catalyst/user-interface/events-514b70/) callback via editor event `.startExport`.                                                                                                                                                                                                                                                                                                                                               |
| `NavigationBar.Buttons.togglePreviewMode` | `NavigationBar.Buttons.ID.togglePreviewMode` | Updates editor view mode via editor event `.setViewMode`: when current view mode is `EditorViewMode.edit`, then `EditorViewMode.preview` is set and vice versa. Note that this button is intended to be used in Photo Editor, Apparel Editor and Postcard Editor and may cause unexpected behaviors when used in other solutions. |
| `NavigationBar.Buttons.togglePagesMode`   | `NavigationBar.Buttons.ID.togglePagesMode`   | Updates editor view mode via editor event `.setViewMode`: when current view mode is `EditorViewMode.edit`, then `EditorViewMode.pages` is set and vice versa. Note that this button is intended to be used in Design Editor and may cause unexpected behaviors when used in other solutions.                                                                                                              |
| `NavigationBar.Buttons.previousPage`      | `NavigationBar.Buttons.ID.previousPage`      | Navigates to the previous page via editor event `.navigateToPreviousPage`.                                                                                                                                                                                                                                                                                                                                                                    |
| `NavigationBar.Buttons.nextPage`          | `NavigationBar.Buttons.ID.nextPage`          | Navigates to the next page via editor event `.navigateToNextPage`.                                                                                                                                                                                                                                                                                                                                                                            |



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
